# AuthzBasepDuplicateSecurityAttributes

- RVA: `0x003023C0`–`0x00302AD4` (길이 `1,812` bytes)
- VA: `0x00000001403023C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007335C`
- 디코드: `489`개 명령, `1,812/1,812` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00302429` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00302443` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030247B` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00302535` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0030254B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030268C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0030274D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003027AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003027C6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00302809` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00302888` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00302911` → [AuthzBasepAllocateSecurityAttributeValue](AuthzBasepAllocateSecurityAttributeValue_function_00302AE0.md) (function, `0x00302AE0`)
- `0x00302938` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003029EA` → [AuthzBasepAllocateSecurityAttributeValue](AuthzBasepAllocateSecurityAttributeValue_function_00302AE0.md) (function, `0x00302AE0`)
- `0x00302A1A` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00302A88` → [AuthzBasepRemoveSecurityAttributeValueFromLists](AuthzBasepRemoveSecurityAttributeValueFromLists_function_00302E00.md) (function, `0x00302E00`)
- `0x00302A92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00302AC6` → [AuthzBasepRollbackSecurityAttributeChanges](../69/AuthzBasepRollbackSecurityAttributeChanges_function_0069D5C0.md) (function, `0x0069D5C0`)

### Direct callers
- [SepGetAnonymousToken](SepGetAnonymousToken_function_00301830.md) at `0x00301970`
- [sub_003A7C07](../3A/Unknown_function_003A7C07.md) at `0x003A7C55`
- [SepValidateAndCopyGlobalEntry](../4F/SepValidateAndCopyGlobalEntry_function_004F825C.md) at `0x004F830D`
- [SepDuplicateToken](../../page/8B/SepDuplicateToken_function_008B87EC.md) at `0x008B8C95`
- [SepFilterToken](../../page/9C/SepFilterToken_function_009C6B80.md) at `0x009C710E`
- [SepDuplicateClaimAttributes](../../page/A7/SepDuplicateClaimAttributes_function_00A76334.md) at `0x00A763B6`
- [SepDuplicateClaimAttributes](../../page/A7/SepDuplicateClaimAttributes_function_00A76334.md) at `0x00A76465`

### Static image references
- `0x003023E6` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00302429` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00302535` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0030268C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0030274D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x003027AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00302888` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00302A92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003023C0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003023C5  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
003023CA  55                              push rbp
003023CB  56                              push rsi
003023CC  57                              push rdi
003023CD  41 54                           push r12
003023CF  41 55                           push r13
003023D1  41 56                           push r14
003023D3  41 57                           push r15
003023D5  48 83 EC 20                     sub rsp, 0x20
003023D9  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
003023DD  48 8D 41 08                     lea rax, [rcx + 8]
003023E1  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003023E6  4C 8D 25 13 DC CF FF            lea r12, [rip - 0x3023ed]
003023ED  41 0F B6 E8                     movzx ebp, r8b
003023F1  4C 8B EA                        mov r13, rdx
003023F4  45 33 FF                        xor r15d, r15d
003023F7  4C 3B F0                        cmp r14, rax
003023FA  0F 84 85 01 00 00               je 0x140302585
00302400  40 84 ED                        test bpl, bpl
00302403  0F 85 C6 04 00 00               jne 0x1403028cf
00302409  41 0F B7 56 20                  movzx edx, word ptr [r14 + 0x20]
0030240E  B9 00 01 00 00                  mov ecx, 0x100
00302413  48 83 C2 70                     add rdx, 0x70
00302417  44 0F 20 C0                     mov rax, cr8
0030241B  3C 02                           cmp al, 2
0030241D  0F 83 7F 06 00 00               jae 0x140302aa2
00302423  41 B8 53 65 41 74               mov r8d, 0x74416553
00302429  E8 C2 FC 87 00                  call 0x140b820f0
0030242E  48 8B F8                        mov rdi, rax
00302431  48 85 C0                        test rax, rax
00302434  0F 84 45 01 00 00               je 0x14030257f
0030243A  33 D2                           xor edx, edx
0030243C  48 8B C8                        mov rcx, rax
0030243F  44 8D 42 70                     lea r8d, [rdx + 0x70]
00302443  E8 F8 47 3C 00                  call 0x1406c6c40
00302448  41 0F B7 46 20                  movzx eax, word ptr [r14 + 0x20]
0030244D  66 89 47 22                     mov word ptr [rdi + 0x22], ax
00302451  48 8D 47 70                     lea rax, [rdi + 0x70]
00302455  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00302459  48 8B F0                        mov rsi, rax
0030245C  41 0F B7 4E 20                  movzx ecx, word ptr [r14 + 0x20]
00302461  0F B7 47 22                     movzx eax, word ptr [rdi + 0x22]
00302465  49 8B 56 28                     mov rdx, qword ptr [r14 + 0x28]
00302469  66 3B C8                        cmp cx, ax
0030246C  0F 46 C1                        cmovbe eax, ecx
0030246F  48 8B CE                        mov rcx, rsi
00302472  8B D8                           mov ebx, eax
00302474  44 8B C0                        mov r8d, eax
00302477  66 89 5F 20                     mov word ptr [rdi + 0x20], bx
0030247B  E8 C0 43 3C 00                  call 0x1406c6840
00302480  0F B7 4F 20                     movzx ecx, word ptr [rdi + 0x20]
00302484  0F B7 47 22                     movzx eax, word ptr [rdi + 0x22]
00302488  48 83 C1 02                     add rcx, 2
0030248C  48 3B C8                        cmp rcx, rax
0030248F  77 08                           ja 0x140302499
00302491  48 D1 EB                        shr rbx, 1
00302494  66 44 89 3C 5E                  mov word ptr [rsi + rbx*2], r15w
00302499  48 8D 47 48                     lea rax, [rdi + 0x48]
0030249D  48 89 40 08                     mov qword ptr [rax + 8], rax
003024A1  48 89 00                        mov qword ptr [rax], rax
003024A4  48 8D 47 60                     lea rax, [rdi + 0x60]
003024A8  48 89 40 08                     mov qword ptr [rax + 8], rax
003024AC  48 89 00                        mov qword ptr [rax], rax
003024AF  41 8B 4E 34                     mov ecx, dword ptr [r14 + 0x34]
003024B3  89 4F 34                        mov dword ptr [rdi + 0x34], ecx
003024B6  40 84 ED                        test bpl, bpl
003024B9  0F 85 96 05 00 00               jne 0x140302a55
003024BF  41 0F B7 46 30                  movzx eax, word ptr [r14 + 0x30]
003024C4  66 89 47 30                     mov word ptr [rdi + 0x30], ax
003024C8  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
003024CB  A8 02                           test al, 2
003024CD  75 2B                           jne 0x1403024fa
003024CF  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003024D3  49 8D 45 20                     lea rax, [r13 + 0x20]
003024D7  48 8D 57 10                     lea rdx, [rdi + 0x10]
003024DB  48 39 01                        cmp qword ptr [rcx], rax
003024DE  0F 85 94 00 00 00               jne 0x140302578
003024E4  48 89 02                        mov qword ptr [rdx], rax
003024E7  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003024EB  48 89 11                        mov qword ptr [rcx], rdx
003024EE  48 89 50 08                     mov qword ptr [rax + 8], rdx
003024F2  83 4F 38 02                     or dword ptr [rdi + 0x38], 2
003024F6  41 FF 45 18                     inc dword ptr [r13 + 0x18]
003024FA  41 0F B7 46 30                  movzx eax, word ptr [r14 + 0x30]
003024FF  83 F8 06                        cmp eax, 6
00302502  0F 85 4C 02 00 00               jne 0x140302754
00302508  49 8B 76 48                     mov rsi, qword ptr [r14 + 0x48]
0030250C  49 8D 6E 48                     lea rbp, [r14 + 0x48]
00302510  48 3B F5                        cmp rsi, rbp
00302513  0F 84 9A 01 00 00               je 0x1403026b3
00302519  B9 00 01 00 00                  mov ecx, 0x100
0030251E  44 0F 20 C0                     mov rax, cr8
00302522  3C 02                           cmp al, 2
00302524  0F 83 8C 05 00 00               jae 0x140302ab6
0030252A  BA 40 00 00 00                  mov edx, 0x40
0030252F  41 B8 53 65 41 74               mov r8d, 0x74416553
00302535  E8 B6 FB 87 00                  call 0x140b820f0
0030253A  48 8B D8                        mov rbx, rax
0030253D  48 85 C0                        test rax, rax
00302540  74 3D                           je 0x14030257f
00302542  33 D2                           xor edx, edx
00302544  48 8B C8                        mov rcx, rax
00302547  44 8D 42 40                     lea r8d, [rdx + 0x40]
0030254B  E8 F0 46 3C 00                  call 0x1406c6c40
00302550  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00302554  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00302558  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0030255B  A8 02                           test al, 2
0030255D  0F 85 92 03 00 00               jne 0x1403028f5
00302563  48 8B 4F 68                     mov rcx, qword ptr [rdi + 0x68]
00302567  48 8D 47 60                     lea rax, [rdi + 0x60]
0030256B  48 8D 53 10                     lea rdx, [rbx + 0x10]
0030256F  48 39 01                        cmp qword ptr [rcx], rax
00302572  0F 84 68 03 00 00               je 0x1403028e0
00302578  B9 03 00 00 00                  mov ecx, 3
0030257D  CD 29                           int 0x29
0030257F  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
00302585  41 8B EF                        mov ebp, r15d
00302588  49 8D 7D 20                     lea rdi, [r13 + 0x20]
0030258C  F7 D5                           not ebp
0030258E  C1 ED 1F                        shr ebp, 0x1f
00302591  48 8B 0F                        mov rcx, qword ptr [rdi]
00302594  48 3B CF                        cmp rcx, rdi
00302597  0F 84 F6 00 00 00               je 0x140302693
0030259D  48 8D 59 F0                     lea rbx, [rcx - 0x10]
003025A1  40 84 ED                        test bpl, bpl
003025A4  0F 84 16 05 00 00               je 0x140302ac0
003025AA  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003025AD  45 32 F6                        xor r14b, r14b
003025B0  A8 02                           test al, 2
003025B2  74 26                           je 0x1403025da
003025B4  48 8B 11                        mov rdx, qword ptr [rcx]
003025B7  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
003025BB  75 BB                           jne 0x140302578
003025BD  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003025C1  48 39 08                        cmp qword ptr [rax], rcx
003025C4  75 B2                           jne 0x140302578
003025C6  48 89 10                        mov qword ptr [rax], rdx
003025C9  48 89 42 08                     mov qword ptr [rdx + 8], rax
003025CD  83 63 38 FD                     and dword ptr [rbx + 0x38], 0xfffffffd
003025D1  4D 85 ED                        test r13, r13
003025D4  74 04                           je 0x1403025da
003025D6  41 FF 4D 18                     dec dword ptr [r13 + 0x18]
003025DA  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003025DD  8B C8                           mov ecx, eax
003025DF  83 E1 01                        and ecx, 1
003025E2  A8 04                           test al, 4
003025E4  0F 85 DB 00 00 00               jne 0x1403026c5
003025EA  85 C9                           test ecx, ecx
003025EC  75 27                           jne 0x140302615
003025EE  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
003025F2  49 8D 45 08                     lea rax, [r13 + 8]
003025F6  48 39 01                        cmp qword ptr [rcx], rax
003025F9  0F 85 79 FF FF FF               jne 0x140302578
003025FF  48 89 03                        mov qword ptr [rbx], rax
00302602  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00302606  48 89 19                        mov qword ptr [rcx], rbx
00302609  48 89 58 08                     mov qword ptr [rax + 8], rbx
0030260D  83 4B 38 01                     or dword ptr [rbx + 0x38], 1
00302611  41 FF 45 00                     inc dword ptr [r13]
00302615  48 8D 73 60                     lea rsi, [rbx + 0x60]
00302619  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00302620  48 8B 0E                        mov rcx, qword ptr [rsi]
00302623  48 3B CE                        cmp rcx, rsi
00302626  0F 84 4E 02 00 00               je 0x14030287a
0030262C  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0030262F  4C 8D 41 F0                     lea r8, [rcx - 0x10]
00302633  8B D0                           mov edx, eax
00302635  83 E2 04                        and edx, 4
00302638  A8 02                           test al, 2
0030263A  0F 85 67 03 00 00               jne 0x1403029a7
00302640  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
00302644  83 E0 01                        and eax, 1
00302647  85 D2                           test edx, edx
00302649  0F 84 24 03 00 00               je 0x140302973
0030264F  85 C0                           test eax, eax
00302651  74 34                           je 0x140302687
00302653  49 8B 08                        mov rcx, qword ptr [r8]
00302656  4C 39 41 08                     cmp qword ptr [rcx + 8], r8
0030265A  0F 85 18 FF FF FF               jne 0x140302578
00302660  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00302664  4C 39 00                        cmp qword ptr [rax], r8
00302667  0F 85 0B FF FF FF               jne 0x140302578
0030266D  48 89 08                        mov qword ptr [rax], rcx
00302670  48 89 41 08                     mov qword ptr [rcx + 8], rax
00302674  41 83 60 20 FE                  and dword ptr [r8 + 0x20], 0xfffffffe
00302679  FF 4B 3C                        dec dword ptr [rbx + 0x3c]
0030267C  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
00302680  A8 04                           test al, 4
00302682  74 03                           je 0x140302687
00302684  FF 4B 40                        dec dword ptr [rbx + 0x40]
00302687  33 D2                           xor edx, edx
00302689  49 8B C8                        mov rcx, r8
0030268C  E8 DF 01 88 00                  call 0x140b82870
00302691  EB 8D                           jmp 0x140302620
00302693  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00302698  41 8B C7                        mov eax, r15d
0030269B  48 83 C4 20                     add rsp, 0x20
0030269F  41 5F                           pop r15
003026A1  41 5E                           pop r14
003026A3  41 5D                           pop r13
003026A5  41 5C                           pop r12
003026A7  5F                              pop rdi
003026A8  5E                              pop rsi
003026A9  5D                              pop rbp
003026AA  C3                              ret
003026AB  CC                              int3
003026AC  4C 8D 25 4D D9 CF FF            lea r12, [rip - 0x3026b3]
003026B3  0F B6 6C 24 70                  movzx ebp, byte ptr [rsp + 0x70]
003026B8  4D 8B 36                        mov r14, qword ptr [r14]
003026BB  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003026C0  E9 32 FD FF FF                  jmp 0x1403023f7
003026C5  85 C9                           test ecx, ecx
003026C7  74 2E                           je 0x1403026f7
003026C9  48 8B 0B                        mov rcx, qword ptr [rbx]
003026CC  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
003026D0  0F 85 A2 FE FF FF               jne 0x140302578
003026D6  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003026DA  48 39 18                        cmp qword ptr [rax], rbx
003026DD  0F 85 95 FE FF FF               jne 0x140302578
003026E3  48 89 08                        mov qword ptr [rax], rcx
003026E6  48 89 41 08                     mov qword ptr [rcx + 8], rax
003026EA  83 63 38 FE                     and dword ptr [rbx + 0x38], 0xfffffffe
003026EE  4D 85 ED                        test r13, r13
003026F1  74 04                           je 0x1403026f7
003026F3  41 FF 4D 00                     dec dword ptr [r13]
003026F7  48 8D 73 48                     lea rsi, [rbx + 0x48]
003026FB  48 8B 0E                        mov rcx, qword ptr [rsi]
003026FE  48 3B CE                        cmp rcx, rsi
00302701  0F 84 5F 01 00 00               je 0x140302866
00302707  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0030270A  A8 02                           test al, 2
0030270C  0F 85 80 01 00 00               jne 0x140302892
00302712  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00302715  A8 01                           test al, 1
00302717  74 32                           je 0x14030274b
00302719  48 8B 11                        mov rdx, qword ptr [rcx]
0030271C  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
00302720  0F 85 52 FE FF FF               jne 0x140302578
00302726  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0030272A  48 39 08                        cmp qword ptr [rax], rcx
0030272D  0F 85 45 FE FF FF               jne 0x140302578
00302733  48 89 10                        mov qword ptr [rax], rdx
00302736  48 89 42 08                     mov qword ptr [rdx + 8], rax
0030273A  83 61 20 FE                     and dword ptr [rcx + 0x20], 0xfffffffe
0030273E  FF 4B 3C                        dec dword ptr [rbx + 0x3c]
00302741  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00302744  A8 04                           test al, 4
00302746  74 03                           je 0x14030274b
00302748  FF 4B 40                        dec dword ptr [rbx + 0x40]
0030274B  33 D2                           xor edx, edx
0030274D  E8 1E 01 88 00                  call 0x140b82870
00302752  EB A7                           jmp 0x1403026fb
00302754  FF C8                           dec eax
00302756  83 F8 0F                        cmp eax, 0xf
00302759  0F 87 65 01 00 00               ja 0x1403028c4
0030275F  48 98                           cdqe
00302761  41 8B 8C 84 9C 30 04 00         mov ecx, dword ptr [r12 + rax*4 + 0x4309c]
00302769  49 03 CC                        add rcx, r12
0030276C  FF E1                           jmp rcx
0030276E  CC                              int3
0030276F  CC                              int3
00302770  CC                              int3
00302771  CC                              int3
00302772  49 8B 6E 48                     mov rbp, qword ptr [r14 + 0x48]
00302776  4D 8D 66 48                     lea r12, [r14 + 0x48]
0030277A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00302780  49 3B EC                        cmp rbp, r12
00302783  0F 84 23 FF FF FF               je 0x1403026ac
00302789  0F B7 55 28                     movzx edx, word ptr [rbp + 0x28]
0030278D  48 8D 75 28                     lea rsi, [rbp + 0x28]
00302791  B9 00 01 00 00                  mov ecx, 0x100
00302796  44 0F 20 C0                     mov rax, cr8
0030279A  3C 02                           cmp al, 2
0030279C  0F 83 0A 03 00 00               jae 0x140302aac
003027A2  48 83 C2 40                     add rdx, 0x40
003027A6  41 B8 53 65 41 74               mov r8d, 0x74416553
003027AC  E8 3F F9 87 00                  call 0x140b820f0
003027B1  48 8B D8                        mov rbx, rax
003027B4  48 85 C0                        test rax, rax
003027B7  0F 84 C2 FD FF FF               je 0x14030257f
003027BD  33 D2                           xor edx, edx
003027BF  48 8B C8                        mov rcx, rax
003027C2  44 8D 42 40                     lea r8d, [rdx + 0x40]
003027C6  E8 75 44 3C 00                  call 0x1406c6c40
003027CB  66 44 89 7B 28                  mov word ptr [rbx + 0x28], r15w
003027D0  0F B7 06                        movzx eax, word ptr [rsi]
003027D3  66 89 43 2A                     mov word ptr [rbx + 0x2a], ax
003027D7  48 8D 43 40                     lea rax, [rbx + 0x40]
003027DB  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
003027DF  48 85 F6                        test rsi, rsi
003027E2  74 48                           je 0x14030282c
003027E4  0F B7 0E                        movzx ecx, word ptr [rsi]
003027E7  4C 8B C8                        mov r9, rax
003027EA  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003027EE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003027F3  0F B7 43 2A                     movzx eax, word ptr [rbx + 0x2a]
003027F7  66 3B C8                        cmp cx, ax
003027FA  0F 46 C1                        cmovbe eax, ecx
003027FD  49 8B C9                        mov rcx, r9
00302800  8B F0                           mov esi, eax
00302802  44 8B C0                        mov r8d, eax
00302805  66 89 73 28                     mov word ptr [rbx + 0x28], si
00302809  E8 32 40 3C 00                  call 0x1406c6840
0030280E  0F B7 4B 28                     movzx ecx, word ptr [rbx + 0x28]
00302812  0F B7 43 2A                     movzx eax, word ptr [rbx + 0x2a]
00302816  48 83 C1 02                     add rcx, 2
0030281A  48 3B C8                        cmp rcx, rax
0030281D  77 0D                           ja 0x14030282c
0030281F  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00302824  48 D1 EE                        shr rsi, 1
00302827  66 44 89 3C 70                  mov word ptr [rax + rsi*2], r15w
0030282C  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0030282F  A8 02                           test al, 2
00302831  75 2A                           jne 0x14030285d
00302833  48 8B 4F 68                     mov rcx, qword ptr [rdi + 0x68]
00302837  48 8D 47 60                     lea rax, [rdi + 0x60]
0030283B  48 8D 53 10                     lea rdx, [rbx + 0x10]
0030283F  48 39 01                        cmp qword ptr [rcx], rax
00302842  0F 85 30 FD FF FF               jne 0x140302578
00302848  48 89 02                        mov qword ptr [rdx], rax
0030284B  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0030284F  48 89 11                        mov qword ptr [rcx], rdx
00302852  48 89 50 08                     mov qword ptr [rax + 8], rdx
00302856  83 4B 20 02                     or dword ptr [rbx + 0x20], 2
0030285A  FF 47 58                        inc dword ptr [rdi + 0x58]
0030285D  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00302861  E9 1A FF FF FF                  jmp 0x140302780
00302866  4C 8B 73 60                     mov r14, qword ptr [rbx + 0x60]
0030286A  48 8D 73 60                     lea rsi, [rbx + 0x60]
0030286E  4C 3B F6                        cmp r14, rsi
00302871  0F 85 F9 01 00 00               jne 0x140302a70
00302877  41 B6 01                        mov r14b, 1
0030287A  45 84 F6                        test r14b, r14b
0030287D  0F 84 0E FD FF FF               je 0x140302591
00302883  33 D2                           xor edx, edx
00302885  48 8B CB                        mov rcx, rbx
00302888  E8 E3 FF 87 00                  call 0x140b82870
0030288D  E9 FF FC FF FF                  jmp 0x140302591
00302892  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
00302896  48 8D 41 10                     lea rax, [rcx + 0x10]
0030289A  49 39 40 08                     cmp qword ptr [r8 + 8], rax
0030289E  0F 85 D4 FC FF FF               jne 0x140302578
003028A4  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003028A8  48 39 02                        cmp qword ptr [rdx], rax
003028AB  0F 85 C7 FC FF FF               jne 0x140302578
003028B1  4C 89 02                        mov qword ptr [rdx], r8
003028B4  49 89 50 08                     mov qword ptr [r8 + 8], rdx
003028B8  83 61 20 FD                     and dword ptr [rcx + 0x20], 0xfffffffd
003028BC  FF 4B 58                        dec dword ptr [rbx + 0x58]
003028BF  E9 4E FE FF FF                  jmp 0x140302712
003028C4  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
003028CA  E9 B6 FC FF FF                  jmp 0x140302585
003028CF  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
003028D3  A8 01                           test al, 1
003028D5  0F 85 DD FD FF FF               jne 0x1403026b8
003028DB  E9 29 FB FF FF                  jmp 0x140302409
003028E0  48 89 02                        mov qword ptr [rdx], rax
003028E3  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003028E7  48 89 11                        mov qword ptr [rcx], rdx
003028EA  48 89 50 08                     mov qword ptr [rax + 8], rdx
003028EE  83 4B 20 02                     or dword ptr [rbx + 0x20], 2
003028F2  FF 47 58                        inc dword ptr [rdi + 0x58]
003028F5  48 8B 36                        mov rsi, qword ptr [rsi]
003028F8  E9 13 FC FF FF                  jmp 0x140302510
003028FD  49 8B 76 48                     mov rsi, qword ptr [r14 + 0x48]
00302901  49 8D 6E 48                     lea rbp, [r14 + 0x48]
00302905  48 3B F5                        cmp rsi, rbp
00302908  0F 84 A5 FD FF FF               je 0x1403026b3
0030290E  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00302911  E8 CA 01 00 00                  call 0x140302ae0
00302916  48 8B D8                        mov rbx, rax
00302919  48 85 C0                        test rax, rax
0030291C  0F 84 5D FC FF FF               je 0x14030257f
00302922  48 8D 48 40                     lea rcx, [rax + 0x40]
00302926  48 89 48 28                     mov qword ptr [rax + 0x28], rcx
0030292A  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
0030292D  89 43 30                        mov dword ptr [rbx + 0x30], eax
00302930  44 8B 46 30                     mov r8d, dword ptr [rsi + 0x30]
00302934  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
00302938  E8 03 3F 3C 00                  call 0x1406c6840
0030293D  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00302940  A8 02                           test al, 2
00302942  75 2A                           jne 0x14030296e
00302944  48 8B 4F 68                     mov rcx, qword ptr [rdi + 0x68]
00302948  48 8D 47 60                     lea rax, [rdi + 0x60]
0030294C  48 8D 53 10                     lea rdx, [rbx + 0x10]
00302950  48 39 01                        cmp qword ptr [rcx], rax
00302953  0F 85 1F FC FF FF               jne 0x140302578
00302959  48 89 02                        mov qword ptr [rdx], rax
0030295C  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00302960  48 89 11                        mov qword ptr [rcx], rdx
00302963  48 89 50 08                     mov qword ptr [rax + 8], rdx
00302967  83 4B 20 02                     or dword ptr [rbx + 0x20], 2
0030296B  FF 47 58                        inc dword ptr [rdi + 0x58]
0030296E  48 8B 36                        mov rsi, qword ptr [rsi]
00302971  EB 92                           jmp 0x140302905
00302973  85 C0                           test eax, eax
00302975  0F 85 A5 FC FF FF               jne 0x140302620
0030297B  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0030297F  48 8D 43 48                     lea rax, [rbx + 0x48]
00302983  48 39 01                        cmp qword ptr [rcx], rax
00302986  0F 85 EC FB FF FF               jne 0x140302578
0030298C  49 89 00                        mov qword ptr [r8], rax
0030298F  49 89 48 08                     mov qword ptr [r8 + 8], rcx
00302993  4C 89 01                        mov qword ptr [rcx], r8
00302996  4C 89 40 08                     mov qword ptr [rax + 8], r8
0030299A  41 83 48 20 01                  or dword ptr [r8 + 0x20], 1
0030299F  FF 43 3C                        inc dword ptr [rbx + 0x3c]
003029A2  E9 79 FC FF FF                  jmp 0x140302620
003029A7  4C 8B 09                        mov r9, qword ptr [rcx]
003029AA  49 39 49 08                     cmp qword ptr [r9 + 8], rcx
003029AE  0F 85 C4 FB FF FF               jne 0x140302578
003029B4  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003029B8  48 39 08                        cmp qword ptr [rax], rcx
003029BB  0F 85 B7 FB FF FF               jne 0x140302578
003029C1  4C 89 08                        mov qword ptr [rax], r9
003029C4  49 89 41 08                     mov qword ptr [r9 + 8], rax
003029C8  41 83 60 20 FD                  and dword ptr [r8 + 0x20], 0xfffffffd
003029CD  FF 4B 58                        dec dword ptr [rbx + 0x58]
003029D0  E9 6B FC FF FF                  jmp 0x140302640
003029D5  49 8B 76 48                     mov rsi, qword ptr [r14 + 0x48]
003029D9  49 8D 6E 48                     lea rbp, [r14 + 0x48]
003029DD  48 3B F5                        cmp rsi, rbp
003029E0  0F 84 CD FC FF FF               je 0x1403026b3
003029E6  0F B7 4E 30                     movzx ecx, word ptr [rsi + 0x30]
003029EA  E8 F1 00 00 00                  call 0x140302ae0
003029EF  48 8B D8                        mov rbx, rax
003029F2  48 85 C0                        test rax, rax
003029F5  0F 84 84 FB FF FF               je 0x14030257f
003029FB  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003029FF  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00302A03  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00302A07  0F B7 46 30                     movzx eax, word ptr [rsi + 0x30]
00302A0B  66 89 43 30                     mov word ptr [rbx + 0x30], ax
00302A0F  44 8B C0                        mov r8d, eax
00302A12  48 89 4B 38                     mov qword ptr [rbx + 0x38], rcx
00302A16  48 8B 56 38                     mov rdx, qword ptr [rsi + 0x38]
00302A1A  E8 21 3E 3C 00                  call 0x1406c6840
00302A1F  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00302A22  A8 02                           test al, 2
00302A24  75 2A                           jne 0x140302a50
00302A26  48 8B 4F 68                     mov rcx, qword ptr [rdi + 0x68]
00302A2A  48 8D 47 60                     lea rax, [rdi + 0x60]
00302A2E  48 8D 53 10                     lea rdx, [rbx + 0x10]
00302A32  48 39 01                        cmp qword ptr [rcx], rax
00302A35  0F 85 3D FB FF FF               jne 0x140302578
00302A3B  48 89 02                        mov qword ptr [rdx], rax
00302A3E  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00302A42  48 89 11                        mov qword ptr [rcx], rdx
00302A45  48 89 50 08                     mov qword ptr [rax + 8], rdx
00302A49  83 4B 20 02                     or dword ptr [rbx + 0x20], 2
00302A4D  FF 47 58                        inc dword ptr [rdi + 0x58]
00302A50  48 8B 36                        mov rsi, qword ptr [rsi]
00302A53  EB 88                           jmp 0x1403029dd
00302A55  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
00302A59  84 C0                           test al, al
00302A5B  0F 89 5E FA FF FF               jns 0x1403024bf
00302A61  0F BA F1 07                     btr ecx, 7
00302A65  83 C9 01                        or ecx, 1
00302A68  89 4F 34                        mov dword ptr [rdi + 0x34], ecx
00302A6B  E9 4F FA FF FF                  jmp 0x1403024bf
00302A70  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00302A74  4D 8D 5E F0                     lea r11, [r14 - 0x10]
00302A78  4D 8B 36                        mov r14, qword ptr [r14]
00302A7B  A8 01                           test al, 1
00302A7D  75 18                           jne 0x140302a97
00302A7F  45 33 C0                        xor r8d, r8d
00302A82  49 8B D3                        mov rdx, r11
00302A85  48 8B CB                        mov rcx, rbx
00302A88  E8 73 03 00 00                  call 0x140302e00
00302A8D  49 8B CB                        mov rcx, r11
00302A90  33 D2                           xor edx, edx
00302A92  E8 D9 FD 87 00                  call 0x140b82870
00302A97  4C 3B F6                        cmp r14, rsi
00302A9A  0F 84 D7 FD FF FF               je 0x140302877
00302AA0  EB CE                           jmp 0x140302a70
00302AA2  B9 40 00 00 00                  mov ecx, 0x40
00302AA7  E9 77 F9 FF FF                  jmp 0x140302423
00302AAC  B9 40 00 00 00                  mov ecx, 0x40
00302AB1  E9 EC FC FF FF                  jmp 0x1403027a2
00302AB6  B9 40 00 00 00                  mov ecx, 0x40
00302ABB  E9 6A FA FF FF                  jmp 0x14030252a
00302AC0  48 8B D3                        mov rdx, rbx
00302AC3  49 8B CD                        mov rcx, r13
00302AC6  E8 F5 AA 39 00                  call 0x14069d5c0
00302ACB  44 0F B6 F0                     movzx r14d, al
00302ACF  E9 A6 FD FF FF                  jmp 0x14030287a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepDuplicateSecurityAttributes(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (32);
    v_stack_p20 = a1 + 8;
    v_r15 = 0;
loc_003023F7:
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_00302585;
    if (a3 != 0) goto loc_003028CF;
loc_00302409:
    a2 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 32)) + (112);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00302AA2;
