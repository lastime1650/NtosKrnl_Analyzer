# NtQueryEaFile

- RVA: `0x008AC1B0`–`0x008AC8AE` (길이 `1,790` bytes)
- VA: `0x00000001408AC1B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F754`
- 디코드: `445`개 명령, `1,790/1,790` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008AC245` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008AC2C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AC2D9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008AC32E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC359` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC3B9` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008AC3D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC3FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC428` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC459` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC47A` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008AC4C9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008AC4F8` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008AC51A` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x008AC522` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008AC535` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008AC641` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x008AC669` → [IopSynchronousApiServiceTail](IopSynchronousApiServiceTail_function_008ACE3C.md) (function, `0x008ACE3C`)
- `0x008AC6A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AC6C5` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x008AC72D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AC758` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AC773` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008AC798` → [IopWaitAndAcquireFileObjectLock](IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008AC7BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AC7D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC7F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC817` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AC841` → [IopExceptionCleanupEx](IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008AC853` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC862` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC86F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008AC87C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x008AC2C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AC2D9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008AC32E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC359` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC3D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC3FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC428` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC459` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC47A` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x008AC4C9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008AC4F8` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008AC51A` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x008AC522` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008AC535` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008AC6A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AC6C5` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008AC72D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AC758` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AC773` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008AC7BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AC7D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC7F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC817` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AC853` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC862` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC86F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC87C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008AC5C6` → [sub_00B1A404](../B1/Unknown_function_00B1A404.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008AC1B0  48 8B C4                        mov rax, rsp
008AC1B3  48 89 58 08                     mov qword ptr [rax + 8], rbx
008AC1B7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008AC1BB  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
008AC1BF  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008AC1C3  57                              push rdi
008AC1C4  41 54                           push r12
008AC1C6  41 55                           push r13
008AC1C8  41 56                           push r14
008AC1CA  41 57                           push r15
008AC1CC  48 81 EC A0 00 00 00            sub rsp, 0xa0
008AC1D3  4D 8B D0                        mov r10, r8
008AC1D6  4C 8B F2                        mov r14, rdx
008AC1D9  4C 8B E9                        mov r13, rcx
008AC1DC  45 33 C0                        xor r8d, r8d
008AC1DF  4C 89 40 90                     mov qword ptr [rax - 0x70], r8
008AC1E3  45 8B E0                        mov r12d, r8d
008AC1E6  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
008AC1EB  4C 89 40 80                     mov qword ptr [rax - 0x80], r8
008AC1EF  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
008AC1F4  44 89 40 88                     mov dword ptr [rax - 0x78], r8d
008AC1F8  0F 57 C0                        xorps xmm0, xmm0
008AC1FB  0F 11 40 C0                     movups xmmword ptr [rax - 0x40], xmm0
008AC1FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AC208  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008AC20D  44 8A B8 32 02 00 00            mov r15b, byte ptr [rax + 0x232]
008AC214  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
008AC219  45 84 FF                        test r15b, r15b
008AC21C  0F 84 B0 04 00 00               je 0x1408ac6d2
008AC222  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
008AC22C  48 8B CB                        mov rcx, rbx
008AC22F  48 3B D3                        cmp rdx, rbx
008AC232  48 0F 42 CA                     cmovb rcx, rdx
008AC236  8B 01                           mov eax, dword ptr [rcx]
008AC238  89 01                           mov dword ptr [rcx], eax
008AC23A  41 8B D1                        mov edx, r9d
008AC23D  45 8D 44 24 04                  lea r8d, [r12 + 4]
008AC242  49 8B CA                        mov rcx, r10
008AC245  E8 76 CF 03 00                  call 0x1408e91c0
008AC24A  48 8B B4 24 08 01 00 00         mov rsi, qword ptr [rsp + 0x108]
008AC252  45 33 C0                        xor r8d, r8d
008AC255  48 85 F6                        test rsi, rsi
008AC258  0F 85 45 01 00 00               jne 0x1408ac3a3
008AC25E  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
008AC266  48 85 FF                        test rdi, rdi
008AC269  75 0A                           jne 0x1408ac275
008AC26B  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008AC270  E9 D4 01 00 00                  jmp 0x1408ac449
008AC275  44 39 84 24 00 01 00 00         cmp dword ptr [rsp + 0x100], r8d
008AC27D  74 EC                           je 0x1408ac26b
008AC27F  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
008AC284  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
008AC289  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008AC28E  40 F6 C7 03                     test dil, 3
008AC292  0F 85 21 01 00 00               jne 0x1408ac3b9
008AC298  8B B4 24 00 01 00 00            mov esi, dword ptr [rsp + 0x100]
008AC29F  48 8D 04 3E                     lea rax, [rsi + rdi]
008AC2A3  48 3B C3                        cmp rax, rbx
008AC2A6  0F 87 12 01 00 00               ja 0x1408ac3be
008AC2AC  48 3B C7                        cmp rax, rdi
008AC2AF  0F 82 09 01 00 00               jb 0x1408ac3be
008AC2B5  41 B8 49 6F 45 61               mov r8d, 0x61456f49
008AC2BB  48 8B D6                        mov rdx, rsi
008AC2BE  B9 61 00 00 00                  mov ecx, 0x61
008AC2C3  E8 28 5E 2D 00                  call 0x140b820f0
008AC2C8  48 8B D8                        mov rbx, rax
008AC2CB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008AC2D0  4C 8B C6                        mov r8, rsi
008AC2D3  48 8B D7                        mov rdx, rdi
008AC2D6  48 8B C8                        mov rcx, rax
008AC2D9  E8 62 A5 E1 FF                  call 0x1406c6840
008AC2DE  48 8B FB                        mov rdi, rbx
008AC2E1  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008AC2E6  8B 8C 24 00 01 00 00            mov ecx, dword ptr [rsp + 0x100]
008AC2ED  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
008AC2F1  45 33 C0                        xor r8d, r8d
008AC2F4  83 F9 05                        cmp ecx, 5
008AC2F7  7C 56                           jl 0x1408ac34f
008AC2F9  0F B6 47 04                     movzx eax, byte ptr [rdi + 4]
008AC2FD  83 C0 06                        add eax, 6
008AC300  3B C8                           cmp ecx, eax
008AC302  0F 82 BD 00 00 00               jb 0x1408ac3c5
008AC308  8B 17                           mov edx, dword ptr [rdi]
008AC30A  85 D2                           test edx, edx
008AC30C  75 6A                           jne 0x1408ac378
008AC30E  2B C8                           sub ecx, eax
008AC310  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
008AC314  78 0D                           js 0x1408ac323
008AC316  4D 8B E0                        mov r12, r8
008AC319  44 8A 7C 24 41                  mov r15b, byte ptr [rsp + 0x41]
008AC31E  E9 26 01 00 00                  jmp 0x1408ac449
008AC323  2B FB                           sub edi, ebx
008AC325  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008AC329  33 D2                           xor edx, edx
008AC32B  48 8B CB                        mov rcx, rbx
008AC32E  E8 3D 65 2D 00                  call 0x140b82870
008AC333  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008AC339  B9 14 00 00 80                  mov ecx, 0x80000014
008AC33E  41 89 0E                        mov dword ptr [r14], ecx
008AC341  48 63 C7                        movsxd rax, edi
008AC344  49 89 46 08                     mov qword ptr [r14 + 8], rax
008AC348  8B C1                           mov eax, ecx
008AC34A  E9 1F 03 00 00                  jmp 0x1408ac66e
008AC34F  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
008AC354  33 D2                           xor edx, edx
008AC356  48 8B CB                        mov rcx, rbx
008AC359  E8 12 65 2D 00                  call 0x140b82870
008AC35E  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008AC364  B9 14 00 00 80                  mov ecx, 0x80000014
008AC369  41 89 0E                        mov dword ptr [r14], ecx
008AC36C  49 83 66 08 00                  and qword ptr [r14 + 8], 0
008AC371  8B C1                           mov eax, ecx
008AC373  E9 F6 02 00 00                  jmp 0x1408ac66e
008AC378  83 C0 03                        add eax, 3
008AC37B  83 E0 FC                        and eax, 0xfffffffc
008AC37E  3B C2                           cmp eax, edx
008AC380  0F 85 97 00 00 00               jne 0x1408ac41d
008AC386  85 D2                           test edx, edx
008AC388  0F 88 8F 00 00 00               js 0x1408ac41d
008AC38E  2B CA                           sub ecx, edx
008AC390  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
008AC394  78 5B                           js 0x1408ac3f1
008AC396  48 03 FA                        add rdi, rdx
008AC399  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
008AC39E  E9 51 FF FF FF                  jmp 0x1408ac2f4
008AC3A3  48 8B C3                        mov rax, rbx
008AC3A6  48 3B F3                        cmp rsi, rbx
008AC3A9  48 0F 42 C6                     cmovb rax, rsi
008AC3AD  90                              nop
008AC3AE  8B 00                           mov eax, dword ptr [rax]
008AC3B0  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008AC3B4  E9 A5 FE FF FF                  jmp 0x1408ac25e
008AC3B9  E8 12 DC FE FF                  call 0x140899fd0
008AC3BE  8A 03                           mov al, byte ptr [rbx]
008AC3C0  E9 F0 FE FF FF                  jmp 0x1408ac2b5
008AC3C5  2B FB                           sub edi, ebx
008AC3C7  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008AC3CB  33 D2                           xor edx, edx
008AC3CD  48 8B CB                        mov rcx, rbx
008AC3D0  E8 9B 64 2D 00                  call 0x140b82870
008AC3D5  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008AC3DB  B9 14 00 00 80                  mov ecx, 0x80000014
008AC3E0  41 89 0E                        mov dword ptr [r14], ecx
008AC3E3  48 63 C7                        movsxd rax, edi
008AC3E6  49 89 46 08                     mov qword ptr [r14 + 8], rax
008AC3EA  8B C1                           mov eax, ecx
008AC3EC  E9 7D 02 00 00                  jmp 0x1408ac66e
008AC3F1  2B FB                           sub edi, ebx
008AC3F3  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008AC3F7  33 D2                           xor edx, edx
008AC3F9  48 8B CB                        mov rcx, rbx
008AC3FC  E8 6F 64 2D 00                  call 0x140b82870
008AC401  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008AC407  B9 14 00 00 80                  mov ecx, 0x80000014
008AC40C  41 89 0E                        mov dword ptr [r14], ecx
008AC40F  48 63 C7                        movsxd rax, edi
008AC412  49 89 46 08                     mov qword ptr [r14 + 8], rax
008AC416  8B C1                           mov eax, ecx
008AC418  E9 51 02 00 00                  jmp 0x1408ac66e
008AC41D  2B FB                           sub edi, ebx
008AC41F  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008AC423  33 D2                           xor edx, edx
008AC425  48 8B CB                        mov rcx, rbx
008AC428  E8 43 64 2D 00                  call 0x140b82870
008AC42D  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008AC433  B9 14 00 00 80                  mov ecx, 0x80000014
008AC438  41 89 0E                        mov dword ptr [r14], ecx
008AC43B  48 63 C7                        movsxd rax, edi
008AC43E  49 89 46 08                     mov qword ptr [r14 + 8], rax
008AC442  8B C1                           mov eax, ecx
008AC444  E9 25 02 00 00                  jmp 0x1408ac66e
008AC449  EB 1A                           jmp 0x1408ac465
008AC44B  8B D8                           mov ebx, eax
008AC44D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008AC452  48 85 C9                        test rcx, rcx
008AC455  74 07                           je 0x1408ac45e
008AC457  33 D2                           xor edx, edx
008AC459  E8 12 64 2D 00                  call 0x140b82870
008AC45E  8B C3                           mov eax, ebx
008AC460  E9 09 02 00 00                  jmp 0x1408ac66e
008AC465  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
008AC46A  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
008AC46F  45 8A C7                        mov r8b, r15b
008AC472  BA 08 00 00 00                  mov edx, 8
008AC477  49 8B CD                        mov rcx, r13
008AC47A  E8 B1 10 9F FF                  call 0x14029d530
008AC47F  8B F8                           mov edi, eax
008AC481  85 C0                           test eax, eax
008AC483  0F 88 03 02 00 00               js 0x1408ac68c
008AC489  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008AC48E  4C 8D 6E 50                     lea r13, [rsi + 0x50]
008AC492  41 8B 7D 00                     mov edi, dword ptr [r13]
008AC496  40 F6 C7 02                     test dil, 2
008AC49A  0F 84 FB 01 00 00               je 0x1408ac69b
008AC4A0  C1 EF 02                        shr edi, 2
008AC4A3  40 80 E7 01                     and dil, 1
008AC4A7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AC4B0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008AC4B7  90                              nop
008AC4B8  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008AC4BD  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
008AC4C4  45 33 C0                        xor r8d, r8d
008AC4C7  33 D2                           xor edx, edx
008AC4C9  E8 62 3D 96 FF                  call 0x140210230
008AC4CE  4C 8B C8                        mov r9, rax
008AC4D1  C6 44 24 42 00                  mov byte ptr [rsp + 0x42], 0
008AC4D6  B8 01 00 00 00                  mov eax, 1
008AC4DB  87 43 74                        xchg dword ptr [rbx + 0x74], eax
008AC4DE  85 C0                           test eax, eax
008AC4E0  0F 85 9A 02 00 00               jne 0x1408ac780
008AC4E6  4D 85 C9                        test r9, r9
008AC4E9  74 05                           je 0x1408ac4f0
008AC4EB  41 C6 41 0A 01                  mov byte ptr [r9 + 0xa], 1
008AC4F0  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008AC4F5  48 8B CE                        mov rcx, rsi
008AC4F8  E8 23 35 96 FF                  call 0x14020fa20
008AC4FD  33 DB                           xor ebx, ebx
008AC4FF  80 7C 24 42 00                  cmp byte ptr [rsp + 0x42], 0
008AC504  0F 85 D5 02 00 00               jne 0x1408ac7df
008AC50A  41 B7 01                        mov r15b, 1
008AC50D  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008AC512  44 88 7C 24 42                  mov byte ptr [rsp + 0x42], r15b
008AC517  48 8B CE                        mov rcx, rsi
008AC51A  E8 D1 10 9F FF                  call 0x14029d5f0
008AC51F  48 8B CE                        mov rcx, rsi
008AC522  E8 F9 EB 9E FF                  call 0x14029b120
008AC527  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008AC52C  45 33 C0                        xor r8d, r8d
008AC52F  8A 50 4C                        mov dl, byte ptr [rax + 0x4c]
008AC532  48 8B C8                        mov rcx, rax
008AC535  E8 E6 B1 95 FF                  call 0x140207720
008AC53A  48 8B F8                        mov rdi, rax
008AC53D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008AC545  33 D2                           xor edx, edx
008AC547  48 85 C0                        test rax, rax
008AC54A  0F 84 54 02 00 00               je 0x1408ac7a4
008AC550  48 89 B0 C0 00 00 00            mov qword ptr [rax + 0xc0], rsi
008AC557  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008AC55C  48 89 87 98 00 00 00            mov qword ptr [rdi + 0x98], rax
008AC563  8A 44 24 41                     mov al, byte ptr [rsp + 0x41]
008AC567  88 47 40                        mov byte ptr [rdi + 0x40], al
008AC56A  4C 8D 67 10                     lea r12, [rdi + 0x10]
008AC56E  45 84 FF                        test r15b, r15b
008AC571  0F 84 89 01 00 00               je 0x1408ac700
008AC577  49 8B C6                        mov rax, r14
008AC57A  8B CA                           mov ecx, edx
008AC57C  48 89 4F 50                     mov qword ptr [rdi + 0x50], rcx
008AC580  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
008AC584  48 89 57 58                     mov qword ptr [rdi + 0x58], rdx
008AC588  4C 8B BF B8 00 00 00            mov r15, qword ptr [rdi + 0xb8]
008AC58F  41 C6 47 B8 07                  mov byte ptr [r15 - 0x48], 7
008AC594  49 89 77 E8                     mov qword ptr [r15 - 0x18], rsi
008AC598  38 54 24 40                     cmp byte ptr [rsp + 0x40], dl
008AC59C  74 16                           je 0x1408ac5b4
008AC59E  48 89 9F A0 00 00 00            mov qword ptr [rdi + 0xa0], rbx
008AC5A5  49 89 5F C8                     mov qword ptr [r15 - 0x38], rbx
008AC5A9  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
008AC5B0  41 89 47 D0                     mov dword ptr [r15 - 0x30], eax
008AC5B4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AC5B9  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
008AC5BC  A8 04                           test al, 4
008AC5BE  0F 85 37 02 00 00               jne 0x1408ac7fb
008AC5C4  A8 10                           test al, 0x10
008AC5C6  0F 85 38 DE 26 00               jne 0x140b1a404
008AC5CC  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008AC5D4  48 89 47 70                     mov qword ptr [rdi + 0x70], rax
008AC5D8  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
008AC5DF  44 8A 64 24 41                  mov r12b, byte ptr [rsp + 0x41]
008AC5E4  41 89 47 C0                     mov dword ptr [r15 - 0x40], eax
008AC5E8  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
008AC5EC  41 89 47 D8                     mov dword ptr [r15 - 0x28], eax
008AC5F0  41 88 57 BA                     mov byte ptr [r15 - 0x46], dl
008AC5F4  8A C2                           mov al, dl
008AC5F6  38 94 24 10 01 00 00            cmp byte ptr [rsp + 0x110], dl
008AC5FD  74 07                           je 0x1408ac606
008AC5FF  41 C6 47 BA 01                  mov byte ptr [r15 - 0x46], 1
008AC604  B0 01                           mov al, 1
008AC606  38 94 24 F0 00 00 00            cmp byte ptr [rsp + 0xf0], dl
008AC60D  74 06                           je 0x1408ac615
008AC60F  0C 02                           or al, 2
008AC611  41 88 47 BA                     mov byte ptr [r15 - 0x46], al
008AC615  48 39 94 24 08 01 00 00         cmp qword ptr [rsp + 0x108], rdx
008AC61D  0F 85 80 02 00 00               jne 0x1408ac8a3
008AC623  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
008AC62B  8A 5C 24 42                     mov bl, byte ptr [rsp + 0x42]
008AC62F  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
008AC633  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
008AC638  45 33 C9                        xor r9d, r9d
008AC63B  4C 8B C6                        mov r8, rsi
008AC63E  48 8B D7                        mov rdx, rdi
008AC641  E8 FA ED 03 00                  call 0x1408eb440
008AC646  84 DB                           test bl, bl
008AC648  75 24                           jne 0x1408ac66e
008AC64A  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008AC64F  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
008AC657  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008AC65C  45 8A CC                        mov r9b, r12b
008AC65F  4C 8B C7                        mov r8, rdi
008AC662  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008AC667  8B C8                           mov ecx, eax
008AC669  E8 CE 07 00 00                  call 0x1408ace3c
008AC66E  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
008AC676  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008AC67A  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
008AC67E  49 8B E3                        mov rsp, r11
008AC681  41 5F                           pop r15
008AC683  41 5E                           pop r14
008AC685  41 5D                           pop r13
008AC687  41 5C                           pop r12
008AC689  5F                              pop rdi
008AC68A  C3                              ret
008AC68B  CC                              int3
008AC68C  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008AC691  0F 85 B7 01 00 00               jne 0x1408ac84e
008AC697  8B C7                           mov eax, edi
008AC699  EB D3                           jmp 0x1408ac66e
008AC69B  BA 18 00 00 00                  mov edx, 0x18
008AC6A0  8D 4A 28                        lea ecx, [rdx + 0x28]
008AC6A3  41 B8 49 6F 45 76               mov r8d, 0x76456f49
008AC6A9  E8 42 5A 2D 00                  call 0x140b820f0
008AC6AE  4C 8B E0                        mov r12, rax
008AC6B1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008AC6B6  48 85 C0                        test rax, rax
008AC6B9  74 5F                           je 0x1408ac71a
008AC6BB  45 33 C0                        xor r8d, r8d
008AC6BE  41 8D 50 01                     lea edx, [r8 + 1]
008AC6C2  48 8B C8                        mov rcx, rax
008AC6C5  E8 46 16 B6 FF                  call 0x14040dd10
008AC6CA  45 32 FF                        xor r15b, r15b
008AC6CD  E9 40 FE FF FF                  jmp 0x1408ac512
008AC6D2  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
008AC6DA  48 85 FF                        test rdi, rdi
008AC6DD  75 5A                           jne 0x1408ac739
008AC6DF  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008AC6E4  48 8B B4 24 08 01 00 00         mov rsi, qword ptr [rsp + 0x108]
008AC6EC  48 85 F6                        test rsi, rsi
008AC6EF  0F 84 70 FD FF FF               je 0x1408ac465
008AC6F5  8B 06                           mov eax, dword ptr [rsi]
008AC6F7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008AC6FB  E9 65 FD FF FF                  jmp 0x1408ac465
008AC700  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
008AC708  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
008AC710  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008AC715  E9 62 FE FF FF                  jmp 0x1408ac57c
008AC71A  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008AC71F  0F 85 38 01 00 00               jne 0x1408ac85d
008AC725  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008AC72A  48 8B CE                        mov rcx, rsi
008AC72D  E8 1E CC A4 FF                  call 0x1402f9350
008AC732  8B C3                           mov eax, ebx
008AC734  E9 35 FF FF FF                  jmp 0x1408ac66e
008AC739  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
008AC740  85 C0                           test eax, eax
008AC742  74 9B                           je 0x1408ac6df
008AC744  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008AC749  8B F0                           mov esi, eax
008AC74B  41 B8 49 6F 45 61               mov r8d, 0x61456f49
008AC751  8B D0                           mov edx, eax
008AC753  B9 41 00 00 00                  mov ecx, 0x41
008AC758  E8 93 59 2D 00                  call 0x140b820f0
008AC75D  48 8B D8                        mov rbx, rax
008AC760  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008AC765  48 85 C0                        test rax, rax
008AC768  74 6B                           je 0x1408ac7d5
008AC76A  44 8B C6                        mov r8d, esi
008AC76D  48 8B D7                        mov rdx, rdi
008AC770  48 8B C8                        mov rcx, rax
008AC773  E8 C8 A0 E1 FF                  call 0x1406c6840
008AC778  45 33 C0                        xor r8d, r8d
008AC77B  E9 64 FF FF FF                  jmp 0x1408ac6e4
008AC780  48 8D 44 24 42                  lea rax, [rsp + 0x42]
008AC785  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AC78A  44 8A C7                        mov r8b, dil
008AC78D  41 8A D7                        mov dl, r15b
008AC790  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008AC795  48 8B CE                        mov rcx, rsi
008AC798  E8 3B 1F 00 00                  call 0x1408ae6d8
008AC79D  8B D8                           mov ebx, eax
008AC79F  E9 5B FD FF FF                  jmp 0x1408ac4ff
008AC7A4  41 8B 45 00                     mov eax, dword ptr [r13]
008AC7A8  A8 02                           test al, 2
008AC7AA  0F 84 BC 00 00 00               je 0x1408ac86c
008AC7B0  41 8B 45 00                     mov eax, dword ptr [r13]
008AC7B4  A8 02                           test al, 2
008AC7B6  0F 85 BD 00 00 00               jne 0x1408ac879
008AC7BC  48 8B CE                        mov rcx, rsi
008AC7BF  E8 8C CB A4 FF                  call 0x1402f9350
008AC7C4  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008AC7C9  74 0A                           je 0x1408ac7d5
008AC7CB  33 D2                           xor edx, edx
008AC7CD  48 8B CB                        mov rcx, rbx
008AC7D0  E8 9B 60 2D 00                  call 0x140b82870
008AC7D5  B8 9A 00 00 C0                  mov eax, 0xc000009a
008AC7DA  E9 8F FE FF FF                  jmp 0x1408ac66e
008AC7DF  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008AC7E4  0F 84 40 FF FF FF               je 0x1408ac72a
008AC7EA  33 D2                           xor edx, edx
008AC7EC  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008AC7F1  E8 7A 60 2D 00                  call 0x140b82870
008AC7F6  E9 2F FF FF FF                  jmp 0x1408ac72a
008AC7FB  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
008AC802  85 C0                           test eax, eax
008AC804  0F 84 8B 00 00 00               je 0x1408ac895
008AC80A  8B D0                           mov edx, eax
008AC80C  B9 41 00 00 00                  mov ecx, 0x41
008AC811  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008AC817  E8 D4 58 2D 00                  call 0x140b820f0
008AC81C  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008AC820  33 D2                           xor edx, edx
008AC822  48 85 C0                        test rax, rax
008AC825  75 5F                           jne 0x1408ac886
008AC827  41 8B 45 00                     mov eax, dword ptr [r13]
008AC82B  D1 E8                           shr eax, 1
008AC82D  24 01                           and al, 1
008AC82F  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008AC833  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
008AC838  45 33 C0                        xor r8d, r8d
008AC83B  48 8B D7                        mov rdx, rdi
008AC83E  48 8B CE                        mov rcx, rsi
008AC841  E8 82 1D 00 00                  call 0x1408ae5c8
008AC846  48 85 DB                        test rbx, rbx
008AC849  E9 7B FF FF FF                  jmp 0x1408ac7c9
008AC84E  33 D2                           xor edx, edx
008AC850  48 8B CB                        mov rcx, rbx
008AC853  E8 18 60 2D 00                  call 0x140b82870
008AC858  E9 3A FE FF FF                  jmp 0x1408ac697
008AC85D  33 D2                           xor edx, edx
008AC85F  48 8B CB                        mov rcx, rbx
008AC862  E8 09 60 2D 00                  call 0x140b82870
008AC867  E9 B9 FE FF FF                  jmp 0x1408ac725
008AC86C  49 8B CC                        mov rcx, r12
008AC86F  E8 FC 5F 2D 00                  call 0x140b82870
008AC874  E9 37 FF FF FF                  jmp 0x1408ac7b0
008AC879  48 8B CE                        mov rcx, rsi
008AC87C  E8 0F 42 9A FF                  call 0x140250a90
008AC881  E9 36 FF FF FF                  jmp 0x1408ac7bc
008AC886  41 83 0C 24 70                  or dword ptr [r12], 0x70
008AC88B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AC890  E9 37 FD FF FF                  jmp 0x1408ac5cc
008AC895  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
008AC899  41 83 0C 24 50                  or dword ptr [r12], 0x50
008AC89E  E9 3C FD FF FF                  jmp 0x1408ac5df
008AC8A3  0C 04                           or al, 4
008AC8A5  41 88 47 BA                     mov byte ptr [r15 - 0x46], al
008AC8A9  E9 75 FD FF FF                  jmp 0x1408ac623
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryEaFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5E;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m86;
    unsigned __int8 v_stack_m87;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (160);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_m68 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m88 = 0;
    *(unsigned int *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m87 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008AC6D2;
    a1 = v_rbx;
    if (a2 < v_rbx) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = ProbeForWrite(0, (unsigned int)(a4), 0 + 4, a4);
    a3 = 0;
    if (a8 != 0) goto loc_008AC3A3;
loc_008AC25E:
    if (a6 != 0) goto loc_008AC275;
loc_008AC26B:
    goto loc_008AC449;
loc_008AC275:
    if (a7 == 0) goto loc_008AC26B;
    v_stack_m58 = 0;
    v_stack_m84 = 0;
    v_stack_m88 = 1;
    if ((((unsigned __int8)(a6)) & (3)) != 0) goto loc_008AC3B9;
    if (((unsigned int)(a7) + a6 * 1) > v_stack_m80) goto loc_008AC3BE;
    if (((unsigned int)(a7) + a6 * 1) < a6) goto loc_008AC3BE;
loc_008AC2B5:
    result = ExAllocatePool2(97, (unsigned int)(a7), (unsigned int)(0x61456F49ULL), a4);
    v_stack_m80 = result;
    result = memcpy(result, a6, (unsigned int)(a7), a4);
    v_stack_m58 = result;
    v_stack_m84 = (unsigned int)((unsigned int)(a7));
    a3 = 0;
loc_008AC2F4:
    if (((unsigned int)((unsigned int)(a7))) < 5) goto loc_008AC34F;
    result = (unsigned int)((*(unsigned __int8 *)(result + 4)) + (6));
    if (((unsigned int)((unsigned int)(a7))) < ((unsigned int)(result))) goto loc_008AC3C5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) != 0) goto loc_008AC378;
    a1 = (unsigned int)(((unsigned int)(a7)) - ((unsigned int)(result)));
    v_stack_m84 = (unsigned int)(a1);
    if (sign_flag) goto loc_008AC323;
    goto loc_008AC449;
