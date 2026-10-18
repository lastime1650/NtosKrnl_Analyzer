# BuildQueryDirectoryIrp

- RVA: `0x008EC770`–`0x008ECF70` (길이 `2,048` bytes)
- VA: `0x00000001408EC770`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00086C94`
- 디코드: `511`개 명령, `2,048/2,048` bytes 표시
- 미해석 바이트: `4` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008EC93F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EC959` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008EC9A1` → [ProbeForWrite](ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008ECA1D` → [ExRaiseAccessViolation](ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008ECA2D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ECAC1` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x008ECAD6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECB05` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008ECB78` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008ECBA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008ECBCB` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x008ECBD3` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008ECBF4` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008ECD11` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008ECD37` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECD3F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ECD52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECD66` → [IopAllocateIrpCleanup](../A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x008ECD75` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECDB0` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008ECDEA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ECDF9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECE17` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x008ECE33` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008ECE6C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ECE78` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECE92` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (function, `0x0040EC90`)
- `0x008ECEA8` → [IopAllocateIrpCleanup](../A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x008ECEB9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ECEE2` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)

### Direct callers
- [NtQueryDirectoryFileEx](NtQueryDirectoryFileEx_function_008EC680.md) at `0x008EC70F`
- [NtQueryDirectoryFile](NtQueryDirectoryFile_function_008ECF80.md) at `0x008ED02D`