loc_00302423:
    result = ExAllocatePool2(256, a2, (unsigned int)(0x74416553ULL), a4);
    if (result == 0) goto loc_0030257F;
    a2 = 0;
    result = memset(result, a2, a2 + 112, a4);
    *(unsigned __int16 *)(result + 34) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 32));
    *(unsigned __int64 *)(result + 40) = result + 112;
    result = *(unsigned __int16 *)(result + 34);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 32))) <= ((unsigned __int16)(*(unsigned __int16 *)(result + 34)))) { result = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 32)); }
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)((unsigned int)((unsigned int)(result)));
    result = memcpy(result + 112, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 40), (unsigned int)((unsigned int)(result)), a4);
    a1 = (*(unsigned __int16 *)(result + 32)) + (2);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (a1 <= (*(unsigned __int16 *)(result + 34))) {
        v_rbx = ((unsigned int)((unsigned int)(result))) >> (1);
        *(unsigned __int16 *)(result + 112 + v_rbx * 2) = 0;
    }
    *(unsigned __int64 *)(result + 72 + 8) = result + 72;
    *(unsigned __int64 *)(result + 72) = result + 72;
    *(unsigned __int64 *)(result + 96 + 8) = result + 96;
    *(unsigned __int64 *)(result + 96) = result + 96;
    *(unsigned int *)(result + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)));
    if (a3 != 0) goto loc_00302A55;