loc_008AC323:
    v_rdi = (unsigned int)((result) - ((unsigned int)(result)));
    v_stack_m84 = (unsigned int)(v_rdi);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0x80000014ULL));
    *(unsigned __int64 *)(a2 + 8) = (int)((unsigned int)(v_rdi));
    goto loc_008AC66E;
loc_008AC34F:
    v_stack_m84 = 0;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0x80000014ULL));
    goto loc_008AC66E;
loc_008AC378:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000014ULL)))) + (3));
    result = (unsigned int)((result) & (0xFFFFFFFCULL));
    if (((unsigned int)(result)) != 0) goto loc_008AC41D;
    if (sign_flag) goto loc_008AC41D;
    a1 = (unsigned int)(((unsigned int)(0x80000014ULL)) - (0));
    v_stack_m84 = (unsigned int)(a1);
    if (sign_flag) goto loc_008AC3F1;
    v_rdi = (v_rdi) + (0);
    v_stack_m58 = v_rdi;
    goto loc_008AC2F4;
loc_008AC3A3:
    if (((unsigned int)(a7)) < result) { result = (unsigned int)(a7); }
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    goto loc_008AC25E;
loc_008AC3B9:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_008AC3BE:
    goto loc_008AC2B5;
loc_008AC3C5:
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    v_stack_m84 = (unsigned int)(v_rdi);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0x80000014ULL));
    *(unsigned __int64 *)(a2 + 8) = (int)((unsigned int)(v_rdi));
    goto loc_008AC66E;
