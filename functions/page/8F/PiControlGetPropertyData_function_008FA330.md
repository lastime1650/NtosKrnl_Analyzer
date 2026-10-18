# PiControlGetPropertyData

- RVA: `0x008FA330`–`0x008FA716` (길이 `998` bytes)
- VA: `0x00000001408FA330`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00087CFC`
- 디코드: `253`개 명령, `998/998` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008FA3BD` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008FA3CB` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x008FA3DA` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x008FA456` → [IoGetDeviceProperty](IoGetDeviceProperty_function_008FA720.md) (function, `0x008FA720`)
- `0x008FA475` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008FA47A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008FA48C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008FA497` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x008FA4CB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008FA4F6` → [PiControlCopyUserModeCallersBuffer](../8E/PiControlCopyUserModeCallersBuffer_function_008E4720.md) (function, `0x008E4720`)
- `0x008FA50B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008FA53E` → [PiControlCopyUserModeCallersBuffer](../8E/PiControlCopyUserModeCallersBuffer_function_008E4720.md) (function, `0x008E4720`)
- `0x008FA5D6` → [PiControlGetDevicePowerData](../A7/PiControlGetDevicePowerData_function_00A7A808.md) (function, `0x00A7A808`)
- `0x008FA617` → [PiControlGetDeviceStack](../A6/PiControlGetDeviceStack_function_00A6FE34.md) (function, `0x00A6FE34`)
- `0x008FA62F` → [PpHotSwapGetDevnodeRemovalPolicy](PpHotSwapGetDevnodeRemovalPolicy_function_008FB1B4.md) (function, `0x008FB1B4`)
- `0x008FA66E` → [PnpGetDeviceDependencyList](../A0/PnpGetDeviceDependencyList_function_00A05090.md) (function, `0x00A05090`)
- `0x008FA6C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008FA3AB` → RVA `0x00F8C560` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008FA3BD` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008FA3DA` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x008FA475` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008FA47A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008FA48C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008FA497` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x008FA4CB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008FA50B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008FA6C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008FA5A6` → [sub_00B1F3CA](../B1/Unknown_function_00B1F3CA.md) (`tail-transfer`)
  - `0x008FA6F5` → [sub_00B1F3CA + 0x65](../B1/Unknown_function_00B1F3CA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008FA330  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008FA335  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008FA33A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008FA33F  55                              push rbp
008FA340  41 54                           push r12
008FA342  41 55                           push r13
008FA344  41 56                           push r14
008FA346  41 57                           push r15
008FA348  48 8B EC                        mov rbp, rsp
008FA34B  48 83 EC 50                     sub rsp, 0x50
008FA34F  0F B7 0A                        movzx ecx, word ptr [rdx]
008FA352  33 FF                           xor edi, edi
008FA354  83 65 38 00                     and dword ptr [rbp + 0x38], 0
008FA358  0F B7 C1                        movzx eax, cx
008FA35B  4C 8B FA                        mov r15, rdx
008FA35E  0F 57 C0                        xorps xmm0, xmm0
008FA361  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
008FA365  44 8D 77 01                     lea r14d, [rdi + 1]
008FA369  66 89 4D F2                     mov word ptr [rbp - 0xe], cx
008FA36D  66 41 2B C6                     sub ax, r14w
008FA371  66 89 4D F0                     mov word ptr [rbp - 0x10], cx
008FA375  BA 8F 01 00 00                  mov edx, 0x18f
008FA37A  45 8A E1                        mov r12b, r9b
008FA37D  66 3B C2                        cmp ax, dx
008FA380  0F 87 76 02 00 00               ja 0x1408fa5fc
008FA386  41 84 CE                        test r14b, cl
008FA389  0F 85 6D 02 00 00               jne 0x1408fa5fc
008FA38F  49 8B 5F 08                     mov rbx, qword ptr [r15 + 8]
008FA393  8B F1                           mov esi, ecx
008FA395  45 84 C9                        test r9b, r9b
008FA398  0F 85 1F 01 00 00               jne 0x1408fa4bd
008FA39E  48 89 5D F8                     mov qword ptr [rbp - 8], rbx
008FA3A2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008FA3AB  48 8D 0D AE 21 69 00            lea rcx, [rip + 0x6921ae]
008FA3B2  41 8A D6                        mov dl, r14b
008FA3B5  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008FA3BC  90                              nop
008FA3BD  E8 FE 77 91 FF                  call 0x140211bc0
008FA3C2  BA 50 6E 70 43                  mov edx, 0x43706e50
008FA3C7  48 8D 4D F0                     lea rcx, [rbp - 0x10]
008FA3CB  E8 C0 D0 FE FF                  call 0x1408e7490
008FA3D0  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
008FA3D4  41 8A CC                        mov cl, r12b
008FA3D7  4C 8B E8                        mov r13, rax
008FA3DA  E8 B1 E5 B4 FF                  call 0x140448990
008FA3DF  4D 85 ED                        test r13, r13
008FA3E2  0F 84 0A 02 00 00               je 0x1408fa5f2
008FA3E8  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
008FA3EF  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
008FA3F3  48 85 DB                        test rbx, rbx
008FA3F6  0F 84 F6 01 00 00               je 0x1408fa5f2
008FA3FC  8B 83 2C 01 00 00               mov eax, dword ptr [rbx + 0x12c]
008FA402  2D 15 03 00 00                  sub eax, 0x315
008FA407  41 3B C6                        cmp eax, r14d
008FA40A  0F 86 FC 02 00 00               jbe 0x1408fa70c
008FA410  49 8D 77 20                     lea rsi, [r15 + 0x20]
008FA414  44 8B 36                        mov r14d, dword ptr [rsi]
008FA417  45 85 F6                        test r14d, r14d
008FA41A  74 0D                           je 0x1408fa429
008FA41C  45 84 E4                        test r12b, r12b
008FA41F  0F 85 90 02 00 00               jne 0x1408fa6b5
008FA425  49 8B 7F 18                     mov rdi, qword ptr [r15 + 0x18]
008FA429  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
008FA42D  83 F8 08                        cmp eax, 8
008FA430  0F 87 32 01 00 00               ja 0x1408fa568
008FA436  0F 84 AC 02 00 00               je 0x1408fa6e8
008FA43C  83 E8 01                        sub eax, 1
008FA43F  0F 85 08 01 00 00               jne 0x1408fa54d
008FA445  8D 50 0B                        lea edx, [rax + 0xb]
008FA448  4C 8B CF                        mov r9, rdi
008FA44B  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008FA450  45 8B C6                        mov r8d, r14d
008FA453  49 8B CD                        mov rcx, r13
008FA456  E8 C5 02 00 00                  call 0x1408fa720
008FA45B  8B D8                           mov ebx, eax
008FA45D  85 DB                           test ebx, ebx
008FA45F  78 0D                           js 0x1408fa46e
008FA461  45 84 E4                        test r12b, r12b
008FA464  0F 85 A8 00 00 00               jne 0x1408fa512
008FA46A  49 89 7F 18                     mov qword ptr [r15 + 0x18], rdi
008FA46E  48 8D 0D EB 20 69 00            lea rcx, [rip + 0x6920eb]
008FA475  E8 96 55 96 FF                  call 0x14025fa10
008FA47A  E8 31 34 96 FF                  call 0x14025d8b0
008FA47F  4D 85 ED                        test r13, r13
008FA482  74 0D                           je 0x1408fa491
008FA484  BA 50 6E 70 43                  mov edx, 0x43706e50
008FA489  49 8B CD                        mov rcx, r13
008FA48C  E8 4F D4 9F FF                  call 0x1402f78e0
008FA491  48 8B D7                        mov rdx, rdi
008FA494  41 8A CC                        mov cl, r12b
008FA497  E8 F4 E4 B4 FF                  call 0x140448990
008FA49C  8B C3                           mov eax, ebx
008FA49E  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
008FA4A3  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008FA4A7  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
008FA4AB  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008FA4AF  49 8B E3                        mov rsp, r11
008FA4B2  41 5F                           pop r15
008FA4B4  41 5E                           pop r14
008FA4B6  41 5D                           pop r13
008FA4B8  41 5C                           pop r12
008FA4BA  5D                              pop rbp
008FA4BB  C3                              ret
008FA4BC  CC                              int3
008FA4BD  48 8B D6                        mov rdx, rsi
008FA4C0  B9 01 01 00 00                  mov ecx, 0x101
008FA4C5  41 B8 50 70 20 20               mov r8d, 0x20207050
008FA4CB  E8 20 7C 28 00                  call 0x140b820f0
008FA4D0  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008FA4D4  48 85 C0                        test rax, rax
008FA4D7  0F 84 CE 01 00 00               je 0x1408fa6ab
008FA4DD  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
008FA4E2  41 B9 02 00 00 00               mov r9d, 2
008FA4E8  44 8B C6                        mov r8d, esi
008FA4EB  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
008FA4F0  48 8B D3                        mov rdx, rbx
008FA4F3  48 8B C8                        mov rcx, rax
008FA4F6  E8 25 A2 FE FF                  call 0x1408e4720
008FA4FB  8B D8                           mov ebx, eax
008FA4FD  85 C0                           test eax, eax
008FA4FF  0F 89 9D FE FF FF               jns 0x1408fa3a2
008FA505  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
008FA509  33 D2                           xor edx, edx
008FA50B  E8 60 83 28 00                  call 0x140b82870
008FA510  EB 8A                           jmp 0x1408fa49c
008FA512  45 85 F6                        test r14d, r14d
008FA515  0F 84 E7 01 00 00               je 0x1408fa702
008FA51B  49 8B 4F 18                     mov rcx, qword ptr [r15 + 0x18]
008FA51F  48 85 C9                        test rcx, rcx
008FA522  0F 84 46 FF FF FF               je 0x1408fa46e
008FA528  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
008FA52D  41 B9 01 00 00 00               mov r9d, 1
008FA533  45 8B C6                        mov r8d, r14d
008FA536  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
008FA53B  48 8B D7                        mov rdx, rdi
008FA53E  E8 DD A1 FE FF                  call 0x1408e4720
008FA543  85 C0                           test eax, eax
008FA545  0F 48 D8                        cmovs ebx, eax
008FA548  E9 21 FF FF FF                  jmp 0x1408fa46e
008FA54D  83 E8 01                        sub eax, 1
008FA550  0F 84 88 01 00 00               je 0x1408fa6de
008FA556  83 E8 01                        sub eax, 1
008FA559  74 59                           je 0x1408fa5b4
008FA55B  83 E8 01                        sub eax, 1
008FA55E  75 3E                           jne 0x1408fa59e
008FA560  8D 50 0E                        lea edx, [rax + 0xe]
008FA563  E9 E0 FE FF FF                  jmp 0x1408fa448
008FA568  83 E8 0A                        sub eax, 0xa
008FA56B  0F 84 B0 00 00 00               je 0x1408fa621
008FA571  83 E8 01                        sub eax, 1
008FA574  74 48                           je 0x1408fa5be
008FA576  83 E8 02                        sub eax, 2
008FA579  0F 85 87 00 00 00               jne 0x1408fa606
008FA57F  C7 06 04 00 00 00               mov dword ptr [rsi], 4
008FA585  41 83 FE 04                     cmp r14d, 4
008FA589  0F 82 B2 00 00 00               jb 0x1408fa641
008FA58F  8B 83 AC 02 00 00               mov eax, dword ptr [rbx + 0x2ac]
008FA595  33 DB                           xor ebx, ebx
008FA597  89 07                           mov dword ptr [rdi], eax
008FA599  E9 C3 FE FF FF                  jmp 0x1408fa461
008FA59E  83 E8 01                        sub eax, 1
008FA5A1  74 25                           je 0x1408fa5c8
008FA5A3  83 E8 01                        sub eax, 1
008FA5A6  0F 85 1E 4E 22 00               jne 0x140b1f3ca
008FA5AC  8D 50 13                        lea edx, [rax + 0x13]
008FA5AF  E9 94 FE FF FF                  jmp 0x1408fa448
008FA5B4  BA 0D 00 00 00                  mov edx, 0xd
008FA5B9  E9 8A FE FF FF                  jmp 0x1408fa448
008FA5BE  BA 12 00 00 00                  mov edx, 0x12
008FA5C3  E9 80 FE FF FF                  jmp 0x1408fa448
008FA5C8  4C 8B CF                        mov r9, rdi
008FA5CB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008FA5D0  45 8B C6                        mov r8d, r14d
008FA5D3  48 8B CB                        mov rcx, rbx
008FA5D6  E8 2D 02 18 00                  call 0x140a7a808
008FA5DB  8B D8                           mov ebx, eax
008FA5DD  3D 05 00 00 80                  cmp eax, 0x80000005
008FA5E2  0F 85 75 FE FF FF               jne 0x1408fa45d
008FA5E8  BB 23 00 00 C0                  mov ebx, 0xc0000023
008FA5ED  E9 6B FE FF FF                  jmp 0x1408fa45d
008FA5F2  BB 0E 00 00 C0                  mov ebx, 0xc000000e
008FA5F7  E9 72 FE FF FF                  jmp 0x1408fa46e
008FA5FC  B8 0D 00 00 C0                  mov eax, 0xc000000d
008FA601  E9 98 FE FF FF                  jmp 0x1408fa49e
008FA606  83 E8 01                        sub eax, 1
008FA609  75 47                           jne 0x1408fa652
008FA60B  4C 8B CE                        mov r9, rsi
008FA60E  4C 8B C7                        mov r8, rdi
008FA611  41 8B D6                        mov edx, r14d
008FA614  48 8B CB                        mov rcx, rbx
008FA617  E8 18 58 17 00                  call 0x140a6fe34
008FA61C  E9 3A FE FF FF                  jmp 0x1408fa45b
008FA621  41 83 FE 04                     cmp r14d, 4
008FA625  72 24                           jb 0x1408fa64b
008FA627  4C 8B C7                        mov r8, rdi
008FA62A  33 D2                           xor edx, edx
008FA62C  48 8B CB                        mov rcx, rbx
008FA62F  E8 80 0B 00 00                  call 0x1408fb1b4
008FA634  33 DB                           xor ebx, ebx
008FA636  C7 06 04 00 00 00               mov dword ptr [rsi], 4
008FA63C  E9 1C FE FF FF                  jmp 0x1408fa45d
008FA641  BB 23 00 00 C0                  mov ebx, 0xc0000023
008FA646  E9 23 FE FF FF                  jmp 0x1408fa46e
008FA64B  BB 23 00 00 C0                  mov ebx, 0xc0000023
008FA650  EB E4                           jmp 0x1408fa636
008FA652  83 E8 01                        sub eax, 1
008FA655  0F 85 97 00 00 00               jne 0x1408fa6f2
008FA65B  33 D2                           xor edx, edx
008FA65D  45 8B CE                        mov r9d, r14d
008FA660  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008FA665  41 D1 E9                        shr r9d, 1
008FA668  4C 8B C7                        mov r8, rdi
008FA66B  48 8B CB                        mov rcx, rbx
008FA66E  E8 1D AA 10 00                  call 0x140a05090
008FA673  8B D8                           mov ebx, eax
008FA675  B9 00 00 00 80                  mov ecx, 0x80000000
008FA67A  8B 06                           mov eax, dword ptr [rsi]
008FA67C  03 C0                           add eax, eax
008FA67E  8B D0                           mov edx, eax
008FA680  89 06                           mov dword ptr [rsi], eax
008FA682  8D 04 0B                        lea eax, [rbx + rcx]
008FA685  85 C1                           test ecx, eax
008FA687  75 0C                           jne 0x1408fa695
008FA689  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008FA68F  0F 85 D9 FD FF FF               jne 0x1408fa46e
008FA695  83 FA 02                        cmp edx, 2
008FA698  0F 87 BF FD FF FF               ja 0x1408fa45d
008FA69E  83 26 00                        and dword ptr [rsi], 0
008FA6A1  BB 34 00 00 C0                  mov ebx, 0xc0000034
008FA6A6  E9 B2 FD FF FF                  jmp 0x1408fa45d
008FA6AB  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008FA6B0  E9 E7 FD FF FF                  jmp 0x1408fa49c
008FA6B5  49 8B D6                        mov rdx, r14
008FA6B8  B9 01 01 00 00                  mov ecx, 0x101
008FA6BD  41 B8 50 70 20 20               mov r8d, 0x20207050
008FA6C3  E8 28 7A 28 00                  call 0x140b820f0
008FA6C8  48 8B F8                        mov rdi, rax
008FA6CB  48 85 C0                        test rax, rax
008FA6CE  0F 85 55 FD FF FF               jne 0x1408fa429
008FA6D4  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008FA6D9  E9 90 FD FF FF                  jmp 0x1408fa46e
008FA6DE  BA 0C 00 00 00                  mov edx, 0xc
008FA6E3  E9 60 FD FF FF                  jmp 0x1408fa448
008FA6E8  BA 10 00 00 00                  mov edx, 0x10
008FA6ED  E9 56 FD FF FF                  jmp 0x1408fa448
008FA6F2  83 F8 01                        cmp eax, 1
008FA6F5  0F 85 34 4D 22 00               jne 0x140b1f42f
008FA6FB  8B D0                           mov edx, eax
008FA6FD  E9 5B FF FF FF                  jmp 0x1408fa65d
008FA702  49 83 67 18 00                  and qword ptr [r15 + 0x18], 0
008FA707  E9 62 FD FF FF                  jmp 0x1408fa46e
008FA70C  BB 56 00 00 C0                  mov ebx, 0xc0000056
008FA711  E9 58 FD FF FF                  jmp 0x1408fa46e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiControlGetPropertyData(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int16 v_stack_m36;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (80);
    v_rdi = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m36 = (unsigned __int16)(*(unsigned __int16 *)(a2));
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) - ((unsigned __int16)(v_rdi + 1)));
    v_stack_m38 = (unsigned __int16)(*(unsigned __int16 *)(a2));
    if (((unsigned __int16)(result)) > 399) goto loc_008FA5FC;
    if ((((unsigned __int8)(v_rdi + 1)) & ((unsigned __int8)(*(unsigned __int16 *)(a2)))) != 0) goto loc_008FA5FC;
    if (a4 != 0) goto loc_008FA4BD;
    v_stack_m30 = *(unsigned __int64 *)(a2 + 8);