loc_003024BF:
    *(unsigned __int16 *)(result + 48) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 48));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (2)) != 0) goto loc_003024FA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40))) != (a2 + 32)) goto loc_00302578;
    *(unsigned __int64 *)(result + 16) = a2 + 32;
    *(unsigned __int64 *)(result + 16 + 8) = *(unsigned __int64 *)(a2 + 40);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 40)) = result + 16;
    *(unsigned __int64 *)(a2 + 32 + 8) = result + 16;
loc_003024FA:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 48))) != 6) goto loc_00302754;
loc_00302510:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72)) == (*(unsigned __int64 *)(a1 + 8) + 72)) goto loc_003026B3;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00302AB6;
loc_0030252A:
    result = ExAllocatePool2(256, 64, (unsigned int)(0x74416553ULL), a4);
    if (result == 0) goto loc_0030257F;
    a2 = 0;
    result = memset(result, a2, a2 + 64, a4);
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 72) + 40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 32)))) & (2)) != 0) goto loc_003028F5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 104))) == (result + 96)) goto loc_003028E0;
loc_00302578:
loc_0030257F:
loc_00302585:
    v_rbp = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))));
    v_rbp = (unsigned int)((v_rbp) >> (31));
loc_00302591:
    if ((*(unsigned __int64 *)(a2 + 32)) == (a2 + 32)) goto loc_00302693;
    if ((unsigned __int8)(v_rbp) == 0) goto loc_00302AC0;
    v_r14 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) - 16 + 56)))) & (2)) == 0) goto loc_003025DA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32)) + 8)) != (*(unsigned __int64 *)(a2 + 32))) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 8))) != (*(unsigned __int64 *)(a2 + 32))) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 8);
    if (0 != 0) {
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) - 16 + 56))))) & (1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) - 16 + 56)))) & (4)) != 0) goto loc_003026C5;
    if ((unsigned int)(a1) != 0) goto loc_00302615;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16))) != (a2 + 8)) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16) = a2 + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 8) = *(unsigned __int64 *)(a2 + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16)) = *(unsigned __int64 *)(a2 + 32) - 16;
    *(unsigned __int64 *)(a2 + 8 + 8) = *(unsigned __int64 *)(a2 + 32) - 16;