loc_008AC3F1:
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    v_stack_m84 = (unsigned int)(v_rdi);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0x80000014ULL));
    *(unsigned __int64 *)(a2 + 8) = (int)((unsigned int)(v_rdi));
    goto loc_008AC66E;
loc_008AC41D:
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    v_stack_m84 = (unsigned int)(v_rdi);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0x80000014ULL));
    *(unsigned __int64 *)(a2 + 8) = (int)((unsigned int)(v_rdi));
    goto loc_008AC66E;
loc_008AC449:
    goto loc_008AC465;
loc_008AC465:
    v_stack_mA8 = 0;
    result = IopReferenceFileObject(a1, 8, (unsigned __int8)(v_stack_m87), v_stack_m70);
    if (sign_flag) goto loc_008AC68C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 80)))) & (2)) == 0) goto loc_008AC69B;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70 + 80))) >> (2));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m70 + 128, a2, a3, v_stack_m70);
    v_stack_m86 = 0;
    if (1 != 0) goto loc_008AC780;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m70, a2, a3, result);
    v_rbx = 0;
loc_008AC4FF:
    if (v_stack_m86 != 0) goto loc_008AC7DF;
loc_008AC512:
    v_stack_m86 = 1;
    result = IopResetEvent(v_stack_m70, a2, a3, result);
    result = IoGetRelatedDeviceObject(v_stack_m70, a2, a3, result);
    v_stack_m60 = result;
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, result);
    v_stack_m48 = result;
    a2 = 0;
    if (result == 0) goto loc_008AC7A4;
    *(unsigned __int64 *)(result + 192) = v_stack_m70;
    *(unsigned __int64 *)(result + 152) = v_stack_m50;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m87);
    if (1 == 0) goto loc_008AC700;
