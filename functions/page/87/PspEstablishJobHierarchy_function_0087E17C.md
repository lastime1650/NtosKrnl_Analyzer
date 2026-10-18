# PspEstablishJobHierarchy

- RVA: `0x0087E17C`–`0x0087E65A` (길이 `1,246` bytes)
- VA: `0x000000014087E17C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007C018`
- 디코드: `284`개 명령, `1,246/1,246` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0087E1BE` → [PspBindProcessSessionToJob](PspBindProcessSessionToJob_function_0087E660.md) (function, `0x0087E660`)
- `0x0087E1D1` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0087E1DC` → [MmLinkJobProcess](../88/MmLinkJobProcess_function_00887C48.md) (function, `0x00887C48`)
- `0x0087E2A9` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0087E2D6` → [PspBindProcessSessionToJob](PspBindProcessSessionToJob_function_0087E660.md) (function, `0x0087E660`)
- `0x0087E2E9` → [PspUnlinkJobProcess](PspUnlinkJobProcess_function_0087D404.md) (function, `0x0087D404`)
- `0x0087E2F4` → [MmLinkJobProcess](../88/MmLinkJobProcess_function_00887C48.md) (function, `0x00887C48`)
- `0x0087E301` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0087E30E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0087E34A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087E3B6` → [PspSetEffectiveJobLimits](PspSetEffectiveJobLimits_function_0087E738.md) (function, `0x0087E738`)
- `0x0087E40D` → [PspUpdateJobEffectivePriorityLimits](PspUpdateJobEffectivePriorityLimits_function_0087EAD4.md) (function, `0x0087EAD4`)
- `0x0087E481` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x0087E4B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087E4D6` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (function, `0x0049521C`)
- `0x0087E4F0` → [PspSetEffectiveRateControlJob](../78/PspSetEffectiveRateControlJob_function_00785498.md) (function, `0x00785498`)
- `0x0087E50F` → [PspUnlinkJobProcess](PspUnlinkJobProcess_function_0087D404.md) (function, `0x0087D404`)
- `0x0087E51A` → [MmLinkJobProcess](../88/MmLinkJobProcess_function_00887C48.md) (function, `0x00887C48`)
- `0x0087E547` → [KeRemoveSchedulingGroup](../../text/4A/KeRemoveSchedulingGroup_function_004AD328.md) (function, `0x004AD328`)
- `0x0087E56F` → [KeInsertSchedulingGroup](../../text/46/KeInsertSchedulingGroup_function_0046D324.md) (function, `0x0046D324`)
- `0x0087E59A` → [PspAddSchedulingGroupToJobChain](../99/PspAddSchedulingGroupToJobChain_function_0099DE5C.md) (function, `0x0099DE5C`)
- `0x0087E5B6` → [KeInsertSchedulingGroup](../../text/46/KeInsertSchedulingGroup_function_0046D324.md) (function, `0x0046D324`)
- `0x0087E5DB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0087E619` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (function, `0x0049521C`)
- `0x0087E62D` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (function, `0x0049521C`)
- `0x0087E63A` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x0087E650` → [PspEstablishDfssHierarchy](../78/PspEstablishDfssHierarchy_function_00784EF0.md) (function, `0x00784EF0`)

### Direct callers
- [PspImplicitAssignProcessToJob](PspImplicitAssignProcessToJob_function_0087D584.md) at `0x0087D663`
- [PspAssignProcessToJob](../A2/PspAssignProcessToJob_function_00A23370.md) at `0x00A2365B`