loc_00302615:
loc_00302620:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96)) == (*(unsigned __int64 *)(a2 + 32) - 16 + 96)) goto loc_0030287A;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) + 16))))) & (4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) + 16)))) & (2)) != 0) goto loc_003029A7;
loc_00302640:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16 + 32))) & (1));
    if ((unsigned int)(a2) == 0) goto loc_00302973;
    if ((unsigned int)(result) == 0) goto loc_00302687;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16)) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16 + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16)) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16 + 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16 + 32)))) & (4)) != 0) {
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16, a4);
    goto loc_00302620;
loc_00302693:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_003026B3:
loc_003026B8:
    goto loc_003023F7;
loc_003026C5:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16) == 0) goto loc_003026F7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10) + 8)) != v_stack_p10) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8))) != v_stack_p10) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8)) = *(unsigned __int64 *)(v_stack_p10);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10) + 8) = *(unsigned __int64 *)(v_stack_p10 + 8);
    if (0 != 0) {
    }
loc_003026FB:
    if ((*(unsigned __int64 *)(v_stack_p10 + 72)) == (v_stack_p10 + 72)) goto loc_00302866;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 32)))) & (2)) != 0) goto loc_00302892;
loc_00302712:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 32)))) & (1)) == 0) goto loc_0030274B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72)) + 8)) != (*(unsigned __int64 *)(v_stack_p10 + 72))) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 8))) != (*(unsigned __int64 *)(v_stack_p10 + 72))) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 72) + 32)))) & (4)) != 0) {
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p10 + 72), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16, a4);
    goto loc_003026FB;