loc_008AC57C:
    *(unsigned __int64 *)(result + 80) = 0;
    *(unsigned __int64 *)(result + 72) = 0;
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_m70;
    result = 0;
    if (v_stack_m88 != 0) {
        *(unsigned __int64 *)(result + 160) = v_stack_m80;
        *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 56) = v_stack_m80;
        result = a7;
        *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 48) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m60 + 48)))) & (4)) != 0) goto loc_008AC7FB;
loc_008AC5CC:
    *(unsigned __int64 *)(result + 112) = v_stack_p18;
loc_008AC5DF:
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 40) = (unsigned int)((unsigned int)(v_stack_m78));
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
    if (a8 != 0) goto loc_008AC8A3;
loc_008AC623:
    v_stack_m98 = 2;
    v_stack_mA0 = (unsigned __int8)(v_stack_m86);
    v_stack_mA8 = (unsigned __int8)(v_stack_m87);
    a4 = 0;
    result = IopSynchronousServiceTail(v_stack_m60, result, v_stack_m70, a4);
    if ((unsigned __int8)(v_stack_m86) == 0) {
        v_stack_mA0 = 0;
        a1 = v_stack_m40;
        v_stack_mA8 = a1;
        a4 = (unsigned __int8)(v_stack_m87);
        a3 = result;
        a2 = v_stack_m68;
        a1 = (unsigned int)(result);
        result = IopSynchronousApiServiceTail(a1, a2, a3, a4);
    }
    return result;