### Static image references
- `0x0087E207` → RVA `0x00FC6ABE` (`ALMOSTRO`; read)
- `0x0087E45A` → RVA `0x00A7E540` (`PspSetJobIoAttributionJobPreCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0087E1D1` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0087E2A9` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0087E301` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0087E30E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0087E34A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087E4B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087E4D6` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (`PAGE` → `.text`)
  - `0x0087E547` → [KeRemoveSchedulingGroup](../../text/4A/KeRemoveSchedulingGroup_function_004AD328.md) (`PAGE` → `.text`)
  - `0x0087E56F` → [KeInsertSchedulingGroup](../../text/46/KeInsertSchedulingGroup_function_0046D324.md) (`PAGE` → `.text`)
  - `0x0087E5B6` → [KeInsertSchedulingGroup](../../text/46/KeInsertSchedulingGroup_function_0046D324.md) (`PAGE` → `.text`)
  - `0x0087E5DB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0087E619` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (`PAGE` → `.text`)
  - `0x0087E62D` → [IoSetDiskIoAttributionOnProcess](../../text/49/IoSetDiskIoAttributionOnProcess_function_0049521C.md) (`PAGE` → `.text`)
  - `0x0087E63A` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0087E57C` → [sub_00B18AB2](../B1/Unknown_function_00B18AB2.md) (`tail-transfer`)
  - `0x0087E5D1` → [sub_00B18AB2 + 0xE](../B1/Unknown_function_00B18AB2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0087E17C  4C 8B DC                        mov r11, rsp
0087E17F  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0087E183  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0087E187  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0087E18B  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0087E18F  41 55                           push r13
0087E191  41 56                           push r14
0087E193  41 57                           push r15
0087E195  48 83 EC 50                     sub rsp, 0x50
0087E199  48 8B D9                        mov rbx, rcx
0087E19C  33 C0                           xor eax, eax
0087E19E  41 8B C9                        mov ecx, r9d
0087E1A1  0F 57 C0                        xorps xmm0, xmm0
0087E1A4  45 8B E9                        mov r13d, r9d
0087E1A7  49 8B F8                        mov rdi, r8
0087E1AA  48 8B EA                        mov rbp, rdx
0087E1AD  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0087E1B2  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0087E1B6  83 E9 01                        sub ecx, 1
0087E1B9  75 7B                           jne 0x14087e236
0087E1BB  48 8B CB                        mov rcx, rbx
0087E1BE  E8 9D 04 00 00                  call 0x14087e660
0087E1C3  8B F0                           mov esi, eax
0087E1C5  85 C0                           test eax, eax
0087E1C7  78 18                           js 0x14087e1e1
0087E1C9  BA 50 73 50 73                  mov edx, 0x73507350
0087E1CE  48 8B CB                        mov rcx, rbx
0087E1D1  E8 3A 25 99 FF                  call 0x140210710
0087E1D6  48 8B D5                        mov rdx, rbp
0087E1D9  48 8B CB                        mov rcx, rbx
0087E1DC  E8 67 9A 00 00                  call 0x140887c48
0087E1E1  83 BB 2C 06 00 00 00            cmp dword ptr [rbx + 0x62c], 0
0087E1E8  48 8B 8B 30 06 00 00            mov rcx, qword ptr [rbx + 0x630]
0087E1EF  0F 85 35 04 00 00               jne 0x14087e62a
0087E1F5  48 85 C9                        test rcx, rcx
0087E1F8  0F 85 25 04 00 00               jne 0x14087e623
0087E1FE  48 85 ED                        test rbp, rbp
0087E201  74 11                           je 0x14087e214
0087E203  85 F6                           test esi, esi
0087E205  78 0D                           js 0x14087e214
0087E207  80 3D B0 88 74 00 00            cmp byte ptr [rip + 0x7488b0], 0
0087E20E  0F 85 23 04 00 00               jne 0x14087e637
0087E214  8B C6                           mov eax, esi
0087E216  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0087E21B  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
0087E21F  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
0087E223  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
0087E227  49 8B 7B 38                     mov rdi, qword ptr [r11 + 0x38]
0087E22B  49 8B E3                        mov rsp, r11
0087E22E  41 5F                           pop r15
0087E230  41 5E                           pop r14
0087E232  41 5D                           pop r13
0087E234  C3                              ret
0087E235  CC                              int3
0087E236  83 E9 01                        sub ecx, 1
0087E239  0F 84 F1 00 00 00               je 0x14087e330
0087E23F  83 E9 01                        sub ecx, 1
0087E242  0F 84 9E 00 00 00               je 0x14087e2e6
0087E248  83 E9 01                        sub ecx, 1
0087E24B  74 09                           je 0x14087e256
0087E24D  83 E9 01                        sub ecx, 1
0087E250  0F 85 23 03 00 00               jne 0x14087e579
0087E256  4D 8B B0 38 05 00 00            mov r14, qword ptr [r8 + 0x538]
0087E25D  45 33 FF                        xor r15d, r15d
0087E260  49 FF C6                        inc r14
0087E263  49 83 FE 02                     cmp r14, 2
0087E267  0F 87 CA 00 00 00               ja 0x14087e337
0087E26D  41 8D 45 FC                     lea eax, [r13 - 4]
0087E271  83 F8 01                        cmp eax, 1
0087E274  76 5A                           jbe 0x14087e2d0
0087E276  48 8B 8B E0 04 00 00            mov rcx, qword ptr [rbx + 0x4e0]
0087E27D  48 85 C9                        test rcx, rcx
0087E280  0F 85 C1 02 00 00               jne 0x14087e547
0087E286  48 8B 87 E0 04 00 00            mov rax, qword ptr [rdi + 0x4e0]
0087E28D  48 85 C0                        test rax, rax
0087E290  74 07                           je 0x14087e299
0087E292  48 89 83 E0 04 00 00            mov qword ptr [rbx + 0x4e0], rax
0087E299  41 83 FD 04                     cmp r13d, 4
0087E29D  48 8B CB                        mov rcx, rbx
0087E2A0  BA 50 73 50 73                  mov edx, 0x73507350
0087E2A5  48 0F 45 CF                     cmovne rcx, rdi
0087E2A9  E8 62 24 99 FF                  call 0x140210710
0087E2AE  48 8D 8F 08 05 00 00            lea rcx, [rdi + 0x508]
0087E2B5  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0087E2B9  48 8D 83 F8 04 00 00            lea rax, [rbx + 0x4f8]
0087E2C0  48 39 0A                        cmp qword ptr [rdx], rcx
0087E2C3  0F 84 9C 00 00 00               je 0x14087e365
0087E2C9  B9 03 00 00 00                  mov ecx, 3
0087E2CE  CD 29                           int 0x29
0087E2D0  48 8B D5                        mov rdx, rbp
0087E2D3  48 8B CB                        mov rcx, rbx
0087E2D6  E8 85 03 00 00                  call 0x14087e660
0087E2DB  8B F0                           mov esi, eax
0087E2DD  85 C0                           test eax, eax
0087E2DF  79 95                           jns 0x14087e276
0087E2E1  E9 BC 01 00 00                  jmp 0x14087e4a2
0087E2E6  48 8B CF                        mov rcx, rdi
0087E2E9  E8 16 F1 FF FF                  call 0x14087d404
0087E2EE  48 8B D5                        mov rdx, rbp
0087E2F1  48 8B CB                        mov rcx, rbx
0087E2F4  E8 4F 99 00 00                  call 0x140887c48
0087E2F9  BA 50 73 50 73                  mov edx, 0x73507350
0087E2FE  48 8B CB                        mov rcx, rbx
0087E301  E8 0A 24 99 FF                  call 0x140210710
0087E306  BA 50 73 50 73                  mov edx, 0x73507350
0087E30B  48 8B CF                        mov rcx, rdi
0087E30E  E8 CD 95 A7 FF                  call 0x1402f78e0
0087E313  83 BB 2C 06 00 00 00            cmp dword ptr [rbx + 0x62c], 0
0087E31A  48 8B 8B 30 06 00 00            mov rcx, qword ptr [rbx + 0x630]
0087E321  0F 85 EF 02 00 00               jne 0x14087e616
0087E327  48 85 C9                        test rcx, rcx
0087E32A  0F 85 DF 02 00 00               jne 0x14087e60f
0087E330  33 F6                           xor esi, esi
0087E332  E9 C7 FE FF FF                  jmp 0x14087e1fe
0087E337  4A 8D 14 F5 F0 FF FF FF         lea rdx, [r14*8 - 0x10]
0087E33F  B9 00 01 00 00                  mov ecx, 0x100
0087E344  41 B8 50 73 4A 62               mov r8d, 0x624a7350
0087E34A  E8 A1 3D 30 00                  call 0x140b820f0
0087E34F  4C 8B F8                        mov r15, rax
0087E352  48 85 C0                        test rax, rax
0087E355  0F 85 12 FF FF FF               jne 0x14087e26d
0087E35B  B8 9A 00 00 C0                  mov eax, 0xc000009a
0087E360  E9 B1 FE FF FF                  jmp 0x14087e216
0087E365  48 89 08                        mov qword ptr [rax], rcx
0087E368  48 89 50 08                     mov qword ptr [rax + 8], rdx
0087E36C  48 89 02                        mov qword ptr [rdx], rax
0087E36F  48 89 41 08                     mov qword ptr [rcx + 8], rax
0087E373  48 89 BB 18 05 00 00            mov qword ptr [rbx + 0x518], rdi
0087E37A  48 8B 87 20 05 00 00            mov rax, qword ptr [rdi + 0x520]
0087E381  48 89 83 20 05 00 00            mov qword ptr [rbx + 0x520], rax
0087E388  8A 87 4E 04 00 00               mov al, byte ptr [rdi + 0x44e]
0087E38E  FE C0                           inc al
0087E390  4C 89 B3 38 05 00 00            mov qword ptr [rbx + 0x538], r14
0087E397  88 83 4E 04 00 00               mov byte ptr [rbx + 0x44e], al
0087E39D  49 83 FE 02                     cmp r14, 2
0087E3A1  0F 87 7D 01 00 00               ja 0x14087e524
0087E3A7  41 83 FD 04                     cmp r13d, 4
0087E3AB  0F 84 58 01 00 00               je 0x14087e509
0087E3B1  33 D2                           xor edx, edx
0087E3B3  48 8B CB                        mov rcx, rbx
0087E3B6  E8 7D 03 00 00                  call 0x14087e738
0087E3BB  8B 87 28 04 00 00               mov eax, dword ptr [rdi + 0x428]
0087E3C1  BA 03 00 00 00                  mov edx, 3
0087E3C6  01 83 28 04 00 00               add dword ptr [rbx + 0x428], eax
0087E3CC  48 8B CB                        mov rcx, rbx
0087E3CF  8B 87 2C 04 00 00               mov eax, dword ptr [rdi + 0x42c]
0087E3D5  01 83 2C 04 00 00               add dword ptr [rbx + 0x42c], eax
0087E3DB  8B 87 34 04 00 00               mov eax, dword ptr [rdi + 0x434]
0087E3E1  01 83 34 04 00 00               add dword ptr [rbx + 0x434], eax
0087E3E7  8B 87 30 04 00 00               mov eax, dword ptr [rdi + 0x430]
0087E3ED  01 83 30 04 00 00               add dword ptr [rbx + 0x430], eax
0087E3F3  8B 87 38 04 00 00               mov eax, dword ptr [rdi + 0x438]
0087E3F9  01 83 38 04 00 00               add dword ptr [rbx + 0x438], eax
0087E3FF  48 8B 87 10 07 00 00            mov rax, qword ptr [rdi + 0x710]
0087E406  48 89 83 10 07 00 00            mov qword ptr [rbx + 0x710], rax
0087E40D  E8 C2 06 00 00                  call 0x14087ead4
0087E412  8B 97 10 06 00 00               mov edx, dword ptr [rdi + 0x610]
0087E418  81 E2 00 10 84 01               and edx, 0x1841000
0087E41E  74 07                           je 0x14087e427
0087E420  F0 09 93 10 06 00 00            lock or dword ptr [rbx + 0x610], edx
0087E427  45 33 C0                        xor r8d, r8d
0087E42A  41 8D 40 FF                     lea eax, [r8 - 1]
0087E42E  83 F8 01                        cmp eax, 1
0087E431  0F 87 A6 00 00 00               ja 0x14087e4dd
0087E437  41 FF C0                        inc r8d
0087E43A  41 83 F8 03                     cmp r8d, 3
0087E43E  7C EA                           jl 0x14087e42a
0087E440  83 BF 2C 06 00 00 00            cmp dword ptr [rdi + 0x62c], 0
0087E447  0F 84 AD 00 00 00               je 0x14087e4fa
0087E44D  48 8B C7                        mov rax, rdi
0087E450  48 85 FF                        test rdi, rdi
0087E453  74 68                           je 0x14087e4bd
0087E455  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0087E45A  48 8D 15 DF 00 20 00            lea rdx, [rip + 0x2000df]
0087E461  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0087E466  C7 44 24 28 05 00 00 00         mov dword ptr [rsp + 0x28], 5
0087E46E  45 33 C9                        xor r9d, r9d
0087E471  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087E476  45 33 C0                        xor r8d, r8d
0087E479  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
0087E47E  48 8B CB                        mov rcx, rbx
0087E481  E8 66 BD 09 00                  call 0x14091a1ec
0087E486  48 8B 8F 00 07 00 00            mov rcx, qword ptr [rdi + 0x700]
0087E48D  48 85 C9                        test rcx, rcx
0087E490  0F 85 40 01 00 00               jne 0x14087e5d6
0087E496  41 83 FD 07                     cmp r13d, 7
0087E49A  0F 84 61 01 00 00               je 0x14087e601
0087E4A0  33 F6                           xor esi, esi
0087E4A2  4D 85 FF                        test r15, r15
0087E4A5  0F 84 53 FD FF FF               je 0x14087e1fe
0087E4AB  BA 50 73 4A 62                  mov edx, 0x624a7350
0087E4B0  49 8B CF                        mov rcx, r15
0087E4B3  E8 B8 43 30 00                  call 0x140b82870
0087E4B8  E9 41 FD FF FF                  jmp 0x14087e1fe
0087E4BD  83 BB 2C 06 00 00 00            cmp dword ptr [rbx + 0x62c], 0
0087E4C4  74 C0                           je 0x14087e486
0087E4C6  41 83 FD 04                     cmp r13d, 4
0087E4CA  75 BA                           jne 0x14087e486
0087E4CC  48 8B 8B 30 06 00 00            mov rcx, qword ptr [rbx + 0x630]
0087E4D3  48 8B D5                        mov rdx, rbp
0087E4D6  E8 41 6D C1 FF                  call 0x14049521c
0087E4DB  EB A9                           jmp 0x14087e486
0087E4DD  48 8B 97 10 04 00 00            mov rdx, qword ptr [rdi + 0x410]
0087E4E4  48 85 D2                        test rdx, rdx
0087E4E7  0F 84 4A FF FF FF               je 0x14087e437
0087E4ED  48 8B CB                        mov rcx, rbx
0087E4F0  E8 A3 6F F0 FF                  call 0x140785498
0087E4F5  E9 3D FF FF FF                  jmp 0x14087e437
0087E4FA  48 8B 87 30 06 00 00            mov rax, qword ptr [rdi + 0x630]
0087E501  48 85 C0                        test rax, rax
0087E504  E9 4A FF FF FF                  jmp 0x14087e453
0087E509  48 8B D5                        mov rdx, rbp
0087E50C  48 8B CF                        mov rcx, rdi
0087E50F  E8 F0 EE FF FF                  call 0x14087d404
0087E514  48 8B D5                        mov rdx, rbp
0087E517  48 8B CB                        mov rcx, rbx
0087E51A  E8 29 97 00 00                  call 0x140887c48
0087E51F  E9 8D FE FF FF                  jmp 0x14087e3b1
0087E524  49 83 FE 03                     cmp r14, 3
0087E528  0F 87 92 00 00 00               ja 0x14087e5c0
0087E52E  48 8B 87 18 05 00 00            mov rax, qword ptr [rdi + 0x518]
0087E535  49 89 07                        mov qword ptr [r15], rax
0087E538  4C 89 BB 40 05 00 00            mov qword ptr [rbx + 0x540], r15
0087E53F  45 33 FF                        xor r15d, r15d
0087E542  E9 60 FE FF FF                  jmp 0x14087e3a7
0087E547  E8 DC ED C2 FF                  call 0x1404ad328
0087E54C  8B 87 10 06 00 00               mov eax, dword ptr [rdi + 0x610]
0087E552  A8 20                           test al, 0x20
0087E554  74 3F                           je 0x14087e595
0087E556  48 8B 8B D8 04 00 00            mov rcx, qword ptr [rbx + 0x4d8]
0087E55D  4C 8B 87 D8 04 00 00            mov r8, qword ptr [rdi + 0x4d8]
0087E564  48 83 E9 80                     sub rcx, -0x80
0087E568  49 83 E8 80                     sub r8, -0x80
0087E56C  48 8B 11                        mov rdx, qword ptr [rcx]
0087E56F  E8 B0 ED BE FF                  call 0x14046d324
0087E574  E9 20 FD FF FF                  jmp 0x14087e299
0087E579  83 E9 01                        sub ecx, 1
0087E57C  0F 84 30 A5 29 00               je 0x140b18ab2
0087E582  83 F9 01                        cmp ecx, 1
0087E585  0F 84 CB FC FF FF               je 0x14087e256
0087E58B  BE 0D 00 00 C0                  mov esi, 0xc000000d
0087E590  E9 69 FC FF FF                  jmp 0x14087e1fe
0087E595  33 D2                           xor edx, edx
0087E597  48 8B CF                        mov rcx, rdi
0087E59A  E8 BD F8 11 00                  call 0x14099de5c
0087E59F  8B F0                           mov esi, eax
0087E5A1  85 C0                           test eax, eax
0087E5A3  79 B1                           jns 0x14087e556
0087E5A5  48 8B 8B D8 04 00 00            mov rcx, qword ptr [rbx + 0x4d8]
0087E5AC  45 33 C0                        xor r8d, r8d
0087E5AF  48 83 E9 80                     sub rcx, -0x80
0087E5B3  48 8B 11                        mov rdx, qword ptr [rcx]
0087E5B6  E8 69 ED BE FF                  call 0x14046d324
0087E5BB  E9 E2 FE FF FF                  jmp 0x14087e4a2
0087E5C0  48 8B 97 38 05 00 00            mov rdx, qword ptr [rdi + 0x538]
0087E5C7  48 83 EA 02                     sub rdx, 2
0087E5CB  0F 84 5D FF FF FF               je 0x14087e52e
0087E5D1  E9 EA A4 29 00                  jmp 0x140b18ac0
0087E5D6  BA 50 73 4A 62                  mov edx, 0x624a7350
0087E5DB  E8 30 21 99 FF                  call 0x140210710
0087E5E0  48 8B 87 00 07 00 00            mov rax, qword ptr [rdi + 0x700]
0087E5E7  48 89 83 00 07 00 00            mov qword ptr [rbx + 0x700], rax
0087E5EE  48 8B 87 08 07 00 00            mov rax, qword ptr [rdi + 0x708]
0087E5F5  48 89 83 08 07 00 00            mov qword ptr [rbx + 0x708], rax
0087E5FC  E9 95 FE FF FF                  jmp 0x14087e496
0087E601  F0 0F BA AB 14 06 00 00 00      lock bts dword ptr [rbx + 0x614], 0
0087E60A  E9 91 FE FF FF                  jmp 0x14087e4a0
0087E60F  48 8B 89 30 06 00 00            mov rcx, qword ptr [rcx + 0x630]
0087E616  48 8B D5                        mov rdx, rbp
0087E619  E8 FE 6B C1 FF                  call 0x14049521c
0087E61E  E9 0D FD FF FF                  jmp 0x14087e330
0087E623  48 8B 89 30 06 00 00            mov rcx, qword ptr [rcx + 0x630]
0087E62A  48 8B D5                        mov rdx, rbp
0087E62D  E8 EA 6B C1 FF                  call 0x14049521c
0087E632  E9 C7 FB FF FF                  jmp 0x14087e1fe
0087E637  48 8B CD                        mov rcx, rbp
0087E63A  E8 61 4D 9A FF                  call 0x1402233a0
0087E63F  85 C0                           test eax, eax
0087E641  0F 84 CD FB FF FF               je 0x14087e214
0087E647  45 8B C5                        mov r8d, r13d
0087E64A  48 8B D5                        mov rdx, rbp
0087E64D  48 8B CB                        mov rcx, rbx
0087E650  E8 9B 68 F0 FF                  call 0x140784ef0
0087E655  E9 BA FB FF FF                  jmp 0x14087e214
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspEstablishJobHierarchy(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    a1 = (unsigned int)(((unsigned int)(a4)) - (1));
    if (condition_is_not_equal) goto loc_0087E236;
    result = PspBindProcessSessionToJob(a1, a2, a3, a4);
    if (!(sign_flag)) {
        a2 = 0x73507350ULL;
        a1 = a1;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
        a2 = a2;
        a1 = a1;
        result = MmLinkJobProcess(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(a1 + 1580)) != 0) goto loc_0087E62A;
    if (*(unsigned __int64 *)(a1 + 1584) != 0) goto loc_0087E623;
loc_0087E1FE:
    if (a2 == 0) goto loc_0087E214;
    if (sign_flag) goto loc_0087E214;
    if ((*(unsigned __int8 *)(v_rip + 7637168)) != 0) goto loc_0087E637;
loc_0087E214:
loc_0087E216:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0087E236:
    a1 = (unsigned int)((*(unsigned __int64 *)(a1 + 1584)) - (1));
    if (condition_is_equal) goto loc_0087E330;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0087E2E6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0087E256;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0087E579;
loc_0087E256:
    v_r15 = 0;
    v_r14 = (*(unsigned __int64 *)(a3 + 1336)) + 1;
    if (v_r14 > 2) goto loc_0087E337;
loc_0087E26D:
    if (((unsigned int)((unsigned int)(a4) - 4)) <= 1) goto loc_0087E2D0;
loc_0087E276:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1248) != 0) goto loc_0087E547;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1248) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1248) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1248);
    }
    a1 = *(unsigned __int64 *)(v_stack_m18 + 32);
    if (((unsigned int)((unsigned int)(a4))) != 4) { a1 = *(unsigned __int64 *)(v_stack_m18 + 56); }
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x73507350ULL), a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1288 + 8))) == (*(unsigned __int64 *)(v_stack_m18 + 56) + 1288)) goto loc_0087E365;
loc_0087E2D0:
    result = PspBindProcessSessionToJob(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    if (!sign_flag) goto loc_0087E276;
    goto loc_0087E4A2;
loc_0087E2E6:
    result = PspUnlinkJobProcess(*(unsigned __int64 *)(v_stack_m18 + 56), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    result = MmLinkJobProcess(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m18 + 32), (unsigned int)(0x73507350ULL), a3, a4);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m18 + 56), (unsigned int)(0x73507350ULL), a3, a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1580)) != 0) goto loc_0087E616;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1584) != 0) goto loc_0087E60F;