loc_00302754:
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) > 15) goto loc_003028C4;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3154925 + result * 4 + 274588))) + (v_rip - 3154925);
loc_00302866:
    if ((*(unsigned __int64 *)(v_stack_p10 + 96)) != (v_stack_p10 + 96)) goto loc_00302A70;
loc_00302877:
loc_0030287A:
    if (1 == 0) goto loc_00302591;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p10, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) - 16 + 96) - 16, a4);
    goto loc_00302591;
loc_00302892:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8)) != (v_stack_p10 + 16)) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16 + 8))) != (v_stack_p10 + 16)) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16 + 8)) = *(unsigned __int64 *)(v_stack_p10 + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8) = *(unsigned __int64 *)(v_stack_p10 + 16 + 8);
    goto loc_00302712;
loc_003028C4:
    goto loc_00302585;
loc_003028CF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 52)))) & (1)) != 0) goto loc_003026B8;
    goto loc_00302409;
loc_003028E0:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16 + 8)) = (unsigned int)(*(unsigned int *)(1 + 52));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16 + 8) + 8) = v_stack_p10;
    *(unsigned __int64 *)(v_stack_p10) = *(unsigned __int64 *)(v_stack_p10 + 16 + 8);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 52)) + 8) = *(unsigned __int64 *)(v_stack_p10 + 16 + 8);
