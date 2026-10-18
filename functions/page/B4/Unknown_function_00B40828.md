# sub_00B40828

- RVA: `0x00B40828`–`0x00B40C48` (길이 `1,056` bytes)
- VA: `0x0000000140B40828`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B5924`
- 디코드: `263`개 명령, `1,056/1,056` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x00B40853` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (function, `0x0026FE90`)
- `0x00B40868` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (function, `0x0049E160`)
- `0x00B40909` → [PiGetDeviceRegProperty](../8F/PiGetDeviceRegProperty_function_008FAC6C.md) (function, `0x008FAC6C`)
- `0x00B40925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B4095C` → [PiGetDeviceRegProperty](../8F/PiGetDeviceRegProperty_function_008FAC6C.md) (function, `0x008FAC6C`)
- `0x00B4096F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B409FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B40AC7` → [PiGetDeviceRegProperty](../8F/PiGetDeviceRegProperty_function_008FAC6C.md) (function, `0x008FAC6C`)
- `0x00B40AE4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B40B0D` → [PiGetDeviceRegProperty](../8F/PiGetDeviceRegProperty_function_008FAC6C.md) (function, `0x008FAC6C`)
- `0x00B40B2F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B40B49` → [PnpGetDeviceResourcesFromRegistry](../A7/PnpGetDeviceResourcesFromRegistry_function_00A74344.md) (function, `0x00A74344`)
- `0x00B40B8B` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00B40BA8` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B40858` → RVA `0x00F8C438` (`.data`; read)
- `0x00B4087C` → RVA `0x00AFE270` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B4088B` → RVA `0x00AFE280` (`PAGE`; read)
- `0x00B40896` → RVA `0x00AFE290` (`PAGE`; read)
- `0x00B408A1` → RVA `0x00AFE2A0` (`PAGE`; read)
- `0x00B408AC` → RVA `0x00AFE2B0` (`PAGE`; read)
- `0x00B408B9` → RVA `0x00AFE2B8` (`PAGE`; read)
- `0x00B408C2` → RVA `0x00AFE2BC` (`PAGE`; read)
- `0x00B40B76` → RVA `0x00024038` (`.rdata`; read)
- `0x00B40B99` → RVA `0x0001BCE8` (`.rdata`; read)
- `0x00B40BBA` → RVA `0x00737DD0` (`IopTranslatorHandlerCm`; read)
- `0x00B40BC5` → RVA `0x00737DF0` (`IopTranslatorHandlerIo`; read)
- `0x00B40BD9` → RVA `0x00ACCFD0` (`ArbArbiterHandler`; read)
- `0x00B40C14` → RVA `0x00F8BA60` (`.data`; read)
- `0x00B40C1D` → RVA `0x00F8BD20` (`.data`; read)
- `0x00B40C26` → RVA `0x00F8BE80` (`.data`; read)
- `0x00B40C2F` → RVA `0x00F8BBC0` (`.data`; read)
- `0x00B40C38` → RVA `0x00F8BFE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00B40853` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (`PAGE` → `.text`)
  - `0x00B40868` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (`PAGE` → `.text`)
  - `0x00B40925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B4096F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B409FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B40AE4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B40B2F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B40B8B` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00B40BA8` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x00B4082D` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B4086E` → [IopPnPDispatch + 0x1F6](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40877` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B408CD` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B408D8` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40930` → [IopPnPDispatch + 0x150](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B4097A` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40980` → [IopPnPDispatch + 0x6B](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B409E4` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A02` → [IopPnPDispatch + 0x150](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A21` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A3A` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A53` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A64` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A83` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40A9C` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40AEF` → [IopPnPDispatch + 0x150](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40B16` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40B37` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40B5D` → [IopPnPDispatch + 0x1F6](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40B6C` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40BB0` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40BD0` → [IopPnPDispatch + 0x1F6](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40C0F` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)
  - `0x00B40C43` → [IopPnPDispatch + 0x73](../A7/IopPnPDispatch_function_00A74B90.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B40828  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B4082D  E9 D1 43 F3 FF                  jmp 0x140a74c03
00B40832  48 85 FF                        test rdi, rdi
00B40835  74 1C                           je 0x140b40853
00B40837  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B4083E  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00B40842  48 85 C0                        test rax, rax
00B40845  74 0C                           je 0x140b40853
00B40847  F7 80 8C 01 00 00 00 00 01 00   test dword ptr [rax + 0x18c], 0x10000
00B40851  74 05                           je 0x140b40858
00B40853  E8 38 F6 72 FF                  call 0x14026fe90
00B40858  48 8B 0D D9 BB 44 00            mov rcx, qword ptr [rip + 0x44bbd9]
00B4085F  BA 05 00 00 00                  mov edx, 5
00B40864  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00B40868  E8 F3 D8 95 FF                  call 0x14049e160
00B4086D  90                              nop
00B4086E  E9 13 45 F3 FF                  jmp 0x140a74d86
00B40873  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
00B40877  E9 87 43 F3 FF                  jmp 0x140a74c03
00B4087C  0F 28 05 ED D9 FB FF            movaps xmm0, xmmword ptr [rip - 0x42613]
00B40883  48 8B F1                        mov rsi, rcx
00B40886  0F 11 00                        movups xmmword ptr [rax], xmm0
00B40889  8B DF                           mov ebx, edi
00B4088B  0F 28 0D EE D9 FB FF            movaps xmm1, xmmword ptr [rip - 0x42612]
00B40892  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00B40896  0F 28 05 F3 D9 FB FF            movaps xmm0, xmmword ptr [rip - 0x4260d]
00B4089D  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00B408A1  0F 28 0D F8 D9 FB FF            movaps xmm1, xmmword ptr [rip - 0x42608]
00B408A8  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00B408AC  F2 0F 10 05 FC D9 FB FF         movsd xmm0, qword ptr [rip - 0x42604]
00B408B4  F2 0F 11 40 40                  movsd qword ptr [rax + 0x40], xmm0
00B408B9  8B 05 F9 D9 FB FF               mov eax, dword ptr [rip - 0x42607]
00B408BF  89 41 48                        mov dword ptr [rcx + 0x48], eax
00B408C2  0F B7 05 F3 D9 FB FF            movzx eax, word ptr [rip - 0x4260d]
00B408C9  66 89 41 4C                     mov word ptr [rcx + 0x4c], ax
00B408CD  E9 31 43 F3 FF                  jmp 0x140a74c03
00B408D2  81 FB BB 00 00 C0               cmp ebx, 0xc00000bb
00B408D8  0F 85 25 43 F3 FF               jne 0x140a74c03
00B408DE  49 8B 4C 24 30                  mov rcx, qword ptr [r12 + 0x30]
00B408E3  48 8D 45 48                     lea rax, [rbp + 0x48]
00B408E7  44 8B CF                        mov r9d, edi
00B408EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B408EF  41 BE 01 00 00 00               mov r14d, 1
00B408F5  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B408FA  45 39 75 08                     cmp dword ptr [r13 + 8], r14d
00B408FE  44 8B C2                        mov r8d, edx
00B40901  41 0F 95 C1                     setne r9b
00B40905  41 83 C1 02                     add r9d, 2
00B40909  E8 5E A3 DB FF                  call 0x1408fac6c
00B4090E  8B D8                           mov ebx, eax
00B40910  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B40915  75 5D                           jne 0x140b40974
00B40917  8B 55 48                        mov edx, dword ptr [rbp + 0x48]
00B4091A  B9 00 01 00 00                  mov ecx, 0x100
00B4091F  41 B8 50 70 64 64               mov r8d, 0x64647050
00B40925  E8 C6 17 04 00                  call 0x140b820f0
00B4092A  48 8B F8                        mov rdi, rax
00B4092D  48 85 C0                        test rax, rax
00B40930  0F 84 AA 43 F3 FF               je 0x140a74ce0
00B40936  49 8B 4C 24 30                  mov rcx, qword ptr [r12 + 0x30]
00B4093B  48 8D 45 48                     lea rax, [rbp + 0x48]
00B4093F  45 33 C9                        xor r9d, r9d
00B40942  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B40947  45 39 75 08                     cmp dword ptr [r13 + 8], r14d
00B4094B  45 8D 46 06                     lea r8d, [r14 + 6]
00B4094F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B40954  41 0F 95 C1                     setne r9b
00B40958  41 83 C1 02                     add r9d, 2
00B4095C  E8 0B A3 DB FF                  call 0x1408fac6c
00B40961  45 33 D2                        xor r10d, r10d
00B40964  8B D8                           mov ebx, eax
00B40966  48 8B CF                        mov rcx, rdi
00B40969  85 C0                           test eax, eax
00B4096B  79 18                           jns 0x140b40985
00B4096D  33 D2                           xor edx, edx
00B4096F  E8 FC 1E 04 00                  call 0x140b82870
00B40974  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
00B4097A  0F 85 83 42 F3 FF               jne 0x140a74c03
00B40980  E9 76 42 F3 FF                  jmp 0x140a74bfb
00B40985  44 8B 4D 48                     mov r9d, dword ptr [rbp + 0x48]
00B40989  4D 8B C2                        mov r8, r10
00B4098C  41 8B C1                        mov eax, r9d
00B4098F  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00B40993  48 03 C7                        add rax, rdi
00B40996  48 3B F8                        cmp rdi, rax
00B40999  73 46                           jae 0x140b409e1
00B4099B  0F B7 11                        movzx edx, word ptr [rcx]
00B4099E  66 85 D2                        test dx, dx
00B409A1  75 13                           jne 0x140b409b6
00B409A3  4D 85 C0                        test r8, r8
00B409A6  74 09                           je 0x140b409b1
00B409A8  49 8D 40 02                     lea rax, [r8 + 2]
00B409AC  48 3B C8                        cmp rcx, rax
00B409AF  74 30                           je 0x140b409e1
00B409B1  4C 8B C1                        mov r8, rcx
00B409B4  EB 18                           jmp 0x140b409ce
00B409B6  8D 42 E0                        lea eax, [rdx - 0x20]
00B409B9  66 83 F8 5F                     cmp ax, 0x5f
00B409BD  77 06                           ja 0x140b409c5
00B409BF  66 83 FA 2C                     cmp dx, 0x2c
00B409C3  75 09                           jne 0x140b409ce
00B409C5  66 C7 01 3F 00                  mov word ptr [rcx], 0x3f
00B409CA  44 8B 4D 48                     mov r9d, dword ptr [rbp + 0x48]
00B409CE  41 8B C1                        mov eax, r9d
00B409D1  48 83 C1 02                     add rcx, 2
00B409D5  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00B409D9  48 03 C7                        add rax, rdi
00B409DC  48 3B C8                        cmp rcx, rax
00B409DF  72 BA                           jb 0x140b4099b
00B409E1  48 8B F7                        mov rsi, rdi
00B409E4  E9 1A 42 F3 FF                  jmp 0x140a74c03
00B409E9  41 0F B7 54 24 28               movzx edx, word ptr [r12 + 0x28]
00B409EF  B9 00 01 00 00                  mov ecx, 0x100
00B409F4  41 B8 50 70 64 64               mov r8d, 0x64647050
00B409FA  E8 F1 16 04 00                  call 0x140b820f0
00B409FF  48 85 C0                        test rax, rax
00B40A02  0F 84 D8 42 F3 FF               je 0x140a74ce0
00B40A08  44 8B C7                        mov r8d, edi
00B40A0B  49 8B 4C 24 30                  mov rcx, qword ptr [r12 + 0x30]
00B40A10  48 8B F0                        mov rsi, rax
00B40A13  8B DF                           mov ebx, edi
00B40A15  41 39 7D 08                     cmp dword ptr [r13 + 8], edi
00B40A19  75 3D                           jne 0x140b40a58
00B40A1B  0F B7 11                        movzx edx, word ptr [rcx]
00B40A1E  66 85 D2                        test dx, dx
00B40A21  0F 84 DC 41 F3 FF               je 0x140a74c03
00B40A27  41 BE 01 00 00 00               mov r14d, 1
00B40A2D  66 83 FA 5C                     cmp dx, 0x5c
00B40A31  75 0D                           jne 0x140b40a40
00B40A33  45 03 C6                        add r8d, r14d
00B40A36  41 83 F8 02                     cmp r8d, 2
00B40A3A  0F 84 C3 41 F3 FF               je 0x140a74c03
00B40A40  48 83 C1 02                     add rcx, 2
00B40A44  66 89 10                        mov word ptr [rax], dx
00B40A47  48 83 C0 02                     add rax, 2
00B40A4B  0F B7 11                        movzx edx, word ptr [rcx]
00B40A4E  66 85 D2                        test dx, dx
00B40A51  75 DA                           jne 0x140b40a2d
00B40A53  E9 AB 41 F3 FF                  jmp 0x140a74c03
00B40A58  41 BE 01 00 00 00               mov r14d, 1
00B40A5E  0F B7 11                        movzx edx, word ptr [rcx]
00B40A61  66 85 D2                        test dx, dx
00B40A64  0F 84 99 41 F3 FF               je 0x140a74c03
00B40A6A  66 83 FA 5C                     cmp dx, 0x5c
00B40A6E  75 31                           jne 0x140b40aa1
00B40A70  45 03 C6                        add r8d, r14d
00B40A73  41 83 F8 02                     cmp r8d, 2
00B40A77  75 28                           jne 0x140b40aa1
00B40A79  48 83 C1 02                     add rcx, 2
00B40A7D  0F B7 11                        movzx edx, word ptr [rcx]
00B40A80  66 85 D2                        test dx, dx
00B40A83  0F 84 7A 41 F3 FF               je 0x140a74c03
00B40A89  48 2B C8                        sub rcx, rax
00B40A8C  66 89 10                        mov word ptr [rax], dx
00B40A8F  48 8D 40 02                     lea rax, [rax + 2]
00B40A93  0F B7 14 01                     movzx edx, word ptr [rcx + rax]
00B40A97  66 85 D2                        test dx, dx
00B40A9A  75 F0                           jne 0x140b40a8c
00B40A9C  E9 62 41 F3 FF                  jmp 0x140a74c03
00B40AA1  48 83 C1 02                     add rcx, 2
00B40AA5  EB B7                           jmp 0x140b40a5e
00B40AA7  49 8B DC                        mov rbx, r12
00B40AAA  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00B40AAE  48 8D 45 48                     lea rax, [rbp + 0x48]
00B40AB2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B40AB7  BF 0E 00 00 00                  mov edi, 0xe
00B40ABC  44 8B CF                        mov r9d, edi
00B40ABF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B40AC4  45 8B C6                        mov r8d, r14d
00B40AC7  E8 A0 A1 DB FF                  call 0x1408fac6c
00B40ACC  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
00B40ACF  85 C0                           test eax, eax
00B40AD1  0F 84 51 FD FF FF               je 0x140b40828
00B40AD7  8B D0                           mov edx, eax
00B40AD9  B9 00 01 00 00                  mov ecx, 0x100
00B40ADE  41 B8 50 70 64 64               mov r8d, 0x64647050
00B40AE4  E8 07 16 04 00                  call 0x140b820f0
00B40AE9  48 8B F0                        mov rsi, rax
00B40AEC  48 85 C0                        test rax, rax
00B40AEF  0F 84 EB 41 F3 FF               je 0x140a74ce0
00B40AF5  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00B40AF9  48 8D 45 48                     lea rax, [rbp + 0x48]
00B40AFD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B40B02  44 8B CF                        mov r9d, edi
00B40B05  45 8B C6                        mov r8d, r14d
00B40B08  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B40B0D  E8 5A A1 DB FF                  call 0x1408fac6c
00B40B12  8B D8                           mov ebx, eax
00B40B14  85 C0                           test eax, eax
00B40B16  0F 89 E7 40 F3 FF               jns 0x140a74c03
00B40B1C  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
00B40B22  B8 34 00 00 C0                  mov eax, 0xc0000034
00B40B27  48 8B CE                        mov rcx, rsi
00B40B2A  0F 44 D8                        cmove ebx, eax
00B40B2D  33 D2                           xor edx, edx
00B40B2F  E8 3C 1D 04 00                  call 0x140b82870
00B40B34  49 8B F4                        mov rsi, r12
00B40B37  E9 C7 40 F3 FF                  jmp 0x140a74c03
00B40B3C  48 8D 45 48                     lea rax, [rbp + 0x48]
00B40B40  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00B40B44  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B40B49  E8 F6 37 F3 FF                  call 0x140a74344
00B40B4E  8B D8                           mov ebx, eax
00B40B50  B8 34 00 00 C0                  mov eax, 0xc0000034
00B40B55  3B D8                           cmp ebx, eax
00B40B57  0F 85 16 FD FF FF               jne 0x140b40873
00B40B5D  E9 24 42 F3 FF                  jmp 0x140a74d86
00B40B62  49 8B CC                        mov rcx, r12
00B40B65  48 3B 0D CC B8 44 00            cmp rcx, qword ptr [rip + 0x44b8cc]
00B40B6C  0F 85 91 40 F3 FF               jne 0x140a74c03
00B40B72  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B40B76  48 8D 15 BB 34 4E FF            lea rdx, [rip - 0xb1cb45]
00B40B7D  48 3B CA                        cmp rcx, rdx
00B40B80  74 53                           je 0x140b40bd5
00B40B82  41 BE 10 00 00 00               mov r14d, 0x10
00B40B88  45 8B C6                        mov r8d, r14d
00B40B8B  E8 E0 9A B7 FF                  call 0x1406ba670
00B40B90  49 3B C6                        cmp rax, r14
00B40B93  74 40                           je 0x140b40bd5
00B40B95  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B40B99  48 8D 15 48 B1 4D FF            lea rdx, [rip - 0xb24eb8]
00B40BA0  48 3B CA                        cmp rcx, rdx
00B40BA3  74 11                           je 0x140b40bb6
00B40BA5  45 8B C6                        mov r8d, r14d
00B40BA8  E8 C3 9A B7 FF                  call 0x1406ba670
00B40BAD  49 3B C6                        cmp rax, r14
00B40BB0  0F 85 4D 40 F3 FF               jne 0x140a74c03
00B40BB6  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00B40BBA  48 8D 0D 0F 72 BF FF            lea rcx, [rip - 0x408df1]
00B40BC1  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
00B40BC5  48 8D 0D 24 72 BF FF            lea rcx, [rip - 0x408ddc]
00B40BCC  48 89 48 28                     mov qword ptr [rax + 0x28], rcx
00B40BD0  E9 B1 41 F3 FF                  jmp 0x140a74d86
00B40BD5  49 8B 55 18                     mov rdx, qword ptr [r13 + 0x18]
00B40BD9  48 8D 05 F0 C3 F8 FF            lea rax, [rip - 0x73c10]
00B40BE0  41 8B DC                        mov ebx, r12d
00B40BE3  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00B40BE7  41 0F B6 4D 20                  movzx ecx, byte ptr [r13 + 0x20]
00B40BEC  83 E9 01                        sub ecx, 1
00B40BEF  74 47                           je 0x140b40c38
00B40BF1  83 E9 01                        sub ecx, 1
00B40BF4  74 39                           je 0x140b40c2f
00B40BF6  83 E9 01                        sub ecx, 1
00B40BF9  74 2B                           je 0x140b40c26
00B40BFB  83 E9 01                        sub ecx, 1
00B40BFE  74 1D                           je 0x140b40c1d
00B40C00  83 E9 02                        sub ecx, 2
00B40C03  74 0F                           je 0x140b40c14
00B40C05  83 F9 01                        cmp ecx, 1
00B40C08  74 1C                           je 0x140b40c26
00B40C0A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00B40C0F  E9 EF 3F F3 FF                  jmp 0x140a74c03
00B40C14  48 8D 05 45 AE 44 00            lea rax, [rip + 0x44ae45]
00B40C1B  EB 22                           jmp 0x140b40c3f
00B40C1D  48 8D 05 FC B0 44 00            lea rax, [rip + 0x44b0fc]
00B40C24  EB 19                           jmp 0x140b40c3f
00B40C26  48 8D 05 53 B2 44 00            lea rax, [rip + 0x44b253]
00B40C2D  EB 10                           jmp 0x140b40c3f
00B40C2F  48 8D 05 8A AF 44 00            lea rax, [rip + 0x44af8a]
00B40C36  EB 07                           jmp 0x140b40c3f
00B40C38  48 8D 05 A1 B3 44 00            lea rax, [rip + 0x44b3a1]
00B40C3F  48 89 42 08                     mov qword ptr [rdx + 8], rax
00B40C43  E9 BB 3F F3 FF                  jmp 0x140a74c03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B40828(__int64 a1)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B40828(int64_t Arg1)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B40828&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