loc_008FA3A2:
    result = ExAcquireResourceSharedLite(v_rip + 6889902, (unsigned __int8)(v_rdi + 1), a3, a4);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_stack_m38, (unsigned int)(0x43706E50ULL), a3, a4);
    result = PiControlFreeUserModeCallersBuffer(a4, v_stack_m30, a3, a4);
    if (result == 0) goto loc_008FA5F2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) == 0) goto loc_008FA5F2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 300))) - (789));
    if (((unsigned int)(result)) <= ((unsigned int)(v_rdi + 1))) goto loc_008FA70C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32))) == 0) goto loc_008FA429;
    if (a4 != 0) goto loc_008FA6B5;
loc_008FA429:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) > 8) goto loc_008FA568;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) == 8) goto loc_008FA6E8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) - (1));
    if (condition_is_not_equal) goto loc_008FA54D;
loc_008FA448:
    v_stack_m58 = a2 + 32;
    result = IoGetDeviceProperty(result, result + 11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(a2 + 24));
loc_008FA45B:
loc_008FA45D:
    if (sign_flag) goto loc_008FA46E;
loc_008FA461:
    if (a4 != 0) goto loc_008FA512;
    *(unsigned __int64 *)(a2 + 24) = *(unsigned __int64 *)(a2 + 24);