loc_0087E330:
    v_rsi = 0;
    goto loc_0087E1FE;
loc_0087E337:
    result = ExAllocatePool2(256, v_r14 * 8 - 16, (unsigned int)(0x624A7350ULL), a4);
    if (result != 0) goto loc_0087E26D;
    goto loc_0087E216;
loc_0087E365:
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL)) = 256;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 8) = v_r14 * 8 - 16;
    *(unsigned __int64 *)(v_r14 * 8 - 16) = (unsigned int)(0xC000009AULL);
    *(unsigned __int64 *)(256 + 8) = (unsigned int)(0xC000009AULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1304) = *(unsigned __int64 *)(v_stack_m18 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1312) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1312);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1102)) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1336) = v_r14;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1102) = (unsigned __int8)(result);
    if (v_r14 > 2) goto loc_0087E524;
loc_0087E3A7:
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_0087E509;
loc_0087E3B1:
    a2 = 0;
    result = PspSetEffectiveJobLimits(*(unsigned __int64 *)(v_stack_m18 + 32), a2, (unsigned int)(0x624A7350ULL), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1808) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1808);
    result = PspUpdateJobEffectivePriorityLimits(*(unsigned __int64 *)(v_stack_m18 + 32), 3, (unsigned int)(0x624A7350ULL), a4);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1552))) & (0x1841000ULL));
    if (!(condition_is_equal)) {
    }
    a3 = 0;
