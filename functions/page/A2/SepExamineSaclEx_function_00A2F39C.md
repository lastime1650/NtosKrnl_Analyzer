# SepExamineSaclEx

- RVA: `0x00A2F39C`–`0x00A2F8A6` (길이 `1,290` bytes)
- VA: `0x0000000140A2F39C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ACAB8`
- 디코드: `281`개 명령, `1,290/1,290` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A2F4C9` → [SepSidInToken](../../text/3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00A2F551` → [AuthzBasepFreeSecurityAttributesList](../../text/30/AuthzBasepFreeSecurityAttributesList_function_00301230.md) (function, `0x00301230`)
- `0x00A2F55B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2F572` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00A2F6A1` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00A2F6D7` → [SepSidInToken](../../text/3D/SepSidInToken_function_003D0430.md) (function, `0x003D0430`)
- `0x00A2F753` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00A2F7FF` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x00A2F841` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)

### Direct callers
- [sub_006F3118](../../text/6F/Unknown_function_006F3118.md) at `0x006F31AD`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1D1A5`

### Static image references
- `0x00A2F42C` → RVA `0x00FD9AC8` (`PAGEDATA`; read)
- `0x00A2F59F` → RVA `0x00E67D48` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A2F4C9` → [SepSidInToken](../../text/3D/SepSidInToken_function_003D0430.md) (`PAGE` → `.text`)
  - `0x00A2F551` → [AuthzBasepFreeSecurityAttributesList](../../text/30/AuthzBasepFreeSecurityAttributesList_function_00301230.md) (`PAGE` → `.text`)
  - `0x00A2F55B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2F572` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00A2F6A1` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (`PAGE` → `.text`)
  - `0x00A2F6D7` → [SepSidInToken](../../text/3D/SepSidInToken_function_003D0430.md) (`PAGE` → `.text`)
  - `0x00A2F753` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00A2F7FF` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (`PAGE` → `.text`)
  - `0x00A2F841` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00A2F7CE` → [sub_00B397DE](../B3/Unknown_function_00B397DE.md) (`tail-transfer`)
  - `0x00A2F7DF` → [sub_00B397DE + 0x61](../B3/Unknown_function_00B397DE.md) (`tail-transfer`)
  - `0x00A2F7E9` → [sub_00B397DE + 0x63](../B3/Unknown_function_00B397DE.md) (`tail-transfer`)
  - `0x00A2F884` → [sub_00B397DE + 0x213](../B3/Unknown_function_00B397DE.md) (`tail-transfer`)
  - `0x00A2F8A1` → [sub_00B397DE + 0x1B6](../B3/Unknown_function_00B397DE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A2F39C  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00A2F3A1  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00A2F3A6  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A2F3AB  53                              push rbx
00A2F3AC  55                              push rbp
00A2F3AD  56                              push rsi
00A2F3AE  57                              push rdi
00A2F3AF  41 54                           push r12
00A2F3B1  41 55                           push r13
00A2F3B3  41 56                           push r14
00A2F3B5  41 57                           push r15
00A2F3B7  48 81 EC 98 00 00 00            sub rsp, 0x98
00A2F3BE  83 4C 24 6C FF                  or dword ptr [rsp + 0x6c], 0xffffffff
00A2F3C3  45 33 E4                        xor r12d, r12d
00A2F3C6  4D 8B D0                        mov r10, r8
00A2F3C9  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00A2F3CE  45 33 C0                        xor r8d, r8d
00A2F3D1  41 8B C1                        mov eax, r9d
00A2F3D4  4C 8B 8C 24 40 01 00 00         mov r9, qword ptr [rsp + 0x140]
00A2F3DC  4C 8B DA                        mov r11, rdx
00A2F3DF  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00A2F3E4  48 8B D9                        mov rbx, rcx
00A2F3E7  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F3EF  45 88 20                        mov byte ptr [r8], r12b
00A2F3F2  45 88 21                        mov byte ptr [r9], r12b
00A2F3F5  48 85 C9                        test rcx, rcx
00A2F3F8  74 61                           je 0x140a2f45b
00A2F3FA  0F B7 69 04                     movzx ebp, word ptr [rcx + 4]
00A2F3FE  89 6C 24 70                     mov dword ptr [rsp + 0x70], ebp
00A2F402  85 ED                           test ebp, ebp
00A2F404  74 55                           je 0x140a2f45b
00A2F406  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
00A2F40E  41 8D 7C 24 40                  lea edi, [r12 + 0x40]
00A2F413  45 32 ED                        xor r13b, r13b
00A2F416  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00A2F41B  0F BA E0 19                     bt eax, 0x19
00A2F41F  0F 82 71 03 00 00               jb 0x140a2f796
00A2F425  49 8B 82 98 00 00 00            mov rax, qword ptr [r10 + 0x98]
00A2F42C  48 8B 15 95 A6 5A 00            mov rdx, qword ptr [rip + 0x5aa695]
00A2F433  48 8B 08                        mov rcx, qword ptr [rax]
00A2F436  0F B7 02                        movzx eax, word ptr [rdx]
00A2F439  66 39 01                        cmp word ptr [rcx], ax
00A2F43C  0F 84 23 01 00 00               je 0x140a2f565
00A2F442  33 D2                           xor edx, edx
00A2F444  48 8D 73 08                     lea rsi, [rbx + 8]
00A2F448  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
00A2F44F  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
00A2F457  85 ED                           test ebp, ebp
00A2F459  75 15                           jne 0x140a2f470
00A2F45B  48 81 C4 98 00 00 00            add rsp, 0x98
00A2F462  41 5F                           pop r15
00A2F464  41 5E                           pop r14
00A2F466  41 5D                           pop r13
00A2F468  41 5C                           pop r12
00A2F46A  5F                              pop rdi
00A2F46B  5E                              pop rsi
00A2F46C  5D                              pop rbp
00A2F46D  5B                              pop rbx
00A2F46E  C3                              ret
00A2F46F  CC                              int3
00A2F470  8B AC 24 08 01 00 00            mov ebp, dword ptr [rsp + 0x108]
00A2F477  41 80 38 00                     cmp byte ptr [r8], 0
00A2F47B  0F 85 60 01 00 00               jne 0x140a2f5e1
00A2F481  41 80 39 00                     cmp byte ptr [r9], 0
00A2F485  0F 85 56 01 00 00               jne 0x140a2f5e1
00A2F48B  44 8A 76 01                     mov r14b, byte ptr [rsi + 1]
00A2F48F  41 F6 C6 08                     test r14b, 8
00A2F493  75 76                           jne 0x140a2f50b
00A2F495  83 4C 24 68 FF                  or dword ptr [rsp + 0x68], 0xffffffff
00A2F49A  8A 06                           mov al, byte ptr [rsi]
00A2F49C  3C 02                           cmp al, 2
00A2F49E  0F 85 4B 01 00 00               jne 0x140a2f5ef
00A2F4A4  8A 84 24 30 01 00 00            mov al, byte ptr [rsp + 0x130]
00A2F4AB  48 8D 5E 08                     lea rbx, [rsi + 8]
00A2F4AF  48 8B 94 24 28 01 00 00         mov rdx, qword ptr [rsp + 0x128]
00A2F4B7  4C 8B C3                        mov r8, rbx
00A2F4BA  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A2F4BE  41 B1 01                        mov r9b, 1
00A2F4C1  49 8B CA                        mov rcx, r10
00A2F4C4  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00A2F4C9  E8 62 0F 9A FF                  call 0x1403d0430
00A2F4CE  84 C0                           test al, al
00A2F4D0  0F 84 59 02 00 00               je 0x140a2f72f
00A2F4D6  8B 7E 04                        mov edi, dword ptr [rsi + 4]
00A2F4D9  85 ED                           test ebp, ebp
00A2F4DB  0F 85 CC 02 00 00               jne 0x140a2f7ad
00A2F4E1  41 39 2F                        cmp dword ptr [r15], ebp
00A2F4E4  0F 8C 7B 02 00 00               jl 0x140a2f765
00A2F4EA  41 F6 C6 40                     test r14b, 0x40
00A2F4EE  0F 85 C6 00 00 00               jne 0x140a2f5ba
00A2F4F4  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F4FC  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00A2F503  4C 8B 8C 24 40 01 00 00         mov r9, qword ptr [rsp + 0x140]
00A2F50B  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
00A2F50F  FF C2                           inc edx
00A2F511  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
00A2F519  48 03 F0                        add rsi, rax
00A2F51C  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
00A2F524  4C 8B 9C 24 E8 00 00 00         mov r11, qword ptr [rsp + 0xe8]
00A2F52C  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
00A2F533  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
00A2F53B  3B 54 24 70                     cmp edx, dword ptr [rsp + 0x70]
00A2F53F  0F 82 32 FF FF FF               jb 0x140a2f477
00A2F545  4D 85 E4                        test r12, r12
00A2F548  0F 84 0D FF FF FF               je 0x140a2f45b
00A2F54E  49 8B CC                        mov rcx, r12
00A2F551  E8 DA 1C 8D FF                  call 0x140301230
00A2F556  33 D2                           xor edx, edx
00A2F558  49 8B CC                        mov rcx, r12
00A2F55B  E8 10 33 15 00                  call 0x140b82870
00A2F560  E9 F6 FE FF FF                  jmp 0x140a2f45b
00A2F565  44 0F B6 42 01                  movzx r8d, byte ptr [rdx + 1]
00A2F56A  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
00A2F572  E8 99 75 C9 FF                  call 0x1406c6b10
00A2F577  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F57F  4C 8B 8C 24 40 01 00 00         mov r9, qword ptr [rsp + 0x140]
00A2F587  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
00A2F58F  4C 8B 9C 24 E8 00 00 00         mov r11, qword ptr [rsp + 0xe8]
00A2F597  85 C0                           test eax, eax
00A2F599  0F 85 A3 FE FF FF               jne 0x140a2f442
00A2F59F  48 8B 05 A2 87 43 00            mov rax, qword ptr [rip + 0x4387a2]
00A2F5A6  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00A2F5AA  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
00A2F5B1  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00A2F5B5  E9 88 FE FF FF                  jmp 0x140a2f442
00A2F5BA  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00A2F5C2  85 38                           test dword ptr [rax], edi
00A2F5C4  75 0A                           jne 0x140a2f5d0
00A2F5C6  41 80 FD 40                     cmp r13b, 0x40
00A2F5CA  0F 85 24 FF FF FF               jne 0x140a2f4f4
00A2F5D0  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F5D8  41 C6 00 01                     mov byte ptr [r8], 1
00A2F5DC  E9 1B FF FF FF                  jmp 0x140a2f4fc
00A2F5E1  83 FD 01                        cmp ebp, 1
00A2F5E4  0F 86 5B FF FF FF               jbe 0x140a2f545
00A2F5EA  E9 9C FE FF FF                  jmp 0x140a2f48b
00A2F5EF  3C 07                           cmp al, 7
00A2F5F1  0F 84 DC 01 00 00               je 0x140a2f7d3
00A2F5F7  3C 0D                           cmp al, 0xd
00A2F5F9  0F 85 0C FF FF FF               jne 0x140a2f50b
00A2F5FF  44 8B 7E 04                     mov r15d, dword ptr [rsi + 4]
00A2F603  48 8D 5E 08                     lea rbx, [rsi + 8]
00A2F607  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
00A2F60B  8D 3C 85 08 00 00 00            lea edi, [rax*4 + 8]
00A2F612  4D 85 DB                        test r11, r11
00A2F615  0F 85 D3 01 00 00               jne 0x140a2f7ee
00A2F61B  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
00A2F61F  2B CF                           sub ecx, edi
00A2F621  8D 41 F8                        lea eax, [rcx - 8]
00A2F624  85 C0                           test eax, eax
00A2F626  0F 8E D7 FE FF FF               jle 0x140a2f503
00A2F62C  4C 8B 9C 24 F0 00 00 00         mov r11, qword ptr [rsp + 0xf0]
00A2F634  49 8B 83 48 04 00 00            mov rax, qword ptr [r11 + 0x448]
00A2F63B  48 85 C0                        test rax, rax
00A2F63E  0F 84 33 01 00 00               je 0x140a2f777
00A2F644  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00A2F64B  48 8B 90 50 02 00 00            mov rdx, qword ptr [rax + 0x250]
00A2F652  4C 8B 80 48 02 00 00            mov r8, qword ptr [rax + 0x248]
00A2F659  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
00A2F660  8D 41 F8                        lea eax, [rcx - 8]
00A2F663  8B CF                           mov ecx, edi
00A2F665  48 03 CB                        add rcx, rbx
00A2F668  48 8D 7C 24 6C                  lea rdi, [rsp + 0x6c]
00A2F66D  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00A2F672  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
00A2F677  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
00A2F67C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A2F680  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A2F685  49 8B CB                        mov rcx, r11
00A2F688  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00A2F68D  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
00A2F692  4D 8B C4                        mov r8, r12
00A2F695  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A2F69A  49 8B 93 08 03 00 00            mov rdx, qword ptr [r11 + 0x308]
00A2F6A1  E8 2A F5 8C FF                  call 0x1402febd0
00A2F6A6  83 7C 24 6C 01                  cmp dword ptr [rsp + 0x6c], 1
00A2F6AB  0F 85 43 FE FF FF               jne 0x140a2f4f4
00A2F6B1  8A 84 24 30 01 00 00            mov al, byte ptr [rsp + 0x130]
00A2F6B8  41 B1 01                        mov r9b, 1
00A2F6BB  48 8B 94 24 28 01 00 00         mov rdx, qword ptr [rsp + 0x128]
00A2F6C3  4C 8B C3                        mov r8, rbx
00A2F6C6  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A2F6CE  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A2F6D2  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00A2F6D7  E8 54 0D 9A FF                  call 0x1403d0430
00A2F6DC  84 C0                           test al, al
00A2F6DE  0F 84 39 01 00 00               je 0x140a2f81d
00A2F6E4  48 8B BC 24 18 01 00 00         mov rdi, qword ptr [rsp + 0x118]
00A2F6EC  85 ED                           test ebp, ebp
00A2F6EE  0F 85 8C 01 00 00               jne 0x140a2f880
00A2F6F4  39 2F                           cmp dword ptr [rdi], ebp
00A2F6F6  0F 8D 57 01 00 00               jge 0x140a2f853
00A2F6FC  45 84 F6                        test r14b, r14b
00A2F6FF  0F 89 EF FD FF FF               jns 0x140a2f4f4
00A2F705  44 85 BC 24 F8 00 00 00         test dword ptr [rsp + 0xf8], r15d
00A2F70D  74 78                           je 0x140a2f787
00A2F70F  4C 8B 8C 24 40 01 00 00         mov r9, qword ptr [rsp + 0x140]
00A2F717  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F71F  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00A2F726  41 C6 01 01                     mov byte ptr [r9], 1
00A2F72A  E9 DC FD FF FF                  jmp 0x140a2f50b
00A2F72F  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00A2F734  45 85 C0                        test r8d, r8d
00A2F737  0F 84 B7 FD FF FF               je 0x140a2f4f4
00A2F73D  48 8B 0D 04 86 43 00            mov rcx, qword ptr [rip + 0x438604]
00A2F744  0F B7 03                        movzx eax, word ptr [rbx]
00A2F747  66 39 01                        cmp word ptr [rcx], ax
00A2F74A  0F 85 A4 FD FF FF               jne 0x140a2f4f4
00A2F750  48 8B D3                        mov rdx, rbx
00A2F753  E8 B8 73 C9 FF                  call 0x1406c6b10
00A2F758  85 C0                           test eax, eax
00A2F75A  0F 84 76 FD FF FF               je 0x140a2f4d6
00A2F760  E9 8F FD FF FF                  jmp 0x140a2f4f4
00A2F765  45 84 F6                        test r14b, r14b
00A2F768  0F 89 86 FD FF FF               jns 0x140a2f4f4
00A2F76E  85 BC 24 F8 00 00 00            test dword ptr [rsp + 0xf8], edi
00A2F775  EB 96                           jmp 0x140a2f70d
00A2F777  45 33 C9                        xor r9d, r9d
00A2F77A  33 D2                           xor edx, edx
00A2F77C  45 33 C0                        xor r8d, r8d
00A2F77F  45 33 D2                        xor r10d, r10d
00A2F782  E9 D9 FE FF FF                  jmp 0x140a2f660
00A2F787  41 80 FD 80                     cmp r13b, 0x80
00A2F78B  0F 85 63 FD FF FF               jne 0x140a2f4f4
00A2F791  E9 79 FF FF FF                  jmp 0x140a2f70f
00A2F796  45 39 27                        cmp dword ptr [r15], r12d
00A2F799  41 BD 80 00 00 00               mov r13d, 0x80
00A2F79F  44 0F 4D EF                     cmovge r13d, edi
00A2F7A3  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00A2F7A8  E9 78 FC FF FF                  jmp 0x140a2f425
00A2F7AD  33 DB                           xor ebx, ebx
00A2F7AF  85 ED                           test ebp, ebp
00A2F7B1  0F 84 3D FD FF FF               je 0x140a2f4f4
00A2F7B7  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
00A2F7BF  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
00A2F7C7  8B B4 24 F8 00 00 00            mov esi, dword ptr [rsp + 0xf8]
00A2F7CE  E9 0B A0 10 00                  jmp 0x140b397de
00A2F7D3  8B 46 08                        mov eax, dword ptr [rsi + 8]
00A2F7D6  8B C8                           mov ecx, eax
00A2F7D8  44 8B 7E 04                     mov r15d, dword ptr [rsi + 4]
00A2F7DC  83 E1 01                        and ecx, 1
00A2F7DF  0F 84 5A A0 10 00               je 0x140b3983f
00A2F7E5  48 8D 7E 0C                     lea rdi, [rsi + 0xc]
00A2F7E9  E9 53 A0 10 00                  jmp 0x140b39841
00A2F7EE  4D 85 E4                        test r12, r12
00A2F7F1  0F 85 24 FE FF FF               jne 0x140a2f61b
00A2F7F7  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00A2F7FC  49 8B CB                        mov rcx, r11
00A2F7FF  E8 80 36 8D FF                  call 0x140302e84
00A2F804  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00A2F80C  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00A2F813  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00A2F818  E9 FE FD FF FF                  jmp 0x140a2f61b
00A2F81D  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00A2F822  45 85 C0                        test r8d, r8d
00A2F825  0F 84 C9 FC FF FF               je 0x140a2f4f4
00A2F82B  48 8B 0D 16 85 43 00            mov rcx, qword ptr [rip + 0x438516]
00A2F832  0F B7 03                        movzx eax, word ptr [rbx]
00A2F835  66 39 01                        cmp word ptr [rcx], ax
00A2F838  0F 85 B6 FC FF FF               jne 0x140a2f4f4
00A2F83E  48 8B D3                        mov rdx, rbx
00A2F841  E8 CA 72 C9 FF                  call 0x1406c6b10
00A2F846  85 C0                           test eax, eax
00A2F848  0F 85 A6 FC FF FF               jne 0x140a2f4f4
00A2F84E  E9 91 FE FF FF                  jmp 0x140a2f6e4
00A2F853  BF 40 00 00 00                  mov edi, 0x40
00A2F858  44 84 F7                        test dil, r14b
00A2F85B  0F 84 93 FC FF FF               je 0x140a2f4f4
00A2F861  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00A2F869  44 85 38                        test dword ptr [rax], r15d
00A2F86C  0F 85 5E FD FF FF               jne 0x140a2f5d0
00A2F872  44 3A EF                        cmp r13b, dil
00A2F875  0F 85 79 FC FF FF               jne 0x140a2f4f4
00A2F87B  E9 50 FD FF FF                  jmp 0x140a2f5d0
00A2F880  33 DB                           xor ebx, ebx
00A2F882  85 ED                           test ebp, ebp
00A2F884  0F 84 67 A1 10 00               je 0x140b399f1
00A2F88A  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
00A2F892  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
00A2F89A  8B B4 24 F8 00 00 00            mov esi, dword ptr [rsp + 0xf8]
00A2F8A1  E9 EE A0 10 00                  jmp 0x140b39994
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepExamineSaclEx(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, unsigned __int8 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned int v_stack_pF8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (152);
    v_r12 = 0;
    v_stack_m60 = 0;
    a3 = 0;
    v_stack_m78 = 0;
    *(unsigned __int8 *)(a12) = 0;
    *(unsigned __int8 *)(a13) = 0;
    if (a1 == 0) goto loc_00A2F45B;
    v_stack_m68 = (unsigned int)(*(unsigned __int16 *)(a1 + 4));
    if ((unsigned int)(*(unsigned __int16 *)(a1 + 4)) == 0) goto loc_00A2F45B;
    v_r13 = 0;
    v_stack_m74 = 0;
    if (condition_is_below) goto loc_00A2F796;
loc_00A2F425:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 152)))) == ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 5940885))))) goto loc_00A2F565;
loc_00A2F442:
    a2 = 0;
    v_stack_p8 = 0;
    v_stack_m58 = a1 + 8;
    if ((unsigned int)(*(unsigned __int16 *)(a1 + 4)) != 0) goto loc_00A2F470;
loc_00A2F45B:
    v_rsp = (v_rsp) + (152);
    return *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 5940885));
loc_00A2F470:
loc_00A2F477:
    if ((*(unsigned __int8 *)(a12)) != 0) goto loc_00A2F5E1;
    if ((*(unsigned __int8 *)(a13)) != 0) goto loc_00A2F5E1;
loc_00A2F48B:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 1))) & (8)) != 0) goto loc_00A2F50B;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 8))) != 2) goto loc_00A2F5EF;
    v_stack_p28 = a11;
    v_stack_p20 = 0;
    result = SepSidInToken(0, a10, a1 + 8 + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00A2F72F;
loc_00A2F4D6:
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00A2F7AD;
    if ((*(unsigned int *)(a8)) < ((unsigned int)((unsigned int)(a6)))) goto loc_00A2F765;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 1))) & (64)) != 0) goto loc_00A2F5BA;
loc_00A2F4F4:
loc_00A2F4FC:
loc_00A2F503:
loc_00A2F50B:
    a2 = (unsigned int)(((unsigned int)(v_stack_pE0)) + 1);
    v_rsi = (a1 + 8) + (*(unsigned __int16 *)(a1 + 8 + 2));
    v_stack_pE0 = (unsigned int)(a2);
    v_stack_p80 = v_rsi;
    if (((unsigned int)(a2)) < v_stack_p70) goto loc_00A2F477;
loc_00A2F545:
    if (0 == 0) goto loc_00A2F45B;
    result = AuthzBasepFreeSecurityAttributesList(0, a2, a12, a13);
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a12, a13);
    goto loc_00A2F45B;
loc_00A2F565:
    result = memcmp(0, a2, *(unsigned __int8 *)(a2 + 1) * 4 + 8, a13);
    if ((unsigned int)(result) != 0) goto loc_00A2F442;
    v_stack_p60 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4425634) + 1) * 4 + 8);
    goto loc_00A2F442;
loc_00A2F5BA:
    if (((*(unsigned int *)(a9)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8 + 4))))) != 0) goto loc_00A2F5D0;
    if (0 != 64) goto loc_00A2F4F4;
loc_00A2F5D0:
    *(unsigned __int8 *)(a12) = 1;
    goto loc_00A2F4FC;
loc_00A2F5E1:
    if (((unsigned int)((unsigned int)(a6))) <= 1) goto loc_00A2F545;
    goto loc_00A2F48B;
loc_00A2F5EF:
    if (((unsigned __int8)(a9)) == 7) goto loc_00A2F7D3;
    if (((unsigned __int8)(a9)) != 13) goto loc_00A2F50B;
    if (v_stack_pE8 != 0) goto loc_00A2F7EE;
loc_00A2F61B:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 2)) - ((unsigned int)(*(unsigned __int8 *)(v_rsi + 8 + 1) * 4 + 8)));
    if (condition_is_less_or_equal) goto loc_00A2F503;
    if (*(unsigned __int64 *)(v_stack_pF0 + 1096) == 0) goto loc_00A2F777;
loc_00A2F660:
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rsi + 8 + 1) * 4 + 8))) + (v_rsi + 8);
    v_stack_p58 = v_stack_p6C;
    v_stack_p50 = 0;
    v_stack_p48 = 1;
    v_stack_p40 = (unsigned int)(a1 - 8);
    v_stack_p38 = a1;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF0 + 1096) + 600);
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF0 + 1096) + 584);
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF0 + 1096) + 592);
    result = AuthzBasepEvaluateAceCondition(v_stack_pF0, *(unsigned __int64 *)(v_stack_pF0 + 776), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF0 + 1096) + 576));
    if (v_stack_p6C != 1) goto loc_00A2F4F4;
    v_stack_p28 = a11;
    v_stack_p20 = 0;
    result = SepSidInToken(v_stack_pF0, a10, v_rsi + 8, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00A2F81D;
loc_00A2F6E4:
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00A2F880;
    if ((*(unsigned int *)(a8)) >= ((unsigned int)((unsigned int)(a6)))) goto loc_00A2F853;
    if (!sign_flag) goto loc_00A2F4F4;
loc_00A2F70D:
    if (((v_stack_pF8) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4))))) == 0) goto loc_00A2F787;
loc_00A2F70F:
    *(unsigned __int8 *)(a13) = 1;
    goto loc_00A2F50B;
loc_00A2F72F:
    if ((unsigned int)((unsigned int)(v_stack_p60)) == 0) goto loc_00A2F4F4;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4425220))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rsi + 8)))) goto loc_00A2F4F4;
    result = memcmp(*(unsigned __int64 *)(v_rip + 4425220), v_rsi + 8, (unsigned int)(v_stack_p60), a13);
    if ((unsigned int)(result) == 0) goto loc_00A2F4D6;
    goto loc_00A2F4F4;
loc_00A2F765:
    if (!sign_flag) goto loc_00A2F4F4;
    goto loc_00A2F70D;
loc_00A2F777:
    a4 = 0;
    a2 = 0;
    a3 = 0;
    v_r10 = 0;
    goto loc_00A2F660;
loc_00A2F787:
    if (0 != 128) goto loc_00A2F4F4;
    goto loc_00A2F70F;
loc_00A2F796:
    v_r13 = 128;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi + 4)))) >= 0) { v_r13 = (unsigned int)(a8); }
    v_stack_p64 = (unsigned int)(v_r13);
    goto loc_00A2F425;
loc_00A2F7AD:
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_00A2F4F4;
loc_00A2F7D3:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_pF8) + 8))))) & (1));
loc_00A2F7EE:
    if (a12 != 0) goto loc_00A2F61B;
    result = AuthzBasepInitializeResourceClaimsFromSacl(v_stack_pF0, v_stack_p78, a3, a4);
    goto loc_00A2F61B;
loc_00A2F81D:
    if ((unsigned int)((unsigned int)(v_stack_p60)) == 0) goto loc_00A2F4F4;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4424982))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)))) goto loc_00A2F4F4;
    result = memcmp(*(unsigned __int64 *)(v_rip + 4424982), 0, (unsigned int)(v_stack_p60), a4);
    if ((unsigned int)(result) != 0) goto loc_00A2F4F4;
    goto loc_00A2F6E4;
loc_00A2F853:
    if (((64) & ((unsigned __int8)(*(unsigned __int8 *)(a1 + 8 + 1)))) == 0) goto loc_00A2F4F4;
    if (((*(unsigned int *)(a9)) & ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_pF8) + 4))))) != 0) goto loc_00A2F5D0;
    if (((unsigned __int8)(a13)) != 64) goto loc_00A2F4F4;
    goto loc_00A2F5D0;
loc_00A2F880:
    v_rbx = 0;
}
```