loc_008FA46E:
    result = ExReleaseResourceLite(v_rip + 6889707, result + 11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(a2 + 24));
    result = KeLeaveCriticalRegion(v_rip + 6889707, result + 11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(a2 + 24));
    if (result != 0) {
        a2 = 0x43706E50ULL;
        a1 = result;
        result = ObfDereferenceObjectWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(a2 + 24));
    }
    result = PiControlFreeUserModeCallersBuffer(a4, *(unsigned __int64 *)(a2 + 24), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(a2 + 24));
loc_008FA49C:
loc_008FA49E:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008FA4BD:
    result = ExAllocatePool2(257, *(unsigned __int64 *)(v_stack_m28 + 64), (unsigned int)(0x20207050ULL), *(unsigned __int64 *)(a2 + 24));
    v_stack_m30 = result;
    if (result == 0) goto loc_008FA6AB;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    v_stack_m30 = a4;
    result = PiControlCopyUserModeCallersBuffer(result, *(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), 2);
    if (!sign_flag) goto loc_008FA3A2;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m30, a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), 2);
    goto loc_008FA49C;
loc_008FA512:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32))) == 0) goto loc_008FA702;
    if (*(unsigned __int64 *)(a2 + 24) == 0) goto loc_008FA46E;
    v_stack_m30 = a4;
    result = PiControlCopyUserModeCallersBuffer(*(unsigned __int64 *)(a2 + 24), *(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), 1);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (sign_flag) { v_rbx = (unsigned int)(result); }
    goto loc_008FA46E;
