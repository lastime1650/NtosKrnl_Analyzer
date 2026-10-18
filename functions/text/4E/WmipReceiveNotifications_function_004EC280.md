# WmipReceiveNotifications

- RVA: `0x004EC280`–`0x004EC76C` (길이 `1,260` bytes)
- VA: `0x00000001404EC280`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D3218`
- 디코드: `329`개 명령, `1,260/1,260` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004EC2F6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004EC325` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x004EC38E` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x004EC446` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x004EC4AB` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x004EC4E8` → [WmipCompleteGuidIrpWithError](../49/WmipCompleteGuidIrpWithError_function_004955BC.md) (function, `0x004955BC`)
- `0x004EC519` → [Feature_2327208251__private_IsEnabledDeviceUsageNoInline](../64/Feature_2327208251__private_IsEnabledDeviceUsageNoInline_function_0064E4B4.md) (function, `0x0064E4B4`)
- `0x004EC538` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EC59A` → [WmipCopyFromEventQueues](../../page/A6/WmipCopyFromEventQueues_function_00A6C92C.md) (function, `0x00A6C92C`)
- `0x004EC5D8` → [WmipCopyFromEventQueues](../../page/A6/WmipCopyFromEventQueues_function_00A6C92C.md) (function, `0x00A6C92C`)
- `0x004EC689` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x004EC6A6` → [WmipClearIrpObjectList](../49/WmipClearIrpObjectList_function_00491D28.md) (function, `0x00491D28`)
- `0x004EC6C8` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x004EC6DE` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004EC6FE` → [KeReleaseMutant](../39/KeReleaseMutant_function_003967D0.md) (function, `0x003967D0`)
- `0x004EC716` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EC732` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EC744` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [WmipIoControl](../../page/9D/WmipIoControl_function_009DEBD0.md) at `0x009DEFDC`