loc_0087E42A:
    if (((unsigned int)(a3 - 1)) > 1) goto loc_0087E4DD;
loc_0087E437:
    a3 = (unsigned int)((a3) + 1);
    if (((unsigned int)(a3)) < 3) goto loc_0087E42A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1580)) == 0) goto loc_0087E4FA;
loc_0087E453:
    if (*(unsigned __int64 *)(v_stack_m18 + 56) == 0) goto loc_0087E4BD;
    v_stack_m18 = *(unsigned __int64 *)(v_stack_m18 + 56);
    v_stack_m28 = 5;
    a4 = 0;
    v_stack_m30 = v_stack_m20;
    a3 = 0;
    v_stack_m10 = 1;
    result = PspEnumJobsAndProcessesInJobHierarchy(*(unsigned __int64 *)(v_stack_m18 + 32), v_rip + 2097375, a3, a4);
loc_0087E486:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1792) != 0) goto loc_0087E5D6;
loc_0087E496:
    if (((unsigned int)((unsigned int)(a4))) == 7) goto loc_0087E601;
loc_0087E4A0:
    v_rsi = 0;
loc_0087E4A2:
    if (result == 0) goto loc_0087E1FE;
    result = ExFreePoolWithTag(result, (unsigned int)(0x624A7350ULL), a3, a4);
    goto loc_0087E1FE;
