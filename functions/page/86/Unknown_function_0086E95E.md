# sub_0086E95E

- RVA: `0x0086E95E`–`0x0086EE15` (길이 `1,207` bytes)
- VA: `0x000000014086E95E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C158`
- 디코드: `300`개 명령, `1,207/1,207` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0086E9A0` → [SeExamineSacl](../97/SeExamineSacl_function_00973A30.md) (function, `0x00973A30`)
- `0x0086E9BB` → [SepRmAcquireGlobalSaclReadLock](../../text/46/SepRmAcquireGlobalSaclReadLock_function_0046B608.md) (function, `0x0046B608`)
- `0x0086E9DB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086E9E9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086EA24` → [SeMaximumAuditMask](../../text/4A/SeMaximumAuditMask_function_004A8D2C.md) (function, `0x004A8D2C`)
- `0x0086EA38` → [SeMaximumAuditMaskFromGlobalSacl](../A8/SeMaximumAuditMaskFromGlobalSacl_function_00A832DC.md) (function, `0x00A832DC`)
- `0x0086EAB8` → [SepAdtAuditPrivilegeUseWithContext](../87/SepAdtAuditPrivilegeUseWithContext_function_00870BD0.md) (function, `0x00870BD0`)
- `0x0086EB18` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x0086EB69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086EB86` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086EBAD` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x0086EBC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086EBE2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086EC09` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x0086EC2B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086EC3A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086EC4B` → [SepAuditFailed](SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x0086EC65` → [SepQueryTypeString](../92/SepQueryTypeString_function_00920420.md) (function, `0x00920420`)
- `0x0086ED13` → [SepAdtOpenObjectAuditAlarm](../91/SepAdtOpenObjectAuditAlarm_function_0091F23C.md) (function, `0x0091F23C`)
- `0x0086ED55` → [SepAdtStagingEvent](../91/SepAdtStagingEvent_function_0091F948.md) (function, `0x0091F948`)
- `0x0086EDA8` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0086EDEE` → [SeExamineSacl](../97/SeExamineSacl_function_00973A30.md) (function, `0x00973A30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0086E9C0` → RVA `0x00E680F8` (`.data`; read)
- `0x0086E9D4` → RVA `0x00E68100` (`.data`; read)
- `0x0086EC97` → RVA `0x000013A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0086E9BB` → [SepRmAcquireGlobalSaclReadLock](../../text/46/SepRmAcquireGlobalSaclReadLock_function_0046B608.md) (`PAGE` → `.text`)
  - `0x0086E9DB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086E9E9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086EA24` → [SeMaximumAuditMask](../../text/4A/SeMaximumAuditMask_function_004A8D2C.md) (`PAGE` → `.text`)
  - `0x0086EB69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086EB86` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086EBAD` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x0086EBC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086EBE2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086EC09` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x0086EC2B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086EC3A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x0086E9F2` → [sub_0086E7EE + 0x69](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EA01` → [sub_0086E7EE + 0x69](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EA41` → [sub_0086E7EE + 0x69](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EABF` → [sub_0086E7EE + 0x12D](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EAC9` → [sub_0086E7EE + 0xBF](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EB1D` → [sub_0086E7EE + 0xB1](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EB26` → [sub_0086E7EE + 0xD0](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EC42` → [sub_0086E7EE + 0x141](Unknown_function_0086E7EE.md) (`tail-transfer`)
  - `0x0086EC50` → [sub_0086E7EE + 0x141](Unknown_function_0086E7EE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0086E95E  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0086E963  BA 00 80 00 00                  mov edx, 0x8000
0086E968  44 8B 7F 14                     mov r15d, dword ptr [rdi + 0x14]
0086E96C  0F B7 C8                        movzx ecx, ax
0086E96F  44 0B 7F 10                     or r15d, dword ptr [rdi + 0x10]
0086E973  66 23 CA                        and cx, dx
0086E976  A8 10                           test al, 0x10
0086E978  0F 85 E1 00 00 00               jne 0x14086ea5f
0086E97E  33 C0                           xor eax, eax
0086E980  8B D0                           mov edx, eax
0086E982  8B C8                           mov ecx, eax
0086E984  48 8D 45 B8                     lea rax, [rbp - 0x48]
0086E988  45 8B CF                        mov r9d, r15d
0086E98B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086E990  4C 8B C6                        mov r8, rsi
0086E993  48 8D 45 B7                     lea rax, [rbp - 0x49]
0086E997  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086E99C  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0086E9A0  E8 8B 50 10 00                  call 0x140973a30
0086E9A5  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0086E9AA  A8 10                           test al, 0x10
0086E9AC  0F 85 94 00 00 00               jne 0x14086ea46
0086E9B2  45 33 F6                        xor r14d, r14d
0086E9B5  44 38 6D B7                     cmp byte ptr [rbp - 0x49], r13b
0086E9B9  75 3D                           jne 0x14086e9f8
0086E9BB  E8 48 CC BF FF                  call 0x14046b608
0086E9C0  48 8B 1D 31 97 5F 00            mov rbx, qword ptr [rip + 0x5f9731]
0086E9C7  48 85 DB                        test rbx, rbx
0086E9CA  0F 85 B0 03 00 00               jne 0x14086ed80
0086E9D0  0F B6 5D 67                     movzx ebx, byte ptr [rbp + 0x67]
0086E9D4  48 8D 0D 25 97 5F 00            lea rcx, [rip + 0x5f9725]
0086E9DB  E8 30 10 9F FF                  call 0x14025fa10
0086E9E0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086E9E9  E8 02 06 9F FF                  call 0x14025eff0
0086E9EE  44 38 6D B7                     cmp byte ptr [rbp - 0x49], r13b
0086E9F2  0F 84 5F FE FF FF               je 0x14086e857
0086E9F8  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0086E9FC  C6 00 01                        mov byte ptr [rax], 1
0086E9FF  84 DB                           test bl, bl
0086EA01  0F 84 50 FE FF FF               je 0x14086e857
0086EA07  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
0086EA0B  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0086EA0F  A8 10                           test al, 0x10
0086EA11  0F 85 B7 00 00 00               jne 0x14086eace
0086EA17  33 C9                           xor ecx, ecx
0086EA19  4D 8D 4C 24 1C                  lea r9, [r12 + 0x1c]
0086EA1E  4C 8B C6                        mov r8, rsi
0086EA21  41 8B D7                        mov edx, r15d
0086EA24  E8 03 A3 C3 FF                  call 0x1404a8d2c
0086EA29  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
0086EA2D  4D 8D 4C 24 1C                  lea r9, [r12 + 0x1c]
0086EA32  4C 8B C6                        mov r8, rsi
0086EA35  41 8B D7                        mov edx, r15d
0086EA38  E8 9F 48 21 00                  call 0x140a832dc
0086EA3D  0F B6 5D 67                     movzx ebx, byte ptr [rbp + 0x67]
0086EA41  E9 11 FE FF FF                  jmp 0x14086e857
0086EA46  66 85 C0                        test ax, ax
0086EA49  0F 89 9A 00 00 00               jns 0x14086eae9
0086EA4F  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0086EA53  85 C0                           test eax, eax
0086EA55  75 3D                           jne 0x14086ea94
0086EA57  45 33 F6                        xor r14d, r14d
0086EA5A  E9 56 FF FF FF                  jmp 0x14086e9b5
0086EA5F  45 33 C0                        xor r8d, r8d
0086EA62  66 85 C9                        test cx, cx
0086EA65  74 7C                           je 0x14086eae3
0086EA67  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0086EA6B  85 C0                           test eax, eax
0086EA6D  75 31                           jne 0x14086eaa0
0086EA6F  41 8B D0                        mov edx, r8d
0086EA72  66 85 C9                        test cx, cx
0086EA75  0F 84 87 00 00 00               je 0x14086eb02
0086EA7B  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0086EA7F  85 C0                           test eax, eax
0086EA81  75 08                           jne 0x14086ea8b
0086EA83  49 8B C8                        mov rcx, r8
0086EA86  E9 F9 FE FF FF                  jmp 0x14086e984
0086EA8B  49 8D 0C 06                     lea rcx, [r14 + rax]
0086EA8F  E9 F0 FE FF FF                  jmp 0x14086e984
0086EA94  4C 8B F0                        mov r14, rax
0086EA97  4C 03 75 4F                     add r14, qword ptr [rbp + 0x4f]
0086EA9B  E9 15 FF FF FF                  jmp 0x14086e9b5
0086EAA0  49 8D 14 06                     lea rdx, [r14 + rax]
0086EAA4  EB CC                           jmp 0x14086ea72
0086EAA6  48 8D 55 BB                     lea rdx, [rbp - 0x45]
0086EAAA  4C 8B C8                        mov r9, rax
0086EAAD  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0086EAB2  45 33 C0                        xor r8d, r8d
0086EAB5  0F B6 D3                        movzx edx, bl
0086EAB8  E8 13 21 00 00                  call 0x140870bd0
0086EABD  84 C0                           test al, al
0086EABF  0F 84 56 FE FF FF               je 0x14086e91b
0086EAC5  C6 47 7C 01                     mov byte ptr [rdi + 0x7c], 1
0086EAC9  E9 DF FD FF FF                  jmp 0x14086e8ad
0086EACE  66 85 C0                        test ax, ax
0086EAD1  79 26                           jns 0x14086eaf9
0086EAD3  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
0086EAD6  85 C0                           test eax, eax
0086EAD8  74 18                           je 0x14086eaf2
0086EADA  48 8D 0C 02                     lea rcx, [rdx + rax]
0086EADE  E9 36 FF FF FF                  jmp 0x14086ea19
0086EAE3  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
0086EAE7  EB 89                           jmp 0x14086ea72
0086EAE9  4D 8B 76 18                     mov r14, qword ptr [r14 + 0x18]
0086EAED  E9 C3 FE FF FF                  jmp 0x14086e9b5
0086EAF2  33 C9                           xor ecx, ecx
0086EAF4  E9 20 FF FF FF                  jmp 0x14086ea19
0086EAF9  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
0086EAFD  E9 17 FF FF FF                  jmp 0x14086ea19
0086EB02  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
0086EB06  E9 79 FE FF FF                  jmp 0x14086e984
0086EB0B  4C 8D 4F 20                     lea r9, [rdi + 0x20]
0086EB0F  41 0F B6 D2                     movzx edx, r10b
0086EB13  B9 82 00 00 00                  mov ecx, 0x82
0086EB18  E8 A3 1F 00 00                  call 0x140870ac0
0086EB1D  E9 7D FD FF FF                  jmp 0x14086e89f
0086EB22  66 45 39 2F                     cmp word ptr [r15], r13w
0086EB26  0F 84 92 FD FF FF               je 0x14086e8be
0086EB2C  48 8B 75 3F                     mov rsi, qword ptr [rbp + 0x3f]
0086EB30  48 8B 45 37                     mov rax, qword ptr [rbp + 0x37]
0086EB34  48 85 C0                        test rax, rax
0086EB37  0F 84 18 01 00 00               je 0x14086ec55
0086EB3D  66 83 38 00                     cmp word ptr [rax], 0
0086EB41  0F 84 0E 01 00 00               je 0x14086ec55
0086EB47  4C 8B F0                        mov r14, rax
0086EB4A  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
0086EB4E  84 DB                           test bl, bl
0086EB50  0F 84 2F 01 00 00               je 0x14086ec85
0086EB56  4D 85 FF                        test r15, r15
0086EB59  74 57                           je 0x14086ebb2
0086EB5B  48 8B 8F 88 00 00 00            mov rcx, qword ptr [rdi + 0x88]
0086EB62  48 85 C9                        test rcx, rcx
0086EB65  74 0F                           je 0x14086eb76
0086EB67  33 D2                           xor edx, edx
0086EB69  E8 02 3D 31 00                  call 0x140b82870
0086EB6E  33 C0                           xor eax, eax
0086EB70  89 87 80 00 00 00               mov dword ptr [rdi + 0x80], eax
0086EB76  41 0F B7 57 02                  movzx edx, word ptr [r15 + 2]
0086EB7B  B9 00 01 00 00                  mov ecx, 0x100
0086EB80  41 B8 53 65 20 20               mov r8d, 0x20206553
0086EB86  E8 65 35 31 00                  call 0x140b820f0
0086EB8B  48 89 87 88 00 00 00            mov qword ptr [rdi + 0x88], rax
0086EB92  48 85 C0                        test rax, rax
0086EB95  74 1B                           je 0x14086ebb2
0086EB97  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
0086EB9C  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
0086EBA3  49 8B D7                        mov rdx, r15
0086EBA6  66 89 87 82 00 00 00            mov word ptr [rdi + 0x82], ax
0086EBAD  E8 7E 03 B9 FF                  call 0x1403fef30
0086EBB2  4D 85 F6                        test r14, r14
0086EBB5  74 57                           je 0x14086ec0e
0086EBB7  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
0086EBBE  48 85 C9                        test rcx, rcx
0086EBC1  74 0F                           je 0x14086ebd2
0086EBC3  33 D2                           xor edx, edx
0086EBC5  E8 A6 3C 31 00                  call 0x140b82870
0086EBCA  33 C0                           xor eax, eax
0086EBCC  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
0086EBD2  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
0086EBD7  B9 00 01 00 00                  mov ecx, 0x100
0086EBDC  41 B8 53 65 20 20               mov r8d, 0x20206553
0086EBE2  E8 09 35 31 00                  call 0x140b820f0
0086EBE7  48 89 87 98 00 00 00            mov qword ptr [rdi + 0x98], rax
0086EBEE  48 85 C0                        test rax, rax
0086EBF1  74 1B                           je 0x14086ec0e
0086EBF3  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0086EBF8  48 8D 8F 90 00 00 00            lea rcx, [rdi + 0x90]
0086EBFF  49 8B D6                        mov rdx, r14
0086EC02  66 89 87 92 00 00 00            mov word ptr [rdi + 0x92], ax
0086EC09  E8 22 03 B9 FF                  call 0x1403fef30
0086EC0E  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0086EC12  48 85 C0                        test rax, rax
0086EC15  74 09                           je 0x14086ec20
0086EC17  0F 10 00                        movups xmm0, xmmword ptr [rax]
0086EC1A  41 0F 11 44 24 20               movups xmmword ptr [r12 + 0x20], xmm0
0086EC20  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0086EC24  48 85 C9                        test rcx, rcx
0086EC27  74 07                           je 0x14086ec30
0086EC29  33 D2                           xor edx, edx
0086EC2B  E8 40 3C 31 00                  call 0x140b82870
0086EC30  48 85 F6                        test rsi, rsi
0086EC33  74 0A                           je 0x14086ec3f
0086EC35  33 D2                           xor edx, edx
0086EC37  48 8B CE                        mov rcx, rsi
0086EC3A  E8 31 3C 31 00                  call 0x140b82870
0086EC3F  45 85 ED                        test r13d, r13d
0086EC42  0F 89 E7 FC FF FF               jns 0x14086e92f
0086EC48  41 8B CD                        mov ecx, r13d
0086EC4B  E8 D0 01 00 00                  call 0x14086ee20
0086EC50  E9 DA FC FF FF                  jmp 0x14086e92f
0086EC55  48 85 F6                        test rsi, rsi
0086EC58  0F 84 01 01 00 00               je 0x14086ed5f
0086EC5E  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0086EC62  48 8B CE                        mov rcx, rsi
0086EC65  E8 B6 17 0B 00                  call 0x140920420
0086EC6A  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
0086EC6E  44 8B E8                        mov r13d, eax
0086EC71  85 C0                           test eax, eax
0086EC73  78 AB                           js 0x14086ec20
0086EC75  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
0086EC79  48 85 F6                        test rsi, rsi
0086EC7C  4C 0F 45 F6                     cmovne r14, rsi
0086EC80  E9 C9 FE FF FF                  jmp 0x14086eb4e
0086EC85  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0086EC89  48 85 C0                        test rax, rax
0086EC8C  75 05                           jne 0x14086ec93
0086EC8E  49 8D 44 24 20                  lea rax, [r12 + 0x20]
0086EC93  0F B7 4D BB                     movzx ecx, word ptr [rbp - 0x45]
0086EC97  48 8D 15 0A 27 79 FF            lea rdx, [rip - 0x86d8f6]
0086EC9E  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0086ECA6  33 DB                           xor ebx, ebx
0086ECA8  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0086ECB0  4D 8B CE                        mov r9, r14
0086ECB3  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0086ECB7  45 33 C0                        xor r8d, r8d
0086ECBA  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
0086ECC2  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0086ECC6  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0086ECCB  C7 44 24 68 02 00 00 00         mov dword ptr [rsp + 0x68], 2
0086ECD3  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0086ECD8  49 8B 04 24                     mov rax, qword ptr [r12]
0086ECDC  88 5C 24 58                     mov byte ptr [rsp + 0x58], bl
0086ECE0  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0086ECE5  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0086ECE8  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0086ECEC  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
0086ECEF  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0086ECF3  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0086ECF7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086ECFC  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0086ED00  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086ED05  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
0086ED09  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086ED0E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0086ED13  E8 24 05 0B 00                  call 0x14091f23c
0086ED18  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0086ED1B  4D 8B CE                        mov r9, r14
0086ED1E  0F B7 4D BB                     movzx ecx, word ptr [rbp - 0x45]
0086ED22  45 33 C0                        xor r8d, r8d
0086ED25  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0086ED2A  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0086ED2F  88 5C 24 48                     mov byte ptr [rsp + 0x48], bl
0086ED33  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0086ED37  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
0086ED3A  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0086ED3E  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0086ED42  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086ED47  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0086ED4B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086ED50  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0086ED55  E8 EE 0B 0B 00                  call 0x14091f948
0086ED5A  E9 C1 FE FF FF                  jmp 0x14086ec20
0086ED5F  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
0086ED63  E9 E2 FD FF FF                  jmp 0x14086eb4a
0086ED68  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
0086ED6C  E9 AF FE FF FF                  jmp 0x14086ec20
0086ED71  4D 8B FD                        mov r15, r13
0086ED74  E9 B7 FD FF FF                  jmp 0x14086eb30
0086ED79  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0086ED80  48 85 DB                        test rbx, rbx
0086ED83  0F 84 47 FC FF FF               je 0x14086e9d0
0086ED89  48 8B 45 37                     mov rax, qword ptr [rbp + 0x37]
0086ED8D  44 0F B7 4B 08                  movzx r9d, word ptr [rbx + 8]
0086ED92  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
0086ED96  49 D1 E9                        shr r9, 1
0086ED99  0F B7 10                        movzx edx, word ptr [rax]
0086ED9C  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0086EDA0  48 D1 EA                        shr rdx, 1
0086EDA3  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
0086EDA8  E8 33 3A 10 00                  call 0x1409727e0
0086EDAD  85 C0                           test eax, eax
0086EDAF  74 05                           je 0x14086edb6
0086EDB1  48 8B 1B                        mov rbx, qword ptr [rbx]
0086EDB4  EB CA                           jmp 0x14086ed80
0086EDB6  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0086EDBA  0F B6 5D 67                     movzx ebx, byte ptr [rbp + 0x67]
0086EDBE  48 85 C9                        test rcx, rcx
0086EDC1  0F 84 0D FC FF FF               je 0x14086e9d4
0086EDC7  48 8D 45 B9                     lea rax, [rbp - 0x47]
0086EDCB  44 88 6D 6F                     mov byte ptr [rbp + 0x6f], r13b
0086EDCF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086EDD4  45 8B CF                        mov r9d, r15d
0086EDD7  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0086EDDB  44 88 6D B9                     mov byte ptr [rbp - 0x47], r13b
0086EDDF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086EDE4  4C 8B C6                        mov r8, rsi
0086EDE7  49 8B D6                        mov rdx, r14
0086EDEA  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0086EDEE  E8 3D 4C 10 00                  call 0x140973a30
0086EDF3  44 38 6D 6F                     cmp byte ptr [rbp + 0x6f], r13b
0086EDF7  0F 95 45 B7                     setne byte ptr [rbp - 0x49]
0086EDFB  44 38 6D B8                     cmp byte ptr [rbp - 0x48], r13b
0086EDFF  74 0A                           je 0x14086ee0b
0086EE01  B0 01                           mov al, 1
0086EE03  88 45 B8                        mov byte ptr [rbp - 0x48], al
0086EE06  E9 C9 FB FF FF                  jmp 0x14086e9d4
0086EE0B  44 38 6D B9                     cmp byte ptr [rbp - 0x47], r13b
0086EE0F  75 F0                           jne 0x14086ee01
0086EE11  32 C0                           xor al, al
0086EE13  EB EE                           jmp 0x14086ee03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0086E95E(void)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;

    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 20))) | (*(unsigned int *)(v_rdi + 16)));
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 2))) & ((unsigned __int16)((unsigned int)(0x8000ULL))));
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_r14 + 2))) & (16)) != 0) goto loc_0086EA5F;
    result = 0;
loc_0086E984:
    v_stack_p30 = v_rbp - 72;
    v_stack_p28 = v_rbp - 73;
    v_stack_p20 = (unsigned __int8)(v_rbx);
    result = SeExamineSacl(0, 0, v_rsi, (unsigned int)((unsigned int)(v_r15)));
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_r14 + 2))) & (16)) != 0) goto loc_0086EA46;
    v_r14 = 0;
loc_0086E9B5:
    if ((*(unsigned __int8 *)(v_rbp - 73)) != ((unsigned __int8)(v_r13))) goto loc_0086E9F8;
    result = SepRmAcquireGlobalSaclReadLock(0, 0, v_rsi, (unsigned int)((unsigned int)(v_r15)));
    if (*(unsigned __int64 *)(v_rip + 6264625) != 0) goto loc_0086ED80;
loc_0086E9D0:
loc_0086E9D4:
    result = ExReleaseResourceLite(v_rip + 6264613, 0, v_rsi, (unsigned int)((unsigned int)(v_r15)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 0, v_rsi, (unsigned int)((unsigned int)(v_r15)));
loc_0086E9F8:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 127)) = 1;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 79) + 2))) & (16)) != 0) goto loc_0086EACE;
    a1 = 0;
loc_0086EA19:
    result = SeMaximumAuditMask(a1, (unsigned int)((unsigned int)(v_r15)), v_rsi, v_r12 + 28);
    result = SeMaximumAuditMaskFromGlobalSacl(*(unsigned __int64 *)(v_rbp + 55), (unsigned int)((unsigned int)(v_r15)), v_rsi, v_r12 + 28);
loc_0086EA46:
    if (!sign_flag) goto loc_0086EAE9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 12))) != 0) goto loc_0086EA94;
    v_r14 = 0;
    goto loc_0086E9B5;
loc_0086EA5F:
    a3 = 0;
    if ((unsigned __int16)(*(unsigned __int64 *)(v_rbp + 55)) == 0) goto loc_0086EAE3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 12))) != 0) goto loc_0086EAA0;
loc_0086EA72:
    if ((unsigned __int16)(*(unsigned __int64 *)(v_rbp + 55)) == 0) goto loc_0086EB02;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 12))) != 0) goto loc_0086EA8B;
    goto loc_0086E984;
loc_0086EA8B:
    goto loc_0086E984;
loc_0086EA94:
    v_r14 = ((unsigned int)(*(unsigned int *)(v_r14 + 12))) + (*(unsigned __int64 *)(v_rbp + 79));
    goto loc_0086E9B5;
loc_0086EAA0:
    goto loc_0086EA72;
loc_0086EACE:
    if (!sign_flag) goto loc_0086EAF9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 12)) * 1 + 12))) == 0) goto loc_0086EAF2;
    goto loc_0086EA19;
loc_0086EAE3:
    goto loc_0086EA72;
loc_0086EAE9:
    goto loc_0086E9B5;
loc_0086EAF2:
    a1 = 0;
    goto loc_0086EA19;
loc_0086EAF9:
    goto loc_0086EA19;
loc_0086EB02:
    goto loc_0086E984;
loc_0086ED80:
    if (*(unsigned __int8 *)(v_rbp + 103) == 0) goto loc_0086E9D0;
    a4 = (*(unsigned __int16 *)(*(unsigned __int8 *)(v_rbp + 103) + 8)) >> (1);
    a2 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 55))) >> (1);
    v_stack_p20 = (unsigned __int8)(v_r13);
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 55) + 8), a2, *(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp + 103) + 16), a4);
    if ((unsigned int)(result) == 0) goto loc_0086EDB6;
    goto loc_0086ED80;
loc_0086EDB6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp + 103)) + 24) == 0) goto loc_0086E9D4;
    *(unsigned __int8 *)(v_rbp + 111) = (unsigned __int8)(v_r13);
    v_stack_p30 = v_rbp - 71;
    *(unsigned __int8 *)(v_rbp - 71) = (unsigned __int8)(v_r13);
    v_stack_p28 = v_rbp + 111;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp + 103));
    result = SeExamineSacl(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp + 103)) + 24), *(unsigned __int64 *)(v_r14 + 24), v_rsi, (unsigned int)((unsigned int)(v_r15)));
    if ((*(unsigned __int8 *)(v_rbp - 72)) == ((unsigned __int8)(v_r13))) goto loc_0086EE0B;
loc_0086EE01:
loc_0086EE03:
    *(unsigned __int8 *)(v_rbp - 72) = 1;
    goto loc_0086E9D4;
loc_0086EE0B:
    if ((*(unsigned __int8 *)(v_rbp - 71)) != ((unsigned __int8)(v_r13))) goto loc_0086EE01;
    result = 0;
    goto loc_0086EE03;
}
```

## 5. (Beta) C Style

```c
void sub_0086E95E(void)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;

    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x14))) | (*(uint32_t *)(local_rdi + 0x10)));
    a1 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_r14 + 0x2))) & ((uint16_t)((uint32_t)(0x8000ULL))));
    if ((((uint8_t)(*(uint16_t *)(local_r14 + 0x2))) & (16)) != 0) goto loc_0086EA5F;
    result = 0;
loc_0086E984:
    v_stack_p30 = local_rbp - 72;
    v_stack_p28 = local_rbp - 73;
    v_stack_p20 = (uint8_t)(local_rbx);
    result = SeExamineSacl(0, 0, local_rsi, (uint32_t)((uint32_t)(local_r15)));
    if ((((uint8_t)(*(uint16_t *)(local_r14 + 0x2))) & (16)) != 0) goto loc_0086EA46;
    local_r14 = 0;
loc_0086E9B5:
    if ((*(uint8_t *)(local_rbp - 0x49)) != ((uint8_t)(local_r13))) goto loc_0086E9F8;
    result = SepRmAcquireGlobalSaclReadLock(0, 0, local_rsi, (uint32_t)((uint32_t)(local_r15)));
    if (*(uint64_t *)(v_rip + 0x5F9731) != 0) goto loc_0086ED80;
loc_0086E9D0:
loc_0086E9D4:
    result = ExReleaseResourceLite(v_rip + 6264613, 0, local_rsi, (uint32_t)((uint32_t)(local_r15)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 0, local_rsi, (uint32_t)((uint32_t)(local_r15)));
loc_0086E9F8:
    *(uint8_t *)(*(uint64_t *)(local_rbp + 0x7F)) = 1;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x4F) + 0x2))) & (16)) != 0) goto loc_0086EACE;
    a1 = 0;
loc_0086EA19:
    result = SeMaximumAuditMask(a1, (uint32_t)((uint32_t)(local_r15)), local_rsi, local_r12 + 28);
    result = SeMaximumAuditMaskFromGlobalSacl(*(uint64_t *)(local_rbp + 0x37), (uint32_t)((uint32_t)(local_r15)), local_rsi, local_r12 + 28);
loc_0086EA46:
    if (!sign_flag) goto loc_0086EAE9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xC))) != 0) goto loc_0086EA94;
    local_r14 = 0;
    goto loc_0086E9B5;
loc_0086EA5F:
    a3 = 0;
    if ((uint16_t)(*(uint64_t *)(local_rbp + 0x37)) == 0) goto loc_0086EAE3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xC))) != 0) goto loc_0086EAA0;
loc_0086EA72:
    if ((uint16_t)(*(uint64_t *)(local_rbp + 0x37)) == 0) goto loc_0086EB02;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0xC))) != 0) goto loc_0086EA8B;
    goto loc_0086E984;
loc_0086EA8B:
    goto loc_0086E984;
loc_0086EA94:
    local_r14 = ((uint32_t)(*(uint32_t *)(local_r14 + 0xC))) + (*(uint64_t *)(local_rbp + 0x4F));
    goto loc_0086E9B5;
loc_0086EAA0:
    goto loc_0086EA72;
loc_0086EACE:
    if (!sign_flag) goto loc_0086EAF9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0xC)) * 1 + 0xC))) == 0) goto loc_0086EAF2;
    goto loc_0086EA19;
loc_0086EAE3:
    goto loc_0086EA72;
loc_0086EAE9:
    goto loc_0086E9B5;
loc_0086EAF2:
    a1 = 0;
    goto loc_0086EA19;
loc_0086EAF9:
    goto loc_0086EA19;
loc_0086EB02:
    goto loc_0086E984;
loc_0086ED80:
    if (*(uint8_t *)(local_rbp + 0x67) == 0) goto loc_0086E9D0;
    a4 = (*(uint16_t *)(*(uint8_t *)(local_rbp + 0x67) + 0x8)) >> (1);
    a2 = (*(uint16_t *)(*(uint64_t *)(local_rbp + 0x37))) >> (1);
    v_stack_p20 = (uint8_t)(local_r13);
    result = RtlCompareUnicodeStrings(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x37) + 0x8), a2, *(uint64_t *)(*(uint8_t *)(local_rbp + 0x67) + 0x10), a4);
    if ((uint32_t)(result) == 0) goto loc_0086EDB6;
    goto loc_0086ED80;
loc_0086EDB6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(local_rbp + 0x67)) + 0x18) == 0) goto loc_0086E9D4;
    *(uint8_t *)(local_rbp + 0x6F) = (uint8_t)(local_r13);
    v_stack_p30 = local_rbp - 71;
    *(uint8_t *)(local_rbp - 0x47) = (uint8_t)(local_r13);
    v_stack_p28 = local_rbp + 111;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(local_rbp + 0x67));
    result = SeExamineSacl(*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(local_rbp + 0x67)) + 0x18), *(uint64_t *)(local_r14 + 0x18), local_rsi, (uint32_t)((uint32_t)(local_r15)));
    if ((*(uint8_t *)(local_rbp - 0x48)) == ((uint8_t)(local_r13))) goto loc_0086EE0B;
loc_0086EE01:
loc_0086EE03:
    *(uint8_t *)(local_rbp - 0x48) = 1;
    goto loc_0086E9D4;
loc_0086EE0B:
    if ((*(uint8_t *)(local_rbp - 0x47)) != ((uint8_t)(local_r13))) goto loc_0086EE01;
    result = 0;
    goto loc_0086EE03;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086E95E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