### Static image references
- `0x004EC29F` → RVA `0x00E0A740` (`.data`; read)
- `0x004EC31C` → RVA `0x00EFFA60` (`.data`; read)
- `0x004EC368` → RVA `0x00FC6D70` (`ALMOSTRO`; read)
- `0x004EC676` → RVA `0x00EFFC20` (`.data`; read)
- `0x004EC68E` → RVA `0x00491BA0` (`WmipNotificationIrpCancel`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x004EC2F6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004EC38E` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x004EC59A` → [WmipCopyFromEventQueues](../../page/A6/WmipCopyFromEventQueues_function_00A6C92C.md) (`.text` → `PAGE`)
  - `0x004EC5D8` → [WmipCopyFromEventQueues](../../page/A6/WmipCopyFromEventQueues_function_00A6C92C.md) (`.text` → `PAGE`)
  - `0x004EC732` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004EC280  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004EC285  55                              push rbp
004EC286  56                              push rsi
004EC287  57                              push rdi
004EC288  41 54                           push r12
004EC28A  41 55                           push r13
004EC28C  41 56                           push r14
004EC28E  41 57                           push r15
004EC290  48 8D AC 24 40 FF FF FF         lea rbp, [rsp - 0xc0]
004EC298  48 81 EC C0 01 00 00            sub rsp, 0x1c0
004EC29F  48 8B 05 9A E4 91 00            mov rax, qword ptr [rip + 0x91e49a]
004EC2A6  48 33 C4                        xor rax, rsp
004EC2A9  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
004EC2B0  44 8B 29                        mov r13d, dword ptr [rcx]
004EC2B3  48 8D 41 08                     lea rax, [rcx + 8]
004EC2B7  8B 1A                           mov ebx, dword ptr [rdx]
004EC2B9  45 33 FF                        xor r15d, r15d
004EC2BC  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
004EC2C1  49 8B F0                        mov rsi, r8
004EC2C4  C7 44 24 64 0D 00 00 C0         mov dword ptr [rsp + 0x64], 0xc000000d
004EC2CC  48 8B F9                        mov rdi, rcx
004EC2CF  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
004EC2D4  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
004EC2D9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004EC2DE  41 83 FD 10                     cmp r13d, 0x10
004EC2E2  76 29                           jbe 0x1404ec30d
004EC2E4  41 8B D5                        mov edx, r13d
004EC2E7  B9 00 01 00 00                  mov ecx, 0x100
004EC2EC  48 C1 E2 04                     shl rdx, 4
004EC2F0  41 B8 57 6D 69 70               mov r8d, 0x70696d57
004EC2F6  E8 F5 5D 69 00                  call 0x140b820f0
004EC2FB  4C 8B F0                        mov r14, rax
004EC2FE  48 85 C0                        test rax, rax
004EC301  75 0E                           jne 0x1404ec311
004EC303  B8 9A 00 00 C0                  mov eax, 0xc000009a
004EC308  E9 2D 04 00 00                  jmp 0x1404ec73a
004EC30D  4C 8D 75 B0                     lea r14, [rbp - 0x50]
004EC311  45 33 C9                        xor r9d, r9d
004EC314  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
004EC319  45 33 C0                        xor r8d, r8d
004EC31C  48 8D 0D 3D 37 A1 00            lea rcx, [rip + 0xa1373d]
004EC323  33 D2                           xor edx, edx
004EC325  E8 86 23 D2 FF                  call 0x14020e6b0
004EC32A  41 8B C7                        mov eax, r15d
004EC32D  44 88 7C 24 50                  mov byte ptr [rsp + 0x50], r15b
004EC332  21 44 24 68                     and dword ptr [rsp + 0x68], eax
004EC336  45 8A E7                        mov r12b, r15b
004EC339  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
004EC33E  41 8B CF                        mov ecx, r15d
004EC341  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
004EC346  BA 01 00 00 00                  mov edx, 1
004EC34B  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
004EC34F  89 4C 24 5C                     mov dword ptr [rsp + 0x5c], ecx
004EC353  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
004EC357  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
004EC35B  45 85 ED                        test r13d, r13d
004EC35E  0F 84 3E 01 00 00               je 0x1404ec4a2
004EC364  48 8D 4F 08                     lea rcx, [rdi + 8]
004EC368  4C 8B 05 01 AA AD 00            mov r8, qword ptr [rip + 0xadaa01]
004EC36F  48 8D 45 90                     lea rax, [rbp - 0x70]
004EC373  48 8B 09                        mov rcx, qword ptr [rcx]
004EC376  44 8A CA                        mov r9b, dl
004EC379  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004EC37F  BA 04 00 00 00                  mov edx, 4
004EC384  48 83 65 90 00                  and qword ptr [rbp - 0x70], 0
004EC389  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EC38E  E8 1D CA 37 00                  call 0x140868db0
004EC393  33 D2                           xor edx, edx
004EC395  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
004EC399  44 8B E8                        mov r13d, eax
004EC39C  85 C0                           test eax, eax
004EC39E  0F 88 47 03 00 00               js 0x1404ec6eb
004EC3A4  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
004EC3A8  8B CA                           mov ecx, edx
004EC3AA  45 85 FF                        test r15d, r15d
004EC3AD  74 1C                           je 0x1404ec3cb
004EC3AF  49 8B C6                        mov rax, r14
004EC3B2  44 8D 42 01                     lea r8d, [rdx + 1]
004EC3B6  4C 3B 28                        cmp r13, qword ptr [rax]
004EC3B9  0F 84 71 01 00 00               je 0x1404ec530
004EC3BF  41 03 C8                        add ecx, r8d
004EC3C2  48 83 C0 10                     add rax, 0x10
004EC3C6  41 3B CF                        cmp ecx, r15d
004EC3C9  72 EB                           jb 0x1404ec3b6
004EC3CB  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
004EC3CF  B9 01 00 00 00                  mov ecx, 1
004EC3D4  49 39 55 48                     cmp qword ptr [r13 + 0x48], rdx
004EC3D8  0F B6 C0                        movzx eax, al
004EC3DB  0F 45 C1                        cmovne eax, ecx
004EC3DE  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
004EC3E2  41 8B C7                        mov eax, r15d
004EC3E5  44 03 F9                        add r15d, ecx
004EC3E8  48 03 C0                        add rax, rax
004EC3EB  4D 89 2C C6                     mov qword ptr [r14 + rax*8], r13
004EC3EF  49 39 55 60                     cmp qword ptr [r13 + 0x60], rdx
004EC3F3  74 11                           je 0x1404ec406
004EC3F5  41 39 55 74                     cmp dword ptr [r13 + 0x74], edx
004EC3F9  45 0F B6 E4                     movzx r12d, r12b
004EC3FD  44 0F 45 E1                     cmovne r12d, ecx
004EC401  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
004EC406  49 39 95 80 00 00 00            cmp qword ptr [r13 + 0x80], rdx
004EC40D  74 15                           je 0x1404ec424
004EC40F  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
004EC413  41 39 95 94 00 00 00            cmp dword ptr [r13 + 0x94], edx
004EC41A  0F B6 C0                        movzx eax, al
004EC41D  0F 45 C1                        cmovne eax, ecx
004EC420  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004EC424  41 8B 45 74                     mov eax, dword ptr [r13 + 0x74]
004EC428  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
004EC42D  83 C0 07                        add eax, 7
004EC430  23 C1                           and eax, ecx
004EC432  01 44 24 58                     add dword ptr [rsp + 0x58], eax
004EC436  41 8B 85 94 00 00 00            mov eax, dword ptr [r13 + 0x94]
004EC43D  83 C0 07                        add eax, 7
004EC440  23 C1                           and eax, ecx
004EC442  01 44 24 5C                     add dword ptr [rsp + 0x5c], eax
004EC446  E8 69 20 16 00                  call 0x14064e4b4
004EC44B  85 C0                           test eax, eax
004EC44D  74 24                           je 0x1404ec473
004EC44F  41 8B 45 74                     mov eax, dword ptr [r13 + 0x74]
004EC453  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
004EC458  83 C0 07                        add eax, 7
004EC45B  48 23 C1                        and rax, rcx
004EC45E  48 01 45 80                     add qword ptr [rbp - 0x80], rax
004EC462  41 8B 85 94 00 00 00            mov eax, dword ptr [r13 + 0x94]
004EC469  83 C0 07                        add eax, 7
004EC46C  48 23 C1                        and rax, rcx
004EC46F  48 01 45 88                     add qword ptr [rbp - 0x78], rax
004EC473  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
004EC477  BA 01 00 00 00                  mov edx, 1
004EC47C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004EC481  03 C2                           add eax, edx
004EC483  48 83 C1 08                     add rcx, 8
004EC487  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
004EC48B  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
004EC490  3B 44 24 48                     cmp eax, dword ptr [rsp + 0x48]
004EC494  0F 82 CE FE FF FF               jb 0x1404ec368
004EC49A  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
004EC49E  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
004EC4A2  44 8D 2C 01                     lea r13d, [rcx + rax]
004EC4A6  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
004EC4AB  E8 04 20 16 00                  call 0x14064e4b4
004EC4B0  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
004EC4B4  41 BA 01 00 00 00               mov r10d, 1
004EC4BA  48 03 4D 88                     add rcx, qword ptr [rbp - 0x78]
004EC4BE  F7 D8                           neg eax
004EC4C0  4D 1B E4                        sbb r12, r12
004EC4C3  4C 23 E1                        and r12, rcx
004EC4C6  44 38 54 24 60                  cmp byte ptr [rsp + 0x60], r10b
004EC4CB  75 3E                           jne 0x1404ec50b
004EC4CD  45 85 FF                        test r15d, r15d
004EC4D0  74 39                           je 0x1404ec50b
004EC4D2  41 8B C7                        mov eax, r15d
004EC4D5  4D 8B EE                        mov r13, r14
004EC4D8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004EC4DD  49 8B 4D 00                     mov rcx, qword ptr [r13]
004EC4E1  48 83 79 48 00                  cmp qword ptr [rcx + 0x48], 0
004EC4E6  74 10                           je 0x1404ec4f8
004EC4E8  E8 CF 90 FA FF                  call 0x1404955bc
004EC4ED  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004EC4F2  41 BA 01 00 00 00               mov r10d, 1
004EC4F8  49 83 C5 10                     add r13, 0x10
004EC4FC  49 2B C2                        sub rax, r10
004EC4FF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004EC504  75 D7                           jne 0x1404ec4dd
004EC506  44 8B 6C 24 48                  mov r13d, dword ptr [rsp + 0x48]
004EC50B  8A 44 24 54                     mov al, byte ptr [rsp + 0x54]
004EC50F  0A 44 24 50                     or al, byte ptr [rsp + 0x50]
004EC513  0F 84 FD 00 00 00               je 0x1404ec616
004EC519  E8 96 1F 16 00                  call 0x14064e4b4
004EC51E  85 C0                           test eax, eax
004EC520  75 20                           jne 0x1404ec542
004EC522  44 3B EB                        cmp r13d, ebx
004EC525  76 3D                           jbe 0x1404ec564
004EC527  44 89 6F 30                     mov dword ptr [rdi + 0x30], r13d
004EC52B  E9 C7 00 00 00                  jmp 0x1404ec5f7
004EC530  BA 44 66 6C 74                  mov edx, 0x746c6644
004EC535  49 8B CD                        mov rcx, r13
004EC538  E8 A3 B3 E0 FF                  call 0x1402f78e0
004EC53D  E9 31 FF FF FF                  jmp 0x1404ec473
004EC542  B8 FF FF FF FF                  mov eax, 0xffffffff
004EC547  4C 3B E0                        cmp r12, rax
004EC54A  76 0F                           jbe 0x1404ec55b
004EC54C  C7 44 24 64 95 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000095
004EC554  33 DB                           xor ebx, ebx
004EC556  E9 AA 00 00 00                  jmp 0x1404ec605
004EC55B  4C 3B E3                        cmp r12, rbx
004EC55E  0F 87 8F 00 00 00               ja 0x1404ec5f3
004EC564  45 33 E4                        xor r12d, r12d
004EC567  8B F3                           mov esi, ebx
004EC569  41 8B C4                        mov eax, r12d
004EC56C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004EC571  44 38 64 24 54                  cmp byte ptr [rsp + 0x54], r12b
004EC576  74 37                           je 0x1404ec5af
004EC578  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004EC57D  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
004EC582  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004EC587  4C 8B C7                        mov r8, rdi
004EC58A  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004EC58F  41 8B D7                        mov edx, r15d
004EC592  49 8B CE                        mov rcx, r14
004EC595  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EC59A  E8 8D 03 58 00                  call 0x140a6c92c
004EC59F  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
004EC5A3  48 03 F8                        add rdi, rax
004EC5A6  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004EC5AB  2B 74 24 40                     sub esi, dword ptr [rsp + 0x40]
004EC5AF  44 38 64 24 50                  cmp byte ptr [rsp + 0x50], r12b
004EC5B4  74 30                           je 0x1404ec5e6
004EC5B6  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004EC5BB  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
004EC5C0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004EC5C5  4C 8B C7                        mov r8, rdi
004EC5C8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004EC5CD  41 8B D7                        mov edx, r15d
004EC5D0  49 8B CE                        mov rcx, r14
004EC5D3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EC5D8  E8 4F 03 58 00                  call 0x140a6c92c
004EC5DD  2B 74 24 40                     sub esi, dword ptr [rsp + 0x40]
004EC5E1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004EC5E6  48 85 C0                        test rax, rax
004EC5E9  74 04                           je 0x1404ec5ef
004EC5EB  44 89 60 0C                     mov dword ptr [rax + 0xc], r12d
004EC5EF  2B DE                           sub ebx, esi
004EC5F1  EB 12                           jmp 0x1404ec605
004EC5F3  44 89 67 30                     mov dword ptr [rdi + 0x30], r12d
004EC5F7  BB 38 00 00 00                  mov ebx, 0x38
004EC5FC  C7 47 2C 20 00 00 00            mov dword ptr [rdi + 0x2c], 0x20
004EC603  89 1F                           mov dword ptr [rdi], ebx
004EC605  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004EC60A  44 8B 6C 24 64                  mov r13d, dword ptr [rsp + 0x64]
004EC60F  89 18                           mov dword ptr [rax], ebx
004EC611  E9 D5 00 00 00                  jmp 0x1404ec6eb
004EC616  33 C0                           xor eax, eax
004EC618  48 8D 4E 78                     lea rcx, [rsi + 0x78]
004EC61C  45 33 C9                        xor r9d, r9d
004EC61F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
004EC623  48 89 49 08                     mov qword ptr [rcx + 8], rcx
004EC627  0F 57 C0                        xorps xmm0, xmm0
004EC62A  48 89 09                        mov qword ptr [rcx], rcx
004EC62D  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
004EC631  45 85 FF                        test r15d, r15d
004EC634  74 35                           je 0x1404ec66b
004EC636  49 8B D6                        mov rdx, r14
004EC639  48 8B 02                        mov rax, qword ptr [rdx]
004EC63C  48 89 70 48                     mov qword ptr [rax + 0x48], rsi
004EC640  48 83 C0 50                     add rax, 0x50
004EC644  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
004EC648  49 39 08                        cmp qword ptr [r8], rcx
004EC64B  0F 85 14 01 00 00               jne 0x1404ec765
004EC651  48 89 08                        mov qword ptr [rax], rcx
004EC654  45 03 CA                        add r9d, r10d
004EC657  4C 89 40 08                     mov qword ptr [rax + 8], r8
004EC65B  48 83 C2 10                     add rdx, 0x10
004EC65F  49 89 00                        mov qword ptr [r8], rax
004EC662  48 89 41 08                     mov qword ptr [rcx + 8], rax
004EC666  45 3B CF                        cmp r9d, r15d
004EC669  72 CE                           jb 0x1404ec639
004EC66B  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
004EC672  48 8D 55 98                     lea rdx, [rbp - 0x68]
004EC676  48 8D 0D A3 35 A1 00            lea rcx, [rip + 0xa135a3]
004EC67D  32 DB                           xor bl, bl
004EC67F  41 BD 03 01 00 00               mov r13d, 0x103
004EC685  44 08 50 03                     or byte ptr [rax + 3], r10b
004EC689  E8 12 91 D8 FF                  call 0x1402757a0
004EC68E  48 8D 05 0B 55 FA FF            lea rax, [rip - 0x5aaf5]
004EC695  BF 20 01 00 C0                  mov edi, 0xc0000120
004EC69A  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
004EC69E  38 5E 44                        cmp byte ptr [rsi + 0x44], bl
004EC6A1  74 21                           je 0x1404ec6c4
004EC6A3  48 8B CE                        mov rcx, rsi
004EC6A6  E8 7D 56 FA FF                  call 0x140491d28
004EC6AB  33 C0                           xor eax, eax
004EC6AD  0F B6 DB                        movzx ebx, bl
004EC6B0  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
004EC6B4  48 85 C0                        test rax, rax
004EC6B7  41 B8 01 00 00 00               mov r8d, 1
004EC6BD  44 8B EF                        mov r13d, edi
004EC6C0  41 0F 45 D8                     cmovne ebx, r8d
004EC6C4  48 8D 4D 98                     lea rcx, [rbp - 0x68]
004EC6C8  E8 13 66 E5 FF                  call 0x140342ce0
004EC6CD  84 DB                           test bl, bl
004EC6CF  74 12                           je 0x1404ec6e3
004EC6D1  48 83 66 38 00                  and qword ptr [rsi + 0x38], 0
004EC6D6  33 D2                           xor edx, edx
004EC6D8  48 8B CE                        mov rcx, rsi
004EC6DB  89 7E 30                        mov dword ptr [rsi + 0x30], edi
004EC6DE  E8 DD EE DA FF                  call 0x14029b5c0
004EC6E3  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004EC6E8  83 20 00                        and dword ptr [rax], 0
004EC6EB  45 33 C9                        xor r9d, r9d
004EC6EE  48 8D 0D 6B 33 A1 00            lea rcx, [rip + 0xa1336b]
004EC6F5  45 33 C0                        xor r8d, r8d
004EC6F8  41 8D 71 01                     lea esi, [r9 + 1]
004EC6FC  8B D6                           mov edx, esi
004EC6FE  E8 CD A0 EA FF                  call 0x1403967d0
004EC703  45 85 FF                        test r15d, r15d
004EC706  74 1C                           je 0x1404ec724
004EC708  49 8B DE                        mov rbx, r14
004EC70B  41 8B FF                        mov edi, r15d
004EC70E  48 8B 0B                        mov rcx, qword ptr [rbx]
004EC711  BA 44 66 6C 74                  mov edx, 0x746c6644
004EC716  E8 C5 B1 E0 FF                  call 0x1402f78e0
004EC71B  48 8D 5B 10                     lea rbx, [rbx + 0x10]
004EC71F  48 2B FE                        sub rdi, rsi
004EC722  75 EA                           jne 0x1404ec70e
004EC724  48 8D 45 B0                     lea rax, [rbp - 0x50]
004EC728  4C 3B F0                        cmp r14, rax
004EC72B  74 0A                           je 0x1404ec737
004EC72D  33 D2                           xor edx, edx
004EC72F  49 8B CE                        mov rcx, r14
004EC732  E8 39 61 69 00                  call 0x140b82870
004EC737  41 8B C5                        mov eax, r13d
004EC73A  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
004EC741  48 33 CC                        xor rcx, rsp
004EC744  E8 F7 FE 1B 00                  call 0x1406ac640
004EC749  48 8B 9C 24 18 02 00 00         mov rbx, qword ptr [rsp + 0x218]
004EC751  48 81 C4 C0 01 00 00            add rsp, 0x1c0
004EC758  41 5F                           pop r15
004EC75A  41 5E                           pop r14
004EC75C  41 5D                           pop r13
004EC75E  41 5C                           pop r12
004EC760  5F                              pop rdi
004EC761  5E                              pop rsi
004EC762  5D                              pop rbp
004EC763  C3                              ret
004EC764  CC                              int3
004EC765  B9 03 00 00 00                  mov ecx, 3
004EC76A  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipReceiveNotifications(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int8 v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int8 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 9561242)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_stack_m180 = a2;
    v_stack_m194 = 0xC000000DULL;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m188 = a1 + 8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) <= 16) goto loc_004EC30D;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) << (4);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x70696D57ULL), a4);
    if (result != 0) goto loc_004EC311;
    goto loc_004EC73A;