loc_0087E4BD:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1580)) == 0) goto loc_0087E486;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_0087E486;
    result = IoSetDiskIoAttributionOnProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1584), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    goto loc_0087E486;
loc_0087E4DD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1040) == 0) goto loc_0087E437;
    result = PspSetEffectiveRateControlJob(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1040), a3, a4);
    goto loc_0087E437;
loc_0087E4FA:
    goto loc_0087E453;
loc_0087E509:
    result = PspUnlinkJobProcess(*(unsigned __int64 *)(v_stack_m18 + 56), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    result = MmLinkJobProcess(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    goto loc_0087E3B1;
loc_0087E524:
    if (v_r14 > 3) goto loc_0087E5C0;
loc_0087E52E:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1304);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1344) = result;
    v_r15 = 0;
    goto loc_0087E3A7;
loc_0087E547:
    result = KeRemoveSchedulingGroup(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1552)))) & (32)) == 0) goto loc_0087E595;
loc_0087E556:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1240)) - (-128);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1240)) - (-128);
    result = KeInsertSchedulingGroup(a1, *(unsigned __int64 *)(a1), a3, a4);
    goto loc_0087E299;
loc_0087E579:
    a1 = (unsigned int)((a1) - (1));
    if (((unsigned int)(a1)) == 1) goto loc_0087E256;
    goto loc_0087E1FE;