loc_008AC68C:
    if (v_stack_m60 != 0) goto loc_008AC84E;
loc_008AC697:
    goto loc_008AC66E;
loc_008AC69B:
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x76456F49ULL), a4);
    v_stack_m40 = result;
    if (result == 0) goto loc_008AC71A;
    a3 = 0;
    result = KeInitializeEvent(result, a3 + 1, a3, a4);
    v_r15 = 0;
    goto loc_008AC512;
loc_008AC6D2:
    if (a6 != 0) goto loc_008AC739;
loc_008AC6DF:
loc_008AC6E4:
    if (a8 == 0) goto loc_008AC465;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(a8)));
    goto loc_008AC465;
loc_008AC700:
    *(unsigned int *)(result) = 4;
    goto loc_008AC57C;
loc_008AC71A:
    if (v_stack_m60 != 0) goto loc_008AC85D;
loc_008AC725:
loc_008AC72A:
    result = ObfDereferenceObject(a8, a3 + 1, a3, a4);
    goto loc_008AC66E;
loc_008AC739:
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_008AC6DF;
    v_stack_m60 = 1;
    result = ExAllocatePool2(65, (unsigned int)((unsigned int)((unsigned int)(a7))), (unsigned int)(0x61456F49ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_008AC7D5;
    result = memcpy(result, a6, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), a4);
    a3 = 0;
    goto loc_008AC6E4;
loc_008AC780:
    v_stack_m80 = v_stack_m5E;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m48, 0, (unsigned __int8)(a6), a4);
    goto loc_008AC4FF;
