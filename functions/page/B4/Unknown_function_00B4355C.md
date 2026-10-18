# sub_00B4355C

- RVA: `0x00B4355C`–`0x00B4387E` (길이 `802` bytes)
- VA: `0x0000000140B4355C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B717C`
- 디코드: `239`개 명령, `802/802` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B435D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B436FE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B437D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B435D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B436FE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B437D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **27**
  - `0x00B4356C` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B4357B` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B4358F` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B435A3` → [SPCallServerHandleUpdatePolicies + 0x244](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B435E8` → [SPCallServerHandleUpdatePolicies + 0x2B](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43614` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43623` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B4363D` → [SPCallServerHandleUpdatePolicies + 0x23D](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43646` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43652` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43669` → [SPCallServerHandleUpdatePolicies + 0x244](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43678` → [SPCallServerHandleUpdatePolicies + 0x212](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43680` → [SPCallServerHandleUpdatePolicies + 0x14D](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43695` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B436A4` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B436B8` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B436CC` → [SPCallServerHandleUpdatePolicies + 0x244](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43711` → [SPCallServerHandleUpdatePolicies + 0x2B](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43745` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43754` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43774` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43783` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43797` → [SPCallServerHandleUpdatePolicies + 0x25](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B437AA` → [SPCallServerHandleUpdatePolicies + 0x244](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B437E8` → [SPCallServerHandleUpdatePolicies + 0x2B](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B4381F` → [SPCallServerHandleUpdatePolicies + 0x2B](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)
  - `0x00B43828` → [SPCallServerHandleUpdatePolicies + 0x2B](../A8/SPCallServerHandleUpdatePolicies_function_00A815EC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B4355C  44 8B 0B                        mov r9d, dword ptr [rbx]
00B4355F  33 C9                           xor ecx, ecx
00B43561  41 3B C9                        cmp ecx, r9d
00B43564  73 22                           jae 0x140b43588
00B43566  8B 02                           mov eax, dword ptr [rdx]
00B43568  03 C5                           add eax, ebp
00B4356A  3B C5                           cmp eax, ebp
00B4356C  0F 82 9F E0 F3 FF               jb 0x140a81611
00B43572  44 8B C0                        mov r8d, eax
00B43575  4C 03 C2                        add r8, rdx
00B43578  4C 3B C2                        cmp r8, rdx
00B4357B  0F 82 90 E0 F3 FF               jb 0x140a81611
00B43581  49 8B D0                        mov rdx, r8
00B43584  FF C1                           inc ecx
00B43586  EB D9                           jmp 0x140b43561
00B43588  4C 8D 42 04                     lea r8, [rdx + 4]
00B4358C  4C 3B C2                        cmp r8, rdx
00B4358F  0F 82 7C E0 F3 FF               jb 0x140a81611
00B43595  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00B43598  48 8D 42 08                     lea rax, [rdx + 8]
00B4359C  48 03 4B 08                     add rcx, qword ptr [rbx + 8]
00B435A0  48 3B C1                        cmp rax, rcx
00B435A3  0F 87 87 E2 F3 FF               ja 0x140a81830
00B435A9  89 2A                           mov dword ptr [rdx], ebp
00B435AB  41 C7 00 01 D5 04 C0            mov dword ptr [r8], 0xc004d501
00B435B2  FF 03                           inc dword ptr [rbx]
00B435B4  4C 8D 73 04                     lea r14, [rbx + 4]
00B435B8  41 8B 06                        mov eax, dword ptr [r14]
00B435BB  85 C0                           test eax, eax
00B435BD  75 08                           jne 0x140b435c7
00B435BF  41 B8 3E 00 00 C0               mov r8d, 0xc000003e
00B435C5  EB 1E                           jmp 0x140b435e5
00B435C7  48 8B D0                        mov rdx, rax
00B435CA  B9 00 01 00 00                  mov ecx, 0x100
00B435CF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00B435D5  E8 16 EB 03 00                  call 0x140b820f0
00B435DA  48 85 C0                        test rax, rax
00B435DD  75 11                           jne 0x140b435f0
00B435DF  41 B8 17 00 00 C0               mov r8d, 0xc0000017
00B435E5  45 85 C0                        test r8d, r8d
00B435E8  0F 88 29 E0 F3 FF               js 0x140a81617
00B435EE  EB 0B                           jmp 0x140b435fb
00B435F0  48 89 43 08                     mov qword ptr [rbx + 8], rax
00B435F4  83 23 00                        and dword ptr [rbx], 0
00B435F7  4C 8D 73 04                     lea r14, [rbx + 4]
00B435FB  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00B435FF  48 85 D2                        test rdx, rdx
00B43602  74 2C                           je 0x140b43630
00B43604  44 8B 0B                        mov r9d, dword ptr [rbx]
00B43607  33 C9                           xor ecx, ecx
00B43609  41 3B C9                        cmp ecx, r9d
00B4360C  73 3D                           jae 0x140b4364b
00B4360E  8B 02                           mov eax, dword ptr [rdx]
00B43610  03 C5                           add eax, ebp
00B43612  3B C5                           cmp eax, ebp
00B43614  0F 82 F7 DF F3 FF               jb 0x140a81611
00B4361A  44 8B C0                        mov r8d, eax
00B4361D  4C 03 C2                        add r8, rdx
00B43620  4C 3B C2                        cmp r8, rdx
00B43623  0F 82 E8 DF F3 FF               jb 0x140a81611
00B43629  49 8B D0                        mov rdx, r8
00B4362C  FF C1                           inc ecx
00B4362E  EB D9                           jmp 0x140b43609
00B43630  41 8B 06                        mov eax, dword ptr [r14]
00B43633  8D 48 08                        lea ecx, [rax + 8]
00B43636  3B C8                           cmp ecx, eax
00B43638  72 08                           jb 0x140b43642
00B4363A  41 89 0E                        mov dword ptr [r14], ecx
00B4363D  E9 E7 E1 F3 FF                  jmp 0x140a81829
00B43642  41 83 0E FF                     or dword ptr [r14], 0xffffffff
00B43646  E9 C6 DF F3 FF                  jmp 0x140a81611
00B4364B  4C 8D 4A 04                     lea r9, [rdx + 4]
00B4364F  4C 3B CA                        cmp r9, rdx
00B43652  0F 82 B9 DF F3 FF               jb 0x140a81611
00B43658  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00B4365B  48 8D 42 08                     lea rax, [rdx + 8]
00B4365F  48 03 4B 08                     add rcx, qword ptr [rbx + 8]
00B43663  45 33 C0                        xor r8d, r8d
00B43666  48 3B C1                        cmp rax, rcx
00B43669  0F 87 C1 E1 F3 FF               ja 0x140a81830
00B4366F  89 2A                           mov dword ptr [rdx], ebp
00B43671  41 C7 01 01 D5 04 C0            mov dword ptr [r9], 0xc004d501
00B43678  E9 81 E1 F3 FF                  jmp 0x140a817fe
00B4367D  45 33 F6                        xor r14d, r14d
00B43680  E9 B4 E0 F3 FF                  jmp 0x140a81739
00B43685  44 8B 0B                        mov r9d, dword ptr [rbx]
00B43688  33 C9                           xor ecx, ecx
00B4368A  41 3B C9                        cmp ecx, r9d
00B4368D  73 22                           jae 0x140b436b1
00B4368F  8B 02                           mov eax, dword ptr [rdx]
00B43691  03 C5                           add eax, ebp
00B43693  3B C5                           cmp eax, ebp
00B43695  0F 82 76 DF F3 FF               jb 0x140a81611
00B4369B  44 8B C0                        mov r8d, eax
00B4369E  4C 03 C2                        add r8, rdx
00B436A1  4C 3B C2                        cmp r8, rdx
00B436A4  0F 82 67 DF F3 FF               jb 0x140a81611
00B436AA  49 8B D0                        mov rdx, r8
00B436AD  FF C1                           inc ecx
00B436AF  EB D9                           jmp 0x140b4368a
00B436B1  4C 8D 42 04                     lea r8, [rdx + 4]
00B436B5  4C 3B C2                        cmp r8, rdx
00B436B8  0F 82 53 DF F3 FF               jb 0x140a81611
00B436BE  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00B436C1  48 8D 42 08                     lea rax, [rdx + 8]
00B436C5  48 03 4B 08                     add rcx, qword ptr [rbx + 8]
00B436C9  48 3B C1                        cmp rax, rcx
00B436CC  0F 87 5E E1 F3 FF               ja 0x140a81830
00B436D2  89 2A                           mov dword ptr [rdx], ebp
00B436D4  41 C7 00 01 D5 04 C0            mov dword ptr [r8], 0xc004d501
00B436DB  FF 03                           inc dword ptr [rbx]
00B436DD  4C 8D 73 04                     lea r14, [rbx + 4]
00B436E1  41 8B 06                        mov eax, dword ptr [r14]
00B436E4  85 C0                           test eax, eax
00B436E6  75 08                           jne 0x140b436f0
00B436E8  41 B8 3E 00 00 C0               mov r8d, 0xc000003e
00B436EE  EB 1E                           jmp 0x140b4370e
00B436F0  48 8B D0                        mov rdx, rax
00B436F3  B9 00 01 00 00                  mov ecx, 0x100
00B436F8  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00B436FE  E8 ED E9 03 00                  call 0x140b820f0
00B43703  48 85 C0                        test rax, rax
00B43706  75 11                           jne 0x140b43719
00B43708  41 B8 17 00 00 C0               mov r8d, 0xc0000017
00B4370E  45 85 C0                        test r8d, r8d
00B43711  0F 88 00 DF F3 FF               js 0x140a81617
00B43717  EB 0B                           jmp 0x140b43724
00B43719  48 89 43 08                     mov qword ptr [rbx + 8], rax
00B4371D  83 23 00                        and dword ptr [rbx], 0
00B43720  4C 8D 73 04                     lea r14, [rbx + 4]
00B43724  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00B43728  48 85 D2                        test rdx, rdx
00B4372B  0F 84 FF FE FF FF               je 0x140b43630
00B43731  44 8B 0B                        mov r9d, dword ptr [rbx]
00B43734  33 C9                           xor ecx, ecx
00B43736  41 3B C9                        cmp ecx, r9d
00B43739  0F 83 0C FF FF FF               jae 0x140b4364b
00B4373F  8B 02                           mov eax, dword ptr [rdx]
00B43741  03 C5                           add eax, ebp
00B43743  3B C5                           cmp eax, ebp
00B43745  0F 82 C6 DE F3 FF               jb 0x140a81611
00B4374B  44 8B C0                        mov r8d, eax
00B4374E  4C 03 C2                        add r8, rdx
00B43751  4C 3B C2                        cmp r8, rdx
00B43754  0F 82 B7 DE F3 FF               jb 0x140a81611
00B4375A  49 8B D0                        mov rdx, r8
00B4375D  FF C1                           inc ecx
00B4375F  EB D5                           jmp 0x140b43736
00B43761  44 8B 13                        mov r10d, dword ptr [rbx]
00B43764  49 8B D0                        mov rdx, r8
00B43767  33 C9                           xor ecx, ecx
00B43769  41 3B CA                        cmp ecx, r10d
00B4376C  73 22                           jae 0x140b43790
00B4376E  8B 02                           mov eax, dword ptr [rdx]
00B43770  03 C5                           add eax, ebp
00B43772  3B C5                           cmp eax, ebp
00B43774  0F 82 97 DE F3 FF               jb 0x140a81611
00B4377A  44 8B C8                        mov r9d, eax
00B4377D  4C 03 CA                        add r9, rdx
00B43780  4C 3B CA                        cmp r9, rdx
00B43783  0F 82 88 DE F3 FF               jb 0x140a81611
00B43789  49 8B D1                        mov rdx, r9
00B4378C  FF C1                           inc ecx
00B4378E  EB D9                           jmp 0x140b43769
00B43790  4C 8D 4A 04                     lea r9, [rdx + 4]
00B43794  4C 3B CA                        cmp r9, rdx
00B43797  0F 82 74 DE F3 FF               jb 0x140a81611
00B4379D  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00B437A0  48 8D 42 08                     lea rax, [rdx + 8]
00B437A4  49 03 C8                        add rcx, r8
00B437A7  48 3B C1                        cmp rax, rcx
00B437AA  0F 87 80 E0 F3 FF               ja 0x140a81830
00B437B0  89 2A                           mov dword ptr [rdx], ebp
00B437B2  41 83 21 00                     and dword ptr [r9], 0
00B437B6  FF 03                           inc dword ptr [rbx]
00B437B8  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B437BB  85 C0                           test eax, eax
00B437BD  75 08                           jne 0x140b437c7
00B437BF  41 B8 3E 00 00 C0               mov r8d, 0xc000003e
00B437C5  EB 1E                           jmp 0x140b437e5
00B437C7  48 8B D0                        mov rdx, rax
00B437CA  B9 00 01 00 00                  mov ecx, 0x100
00B437CF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00B437D5  E8 16 E9 03 00                  call 0x140b820f0
00B437DA  48 85 C0                        test rax, rax
00B437DD  75 11                           jne 0x140b437f0
00B437DF  41 B8 17 00 00 C0               mov r8d, 0xc0000017
00B437E5  45 85 C0                        test r8d, r8d
00B437E8  0F 88 29 DE F3 FF               js 0x140a81617
00B437EE  EB 06                           jmp 0x140b437f6
00B437F0  49 89 06                        mov qword ptr [r14], rax
00B437F3  83 23 00                        and dword ptr [rbx], 0
00B437F6  49 8B 16                        mov rdx, qword ptr [r14]
00B437F9  48 85 D2                        test rdx, rdx
00B437FC  75 2F                           jne 0x140b4382d
00B437FE  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B43801  8D 48 08                        lea ecx, [rax + 8]
00B43804  3B C8                           cmp ecx, eax
00B43806  72 0A                           jb 0x140b43812
00B43808  89 4B 04                        mov dword ptr [rbx + 4], ecx
00B4380B  FF 03                           inc dword ptr [rbx]
00B4380D  45 33 C0                        xor r8d, r8d
00B43810  EB 0A                           jmp 0x140b4381c
00B43812  83 4B 04 FF                     or dword ptr [rbx + 4], 0xffffffff
00B43816  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00B4381C  45 85 C0                        test r8d, r8d
00B4381F  0F 88 F2 DD F3 FF               js 0x140a81617
00B43825  45 33 C0                        xor r8d, r8d
00B43828  E9 EA DD F3 FF                  jmp 0x140a81617
00B4382D  44 8B 0B                        mov r9d, dword ptr [rbx]
00B43830  33 C9                           xor ecx, ecx
00B43832  41 3B C9                        cmp ecx, r9d
00B43835  73 1A                           jae 0x140b43851
00B43837  8B 02                           mov eax, dword ptr [rdx]
00B43839  03 C5                           add eax, ebp
00B4383B  3B C5                           cmp eax, ebp
00B4383D  72 D7                           jb 0x140b43816
00B4383F  44 8B C0                        mov r8d, eax
00B43842  4C 03 C2                        add r8, rdx
00B43845  4C 3B C2                        cmp r8, rdx
00B43848  72 CC                           jb 0x140b43816
00B4384A  49 8B D0                        mov rdx, r8
00B4384D  FF C1                           inc ecx
00B4384F  EB E1                           jmp 0x140b43832
00B43851  4C 8D 4A 04                     lea r9, [rdx + 4]
00B43855  4C 3B CA                        cmp r9, rdx
00B43858  72 BC                           jb 0x140b43816
00B4385A  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00B4385D  48 8D 42 08                     lea rax, [rdx + 8]
00B43861  48 03 4B 08                     add rcx, qword ptr [rbx + 8]
00B43865  45 33 C0                        xor r8d, r8d
00B43868  48 3B C1                        cmp rax, rcx
00B4386B  76 08                           jbe 0x140b43875
00B4386D  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00B43873  EB A7                           jmp 0x140b4381c
00B43875  89 2A                           mov dword ptr [rdx], ebp
00B43877  45 21 01                        and dword ptr [r9], r8d
00B4387A  FF 03                           inc dword ptr [rbx]
00B4387C  EB 9E                           jmp 0x140b4381c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B4355C(int a1, __int64 a2)
{
    __int64 result;

    a1 = 0;
loc_00B43561:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) goto loc_00B43588;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + ((unsigned int)(v_rbp)));
    a3 = ((unsigned int)((unsigned int)(result))) + (a2);
    a1 = (unsigned int)((a1) + 1);
    goto loc_00B43561;
loc_00B43588:
    a1 = ((unsigned int)(*(unsigned int *)(v_rbx + 4))) + (*(unsigned __int64 *)(v_rbx + 8));
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    *(unsigned int *)(a3 + 4) = 0xC004D501ULL;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4))) != 0) goto loc_00B435C7;
    goto loc_00B435E5;
loc_00B435C7:
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rbx + 4)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_rbx)));
    if (result != 0) goto loc_00B435F0;
loc_00B435E5:
    goto loc_00B435FB;
loc_00B435F0:
    *(unsigned __int64 *)(v_rbx + 8) = result;
loc_00B435FB:
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_00B43630;
    a1 = 0;
loc_00B43609:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) goto loc_00B4364B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 8)))) + ((unsigned int)(v_rbp)));
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(v_rbx + 8));
    a1 = (unsigned int)((a1) + 1);
    goto loc_00B43609;
loc_00B43630:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4))))) goto loc_00B43642;
    *(unsigned int *)(v_rbx + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4)) + 8);
loc_00B43642:
loc_00B4364B:
    a1 = ((unsigned int)(*(unsigned int *)(v_rbx + 4))) + (*(unsigned __int64 *)(v_rbx + 8));
    a3 = 0;
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    *(unsigned int *)(a3 + 4) = 0xC004D501ULL;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B4355C(int32_t Arg1, int64_t Arg2)
{
    int64_t result;

    Arg1 = 0;
loc_00B43561:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) goto loc_00B43588;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + ((uint32_t)(local_rbp)));
    a3 = ((uint32_t)((uint32_t)(result))) + (Arg2);
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00B43561;
loc_00B43588:
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rbx + 0x4))) + (*(uint64_t *)(local_rbx + 0x8));
    *(uint32_t *)(a3) = (uint32_t)(local_rbp);
    *(uint32_t *)(a3 + 0x4) = 0xC004D501ULL;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4))) != 0) goto loc_00B435C7;
    goto loc_00B435E5;
loc_00B435C7:
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rbx + 0x4)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(local_rbx)));
    if (result != 0) goto loc_00B435F0;
loc_00B435E5:
    goto loc_00B435FB;
loc_00B435F0:
    *(uint64_t *)(local_rbx + 0x8) = result;
loc_00B435FB:
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_00B43630;
    Arg1 = 0;
loc_00B43609:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) goto loc_00B4364B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x8)))) + ((uint32_t)(local_rbp)));
    a3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(local_rbx + 0x8));
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00B43609;
loc_00B43630:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4))))) goto loc_00B43642;
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)) + 8);
loc_00B43642:
loc_00B4364B:
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rbx + 0x4))) + (*(uint64_t *)(local_rbx + 0x8));
    a3 = 0;
    *(uint32_t *)(a3) = (uint32_t)(local_rbp);
    *(uint32_t *)(a3 + 0x4) = 0xC004D501ULL;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B4355C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