loc_0087E595:
    a2 = 0;
    result = PspAddSchedulingGroupToJobChain(*(unsigned __int64 *)(v_stack_m18 + 56), a2, a3, a4);
    if (!sign_flag) goto loc_0087E556;
    a3 = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1240)) - (-128);
    result = KeInsertSchedulingGroup(a1, *(unsigned __int64 *)(a1), a3, a4);
    goto loc_0087E4A2;
loc_0087E5C0:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1336)) - (2);
    if (condition_is_equal) goto loc_0087E52E;
loc_0087E5D6:
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x624A7350ULL), a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1792) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1792);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 32) + 1800) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m18 + 56) + 1800);
    goto loc_0087E496;
loc_0087E601:
    goto loc_0087E4A0;
loc_0087E60F:
loc_0087E616:
    result = IoSetDiskIoAttributionOnProcess(*(unsigned __int64 *)(a1 + 1584), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    goto loc_0087E330;
loc_0087E623:
loc_0087E62A:
    result = IoSetDiskIoAttributionOnProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1584) + 1584), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    goto loc_0087E1FE;
loc_0087E637:
    result = PsGetProcessSessionId(*(unsigned __int64 *)(v_stack_m18 + 40), *(unsigned __int64 *)(v_stack_m18 + 40), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0087E214;
    result = PspEstablishDfssHierarchy(*(unsigned __int64 *)(v_stack_m18 + 32), *(unsigned __int64 *)(v_stack_m18 + 40), (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    goto loc_0087E214;
}
```

## 5. (Beta) C Style

```c
int64_t PspEstablishJobHierarchy(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    Arg1 = (uint32_t)(((uint32_t)(Arg4)) - (1));
    if (condition_is_not_equal) goto loc_0087E236;
    result = PspBindProcessSessionToJob(Arg1, Arg2, Arg3, Arg4);
    if (!(sign_flag)) {
        Arg2 = 0x73507350ULL;
        Arg1 = Arg1;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = MmLinkJobProcess(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(arg1 + 0x62C)) != 0) goto loc_0087E62A;
    if (*(uint64_t *)(arg1 + 0x630) != 0) goto loc_0087E623;
loc_0087E1FE:
    if (Arg2 == 0) goto loc_0087E214;
    if (sign_flag) goto loc_0087E214;
    if ((*(uint8_t *)(v_rip + 0x7488B0)) != 0) goto loc_0087E637;
loc_0087E214:
loc_0087E216:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0087E236:
    Arg1 = (uint32_t)((*(uint64_t *)(arg1 + 0x630)) - (1));
    if (condition_is_equal) goto loc_0087E330;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0087E2E6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0087E256;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0087E579;
loc_0087E256:
    local_r15 = 0;
    local_r14 = (*(uint64_t *)(arg3 + 0x538)) + 1;
    if (local_r14 > 2) goto loc_0087E337;
loc_0087E26D:
    if (((uint32_t)((uint32_t)(Arg4) - 4)) <= 1) goto loc_0087E2D0;
loc_0087E276:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x4E0) != 0) goto loc_0087E547;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x4E0) != 0) {
        *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x4E0) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x4E0);
    }
    Arg1 = *(uint64_t *)(v_stack_m18 + 0x20);
    if (((uint32_t)((uint32_t)(Arg4))) != 4) { Arg1 = *(uint64_t *)(v_stack_m18 + 0x38); }
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x73507350ULL), Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x508 + 0x8))) == (*(uint64_t *)(v_stack_m18 + 0x38) + 1288)) goto loc_0087E365;
loc_0087E2D0:
    result = PspBindProcessSessionToJob(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    if (!sign_flag) goto loc_0087E276;
    goto loc_0087E4A2;
loc_0087E2E6:
    result = PspUnlinkJobProcess(*(uint64_t *)(v_stack_m18 + 0x38), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    result = MmLinkJobProcess(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(v_stack_m18 + 0x20), (uint32_t)(0x73507350ULL), Arg3, Arg4);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_m18 + 0x38), (uint32_t)(0x73507350ULL), Arg3, Arg4);
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x62C)) != 0) goto loc_0087E616;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x630) != 0) goto loc_0087E60F;
loc_0087E330:
    local_rsi = 0;
    goto loc_0087E1FE;
