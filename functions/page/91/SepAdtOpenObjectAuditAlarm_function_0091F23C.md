# SepAdtOpenObjectAuditAlarm

- RVA: `0x0091F23C`–`0x0091F940` (길이 `1,796` bytes)
- VA: `0x000000014091F23C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008B51C`
- 디코드: `414`개 명령, `1,796/1,796` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0091F2C5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091F32F` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x0091F345` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0091F37E` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (function, `0x0047C7E0`)
- `0x0091F38B` → [PsGetAllocatedFullProcessImageNameEx](PsGetAllocatedFullProcessImageNameEx_function_0091D6F0.md) (function, `0x0091D6F0`)
- `0x0091F4C3` → [ObNormalizeHandleValue](ObNormalizeHandleValue_function_0091E6A8.md) (function, `0x0091E6A8`)
- `0x0091F55A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0091F573` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091F732` → [SepAdtLogAuditRecord](../../text/22/SepAdtLogAuditRecord_function_00224B6C.md) (function, `0x00224B6C`)
- `0x0091F74A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F837` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091F853` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091F8D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F8E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F8FA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F912` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F92A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0091F936` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)

### Direct callers
- [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) at `0x0086D36F`
- [sub_0086E95E](../86/Unknown_function_0086E95E.md) at `0x0086ED13`
- [sub_0091EFFE](Unknown_function_0091EFFE.md) at `0x0091F149`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1D43D`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1D537`
- [sub_00B29542](../B2/Unknown_function_00B29542.md) at `0x00B29656`
- [sub_00B2983E](../B2/Unknown_function_00B2983E.md) at `0x00B29922`
- [sub_00B46176](../B4/Unknown_function_00B46176.md) at `0x00B462E1`

### Static image references
- `0x0091F262` → RVA `0x00E0A740` (`.data`; read)
- `0x0091F40A` → RVA `0x000013A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0091F2C5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091F345` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0091F37E` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (`PAGE` → `.text`)
  - `0x0091F55A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0091F573` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091F732` → [SepAdtLogAuditRecord](../../text/22/SepAdtLogAuditRecord_function_00224B6C.md) (`PAGE` → `.text`)
  - `0x0091F74A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0091F837` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091F853` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091F8D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0091F8E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0091F8FA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0091F912` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0091F92A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0091F527` → [sub_00B21BFA + 0x1B](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F5AC` → [sub_00B21BFA + 0x85](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F725` → [sub_00B21BFA + 0x211](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F7F0` → [sub_00B21BFA](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F802` → [sub_00B21BFA](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F808` → [sub_00B21BFA + 0x7](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)
  - `0x0091F8CC` → [sub_00B21BFA + 0xE6](../B2/Unknown_function_00B21BFA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0091F23C  48 8B C4                        mov rax, rsp
0091F23F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0091F243  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0091F247  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0091F24B  55                              push rbp
0091F24C  41 54                           push r12
0091F24E  41 55                           push r13
0091F250  41 56                           push r14
0091F252  41 57                           push r15
0091F254  48 8D A8 E8 FB FF FF            lea rbp, [rax - 0x418]
0091F25B  48 81 EC F0 04 00 00            sub rsp, 0x4f0
0091F262  48 8B 05 D7 B4 4E 00            mov rax, qword ptr [rip + 0x4eb4d7]
0091F269  48 33 C4                        xor rax, rsp
0091F26C  48 89 85 E0 03 00 00            mov qword ptr [rbp + 0x3e0], rax
0091F273  4C 8B BD 48 04 00 00            mov r15, qword ptr [rbp + 0x448]
0091F27A  4C 8B EA                        mov r13, rdx
0091F27D  48 8B 85 B0 04 00 00            mov rax, qword ptr [rbp + 0x4b0]
0091F284  33 D2                           xor edx, edx
0091F286  48 8B B5 58 04 00 00            mov rsi, qword ptr [rbp + 0x458]
0091F28D  4D 8B E1                        mov r12, r9
0091F290  48 8B BD A8 04 00 00            mov rdi, qword ptr [rbp + 0x4a8]
0091F297  4C 8B B5 50 04 00 00            mov r14, qword ptr [rbp + 0x450]
0091F29E  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0091F2A3  41 B8 18 04 00 00               mov r8d, 0x418
0091F2A9  66 89 4C 24 24                  mov word ptr [rsp + 0x24], cx
0091F2AE  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0091F2B2  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0091F2B6  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091F2BB  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0091F2C0  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0091F2C5  E8 76 79 DA FF                  call 0x1406c6c40
0091F2CA  8A 85 78 04 00 00               mov al, byte ptr [rbp + 0x478]
0091F2D0  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0091F2D4  33 C9                           xor ecx, ecx
0091F2D6  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0091F2DA  8B D9                           mov ebx, ecx
0091F2DC  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0091F2E1  84 C0                           test al, al
0091F2E3  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0091F2E8  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0091F2EC  0F 57 C0                        xorps xmm0, xmm0
0091F2EF  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
0091F2F3  41 0F 94 C0                     sete r8b
0091F2F7  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0091F2FB  8A D0                           mov dl, al
0091F2FD  89 4C 24 2C                     mov dword ptr [rsp + 0x2c], ecx
0091F301  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0091F306  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0091F30B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0091F310  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0091F315  88 4C 24 21                     mov byte ptr [rsp + 0x21], cl
0091F319  88 4C 24 22                     mov byte ptr [rsp + 0x22], cl
0091F31D  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
0091F321  8D 4B 7C                        lea ecx, [rbx + 0x7c]
0091F324  0F 11 85 D0 03 00 00            movups xmmword ptr [rbp + 0x3d0], xmm0
0091F32B  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0091F32F  E8 8C 17 F5 FF                  call 0x140870ac0
0091F334  84 C0                           test al, al
0091F336  75 34                           jne 0x14091f36c
0091F338  8D 43 01                        lea eax, [rbx + 1]
0091F33B  48 8B 8D E0 03 00 00            mov rcx, qword ptr [rbp + 0x3e0]
0091F342  48 33 CC                        xor rcx, rsp
0091F345  E8 F6 D2 D8 FF                  call 0x1406ac640
0091F34A  4C 8D 9C 24 F0 04 00 00         lea r11, [rsp + 0x4f0]
0091F352  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0091F356  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0091F35A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0091F35E  49 8B E3                        mov rsp, r11
0091F361  41 5F                           pop r15
0091F363  41 5E                           pop r14
0091F365  41 5D                           pop r13
0091F367  41 5C                           pop r12
0091F369  5D                              pop rbp
0091F36A  C3                              ret
0091F36B  CC                              int3
0091F36C  48 85 FF                        test rdi, rdi
0091F36F  48 8D 85 D0 03 00 00            lea rax, [rbp + 0x3d0]
0091F376  48 0F 45 C7                     cmovne rax, rdi
0091F37A  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0091F37E  E8 5D D4 B5 FF                  call 0x14047c7e0
0091F383  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
0091F388  48 8B C8                        mov rcx, rax
0091F38B  E8 60 E3 FF FF                  call 0x14091d6f0
0091F390  8B F8                           mov edi, eax
0091F392  BE 01 00 00 00                  mov esi, 1
0091F397  85 C0                           test eax, eax
0091F399  0F 88 7E 04 00 00               js 0x14091f81d
0091F39F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0091F3A4  4D 85 F6                        test r14, r14
0091F3A7  0F 84 F1 03 00 00               je 0x14091f79e
0091F3AD  49 8B 5E 18                     mov rbx, qword ptr [r14 + 0x18]
0091F3B1  49 8B 86 98 00 00 00            mov rax, qword ptr [r14 + 0x98]
0091F3B8  4C 8B 00                        mov r8, qword ptr [rax]
0091F3BB  41 BB 08 00 00 00               mov r11d, 8
0091F3C1  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0091F3C5  41 8B CB                        mov ecx, r11d
0091F3C8  44 0F B7 54 24 24               movzx r10d, word ptr [rsp + 0x24]
0091F3CE  C7 45 B4 30 12 00 00            mov dword ptr [rbp - 0x4c], 0x1230
0091F3D5  45 8D 4B FA                     lea r9d, [r11 - 6]
0091F3D9  66 44 89 55 C0                  mov word ptr [rbp - 0x40], r10w
0091F3DE  44 39 8D 88 04 00 00            cmp dword ptr [rbp + 0x488], r9d
0091F3E5  41 8D 53 FB                     lea edx, [r11 - 5]
0091F3E9  44 8A 8D 78 04 00 00            mov r9b, byte ptr [rbp + 0x478]
0091F3F0  0F 44 CA                        cmove ecx, edx
0091F3F3  66 44 89 5D C2                  mov word ptr [rbp - 0x3e], r11w
0091F3F8  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
0091F3FB  8D 4A 0D                        lea ecx, [rdx + 0xd]
0091F3FE  45 84 C9                        test r9b, r9b
0091F401  75 04                           jne 0x14091f407
0091F403  66 89 4D C2                     mov word ptr [rbp - 0x3e], cx
0091F407  4D 85 ED                        test r13, r13
0091F40A  48 8D 15 97 1F 6E FF            lea rdx, [rip - 0x91e069]
0091F411  41 BB 04 00 00 00               mov r11d, 4
0091F417  49 0F 45 D5                     cmovne rdx, r13
0091F41B  44 89 5D C8                     mov dword ptr [rbp - 0x38], r11d
0091F41F  41 0F B6 48 01                  movzx ecx, byte ptr [r8 + 1]
0091F424  45 33 ED                        xor r13d, r13d
0091F427  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
0091F42B  89 75 E8                        mov dword ptr [rbp - 0x18], esi
0091F42E  48 89 55 00                     mov qword ptr [rbp], rdx
0091F432  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
0091F439  C7 45 08 05 00 00 00            mov dword ptr [rbp + 8], 5
0091F440  89 4D CC                        mov dword ptr [rbp - 0x34], ecx
0091F443  0F B7 0A                        movzx ecx, word ptr [rdx]
0091F446  83 C1 10                        add ecx, 0x10
0091F449  48 89 5D 10                     mov qword ptr [rbp + 0x10], rbx
0091F44D  4D 85 F6                        test r14, r14
0091F450  89 4D EC                        mov dword ptr [rbp - 0x14], ecx
0091F453  45 8D 73 04                     lea r14d, [r11 + 4]
0091F457  44 89 75 0C                     mov dword ptr [rbp + 0xc], r14d
0091F45B  75 04                           jne 0x14091f461
0091F45D  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0091F461  89 75 28                        mov dword ptr [rbp + 0x28], esi
0091F464  89 4D 2C                        mov dword ptr [rbp + 0x2c], ecx
0091F467  48 89 55 40                     mov qword ptr [rbp + 0x40], rdx
0091F46B  44 89 5D B8                     mov dword ptr [rbp - 0x48], r11d
0091F46F  4D 85 E4                        test r12, r12
0091F472  0F 84 6A 03 00 00               je 0x14091f7e2
0091F478  41 0F B7 04 24                  movzx eax, word ptr [r12]
0091F47D  BB 10 00 00 00                  mov ebx, 0x10
0091F482  48 8B 8D 40 04 00 00            mov rcx, qword ptr [rbp + 0x440]
0091F489  03 C3                           add eax, ebx
0091F48B  89 45 4C                        mov dword ptr [rbp + 0x4c], eax
0091F48E  89 75 48                        mov dword ptr [rbp + 0x48], esi
0091F491  4C 89 65 60                     mov qword ptr [rbp + 0x60], r12
0091F495  8D 43 65                        lea eax, [rbx + 0x65]
0091F498  48 85 C9                        test rcx, rcx
0091F49B  0F 85 4B 03 00 00               jne 0x14091f7ec
0091F4A1  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0091F4A6  C7 85 88 00 00 00 0B 00 00 00   mov dword ptr [rbp + 0x88], 0xb
0091F4B0  44 89 B5 8C 00 00 00            mov dword ptr [rbp + 0x8c], r14d
0091F4B7  48 85 C0                        test rax, rax
0091F4BA  0F 84 EA 02 00 00               je 0x14091f7aa
0091F4C0  48 8B 08                        mov rcx, qword ptr [rax]
0091F4C3  E8 E0 F1 FF FF                  call 0x14091e6a8
0091F4C8  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0091F4CF  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0091F4D3  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
0091F4DA  8B 85 68 04 00 00               mov eax, dword ptr [rbp + 0x468]
0091F4E0  C7 85 A8 00 00 00 0D 00 00 00   mov dword ptr [rbp + 0xa8], 0xd
0091F4EA  89 9D AC 00 00 00               mov dword ptr [rbp + 0xac], ebx
0091F4F0  C7 85 C8 00 00 00 07 00 00 00   mov dword ptr [rbp + 0xc8], 7
0091F4FA  44 89 9D CC 00 00 00            mov dword ptr [rbp + 0xcc], r11d
0091F501  4C 89 9D D8 00 00 00            mov qword ptr [rbp + 0xd8], r11
0091F508  45 84 C9                        test r9b, r9b
0091F50B  0F 84 A5 02 00 00               je 0x14091f7b6
0091F511  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0091F516  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
0091F51D  C7 45 B8 09 00 00 00            mov dword ptr [rbp - 0x48], 9
0091F524  48 85 DB                        test rbx, rbx
0091F527  0F 85 E8 26 20 00               jne 0x140b21c15
0091F52D  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
0091F532  33 C9                           xor ecx, ecx
0091F534  8B 44 24 2C                     mov eax, dword ptr [rsp + 0x2c]
0091F538  41 B8 53 65 41 70               mov r8d, 0x70416553
0091F53E  44 8B 64 24 28                  mov r12d, dword ptr [rsp + 0x28]
0091F543  2B C1                           sub eax, ecx
0091F545  41 81 C4 98 00 00 00            add r12d, 0x98
0091F54C  B9 00 01 00 00                  mov ecx, 0x100
0091F551  44 03 E0                        add r12d, eax
0091F554  41 8B D4                        mov edx, r12d
0091F557  45 8B F4                        mov r14d, r12d
0091F55A  E8 91 2B 26 00                  call 0x140b820f0
0091F55F  48 8B D8                        mov rbx, rax
0091F562  48 85 C0                        test rax, rax
0091F565  0F 84 AD 02 00 00               je 0x14091f818
0091F56B  45 8B C6                        mov r8d, r14d
0091F56E  33 D2                           xor edx, edx
0091F570  48 8B C8                        mov rcx, rax
0091F573  E8 C8 76 DA FF                  call 0x1406c6c40
0091F578  0F B6 8D 78 04 00 00            movzx ecx, byte ptr [rbp + 0x478]
0091F57F  8B 85 68 04 00 00               mov eax, dword ptr [rbp + 0x468]
0091F585  84 C9                           test cl, cl
0091F587  89 8B 88 00 00 00               mov dword ptr [rbx + 0x88], ecx
0091F58D  0F 44 85 60 04 00 00            cmove eax, dword ptr [rbp + 0x460]
0091F594  0F BA F0 19                     btr eax, 0x19
0091F598  C7 83 84 00 00 00 04 00 00 00   mov dword ptr [rbx + 0x84], 4
0091F5A2  89 03                           mov dword ptr [rbx], eax
0091F5A4  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0091F5A9  48 85 C0                        test rax, rax
0091F5AC  0F 85 CD 26 20 00               jne 0x140b21c7f
0091F5B2  4D 85 ED                        test r13, r13
0091F5B5  0F 85 6A 02 00 00               jne 0x14091f825
0091F5BB  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
0091F5C0  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0091F5C5  45 33 ED                        xor r13d, r13d
0091F5C8  48 85 D2                        test rdx, rdx
0091F5CB  0F 85 70 02 00 00               jne 0x14091f841
0091F5D1  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F5D4  48 C1 E0 05                     shl rax, 5
0091F5D8  C7 44 05 C8 1D 00 00 00         mov dword ptr [rbp + rax - 0x38], 0x1d
0091F5E0  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F5E3  48 C1 E0 05                     shl rax, 5
0091F5E7  44 89 64 05 CC                  mov dword ptr [rbp + rax - 0x34], r12d
0091F5EC  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F5EF  48 C1 E0 05                     shl rax, 5
0091F5F3  48 89 5C 05 E0                  mov qword ptr [rbp + rax - 0x20], rbx
0091F5F8  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F5FB  03 C6                           add eax, esi
0091F5FD  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0091F600  8B C8                           mov ecx, eax
0091F602  48 C1 E1 05                     shl rcx, 5
0091F606  C7 44 0D C8 0A 00 00 00         mov dword ptr [rbp + rcx - 0x38], 0xa
0091F60E  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F611  8B 8D 68 04 00 00               mov ecx, dword ptr [rbp + 0x468]
0091F617  48 C1 E0 05                     shl rax, 5
0091F61B  C7 44 05 CC 04 00 00 00         mov dword ptr [rbp + rax - 0x34], 4
0091F623  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F626  48 C1 E0 05                     shl rax, 5
0091F62A  44 38 AD 78 04 00 00            cmp byte ptr [rbp + 0x478], r13b
0091F631  75 06                           jne 0x14091f639
0091F633  8B 8D 60 04 00 00               mov ecx, dword ptr [rbp + 0x460]
0091F639  48 8B 95 70 04 00 00            mov rdx, qword ptr [rbp + 0x470]
0091F640  48 89 4C 05 D0                  mov qword ptr [rbp + rax - 0x30], rcx
0091F645  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
0091F648  FF C1                           inc ecx
0091F64A  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
0091F64D  48 85 D2                        test rdx, rdx
0091F650  0F 85 07 02 00 00               jne 0x14091f85d
0091F656  44 8B B5 98 04 00 00            mov r14d, dword ptr [rbp + 0x498]
0091F65D  03 CE                           add ecx, esi
0091F65F  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
0091F662  45 85 F6                        test r14d, r14d
0091F665  0F 85 36 02 00 00               jne 0x14091f8a1
0091F66B  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0091F670  8B C1                           mov eax, ecx
0091F672  48 C1 E0 05                     shl rax, 5
0091F676  C7 44 05 C8 1B 00 00 00         mov dword ptr [rbp + rax - 0x38], 0x1b
0091F67E  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F681  48 C1 E0 05                     shl rax, 5
0091F685  C7 44 05 CC 04 00 00 00         mov dword ptr [rbp + rax - 0x34], 4
0091F68D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0091F692  8B 88 80 00 00 00               mov ecx, dword ptr [rax + 0x80]
0091F698  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F69B  48 C1 E0 05                     shl rax, 5
0091F69F  48 89 4C 05 D0                  mov qword ptr [rbp + rax - 0x30], rcx
0091F6A4  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F6A7  03 C6                           add eax, esi
0091F6A9  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0091F6AC  8B C8                           mov ecx, eax
0091F6AE  48 C1 E1 05                     shl rcx, 5
0091F6B2  C7 44 0D C8 0B 00 00 00         mov dword ptr [rbp + rcx - 0x38], 0xb
0091F6BA  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F6BD  48 C1 E0 05                     shl rax, 5
0091F6C1  C7 44 05 CC 08 00 00 00         mov dword ptr [rbp + rax - 0x34], 8
0091F6C9  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
0091F6CC  48 8B 85 80 04 00 00            mov rax, qword ptr [rbp + 0x480]
0091F6D3  48 C1 E1 05                     shl rcx, 5
0091F6D7  48 89 44 0D D0                  mov qword ptr [rbp + rcx - 0x30], rax
0091F6DC  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F6DF  03 C6                           add eax, esi
0091F6E1  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0091F6E4  8B C8                           mov ecx, eax
0091F6E6  B8 02 00 00 00                  mov eax, 2
0091F6EB  48 C1 E1 05                     shl rcx, 5
0091F6EF  89 44 0D C8                     mov dword ptr [rbp + rcx - 0x38], eax
0091F6F3  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F6F6  0F B7 0A                        movzx ecx, word ptr [rdx]
0091F6F9  48 C1 E0 05                     shl rax, 5
0091F6FD  83 C1 10                        add ecx, 0x10
0091F700  89 4C 05 CC                     mov dword ptr [rbp + rax - 0x34], ecx
0091F704  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F707  0F B7 4C 24 24                  movzx ecx, word ptr [rsp + 0x24]
0091F70C  48 C1 E0 05                     shl rax, 5
0091F710  48 89 54 05 E0                  mov qword ptr [rbp + rax - 0x20], rdx
0091F715  01 75 B8                        add dword ptr [rbp - 0x48], esi
0091F718  83 E9 75                        sub ecx, 0x75
0091F71B  74 05                           je 0x14091f722
0091F71D  83 F9 0C                        cmp ecx, 0xc
0091F720  75 09                           jne 0x14091f72b
0091F722  4D 85 FF                        test r15, r15
0091F725  0F 85 E0 26 20 00               jne 0x140b21e0b
0091F72B  01 75 B8                        add dword ptr [rbp - 0x48], esi
0091F72E  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0091F732  E8 35 54 90 FF                  call 0x140224b6c
0091F737  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0091F73C  48 85 C0                        test rax, rax
0091F73F  0F 85 8C 01 00 00               jne 0x14091f8d1
0091F745  33 D2                           xor edx, edx
0091F747  48 8B CB                        mov rcx, rbx
0091F74A  E8 21 31 26 00                  call 0x140b82870
0091F74F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0091F754  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0091F759  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0091F75E  48 85 C9                        test rcx, rcx
0091F761  0F 85 79 01 00 00               jne 0x14091f8e0
0091F767  44 38 6C 24 20                  cmp byte ptr [rsp + 0x20], r13b
0091F76C  0F 85 7A 01 00 00               jne 0x14091f8ec
0091F772  44 38 6C 24 21                  cmp byte ptr [rsp + 0x21], r13b
0091F777  0F 85 87 01 00 00               jne 0x14091f904
0091F77D  44 38 6C 24 22                  cmp byte ptr [rsp + 0x22], r13b
0091F782  0F 85 94 01 00 00               jne 0x14091f91c
0091F788  85 FF                           test edi, edi
0091F78A  0F 88 A4 01 00 00               js 0x14091f934
0091F790  C1 EF 1F                        shr edi, 0x1f
0091F793  40 32 FE                        xor dil, sil
0091F796  40 8A C7                        mov al, dil
0091F799  E9 9D FB FF FF                  jmp 0x14091f33b
0091F79E  48 8B 81 98 00 00 00            mov rax, qword ptr [rcx + 0x98]
0091F7A5  E9 0E FC FF FF                  jmp 0x14091f3b8
0091F7AA  4C 89 AD 90 00 00 00            mov qword ptr [rbp + 0x90], r13
0091F7B1  E9 19 FD FF FF                  jmp 0x14091f4cf
0091F7B6  8B 85 60 04 00 00               mov eax, dword ptr [rbp + 0x460]
0091F7BC  E9 50 FD FF FF                  jmp 0x14091f511
0091F7C1  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
0091F7C6  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0091F7CB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0091F7D0  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0091F7D5  4D 85 ED                        test r13, r13
0091F7D8  74 33                           je 0x14091f80d
0091F7DA  41 8B CE                        mov ecx, r14d
0091F7DD  E9 52 FD FF FF                  jmp 0x14091f534
0091F7E2  BF 0D 00 00 C0                  mov edi, 0xc000000d
0091F7E7  E9 63 FF FF FF                  jmp 0x14091f74f
0091F7EC  66 44 3B D0                     cmp r10w, ax
0091F7F0  0F 84 04 24 20 00               je 0x140b21bfa
0091F7F6  B8 81 00 00 00                  mov eax, 0x81
0091F7FB  89 75 68                        mov dword ptr [rbp + 0x68], esi
0091F7FE  66 44 3B D0                     cmp r10w, ax
0091F802  0F 84 F2 23 20 00               je 0x140b21bfa
0091F808  E9 F4 23 20 00                  jmp 0x140b21c01
0091F80D  48 85 C0                        test rax, rax
0091F810  0F 84 1C FD FF FF               je 0x14091f532
0091F816  EB C2                           jmp 0x14091f7da
0091F818  BF 9A 00 00 C0                  mov edi, 0xc000009a
0091F81D  45 33 ED                        xor r13d, r13d
0091F820  E9 2A FF FF FF                  jmp 0x14091f74f
0091F825  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
0091F82A  48 8D 8B 90 00 00 00            lea rcx, [rbx + 0x90]
0091F831  45 8B C6                        mov r8d, r14d
0091F834  49 8B D5                        mov rdx, r13
0091F837  E8 04 70 DA FF                  call 0x1406c6840
0091F83C  E9 7F FD FF FF                  jmp 0x14091f5c0
0091F841  44 8B 44 24 2C                  mov r8d, dword ptr [rsp + 0x2c]
0091F846  41 8B CE                        mov ecx, r14d
0091F849  48 81 C1 90 00 00 00            add rcx, 0x90
0091F850  48 03 CB                        add rcx, rbx
0091F853  E8 E8 6F DA FF                  call 0x1406c6840
0091F858  E9 74 FD FF FF                  jmp 0x14091f5d1
0091F85D  44 8B 02                        mov r8d, dword ptr [rdx]
0091F860  45 85 C0                        test r8d, r8d
0091F863  0F 84 ED FD FF FF               je 0x14091f656
0091F869  8B C1                           mov eax, ecx
0091F86B  48 C1 E0 05                     shl rax, 5
0091F86F  C7 44 05 C8 08 00 00 00         mov dword ptr [rbp + rax - 0x38], 8
0091F877  43 8D 04 40                     lea eax, [r8 + r8*2]
0091F87B  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
0091F882  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F885  48 C1 E0 05                     shl rax, 5
0091F889  89 4C 05 CC                     mov dword ptr [rbp + rax - 0x34], ecx
0091F88D  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
0091F890  48 C1 E0 05                     shl rax, 5
0091F894  48 89 54 05 E0                  mov qword ptr [rbp + rax - 0x20], rdx
0091F899  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
0091F89C  E9 B5 FD FF FF                  jmp 0x14091f656
0091F8A1  8A 85 78 04 00 00               mov al, byte ptr [rbp + 0x478]
0091F8A7  41 8B D5                        mov edx, r13d
0091F8AA  F6 D8                           neg al
0091F8AC  41 8B C5                        mov eax, r13d
0091F8AF  66 45 1B E4                     sbb r12w, r12w
0091F8B3  66 41 83 C4 02                  add r12w, 2
0091F8B8  45 85 F6                        test r14d, r14d
0091F8BB  0F 84 AA FD FF FF               je 0x14091f66b
0091F8C1  4C 8B AD 90 04 00 00            mov r13, qword ptr [rbp + 0x490]
0091F8C8  4D 8D 45 02                     lea r8, [r13 + 2]
0091F8CC  E9 0F 24 20 00                  jmp 0x140b21ce0
0091F8D1  33 D2                           xor edx, edx
0091F8D3  48 8B C8                        mov rcx, rax
0091F8D6  E8 95 2F 26 00                  call 0x140b82870
0091F8DB  E9 65 FE FF FF                  jmp 0x14091f745
0091F8E0  33 D2                           xor edx, edx
0091F8E2  E8 89 2F 26 00                  call 0x140b82870
0091F8E7  E9 7B FE FF FF                  jmp 0x14091f767
0091F8EC  4D 85 FF                        test r15, r15
0091F8EF  0F 84 7D FE FF FF               je 0x14091f772
0091F8F5  33 D2                           xor edx, edx
0091F8F7  49 8B CF                        mov rcx, r15
0091F8FA  E8 71 2F 26 00                  call 0x140b82870
0091F8FF  E9 6E FE FF FF                  jmp 0x14091f772
0091F904  48 85 DB                        test rbx, rbx
0091F907  0F 84 70 FE FF FF               je 0x14091f77d
0091F90D  33 D2                           xor edx, edx
0091F90F  48 8B CB                        mov rcx, rbx
0091F912  E8 59 2F 26 00                  call 0x140b82870
0091F917  E9 61 FE FF FF                  jmp 0x14091f77d
0091F91C  4D 85 F6                        test r14, r14
0091F91F  0F 84 63 FE FF FF               je 0x14091f788
0091F925  33 D2                           xor edx, edx
0091F927  49 8B CE                        mov rcx, r14
0091F92A  E8 41 2F 26 00                  call 0x140b82870
0091F92F  E9 54 FE FF FF                  jmp 0x14091f788
0091F934  8B CF                           mov ecx, edi
0091F936  E8 E5 F4 F4 FF                  call 0x14086ee20
0091F93B  E9 50 FE FF FF                  jmp 0x14091f790
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAdtOpenObjectAuditAlarm(unsigned __int16 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned int v_stack_m4C4;
    unsigned __int64 v_stack_m4C8;
    unsigned __int16 v_stack_m4CC;
    unsigned __int8 v_stack_m4CE;
    unsigned __int8 v_stack_m4CF;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned __int64 v_stack_m4E8;
    unsigned int v_stack_m4EC;
    unsigned int v_stack_m4F0;
    unsigned __int16 v_stack_m4F4;
    unsigned __int8 v_stack_m4F6;
    unsigned __int8 v_stack_m4F7;
    unsigned __int8 v_stack_m4F8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (0x4F0ULL);
    result = (*(unsigned __int64 *)(v_rip + 5158103)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 1048 + 992) = result;
    a2 = 0;
    v_stack_m4A0 = a3;
    v_stack_m4F4 = a1;
    *(unsigned __int64 *)(v_rsp - 1048 - 120) = *(unsigned __int64 *)(v_rsp - 1048 + 1096);
    v_stack_m4C0 = *(unsigned __int64 *)(v_rsp - 1048 + 1096);
    v_stack_m4C8 = *(unsigned __int64 *)(v_rsp - 1048 + 1112);
    v_stack_m4A8 = *(unsigned __int64 *)(v_rsp - 1048 + 1200);
    result = memset(v_rsp - 1048 - 80, a2, (unsigned int)(0x418ULL), a4);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 1048 - 112) = *(unsigned __int64 *)(v_rsp - 1048 + 1104);
    v_stack_m4B8 = 0;
    v_stack_m4B0 = 0;
    *(unsigned __int64 *)(v_rsp - 1048 - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 1048 - 88) = 0;
    a3 = ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)) == 0) ? 1 : 0;
    v_stack_m4F0 = 0;
    v_stack_m4EC = 0;
    v_stack_m4E8 = 0;
    v_stack_m4D8 = 0;
    v_stack_m4E0 = 0;
    v_stack_m4D0 = 0;
    v_stack_m4F7 = 0;
    v_stack_m4F6 = 0;
    v_stack_m4F8 = 0;
    *(unsigned __int64 *)(v_rsp - 1048 + 976) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1048 - 96) = *(unsigned __int64 *)(v_rsp - 1048 + 1112);
    result = SepAdtAuditThisEventWithContext(0 + 124, (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)), a3, v_rsp - 1048 - 112);
    if ((unsigned __int8)(result) != 0) goto loc_0091F36C;
loc_0091F33B:
    a1 = (*(unsigned __int64 *)(v_rsp - 1048 + 992)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)), a3, v_rsp - 1048 - 112);
    return result;
loc_0091F36C:
    result = v_rsp - 1048 + 976;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) != 0) { result = *(unsigned __int64 *)(v_stack_m28 + 72); }
    *(unsigned __int64 *)(v_rsp - 1048 - 128) = result;
    result = PsGetCurrentThreadProcess(a1, (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)), a3, v_rsp - 1048 - 112);
    result = PsGetAllocatedFullProcessImageNameEx(result, v_stack_m488, a3, v_rsp - 1048 - 112);
    if (sign_flag) goto loc_0091F81D;
    if (*(unsigned __int64 *)(v_rsp - 1048 + 1104) == 0) goto loc_0091F79E;
loc_0091F3B8:
    *(unsigned int *)(v_rsp - 1048 - 76) = 0x1230ULL;
    *(unsigned __int16 *)(v_rsp - 1048 - 64) = (unsigned __int16)(v_stack_m4CC);
    a1 = 8;
    if ((*(unsigned int *)(v_rsp - 1048 + 1160)) == ((unsigned int)(8 - 6))) { a1 = (unsigned int)(8 - 5); }
    *(unsigned __int16 *)(v_rsp - 1048 - 62) = 8;
    *(unsigned int *)(v_rsp - 1048 - 80) = a1;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)) == 0) {
        *(unsigned __int16 *)(v_rsp - 1048 - 62) = (unsigned __int16)(8 - 5 + 13);
    }
    a2 = v_rip - 9560169;
    if (0 != 0) { a2 = 0; }
    *(unsigned int *)(v_rsp - 1048 - 56) = 4;
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 1048 - 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 1048 + 1104) + 152));
    *(unsigned int *)(v_rsp - 1048 - 24) = 1;
    *(unsigned __int64 *)(v_rsp - 1048) = a2;
    *(unsigned int *)(v_rsp - 1048 + 8) = 5;
    *(unsigned int *)(v_rsp - 1048 - 52) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 1048 + 1104) + 152)) + 1) * 4 + 8);
    a1 = (unsigned int)((*(unsigned __int16 *)(a2)) + (16));
    *(unsigned __int64 *)(v_rsp - 1048 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 1048 + 1104) + 24);
    *(unsigned int *)(v_rsp - 1048 - 20) = a1;
    *(unsigned int *)(v_rsp - 1048 + 12) = (unsigned int)(4 + 4);
    if (*(unsigned __int64 *)(v_rsp - 1048 + 1104) == 0) {
        *(unsigned __int64 *)(v_rsp - 1048 + 16) = *(unsigned __int64 *)(v_stack_m4A0 + 24);
    }
    *(unsigned int *)(v_rsp - 1048 + 40) = 1;
    *(unsigned int *)(v_rsp - 1048 + 44) = a1;
    *(unsigned __int64 *)(v_rsp - 1048 + 64) = a2;
    *(unsigned int *)(v_rsp - 1048 - 72) = 4;
    if (a4 == 0) goto loc_0091F7E2;
    result = (unsigned int)((*(unsigned __int16 *)(a4)) + (16));
    *(unsigned int *)(v_rsp - 1048 + 76) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 1048 + 72) = 1;
    *(unsigned __int64 *)(v_rsp - 1048 + 96) = a4;
    if (*(unsigned __int64 *)(v_rsp - 1048 + 1088) != 0) goto loc_0091F7EC;
    *(unsigned int *)(v_rsp - 1048 + 136) = 11;
    *(unsigned int *)(v_rsp - 1048 + 140) = (unsigned int)(4 + 4);
    if (v_stack_m478 == 0) goto loc_0091F7AA;
    result = ObNormalizeHandleValue(*(unsigned __int64 *)(v_stack_m478), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 1048 + 1104) + 152)), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    *(unsigned __int64 *)(v_rsp - 1048 + 144) = result;
loc_0091F4CF:
    *(unsigned __int64 *)(v_rsp - 1048 + 192) = *(unsigned __int64 *)(v_rsp - 1048 - 128);
    *(unsigned int *)(v_rsp - 1048 + 168) = 13;
    *(unsigned int *)(v_rsp - 1048 + 172) = 16;
    *(unsigned int *)(v_rsp - 1048 + 200) = 7;
    *(unsigned int *)(v_rsp - 1048 + 204) = 4;
    *(unsigned __int64 *)(v_rsp - 1048 + 216) = 4;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)) == 0) goto loc_0091F7B6;
loc_0091F511:
    *(unsigned __int64 *)(v_rsp - 1048 + 208) = (unsigned int)(*(unsigned int *)(v_rsp - 1048 + 1128));
    *(unsigned int *)(v_rsp - 1048 - 72) = 9;
loc_0091F532:
    a1 = 0;
loc_0091F534:
    result = (unsigned int)(((unsigned int)(v_stack_m4C4)) - (0));
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m4C8)) + (152));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(result)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x70416553ULL), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    if (result == 0) goto loc_0091F818;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    *(unsigned int *)(result + 136) = (unsigned int)(*(unsigned __int8 *)(v_rsp - 1048 + 1144));
    result = (unsigned int)(*(unsigned int *)(v_rsp - 1048 + 1128));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 1048 + 1144)) == 0) { result = *(unsigned int *)(v_rsp - 1048 + 1120); }
    *(unsigned int *)(result + 132) = 4;
    *(unsigned int *)(result) = (unsigned int)(result);
    if (v_stack_m4C0 != 0) goto loc_0091F825;
loc_0091F5C0:
    v_r13 = 0;
    if (v_stack_m4B8 != 0) goto loc_0091F841;
loc_0091F5D1:
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 56) = 29;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = (unsigned int)(v_r12);
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned __int64 *)(v_rsp - 1048 + result * 1 - 32) = result;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) + (1));
    *(unsigned int *)(v_rsp - 1048 - 72) = (unsigned int)(result);
    a1 = ((unsigned int)((unsigned int)(result))) << (5);
    *(unsigned int *)(v_rsp - 1048 + a1 * 1 - 56) = 10;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = 4;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    if ((*(unsigned __int8 *)(v_rsp - 1048 + 1144)) == 0) {
        a1 = *(unsigned int *)(v_rsp - 1048 + 1120);
    }
    *(unsigned __int64 *)(v_rsp - 1048 + result * 1 - 48) = a1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) + 1);
    *(unsigned int *)(v_rsp - 1048 - 72) = a1;
    if (*(unsigned __int64 *)(v_rsp - 1048 + 1136) != 0) goto loc_0091F85D;
loc_0091F656:
    a1 = (unsigned int)((a1) + (1));
    *(unsigned int *)(v_rsp - 1048 - 72) = a1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 1048 + 1176))) != 0) goto loc_0091F8A1;
loc_0091F66B:
    result = ((unsigned int)(a1)) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 56) = 27;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = 4;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned __int64 *)(v_rsp - 1048 + result * 1 - 48) = (unsigned int)(*(unsigned int *)(v_stack_m4A0 + 128));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) + (1));
    *(unsigned int *)(v_rsp - 1048 - 72) = (unsigned int)(result);
    a1 = ((unsigned int)((unsigned int)(result))) << (5);
    *(unsigned int *)(v_rsp - 1048 + a1 * 1 - 56) = 11;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = 8;
    a1 = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned __int64 *)(v_rsp - 1048 + a1 * 1 - 48) = *(unsigned __int64 *)(v_rsp - 1048 + 1152);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) + (1));
    *(unsigned int *)(v_rsp - 1048 - 72) = (unsigned int)(result);
    a1 = ((unsigned int)((unsigned int)(result))) << (5);
    *(unsigned int *)(v_rsp - 1048 + a1 * 1 - 56) = 2;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m488)) + (16));
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = a1;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned __int64 *)(v_rsp - 1048 + result * 1 - 32) = v_stack_m488;
    a1 = (unsigned int)((v_stack_m4CC) - (117));
    if (condition_is_equal) goto loc_0091F722;
    if (a1 != 12) goto loc_0091F72B;
loc_0091F722:
loc_0091F72B:
    result = SepAdtLogAuditRecord(v_rsp - 1048 - 80, v_stack_m488, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    if (v_stack_m490 != 0) goto loc_0091F8D1;
loc_0091F745:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
loc_0091F74F:
    if (v_stack_m488 != 0) goto loc_0091F8E0;
loc_0091F767:
    if (v_stack_m4D0 != 0) goto loc_0091F8EC;
loc_0091F772:
    if (v_stack_m4CF != 0) goto loc_0091F904;
loc_0091F77D:
    if (v_stack_m4CE != 0) goto loc_0091F91C;
loc_0091F788:
    if (sign_flag) goto loc_0091F934;
loc_0091F790:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    v_rdi = (unsigned __int8)((v_rdi) ^ (1));
    goto loc_0091F33B;
loc_0091F79E:
    goto loc_0091F3B8;
loc_0091F7AA:
    *(unsigned __int64 *)(v_rsp - 1048 + 144) = 0;
    goto loc_0091F4CF;
loc_0091F7B6:
    goto loc_0091F511;
loc_0091F7E2:
    goto loc_0091F74F;
loc_0091F7EC:
    *(unsigned int *)(v_rsp - 1048 + 104) = 1;
loc_0091F818:
loc_0091F81D:
    v_r13 = 0;
    goto loc_0091F74F;
loc_0091F825:
    result = memcpy(v_stack_m4C0 + 144, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C8))), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F5C0;
loc_0091F841:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m4C8)))) + (144);
    a1 = (a1) + (v_stack_m4C0);
    result = memcpy(a1, 0, (unsigned int)(v_stack_m4C4), *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F5D1;
loc_0091F85D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0))) == 0) goto loc_0091F656;
    result = ((unsigned int)(a1)) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 56) = 8;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned int *)(v_rsp - 1048 + result * 1 - 52) = (unsigned int)((unsigned int)(*(unsigned int *)(0)) + (unsigned int)(*(unsigned int *)(0)) * 2 * 4 + 8);
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 1048 - 72))) << (5);
    *(unsigned __int64 *)(v_rsp - 1048 + result * 1 - 32) = 0;
    goto loc_0091F656;
loc_0091F8A1:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rsp - 1048 + 1144)));
    v_r12 = (unsigned __int16)((v_r12) + (2));
    if ((unsigned int)((unsigned int)(v_stack_m4C8)) == 0) goto loc_0091F66B;
loc_0091F8D1:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F745;
loc_0091F8E0:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F767;
loc_0091F8EC:
    if (*(unsigned __int64 *)(v_rsp - 1048 + 1096) == 0) goto loc_0091F772;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 1048 + 1096), a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F772;
loc_0091F904:
    if (v_stack_m4C0 == 0) goto loc_0091F77D;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m4C0, a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F77D;
loc_0091F91C:
    if ((unsigned int)(v_stack_m4C8) == 0) goto loc_0091F788;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(v_stack_m4C8), a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F788;
loc_0091F934:
    result = SepAuditFailed((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a2, *(unsigned __int64 *)(v_rsp - 1048 + 1168) + 2, *(unsigned __int8 *)(v_rsp - 1048 + 1144));
    goto loc_0091F790;
}
```

## 5. (Beta) C Style

```c
int64_t SepAdtOpenObjectAuditAlarm(uint16_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m478;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint32_t v_stack_m4C4;
    uint64_t v_stack_m4C8;
    uint16_t v_stack_m4CC;
    uint8_t v_stack_m4CE;
    uint8_t v_stack_m4CF;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint64_t v_stack_m4E8;
    uint32_t v_stack_m4EC;
    uint32_t v_stack_m4F0;
    uint16_t v_stack_m4F4;
    uint8_t v_stack_m4F6;
    uint8_t v_stack_m4F7;
    uint8_t v_stack_m4F8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (0x4F0ULL);
    result = (*(uint64_t *)(v_rip + 0x4EB4D7)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x418 + 0x3E0) = result;
    Arg2 = 0;
    v_stack_m4A0 = Arg3;
    v_stack_m4F4 = Arg1;
    *(uint64_t *)(local_rsp - 0x418 - 0x78) = *(uint64_t *)(local_rsp - 0x418 + 0x448);
    v_stack_m4C0 = *(uint64_t *)(local_rsp - 0x418 + 0x448);
    v_stack_m4C8 = *(uint64_t *)(local_rsp - 0x418 + 0x458);
    v_stack_m4A8 = *(uint64_t *)(local_rsp - 0x418 + 0x4B0);
    result = memset(local_rsp - 1048 - 80, Arg2, (uint32_t)(0x418ULL), Arg4);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x418 - 0x70) = *(uint64_t *)(local_rsp - 0x418 + 0x450);
    v_stack_m4B8 = 0;
    v_stack_m4B0 = 0;
    *(uint64_t *)(local_rsp - 0x418 - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x418 - 0x58) = 0;
    Arg3 = ((uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)) == 0) ? 1 : 0;
    v_stack_m4F0 = 0;
    v_stack_m4EC = 0;
    v_stack_m4E8 = 0;
    v_stack_m4D8 = 0;
    v_stack_m4E0 = 0;
    v_stack_m4D0 = 0;
    v_stack_m4F7 = 0;
    v_stack_m4F6 = 0;
    v_stack_m4F8 = 0;
    *(uint64_t *)(local_rsp - 0x418 + 0x3D0) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x418 - 0x60) = *(uint64_t *)(local_rsp - 0x418 + 0x458);
    result = SepAdtAuditThisEventWithContext(0 + 124, (uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)), Arg3, local_rsp - 1048 - 112);
    if ((uint8_t)(result) != 0) goto loc_0091F36C;
loc_0091F33B:
    Arg1 = (*(uint64_t *)(local_rsp - 0x418 + 0x3E0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)), Arg3, local_rsp - 1048 - 112);
    return result;
loc_0091F36C:
    result = local_rsp - 1048 + 976;
    if (*(uint64_t *)(v_stack_m28 + 0x48) != 0) { result = *(uint64_t *)(v_stack_m28 + 0x48); }
    *(uint64_t *)(local_rsp - 0x418 - 0x80) = result;
    result = PsGetCurrentThreadProcess(Arg1, (uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)), Arg3, local_rsp - 1048 - 112);
    result = PsGetAllocatedFullProcessImageNameEx(result, v_stack_m488, Arg3, local_rsp - 1048 - 112);
    if (sign_flag) goto loc_0091F81D;
    if (*(uint64_t *)(local_rsp - 0x418 + 0x450) == 0) goto loc_0091F79E;
loc_0091F3B8:
    *(uint32_t *)(local_rsp - 0x418 - 0x4C) = 0x1230ULL;
    *(uint16_t *)(local_rsp - 0x418 - 0x40) = (uint16_t)(v_stack_m4CC);
    Arg1 = 8;
    if ((*(uint32_t *)(local_rsp - 0x418 + 0x488)) == ((uint32_t)(8 - 6))) { Arg1 = (uint32_t)(8 - 5); }
    *(uint16_t *)(local_rsp - 0x418 - 0x3E) = 8;
    *(uint32_t *)(local_rsp - 0x418 - 0x50) = Arg1;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)) == 0) {
        *(uint16_t *)(local_rsp - 0x418 - 0x3E) = (uint16_t)(8 - 5 + 13);
    }
    Arg2 = v_rip - 9560169;
    if (0 != 0) { Arg2 = 0; }
    *(uint32_t *)(local_rsp - 0x418 - 0x38) = 4;
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x418 - 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x418 + 0x450) + 0x98));
    *(uint32_t *)(local_rsp - 0x418 - 0x18) = 1;
    *(uint64_t *)(local_rsp - 0x418) = Arg2;
    *(uint32_t *)(local_rsp - 0x418 + 0x8) = 5;
    *(uint32_t *)(local_rsp - 0x418 - 0x34) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x418 + 0x450) + 0x98)) + 0x1) * 4 + 8);
    Arg1 = (uint32_t)((*(uint16_t *)(Arg2)) + (16));
    *(uint64_t *)(local_rsp - 0x418 + 0x10) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x418 + 0x450) + 0x18);
    *(uint32_t *)(local_rsp - 0x418 - 0x14) = Arg1;
    *(uint32_t *)(local_rsp - 0x418 + 0xC) = (uint32_t)(4 + 4);
    if (*(uint64_t *)(local_rsp - 0x418 + 0x450) == 0) {
        *(uint64_t *)(local_rsp - 0x418 + 0x10) = *(uint64_t *)(v_stack_m4A0 + 0x18);
    }
    *(uint32_t *)(local_rsp - 0x418 + 0x28) = 1;
    *(uint32_t *)(local_rsp - 0x418 + 0x2C) = Arg1;
    *(uint64_t *)(local_rsp - 0x418 + 0x40) = Arg2;
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = 4;
    if (Arg4 == 0) goto loc_0091F7E2;
    result = (uint32_t)((*(uint16_t *)(Arg4)) + (16));
    *(uint32_t *)(local_rsp - 0x418 + 0x4C) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x418 + 0x48) = 1;
    *(uint64_t *)(local_rsp - 0x418 + 0x60) = Arg4;
    if (*(uint64_t *)(local_rsp - 0x418 + 0x440) != 0) goto loc_0091F7EC;
    *(uint32_t *)(local_rsp - 0x418 + 0x88) = 11;
    *(uint32_t *)(local_rsp - 0x418 + 0x8C) = (uint32_t)(4 + 4);
    if (v_stack_m478 == 0) goto loc_0091F7AA;
    result = ObNormalizeHandleValue(*(uint64_t *)(v_stack_m478), Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x418 + 0x450) + 0x98)), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    *(uint64_t *)(local_rsp - 0x418 + 0x90) = result;
loc_0091F4CF:
    *(uint64_t *)(local_rsp - 0x418 + 0xC0) = *(uint64_t *)(local_rsp - 0x418 - 0x80);
    *(uint32_t *)(local_rsp - 0x418 + 0xA8) = 13;
    *(uint32_t *)(local_rsp - 0x418 + 0xAC) = 16;
    *(uint32_t *)(local_rsp - 0x418 + 0xC8) = 7;
    *(uint32_t *)(local_rsp - 0x418 + 0xCC) = 4;
    *(uint64_t *)(local_rsp - 0x418 + 0xD8) = 4;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)) == 0) goto loc_0091F7B6;
loc_0091F511:
    *(uint64_t *)(local_rsp - 0x418 + 0xD0) = (uint32_t)(*(uint32_t *)(local_rsp - 0x418 + 0x468));
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = 9;
loc_0091F532:
    Arg1 = 0;
loc_0091F534:
    result = (uint32_t)(((uint32_t)(v_stack_m4C4)) - (0));
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m4C8)) + (152));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(result)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x70416553ULL), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    if (result == 0) goto loc_0091F818;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    *(uint32_t *)(result + 0x88) = (uint32_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478));
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x418 + 0x468));
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x418 + 0x478)) == 0) { result = *(uint32_t *)(local_rsp - 0x418 + 0x460); }
    *(uint32_t *)(result + 0x84) = 4;
    *(uint32_t *)(result) = (uint32_t)(result);
    if (v_stack_m4C0 != 0) goto loc_0091F825;
loc_0091F5C0:
    local_r13 = 0;
    if (v_stack_m4B8 != 0) goto loc_0091F841;
loc_0091F5D1:
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x38) = 29;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = (uint32_t)(local_r12);
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint64_t *)(local_rsp - 0x418 + result * 1 - 0x20) = result;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) + (1));
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = (uint32_t)(result);
    Arg1 = ((uint32_t)((uint32_t)(result))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + Arg1 * 1 - 0x38) = 10;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = 4;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    if ((*(uint8_t *)(local_rsp - 0x418 + 0x478)) == 0) {
        Arg1 = *(uint32_t *)(local_rsp - 0x418 + 0x460);
    }
    *(uint64_t *)(local_rsp - 0x418 + result * 1 - 0x30) = Arg1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) + 1);
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = Arg1;
    if (*(uint64_t *)(local_rsp - 0x418 + 0x470) != 0) goto loc_0091F85D;
loc_0091F656:
    Arg1 = (uint32_t)((Arg1) + (1));
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = Arg1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x418 + 0x498))) != 0) goto loc_0091F8A1;
loc_0091F66B:
    result = ((uint32_t)(Arg1)) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x38) = 27;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = 4;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint64_t *)(local_rsp - 0x418 + result * 1 - 0x30) = (uint32_t)(*(uint32_t *)(v_stack_m4A0 + 0x80));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) + (1));
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = (uint32_t)(result);
    Arg1 = ((uint32_t)((uint32_t)(result))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + Arg1 * 1 - 0x38) = 11;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = 8;
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint64_t *)(local_rsp - 0x418 + Arg1 * 1 - 0x30) = *(uint64_t *)(local_rsp - 0x418 + 0x480);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) + (1));
    *(uint32_t *)(local_rsp - 0x418 - 0x48) = (uint32_t)(result);
    Arg1 = ((uint32_t)((uint32_t)(result))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + Arg1 * 1 - 0x38) = 2;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m488)) + (16));
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = Arg1;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint64_t *)(local_rsp - 0x418 + result * 1 - 0x20) = v_stack_m488;
    Arg1 = (uint32_t)((v_stack_m4CC) - (117));
    if (condition_is_equal) goto loc_0091F722;
    if (Arg1 != 12) goto loc_0091F72B;
loc_0091F722:
loc_0091F72B:
    result = SepAdtLogAuditRecord(local_rsp - 1048 - 80, v_stack_m488, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    if (v_stack_m490 != 0) goto loc_0091F8D1;
loc_0091F745:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), *(uint8_t *)(local_rsp - 0x418 + 0x478));
loc_0091F74F:
    if (v_stack_m488 != 0) goto loc_0091F8E0;
loc_0091F767:
    if (v_stack_m4D0 != 0) goto loc_0091F8EC;
loc_0091F772:
    if (v_stack_m4CF != 0) goto loc_0091F904;
loc_0091F77D:
    if (v_stack_m4CE != 0) goto loc_0091F91C;
loc_0091F788:
    if (sign_flag) goto loc_0091F934;
loc_0091F790:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    local_rdi = (uint8_t)((local_rdi) ^ (1));
    goto loc_0091F33B;
loc_0091F79E:
    goto loc_0091F3B8;
loc_0091F7AA:
    *(uint64_t *)(local_rsp - 0x418 + 0x90) = 0;
    goto loc_0091F4CF;
loc_0091F7B6:
    goto loc_0091F511;
loc_0091F7E2:
    goto loc_0091F74F;
loc_0091F7EC:
    *(uint32_t *)(local_rsp - 0x418 + 0x68) = 1;
loc_0091F818:
loc_0091F81D:
    local_r13 = 0;
    goto loc_0091F74F;
loc_0091F825:
    result = memcpy(v_stack_m4C0 + 144, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C8))), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F5C0;
loc_0091F841:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m4C8)))) + (144);
    Arg1 = (Arg1) + (v_stack_m4C0);
    result = memcpy(Arg1, 0, (uint32_t)(v_stack_m4C4), *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F5D1;
loc_0091F85D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0))) == 0) goto loc_0091F656;
    result = ((uint32_t)(Arg1)) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x38) = 8;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint32_t *)(local_rsp - 0x418 + result * 1 - 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(0)) + (uint32_t)(*(uint32_t *)(0)) * 2 * 4 + 8);
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x418 - 0x48))) << (5);
    *(uint64_t *)(local_rsp - 0x418 + result * 1 - 0x20) = 0;
    goto loc_0091F656;
loc_0091F8A1:
    result = (uint8_t)(-(*(uint8_t *)(local_rsp - 0x418 + 0x478)));
    local_r12 = (uint16_t)((local_r12) + (2));
    if ((uint32_t)((uint32_t)(v_stack_m4C8)) == 0) goto loc_0091F66B;
loc_0091F8D1:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F745;
loc_0091F8E0:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F767;
loc_0091F8EC:
    if (*(uint64_t *)(local_rsp - 0x418 + 0x448) == 0) goto loc_0091F772;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x418 + 0x448), Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F772;
loc_0091F904:
    if (v_stack_m4C0 == 0) goto loc_0091F77D;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m4C0, Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F77D;
loc_0091F91C:
    if ((uint32_t)(v_stack_m4C8) == 0) goto loc_0091F788;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(v_stack_m4C8), Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F788;
loc_0091F934:
    result = SepAuditFailed((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), Arg2, *(uint64_t *)(local_rsp - 0x418 + 0x490) + 2, *(uint8_t *)(local_rsp - 0x418 + 0x478));
    goto loc_0091F790;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091F23C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