loc_003028F5:
    goto loc_00302510;
loc_00302973:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 52))) != 0) goto loc_00302620;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80))) != (v_stack_p10 + 72)) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)) = v_stack_p10 + 72;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8) = *(unsigned __int64 *)(v_stack_p10 + 80);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)) = *(unsigned __int64 *)(v_stack_p10 + 16);
    *(unsigned __int64 *)(v_stack_p10 + 72 + 8) = *(unsigned __int64 *)(v_stack_p10 + 16);
    goto loc_00302620;
loc_003029A7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)) + 8)) != (*(unsigned __int64 *)(v_stack_p10 + 80))) goto loc_00302578;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80) + 8))) != (*(unsigned __int64 *)(v_stack_p10 + 80))) goto loc_00302578;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80) + 8);
    goto loc_00302640;
loc_00302A55:
    if (!sign_flag) goto loc_003024BF;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_p10 + 80)) | (1));
    *(unsigned int *)(a2 + 32 + 52) = (unsigned int)(a1);
    goto loc_003024BF;
loc_00302A70:
    result = (unsigned int)(*(unsigned int *)(1 + 16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 16)))) & (1)) == 0) {
        a3 = 0;
        a2 = 1 - 16;
        a1 = v_stack_p10;
        result = AuthzBasepRemoveSecurityAttributeValueFromLists(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)));
        a1 = 1 - 16;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)));
    }
    if ((*(unsigned __int64 *)(1)) == (*(unsigned __int64 *)(v_stack_p10 + 96))) goto loc_00302877;
    goto loc_00302A70;