## 5. (Beta) C Style

```c
int64_t SepExamineSaclEx(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint64_t Arg5, uint32_t Arg6, uint64_t Arg7, void *Arg8, void *Arg9, int64_t Arg10, uint8_t Arg11, void *Arg12, void *Arg13)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint8_t v_stack_p48;
    uint8_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint32_t v_stack_pF8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (152);
    local_r12 = 0;
    v_stack_m60 = 0;
    Arg3 = 0;
    v_stack_m78 = 0;
    *(uint8_t *)(arg12) = 0;
    *(uint8_t *)(arg13) = 0;
    if (Arg1 == NULL) goto loc_00A2F45B;
    v_stack_m68 = (uint32_t)(*(uint16_t *)(arg1 + 0x4));
    if ((uint32_t)(*(uint16_t *)(arg1 + 0x4)) == 0) goto loc_00A2F45B;
    local_r13 = 0;
    v_stack_m74 = 0;
    if (condition_is_below) goto loc_00A2F796;
loc_00A2F425:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x98)))) == ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x5AA695))))) goto loc_00A2F565;
loc_00A2F442:
    Arg2 = 0;
    v_stack_p8 = 0;
    v_stack_m58 = Arg1 + 8;
    if ((uint32_t)(*(uint16_t *)(arg1 + 0x4)) != 0) goto loc_00A2F470;
loc_00A2F45B:
    local_rsp = (local_rsp) + (152);
    return *(uint16_t *)(*(uint64_t *)(v_rip + 0x5AA695));
loc_00A2F470:
loc_00A2F477:
    if ((*(uint8_t *)(arg12)) != 0) goto loc_00A2F5E1;
    if ((*(uint8_t *)(arg13)) != 0) goto loc_00A2F5E1;
loc_00A2F48B:
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0x1))) & (8)) != 0) goto loc_00A2F50B;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8))) != 2) goto loc_00A2F5EF;
    v_stack_p28 = Arg11;
    v_stack_p20 = 0;
    result = SepSidInToken(0, Arg10, Arg1 + 8 + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_00A2F72F;
loc_00A2F4D6:
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00A2F7AD;
    if ((*(uint32_t *)(arg8)) < ((uint32_t)((uint32_t)(Arg6)))) goto loc_00A2F765;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0x1))) & (64)) != 0) goto loc_00A2F5BA;
loc_00A2F4F4:
loc_00A2F4FC:
loc_00A2F503:
loc_00A2F50B:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_pE0)) + 1);
    local_rsi = (Arg1 + 8) + (*(uint16_t *)(arg1 + 0x8 + 0x2));
    v_stack_pE0 = (uint32_t)(Arg2);
    v_stack_p80 = local_rsi;
    if (((uint32_t)(Arg2)) < v_stack_p70) goto loc_00A2F477;
loc_00A2F545:
    if (0 == 0) goto loc_00A2F45B;
    result = AuthzBasepFreeSecurityAttributesList(0, Arg2, Arg12, Arg13);
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, Arg12, Arg13);
    goto loc_00A2F45B;
loc_00A2F565:
    result = memcmp(0, Arg2, *(uint8_t *)(Arg2 + 0x1) * 4 + 8, Arg13);
    if ((uint32_t)(result) != 0) goto loc_00A2F442;
    v_stack_p60 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x4387A2) + 0x1) * 4 + 8);
    goto loc_00A2F442;
loc_00A2F5BA:
    if (((*(uint32_t *)(arg9)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8 + 0x4))))) != 0) goto loc_00A2F5D0;
    if (0 != 64) goto loc_00A2F4F4;
loc_00A2F5D0:
    *(uint8_t *)(arg12) = 1;
    goto loc_00A2F4FC;
loc_00A2F5E1:
    if (((uint32_t)((uint32_t)(Arg6))) <= 1) goto loc_00A2F545;
    goto loc_00A2F48B;
loc_00A2F5EF:
    if (((uint8_t)(Arg9)) == 7) goto loc_00A2F7D3;
    if (((uint8_t)(Arg9)) != 13) goto loc_00A2F50B;
    if (v_stack_pE8 != 0) goto loc_00A2F7EE;
loc_00A2F61B:
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x2)) - ((uint32_t)(*(uint8_t *)(local_rsi + 0x8 + 0x1) * 4 + 8)));
    if (condition_is_less_or_equal) goto loc_00A2F503;
    if (*(uint64_t *)(v_stack_pF0 + 0x448) == 0) goto loc_00A2F777;
loc_00A2F660:
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(local_rsi + 0x8 + 0x1) * 4 + 8))) + (local_rsi + 8);
    v_stack_p58 = v_stack_p6C;
    v_stack_p50 = 0;
    v_stack_p48 = 1;
    v_stack_p40 = (uint32_t)(Arg1 - 8);
    v_stack_p38 = Arg1;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(v_stack_pF0 + 0x448) + 0x258);
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(v_stack_pF0 + 0x448) + 0x248);
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(v_stack_pF0 + 0x448) + 0x250);
    result = AuthzBasepEvaluateAceCondition(v_stack_pF0, *(uint64_t *)(v_stack_pF0 + 0x308), 0, *(uint64_t *)(*(uint64_t *)(v_stack_pF0 + 0x448) + 0x240));
    if (v_stack_p6C != 1) goto loc_00A2F4F4;
    v_stack_p28 = Arg11;
    v_stack_p20 = 0;
    result = SepSidInToken(v_stack_pF0, Arg10, local_rsi + 8, 1);
    if ((uint8_t)(result) == 0) goto loc_00A2F81D;
loc_00A2F6E4:
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00A2F880;
    if ((*(uint32_t *)(arg8)) >= ((uint32_t)((uint32_t)(Arg6)))) goto loc_00A2F853;
    if (!sign_flag) goto loc_00A2F4F4;
loc_00A2F70D:
    if (((v_stack_pF8) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4))))) == 0) goto loc_00A2F787;
loc_00A2F70F:
    *(uint8_t *)(arg13) = 1;
    goto loc_00A2F50B;
loc_00A2F72F:
    if ((uint32_t)((uint32_t)(v_stack_p60)) == 0) goto loc_00A2F4F4;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x438604))) != ((uint16_t)(*(uint16_t *)(local_rsi + 0x8)))) goto loc_00A2F4F4;
    result = memcmp(*(uint64_t *)(v_rip + 0x438604), local_rsi + 8, (uint32_t)(v_stack_p60), Arg13);
    if ((uint32_t)(result) == 0) goto loc_00A2F4D6;
    goto loc_00A2F4F4;
loc_00A2F765:
    if (!sign_flag) goto loc_00A2F4F4;
    goto loc_00A2F70D;
loc_00A2F777:
    Arg4 = 0;
    Arg2 = 0;
    Arg3 = 0;
    local_r10 = 0;
    goto loc_00A2F660;
loc_00A2F787:
    if (0 != 128) goto loc_00A2F4F4;
    goto loc_00A2F70F;
loc_00A2F796:
    local_r13 = 128;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)))) >= 0) { local_r13 = (uint32_t)(Arg8); }
    v_stack_p64 = (uint32_t)(local_r13);
    goto loc_00A2F425;
loc_00A2F7AD:
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_00A2F4F4;
loc_00A2F7D3:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_pF8) + 0x8))))) & (1));
loc_00A2F7EE:
    if (Arg12 != NULL) goto loc_00A2F61B;
    result = AuthzBasepInitializeResourceClaimsFromSacl(v_stack_pF0, v_stack_p78, Arg3, Arg4);
    goto loc_00A2F61B;
loc_00A2F81D:
    if ((uint32_t)((uint32_t)(v_stack_p60)) == 0) goto loc_00A2F4F4;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x438516))) != ((uint16_t)(*(uint16_t *)(local_rbx)))) goto loc_00A2F4F4;
    result = memcmp(*(uint64_t *)(v_rip + 0x438516), 0, (uint32_t)(v_stack_p60), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A2F4F4;
    goto loc_00A2F6E4;
loc_00A2F853:
    if (((64) & ((uint8_t)(*(uint8_t *)(arg1 + 0x8 + 0x1)))) == 0) goto loc_00A2F4F4;
    if (((*(uint32_t *)(arg9)) & ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_pF8) + 0x4))))) != 0) goto loc_00A2F5D0;
    if (((uint8_t)(Arg13)) != 64) goto loc_00A2F4F4;
    goto loc_00A2F5D0;
loc_00A2F880:
    local_rbx = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0xC` | `64` | `R` |
| `Arg3` | `+ 0x98` | `64` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |
| `Arg12` | `+ 0x0` | `8` | `R` |
| `Arg12` | `+ 0x0` | `8` | `W` |
| `Arg13` | `+ 0x0` | `8` | `R` |
| `Arg13` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2F39C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