loc_004EC30D:
loc_004EC311:
    a4 = 0;
    v_stack_m1D8 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 10565437, a2, a3, a4);
    v_stack_m1A8 = 0;
    v_stack_m1A4 = 0;
    v_stack_m198 = 0;
    v_stack_m1A0 = 0;
    v_stack_m19C = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_004EC4A2;
loc_004EC368:
    v_stack_m1D8 = v_stack_m168;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a1 + 8), 4, *(unsigned __int64 *)(v_rip + 11381249), 1);
    a2 = 0;
    v_stack_m194 = (unsigned int)(result);
    if (sign_flag) goto loc_004EC6EB;
    if (0 == 0) goto loc_004EC3CB;
loc_004EC3B6:
    if (v_stack_m168 == (*(unsigned __int64 *)(v_stack_m148))) goto loc_004EC530;
    a1 = (unsigned int)((0) + ((unsigned int)(a2 + 1)));
    result = (v_stack_m148) + (16);
    if (((unsigned int)(a1)) < 0) goto loc_004EC3B6;
loc_004EC3CB:
    result = (unsigned __int8)((unsigned int)(v_stack_m198));
    if ((*(unsigned __int64 *)(v_stack_m168 + 72)) != 0) { result = 1; }
    v_stack_m198 = (unsigned int)(result);
    v_r15 = (unsigned int)((v_r15) + (1));
    result = (0) + (0);
    *(unsigned __int64 *)(v_stack_m148 + result * 8) = v_stack_m168;
    v_r12 = 0;
    if ((*(unsigned __int64 *)(v_stack_m168 + 96)) != 0) {
        v_r12 = 0;
        if ((*(unsigned int *)(v_stack_m168 + 116)) != 0) { v_r12 = 1; }
        v_stack_m1A4 = (unsigned int)(v_r12);
    }
    if ((*(unsigned __int64 *)(v_stack_m168 + 128)) != 0) {
        result = v_stack_m1A8;
        result = (unsigned __int8)(result);
        if ((*(unsigned int *)(v_stack_m168 + 148)) != 0) { result = 1; }
        v_stack_m1A8 = (unsigned int)(result);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m168 + 116))) + (7));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m168 + 148))) + (7));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((unsigned int)(0xFFFFFFF8ULL), a2, a2 + 1, 1);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned int *)(v_stack_m168 + 116);
        a1 = 0xFFFFFFF8ULL;
        result = (unsigned int)((result) + (7));
        result = (result) & (a1);
        result = *(unsigned int *)(v_stack_m168 + 148);
        result = (unsigned int)((result) + (7));
        result = (result) & (a1);
    }
    result = (unsigned int)(((unsigned int)(v_stack_m190)) + (1));
    a1 = (v_stack_m188) + (8);
    v_stack_m190 = (unsigned int)(result);
    v_stack_m188 = a1;
    if (((unsigned int)(result)) < v_stack_m1B0) goto loc_004EC368;