loc_008FA54D:
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008FA6DE;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008FA5B4;
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_008FA59E;
    goto loc_008FA448;
loc_008FA568:
    result = (unsigned int)((result) - (10));
    if (condition_is_equal) goto loc_008FA621;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008FA5BE;
    result = (unsigned int)((result) - (2));
    if (condition_is_not_equal) goto loc_008FA606;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64)) = 4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))) < 4) goto loc_008FA641;
    v_rbx = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 684)));
    goto loc_008FA461;
loc_008FA59E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 684))) - (1));
    if (condition_is_equal) goto loc_008FA5C8;
    result = (unsigned int)((result) - (1));
    goto loc_008FA448;
loc_008FA5B4:
    goto loc_008FA448;
loc_008FA5BE:
    goto loc_008FA448;
loc_008FA5C8:
    v_stack_m30 = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = PiControlGetDevicePowerData(0, 18, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(v_stack_m28 + 72));
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_008FA45D;
    goto loc_008FA45D;
loc_008FA5F2:
    goto loc_008FA46E;
loc_008FA5FC:
    goto loc_008FA49E;
loc_008FA606:
    result = (unsigned int)(((unsigned int)(0xC000000DULL)) - (1));
    if (condition_is_not_equal) goto loc_008FA652;
    result = PiControlGetDeviceStack((unsigned int)(0xC000000EULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))), *(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 64));
    goto loc_008FA45B;