### Static image references
- `0x008EC810` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008ECCE2` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x008ECF59` → RVA `0x0994D868` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x008EC93F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EC959` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008ECAC1` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x008ECAD6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECB05` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x008ECB78` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008ECBA3` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008ECBCB` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x008ECBD3` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008ECBF4` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008ECD37` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECD3F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ECD52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECD75` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECDEA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ECDF9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECE17` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x008ECE33` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008ECE6C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ECE78` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ECE92` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (`PAGE` → `.text`)
  - `0x008ECEB9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008ECC92` → [sub_00B1D822](../B1/Unknown_function_00B1D822.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008EC770  4C 8B DC                        mov r11, rsp
008EC773  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
008EC777  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
008EC77B  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
008EC77F  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
008EC783  53                              push rbx
008EC784  56                              push rsi
008EC785  57                              push rdi
008EC786  41 54                           push r12
008EC788  41 55                           push r13
008EC78A  41 56                           push r14
008EC78C  41 57                           push r15
008EC78E  48 83 EC 70                     sub rsp, 0x70
008EC792  48 8B FA                        mov rdi, rdx
008EC795  33 C9                           xor ecx, ecx
008EC797  49 89 4B 90                     mov qword ptr [r11 - 0x70], rcx
008EC79B  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
008EC7A0  49 89 4B A0                     mov qword ptr [r11 - 0x60], rcx
008EC7A4  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
008EC7AD  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
008EC7B2  45 0F B6 AA 32 02 00 00         movzx r13d, byte ptr [r10 + 0x232]
008EC7BA  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
008EC7BF  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
008EC7C7  44 88 28                        mov byte ptr [rax], r13b
008EC7CA  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
008EC7D4  45 84 ED                        test r13b, r13b
008EC7D7  0F 84 D0 00 00 00               je 0x1408ec8ad
008EC7DD  8B D1                           mov edx, ecx
008EC7DF  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
008EC7E3  49 8B 4B 28                     mov rcx, qword ptr [r11 + 0x28]
008EC7E7  48 3B CB                        cmp rcx, rbx
008EC7EA  48 0F 43 CB                     cmovae rcx, rbx
008EC7EE  8B 01                           mov eax, dword ptr [rcx]
008EC7F0  89 01                           mov dword ptr [rcx], eax
008EC7F2  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008EC7F9  83 F9 01                        cmp ecx, 1
008EC7FC  0F 84 21 02 00 00               je 0x1408eca23
008EC802  83 F9 03                        cmp ecx, 3
008EC805  0F 85 A0 01 00 00               jne 0x1408ec9ab
008EC80B  BA 60 00 00 00                  mov edx, 0x60
008EC810  4C 8D 05 E9 37 71 FF            lea r8, [rip - 0x8ec817]
008EC817  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
008EC81B  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
008EC822  3B C2                           cmp eax, edx
008EC824  0F 82 CE 01 00 00               jb 0x1408ec9f8
008EC82A  44 8B C8                        mov r9d, eax
008EC82D  49 8B 82 B8 00 00 00            mov rax, qword ptr [r10 + 0xb8]
008EC834  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
008EC83C  48 83 B8 10 03 00 00 00         cmp qword ptr [rax + 0x310], 0
008EC844  0F 85 4B 01 00 00               jne 0x1408ec995
008EC84A  48 63 C1                        movsxd rax, ecx
008EC84D  42 0F B6 8C 00 20 C8 B4 00      movzx ecx, byte ptr [rax + r8 + 0xb4c820]
008EC856  4D 85 C9                        test r9, r9
008EC859  0F 84 30 01 00 00               je 0x1408ec98f
008EC85F  49 8B C7                        mov rax, r15
008EC862  8D 51 FF                        lea edx, [rcx - 1]
008EC865  49 85 D7                        test r15, rdx
008EC868  0F 85 BF 01 00 00               jne 0x1408eca2d
008EC86E  49 8D 57 FF                     lea rdx, [r15 - 1]
008EC872  49 03 D1                        add rdx, r9
008EC875  4C 3B FA                        cmp r15, rdx
008EC878  0F 87 9F 01 00 00               ja 0x1408eca1d
008EC87E  48 3B D3                        cmp rdx, rbx
008EC881  0F 83 96 01 00 00               jae 0x1408eca1d
008EC887  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
008EC88E  48 81 C2 00 10 00 00            add rdx, 0x1000
008EC895  0F B6 08                        movzx ecx, byte ptr [rax]
008EC898  88 08                           mov byte ptr [rax], cl
008EC89A  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008EC8A0  48 05 00 10 00 00               add rax, 0x1000
008EC8A6  48 3B C2                        cmp rax, rdx
008EC8A9  75 EA                           jne 0x1408ec895
008EC8AB  EB 08                           jmp 0x1408ec8b5
008EC8AD  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
008EC8B5  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
008EC8BD  48 85 C0                        test rax, rax
008EC8C0  75 0A                           jne 0x1408ec8cc
008EC8C2  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008EC8C7  E9 FA 01 00 00                  jmp 0x1408ecac6
008EC8CC  45 84 ED                        test r13b, r13b
008EC8CF  0F 84 A3 00 00 00               je 0x1408ec978
008EC8D5  48 8B CB                        mov rcx, rbx
008EC8D8  48 3B C3                        cmp rax, rbx
008EC8DB  48 0F 42 C8                     cmovb rcx, rax
008EC8DF  90                              nop
008EC8E0  8B 01                           mov eax, dword ptr [rcx]
008EC8E2  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008EC8E6  4C 8B 61 08                     mov r12, qword ptr [rcx + 8]
008EC8EA  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
008EC8EF  F6 44 24 60 01                  test byte ptr [rsp + 0x60], 1
008EC8F4  0F 85 19 01 00 00               jne 0x1408eca13
008EC8FA  0F B7 74 24 60                  movzx esi, word ptr [rsp + 0x60]
008EC8FF  66 85 F6                        test si, si
008EC902  74 BE                           je 0x1408ec8c2
008EC904  45 84 ED                        test r13b, r13b
008EC907  74 24                           je 0x1408ec92d
008EC909  49 8D 0C 34                     lea rcx, [r12 + rsi]
008EC90D  48 3B CB                        cmp rcx, rbx
008EC910  0F 87 94 01 00 00               ja 0x1408ecaaa
008EC916  49 3B CC                        cmp rcx, r12
008EC919  0F 82 8B 01 00 00               jb 0x1408ecaaa
008EC91F  B8 00 02 00 00                  mov eax, 0x200
008EC924  66 3B F0                        cmp si, ax
008EC927  0F 83 8F 01 00 00               jae 0x1408ecabc
008EC92D  0F B7 FE                        movzx edi, si
008EC930  48 8D 57 10                     lea rdx, [rdi + 0x10]
008EC934  B9 61 00 00 00                  mov ecx, 0x61
008EC939  41 B8 49 6F 44 69               mov r8d, 0x69446f49
008EC93F  E8 AC 57 29 00                  call 0x140b820f0
008EC944  4C 8B F0                        mov r14, rax
008EC947  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008EC94C  48 8D 58 10                     lea rbx, [rax + 0x10]
008EC950  44 8B C7                        mov r8d, edi
008EC953  49 8B D4                        mov rdx, r12
008EC956  48 8B CB                        mov rcx, rbx
008EC959  E8 E2 9E DD FF                  call 0x1406c6840
008EC95E  66 41 89 36                     mov word ptr [r14], si
008EC962  66 41 89 76 02                  mov word ptr [r14 + 2], si
008EC967  49 89 5E 08                     mov qword ptr [r14 + 8], rbx
008EC96B  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
008EC973  E9 4E 01 00 00                  jmp 0x1408ecac6
008EC978  0F 10 00                        movups xmm0, xmmword ptr [rax]
008EC97B  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
008EC980  66 0F 73 D8 08                  psrldq xmm0, 8
008EC985  66 49 0F 7E C4                  movq r12, xmm0
008EC98A  E9 60 FF FF FF                  jmp 0x1408ec8ef
008EC98F  90                              nop
008EC990  E9 20 FF FF FF                  jmp 0x1408ec8b5
008EC995  41 B8 04 00 00 00               mov r8d, 4
008EC99B  49 8B D1                        mov rdx, r9
008EC99E  49 8B CF                        mov rcx, r15
008EC9A1  E8 1A C8 FF FF                  call 0x1408e91c0
008EC9A6  E9 0A FF FF FF                  jmp 0x1408ec8b5
008EC9AB  8D 41 FE                        lea eax, [rcx - 2]
008EC9AE  4C 8D 05 4B 36 71 FF            lea r8, [rip - 0x8ec9b5]
008EC9B5  83 F8 4F                        cmp eax, 0x4f
008EC9B8  77 2C                           ja 0x1408ec9e6
008EC9BA  48 98                           cdqe
008EC9BC  41 0F B6 84 00 20 CF 8E 00      movzx eax, byte ptr [r8 + rax + 0x8ecf20]
008EC9C5  41 8B 8C 80 F8 CE 8E 00         mov ecx, dword ptr [r8 + rax*4 + 0x8ecef8]
008EC9CD  49 03 C8                        add rcx, r8
008EC9D0  FF E1                           jmp rcx
008EC9D2  CC                              int3
008EC9D3  CC                              int3
008EC9D4  CC                              int3
008EC9D5  CC                              int3
008EC9D6  BA 80 00 00 00                  mov edx, 0x80
008EC9DB  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
008EC9DF  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008EC9E6  85 D2                           test edx, edx
008EC9E8  0F 85 2D FE FF FF               jne 0x1408ec81b
008EC9EE  B8 03 00 00 C0                  mov eax, 0xc0000003
008EC9F3  E9 D9 02 00 00                  jmp 0x1408eccd1
008EC9F8  B8 04 00 00 C0                  mov eax, 0xc0000004
008EC9FD  E9 CF 02 00 00                  jmp 0x1408eccd1
008ECA02  BA 48 00 00 00                  mov edx, 0x48
008ECA07  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA0E  E9 04 FE FF FF                  jmp 0x1408ec817
008ECA13  B8 0D 00 00 C0                  mov eax, 0xc000000d
008ECA18  E9 B4 02 00 00                  jmp 0x1408eccd1
008ECA1D  E8 1E C8 FF FF                  call 0x1408e9240
008ECA22  CC                              int3
008ECA23  BA 48 00 00 00                  mov edx, 0x48
008ECA28  E9 E3 FD FF FF                  jmp 0x1408ec810
008ECA2D  E8 9E D5 FA FF                  call 0x140899fd0
008ECA32  CC                              int3
008ECA33  BA 58 00 00 00                  mov edx, 0x58
008ECA38  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA3F  E9 D3 FD FF FF                  jmp 0x1408ec817
008ECA44  BA 70 00 00 00                  mov edx, 0x70
008ECA49  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA50  E9 C2 FD FF FF                  jmp 0x1408ec817
008ECA55  BA 10 00 00 00                  mov edx, 0x10
008ECA5A  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA61  E9 B1 FD FF FF                  jmp 0x1408ec817
008ECA66  BA 38 00 00 00                  mov edx, 0x38
008ECA6B  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA72  E9 A0 FD FF FF                  jmp 0x1408ec817
008ECA77  BA 60 00 00 00                  mov edx, 0x60
008ECA7C  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA83  E9 8F FD FF FF                  jmp 0x1408ec817
008ECA88  BA 78 00 00 00                  mov edx, 0x78
008ECA8D  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECA94  E9 7E FD FF FF                  jmp 0x1408ec817
008ECA99  BA 68 00 00 00                  mov edx, 0x68
008ECA9E  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
008ECAA5  E9 6D FD FF FF                  jmp 0x1408ec817
008ECAAA  0F B6 03                        movzx eax, byte ptr [rbx]
008ECAAD  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008ECAB2  0F B7 74 24 60                  movzx esi, word ptr [rsp + 0x60]
008ECAB7  E9 63 FE FF FF                  jmp 0x1408ec91f
008ECABC  B9 0D 00 00 C0                  mov ecx, 0xc000000d
008ECAC1  E8 8A 9F A0 FF                  call 0x1402f6a50
008ECAC6  EB 1A                           jmp 0x1408ecae2
008ECAC8  8B D8                           mov ebx, eax
008ECACA  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008ECACF  48 85 C9                        test rcx, rcx
008ECAD2  74 07                           je 0x1408ecadb
008ECAD4  33 D2                           xor edx, edx
008ECAD6  E8 95 5D 29 00                  call 0x140b82870
008ECADB  8B C3                           mov eax, ebx
008ECADD  E9 EF 01 00 00                  jmp 0x1408eccd1
008ECAE2  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
008ECAEB  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
008ECAF0  45 0F B6 C5                     movzx r8d, r13b
008ECAF4  41 BC 01 00 00 00               mov r12d, 1
008ECAFA  41 8B D4                        mov edx, r12d
008ECAFD  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008ECB05  E8 26 0A 9B FF                  call 0x14029d530
008ECB0A  8B D8                           mov ebx, eax
008ECB0C  85 C0                           test eax, eax
008ECB0E  0F 88 34 02 00 00               js 0x1408ecd48
008ECB14  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008ECB19  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
008ECB21  48 89 30                        mov qword ptr [rax], rsi
008ECB24  48 83 BE B0 00 00 00 00         cmp qword ptr [rsi + 0xb0], 0
008ECB2C  0F 85 A3 02 00 00               jne 0x1408ecdd5
008ECB32  48 85 FF                        test rdi, rdi
008ECB35  0F 85 A7 01 00 00               jne 0x1408ecce2
008ECB3B  48 8D 46 50                     lea rax, [rsi + 0x50]
008ECB3F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008ECB44  8B 38                           mov edi, dword ptr [rax]
008ECB46  40 F6 C7 02                     test dil, 2
008ECB4A  0F 84 6C 02 00 00               je 0x1408ecdbc
008ECB50  C1 EF 02                        shr edi, 2
008ECB53  41 22 FC                        and dil, r12b
008ECB56  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008ECB5F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008ECB66  90                              nop
008ECB67  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
008ECB6C  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
008ECB73  45 33 C0                        xor r8d, r8d
008ECB76  33 D2                           xor edx, edx
008ECB78  E8 B3 36 92 FF                  call 0x140210230
008ECB7D  C6 84 24 00 01 00 00 00         mov byte ptr [rsp + 0x100], 0
008ECB85  44 87 63 74                     xchg dword ptr [rbx + 0x74], r12d
008ECB89  45 85 E4                        test r12d, r12d
008ECB8C  0F 85 FE 01 00 00               jne 0x1408ecd90
008ECB92  48 85 C0                        test rax, rax
008ECB95  74 04                           je 0x1408ecb9b
008ECB97  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
008ECB9B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008ECBA0  48 8B CE                        mov rcx, rsi
008ECBA3  E8 78 2E 92 FF                  call 0x14020fa20
008ECBA8  33 DB                           xor ebx, ebx
008ECBAA  80 BC 24 00 01 00 00 00         cmp byte ptr [rsp + 0x100], 0
008ECBB2  0F 85 99 02 00 00               jne 0x1408ece51
008ECBB8  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008ECBC0  C6 03 01                        mov byte ptr [rbx], 1
008ECBC3  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008ECBC8  48 8B CE                        mov rcx, rsi
008ECBCB  E8 20 0A 9B FF                  call 0x14029d5f0
008ECBD0  48 8B CE                        mov rcx, rsi
008ECBD3  E8 48 E5 9A FF                  call 0x14029b120
008ECBD8  4C 8B E8                        mov r13, rax
008ECBDB  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
008ECBE3  48 89 01                        mov qword ptr [rcx], rax
008ECBE6  80 3B 00                        cmp byte ptr [rbx], 0
008ECBE9  41 0F 94 C0                     sete r8b
008ECBED  0F B6 50 4C                     movzx edx, byte ptr [rax + 0x4c]
008ECBF1  48 8B C8                        mov rcx, rax
008ECBF4  E8 27 AB 91 FF                  call 0x140207720
008ECBF9  48 8B D8                        mov rbx, rax
008ECBFC  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008ECC04  48 85 C0                        test rax, rax
008ECC07  0F 84 51 01 00 00               je 0x1408ecd5e
008ECC0D  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
008ECC15  48 89 18                        mov qword ptr [rax], rbx
008ECC18  48 89 B3 C0 00 00 00            mov qword ptr [rbx + 0xc0], rsi
008ECC1F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008ECC24  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
008ECC2B  44 0F B6 64 24 30               movzx r12d, byte ptr [rsp + 0x30]
008ECC31  44 88 63 40                     mov byte ptr [rbx + 0x40], r12b
008ECC35  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008ECC3A  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
008ECC3E  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008ECC46  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
008ECC4A  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
008ECC52  48 89 43 58                     mov qword ptr [rbx + 0x58], rax
008ECC56  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
008ECC5E  48 89 43 60                     mov qword ptr [rbx + 0x60], rax
008ECC62  48 8B BB B8 00 00 00            mov rdi, qword ptr [rbx + 0xb8]
008ECC69  66 C7 47 B8 0C 01               mov word ptr [rdi - 0x48], 0x10c
008ECC6F  48 89 77 E8                     mov qword ptr [rdi - 0x18], rsi
008ECC73  4C 89 B3 A0 00 00 00            mov qword ptr [rbx + 0xa0], r14
008ECC7A  33 C0                           xor eax, eax
008ECC7C  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
008ECC80  48 89 43 08                     mov qword ptr [rbx + 8], rax
008ECC84  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
008ECC88  A8 04                           test al, 4
008ECC8A  0F 85 91 01 00 00               jne 0x1408ece21
008ECC90  A8 10                           test al, 0x10
008ECC92  0F 85 8A 0B 23 00               jne 0x140b1d822
008ECC98  4C 89 7B 70                     mov qword ptr [rbx + 0x70], r15
008ECC9C  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
008ECCA3  89 47 C0                        mov dword ptr [rdi - 0x40], eax
008ECCA6  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
008ECCAD  89 47 D0                        mov dword ptr [rdi - 0x30], eax
008ECCB0  C7 47 D8 00 00 00 00            mov dword ptr [rdi - 0x28], 0
008ECCB7  4C 89 77 C8                     mov qword ptr [rdi - 0x38], r14
008ECCBB  0F B6 84 24 F0 00 00 00         movzx eax, byte ptr [rsp + 0xf0]
008ECCC3  24 1B                           and al, 0x1b
008ECCC5  88 47 BA                        mov byte ptr [rdi - 0x46], al
008ECCC8  81 4B 10 00 08 00 00            or dword ptr [rbx + 0x10], 0x800
008ECCCF  33 C0                           xor eax, eax
008ECCD1  48 83 C4 70                     add rsp, 0x70
008ECCD5  41 5F                           pop r15
008ECCD7  41 5E                           pop r14
008ECCD9  41 5D                           pop r13
008ECCDB  41 5C                           pop r12
008ECCDD  5F                              pop rdi
008ECCDE  5E                              pop rsi
008ECCDF  5B                              pop rbx
008ECCE0  C3                              ret
008ECCE1  CC                              int3
008ECCE2  4C 8B 05 97 9E 6D 00            mov r8, qword ptr [rip + 0x6d9e97]
008ECCE9  33 C0                           xor eax, eax
008ECCEB  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008ECCF3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008ECCF8  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
008ECD00  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008ECD05  45 0F B6 CD                     movzx r9d, r13b
008ECD09  BA 02 00 00 00                  mov edx, 2
008ECD0E  48 8B CF                        mov rcx, rdi
008ECD11  E8 9A C0 F7 FF                  call 0x140868db0
008ECD16  8B D8                           mov ebx, eax
008ECD18  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
008ECD20  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008ECD25  85 DB                           test ebx, ebx
008ECD27  0F 89 E7 00 00 00               jns 0x1408ece14
008ECD2D  4D 85 F6                        test r14, r14
008ECD30  74 0A                           je 0x1408ecd3c
008ECD32  33 D2                           xor edx, edx
008ECD34  49 8B CE                        mov rcx, r14
008ECD37  E8 34 5B 29 00                  call 0x140b82870
008ECD3C  48 8B CE                        mov rcx, rsi
008ECD3F  E8 0C C6 A0 FF                  call 0x1402f9350
008ECD44  8B C3                           mov eax, ebx
008ECD46  EB 89                           jmp 0x1408eccd1
008ECD48  4D 85 F6                        test r14, r14
008ECD4B  74 F7                           je 0x1408ecd44
008ECD4D  33 D2                           xor edx, edx
008ECD4F  49 8B CE                        mov rcx, r14
008ECD52  E8 19 5B 29 00                  call 0x140b82870
008ECD57  8B C3                           mov eax, ebx
008ECD59  E9 73 FF FF FF                  jmp 0x1408eccd1
008ECD5E  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
008ECD63  48 8B CE                        mov rcx, rsi
008ECD66  E8 69 15 13 00                  call 0x140a1e2d4
008ECD6B  4D 85 F6                        test r14, r14
008ECD6E  74 0A                           je 0x1408ecd7a
008ECD70  33 D2                           xor edx, edx
008ECD72  49 8B CE                        mov rcx, r14
008ECD75  E8 F6 5A 29 00                  call 0x140b82870
008ECD7A  B8 9A 00 00 C0                  mov eax, 0xc000009a
008ECD7F  48 83 C4 70                     add rsp, 0x70
008ECD83  41 5F                           pop r15
008ECD85  41 5E                           pop r14
008ECD87  41 5D                           pop r13
008ECD89  41 5C                           pop r12
008ECD8B  5F                              pop rdi
008ECD8C  5E                              pop rsi
008ECD8D  5B                              pop rbx
008ECD8E  C3                              ret
008ECD8F  CC                              int3
008ECD90  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
008ECD98  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008ECD9D  4C 8B C8                        mov r9, rax
008ECDA0  44 0F B6 C7                     movzx r8d, dil
008ECDA4  41 0F B6 D5                     movzx edx, r13b
008ECDA8  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008ECDAD  48 8B CE                        mov rcx, rsi
008ECDB0  E8 23 19 FC FF                  call 0x1408ae6d8
008ECDB5  8B D8                           mov ebx, eax
008ECDB7  E9 EE FD FF FF                  jmp 0x1408ecbaa
008ECDBC  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008ECDC4  C6 03 00                        mov byte ptr [rbx], 0
008ECDC7  45 84 ED                        test r13b, r13b
008ECDCA  0F 84 F8 FD FF FF               je 0x1408ecbc8
008ECDD0  E9 AA 00 00 00                  jmp 0x1408ece7f
008ECDD5  48 F7 84 24 C0 00 00 00 FE FF FF FF  test qword ptr [rsp + 0xc0], -2
008ECDE1  0F 84 4B FD FF FF               je 0x1408ecb32
008ECDE7  48 8B CE                        mov rcx, rsi
008ECDEA  E8 61 C5 A0 FF                  call 0x1402f9350
008ECDEF  4D 85 F6                        test r14, r14
008ECDF2  74 0A                           je 0x1408ecdfe
008ECDF4  33 D2                           xor edx, edx
008ECDF6  49 8B CE                        mov rcx, r14
008ECDF9  E8 72 5A 29 00                  call 0x140b82870
008ECDFE  B8 0D 00 00 C0                  mov eax, 0xc000000d
008ECE03  48 83 C4 70                     add rsp, 0x70
008ECE07  41 5F                           pop r15
008ECE09  41 5E                           pop r14
008ECE0B  41 5D                           pop r13
008ECE0D  41 5C                           pop r12
008ECE0F  5F                              pop rdi
008ECE10  5E                              pop rsi
008ECE11  5B                              pop rbx
008ECE12  C3                              ret
008ECE13  CC                              int3
008ECE14  48 8B C8                        mov rcx, rax
008ECE17  E8 34 B5 95 FF                  call 0x140248350
008ECE1C  E9 1A FD FF FF                  jmp 0x1408ecb3b
008ECE21  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
008ECE28  B9 41 00 00 00                  mov ecx, 0x41
008ECE2D  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008ECE33  E8 B8 52 29 00                  call 0x140b820f0
008ECE38  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
008ECE3C  48 85 C0                        test rax, rax
008ECE3F  0F 84 80 00 00 00               je 0x1408ecec5
008ECE45  C7 43 10 70 00 00 00            mov dword ptr [rbx + 0x10], 0x70
008ECE4C  E9 47 FE FF FF                  jmp 0x1408ecc98
008ECE51  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008ECE56  48 85 C9                        test rcx, rcx
008ECE59  75 1B                           jne 0x1408ece76
008ECE5B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008ECE60  48 85 C0                        test rax, rax
008ECE63  0F 84 D3 FE FF FF               je 0x1408ecd3c
008ECE69  48 8B C8                        mov rcx, rax
008ECE6C  E8 DF C4 A0 FF                  call 0x1402f9350
008ECE71  E9 C6 FE FF FF                  jmp 0x1408ecd3c
008ECE76  33 D2                           xor edx, edx
008ECE78  E8 F3 59 29 00                  call 0x140b82870
008ECE7D  EB DC                           jmp 0x1408ece5b
008ECE7F  45 33 C0                        xor r8d, r8d
008ECE82  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
008ECE8A  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
008ECE92  E8 F9 1D B2 FF                  call 0x14040ec90
008ECE97  E9 2C FD FF FF                  jmp 0x1408ecbc8
008ECE9C  8B D8                           mov ebx, eax
008ECE9E  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
008ECEA3  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
008ECEA8  E8 27 14 13 00                  call 0x140a1e2d4
008ECEAD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008ECEB2  48 85 C9                        test rcx, rcx
008ECEB5  74 07                           je 0x1408ecebe
008ECEB7  33 D2                           xor edx, edx
008ECEB9  E8 B2 59 29 00                  call 0x140b82870
008ECEBE  8B C3                           mov eax, ebx
008ECEC0  E9 0C FE FF FF                  jmp 0x1408eccd1
008ECEC5  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008ECECA  8B 00                           mov eax, dword ptr [rax]
008ECECC  D1 E8                           shr eax, 1
008ECECE  24 01                           and al, 1
008ECED0  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008ECED4  45 33 C9                        xor r9d, r9d
008ECED7  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
008ECEDC  48 8B D3                        mov rdx, rbx
008ECEDF  48 8B CE                        mov rcx, rsi
008ECEE2  E8 E1 16 FC FF                  call 0x1408ae5c8
008ECEE7  4D 85 F6                        test r14, r14
008ECEEA  0F 84 8A FE FF FF               je 0x1408ecd7a
008ECEF0  E9 7B FE FF FF                  jmp 0x1408ecd70
008ECEF5  0F 1F 00                        nop dword ptr [rax]
008ECEF8  02 CA                           add cl, dl
008ECEFA  8E 00                           mov es, word ptr [rax]
008ECEFC  55                              push rbp
008ECEFD  CA 8E 00                        retf 0x8e
008ECF00  66 CA 8E 00                     retf 0x8e
008ECF04  44 CA 8E 00                     retf 0x8e
008ECF08  33 CA                           xor ecx, edx
008ECF0A  8E 00                           mov es, word ptr [rax]
008ECF0C  77 CA                           ja 0x1408eced8
008ECF0E  8E 00                           mov es, word ptr [rax]
008ECF10  88 CA                           mov dl, cl
008ECF12  8E 00                           mov es, word ptr [rax]
008ECF14  99                              cdq
008ECF15  CA 8E 00                        retf 0x8e
008ECF18  D6                              .byte 0xd6
008ECF19  C9                              leave
008ECF1A  8E 00                           mov es, word ptr [rax]
008ECF1C  DF                              .byte 0xdf
008ECF1D  C9                              leave
008ECF1E  8E 00                           mov es, word ptr [rax]
008ECF20  00 09                           add byte ptr [rcx], cl
008ECF22  09 09                           or dword ptr [rcx], ecx
008ECF24  09 09                           or dword ptr [rcx], ecx
008ECF26  09 09                           or dword ptr [rcx], ecx
008ECF28  09 09                           or dword ptr [rcx], ecx
008ECF2A  01 09                           add dword ptr [rcx], ecx
008ECF2C  09 09                           or dword ptr [rcx], ecx
008ECF2E  09 09                           or dword ptr [rcx], ecx
008ECF30  09 09                           or dword ptr [rcx], ecx
008ECF32  09 09                           or dword ptr [rcx], ecx
008ECF34  09 09                           or dword ptr [rcx], ecx
008ECF36  09 09                           or dword ptr [rcx], ecx
008ECF38  09 09                           or dword ptr [rcx], ecx
008ECF3A  09 00                           or dword ptr [rax], eax
008ECF3C  09 09                           or dword ptr [rcx], ecx
008ECF3E  02 01                           add al, byte ptr [rcx]
008ECF40  09 09                           or dword ptr [rcx], ecx
008ECF42  09 03                           or dword ptr [rbx], eax
008ECF44  04 09                           add al, 9
008ECF46  09 09                           or dword ptr [rcx], ecx
008ECF48  09 09                           or dword ptr [rcx], ecx
008ECF4A  09 09                           or dword ptr [rcx], ecx
008ECF4C  09 09                           or dword ptr [rcx], ecx
008ECF4E  09 09                           or dword ptr [rcx], ecx
008ECF50  05 09 09 09 09                  add eax, 0x9090909
008ECF55  09 09                           or dword ptr [rcx], ecx
008ECF57  09 09                           or dword ptr [rcx], ecx
008ECF59  09 05 09 09 06 09               or dword ptr [rip + 0x9060909], eax
008ECF5F  09 09                           or dword ptr [rcx], ecx
008ECF61  09 09                           or dword ptr [rcx], ecx
008ECF63  09 09                           or dword ptr [rcx], ecx
008ECF65  09 09                           or dword ptr [rcx], ecx
008ECF67  09 09                           or dword ptr [rcx], ecx
008ECF69  09 09                           or dword ptr [rcx], ecx
008ECF6B  09 04 03                        or dword ptr [rbx + rax], eax
008ECF6E  07                              .byte 0x07
008ECF6F  08                              .byte 0x08
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BuildQueryDirectoryIrp(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p168;
    unsigned __int8 v_stack_p170;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pE0;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_m68 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m78 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    *(unsigned __int8 *)(a16) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EC8AD;
    v_stack_m74 = 0;
    a1 = *(unsigned __int64 *)(v_rsp + 40);
    if ((*(unsigned __int64 *)(v_rsp + 40)) >= v_rbx) { a1 = v_rbx; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (((unsigned int)((unsigned int)(a8))) == 1) goto loc_008ECA23;
    if (((unsigned int)((unsigned int)(a8))) != 3) goto loc_008EC9AB;
loc_008EC810:
loc_008EC817:
    v_stack_m74 = 96;
loc_008EC81B:
    if (((unsigned int)((unsigned int)(a7))) < 96) goto loc_008EC9F8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) != 0) goto loc_008EC995;
    if ((unsigned int)((unsigned int)((unsigned int)(a7))) == 0) goto loc_008EC98F;
    if (((a6) & (*(unsigned __int8 *)((int)((unsigned int)((unsigned int)(a8))) + v_rip - 9357335 * 1 + 11847712) - 1)) != 0) goto loc_008ECA2D;
    a2 = (a6 - 1) + ((unsigned int)((unsigned int)((unsigned int)(a7))));
    if (a6 > a2) goto loc_008ECA1D;
    if (a2 >= v_rbx) goto loc_008ECA1D;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_008EC895:
    *(unsigned __int8 *)(a6) = (unsigned __int8)(*(unsigned __int8 *)(a6));
    result = (a6) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != a2) goto loc_008EC895;
    goto loc_008EC8B5;