loc_0087E337:
    result = ExAllocatePool2(256, local_r14 * 8 - 16, (uint32_t)(0x624A7350ULL), Arg4);
    if (result != 0) goto loc_0087E26D;
    goto loc_0087E216;
loc_0087E365:
    *(uint64_t *)((uint32_t)(0xC000009AULL)) = 256;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x8) = local_r14 * 8 - 16;
    *(uint64_t *)(local_r14 * 8 - 0x10) = (uint32_t)(0xC000009AULL);
    *(uint64_t *)(256 + 0x8) = (uint32_t)(0xC000009AULL);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x518) = *(uint64_t *)(v_stack_m18 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x520) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x520);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x44E)) + 1);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x538) = local_r14;
    *(uint8_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x44E) = (uint8_t)(result);
    if (local_r14 > 2) goto loc_0087E524;
loc_0087E3A7:
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_0087E509;
loc_0087E3B1:
    Arg2 = 0;
    result = PspSetEffectiveJobLimits(*(uint64_t *)(v_stack_m18 + 0x20), Arg2, (uint32_t)(0x624A7350ULL), Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x710) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x710);
    result = PspUpdateJobEffectivePriorityLimits(*(uint64_t *)(v_stack_m18 + 0x20), 3, (uint32_t)(0x624A7350ULL), Arg4);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x610))) & (0x1841000ULL));
    if (!(condition_is_equal)) {
    }
    Arg3 = 0;
loc_0087E42A:
    if (((uint32_t)(Arg3 - 1)) > 1) goto loc_0087E4DD;
loc_0087E437:
    Arg3 = (uint32_t)((Arg3) + 1);
    if (((uint32_t)(Arg3)) < 3) goto loc_0087E42A;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x62C)) == 0) goto loc_0087E4FA;
loc_0087E453:
    if (*(uint64_t *)(v_stack_m18 + 0x38) == 0) goto loc_0087E4BD;
    v_stack_m18 = *(uint64_t *)(v_stack_m18 + 0x38);
    v_stack_m28 = 5;
    Arg4 = 0;
    v_stack_m30 = v_stack_m20;
    Arg3 = 0;
    v_stack_m10 = 1;
    result = PspEnumJobsAndProcessesInJobHierarchy(*(uint64_t *)(v_stack_m18 + 0x20), v_rip + 2097375, Arg3, Arg4);