loc_008FA621:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)))) < 4) goto loc_008FA64B;
    a2 = 0;
    result = PpHotSwapGetDevnodeRemovalPolicy((unsigned int)(0xC000000EULL), a2, *(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 64));
    v_rbx = 0;
loc_008FA636:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64)) = 4;
    goto loc_008FA45D;
loc_008FA641:
    goto loc_008FA46E;
loc_008FA64B:
    goto loc_008FA636;
loc_008FA652:
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_008FA6F2;
    a2 = 0;
loc_008FA65D:
    v_stack_m30 = *(unsigned __int64 *)(v_stack_m28 + 64);
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32))))) >> (1));
    result = PnpGetDeviceDependencyList((unsigned int)(0xC0000023ULL), a2, *(unsigned __int64 *)(v_stack_m28 + 72), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64))))));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64)) = (unsigned int)(result);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_008FA695;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_008FA46E;
loc_008FA695:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) > 2) goto loc_008FA45D;
    goto loc_008FA45D;
loc_008FA6AB:
    goto loc_008FA49C;
loc_008FA6B5:
    result = ExAllocatePool2(257, (unsigned int)(*(unsigned int *)(a2 + 32)), (unsigned int)(0x20207050ULL), a4);
    if (result != 0) goto loc_008FA429;
    goto loc_008FA46E;