loc_008EC8AD:
loc_008EC8B5:
    if (a10 != 0) goto loc_008EC8CC;
loc_008EC8C2:
    goto loc_008ECAC6;
loc_008EC8CC:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EC978;
    a1 = v_rbx;
    if (a10 < v_rbx) { a1 = a10; }
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m40 = *(unsigned __int64 *)(a1 + 8);
loc_008EC8EF:
    if (((v_stack_m48) & (1)) != 0) goto loc_008ECA13;
    if ((unsigned __int16)(v_stack_m48) == 0) goto loc_008EC8C2;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EC92D;
    if ((*(unsigned __int64 *)(a1 + 8) + v_stack_m48 * 1) > v_rbx) goto loc_008ECAAA;
    if ((*(unsigned __int64 *)(a1 + 8) + v_stack_m48 * 1) < (*(unsigned __int64 *)(a1 + 8))) goto loc_008ECAAA;
loc_008EC91F:
    if (((unsigned __int16)(v_stack_m48)) >= 512) goto loc_008ECABC;
loc_008EC92D:
    result = ExAllocatePool2(97, (unsigned __int16)(v_stack_m48) + 16, (unsigned int)(0x69446F49ULL), (unsigned int)((unsigned int)((unsigned int)(a7))));
    v_stack_m60 = result;
    result = memcpy(result + 16, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned __int16)(v_stack_m48))), (unsigned int)((unsigned int)((unsigned int)(a7))));
    *(unsigned __int16 *)(result) = (unsigned __int16)(v_stack_m48);
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(v_stack_m48);
    *(unsigned __int64 *)(result + 8) = result + 16;
    goto loc_008ECAC6;