loc_00302AA2:
    goto loc_00302423;
loc_00302AB6:
    goto loc_0030252A;
loc_00302AC0:
    result = AuthzBasepRollbackSecurityAttributeChanges(0, v_stack_p10, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)));
    goto loc_0030287A;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepDuplicateSecurityAttributes(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p60;
    uint8_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (32);
    v_stack_p20 = Arg1 + 8;
    local_r15 = 0;
loc_003023F7:
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_00302585;
    if (Arg3 != 0) goto loc_003028CF;
loc_00302409:
    Arg2 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20)) + (112);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00302AA2;
loc_00302423:
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x74416553ULL), a4);
    if (result == 0) goto loc_0030257F;
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 112, a4);
    *(uint16_t *)(result + 0x22) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20));
    *(uint64_t *)(result + 0x28) = result + 112;
    result = *(uint16_t *)(result + 0x22);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20))) <= ((uint16_t)(*(uint16_t *)(result + 0x22)))) { result = (uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20)); }
    *(uint16_t *)(result + 0x20) = (uint16_t)((uint32_t)((uint32_t)(result)));
    result = memcpy(result + 112, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28), (uint32_t)((uint32_t)(result)), a4);
    Arg1 = (*(uint16_t *)(result + 0x20)) + (2);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (Arg1 <= (*(uint16_t *)(result + 0x22))) {
        local_rbx = ((uint32_t)((uint32_t)(result))) >> (1);
        *(uint16_t *)(result + 0x70 + local_rbx * 2) = 0;
    }
    *(uint64_t *)(result + 0x48 + 0x8) = result + 72;
    *(uint64_t *)(result + 0x48) = result + 72;
    *(uint64_t *)(result + 0x60 + 0x8) = result + 96;
    *(uint64_t *)(result + 0x60) = result + 96;
    *(uint32_t *)(result + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)));
    if (Arg3 != 0) goto loc_00302A55;
loc_003024BF:
    *(uint16_t *)(result + 0x30) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (2)) != 0) goto loc_003024FA;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x28))) != (Arg2 + 32)) goto loc_00302578;
    *(void **)(result + 0x10) = Arg2 + 32;
    *(uint64_t *)(result + 0x10 + 0x8) = *(uint64_t *)(arg2 + 0x28);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x28)) = result + 16;
    *(uint64_t *)(arg2 + 0x20 + 0x8) = result + 16;
loc_003024FA:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30))) != 6) goto loc_00302754;
loc_00302510:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48)) == (*(uint64_t *)(arg1 + 0x8) + 72)) goto loc_003026B3;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00302AB6;
loc_0030252A:
    result = ExAllocatePool2(256, 64, (uint32_t)(0x74416553ULL), a4);
    if (result == 0) goto loc_0030257F;
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 64, a4);
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48) + 0x28);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) & (2)) != 0) goto loc_003028F5;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x68))) == (result + 96)) goto loc_003028E0;
loc_00302578:
loc_0030257F:
loc_00302585:
    local_rbp = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))));
    local_rbp = (uint32_t)((local_rbp) >> (31));