loc_008AC7A4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 80)))) & (2)) == 0) goto loc_008AC86C;
loc_008AC7B0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 80)))) & (2)) != 0) goto loc_008AC879;
loc_008AC7BC:
    result = ObfDereferenceObject(v_stack_m48, 0, (unsigned __int8)(a6), a4);
loc_008AC7C9:
    if (v_stack_m60 != 0) {
        a2 = 0;
        a1 = (unsigned int)((unsigned int)(result));
        result = ExFreePoolWithTag(a1, a2, (unsigned __int8)(a6), a4);
    }
    goto loc_008AC66E;
loc_008AC7DF:
    if (v_stack_m60 == 0) goto loc_008AC72A;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m58, a2, (unsigned __int8)(a6), a4);
    goto loc_008AC72A;
loc_008AC7FB:
    if ((unsigned int)((unsigned int)(v_stack_p48)) == 0) goto loc_008AC895;
    result = ExAllocatePool2(65, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), (unsigned int)(0x42536F49ULL), a4);
    *(unsigned __int64 *)(a6 + 24) = result;
    a2 = 0;
    if (result != 0) goto loc_008AC886;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70 + 80))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_m80 = (unsigned __int8)(result);
    a3 = 0;
    result = IopExceptionCleanupEx(v_stack_m48, a6, a3, v_stack_m40);
    goto loc_008AC7C9;