loc_008EC978:
    v_stack_m48 = v_xmm0;
    goto loc_008EC8EF;
loc_008EC98F:
    goto loc_008EC8B5;
loc_008EC995:
    result = ProbeForWrite(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), 4, (unsigned int)((unsigned int)((unsigned int)(a7))));
    goto loc_008EC8B5;
loc_008EC9AB:
    if (((unsigned int)(a6 - 2)) > 79) goto loc_008EC9E6;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9357749 + *(unsigned __int8 *)(v_rip - 9357749 + a6 - 2 * 1 + 9359136) * 4 + 9359096))) + (v_rip - 9357749);
loc_008EC9E6:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7)))) != 0) goto loc_008EC81B;
    goto loc_008ECCD1;
loc_008EC9F8:
    goto loc_008ECCD1;
loc_008ECA13:
    goto loc_008ECCD1;
loc_008ECA1D:
    result = ExRaiseAccessViolation(a1, (unsigned int)((unsigned int)((unsigned int)(a7))), v_rip - 9357749, (unsigned int)((unsigned int)((unsigned int)(a7))));
loc_008ECA23:
    goto loc_008EC810;
loc_008ECA2D:
    result = ExRaiseDatatypeMisalignment(a1, 72, v_rip - 9357749, (unsigned int)((unsigned int)((unsigned int)(a7))));
    goto loc_008EC817;