loc_00302591:
    if ((*(uint64_t *)(arg2 + 0x20)) == (Arg2 + 32)) goto loc_00302693;
    if ((uint8_t)(local_rbp) == 0) goto loc_00302AC0;
    local_r14 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x38)))) & (2)) == 0) goto loc_003025DA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20)) + 0x8)) != (*(uint64_t *)(arg2 + 0x20))) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x8))) != (*(uint64_t *)(arg2 + 0x20))) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x8);
    if (0 != 0) {
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x38))))) & (1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x38)))) & (4)) != 0) goto loc_003026C5;
    if ((uint32_t)(Arg1) != 0) goto loc_00302615;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x10))) != (Arg2 + 8)) goto loc_00302578;
    *(void **)(*(uint64_t *)(arg2 + 0x20) - 0x10) = Arg2 + 8;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x8) = *(uint64_t *)(arg2 + 0x10);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x10)) = *(uint64_t *)(arg2 + 0x20) - 16;
    *(uint64_t *)(arg2 + 0x8 + 0x8) = *(uint64_t *)(arg2 + 0x20) - 16;
loc_00302615:
loc_00302620:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60)) == (*(uint64_t *)(arg2 + 0x20) - 16 + 96)) goto loc_0030287A;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) + 0x10))))) & (4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) + 0x10)))) & (2)) != 0) goto loc_003029A7;
loc_00302640:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10 + 0x20))) & (1));
    if ((uint32_t)(Arg2) == 0) goto loc_00302973;
    if ((uint32_t)(result) == 0) goto loc_00302687;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16)) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10 + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16)) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10 + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10 + 0x8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 0x10 + 0x20)))) & (4)) != 0) {
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16, Arg2, *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16, a4);
    goto loc_00302620;
loc_00302693:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_003026B3:
loc_003026B8:
    goto loc_003023F7;
loc_003026C5:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16) == 0) goto loc_003026F7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10) + 0x8)) != v_stack_p10) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8))) != v_stack_p10) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8)) = *(uint64_t *)(v_stack_p10);
    *(uint64_t *)(*(uint64_t *)(v_stack_p10) + 0x8) = *(uint64_t *)(v_stack_p10 + 0x8);
    if (0 != 0) {
    }
loc_003026FB:
    if ((*(uint64_t *)(v_stack_p10 + 0x48)) == (v_stack_p10 + 72)) goto loc_00302866;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x20)))) & (2)) != 0) goto loc_00302892;
loc_00302712:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x20)))) & (1)) == 0) goto loc_0030274B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48)) + 0x8)) != (*(uint64_t *)(v_stack_p10 + 0x48))) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x8))) != (*(uint64_t *)(v_stack_p10 + 0x48))) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x48) + 0x20)))) & (4)) != 0) {
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p10 + 0x48), Arg2, *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16, a4);
    goto loc_003026FB;
loc_00302754:
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) > 15) goto loc_003028C4;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x3023ED + result * 4 + 0x4309C))) + (v_rip - 3154925);
loc_00302866:
    if ((*(uint64_t *)(v_stack_p10 + 0x60)) != (v_stack_p10 + 96)) goto loc_00302A70;
loc_00302877:
loc_0030287A:
    if (1 == 0) goto loc_00302591;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p10, Arg2, *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) - 0x10 + 0x60) - 16, a4);
    goto loc_00302591;
loc_00302892:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8)) != (v_stack_p10 + 16)) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10 + 0x8))) != (v_stack_p10 + 16)) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10 + 0x8)) = *(uint64_t *)(v_stack_p10 + 0x10);
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8) = *(uint64_t *)(v_stack_p10 + 0x10 + 0x8);
    goto loc_00302712;
loc_003028C4:
    goto loc_00302585;
loc_003028CF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x34)))) & (1)) != 0) goto loc_003026B8;
    goto loc_00302409;
loc_003028E0:
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10 + 0x8)) = (uint32_t)(*(uint32_t *)(1 + 0x34));
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10 + 0x8) + 0x8) = v_stack_p10;
    *(uint64_t *)(v_stack_p10) = *(uint64_t *)(v_stack_p10 + 0x10 + 0x8);
    *(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0x34)) + 0x8) = *(uint64_t *)(v_stack_p10 + 0x10 + 0x8);
loc_003028F5:
    goto loc_00302510;
loc_00302973:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x34))) != 0) goto loc_00302620;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50))) != (v_stack_p10 + 72)) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)) = v_stack_p10 + 72;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8) = *(uint64_t *)(v_stack_p10 + 0x50);
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)) = *(uint64_t *)(v_stack_p10 + 0x10);
    *(uint64_t *)(v_stack_p10 + 0x48 + 0x8) = *(uint64_t *)(v_stack_p10 + 0x10);
    goto loc_00302620;
loc_003029A7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)) + 0x8)) != (*(uint64_t *)(v_stack_p10 + 0x50))) goto loc_00302578;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50) + 0x8))) != (*(uint64_t *)(v_stack_p10 + 0x50))) goto loc_00302578;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50) + 0x8);
    goto loc_00302640;
loc_00302A55:
    if (!sign_flag) goto loc_003024BF;
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_p10 + 0x50)) | (1));
    *(uint32_t *)(arg2 + 0x20 + 0x34) = (uint32_t)(Arg1);
    goto loc_003024BF;
loc_00302A70:
    result = (uint32_t)(*(uint32_t *)(1 + 0x10));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x10)))) & (1)) == 0) {
        Arg3 = 0;
        Arg2 = 1 - 16;
        Arg1 = v_stack_p10;
        result = AuthzBasepRemoveSecurityAttributeValueFromLists(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)));
        Arg1 = 1 - 16;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)));
    }
    if ((*(uint64_t *)(1)) == (*(uint64_t *)(v_stack_p10 + 0x60))) goto loc_00302877;
    goto loc_00302A70;
loc_00302AA2:
    goto loc_00302423;
loc_00302AB6:
    goto loc_0030252A;
loc_00302AC0:
    result = AuthzBasepRollbackSecurityAttributeChanges(0, v_stack_p10, Arg3, *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)));
    goto loc_0030287A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x18` | `32` | `R/W` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003023C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