loc_008AC84E:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(result)), a2, a3, v_stack_m40);
    goto loc_008AC697;
loc_008AC85D:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(result)), a2, a3, v_stack_m40);
    goto loc_008AC725;
loc_008AC86C:
    result = ExFreePoolWithTag(result, a2, a3, v_stack_m40);
    goto loc_008AC7B0;
loc_008AC879:
    result = IopReleaseFileObjectLock(v_stack_m48, a2, a3, v_stack_m40);
    goto loc_008AC7BC;
loc_008AC886:
    goto loc_008AC5CC;
loc_008AC895:
    *(unsigned __int64 *)(a6 + 24) = 0;
    goto loc_008AC5DF;
loc_008AC8A3:
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(v_r15 - 70) = (unsigned __int8)(result);
    goto loc_008AC623;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryEaFile(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, uint8_t Arg9)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5E;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m86;
    uint8_t v_stack_m87;
    uint8_t v_stack_m88;
    uint32_t v_stack_m98;
    uint8_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (160);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_m68 = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m88 = 0;
    *(uint32_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m87 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008AC6D2;
    Arg1 = local_rbx;
    if (Arg2 < local_rbx) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    result = ProbeForWrite(0, (uint32_t)(Arg4), 0 + 4, Arg4);
    Arg3 = 0;
    if (Arg8 != 0) goto loc_008AC3A3;
loc_008AC25E:
    if (Arg6 != 0) goto loc_008AC275;
loc_008AC26B:
    goto loc_008AC449;
loc_008AC275:
    if (Arg7 == NULL) goto loc_008AC26B;
    v_stack_m58 = 0;
    v_stack_m84 = 0;
    v_stack_m88 = 1;
    if ((((uint8_t)(Arg6)) & (3)) != 0) goto loc_008AC3B9;
    if (((uint32_t)(Arg7) + Arg6 * 1) > v_stack_m80) goto loc_008AC3BE;
    if (((uint32_t)(Arg7) + Arg6 * 1) < Arg6) goto loc_008AC3BE;
loc_008AC2B5:
    result = ExAllocatePool2(97, (uint32_t)(Arg7), (uint32_t)(0x61456F49ULL), Arg4);
    v_stack_m80 = result;
    result = memcpy(result, Arg6, (uint32_t)(Arg7), Arg4);
    v_stack_m58 = result;
    v_stack_m84 = (uint32_t)((uint32_t)(Arg7));
    Arg3 = 0;
loc_008AC2F4:
    if (((uint32_t)((uint32_t)(Arg7))) < 5) goto loc_008AC34F;
    result = (uint32_t)((*(uint8_t *)(result + 0x4)) + (6));
    if (((uint32_t)((uint32_t)(Arg7))) < ((uint32_t)(result))) goto loc_008AC3C5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) != 0) goto loc_008AC378;
    Arg1 = (uint32_t)(((uint32_t)(Arg7)) - ((uint32_t)(result)));
    v_stack_m84 = (uint32_t)(Arg1);
    if (sign_flag) goto loc_008AC323;
    goto loc_008AC449;
loc_008AC323:
    local_rdi = (uint32_t)((result) - ((uint32_t)(result)));
    v_stack_m84 = (uint32_t)(local_rdi);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(0x80000014ULL));
    *(uint64_t *)(arg2 + 0x8) = (int32_t)((uint32_t)(local_rdi));
    goto loc_008AC66E;
loc_008AC34F:
    v_stack_m84 = 0;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(0x80000014ULL));
    goto loc_008AC66E;
loc_008AC378:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000014ULL)))) + (3));
    result = (uint32_t)((result) & (0xFFFFFFFCULL));
    if (((uint32_t)(result)) != 0) goto loc_008AC41D;
    if (sign_flag) goto loc_008AC41D;
    Arg1 = (uint32_t)(((uint32_t)(0x80000014ULL)) - (0));
    v_stack_m84 = (uint32_t)(Arg1);
    if (sign_flag) goto loc_008AC3F1;
    local_rdi = (local_rdi) + (0);
    v_stack_m58 = local_rdi;
    goto loc_008AC2F4;
loc_008AC3A3:
    if (((uint32_t)(Arg7)) < result) { result = (uint32_t)(Arg7); }
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    goto loc_008AC25E;
loc_008AC3B9:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_008AC3BE:
    goto loc_008AC2B5;
loc_008AC3C5:
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    v_stack_m84 = (uint32_t)(local_rdi);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(0x80000014ULL));
    *(uint64_t *)(arg2 + 0x8) = (int32_t)((uint32_t)(local_rdi));
    goto loc_008AC66E;
loc_008AC3F1:
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    v_stack_m84 = (uint32_t)(local_rdi);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(0x80000014ULL));
    *(uint64_t *)(arg2 + 0x8) = (int32_t)((uint32_t)(local_rdi));
    goto loc_008AC66E;
loc_008AC41D:
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    v_stack_m84 = (uint32_t)(local_rdi);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(0x80000014ULL));
    *(uint64_t *)(arg2 + 0x8) = (int32_t)((uint32_t)(local_rdi));
    goto loc_008AC66E;
loc_008AC449:
    goto loc_008AC465;
loc_008AC465:
    v_stack_mA8 = 0;
    result = IopReferenceFileObject(Arg1, 8, (uint8_t)(v_stack_m87), v_stack_m70);
    if (sign_flag) goto loc_008AC68C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50)))) & (2)) == 0) goto loc_008AC69B;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50))) >> (2));
    local_rdi = (uint8_t)((local_rdi) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m70 + 128, Arg2, Arg3, v_stack_m70);
    v_stack_m86 = 0;
    if (1 != 0) goto loc_008AC780;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m70, Arg2, Arg3, result);
    local_rbx = 0;
loc_008AC4FF:
    if (v_stack_m86 != 0) goto loc_008AC7DF;