loc_008ECAAA:
    goto loc_008EC91F;
loc_008ECABC:
    result = RtlRaiseStatus((unsigned int)(0xC000000DULL), 88, v_rip - 9357749, (unsigned int)((unsigned int)((unsigned int)(a7))));
loc_008ECAC6:
    goto loc_008ECAE2;
loc_008ECAE2:
    v_stack_m88 = 0;
    result = IopReferenceFileObject(v_stack_p8, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m70);
    if (sign_flag) goto loc_008ECD48;
    *(unsigned __int64 *)(a15) = v_stack_m70;
    if ((*(unsigned __int64 *)(v_stack_m70 + 176)) != 0) goto loc_008ECDD5;
loc_008ECB32:
    if (v_stack_p10 != 0) goto loc_008ECCE2;
loc_008ECB3B:
    v_stack_m50 = v_stack_m70 + 80;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 80)))) & (2)) == 0) goto loc_008ECDBC;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70 + 80))) >> (2));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m70 + 128, a2, a3, v_stack_m70);
    v_stack_p58 = 0;
    if (1 != 0) goto loc_008ECD90;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m70, a2, a3, v_stack_m70);
    v_rbx = 0;
loc_008ECBAA:
    if (a11 != 0) goto loc_008ECE51;
    *(unsigned __int8 *)(a12) = 1;