loc_008FA6DE:
    goto loc_008FA448;
loc_008FA6E8:
    goto loc_008FA448;
loc_008FA6F2:
    goto loc_008FA65D;
loc_008FA702:
    goto loc_008FA46E;
loc_008FA70C:
    goto loc_008FA46E;
}
```

## 5. (Beta) C Style

```c
int64_t PiControlGetPropertyData(int64_t Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint16_t v_stack_m36;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (80);
    local_rdi = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m36 = (uint16_t)(*(uint16_t *)(arg2));
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2))) - ((uint16_t)(local_rdi + 1)));
    v_stack_m38 = (uint16_t)(*(uint16_t *)(arg2));
    if (((uint16_t)(result)) > 399) goto loc_008FA5FC;
    if ((((uint8_t)(local_rdi + 1)) & ((uint8_t)(*(uint16_t *)(arg2)))) != 0) goto loc_008FA5FC;
    if (Arg4 != 0) goto loc_008FA4BD;
    v_stack_m30 = *(uint64_t *)(arg2 + 0x8);
loc_008FA3A2:
    result = ExAcquireResourceSharedLite(v_rip + 6889902, (uint8_t)(local_rdi + 1), Arg3, Arg4);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_stack_m38, (uint32_t)(0x43706E50ULL), Arg3, Arg4);
    result = PiControlFreeUserModeCallersBuffer(Arg4, v_stack_m30, Arg3, Arg4);
    if (result == 0) goto loc_008FA5F2;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) == 0) goto loc_008FA5F2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x12C))) - (789));
    if (((uint32_t)(result)) <= ((uint32_t)(local_rdi + 1))) goto loc_008FA70C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))) == 0) goto loc_008FA429;
    if (Arg4 != 0) goto loc_008FA6B5;