loc_004EC4A2:
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m19C) + (unsigned int)(v_stack_m1A0) * 1);
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_m19C), 1, a2 + 1, 1);
    a1 = (v_stack_m178) + (v_stack_m170);
    result = (unsigned int)(-(result));
    v_r12 = (v_r12) & (a1);
    if (v_stack_m198 != 1) goto loc_004EC50B;
    if ((unsigned int)(v_r15) == 0) goto loc_004EC50B;
    v_stack_m188 = (unsigned int)((unsigned int)(v_r15));
loc_004EC4DD:
    result = (unsigned int)((unsigned int)(v_r15));
    v_r10 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m148) + 72)) != 0) {
        result = WmipCompleteGuidIrpWithError(*(unsigned __int64 *)(v_stack_m148), 1, a2 + 1, 1);
        result = v_stack_m188;
        v_r10 = 1;
    }
    v_r13 = (v_stack_m148) + (16);
    result = (result) - (v_r10);
    v_stack_m188 = result;
    if (condition_is_not_equal) goto loc_004EC4DD;
loc_004EC50B:
    result = (unsigned __int8)((v_stack_m1A4) | (v_stack_m1A8));
    if (condition_is_equal) goto loc_004EC616;
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_m148), 1, a2 + 1, 1);
    if ((unsigned int)(result) != 0) goto loc_004EC542;
    if (((unsigned int)((unsigned int)(v_stack_m1B0))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_004EC564;
    *(unsigned int *)(a1 + 48) = (unsigned int)((unsigned int)(v_stack_m1B0));
    goto loc_004EC5F7;
loc_004EC530:
    result = ObfDereferenceObjectWithTag((unsigned int)(v_stack_m1B0), (unsigned int)(0x746C6644ULL), a2 + 1, 1);
    goto loc_004EC473;
loc_004EC542:
    if (v_r12 <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_004EC55B;
    v_stack_m194 = 0xC0000095ULL;
    v_rbx = 0;
    goto loc_004EC605;
loc_004EC55B:
    if (v_r12 > 0) goto loc_004EC5F3;
loc_004EC564:
    v_r12 = 0;
    v_stack_m1B0 = 0;
    result = 0;
    v_rsi = 0;
    v_rdi = a1;
    if (v_stack_m1A4 != 0) {
        result = v_stack_m1B0;
        v_stack_m1C8 = 1;
        v_stack_m1D0 = result;
        a3 = a1;
        result = v_stack_m1B8;
        a2 = (unsigned int)(v_r15);
        a1 = v_stack_m148;
        v_stack_m1D8 = result;
        result = WmipCopyFromEventQueues(a1, a2, a3, 1);
        result = v_stack_m1B8;
        v_rdi = (a1) + (result);
        result = v_stack_m1B0;
        v_rsi = (unsigned int)((0) - (v_stack_m1B8));
    }
    if (v_stack_m1A8 != 0) {
        result = v_stack_m1B0;
        v_stack_m1C8 = 0;
        v_stack_m1D0 = result;
        a3 = v_rdi;
        result = v_stack_m1B8;
        a2 = (unsigned int)(v_r15);
        a1 = v_stack_m148;
        v_stack_m1D8 = result;
        result = WmipCopyFromEventQueues(a1, a2, a3, 1);
        v_rsi = (unsigned int)((v_rsi) - (v_stack_m1B8));
        result = v_stack_m1B0;
    }
    if (result != 0) {
        *(unsigned int *)(result + 12) = 0;
    }
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_rsi)));
    goto loc_004EC605;