loc_008ECBC8:
    result = IopResetEvent(v_stack_m70, a2, a3, v_stack_m70);
    result = IoGetRelatedDeviceObject(v_stack_m70, a2, a3, v_stack_m70);
    *(unsigned __int64 *)(a13) = result;
    a3 = ((*(unsigned __int8 *)(a12)) == 0) ? 1 : 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, v_stack_m70);
    v_stack_p80 = result;
    if (result == 0) goto loc_008ECD5E;
    *(unsigned __int64 *)(a14) = result;
    *(unsigned __int64 *)(result + 192) = v_stack_m70;
    *(unsigned __int64 *)(result + 152) = v_stack_m58;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m78);
    *(unsigned __int64 *)(result + 80) = v_stack_m68;
    *(unsigned __int64 *)(result + 72) = a5;
    *(unsigned __int64 *)(result + 88) = v_stack_p18;
    *(unsigned __int64 *)(result + 96) = v_stack_p20;
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 184) - 72) = 268;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_m70;
    *(unsigned __int64 *)(result + 160) = v_stack_m60;
    result = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (4)) != 0) goto loc_008ECE21;
loc_008ECC98:
    *(unsigned __int64 *)(result + 112) = a6;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 48) = (unsigned int)((unsigned int)(a8));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 40) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 56) = v_stack_m60;
    result = (unsigned __int8)((a9) & (27));
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = (unsigned __int8)(result);
    result = 0;
loc_008ECCD1:
    v_rsp = (v_rsp) + (112);
    return result;
loc_008ECCE2:
    result = 0;
    v_stack_p128 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = a16;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(result + 184), 2, *(unsigned __int64 *)(v_rip + 7184023), 0);
    v_stack_p40 = a16;
    if (!sign_flag) goto loc_008ECE14;
    result = a16;
    if (v_stack_m60 != 0) {
        a2 = 0;
        a1 = v_stack_m60;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 7184023), 0);
    }
    result = ObfDereferenceObject(v_stack_m70, a2, *(unsigned __int64 *)(v_rip + 7184023), 0);
loc_008ECD44:
    goto loc_008ECCD1;
loc_008ECD48:
    if (v_stack_m60 == 0) goto loc_008ECD44;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m60, a2, *(unsigned __int64 *)(v_rip + 7184023), 0);
    goto loc_008ECCD1;
loc_008ECD5E:
    result = IopAllocateIrpCleanup(v_stack_m70, v_stack_p40, *(unsigned __int64 *)(v_rip + 7184023), 0);
    if (v_stack_m60 != 0) {
        a2 = 0;
        a1 = v_stack_m60;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 7184023), 0);
    }
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC000009AULL);
loc_008ECD90:
    v_stack_pC8 = a11;
    result = IopWaitAndAcquireFileObjectLock(v_stack_pE0, (unsigned __int8)(result), (unsigned __int8)(*(unsigned __int64 *)(result + 184)), (unsigned int)(0xC000009AULL));
    goto loc_008ECBAA;
loc_008ECDBC:
    *(unsigned __int8 *)(a12) = 0;
    if ((unsigned __int8)(result) == 0) goto loc_008ECBC8;
    goto loc_008ECE7F;
loc_008ECDD5:
    if (((v_stack_p168) & (-2)) == 0) goto loc_008ECB32;
    result = ObfDereferenceObject(v_stack_pE0, (unsigned __int8)(result), (unsigned __int8)(*(unsigned __int64 *)(result + 184)), (unsigned int)(0xC000009AULL));
    if (v_stack_m60 != 0) {
        a2 = 0;
        a1 = v_stack_m60;
        result = ExFreePoolWithTag(a1, a2, (unsigned __int8)(*(unsigned __int64 *)(result + 184)), (unsigned int)(0xC000009AULL));
    }
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC000000DULL);
loc_008ECE14:
    result = KeResetEvent((unsigned int)(0xC000000DULL), a2, (unsigned __int8)(*(unsigned __int64 *)(result + 184)), (unsigned int)(0xC000009AULL));
    goto loc_008ECB3B;