loc_008FA429:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) > 8) goto loc_008FA568;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) == 8) goto loc_008FA6E8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) - (1));
    if (condition_is_not_equal) goto loc_008FA54D;
loc_008FA448:
    v_stack_m58 = Arg2 + 32;
    result = IoGetDeviceProperty(result, result + 11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(arg2 + 0x18));
loc_008FA45B:
loc_008FA45D:
    if (sign_flag) goto loc_008FA46E;
loc_008FA461:
    if (Arg4 != 0) goto loc_008FA512;
    *(uint64_t *)(arg2 + 0x18) = *(uint64_t *)(arg2 + 0x18);
loc_008FA46E:
    result = ExReleaseResourceLite(v_rip + 6889707, result + 11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(arg2 + 0x18));
    result = KeLeaveCriticalRegion(v_rip + 6889707, result + 11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(arg2 + 0x18));
    if (result != 0) {
        Arg2 = 0x43706E50ULL;
        Arg1 = result;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(arg2 + 0x18));
    }
    result = PiControlFreeUserModeCallersBuffer(Arg4, *(uint64_t *)(arg2 + 0x18), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(arg2 + 0x18));
loc_008FA49C:
loc_008FA49E:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008FA4BD:
    result = ExAllocatePool2(257, *(uint64_t *)(v_stack_m28 + 0x40), (uint32_t)(0x20207050ULL), *(uint64_t *)(arg2 + 0x18));
    v_stack_m30 = result;
    if (result == 0) goto loc_008FA6AB;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    v_stack_m30 = Arg4;
    result = PiControlCopyUserModeCallersBuffer(result, *(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), 2);
    if (!sign_flag) goto loc_008FA3A2;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m30, Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), 2);
    goto loc_008FA49C;