loc_008AC512:
    v_stack_m86 = 1;
    result = IopResetEvent(v_stack_m70, Arg2, Arg3, result);
    result = IoGetRelatedDeviceObject(v_stack_m70, Arg2, Arg3, result);
    v_stack_m60 = result;
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, result);
    v_stack_m48 = result;
    Arg2 = 0;
    if (result == 0) goto loc_008AC7A4;
    *(uint64_t *)(result + 0xC0) = v_stack_m70;
    *(uint64_t *)(result + 0x98) = v_stack_m50;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m87);
    if (1 == 0) goto loc_008AC700;
loc_008AC57C:
    *(uint64_t *)(result + 0x50) = 0;
    *(uint64_t *)(result + 0x48) = 0;
    *(uint64_t *)(result + 0x58) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 7;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_m70;
    result = 0;
    if (v_stack_m88 != 0) {
        *(uint64_t *)(result + 0xA0) = v_stack_m80;
        *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = v_stack_m80;
        result = Arg7;
        *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x30)))) & (4)) != 0) goto loc_008AC7FB;
loc_008AC5CC:
    *(uint64_t *)(result + 0x70) = v_stack_p18;
loc_008AC5DF:
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x28) = (uint32_t)((uint32_t)(v_stack_m78));
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
    if (Arg8 != 0) goto loc_008AC8A3;
loc_008AC623:
    v_stack_m98 = 2;
    v_stack_mA0 = (uint8_t)(v_stack_m86);
    v_stack_mA8 = (uint8_t)(v_stack_m87);
    Arg4 = 0;
    result = IopSynchronousServiceTail(v_stack_m60, result, v_stack_m70, Arg4);
    if ((uint8_t)(v_stack_m86) == 0) {
        v_stack_mA0 = 0;
        Arg1 = v_stack_m40;
        v_stack_mA8 = Arg1;
        Arg4 = (uint8_t)(v_stack_m87);
        Arg3 = result;
        Arg2 = v_stack_m68;
        Arg1 = (uint32_t)(result);
        result = IopSynchronousApiServiceTail(Arg1, Arg2, Arg3, Arg4);
    }
    return result;
loc_008AC68C:
    if (v_stack_m60 != 0) goto loc_008AC84E;
loc_008AC697:
    goto loc_008AC66E;
loc_008AC69B:
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x76456F49ULL), Arg4);
    v_stack_m40 = result;
    if (result == 0) goto loc_008AC71A;
    Arg3 = 0;
    result = KeInitializeEvent(result, Arg3 + 1, Arg3, Arg4);
    local_r15 = 0;
    goto loc_008AC512;
loc_008AC6D2:
    if (Arg6 != 0) goto loc_008AC739;
loc_008AC6DF:
loc_008AC6E4:
    if (Arg8 == 0) goto loc_008AC465;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8)));
    goto loc_008AC465;
loc_008AC700:
    *(uint32_t *)(result) = 4;
    goto loc_008AC57C;
loc_008AC71A:
    if (v_stack_m60 != 0) goto loc_008AC85D;
loc_008AC725:
loc_008AC72A:
    result = ObfDereferenceObject(Arg8, Arg3 + 1, Arg3, Arg4);
    goto loc_008AC66E;
loc_008AC739:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_008AC6DF;
    v_stack_m60 = 1;
    result = ExAllocatePool2(65, (uint32_t)((uint32_t)((uint32_t)(Arg7))), (uint32_t)(0x61456F49ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_008AC7D5;
    result = memcpy(result, Arg6, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), Arg4);
    Arg3 = 0;
    goto loc_008AC6E4;
loc_008AC780:
    v_stack_m80 = v_stack_m5E;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m48, 0, (uint8_t)(Arg6), Arg4);
    goto loc_008AC4FF;
loc_008AC7A4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50)))) & (2)) == 0) goto loc_008AC86C;
loc_008AC7B0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50)))) & (2)) != 0) goto loc_008AC879;
loc_008AC7BC:
    result = ObfDereferenceObject(v_stack_m48, 0, (uint8_t)(Arg6), Arg4);
loc_008AC7C9:
    if (v_stack_m60 != 0) {
        Arg2 = 0;
        Arg1 = (uint32_t)((uint32_t)(result));
        result = ExFreePoolWithTag(Arg1, Arg2, (uint8_t)(Arg6), Arg4);
    }
    goto loc_008AC66E;
loc_008AC7DF:
    if (v_stack_m60 == 0) goto loc_008AC72A;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m58, Arg2, (uint8_t)(Arg6), Arg4);
    goto loc_008AC72A;
loc_008AC7FB:
    if ((uint32_t)((uint32_t)(v_stack_p48)) == 0) goto loc_008AC895;
    result = ExAllocatePool2(65, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), (uint32_t)(0x42536F49ULL), Arg4);
    *(uint64_t *)(Arg6 + 0x18) = result;
    Arg2 = 0;
    if (result != 0) goto loc_008AC886;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x50))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_m80 = (uint8_t)(result);
    Arg3 = 0;
    result = IopExceptionCleanupEx(v_stack_m48, Arg6, Arg3, v_stack_m40);
    goto loc_008AC7C9;
loc_008AC84E:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(result)), Arg2, Arg3, v_stack_m40);
    goto loc_008AC697;
loc_008AC85D:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(result)), Arg2, Arg3, v_stack_m40);
    goto loc_008AC725;
loc_008AC86C:
    result = ExFreePoolWithTag(result, Arg2, Arg3, v_stack_m40);
    goto loc_008AC7B0;
loc_008AC879:
    result = IopReleaseFileObjectLock(v_stack_m48, Arg2, Arg3, v_stack_m40);
    goto loc_008AC7BC;
loc_008AC886:
    goto loc_008AC5CC;
loc_008AC895:
    *(uint64_t *)(Arg6 + 0x18) = 0;
    goto loc_008AC5DF;
loc_008AC8A3:
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(local_r15 - 0x46) = (uint8_t)(result);
    goto loc_008AC623;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R/W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg7` | `+ 0x0 + rdi*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AC1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