loc_004EC5F3:
    *(unsigned int *)(v_rdi + 48) = 0;
loc_004EC5F7:
    *(unsigned int *)(v_rdi + 44) = 32;
    *(unsigned int *)(v_rdi) = 56;
loc_004EC605:
    *(unsigned int *)(v_stack_m180) = 56;
    goto loc_004EC6EB;
loc_004EC616:
    result = 0;
    a4 = 0;
    v_stack_m150 = 0;
    *(unsigned __int64 *)(v_rsi + 120 + 8) = v_rsi + 120;
    *(unsigned __int64 *)(v_rsi + 120) = v_rsi + 120;
    v_stack_m160 = v_xmm0;
    if ((unsigned int)(v_r15) == 0) goto loc_004EC66B;
loc_004EC639:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m148) + 72) = v_rsi;
    result = (*(unsigned __int64 *)(v_stack_m148)) + (80);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 120 + 8))) != (v_rsi + 120)) goto loc_004EC765;
    *(unsigned __int64 *)(result) = v_rsi + 120;
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r10)));
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rsi + 120 + 8);
    a2 = (v_stack_m148) + (16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 120 + 8)) = result;
    *(unsigned __int64 *)(v_rsi + 120 + 8) = result;
    if (a4 < ((unsigned int)(v_r15))) goto loc_004EC639;
