# sub_006ECA3A

- RVA: `0x006ECA3A`–`0x006ECEEA` (길이 `1,200` bytes)
- VA: `0x00000001406ECA3A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BAF0`
- 디코드: `288`개 명령, `1,200/1,200` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x006ECAE3` → [AdtpBuildPrivilegeAuditString](../../page/A6/AdtpBuildPrivilegeAuditString_function_00A62AE8.md) (function, `0x00A62AE8`)
- `0x006ECB0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006ECBE4` → [StringCchPrintfExW](../69/StringCchPrintfExW_function_0069DE98.md) (function, `0x0069DE98`)
- `0x006ECC1F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006ECC83` → [RtlAppendUnicodeStringToString](../40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x006ECCEE` → [RtlAppendUnicodeStringToString](../40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x006ECCFB` → [RtlAppendUnicodeToString](../40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x006ECD0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006ECD1C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006ECD37` → [RtlAppendUnicodeStringToString](../40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x006ECD45` → [RtlAppendUnicodeStringToString](../40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x006ECD59` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006ECDF1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006ECE18` → [RtlAppendUnicodeToString](../40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x006ECE28` → [RtlIntegerToUnicodeString](../../page/91/RtlIntegerToUnicodeString_function_0091D3E0.md) (function, `0x0091D3E0`)
- `0x006ECE40` → [RtlAppendUnicodeStringToString](../40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x006ECE51` → [RtlAppendUnicodeToString](../40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x006ECE7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006ECEA7` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006ECEBE` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006ECB48` → RVA `0x000419C8` (`.rdata`; read)
- `0x006ECB4F` → RVA `0x0001A748` (`.rdata`; read)
- `0x006ECB56` → RVA `0x000419C0` (`.rdata`; read)
- `0x006ECE04` → RVA `0x000134F8` (`.rdata`; read)
- `0x006ECE45` → RVA `0x0001BEC8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x006ECAE3` → [AdtpBuildPrivilegeAuditString](../../page/A6/AdtpBuildPrivilegeAuditString_function_00A62AE8.md) (`.text` → `PAGE`)
  - `0x006ECB0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x006ECC1F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x006ECD0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006ECD1C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006ECD59` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006ECDF1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x006ECE28` → [RtlIntegerToUnicodeString](../../page/91/RtlIntegerToUnicodeString_function_0091D3E0.md) (`.text` → `PAGE`)
  - `0x006ECE7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x006ECA3D` → [AdtpBuildAccessReasonAuditStringInternal + 0xB5](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECA48` → [AdtpBuildAccessReasonAuditStringInternal + 0x2D2](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECA54` → [AdtpBuildAccessReasonAuditStringInternal + 0x2D2](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECA60` → [AdtpBuildAccessReasonAuditStringInternal + 0x2D2](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECAEC` → [AdtpBuildAccessReasonAuditStringInternal + 0x1F9](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECB18` → [AdtpBuildAccessReasonAuditStringInternal + 0x557](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECC2C` → [AdtpBuildAccessReasonAuditStringInternal + 0x557](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECC70` → [AdtpBuildAccessReasonAuditStringInternal + 0x1F9](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECCA0` → [AdtpBuildAccessReasonAuditStringInternal + 0x51A](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECDFE` → [AdtpBuildAccessReasonAuditStringInternal + 0x557](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECE31` → [AdtpBuildAccessReasonAuditStringInternal + 0x1F9](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)
  - `0x006ECEE5` → [AdtpBuildAccessReasonAuditStringInternal + 0x472](../40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ECA3A  44 8B F0                        mov r14d, eax
006ECA3D  E9 B7 29 D2 FF                  jmp 0x14040f3f9
006ECA42  81 FF 00 00 01 00               cmp edi, 0x10000
006ECA48  0F 84 C8 2B D2 FF               je 0x14040f616
006ECA4E  81 FF 00 00 02 00               cmp edi, 0x20000
006ECA54  0F 84 BC 2B D2 FF               je 0x14040f616
006ECA5A  81 FF 00 00 03 00               cmp edi, 0x30000
006ECA60  0F 84 B0 2B D2 FF               je 0x14040f616
006ECA66  41 BE 00 00 06 00               mov r14d, 0x60000
006ECA6C  81 FF 00 00 05 00               cmp edi, 0x50000
006ECA72  0F 84 D0 00 00 00               je 0x1406ecb48
006ECA78  41 3B FE                        cmp edi, r14d
006ECA7B  0F 84 C7 00 00 00               je 0x1406ecb48
006ECA81  81 FF 00 00 07 00               cmp edi, 0x70000
006ECA87  0F 84 B1 00 00 00               je 0x1406ecb3e
006ECA8D  81 FF 00 00 10 00               cmp edi, 0x100000
006ECA93  0F 85 AC 03 00 00               jne 0x1406ece45
006ECA99  41 BE 00 00 20 00               mov r14d, 0x200000
006ECA9F  B8 01 00 00 00                  mov eax, 1
006ECAA4  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
006ECAA8  89 45 40                        mov dword ptr [rbp + 0x40], eax
006ECAAB  48 8D 4D 40                     lea rcx, [rbp + 0x40]
006ECAAF  89 45 44                        mov dword ptr [rbp + 0x44], eax
006ECAB2  45 33 C9                        xor r9d, r9d
006ECAB5  0F B7 C2                        movzx eax, dx
006ECAB8  45 33 C0                        xor r8d, r8d
006ECABB  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
006ECABF  48 8D 55 A0                     lea rdx, [rbp - 0x60]
006ECAC3  48 C1 E8 20                     shr rax, 0x20
006ECAC7  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
006ECACB  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
006ECAD0  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
006ECAD4  48 8D 44 24 50                  lea rax, [rsp + 0x50]
006ECAD9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006ECADE  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
006ECAE3  E8 00 60 37 00                  call 0x140a62ae8
006ECAE8  8B D8                           mov ebx, eax
006ECAEA  85 C0                           test eax, eax
006ECAEC  0F 88 4B 2A D2 FF               js 0x14040f53d
006ECAF2  0F B7 5D A0                     movzx ebx, word ptr [rbp - 0x60]
006ECAF6  B9 00 01 00 00                  mov ecx, 0x100
006ECAFB  D1 EB                           shr ebx, 1
006ECAFD  41 B8 53 65 41 6B               mov r8d, 0x6b416553
006ECB03  83 C3 1B                        add ebx, 0x1b
006ECB06  8B D3                           mov edx, ebx
006ECB08  48 03 D2                        add rdx, rdx
006ECB0B  E8 E0 55 49 00                  call 0x140b820f0
006ECB10  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006ECB15  48 85 C0                        test rax, rax
006ECB18  0F 84 7D 2D D2 FF               je 0x14040f89b
006ECB1E  66 03 DB                        add bx, bx
006ECB21  66 44 89 64 24 58               mov word ptr [rsp + 0x58], r12w
006ECB27  66 89 5C 24 5A                  mov word ptr [rsp + 0x5a], bx
006ECB2C  41 3B FE                        cmp edi, r14d
006ECB2F  0F 85 F1 01 00 00               jne 0x1406ecd26
006ECB35  48 8D 55 90                     lea rdx, [rbp - 0x70]
006ECB39  E9 F4 01 00 00                  jmp 0x1406ecd32
006ECB3E  BB 26 07 00 00                  mov ebx, 0x726
006ECB43  E9 99 02 00 00                  jmp 0x1406ecde1
006ECB48  0F B7 05 79 4E 95 FF            movzx eax, word ptr [rip - 0x6ab187]
006ECB4F  48 8D 0D F2 DB 92 FF            lea rcx, [rip - 0x6d240e]
006ECB56  F2 0F 10 05 62 4E 95 FF         movsd xmm0, qword ptr [rip - 0x6ab19e]
006ECB5E  41 B9 02 00 00 00               mov r9d, 2
006ECB64  66 89 45 38                     mov word ptr [rbp + 0x38], ax
006ECB68  41 0F B7 D9                     movzx ebx, r9w
006ECB6C  33 C0                           xor eax, eax
006ECB6E  F2 0F 11 45 30                  movsd qword ptr [rbp + 0x30], xmm0
006ECB73  66 89 5C 24 70                  mov word ptr [rsp + 0x70], bx
006ECB78  66 44 89 4C 24 72               mov word ptr [rsp + 0x72], r9w
006ECB7E  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
006ECB82  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
006ECB87  0F B7 D2                        movzx edx, dx
006ECB8A  41 3B FE                        cmp edi, r14d
006ECB8D  0F 84 BB 00 00 00               je 0x1406ecc4e
006ECB93  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
006ECB97  85 C0                           test eax, eax
006ECB99  74 1F                           je 0x1406ecbba
006ECB9B  3B D0                           cmp edx, eax
006ECB9D  0F 83 C8 00 00 00               jae 0x1406ecc6b
006ECBA3  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
006ECBA7  48 8B CA                        mov rcx, rdx
006ECBAA  48 03 C9                        add rcx, rcx
006ECBAD  0F 10 04 C8                     movups xmm0, xmmword ptr [rax + rcx*8]
006ECBB1  66 0F 7E C3                     movd ebx, xmm0
006ECBB5  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
006ECBBA  66 41 3B D9                     cmp bx, r9w
006ECBBE  77 4C                           ja 0x1406ecc0c
006ECBC0  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
006ECBC4  48 8D 45 30                     lea rax, [rbp + 0x30]
006ECBC8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006ECBCD  4C 8D 4D 80                     lea r9, [rbp - 0x80]
006ECBD1  45 33 C0                        xor r8d, r8d
006ECBD4  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
006ECBD9  48 8B D6                        mov rdx, rsi
006ECBDC  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
006ECBE0  48 8D 4D 60                     lea rcx, [rbp + 0x60]
006ECBE4  E8 AF 12 FB FF                  call 0x14069de98
006ECBE9  85 C0                           test eax, eax
006ECBEB  78 1F                           js 0x1406ecc0c
006ECBED  66 2B 75 80                     sub si, word ptr [rbp - 0x80]
006ECBF1  B8 28 00 00 00                  mov eax, 0x28
006ECBF6  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
006ECBFB  48 8D 45 60                     lea rax, [rbp + 0x60]
006ECBFF  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
006ECC04  8D 1C 36                        lea ebx, [rsi + rsi]
006ECC07  66 89 5C 24 70                  mov word ptr [rsp + 0x70], bx
006ECC0C  0F B7 DB                        movzx ebx, bx
006ECC0F  B9 00 01 00 00                  mov ecx, 0x100
006ECC14  83 C3 36                        add ebx, 0x36
006ECC17  41 B8 53 65 41 6B               mov r8d, 0x6b416553
006ECC1D  8B D3                           mov edx, ebx
006ECC1F  E8 CC 54 49 00                  call 0x140b820f0
006ECC24  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006ECC29  48 85 C0                        test rax, rax
006ECC2C  0F 84 69 2C D2 FF               je 0x14040f89b
006ECC32  66 03 DB                        add bx, bx
006ECC35  66 44 89 64 24 58               mov word ptr [rsp + 0x58], r12w
006ECC3B  66 89 5C 24 5A                  mov word ptr [rsp + 0x5a], bx
006ECC40  81 FF 00 00 05 00               cmp edi, 0x50000
006ECC46  75 2D                           jne 0x1406ecc75
006ECC48  48 8D 55 B0                     lea rdx, [rbp - 0x50]
006ECC4C  EB 30                           jmp 0x1406ecc7e
006ECC4E  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
006ECC52  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
006ECC56  85 C0                           test eax, eax
006ECC58  0F 84 5C FF FF FF               je 0x1406ecbba
006ECC5E  3B D0                           cmp edx, eax
006ECC60  73 09                           jae 0x1406ecc6b
006ECC62  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
006ECC66  E9 3C FF FF FF                  jmp 0x1406ecba7
006ECC6B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
006ECC70  E9 C8 28 D2 FF                  jmp 0x14040f53d
006ECC75  41 3B FE                        cmp edi, r14d
006ECC78  75 0E                           jne 0x1406ecc88
006ECC7A  48 8D 55 C0                     lea rdx, [rbp - 0x40]
006ECC7E  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECC83  E8 C8 2D D2 FF                  call 0x14040fa50
006ECC88  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
006ECC8D  E9 A9 01 00 00                  jmp 0x1406ece3b
006ECC92  49 FF C6                        inc r14
006ECC95  66 42 39 04 71                  cmp word ptr [rcx + r14*2], ax
006ECC9A  75 F6                           jne 0x1406ecc92
006ECC9C  41 8D 4E 01                     lea ecx, [r14 + 1]
006ECCA0  E9 B9 2B D2 FF                  jmp 0x14040f85e
006ECCA5  66 03 DB                        add bx, bx
006ECCA8  66 44 89 74 24 58               mov word ptr [rsp + 0x58], r14w
006ECCAE  66 89 5C 24 5A                  mov word ptr [rsp + 0x5a], bx
006ECCB3  81 FF 00 00 01 00               cmp edi, 0x10000
006ECCB9  75 06                           jne 0x1406eccc1
006ECCBB  48 8D 55 90                     lea rdx, [rbp - 0x70]
006ECCBF  EB 28                           jmp 0x1406ecce9
006ECCC1  81 FF 00 00 02 00               cmp edi, 0x20000
006ECCC7  75 06                           jne 0x1406ecccf
006ECCC9  48 8D 55 D0                     lea rdx, [rbp - 0x30]
006ECCCD  EB 1A                           jmp 0x1406ecce9
006ECCCF  81 FF 00 00 03 00               cmp edi, 0x30000
006ECCD5  75 06                           jne 0x1406eccdd
006ECCD7  48 8D 55 E0                     lea rdx, [rbp - 0x20]
006ECCDB  EB 0C                           jmp 0x1406ecce9
006ECCDD  81 FF 00 00 04 00               cmp edi, 0x40000
006ECCE3  75 0E                           jne 0x1406eccf3
006ECCE5  48 8D 55 F0                     lea rdx, [rbp - 0x10]
006ECCE9  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECCEE  E8 5D 2D D2 FF                  call 0x14040fa50
006ECCF3  49 8B D7                        mov rdx, r15
006ECCF6  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECCFB  E8 90 2C D2 FF                  call 0x14040f990
006ECD00  4D 85 E4                        test r12, r12
006ECD03  74 12                           je 0x1406ecd17
006ECD05  33 D2                           xor edx, edx
006ECD07  49 8B CC                        mov rcx, r12
006ECD0A  E8 61 5B 49 00                  call 0x140b82870
006ECD0F  45 33 E4                        xor r12d, r12d
006ECD12  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
006ECD17  33 D2                           xor edx, edx
006ECD19  48 8B CE                        mov rcx, rsi
006ECD1C  E8 4F 5B 49 00                  call 0x140b82870
006ECD21  E9 1F 01 00 00                  jmp 0x1406ece45
006ECD26  81 FF 00 00 10 00               cmp edi, 0x100000
006ECD2C  75 0E                           jne 0x1406ecd3c
006ECD2E  48 8D 55 00                     lea rdx, [rbp]
006ECD32  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECD37  E8 14 2D D2 FF                  call 0x14040fa50
006ECD3C  48 8D 55 A0                     lea rdx, [rbp - 0x60]
006ECD40  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECD45  E8 06 2D D2 FF                  call 0x14040fa50
006ECD4A  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
006ECD4E  48 85 C9                        test rcx, rcx
006ECD51  0F 84 EE 00 00 00               je 0x1406ece45
006ECD57  33 D2                           xor edx, edx
006ECD59  E8 12 5B 49 00                  call 0x140b82870
006ECD5E  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
006ECD62  E9 DE 00 00 00                  jmp 0x1406ece45
006ECD67  81 FF 00 00 30 00               cmp edi, 0x300000
006ECD6D  74 6D                           je 0x1406ecddc
006ECD6F  81 FF 00 00 40 00               cmp edi, 0x400000
006ECD75  74 5E                           je 0x1406ecdd5
006ECD77  81 FF 00 00 50 00               cmp edi, 0x500000
006ECD7D  74 4F                           je 0x1406ecdce
006ECD7F  81 FF 00 00 60 00               cmp edi, 0x600000
006ECD85  74 40                           je 0x1406ecdc7
006ECD87  81 FF 00 00 70 00               cmp edi, 0x700000
006ECD8D  74 31                           je 0x1406ecdc0
006ECD8F  81 FF 00 00 80 00               cmp edi, 0x800000
006ECD95  74 22                           je 0x1406ecdb9
006ECD97  81 FF 00 00 90 00               cmp edi, 0x900000
006ECD9D  74 13                           je 0x1406ecdb2
006ECD9F  81 FF 00 00 A0 00               cmp edi, 0xa00000
006ECDA5  0F 85 9A 00 00 00               jne 0x1406ece45
006ECDAB  BB 40 07 00 00                  mov ebx, 0x740
006ECDB0  EB 2F                           jmp 0x1406ecde1
006ECDB2  BB 31 07 00 00                  mov ebx, 0x731
006ECDB7  EB 28                           jmp 0x1406ecde1
006ECDB9  BB 0D 07 00 00                  mov ebx, 0x70d
006ECDBE  EB 21                           jmp 0x1406ecde1
006ECDC0  BB 10 07 00 00                  mov ebx, 0x710
006ECDC5  EB 1A                           jmp 0x1406ecde1
006ECDC7  BB 0F 07 00 00                  mov ebx, 0x70f
006ECDCC  EB 13                           jmp 0x1406ecde1
006ECDCE  BB 0E 07 00 00                  mov ebx, 0x70e
006ECDD3  EB 0C                           jmp 0x1406ecde1
006ECDD5  BB 0C 07 00 00                  mov ebx, 0x70c
006ECDDA  EB 05                           jmp 0x1406ecde1
006ECDDC  BB 0B 07 00 00                  mov ebx, 0x70b
006ECDE1  BA 4E 00 00 00                  mov edx, 0x4e
006ECDE6  B9 00 01 00 00                  mov ecx, 0x100
006ECDEB  41 B8 53 65 41 6B               mov r8d, 0x6b416553
006ECDF1  E8 FA 52 49 00                  call 0x140b820f0
006ECDF6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006ECDFB  48 85 C0                        test rax, rax
006ECDFE  0F 84 97 2A D2 FF               je 0x14040f89b
006ECE04  48 8D 15 ED 66 92 FF            lea rdx, [rip - 0x6d9913]
006ECE0B  C7 44 24 58 00 00 4E 00         mov dword ptr [rsp + 0x58], 0x4e0000
006ECE13  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECE18  E8 73 2B D2 FF                  call 0x14040f990
006ECE1D  4C 8D 45 40                     lea r8, [rbp + 0x40]
006ECE21  BA 0A 00 00 00                  mov edx, 0xa
006ECE26  8B CB                           mov ecx, ebx
006ECE28  E8 B3 05 23 00                  call 0x14091d3e0
006ECE2D  8B D8                           mov ebx, eax
006ECE2F  85 C0                           test eax, eax
006ECE31  0F 88 06 27 D2 FF               js 0x14040f53d
006ECE37  48 8D 55 40                     lea rdx, [rbp + 0x40]
006ECE3B  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECE40  E8 0B 2C D2 FF                  call 0x14040fa50
006ECE45  48 8D 15 7C F0 92 FF            lea rdx, [rip - 0x6d0f84]
006ECE4C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
006ECE51  E8 3A 2B D2 FF                  call 0x14040f990
006ECE56  44 0F B7 74 24 58               movzx r14d, word ptr [rsp + 0x58]
006ECE5C  B9 00 01 00 00                  mov ecx, 0x100
006ECE61  45 8B FE                        mov r15d, r14d
006ECE64  41 B8 53 65 41 6B               mov r8d, 0x6b416553
006ECE6A  41 D1 EF                        shr r15d, 1
006ECE6D  8B D8                           mov ebx, eax
006ECE6F  44 03 7D 88                     add r15d, dword ptr [rbp - 0x78]
006ECE73  41 8D 77 01                     lea esi, [r15 + 1]
006ECE77  8B D6                           mov edx, esi
006ECE79  48 03 D2                        add rdx, rdx
006ECE7C  E8 6F 52 49 00                  call 0x140b820f0
006ECE81  48 8B F8                        mov rdi, rax
006ECE84  48 85 C0                        test rax, rax
006ECE87  75 07                           jne 0x1406ece90
006ECE89  BB 17 00 00 C0                  mov ebx, 0xc0000017
006ECE8E  EB 4D                           jmp 0x1406ecedd
006ECE90  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
006ECE94  C6 00 01                        mov byte ptr [rax], 1
006ECE97  66 45 85 ED                     test r13w, r13w
006ECE9B  74 0F                           je 0x1406eceac
006ECE9D  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
006ECEA1  4D 8B C5                        mov r8, r13
006ECEA4  48 8B CF                        mov rcx, rdi
006ECEA7  E8 94 99 FD FF                  call 0x1406c6840
006ECEAC  66 45 85 F6                     test r14w, r14w
006ECEB0  74 11                           je 0x1406ecec3
006ECEB2  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
006ECEB7  4A 8D 0C 2F                     lea rcx, [rdi + r13]
006ECEBB  4D 8B C6                        mov r8, r14
006ECEBE  E8 7D 99 FD FF                  call 0x1406c6840
006ECEC3  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006ECEC7  66 03 F6                        add si, si
006ECECA  66 46 89 24 7F                  mov word ptr [rdi + r15*2], r12w
006ECECF  8D 46 FE                        lea eax, [rsi - 2]
006ECED2  66 89 71 02                     mov word ptr [rcx + 2], si
006ECED6  66 89 01                        mov word ptr [rcx], ax
006ECED9  48 89 79 08                     mov qword ptr [rcx + 8], rdi
006ECEDD  49 8B F4                        mov rsi, r12
006ECEE0  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
006ECEE5  E9 CC 28 D2 FF                  jmp 0x14040f7b6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006ECA3A(__int64 a1, unsigned __int16 a2, int a3, int a4)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p50;
    unsigned __int16 v_stack_p58;
    unsigned __int16 v_stack_p5A;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int16 v_stack_p72;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006ECA3A(int64_t Arg1, uint16_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p50;
    uint16_t v_stack_p58;
    uint16_t v_stack_p5A;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint16_t v_stack_p72;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ECA3A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