loc_0087E486:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x700) != 0) goto loc_0087E5D6;
loc_0087E496:
    if (((uint32_t)((uint32_t)(Arg4))) == 7) goto loc_0087E601;
loc_0087E4A0:
    local_rsi = 0;
loc_0087E4A2:
    if (result == 0) goto loc_0087E1FE;
    result = ExFreePoolWithTag(result, (uint32_t)(0x624A7350ULL), Arg3, Arg4);
    goto loc_0087E1FE;
loc_0087E4BD:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x62C)) == 0) goto loc_0087E486;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_0087E486;
    result = IoSetDiskIoAttributionOnProcess(*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x630), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    goto loc_0087E486;
loc_0087E4DD:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x410) == 0) goto loc_0087E437;
    result = PspSetEffectiveRateControlJob(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x410), Arg3, Arg4);
    goto loc_0087E437;
loc_0087E4FA:
    goto loc_0087E453;
loc_0087E509:
    result = PspUnlinkJobProcess(*(uint64_t *)(v_stack_m18 + 0x38), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    result = MmLinkJobProcess(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    goto loc_0087E3B1;
loc_0087E524:
    if (local_r14 > 3) goto loc_0087E5C0;
loc_0087E52E:
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x518);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x540) = result;
    local_r15 = 0;
    goto loc_0087E3A7;
loc_0087E547:
    result = KeRemoveSchedulingGroup(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x610)))) & (32)) == 0) goto loc_0087E595;
loc_0087E556:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x4D8)) - (-128);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x4D8)) - (-128);
    result = KeInsertSchedulingGroup(Arg1, *(uint64_t *)(arg1), Arg3, Arg4);
    goto loc_0087E299;
loc_0087E579:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (((uint32_t)(Arg1)) == 1) goto loc_0087E256;
    goto loc_0087E1FE;
loc_0087E595:
    Arg2 = 0;
    result = PspAddSchedulingGroupToJobChain(*(uint64_t *)(v_stack_m18 + 0x38), Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_0087E556;
    Arg3 = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x4D8)) - (-128);
    result = KeInsertSchedulingGroup(Arg1, *(uint64_t *)(arg1), Arg3, Arg4);
    goto loc_0087E4A2;
loc_0087E5C0:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x538)) - (2);
    if (condition_is_equal) goto loc_0087E52E;
loc_0087E5D6:
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x624A7350ULL), Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x700) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x700);
    *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x20) + 0x708) = *(uint64_t *)(*(uint64_t *)(v_stack_m18 + 0x38) + 0x708);
    goto loc_0087E496;
loc_0087E601:
    goto loc_0087E4A0;
loc_0087E60F:
loc_0087E616:
    result = IoSetDiskIoAttributionOnProcess(*(uint64_t *)(arg1 + 0x630), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    goto loc_0087E330;
loc_0087E623:
loc_0087E62A:
    result = IoSetDiskIoAttributionOnProcess(*(uint64_t *)(*(uint64_t *)(arg1 + 0x630) + 0x630), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    goto loc_0087E1FE;
loc_0087E637:
    result = PsGetProcessSessionId(*(uint64_t *)(v_stack_m18 + 0x28), *(uint64_t *)(v_stack_m18 + 0x28), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0087E214;
    result = PspEstablishDfssHierarchy(*(uint64_t *)(v_stack_m18 + 0x20), *(uint64_t *)(v_stack_m18 + 0x28), (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    goto loc_0087E214;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x428` | `32` | `R/W` |
| `Arg1` | `+ 0x42C` | `32` | `R/W` |
| `Arg1` | `+ 0x430` | `32` | `R/W` |
| `Arg1` | `+ 0x434` | `32` | `R/W` |
| `Arg1` | `+ 0x438` | `32` | `R/W` |
| `Arg1` | `+ 0x44E` | `8` | `W` |
| `Arg1` | `+ 0x4D8` | `64` | `R` |
| `Arg1` | `+ 0x4E0` | `64` | `R` |
| `Arg1` | `+ 0x4E0` | `64` | `W` |
| `Arg1` | `+ 0x4F8` | `64` | `R` |
| `Arg1` | `+ 0x518` | `64` | `W` |
| `Arg1` | `+ 0x520` | `64` | `W` |
| `Arg1` | `+ 0x538` | `64` | `W` |
| `Arg1` | `+ 0x540` | `64` | `W` |
| `Arg1` | `+ 0x610` | `32` | `R/W` |
| `Arg1` | `+ 0x614` | `32` | `R/W` |
| `Arg1` | `+ 0x62C` | `32` | `R` |
| `Arg1` | `+ 0x630` | `64` | `R` |
| `Arg1` | `+ 0x700` | `64` | `W` |
| `Arg1` | `+ 0x708` | `64` | `W` |
| `Arg1` | `+ 0x710` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x410` | `64` | `R` |
| `Arg3` | `+ 0x428` | `32` | `R` |
| `Arg3` | `+ 0x42C` | `32` | `R` |
| `Arg3` | `+ 0x430` | `32` | `R` |
| `Arg3` | `+ 0x434` | `32` | `R` |
| `Arg3` | `+ 0x438` | `32` | `R` |
| `Arg3` | `+ 0x44E` | `8` | `R` |

추가 오프셋 11개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087E17C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