loc_004EC66B:
    v_rbx = 0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10565027, v_stack_m160, *(unsigned __int64 *)(v_rsi + 120 + 8), a4);
    result = v_rip - 371445;
    v_r13 = 259;
    if ((*(unsigned __int8 *)(v_rsi + 68)) != 0) {
        a1 = v_rsi;
        result = WmipClearIrpObjectList(a1, v_stack_m160, *(unsigned __int64 *)(v_rsi + 120 + 8), a4);
        result = 0;
        v_rbx = 0;
        a3 = 1;
        v_r13 = (unsigned int)((unsigned int)(0xC0000120ULL));
        if (0 != 0) { v_rbx = (unsigned int)(a3); }
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m160, v_stack_m160, a3, a4);
    if ((unsigned __int8)(v_rbx) != 0) {
        a2 = 0;
        a1 = v_rsi;
        *(unsigned int *)(v_rsi + 48) = (unsigned int)((unsigned int)(0xC0000120ULL));
        result = IofCompleteRequest(a1, a2, a3, a4);
    }
loc_004EC6EB:
    a4 = 0;
    a3 = 0;
    result = KeReleaseMutant(v_rip + 10564459, (unsigned int)((unsigned int)(a4 + 1)), a3, a4);
    if ((unsigned int)(v_r15) == 0) goto loc_004EC724;
loc_004EC70E:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m148), (unsigned int)(0x746C6644ULL), a3, a4);
    v_rdi = ((unsigned int)((unsigned int)(v_r15))) - (a4 + 1);
    if (condition_is_not_equal) goto loc_004EC70E;