loc_008ECE21:
    result = ExAllocatePool2(65, (unsigned int)(a7), (unsigned int)(0x42536F49ULL), (unsigned int)(0xC000009AULL));
    *(unsigned __int64 *)(a12 + 24) = result;
    if (result == 0) goto loc_008ECEC5;
    *(unsigned int *)(a12 + 16) = 112;
    goto loc_008ECC98;
loc_008ECE51:
    if (v_stack_p198 != 0) goto loc_008ECE76;
loc_008ECE5B:
    if (v_stack_p190 == 0) goto loc_008ECD3C;
    result = ObfDereferenceObject(v_stack_p190, (unsigned int)(a7), (unsigned int)(0x42536F49ULL), (unsigned int)(0xC000009AULL));
    goto loc_008ECD3C;
loc_008ECE76:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p190, a2, (unsigned int)(0x42536F49ULL), (unsigned int)(0xC000009AULL));
    goto loc_008ECE5B;
loc_008ECE7F:
    a3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(a5, v_stack_p210, a3, (unsigned int)(0xC000009AULL));
    goto loc_008ECBC8;
loc_008ECEC5:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p1A8))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_p170 = (unsigned __int8)(result);
    a4 = 0;
    result = IopExceptionCleanupEx(v_stack_pE0, a12, v_stack_p190, a4);
    if (v_stack_m60 == 0) goto loc_008ECD7A;
    goto loc_008ECD70;
}
```

## 5. (Beta) C Style

```c
int64_t BuildQueryDirectoryIrp(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, uint8_t Arg9, int64_t Arg10, uint8_t Arg11, void *Arg12, void *Arg13, void *Arg14, void *Arg15, void *Arg16)
{
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg13 = (uint8_t *)Arg13;
    uint8_t *arg14 = (uint8_t *)Arg14;
    uint8_t *arg15 = (uint8_t *)Arg15;
    uint8_t *arg16 = (uint8_t *)Arg16;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p128;
    uint64_t v_stack_p168;
    uint8_t v_stack_p170;
    uint64_t v_stack_p18;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p210;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint8_t v_stack_p58;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pE0;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_m68 = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m78 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    *(uint8_t *)(arg16) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EC8AD;
    v_stack_m74 = 0;
    Arg1 = *(uint64_t *)(local_rsp + 0x28);
    if ((*(uint64_t *)(local_rsp + 0x28)) >= local_rbx) { Arg1 = local_rbx; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (((uint32_t)((uint32_t)(Arg8))) == 1) goto loc_008ECA23;
    if (((uint32_t)((uint32_t)(Arg8))) != 3) goto loc_008EC9AB;
loc_008EC810:
loc_008EC817:
    v_stack_m74 = 96;
loc_008EC81B:
    if (((uint32_t)((uint32_t)(Arg7))) < 96) goto loc_008EC9F8;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) != 0) goto loc_008EC995;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg7))) == 0) goto loc_008EC98F;
    if (((Arg6) & (*(uint8_t *)((int32_t)((uint32_t)((uint32_t)(Arg8))) + v_rip - 0x8EC817 * 1 + 0xB4C820) - 1)) != 0) goto loc_008ECA2D;
    Arg2 = (Arg6 - 1) + ((uint32_t)((uint32_t)((uint32_t)(Arg7))));
    if (Arg6 > Arg2) goto loc_008ECA1D;
    if (Arg2 >= local_rbx) goto loc_008ECA1D;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_008EC895:
    *(uint8_t *)(Arg6) = (uint8_t)(*(uint8_t *)(Arg6));
    result = (Arg6) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != Arg2) goto loc_008EC895;
    goto loc_008EC8B5;
loc_008EC8AD:
loc_008EC8B5:
    if (Arg10 != 0) goto loc_008EC8CC;
loc_008EC8C2:
    goto loc_008ECAC6;
loc_008EC8CC:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EC978;
    Arg1 = local_rbx;
    if (Arg10 < local_rbx) { Arg1 = Arg10; }
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_m40 = *(uint64_t *)(Arg1 + 0x8);
loc_008EC8EF:
    if (((v_stack_m48) & (1)) != 0) goto loc_008ECA13;
    if ((uint16_t)(v_stack_m48) == 0) goto loc_008EC8C2;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EC92D;
    if ((*(uint64_t *)(Arg1 + 0x8) + v_stack_m48 * 1) > local_rbx) goto loc_008ECAAA;
    if ((*(uint64_t *)(Arg1 + 0x8) + v_stack_m48 * 1) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_008ECAAA;
loc_008EC91F:
    if (((uint16_t)(v_stack_m48)) >= 512) goto loc_008ECABC;
loc_008EC92D:
    result = ExAllocatePool2(97, (uint16_t)(v_stack_m48) + 16, (uint32_t)(0x69446F49ULL), (uint32_t)((uint32_t)((uint32_t)(Arg7))));
    v_stack_m60 = result;
    result = memcpy(result + 16, *(uint64_t *)(Arg1 + 0x8), (uint32_t)((uint32_t)((uint16_t)(v_stack_m48))), (uint32_t)((uint32_t)((uint32_t)(Arg7))));
    *(uint16_t *)(result) = (uint16_t)(v_stack_m48);
    *(uint16_t *)(result + 0x2) = (uint16_t)(v_stack_m48);
    *(uint64_t *)(result + 0x8) = result + 16;
    goto loc_008ECAC6;
loc_008EC978:
    v_stack_m48 = v_xmm0;
    goto loc_008EC8EF;
loc_008EC98F:
    goto loc_008EC8B5;
loc_008EC995:
    result = ProbeForWrite(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), 4, (uint32_t)((uint32_t)((uint32_t)(Arg7))));
    goto loc_008EC8B5;
loc_008EC9AB:
    if (((uint32_t)(Arg6 - 2)) > 79) goto loc_008EC9E6;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x8EC9B5 + *(uint8_t *)(v_rip - 0x8EC9B5 + Arg6 - 0x2 * 1 + 0x8ECF20) * 4 + 0x8ECEF8))) + (v_rip - 9357749);
loc_008EC9E6:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7)))) != 0) goto loc_008EC81B;
    goto loc_008ECCD1;
loc_008EC9F8:
    goto loc_008ECCD1;
loc_008ECA13:
    goto loc_008ECCD1;
loc_008ECA1D:
    result = ExRaiseAccessViolation(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg7))), v_rip - 9357749, (uint32_t)((uint32_t)((uint32_t)(Arg7))));
loc_008ECA23:
    goto loc_008EC810;
loc_008ECA2D:
    result = ExRaiseDatatypeMisalignment(Arg1, 72, v_rip - 9357749, (uint32_t)((uint32_t)((uint32_t)(Arg7))));
    goto loc_008EC817;
loc_008ECAAA:
    goto loc_008EC91F;
