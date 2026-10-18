# IopQueryNameInternal

- RVA: `0x008A6770`–`0x008A6DA9` (길이 `1,593` bytes)
- VA: `0x00000001408A6770`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F11C`
- 디코드: `369`개 명령, `1,593/1,593` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008A680E` → [ObQueryNameStringMode](ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008A6916` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A692A` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x008A6937` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008A694B` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008A69CD` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x008A69DA` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x008A69FD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x008A6A40` → [IopQueryXxxInformation](IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x008A6AF0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A6B3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A6BD2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A6BF5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A6C20` → [IoVolumeDeviceToDosName](IoVolumeDeviceToDosName_function_008A63F0.md) (function, `0x008A63F0`)
- `0x008A6C82` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008A6CBC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008A6D44` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [IoQueryFileDosDeviceName](IoQueryFileDosDeviceName_function_008A6340.md) at `0x008A6398`
- [IopQueryName](IopQueryName_function_008A8990.md) at `0x008A89B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x008A6916` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A692A` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008A6937` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008A694B` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008A69CD` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x008A69DA` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x008A69FD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x008A6AF0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A6B3B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A6BD2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A6BF5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A6C82` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008A6CBC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008A6D44` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008A6C17` → [sub_00B19D50](../B1/Unknown_function_00B19D50.md) (`tail-transfer`)
  - `0x008A6D89` → [sub_00B19D50 + 0x65](../B1/Unknown_function_00B19D50.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008A6770  4C 8B DC                        mov r11, rsp
008A6773  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
008A6777  45 88 43 18                     mov byte ptr [r11 + 0x18], r8b
008A677B  88 54 24 10                     mov byte ptr [rsp + 0x10], dl
008A677F  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
008A6783  53                              push rbx
008A6784  56                              push rsi
008A6785  57                              push rdi
008A6786  41 54                           push r12
008A6788  41 55                           push r13
008A678A  41 56                           push r14
008A678C  41 57                           push r15
008A678E  48 81 EC B0 00 00 00            sub rsp, 0xb0
008A6795  4D 8B E9                        mov r13, r9
008A6798  41 0F B6 D8                     movzx ebx, r8b
008A679C  48 8B C1                        mov rax, rcx
008A679F  45 33 C9                        xor r9d, r9d
008A67A2  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
008A67A7  45 8B F1                        mov r14d, r9d
008A67AA  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
008A67AF  44 88 8C 24 F8 00 00 00         mov byte ptr [rsp + 0xf8], r9b
008A67B7  0F 57 C0                        xorps xmm0, xmm0
008A67BA  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
008A67BF  BF 10 00 00 00                  mov edi, 0x10
008A67C4  44 8B BC 24 10 01 00 00         mov r15d, dword ptr [rsp + 0x110]
008A67CC  44 3B FF                        cmp r15d, edi
008A67CF  41 0F 43 FF                     cmovae edi, r15d
008A67D3  44 0F B6 A4 24 20 01 00 00      movzx r12d, byte ptr [rsp + 0x120]
008A67DC  41 80 FC 01                     cmp r12b, 1
008A67E0  0F 84 C9 04 00 00               je 0x1408a6caf
008A67E6  49 8D 73 B0                     lea rsi, [r11 - 0x50]
008A67EA  41 83 FF 10                     cmp r15d, 0x10
008A67EE  49 0F 43 F5                     cmovae rsi, r13
008A67F2  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008A67F6  84 DB                           test bl, bl
008A67F8  0F 85 14 04 00 00               jne 0x1408a6c12
008A67FE  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008A6803  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
008A6808  44 8B C7                        mov r8d, edi
008A680B  48 8B D6                        mov rdx, rsi
008A680E  E8 BD 16 00 00                  call 0x1408a7ed0
008A6813  8B D8                           mov ebx, eax
008A6815  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
008A6819  32 C0                           xor al, al
008A681B  89 94 24 10 01 00 00            mov dword ptr [rsp + 0x110], edx
008A6822  85 DB                           test ebx, ebx
008A6824  0F 88 BB 04 00 00               js 0x1408a6ce5
008A682A  84 C0                           test al, al
008A682C  0F 84 47 03 00 00               je 0x1408a6b79
008A6832  49 83 C5 10                     add r13, 0x10
008A6836  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
008A683B  0F B6 8C 24 00 01 00 00         movzx ecx, byte ptr [rsp + 0x100]
008A6843  84 C9                           test cl, cl
008A6845  0F 85 6A 03 00 00               jne 0x1408a6bb5
008A684B  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
008A6852  41 80 FC 01                     cmp r12b, 1
008A6856  0F 84 EB 03 00 00               je 0x1408a6c47
008A685C  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
008A6864  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008A686C  80 BC 24 F8 00 00 00 00         cmp byte ptr [rsp + 0xf8], 0
008A6874  0F 85 1C 05 00 00               jne 0x1408a6d96
008A687A  32 D2                           xor dl, dl
008A687C  88 94 24 F8 00 00 00            mov byte ptr [rsp + 0xf8], dl
008A6883  41 83 FF 10                     cmp r15d, 0x10
008A6887  0F 82 10 03 00 00               jb 0x1408a6b9d
008A688D  3B C7                           cmp eax, edi
008A688F  0F 87 08 03 00 00               ja 0x1408a6b9d
008A6895  4C 89 6B 08                     mov qword ptr [rbx + 8], r13
008A6899  EB 0C                           jmp 0x1408a68a7
008A689B  8B D8                           mov ebx, eax
008A689D  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008A68A2  E9 8A 02 00 00                  jmp 0x1408a6b31
008A68A7  0F B7 06                        movzx eax, word ptr [rsi]
008A68AA  4C 03 E8                        add r13, rax
008A68AD  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
008A68B2  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
008A68B9  48 8B B4 24 08 01 00 00         mov rsi, qword ptr [rsp + 0x108]
008A68C1  41 80 FC 01                     cmp r12b, 1
008A68C5  0F 85 8B 02 00 00               jne 0x1408a6b56
008A68CB  49 8B DE                        mov rbx, r14
008A68CE  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
008A68D3  84 D2                           test dl, dl
008A68D5  75 05                           jne 0x1408a68dc
008A68D7  2B F8                           sub edi, eax
008A68D9  83 C7 04                        add edi, 4
008A68DC  89 BC 24 10 01 00 00            mov dword ptr [rsp + 0x110], edi
008A68E3  41 80 FC 01                     cmp r12b, 1
008A68E7  0F 84 28 01 00 00               je 0x1408a6a15
008A68ED  41 8B 42 50                     mov eax, dword ptr [r10 + 0x50]
008A68F1  A8 02                           test al, 2
008A68F3  0F 84 24 01 00 00               je 0x1408a6a1d
008A68F9  0F 57 C0                        xorps xmm0, xmm0
008A68FC  33 C0                           xor eax, eax
008A68FE  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
008A6906  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
008A690E  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
008A6913  49 8B CA                        mov rcx, r10
008A6916  E8 05 91 96 FF                  call 0x14020fa20
008A691B  45 33 C0                        xor r8d, r8d
008A691E  41 8D 50 01                     lea edx, [r8 + 1]
008A6922  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008A692A  E8 E1 73 B6 FF                  call 0x14040dd10
008A692F  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
008A6937  E8 E4 47 9F FF                  call 0x14029b120
008A693C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008A6941  45 33 C0                        xor r8d, r8d
008A6944  0F B6 50 4C                     movzx edx, byte ptr [rax + 0x4c]
008A6948  48 8B C8                        mov rcx, rax
008A694B  E8 D0 0D 96 FF                  call 0x140207720
008A6950  48 8B F8                        mov rdi, rax
008A6953  48 85 C0                        test rax, rax
008A6956  0F 84 E0 03 00 00               je 0x1408a6d3c
008A695C  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
008A6964  48 89 90 C0 00 00 00            mov qword ptr [rax + 0xc0], rdx
008A696B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A6974  48 89 87 98 00 00 00            mov qword ptr [rdi + 0x98], rax
008A697B  C6 47 40 00                     mov byte ptr [rdi + 0x40], 0
008A697F  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008A6987  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
008A698B  C7 47 10 04 10 00 00            mov dword ptr [rdi + 0x10], 0x1004
008A6992  48 8D 44 24 70                  lea rax, [rsp + 0x70]
008A6997  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
008A699B  45 33 ED                        xor r13d, r13d
008A699E  4C 89 6F 58                     mov qword ptr [rdi + 0x58], r13
008A69A2  48 8B 8F B8 00 00 00            mov rcx, qword ptr [rdi + 0xb8]
008A69A9  C6 41 B8 05                     mov byte ptr [rcx - 0x48], 5
008A69AD  48 89 51 E8                     mov qword ptr [rcx - 0x18], rdx
008A69B1  48 89 5F 18                     mov qword ptr [rdi + 0x18], rbx
008A69B5  83 4F 10 10                     or dword ptr [rdi + 0x10], 0x10
008A69B9  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
008A69C0  89 41 C0                        mov dword ptr [rcx - 0x40], eax
008A69C3  C7 41 C8 09 00 00 00            mov dword ptr [rcx - 0x38], 9
008A69CA  48 8B CF                        mov rcx, rdi
008A69CD  E8 EE 0B 96 FF                  call 0x1402075c0
008A69D2  48 8B D7                        mov rdx, rdi
008A69D5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008A69DA  E8 D1 4A 9F FF                  call 0x14029b4b0
008A69DF  8B D8                           mov ebx, eax
008A69E1  3D 03 01 00 00                  cmp eax, 0x103
008A69E6  75 1E                           jne 0x1408a6a06
008A69E8  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008A69ED  45 33 C9                        xor r9d, r9d
008A69F0  45 33 C0                        xor r8d, r8d
008A69F3  33 D2                           xor edx, edx
008A69F5  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008A69FD  E8 AE 7C 96 FF                  call 0x14020e6b0
008A6A02  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
008A6A06  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008A6A0A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008A6A0E  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
008A6A13  EB 32                           jmp 0x1408a6a47
008A6A15  84 C9                           test cl, cl
008A6A17  0F 85 D0 FE FF FF               jne 0x1408a68ed
008A6A1D  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
008A6A22  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008A6A27  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008A6A2C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008A6A31  45 0F B6 CC                     movzx r9d, r12b
008A6A35  44 8B C7                        mov r8d, edi
008A6A38  BA 09 00 00 00                  mov edx, 9
008A6A3D  49 8B CA                        mov rcx, r10
008A6A40  E8 8B 1F 00 00                  call 0x1408a89d0
008A6A45  8B D8                           mov ebx, eax
008A6A47  8B C3                           mov eax, ebx
008A6A49  25 00 00 00 C0                  and eax, 0xc0000000
008A6A4E  3D 00 00 00 C0                  cmp eax, 0xc0000000
008A6A53  75 38                           jne 0x1408a6a8d
008A6A55  8D 83 FE FF FF 3F               lea eax, [rbx + 0x3ffffffe]
008A6A5B  83 F8 0E                        cmp eax, 0xe
008A6A5E  0F 87 CD 00 00 00               ja 0x1408a6b31
008A6A64  B9 03 48 00 00                  mov ecx, 0x4803
008A6A69  0F A3 C1                        bt ecx, eax
008A6A6C  0F 83 BF 00 00 00               jae 0x1408a6b31
008A6A72  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
008A6A7A  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
008A6A7F  33 C9                           xor ecx, ecx
008A6A81  89 0A                           mov dword ptr [rdx], ecx
008A6A83  66 C7 42 04 5C 00               mov word ptr [rdx + 4], 0x5c
008A6A89  8B D9                           mov ebx, ecx
008A6A8B  EB 14                           jmp 0x1408a6aa1
008A6A8D  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
008A6A92  83 7C 24 40 04                  cmp dword ptr [rsp + 0x40], 4
008A6A97  73 08                           jae 0x1408a6aa1
008A6A99  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
008A6AA1  80 BC 24 F8 00 00 00 00         cmp byte ptr [rsp + 0xf8], 0
008A6AA9  0F 85 47 02 00 00               jne 0x1408a6cf6
008A6AAF  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008A6AB3  83 C0 FC                        add eax, -4
008A6AB6  8B 0A                           mov ecx, dword ptr [rdx]
008A6AB8  44 8B C1                        mov r8d, ecx
008A6ABB  3B C1                           cmp eax, ecx
008A6ABD  44 0F 46 C0                     cmovbe r8d, eax
008A6AC1  2B CE                           sub ecx, esi
008A6AC3  41 03 CD                        add ecx, r13d
008A6AC6  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
008A6ACA  66 83 7A 04 5C                  cmp word ptr [rdx + 4], 0x5c
008A6ACF  0F 85 5D 02 00 00               jne 0x1408a6d32
008A6AD5  41 8B F8                        mov edi, r8d
008A6AD8  41 80 FC 01                     cmp r12b, 1
008A6ADC  74 08                           je 0x1408a6ae6
008A6ADE  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
008A6AE2  89 02                           mov dword ptr [rdx], eax
008A6AE4  EB 0F                           jmp 0x1408a6af5
008A6AE6  4C 8B C7                        mov r8, rdi
008A6AE9  48 83 C2 04                     add rdx, 4
008A6AED  49 8B CD                        mov rcx, r13
008A6AF0  E8 4B FD E1 FF                  call 0x1406c6840
008A6AF5  4A 8D 0C 2F                     lea rcx, [rdi + r13]
008A6AF9  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
008A6AFE  33 C0                           xor eax, eax
008A6B00  66 89 01                        mov word ptr [rcx], ax
008A6B03  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008A6B07  83 C0 02                        add eax, 2
008A6B0A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008A6B0E  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
008A6B16  89 02                           mov dword ptr [rdx], eax
008A6B18  2B CE                           sub ecx, esi
008A6B1A  8D 41 F0                        lea eax, [rcx - 0x10]
008A6B1D  66 89 06                        mov word ptr [rsi], ax
008A6B20  66 83 E9 0E                     sub cx, 0xe
008A6B24  66 89 4E 02                     mov word ptr [rsi + 2], cx
008A6B28  EB 07                           jmp 0x1408a6b31
008A6B2A  8B D8                           mov ebx, eax
008A6B2C  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008A6B31  4D 85 F6                        test r14, r14
008A6B34  74 0A                           je 0x1408a6b40
008A6B36  33 D2                           xor edx, edx
008A6B38  49 8B CE                        mov rcx, r14
008A6B3B  E8 30 BD 2D 00                  call 0x140b82870
008A6B40  8B C3                           mov eax, ebx
008A6B42  48 81 C4 B0 00 00 00            add rsp, 0xb0
008A6B49  41 5F                           pop r15
008A6B4B  41 5E                           pop r14
008A6B4D  41 5D                           pop r13
008A6B4F  41 5C                           pop r12
008A6B51  5F                              pop rdi
008A6B52  5E                              pop rsi
008A6B53  5B                              pop rbx
008A6B54  C3                              ret
008A6B55  CC                              int3
008A6B56  84 D2                           test dl, dl
008A6B58  0F 85 BA 01 00 00               jne 0x1408a6d18
008A6B5E  49 8D 5D FC                     lea rbx, [r13 - 4]
008A6B62  8B 03                           mov eax, dword ptr [rbx]
008A6B64  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008A6B68  2B FB                           sub edi, ebx
008A6B6A  83 C7 FE                        add edi, -2
008A6B6D  03 FE                           add edi, esi
008A6B6F  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
008A6B74  E9 63 FD FF FF                  jmp 0x1408a68dc
008A6B79  8B 9C 24 F8 00 00 00            mov ebx, dword ptr [rsp + 0xf8]
008A6B80  0F B6 DB                        movzx ebx, bl
008A6B83  41 B8 01 00 00 00               mov r8d, 1
008A6B89  66 83 3E 00                     cmp word ptr [rsi], 0
008A6B8D  41 0F 44 D8                     cmove ebx, r8d
008A6B91  89 9C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ebx
008A6B98  E9 95 FC FF FF                  jmp 0x1408a6832
008A6B9D  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
008A6BA5  89 02                           mov dword ptr [rdx], eax
008A6BA7  B2 01                           mov dl, 1
008A6BA9  88 94 24 F8 00 00 00            mov byte ptr [rsp + 0xf8], dl
008A6BB0  E9 04 FD FF FF                  jmp 0x1408a68b9
008A6BB5  84 C0                           test al, al
008A6BB7  0F 84 8E FC FF FF               je 0x1408a684b
008A6BBD  3B FA                           cmp edi, edx
008A6BBF  0F 82 C1 01 00 00               jb 0x1408a6d86
008A6BC5  0F B7 06                        movzx eax, word ptr [rsi]
008A6BC8  44 8B C0                        mov r8d, eax
008A6BCB  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
008A6BCF  49 8B CD                        mov rcx, r13
008A6BD2  E8 69 FC E1 FF                  call 0x1406c6840
008A6BD7  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
008A6BDF  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
008A6BE3  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
008A6BE6  F6 C1 10                        test cl, 0x10
008A6BE9  0F 85 64 01 00 00               jne 0x1408a6d53
008A6BEF  33 D2                           xor edx, edx
008A6BF1  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
008A6BF5  E8 76 BC 2D 00                  call 0x140b82870
008A6BFA  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008A6BFE  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
008A6C05  0F B6 8C 24 00 01 00 00         movzx ecx, byte ptr [rsp + 0x100]
008A6C0D  E9 4A FC FF FF                  jmp 0x1408a685c
008A6C12  8B 41 34                        mov eax, dword ptr [rcx + 0x34]
008A6C15  A8 10                           test al, 0x10
008A6C17  0F 85 33 31 27 00               jne 0x140b19d50
008A6C1D  48 8B D6                        mov rdx, rsi
008A6C20  E8 CB F7 FF FF                  call 0x1408a63f0
008A6C25  8B D8                           mov ebx, eax
008A6C27  0F B7 16                        movzx edx, word ptr [rsi]
008A6C2A  83 C2 12                        add edx, 0x12
008A6C2D  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
008A6C31  89 94 24 10 01 00 00            mov dword ptr [rsp + 0x110], edx
008A6C38  85 DB                           test ebx, ebx
008A6C3A  0F 88 2B 01 00 00               js 0x1408a6d6b
008A6C40  B0 01                           mov al, 1
008A6C42  E9 DB FB FF FF                  jmp 0x1408a6822
008A6C47  41 83 FF 10                     cmp r15d, 0x10
008A6C4B  0F 82 0B FC FF FF               jb 0x1408a685c
008A6C51  3B C7                           cmp eax, edi
008A6C53  0F 87 03 FC FF FF               ja 0x1408a685c
008A6C59  0F B7 06                        movzx eax, word ptr [rsi]
008A6C5C  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008A6C64  66 89 03                        mov word ptr [rbx], ax
008A6C67  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
008A6C6B  66 89 43 02                     mov word ptr [rbx + 2], ax
008A6C6F  44 8B 84 24 10 01 00 00         mov r8d, dword ptr [rsp + 0x110]
008A6C77  49 83 E8 10                     sub r8, 0x10
008A6C7B  48 8D 56 10                     lea rdx, [rsi + 0x10]
008A6C7F  49 8B CD                        mov rcx, r13
008A6C82  E8 B9 FB E1 FF                  call 0x1406c6840
008A6C87  0F B6 8C 24 00 01 00 00         movzx ecx, byte ptr [rsp + 0x100]
008A6C8F  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
008A6C97  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
008A6C9E  E9 C9 FB FF FF                  jmp 0x1408a686c
008A6CA3  8B D8                           mov ebx, eax
008A6CA5  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008A6CAA  E9 82 FE FF FF                  jmp 0x1408a6b31
008A6CAF  8B D7                           mov edx, edi
008A6CB1  B9 00 01 00 00                  mov ecx, 0x100
008A6CB6  41 B8 49 6F 4E 32               mov r8d, 0x324e6f49
008A6CBC  E8 2F B4 2D 00                  call 0x140b820f0
008A6CC1  4C 8B F0                        mov r14, rax
008A6CC4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008A6CC9  48 85 C0                        test rax, rax
008A6CCC  0F 84 AA 00 00 00               je 0x1408a6d7c
008A6CD2  48 8B F0                        mov rsi, rax
008A6CD5  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008A6CDD  45 33 C9                        xor r9d, r9d
008A6CE0  E9 0D FB FF FF                  jmp 0x1408a67f2
008A6CE5  81 FB 04 00 00 C0               cmp ebx, 0xc0000004
008A6CEB  0F 84 41 FB FF FF               je 0x1408a6832
008A6CF1  E9 3B FE FF FF                  jmp 0x1408a6b31
008A6CF6  8B 02                           mov eax, dword ptr [rdx]
008A6CF8  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
008A6D00  01 01                           add dword ptr [rcx], eax
008A6D02  BB 04 00 00 C0                  mov ebx, 0xc0000004
008A6D07  B8 05 00 00 80                  mov eax, 0x80000005
008A6D0C  41 83 FF 10                     cmp r15d, 0x10
008A6D10  0F 43 D8                        cmovae ebx, eax
008A6D13  E9 19 FE FF FF                  jmp 0x1408a6b31
008A6D18  48 8D 9C 24 98 00 00 00         lea rbx, [rsp + 0x98]
008A6D20  41 83 FF 10                     cmp r15d, 0x10
008A6D24  48 0F 43 DE                     cmovae rbx, rsi
008A6D28  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
008A6D2D  E9 AA FB FF FF                  jmp 0x1408a68dc
008A6D32  BB 39 00 00 C0                  mov ebx, 0xc0000039
008A6D37  E9 F5 FD FF FF                  jmp 0x1408a6b31
008A6D3C  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
008A6D44  E8 07 26 A5 FF                  call 0x1402f9350
008A6D49  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008A6D4E  E9 F4 FC FF FF                  jmp 0x1408a6a47
008A6D53  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008A6D57  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
008A6D5E  0F B6 8C 24 00 01 00 00         movzx ecx, byte ptr [rsp + 0x100]
008A6D66  E9 F9 FA FF FF                  jmp 0x1408a6864
008A6D6B  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
008A6D73  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
008A6D77  E9 82 FA FF FF                  jmp 0x1408a67fe
008A6D7C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008A6D81  E9 AB FD FF FF                  jmp 0x1408a6b31
008A6D86  83 FF 10                        cmp edi, 0x10
008A6D89  0F 83 26 30 27 00               jae 0x140b19db5
008A6D8F  33 C0                           xor eax, eax
008A6D91  E9 32 FE FF FF                  jmp 0x1408a6bc8
008A6D96  83 C0 02                        add eax, 2
008A6D99  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
008A6DA0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008A6DA4  E9 D1 FA FF FF                  jmp 0x1408a687a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopQueryNameInternal(__int64 a1, unsigned __int8 a2, unsigned __int8 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p110;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pF0;
    unsigned int v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    a4 = 0;
    v_stack_mA8 = 0;
    v_stack_m98 = 0;
    v_stack_p10 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_rdi = 16;
    if (((unsigned int)((unsigned int)(a5))) >= 16) { v_rdi = (unsigned int)((unsigned int)(a5)); }
    if (a7 == 1) goto loc_008A6CAF;
    v_rsi = v_rsp - 80;
    if (((unsigned int)((unsigned int)(a5))) >= 16) { v_rsi = 0; }
loc_008A67F2:
    if (a3 != 0) goto loc_008A6C12;
loc_008A67FE:
    v_stack_mC8 = 0;
    result = ObQueryNameStringMode(*(unsigned __int64 *)(a1 + 8), v_rsi, (unsigned int)((unsigned int)(v_rdi)), v_stack_mA8);
    result = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_mA8));
loc_008A6822:
    if (sign_flag) goto loc_008A6CE5;
    if (0 == 0) goto loc_008A6B79;
loc_008A6832:
    v_r13 = (a4) + (16);
    v_stack_m88 = v_r13;
    if ((unsigned __int8)(v_stack_p18) != 0) goto loc_008A6BB5;
loc_008A684B:
    if (a7 == 1) goto loc_008A6C47;
loc_008A685C:
loc_008A6864:
loc_008A686C:
    if (v_stack_p10 != 0) goto loc_008A6D96;
loc_008A687A:
    a2 = 0;
    v_stack_p10 = 0;
    if (((unsigned int)((unsigned int)(a5))) < 16) goto loc_008A6B9D;
    if (((unsigned int)((unsigned int)(a5))) > ((unsigned int)(v_rdi))) goto loc_008A6B9D;
    *(unsigned __int64 *)(v_stack_p20 + 8) = v_r13;
    goto loc_008A68A7;
loc_008A68A7:
    v_r13 = (v_r13) + (*(unsigned __int16 *)(v_rsi));
    v_stack_m88 = v_r13;
loc_008A68B9:
    if (a7 != 1) goto loc_008A6B56;
    v_stack_mA0 = 0;
    if (0 == 0) {
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)((unsigned int)(a5))));
        v_rdi = (unsigned int)((v_rdi) + (4));
    }
    v_stack_p28 = (unsigned int)(v_rdi);
    if (a7 == 1) goto loc_008A6A15;
loc_008A68ED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 80)))) & (2)) == 0) goto loc_008A6A1D;
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m78 = v_xmm0;
    result = ObfReferenceObject(v_stack_p8, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_mA8);
    a3 = 0;
    result = KeInitializeEvent(v_stack_m68, a3 + 1, a3, v_stack_mA8);
    result = IoGetRelatedDeviceObject(v_stack_p8, a3 + 1, a3, v_stack_mA8);
    v_stack_m80 = result;
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, v_stack_mA8);
    if (result == 0) goto loc_008A6D3C;
    *(unsigned __int64 *)(result + 192) = v_stack_p8;
    *(unsigned __int64 *)(result + 152) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(result + 64) = 0;
    *(unsigned __int64 *)(result + 80) = v_stack_m68;
    *(unsigned int *)(result + 16) = 0x1004ULL;
    *(unsigned __int64 *)(result + 72) = v_stack_m78;
    v_r13 = 0;
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 5;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_p8;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(a5));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = 9;
    result = IopQueueThreadIrp(result, v_stack_p8, a3, v_stack_mA8);
    result = IofCallDriver(v_stack_m80, result, a3, v_stack_mA8);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 259) {
        v_stack_mC8 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_m68;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        v_rbx = v_stack_m78;
    }
    v_stack_mA8 = (unsigned int)((unsigned int)(v_stack_m70));
    goto loc_008A6A47;
loc_008A6A15:
    if ((unsigned __int8)(a1) != 0) goto loc_008A68ED;
loc_008A6A1D:
    v_stack_mB8 = 1;
    v_stack_mC0 = v_stack_mA8;
    v_stack_mC8 = v_rbx;
    result = IopQueryXxxInformation(v_stack_p8, 9, (unsigned int)((unsigned int)(result)), a7);
loc_008A6A47:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (0xC0000000ULL));
    if (((unsigned int)(result)) != 0xC0000000ULL) goto loc_008A6A8D;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 1073741822)) > 14) goto loc_008A6B31;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 1073741822)) >= 14) goto loc_008A6B31;
    v_stack_mA8 = 4;
    a1 = 0;
    *(unsigned int *)(v_stack_mA0) = 0;
    *(unsigned __int16 *)(v_stack_mA0 + 4) = 92;
    goto loc_008A6AA1;
loc_008A6A8D:
    if (v_stack_mA8 < 4) {
        v_stack_mA8 = 4;
    }
    if (v_stack_p10 != 0) goto loc_008A6CF6;
    result = (unsigned int)(((unsigned int)(v_stack_mA8)) + (-4));
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0))));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0))))) { a3 = (unsigned int)(result); }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA0))) - ((unsigned int)(v_stack_p20)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_stack_m88)));
    v_stack_mA8 = (unsigned int)(a1);
    if ((*(unsigned __int16 *)(v_stack_mA0 + 4)) != 92) goto loc_008A6D32;
    if (a7 == 1) goto loc_008A6AE6;
    *(unsigned int *)(v_stack_mA0) = (unsigned int)((unsigned int)(v_stack_m90));
    goto loc_008A6AF5;
loc_008A6AE6:
    a2 = (v_stack_mA0) + (4);
    result = memcpy(v_stack_m88, a2, (unsigned int)(a3), a7);
loc_008A6AF5:
    v_stack_m88 = (unsigned int)(a3) + v_stack_m88 * 1;
    result = 0;
    *(unsigned __int16 *)((unsigned int)(a3) + v_stack_m88 * 1) = 0;
    result = (unsigned int)(((unsigned int)(v_stack_mA8)) + (2));
    v_stack_mA8 = (unsigned int)(result);
    *(unsigned int *)(a6) = (unsigned int)(result);
    a1 = (unsigned int)(((unsigned int)(a3) + v_stack_m88 * 1) - ((unsigned int)(v_stack_p20)));
    *(unsigned __int16 *)(v_stack_p20) = (unsigned __int16)(a1 - 16);
    a1 = (unsigned __int16)((a1) - (14));
    *(unsigned __int16 *)(v_stack_p20 + 2) = (unsigned __int16)(a1);
    goto loc_008A6B31;
loc_008A6B31:
    result = a1 - 16;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(a3), a7);
    }
    v_rsp = (v_rsp) + (176);
    return 0;
loc_008A6B56:
    if (0 != 0) goto loc_008A6D18;
    v_stack_p58 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 - 4)));
    v_rdi = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(v_stack_m88 - 4)));
    v_rdi = (unsigned int)((v_rdi) + (-2));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_stack_p20)));
    v_stack_p48 = v_stack_m88 - 4;
    goto loc_008A68DC;
loc_008A6B79:
    v_rbx = (unsigned __int8)((unsigned int)(v_stack_pF8));
    if ((*(unsigned __int16 *)(v_stack_p20)) == 0) { v_rbx = 1; }
    v_stack_pF8 = (unsigned int)(v_rbx);
    goto loc_008A6832;
loc_008A6B9D:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 - 4)));
    v_stack_pF8 = 1;
    goto loc_008A68B9;
loc_008A6BB5:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m88 - 4))) == 0) goto loc_008A684B;
    if (((unsigned int)(v_rdi)) < 1) goto loc_008A6D86;
loc_008A6BC8:
    result = memcpy(v_stack_m88, *(unsigned __int64 *)(v_stack_p20 + 8), (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p20))), a7);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pF0 + 8) + 52)))) & (16)) != 0) goto loc_008A6D53;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p20 + 8), a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p20))), a7);
    v_stack_p110 = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_008A685C;
loc_008A6C12:
    result = IoVolumeDeviceToDosName(v_stack_p100, v_stack_p20, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p20))), a7);
    a2 = (unsigned int)((*(unsigned __int16 *)(v_stack_p20)) + (18));
    v_stack_p40 = a2;
    v_stack_p110 = a2;
    if (sign_flag) goto loc_008A6D6B;
    goto loc_008A6822;
loc_008A6C47:
    if (((unsigned int)((unsigned int)(a5))) < 16) goto loc_008A685C;
    if (1 > ((unsigned int)(v_rdi))) goto loc_008A685C;
    *(unsigned __int16 *)(v_stack_p108) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p20));
    *(unsigned __int16 *)(v_stack_p108 + 2) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p20 + 2));
    a3 = ((unsigned int)(a5)) - (16);
    result = memcpy(v_stack_m88, v_stack_p20 + 16, a3, a7);
    goto loc_008A686C;
loc_008A6CAF:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x324E6F49ULL), a7);
    v_stack_p50 = result;
    if (result == 0) goto loc_008A6D7C;
    a4 = 0;
    goto loc_008A67F2;
loc_008A6CE5:
    if (((unsigned int)(v_stack_p108)) == 0xC0000004ULL) goto loc_008A6832;
    goto loc_008A6B31;
loc_008A6CF6:
    v_rbx = (unsigned int)(0xC0000004ULL);
    if (((unsigned int)((unsigned int)(a5))) >= 16) { v_rbx = (unsigned int)((unsigned int)(0x80000005ULL)); }
    goto loc_008A6B31;
loc_008A6D18:
    v_rbx = v_stack_p98;
    if (((unsigned int)((unsigned int)(a5))) >= 16) { v_rbx = result; }
    v_stack_p48 = v_rbx;
    goto loc_008A68DC;
loc_008A6D32:
    goto loc_008A6B31;
loc_008A6D3C:
    result = ObfDereferenceObject(v_stack_pF0, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x324E6F49ULL), a4);
    goto loc_008A6A47;
loc_008A6D53:
    v_stack_p110 = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_008A6864;
loc_008A6D6B:
    goto loc_008A67FE;
loc_008A6D7C:
    goto loc_008A6B31;
loc_008A6D86:
    result = 0;
    goto loc_008A6BC8;
loc_008A6D96:
    result = (unsigned int)((result) + (2));
    v_stack_p110 = (unsigned int)(result);
    v_stack_p40 = (unsigned int)(result);
    goto loc_008A687A;
}
```

## 5. (Beta) C Style

```c
int64_t IopQueryNameInternal(int64_t Arg1, uint8_t Arg2, uint8_t Arg3, void *Arg4, uint32_t Arg5, void *Arg6, uint8_t Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint8_t v_stack_p10;
    uint8_t v_stack_p100;
    uint64_t v_stack_p108;
    uint32_t v_stack_p110;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pF0;
    uint32_t v_stack_pF8;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    Arg4 = 0;
    v_stack_mA8 = 0;
    v_stack_m98 = 0;
    v_stack_p10 = 0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    local_rdi = 16;
    if (((uint32_t)((uint32_t)(Arg5))) >= 16) { local_rdi = (uint32_t)((uint32_t)(Arg5)); }
    if (Arg7 == 1) goto loc_008A6CAF;
    local_rsi = local_rsp - 80;
    if (((uint32_t)((uint32_t)(Arg5))) >= 16) { local_rsi = 0; }
loc_008A67F2:
    if (Arg3 != 0) goto loc_008A6C12;
loc_008A67FE:
    v_stack_mC8 = 0;
    result = ObQueryNameStringMode(*(uint64_t *)(Arg1 + 0x8), local_rsi, (uint32_t)((uint32_t)(local_rdi)), v_stack_mA8);
    result = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_mA8));
loc_008A6822:
    if (sign_flag) goto loc_008A6CE5;
    if (0 == 0) goto loc_008A6B79;
loc_008A6832:
    local_r13 = (Arg4) + (16);
    v_stack_m88 = local_r13;
    if ((uint8_t)(v_stack_p18) != 0) goto loc_008A6BB5;
loc_008A684B:
    if (Arg7 == 1) goto loc_008A6C47;
loc_008A685C:
loc_008A6864:
loc_008A686C:
    if (v_stack_p10 != 0) goto loc_008A6D96;
loc_008A687A:
    Arg2 = 0;
    v_stack_p10 = 0;
    if (((uint32_t)((uint32_t)(Arg5))) < 16) goto loc_008A6B9D;
    if (((uint32_t)((uint32_t)(Arg5))) > ((uint32_t)(local_rdi))) goto loc_008A6B9D;
    *(uint64_t *)(v_stack_p20 + 0x8) = local_r13;
    goto loc_008A68A7;
loc_008A68A7:
    local_r13 = (local_r13) + (*(uint16_t *)(local_rsi));
    v_stack_m88 = local_r13;
loc_008A68B9:
    if (Arg7 != 1) goto loc_008A6B56;
    v_stack_mA0 = 0;
    if (0 == 0) {
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)((uint32_t)(Arg5))));
        local_rdi = (uint32_t)((local_rdi) + (4));
    }
    v_stack_p28 = (uint32_t)(local_rdi);
    if (Arg7 == 1) goto loc_008A6A15;
loc_008A68ED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x50)))) & (2)) == 0) goto loc_008A6A1D;
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m78 = v_xmm0;
    result = ObfReferenceObject(v_stack_p8, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_mA8);
    Arg3 = 0;
    result = KeInitializeEvent(v_stack_m68, Arg3 + 1, Arg3, v_stack_mA8);
    result = IoGetRelatedDeviceObject(v_stack_p8, Arg3 + 1, Arg3, v_stack_mA8);
    v_stack_m80 = result;
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, v_stack_mA8);
    if (result == 0) goto loc_008A6D3C;
    *(uint64_t *)(result + 0xC0) = v_stack_p8;
    *(uint64_t *)(result + 0x98) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(result + 0x40) = 0;
    *(uint64_t *)(result + 0x50) = v_stack_m68;
    *(uint32_t *)(result + 0x10) = 0x1004ULL;
    *(uint64_t *)(result + 0x48) = v_stack_m78;
    local_r13 = 0;
    *(uint64_t *)(result + 0x58) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 5;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_p8;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(Arg5));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = 9;
    result = IopQueueThreadIrp(result, v_stack_p8, Arg3, v_stack_mA8);
    result = IofCallDriver(v_stack_m80, result, Arg3, v_stack_mA8);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 259) {
        v_stack_mC8 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_m68;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m78;
    }
    v_stack_mA8 = (uint32_t)((uint32_t)(v_stack_m70));
    goto loc_008A6A47;
loc_008A6A15:
    if ((uint8_t)(Arg1) != 0) goto loc_008A68ED;
loc_008A6A1D:
    v_stack_mB8 = 1;
    v_stack_mC0 = v_stack_mA8;
    v_stack_mC8 = local_rbx;
    result = IopQueryXxxInformation(v_stack_p8, 9, (uint32_t)((uint32_t)(result)), Arg7);
loc_008A6A47:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (0xC0000000ULL));
    if (((uint32_t)(result)) != 0xC0000000ULL) goto loc_008A6A8D;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 1073741822)) > 14) goto loc_008A6B31;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 1073741822)) >= 14) goto loc_008A6B31;
    v_stack_mA8 = 4;
    Arg1 = 0;
    *(uint32_t *)(v_stack_mA0) = 0;
    *(uint16_t *)(v_stack_mA0 + 0x4) = 92;
    goto loc_008A6AA1;
loc_008A6A8D:
    if (v_stack_mA8 < 4) {
        v_stack_mA8 = 4;
    }
    if (v_stack_p10 != 0) goto loc_008A6CF6;
    result = (uint32_t)(((uint32_t)(v_stack_mA8)) + (-4));
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0))));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0))))) { Arg3 = (uint32_t)(result); }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA0))) - ((uint32_t)(v_stack_p20)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(v_stack_m88)));
    v_stack_mA8 = (uint32_t)(Arg1);
    if ((*(uint16_t *)(v_stack_mA0 + 0x4)) != 92) goto loc_008A6D32;
    if (Arg7 == 1) goto loc_008A6AE6;
    *(uint32_t *)(v_stack_mA0) = (uint32_t)((uint32_t)(v_stack_m90));
    goto loc_008A6AF5;
loc_008A6AE6:
    Arg2 = (v_stack_mA0) + (4);
    result = memcpy(v_stack_m88, Arg2, (uint32_t)(Arg3), Arg7);
loc_008A6AF5:
    v_stack_m88 = (uint32_t)(Arg3) + v_stack_m88 * 1;
    result = 0;
    *(uint16_t *)((uint32_t)(Arg3) + v_stack_m88 * 1) = 0;
    result = (uint32_t)(((uint32_t)(v_stack_mA8)) + (2));
    v_stack_mA8 = (uint32_t)(result);
    *(uint32_t *)(arg6) = (uint32_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(Arg3) + v_stack_m88 * 1) - ((uint32_t)(v_stack_p20)));
    *(uint16_t *)(v_stack_p20) = (uint16_t)(Arg1 - 16);
    Arg1 = (uint16_t)((Arg1) - (14));
    *(uint16_t *)(v_stack_p20 + 0x2) = (uint16_t)(Arg1);
    goto loc_008A6B31;
loc_008A6B31:
    result = Arg1 - 16;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(Arg3), Arg7);
    }
    local_rsp = (local_rsp) + (176);
    return 0;
loc_008A6B56:
    if (0 != 0) goto loc_008A6D18;
    v_stack_p58 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 - 0x4)));
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(v_stack_m88 - 4)));
    local_rdi = (uint32_t)((local_rdi) + (-2));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(v_stack_p20)));
    v_stack_p48 = v_stack_m88 - 4;
    goto loc_008A68DC;
loc_008A6B79:
    local_rbx = (uint8_t)((uint32_t)(v_stack_pF8));
    if ((*(uint16_t *)(v_stack_p20)) == 0) { local_rbx = 1; }
    v_stack_pF8 = (uint32_t)(local_rbx);
    goto loc_008A6832;
loc_008A6B9D:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 - 0x4)));
    v_stack_pF8 = 1;
    goto loc_008A68B9;
loc_008A6BB5:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m88 - 0x4))) == 0) goto loc_008A684B;
    if (((uint32_t)(local_rdi)) < 1) goto loc_008A6D86;
loc_008A6BC8:
    result = memcpy(v_stack_m88, *(uint64_t *)(v_stack_p20 + 0x8), (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p20))), Arg7);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pF0 + 0x8) + 0x34)))) & (16)) != 0) goto loc_008A6D53;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p20 + 0x8), Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p20))), Arg7);
    v_stack_p110 = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_008A685C;
loc_008A6C12:
    result = IoVolumeDeviceToDosName(v_stack_p100, v_stack_p20, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p20))), Arg7);
    Arg2 = (uint32_t)((*(uint16_t *)(v_stack_p20)) + (18));
    v_stack_p40 = Arg2;
    v_stack_p110 = Arg2;
    if (sign_flag) goto loc_008A6D6B;
    goto loc_008A6822;
loc_008A6C47:
    if (((uint32_t)((uint32_t)(Arg5))) < 16) goto loc_008A685C;
    if (1 > ((uint32_t)(local_rdi))) goto loc_008A685C;
    *(uint16_t *)(v_stack_p108) = (uint16_t)(*(uint16_t *)(v_stack_p20));
    *(uint16_t *)(v_stack_p108 + 0x2) = (uint16_t)(*(uint16_t *)(v_stack_p20 + 0x2));
    Arg3 = ((uint32_t)(Arg5)) - (16);
    result = memcpy(v_stack_m88, v_stack_p20 + 16, Arg3, Arg7);
    goto loc_008A686C;
loc_008A6CAF:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x324E6F49ULL), Arg7);
    v_stack_p50 = result;
    if (result == 0) goto loc_008A6D7C;
    Arg4 = 0;
    goto loc_008A67F2;
loc_008A6CE5:
    if (((uint32_t)(v_stack_p108)) == 0xC0000004ULL) goto loc_008A6832;
    goto loc_008A6B31;
loc_008A6CF6:
    local_rbx = (uint32_t)(0xC0000004ULL);
    if (((uint32_t)((uint32_t)(Arg5))) >= 16) { local_rbx = (uint32_t)((uint32_t)(0x80000005ULL)); }
    goto loc_008A6B31;
loc_008A6D18:
    local_rbx = v_stack_p98;
    if (((uint32_t)((uint32_t)(Arg5))) >= 16) { local_rbx = result; }
    v_stack_p48 = local_rbx;
    goto loc_008A68DC;
loc_008A6D32:
    goto loc_008A6B31;
loc_008A6D3C:
    result = ObfDereferenceObject(v_stack_pF0, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x324E6F49ULL), Arg4);
    goto loc_008A6A47;
loc_008A6D53:
    v_stack_p110 = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_008A6864;
loc_008A6D6B:
    goto loc_008A67FE;
loc_008A6D7C:
    goto loc_008A6B31;
loc_008A6D86:
    result = 0;
    goto loc_008A6BC8;
loc_008A6D96:
    result = (uint32_t)((result) + (2));
    v_stack_p110 = (uint32_t)(result);
    v_stack_p40 = (uint32_t)(result);
    goto loc_008A687A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x4` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A6770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