loc_004EC724:
    result = v_stack_m148;
    if (v_stack_m148 != v_stack_m148) {
        a2 = 0;
        a1 = v_stack_m148;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
loc_004EC73A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (448);
    return result;
loc_004EC765:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmipReceiveNotifications(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint8_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint8_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x91E49A)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    v_stack_m180 = Arg2;
    v_stack_m194 = 0xC000000DULL;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m188 = Arg1 + 8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) <= 16) goto loc_004EC30D;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) << (4);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x70696D57ULL), Arg4);
    if (result != 0) goto loc_004EC311;
    goto loc_004EC73A;
loc_004EC30D:
loc_004EC311:
    Arg4 = 0;
    v_stack_m1D8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 10565437, Arg2, Arg3, Arg4);
    v_stack_m1A8 = 0;
    v_stack_m1A4 = 0;
    v_stack_m198 = 0;
    v_stack_m1A0 = 0;
    v_stack_m19C = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_004EC4A2;
loc_004EC368:
    v_stack_m1D8 = v_stack_m168;
    result = ObReferenceObjectByHandle(*(uint64_t *)(arg1 + 0x8), 4, *(uint64_t *)(v_rip + 0xADAA01), 1);
    Arg2 = 0;
    v_stack_m194 = (uint32_t)(result);
    if (sign_flag) goto loc_004EC6EB;
    if (0 == 0) goto loc_004EC3CB;
loc_004EC3B6:
    if (v_stack_m168 == (*(uint64_t *)(v_stack_m148))) goto loc_004EC530;
    Arg1 = (uint32_t)((0) + ((uint32_t)(Arg2 + 1)));
    result = (v_stack_m148) + (16);
    if (((uint32_t)(Arg1)) < 0) goto loc_004EC3B6;
loc_004EC3CB:
    result = (uint8_t)((uint32_t)(v_stack_m198));
    if ((*(uint64_t *)(v_stack_m168 + 0x48)) != 0) { result = 1; }
    v_stack_m198 = (uint32_t)(result);
    local_r15 = (uint32_t)((local_r15) + (1));
    result = (0) + (0);
    *(uint64_t *)(v_stack_m148 + result * 8) = v_stack_m168;
    local_r12 = 0;
    if ((*(uint64_t *)(v_stack_m168 + 0x60)) != 0) {
        local_r12 = 0;
        if ((*(uint32_t *)(v_stack_m168 + 0x74)) != 0) { local_r12 = 1; }
        v_stack_m1A4 = (uint32_t)(local_r12);
    }
    if ((*(uint64_t *)(v_stack_m168 + 0x80)) != 0) {
        result = v_stack_m1A8;
        result = (uint8_t)(result);
        if ((*(uint32_t *)(v_stack_m168 + 0x94)) != 0) { result = 1; }
        v_stack_m1A8 = (uint32_t)(result);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x74))) + (7));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x94))) + (7));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((uint32_t)(0xFFFFFFF8ULL), Arg2, Arg2 + 1, 1);
    if ((uint32_t)(result) != 0) {
        result = *(uint32_t *)(v_stack_m168 + 0x74);
        Arg1 = 0xFFFFFFF8ULL;
        result = (uint32_t)((result) + (7));
        result = (result) & (Arg1);
        result = *(uint32_t *)(v_stack_m168 + 0x94);
        result = (uint32_t)((result) + (7));
        result = (result) & (Arg1);
    }
    result = (uint32_t)(((uint32_t)(v_stack_m190)) + (1));
    Arg1 = (v_stack_m188) + (8);
    v_stack_m190 = (uint32_t)(result);
    v_stack_m188 = Arg1;
    if (((uint32_t)(result)) < v_stack_m1B0) goto loc_004EC368;
loc_004EC4A2:
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m19C) + (uint32_t)(v_stack_m1A0) * 1);
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_m19C), 1, Arg2 + 1, 1);
    Arg1 = (v_stack_m178) + (v_stack_m170);
    result = (uint32_t)(-(result));
    local_r12 = (local_r12) & (Arg1);
    if (v_stack_m198 != 1) goto loc_004EC50B;
    if ((uint32_t)(local_r15) == 0) goto loc_004EC50B;
    v_stack_m188 = (uint32_t)((uint32_t)(local_r15));
loc_004EC4DD:
    result = (uint32_t)((uint32_t)(local_r15));
    local_r10 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m148) + 0x48)) != 0) {
        result = WmipCompleteGuidIrpWithError(*(uint64_t *)(v_stack_m148), 1, Arg2 + 1, 1);
        result = v_stack_m188;
        local_r10 = 1;
    }
    local_r13 = (v_stack_m148) + (16);
    result = (result) - (local_r10);
    v_stack_m188 = result;
    if (condition_is_not_equal) goto loc_004EC4DD;