loc_008FA512:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))) == 0) goto loc_008FA702;
    if (*(uint64_t *)(arg2 + 0x18) == 0) goto loc_008FA46E;
    v_stack_m30 = Arg4;
    result = PiControlCopyUserModeCallersBuffer(*(uint64_t *)(arg2 + 0x18), *(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), 1);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (sign_flag) { local_rbx = (uint32_t)(result); }
    goto loc_008FA46E;
loc_008FA54D:
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008FA6DE;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008FA5B4;
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_008FA59E;
    goto loc_008FA448;
loc_008FA568:
    result = (uint32_t)((result) - (10));
    if (condition_is_equal) goto loc_008FA621;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008FA5BE;
    result = (uint32_t)((result) - (2));
    if (condition_is_not_equal) goto loc_008FA606;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40)) = 4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))) < 4) goto loc_008FA641;
    local_rbx = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x2AC)));
    goto loc_008FA461;
loc_008FA59E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x2AC))) - (1));
    if (condition_is_equal) goto loc_008FA5C8;
    result = (uint32_t)((result) - (1));
    goto loc_008FA448;
loc_008FA5B4:
    goto loc_008FA448;
loc_008FA5BE:
    goto loc_008FA448;
loc_008FA5C8:
    v_stack_m30 = *(uint64_t *)(v_stack_m28 + 0x40);
    result = PiControlGetDevicePowerData(0, 18, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(v_stack_m28 + 0x48));
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_008FA45D;
    goto loc_008FA45D;
loc_008FA5F2:
    goto loc_008FA46E;
loc_008FA5FC:
    goto loc_008FA49E;
loc_008FA606:
    result = (uint32_t)(((uint32_t)(0xC000000DULL)) - (1));
    if (condition_is_not_equal) goto loc_008FA652;
    result = PiControlGetDeviceStack((uint32_t)(0xC000000EULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))), *(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x40));
    goto loc_008FA45B;
loc_008FA621:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))) < 4) goto loc_008FA64B;
    Arg2 = 0;
    result = PpHotSwapGetDevnodeRemovalPolicy((uint32_t)(0xC000000EULL), Arg2, *(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x40));
    local_rbx = 0;
loc_008FA636:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40)) = 4;
    goto loc_008FA45D;
loc_008FA641:
    goto loc_008FA46E;
loc_008FA64B:
    goto loc_008FA636;
loc_008FA652:
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_008FA6F2;
    Arg2 = 0;
loc_008FA65D:
    v_stack_m30 = *(uint64_t *)(v_stack_m28 + 0x40);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))))) >> (1));
    result = PnpGetDeviceDependencyList((uint32_t)(0xC0000023ULL), Arg2, *(uint64_t *)(v_stack_m28 + 0x48), Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40)) = (uint32_t)(result);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_008FA695;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_008FA46E;
loc_008FA695:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) > 2) goto loc_008FA45D;
    goto loc_008FA45D;
loc_008FA6AB:
    goto loc_008FA49C;
loc_008FA6B5:
    result = ExAllocatePool2(257, (uint32_t)(*(uint32_t *)(arg2 + 0x20)), (uint32_t)(0x20207050ULL), Arg4);
    if (result != 0) goto loc_008FA429;
    goto loc_008FA46E;
loc_008FA6DE:
    goto loc_008FA448;
loc_008FA6E8:
    goto loc_008FA448;
loc_008FA6F2:
    goto loc_008FA65D;
loc_008FA702:
    goto loc_008FA46E;
loc_008FA70C:
    goto loc_008FA46E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FA330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