loc_008ECABC:
    result = RtlRaiseStatus((uint32_t)(0xC000000DULL), 88, v_rip - 9357749, (uint32_t)((uint32_t)((uint32_t)(Arg7))));
loc_008ECAC6:
    goto loc_008ECAE2;
loc_008ECAE2:
    v_stack_m88 = 0;
    result = IopReferenceFileObject(v_stack_p8, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m70);
    if (sign_flag) goto loc_008ECD48;
    *(uint64_t *)(arg15) = v_stack_m70;
    if ((*(uint64_t *)(v_stack_m70 + 0xB0)) != 0) goto loc_008ECDD5;
loc_008ECB32:
    if (v_stack_p10 != 0) goto loc_008ECCE2;
loc_008ECB3B:
    v_stack_m50 = v_stack_m70 + 80;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50)))) & (2)) == 0) goto loc_008ECDBC;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50))) >> (2));
    local_rdi = (uint8_t)((local_rdi) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m70 + 128, Arg2, Arg3, v_stack_m70);
    v_stack_p58 = 0;
    if (1 != 0) goto loc_008ECD90;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m70, Arg2, Arg3, v_stack_m70);
    local_rbx = 0;
loc_008ECBAA:
    if (Arg11 != 0) goto loc_008ECE51;
    *(uint8_t *)(arg12) = 1;
loc_008ECBC8:
    result = IopResetEvent(v_stack_m70, Arg2, Arg3, v_stack_m70);
    result = IoGetRelatedDeviceObject(v_stack_m70, Arg2, Arg3, v_stack_m70);
    *(uint64_t *)(arg13) = result;
    Arg3 = ((*(uint8_t *)(arg12)) == 0) ? 1 : 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, v_stack_m70);
    v_stack_p80 = result;
    if (result == 0) goto loc_008ECD5E;
    *(uint64_t *)(arg14) = result;
    *(uint64_t *)(result + 0xC0) = v_stack_m70;
    *(uint64_t *)(result + 0x98) = v_stack_m58;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m78);
    *(uint64_t *)(result + 0x50) = v_stack_m68;
    *(uint64_t *)(result + 0x48) = Arg5;
    *(uint64_t *)(result + 0x58) = v_stack_p18;
    *(uint64_t *)(result + 0x60) = v_stack_p20;
    *(uint16_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 268;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_m70;
    *(uint64_t *)(result + 0xA0) = v_stack_m60;
    result = 0;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (4)) != 0) goto loc_008ECE21;
loc_008ECC98:
    *(uint64_t *)(result + 0x70) = Arg6;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = (uint32_t)((uint32_t)(Arg8));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x28) = 0;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = v_stack_m60;
    result = (uint8_t)((Arg9) & (27));
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = (uint8_t)(result);
    result = 0;
loc_008ECCD1:
    local_rsp = (local_rsp) + (112);
    return result;
loc_008ECCE2:
    result = 0;
    v_stack_p128 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = Arg16;
    result = ObReferenceObjectByHandle(*(uint64_t *)(result + 0xB8), 2, *(uint64_t *)(v_rip + 0x6D9E97), 0);
    v_stack_p40 = Arg16;
    if (!sign_flag) goto loc_008ECE14;
    result = Arg16;
    if (v_stack_m60 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m60;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x6D9E97), 0);
    }
    result = ObfDereferenceObject(v_stack_m70, Arg2, *(uint64_t *)(v_rip + 0x6D9E97), 0);
loc_008ECD44:
    goto loc_008ECCD1;
loc_008ECD48:
    if (v_stack_m60 == 0) goto loc_008ECD44;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m60, Arg2, *(uint64_t *)(v_rip + 0x6D9E97), 0);
    goto loc_008ECCD1;
loc_008ECD5E:
    result = IopAllocateIrpCleanup(v_stack_m70, v_stack_p40, *(uint64_t *)(v_rip + 0x6D9E97), 0);
    if (v_stack_m60 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m60;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x6D9E97), 0);
    }
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC000009AULL);
loc_008ECD90:
    v_stack_pC8 = Arg11;
    result = IopWaitAndAcquireFileObjectLock(v_stack_pE0, (uint8_t)(result), (uint8_t)(*(uint64_t *)(result + 0xB8)), (uint32_t)(0xC000009AULL));
    goto loc_008ECBAA;
loc_008ECDBC:
    *(uint8_t *)(arg12) = 0;
    if ((uint8_t)(result) == 0) goto loc_008ECBC8;
    goto loc_008ECE7F;
loc_008ECDD5:
    if (((v_stack_p168) & (-2)) == 0) goto loc_008ECB32;
    result = ObfDereferenceObject(v_stack_pE0, (uint8_t)(result), (uint8_t)(*(uint64_t *)(result + 0xB8)), (uint32_t)(0xC000009AULL));
    if (v_stack_m60 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m60;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint8_t)(*(uint64_t *)(result + 0xB8)), (uint32_t)(0xC000009AULL));
    }
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC000000DULL);
loc_008ECE14:
    result = KeResetEvent((uint32_t)(0xC000000DULL), Arg2, (uint8_t)(*(uint64_t *)(result + 0xB8)), (uint32_t)(0xC000009AULL));
    goto loc_008ECB3B;
loc_008ECE21:
    result = ExAllocatePool2(65, (uint32_t)(Arg7), (uint32_t)(0x42536F49ULL), (uint32_t)(0xC000009AULL));
    *(uint64_t *)(arg12 + 0x18) = result;
    if (result == 0) goto loc_008ECEC5;
    *(uint32_t *)(arg12 + 0x10) = 112;
    goto loc_008ECC98;
loc_008ECE51:
    if (v_stack_p198 != 0) goto loc_008ECE76;
loc_008ECE5B:
    if (v_stack_p190 == 0) goto loc_008ECD3C;
    result = ObfDereferenceObject(v_stack_p190, (uint32_t)(Arg7), (uint32_t)(0x42536F49ULL), (uint32_t)(0xC000009AULL));
    goto loc_008ECD3C;
loc_008ECE76:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p190, Arg2, (uint32_t)(0x42536F49ULL), (uint32_t)(0xC000009AULL));
    goto loc_008ECE5B;
loc_008ECE7F:
    Arg3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(Arg5, v_stack_p210, Arg3, (uint32_t)(0xC000009AULL));
    goto loc_008ECBC8;
loc_008ECEC5:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p1A8))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_p170 = (uint8_t)(result);
    Arg4 = 0;
    result = IopExceptionCleanupEx(v_stack_pE0, Arg12, v_stack_p190, Arg4);
    if (v_stack_m60 == 0) goto loc_008ECD7A;
    goto loc_008ECD70;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg12` | `+ 0x0` | `8` | `R` |
| `Arg12` | `+ 0x0` | `8` | `W` |
| `Arg13` | `+ 0x0` | `64` | `W` |
| `Arg14` | `+ 0x0` | `64` | `W` |
| `Arg15` | `+ 0x0` | `64` | `W` |
| `Arg16` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EC770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