loc_004EC50B:
    result = (uint8_t)((v_stack_m1A4) | (v_stack_m1A8));
    if (condition_is_equal) goto loc_004EC616;
    result = Feature_2327208251__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_m148), 1, Arg2 + 1, 1);
    if ((uint32_t)(result) != 0) goto loc_004EC542;
    if (((uint32_t)((uint32_t)(v_stack_m1B0))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_004EC564;
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)((uint32_t)(v_stack_m1B0));
    goto loc_004EC5F7;
loc_004EC530:
    result = ObfDereferenceObjectWithTag((uint32_t)(v_stack_m1B0), (uint32_t)(0x746C6644ULL), Arg2 + 1, 1);
    goto loc_004EC473;
loc_004EC542:
    if (local_r12 <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_004EC55B;
    v_stack_m194 = 0xC0000095ULL;
    local_rbx = 0;
    goto loc_004EC605;
loc_004EC55B:
    if (local_r12 > 0) goto loc_004EC5F3;
loc_004EC564:
    local_r12 = 0;
    v_stack_m1B0 = 0;
    result = 0;
    local_rsi = 0;
    local_rdi = Arg1;
    if (v_stack_m1A4 != 0) {
        result = v_stack_m1B0;
        v_stack_m1C8 = 1;
        v_stack_m1D0 = result;
        Arg3 = Arg1;
        result = v_stack_m1B8;
        Arg2 = (uint32_t)(local_r15);
        Arg1 = v_stack_m148;
        v_stack_m1D8 = result;
        result = WmipCopyFromEventQueues(Arg1, Arg2, Arg3, 1);
        result = v_stack_m1B8;
        local_rdi = (Arg1) + (result);
        result = v_stack_m1B0;
        local_rsi = (uint32_t)((0) - (v_stack_m1B8));
    }
    if (v_stack_m1A8 != 0) {
        result = v_stack_m1B0;
        v_stack_m1C8 = 0;
        v_stack_m1D0 = result;
        Arg3 = local_rdi;
        result = v_stack_m1B8;
        Arg2 = (uint32_t)(local_r15);
        Arg1 = v_stack_m148;
        v_stack_m1D8 = result;
        result = WmipCopyFromEventQueues(Arg1, Arg2, Arg3, 1);
        local_rsi = (uint32_t)((local_rsi) - (v_stack_m1B8));
        result = v_stack_m1B0;
    }
    if (result != 0) {
        *(uint32_t *)(result + 0xC) = 0;
    }
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_rsi)));
    goto loc_004EC605;
loc_004EC5F3:
    *(uint32_t *)(local_rdi + 0x30) = 0;
loc_004EC5F7:
    *(uint32_t *)(local_rdi + 0x2C) = 32;
    *(uint32_t *)(local_rdi) = 56;
loc_004EC605:
    *(uint32_t *)(v_stack_m180) = 56;
    goto loc_004EC6EB;
loc_004EC616:
    result = 0;
    Arg4 = 0;
    v_stack_m150 = 0;
    *(uint64_t *)(local_rsi + 0x78 + 0x8) = local_rsi + 120;
    *(uint64_t *)(local_rsi + 0x78) = local_rsi + 120;
    v_stack_m160 = v_xmm0;
    if ((uint32_t)(local_r15) == 0) goto loc_004EC66B;
loc_004EC639:
    *(uint64_t *)(*(uint64_t *)(v_stack_m148) + 0x48) = local_rsi;
    result = (*(uint64_t *)(v_stack_m148)) + (80);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x78 + 0x8))) != (local_rsi + 120)) goto loc_004EC765;
    *(uint64_t *)(result) = local_rsi + 120;
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(local_r10)));
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(local_rsi + 0x78 + 0x8);
    Arg2 = (v_stack_m148) + (16);
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x78 + 0x8)) = result;
    *(uint64_t *)(local_rsi + 0x78 + 0x8) = result;
    if (Arg4 < ((uint32_t)(local_r15))) goto loc_004EC639;
loc_004EC66B:
    local_rbx = 0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10565027, v_stack_m160, *(uint64_t *)(local_rsi + 0x78 + 0x8), Arg4);
    result = v_rip - 371445;
    local_r13 = 259;
    if ((*(uint8_t *)(local_rsi + 0x44)) != 0) {
        Arg1 = local_rsi;
        result = WmipClearIrpObjectList(Arg1, v_stack_m160, *(uint64_t *)(local_rsi + 0x78 + 0x8), Arg4);
        result = 0;
        local_rbx = 0;
        Arg3 = 1;
        local_r13 = (uint32_t)((uint32_t)(0xC0000120ULL));
        if (0 != 0) { local_rbx = (uint32_t)(Arg3); }
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m160, v_stack_m160, Arg3, Arg4);
    if ((uint8_t)(local_rbx) != 0) {
        Arg2 = 0;
        Arg1 = local_rsi;
        *(uint32_t *)(local_rsi + 0x30) = (uint32_t)((uint32_t)(0xC0000120ULL));
        result = IofCompleteRequest(Arg1, Arg2, Arg3, Arg4);
    }
loc_004EC6EB:
    Arg4 = 0;
    Arg3 = 0;
    result = KeReleaseMutant(v_rip + 10564459, (uint32_t)((uint32_t)(Arg4 + 1)), Arg3, Arg4);
    if ((uint32_t)(local_r15) == 0) goto loc_004EC724;
loc_004EC70E:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_m148), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    local_rdi = ((uint32_t)((uint32_t)(local_r15))) - (Arg4 + 1);
    if (condition_is_not_equal) goto loc_004EC70E;
loc_004EC724:
    result = v_stack_m148;
    if (v_stack_m148 != v_stack_m148) {
        Arg2 = 0;
        Arg1 = v_stack_m148;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
loc_004EC73A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (448);
    return result;
loc_004EC765:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `W` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg3` | `+ 0x38` | `64` | `R/W` |
| `Arg3` | `+ 0x44` | `8` | `R` |
| `Arg3` | `+ 0x68` | `64` | `R/W` |
| `Arg3` | `+ 0x78` | `64` | `R` |
| `Arg3` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004EC280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
