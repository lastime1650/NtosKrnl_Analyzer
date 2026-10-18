# PiDevCfgFindDeviceMigrationNode

- RVA: `0x00732920`–`0x0073334B` (길이 `2,603` bytes)
- VA: `0x0000000140732920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8B0C`
- 디코드: `651`개 명령, `2,603/2,603` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00732A12` → [NtQueryKey](../86/NtQueryKey_function_008676E0.md) (function, `0x008676E0`)
- `0x00732A48` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00732A71` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00732AA8` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (function, `0x006AD330`)
- `0x00732ACC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00732AE9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00732B16` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (function, `0x004D109C`)
- `0x00732B38` → [CmIsRootEnumeratedDevice](../8F/CmIsRootEnumeratedDevice_function_008F6E08.md) (function, `0x008F6E08`)
- `0x00732B4C` → [PiDevCfgQueryDeviceMigrationNode](../9B/PiDevCfgQueryDeviceMigrationNode_function_009BD328.md) (function, `0x009BD328`)
- `0x00732B6B` → [PiDevCfgClearDeviceMigrationNode](../96/PiDevCfgClearDeviceMigrationNode_function_00965780.md) (function, `0x00965780`)
- `0x00732BCD` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00732C1F` → [PiDevCfgGetMigrationDeviceIdScore](../../text/4A/PiDevCfgGetMigrationDeviceIdScore_function_004A6888.md) (function, `0x004A6888`)
- `0x00732CB2` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x00732D20` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00732D67` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00732D86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00732DB9` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00732DFA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00732E63` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00732E82` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00732EE0` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00732F4E` → [PiDevCfgGetDriverPackageId](../97/PiDevCfgGetDriverPackageId_function_00977690.md) (function, `0x00977690`)
- `0x00732F61` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00732FA3` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00732FC3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0073301F` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00733148` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0073323E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00733269` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00733277` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (function, `0x004D109C`)
- `0x0073328F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007332EC` → [PiDevCfgFreeDeviceMigrationNode](../9B/PiDevCfgFreeDeviceMigrationNode_function_009BCD54.md) (function, `0x009BCD54`)
- `0x007332FE` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00733307` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00733310` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00733319` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073332A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgMigrateDevice](../96/PiDevCfgMigrateDevice_function_00963E60.md) at `0x00964222`
- [sub_00B2819A](../B2/Unknown_function_00B2819A.md) at `0x00B2821E`

### Static image references
- `0x0073293F` → RVA `0x00E0A740` (`.data`; read)
- `0x00732C06` → RVA `0x00B4AF90` (`PAGE`; read)
- `0x00732D2A` → RVA `0x0001BD98` (`.rdata`; read)
- `0x00732E04` → RVA `0x000142D8` (`.rdata`; read)
- `0x00732E23` → RVA `0x00027C80` (`.rdata`; read)
- `0x00732F6A` → RVA `0x00022D18` (`.rdata`; read)
- `0x00733185` → RVA `0x00E66245` (`.data`; read)
- `0x007331F2` → RVA `0x00AFF3B0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00732A48` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00732AA8` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (`PAGE` → `.text`)
  - `0x00732ACC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00732AE9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00732B16` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (`PAGE` → `.text`)
  - `0x00732BCD` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00732C1F` → [PiDevCfgGetMigrationDeviceIdScore](../../text/4A/PiDevCfgGetMigrationDeviceIdScore_function_004A6888.md) (`PAGE` → `.text`)
  - `0x00732CB2` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x00732D20` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00732D86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00732DFA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00732E82` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00732F61` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00732FC3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00733148` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0073323E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x00733277` → [PnpValidateRegistryDword](../../text/4D/PnpValidateRegistryDword_function_004D109C.md) (`PAGE` → `.text`)
  - `0x0073328F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0073332A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00732920  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00732925  55                              push rbp
00732926  56                              push rsi
00732927  57                              push rdi
00732928  41 54                           push r12
0073292A  41 55                           push r13
0073292C  41 56                           push r14
0073292E  41 57                           push r15
00732930  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
00732938  48 81 EC 90 01 00 00            sub rsp, 0x190
0073293F  48 8B 05 FA 7D 6D 00            mov rax, qword ptr [rip + 0x6d7dfa]
00732946  48 33 C4                        xor rax, rsp
00732949  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00732950  48 8B 85 F0 00 00 00            mov rax, qword ptr [rbp + 0xf0]
00732957  45 33 FF                        xor r15d, r15d
0073295A  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0073295E  0F 57 C0                        xorps xmm0, xmm0
00732961  33 C0                           xor eax, eax
00732963  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00732968  89 45 DC                        mov dword ptr [rbp - 0x24], eax
0073296B  4D 8B D0                        mov r10, r8
0073296E  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00732975  45 8B F1                        mov r14d, r9d
00732978  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0073297D  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
00732981  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00732986  45 8D 4F 28                     lea r9d, [r15 + 0x28]
0073298A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0073298F  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
00732993  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00732998  4C 8D 45 60                     lea r8, [rbp + 0x60]
0073299C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007329A1  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
007329A5  4C 8B E2                        mov r12, rdx
007329A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007329AD  4C 8B E9                        mov r13, rcx
007329B0  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
007329B5  41 8D 57 04                     lea edx, [r15 + 4]
007329B9  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
007329BE  49 8B CA                        mov rcx, r10
007329C1  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
007329C6  41 8B F7                        mov esi, r15d
007329C9  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
007329CE  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
007329D2  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
007329D6  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
007329DA  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
007329DE  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
007329E2  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
007329E6  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
007329EA  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
007329EE  4C 89 7D C8                     mov qword ptr [rbp - 0x38], r15
007329F2  66 44 89 7C 24 70               mov word ptr [rsp + 0x70], r15w
007329F8  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
007329FC  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
00732A00  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
00732A04  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00732A08  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
00732A0D  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
00732A12  E8 C9 4C 13 00                  call 0x1408676e0
00732A17  8B F8                           mov edi, eax
00732A19  85 C0                           test eax, eax
00732A1B  0F 88 9A 08 00 00               js 0x1407332bb
00732A21  44 39 7D 74                     cmp dword ptr [rbp + 0x74], r15d
00732A25  0F 84 8B 08 00 00               je 0x1407332b6
00732A2B  8B 4D 78                        mov ecx, dword ptr [rbp + 0x78]
00732A2E  41 B8 50 70 64 63               mov r8d, 0x63647050
00732A34  8B 45 7C                        mov eax, dword ptr [rbp + 0x7c]
00732A37  83 C1 0D                        add ecx, 0xd
00732A3A  8D 1C 48                        lea ebx, [rax + rcx*2]
00732A3D  B9 00 01 00 00                  mov ecx, 0x100
00732A42  8B D3                           mov edx, ebx
00732A44  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00732A48  E8 A3 F6 44 00                  call 0x140b820f0
00732A4D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00732A52  48 8B F8                        mov rdi, rax
00732A55  48 85 C0                        test rax, rax
00732A58  75 0A                           jne 0x140732a64
00732A5A  BF 9A 00 00 C0                  mov edi, 0xc000009a
00732A5F  E9 57 08 00 00                  jmp 0x1407332bb
00732A64  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
00732A68  48 85 C9                        test rcx, rcx
00732A6B  74 18                           je 0x140732a85
00732A6D  48 8D 55 50                     lea rdx, [rbp + 0x50]
00732A71  E8 7A F4 1B 00                  call 0x1408f1ef0
00732A76  8B F8                           mov edi, eax
00732A78  85 C0                           test eax, eax
00732A7A  0F 88 3B 08 00 00               js 0x1407332bb
00732A80  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00732A85  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00732A89  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00732A8E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00732A93  4C 8B CF                        mov r9, rdi
00732A96  41 B8 01 00 00 00               mov r8d, 1
00732A9C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00732AA0  41 8B D7                        mov edx, r15d
00732AA3  44 89 7C 24 6C                  mov dword ptr [rsp + 0x6c], r15d
00732AA8  E8 83 A8 F7 FF                  call 0x1406ad330
00732AAD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00732AB1  8B F8                           mov edi, eax
00732AB3  3D 1A 00 00 80                  cmp eax, 0x8000001a
00732AB8  0F 84 EC 06 00 00               je 0x1407331aa
00732ABE  3D 05 00 00 80                  cmp eax, 0x80000005
00732AC3  75 3F                           jne 0x140732b04
00732AC5  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00732ACA  33 D2                           xor edx, edx
00732ACC  E8 9F FD 44 00                  call 0x140b82870
00732AD1  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
00732AD5  B9 00 01 00 00                  mov ecx, 0x100
00732ADA  83 C3 02                        add ebx, 2
00732ADD  41 B8 50 70 64 63               mov r8d, 0x63647050
00732AE3  8B D3                           mov edx, ebx
00732AE5  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00732AE9  E8 02 F6 44 00                  call 0x140b820f0
00732AEE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00732AF3  48 8B F8                        mov rdi, rax
00732AF6  48 85 C0                        test rax, rax
00732AF9  0F 84 31 06 00 00               je 0x140733130
00732AFF  41 FF CF                        dec r15d
00732B02  EB 7A                           jmp 0x140732b7e
00732B04  33 D2                           xor edx, edx
00732B06  85 C0                           test eax, eax
00732B08  0F 88 2B 06 00 00               js 0x140733139
00732B0E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00732B13  48 8B CF                        mov rcx, rdi
00732B16  E8 81 E5 D9 FF                  call 0x1404d109c
00732B1B  84 C0                           test al, al
00732B1D  74 07                           je 0x140732b26
00732B1F  8B 47 08                        mov eax, dword ptr [rdi + 8]
00732B22  44 8B 34 38                     mov r14d, dword ptr [rax + rdi]
00732B26  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00732B29  48 8D 5F 14                     lea rbx, [rdi + 0x14]
00732B2D  48 D1 E8                        shr rax, 1
00732B30  48 8B CB                        mov rcx, rbx
00732B33  66 89 54 47 14                  mov word ptr [rdi + rax*2 + 0x14], dx
00732B38  E8 CB 42 1C 00                  call 0x1408f6e08
00732B3D  84 C0                           test al, al
00732B3F  75 34                           jne 0x140732b75
00732B41  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00732B46  48 8B D3                        mov rdx, rbx
00732B49  49 8B CD                        mov rcx, r13
00732B4C  E8 D7 A7 28 00                  call 0x1409bd328
00732B51  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00732B55  8B F8                           mov edi, eax
00732B57  3D 34 00 00 C0                  cmp eax, 0xc0000034
00732B5C  75 28                           jne 0x140732b86
00732B5E  33 C0                           xor eax, eax
00732B60  48 8B D3                        mov rdx, rbx
00732B63  49 8B CD                        mov rcx, r13
00732B66  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00732B6B  E8 10 2C 23 00                  call 0x140965780
00732B70  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00732B75  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
00732B7A  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
00732B7E  41 FF C7                        inc r15d
00732B81  E9 FF FE FF FF                  jmp 0x140732a85
00732B86  45 33 ED                        xor r13d, r13d
00732B89  85 C0                           test eax, eax
00732B8B  0F 88 AB 05 00 00               js 0x14073313c
00732B91  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00732B96  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00732B9B  44 89 B3 B4 00 00 00            mov dword ptr [rbx + 0xb4], r14d
00732BA2  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00732BA7  48 39 08                        cmp qword ptr [rax], rcx
00732BAA  0F 85 43 07 00 00               jne 0x1407332f3
00732BB0  48 89 43 08                     mov qword ptr [rbx + 8], rax
00732BB4  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00732BB9  48 89 0B                        mov qword ptr [rbx], rcx
00732BBC  48 89 18                        mov qword ptr [rax], rbx
00732BBF  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00732BC4  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00732BC9  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00732BCD  E8 AE D4 DC FF                  call 0x140500080
00732BD2  F7 D8                           neg eax
00732BD4  B8 00 00 00 10                  mov eax, 0x10000000
00732BD9  45 1B F6                        sbb r14d, r14d
00732BDC  41 F7 D6                        not r14d
00732BDF  44 23 F0                        and r14d, eax
00732BE2  85 83 B4 00 00 00               test dword ptr [rbx + 0xb4], eax
00732BE8  0F 95 C1                        setne cl
00732BEB  41 0F BA E6 1C                  bt r14d, 0x1c
00732BF0  0F 93 C0                        setae al
00732BF3  84 C8                           test al, cl
00732BF5  74 04                           je 0x140732bfb
00732BF7  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732BFB  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
00732BFF  48 8D 7B 38                     lea rdi, [rbx + 0x38]
00732C03  4C 2B EB                        sub r13, rbx
00732C06  4C 8D 3D 83 83 41 00            lea r15, [rip + 0x418383]
00732C0D  BB 02 00 00 00                  mov ebx, 2
00732C12  4C 8D 64 24 68                  lea r12, [rsp + 0x68]
00732C17  4A 8B 54 2F F8                  mov rdx, qword ptr [rdi + r13 - 8]
00732C1C  48 8B 0F                        mov rcx, qword ptr [rdi]
00732C1F  E8 64 3C D7 FF                  call 0x1404a6888
00732C24  B9 FF FF 00 00                  mov ecx, 0xffff
00732C29  66 41 89 04 24                  mov word ptr [r12], ax
00732C2E  66 3B C1                        cmp ax, cx
00732C31  74 03                           je 0x140732c36
00732C33  45 0B 37                        or r14d, dword ptr [r15]
00732C36  48 83 C7 10                     add rdi, 0x10
00732C3A  49 83 C4 02                     add r12, 2
00732C3E  49 83 C7 04                     add r15, 4
00732C42  48 83 EB 01                     sub rbx, 1
00732C46  75 CF                           jne 0x140732c17
00732C48  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00732C4D  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
00732C53  0F BA E0 10                     bt eax, 0x10
00732C57  73 1A                           jae 0x140732c73
00732C59  41 0F BA E6 10                  bt r14d, 0x10
00732C5E  73 26                           jae 0x140732c86
00732C60  41 F7 C6 00 10 01 00            test r14d, 0x11000
00732C67  0F 94 C1                        sete cl
00732C6A  0F BA E0 0C                     bt eax, 0xc
00732C6E  0F 92 C0                        setb al
00732C71  EB 0F                           jmp 0x140732c82
00732C73  0F BA E0 0C                     bt eax, 0xc
00732C77  0F 92 C1                        setb cl
00732C7A  41 0F BA E6 0C                  bt r14d, 0xc
00732C7F  0F 93 C0                        setae al
00732C82  84 C8                           test al, cl
00732C84  74 04                           je 0x140732c8a
00732C86  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732C8A  48 8B BB 90 00 00 00            mov rdi, qword ptr [rbx + 0x90]
00732C91  45 33 ED                        xor r13d, r13d
00732C94  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00732C98  48 85 FF                        test rdi, rdi
00732C9B  74 43                           je 0x140732ce0
00732C9D  4D 39 6C 24 50                  cmp qword ptr [r12 + 0x50], r13
00732CA2  74 3C                           je 0x140732ce0
00732CA4  66 44 39 2F                     cmp word ptr [rdi], r13w
00732CA8  74 36                           je 0x140732ce0
00732CAA  49 8B 4C 24 50                  mov rcx, qword ptr [r12 + 0x50]
00732CAF  48 8B D7                        mov rdx, rdi
00732CB2  E8 89 FA D8 FF                  call 0x1404c2740
00732CB7  48 85 C0                        test rax, rax
00732CBA  75 18                           jne 0x140732cd4
00732CBC  48 83 C8 FF                     or rax, 0xffffffffffffffff
00732CC0  48 FF C0                        inc rax
00732CC3  66 44 39 2C 47                  cmp word ptr [rdi + rax*2], r13w
00732CC8  75 F6                           jne 0x140732cc0
00732CCA  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00732CCE  48 83 C7 02                     add rdi, 2
00732CD2  EB D0                           jmp 0x140732ca4
00732CD4  41 0F BA EE 09                  bts r14d, 9
00732CD9  48 89 BB 98 00 00 00            mov qword ptr [rbx + 0x98], rdi
00732CE0  F7 83 B4 00 00 00 00 02 00 00   test dword ptr [rbx + 0xb4], 0x200
00732CEA  0F 95 C1                        setne cl
00732CED  41 0F BA E6 09                  bt r14d, 9
00732CF2  0F 93 C0                        setae al
00732CF5  84 C8                           test al, cl
00732CF7  74 04                           je 0x140732cfd
00732CF9  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732CFD  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
00732D02  4C 39 AB 80 00 00 00            cmp qword ptr [rbx + 0x80], r13
00732D09  0F 84 B8 00 00 00               je 0x140732dc7
00732D0F  41 0F BA E7 08                  bt r15d, 8
00732D14  72 7F                           jb 0x140732d95
00732D16  33 D2                           xor edx, edx
00732D18  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00732D1C  44 8D 42 50                     lea r8d, [rdx + 0x50]
00732D20  E8 1B 3F F9 FF                  call 0x1406c6c40
00732D25  4D 8B 4C 24 10                  mov r9, qword ptr [r12 + 0x10]
00732D2A  48 8D 05 67 90 8E FF            lea rax, [rip - 0x716f99]
00732D31  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00732D36  41 B8 01 00 00 00               mov r8d, 1
00732D3C  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00732D40  48 8D 45 90                     lea rax, [rbp - 0x70]
00732D44  48 89 45 00                     mov qword ptr [rbp], rax
00732D48  48 8D 45 F0                     lea rax, [rbp - 0x10]
00732D4C  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00732D54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00732D59  C7 45 F8 12 00 00 00            mov dword ptr [rbp - 8], 0x12
00732D60  C7 45 0C 06 00 00 00            mov dword ptr [rbp + 0xc], 6
00732D67  E8 00 4A 24 00                  call 0x14097776c
00732D6C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00732D70  8B F8                           mov edi, eax
00732D72  85 C0                           test eax, eax
00732D74  0F 88 C2 03 00 00               js 0x14073313c
00732D7A  44 39 6D 10                     cmp dword ptr [rbp + 0x10], r13d
00732D7E  7D 0B                           jge 0x140732d8b
00732D80  33 D2                           xor edx, edx
00732D82  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00732D86  E8 F5 79 CF FF                  call 0x14042a780
00732D8B  41 0F BA EF 08                  bts r15d, 8
00732D90  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00732D95  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
00732D99  4D 85 C0                        test r8, r8
00732D9C  74 29                           je 0x140732dc7
00732D9E  44 0F B7 4D 90                  movzx r9d, word ptr [rbp - 0x70]
00732DA3  0F B7 53 78                     movzx edx, word ptr [rbx + 0x78]
00732DA7  48 8B 8B 80 00 00 00            mov rcx, qword ptr [rbx + 0x80]
00732DAE  49 D1 E9                        shr r9, 1
00732DB1  48 D1 EA                        shr rdx, 1
00732DB4  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00732DB9  E8 22 FA 23 00                  call 0x1409727e0
00732DBE  85 C0                           test eax, eax
00732DC0  75 05                           jne 0x140732dc7
00732DC2  41 0F BA EE 08                  bts r14d, 8
00732DC7  41 F7 C6 00 03 00 00            test r14d, 0x300
00732DCE  0F 94 C1                        sete cl
00732DD1  F7 83 B4 00 00 00 00 01 00 00   test dword ptr [rbx + 0xb4], 0x100
00732DDB  0F 95 C0                        setne al
00732DDE  84 C8                           test al, cl
00732DE0  74 04                           je 0x140732de6
00732DE2  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732DE6  41 F6 C7 30                     test r15b, 0x30
00732DEA  0F 85 A0 00 00 00               jne 0x140732e90
00732DF0  33 D2                           xor edx, edx
00732DF2  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00732DF6  44 8D 42 50                     lea r8d, [rdx + 0x50]
00732DFA  E8 41 3E F9 FF                  call 0x1406c6c40
00732DFF  4D 8B 4C 24 10                  mov r9, qword ptr [r12 + 0x10]
00732E04  48 8D 05 CD 14 8E FF            lea rax, [rip - 0x71eb33]
00732E0B  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00732E10  41 B8 01 00 00 00               mov r8d, 1
00732E16  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00732E1A  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00732E1F  48 89 45 00                     mov qword ptr [rbp], rax
00732E23  48 8D 05 56 4E 8F FF            lea rax, [rip - 0x70b1aa]
00732E2A  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00732E2E  48 8D 45 80                     lea rax, [rbp - 0x80]
00732E32  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00732E36  48 8D 45 F0                     lea rax, [rbp - 0x10]
00732E3A  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00732E42  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00732E47  C7 45 F8 07 00 00 00            mov dword ptr [rbp - 8], 7
00732E4E  C7 45 08 04 00 00 00            mov dword ptr [rbp + 8], 4
00732E55  C7 45 20 12 00 00 00            mov dword ptr [rbp + 0x20], 0x12
00732E5C  C7 45 34 06 00 00 00            mov dword ptr [rbp + 0x34], 6
00732E63  E8 04 49 24 00                  call 0x14097776c
00732E68  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00732E6C  8B F8                           mov edi, eax
00732E6E  85 C0                           test eax, eax
00732E70  0F 88 C6 02 00 00               js 0x14073313c
00732E76  44 39 6D 38                     cmp dword ptr [rbp + 0x38], r13d
00732E7A  7D 0B                           jge 0x140732e87
00732E7C  33 D2                           xor edx, edx
00732E7E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00732E82  E8 F9 78 CF FF                  call 0x14042a780
00732E87  41 83 CF 30                     or r15d, 0x30
00732E8B  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00732E90  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00732E94  33 43 60                        xor eax, dword ptr [rbx + 0x60]
00732E97  A8 10                           test al, 0x10
00732E99  75 06                           jne 0x140732ea1
00732E9B  41 83 CE 10                     or r14d, 0x10
00732E9F  EB 15                           jmp 0x140732eb6
00732EA1  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
00732EA7  A8 10                           test al, 0x10
00732EA9  75 07                           jne 0x140732eb2
00732EAB  F6 44 24 64 10                  test byte ptr [rsp + 0x64], 0x10
00732EB0  74 04                           je 0x140732eb6
00732EB2  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732EB6  4C 39 6B 70                     cmp qword ptr [rbx + 0x70], r13
00732EBA  74 2D                           je 0x140732ee9
00732EBC  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00732EC0  48 85 C0                        test rax, rax
00732EC3  74 28                           je 0x140732eed
00732EC5  44 0F B7 4D 80                  movzx r9d, word ptr [rbp - 0x80]
00732ECA  4C 8B C0                        mov r8, rax
00732ECD  0F B7 53 68                     movzx edx, word ptr [rbx + 0x68]
00732ED1  48 8B 4B 70                     mov rcx, qword ptr [rbx + 0x70]
00732ED5  49 D1 E9                        shr r9, 1
00732ED8  48 D1 EA                        shr rdx, 1
00732EDB  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00732EE0  E8 FB F8 23 00                  call 0x1409727e0
00732EE5  85 C0                           test eax, eax
00732EE7  74 0F                           je 0x140732ef8
00732EE9  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00732EED  4C 39 6B 70                     cmp qword ptr [rbx + 0x70], r13
00732EF1  75 09                           jne 0x140732efc
00732EF3  48 85 C0                        test rax, rax
00732EF6  75 04                           jne 0x140732efc
00732EF8  41 83 CE 20                     or r14d, 0x20
00732EFC  F6 83 B4 00 00 00 20            test byte ptr [rbx + 0xb4], 0x20
00732F03  0F 95 C1                        setne cl
00732F06  41 F6 C6 20                     test r14b, 0x20
00732F0A  0F 94 C0                        sete al
00732F0D  84 C8                           test al, cl
00732F0F  74 04                           je 0x140732f15
00732F11  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00732F15  4C 39 AB A8 00 00 00            cmp qword ptr [rbx + 0xa8], r13
00732F1C  0F 84 0A 01 00 00               je 0x14073302c
00732F22  41 F6 C7 02                     test r15b, 2
00732F26  0F 85 C8 00 00 00               jne 0x140732ff4
00732F2C  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
00732F30  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
00732F34  48 85 C0                        test rax, rax
00732F37  0F 84 AE 00 00 00               je 0x140732feb
00732F3D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00732F41  48 85 C9                        test rcx, rcx
00732F44  0F 84 A1 00 00 00               je 0x140732feb
00732F4A  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00732F4E  E8 3D 47 24 00                  call 0x140977690
00732F53  85 C0                           test eax, eax
00732F55  78 71                           js 0x140732fc8
00732F57  33 D2                           xor edx, edx
00732F59  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00732F5D  44 8D 42 50                     lea r8d, [rdx + 0x50]
00732F61  E8 DA 3C F9 FF                  call 0x1406c6c40
00732F66  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
00732F6A  48 8D 05 A7 FD 8E FF            lea rax, [rip - 0x710259]
00732F71  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00732F75  45 33 C9                        xor r9d, r9d
00732F78  48 8D 45 A0                     lea rax, [rbp - 0x60]
00732F7C  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00732F84  48 89 45 00                     mov qword ptr [rbp], rax
00732F88  48 8D 45 F0                     lea rax, [rbp - 0x10]
00732F8C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00732F91  45 8D 41 08                     lea r8d, [r9 + 8]
00732F95  C7 45 F8 12 00 00 00            mov dword ptr [rbp - 8], 0x12
00732F9C  C7 45 0C 06 00 00 00            mov dword ptr [rbp + 0xc], 6
00732FA3  E8 C4 47 24 00                  call 0x14097776c
00732FA8  8B F8                           mov edi, eax
00732FAA  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00732FAE  33 C0                           xor eax, eax
00732FB0  85 FF                           test edi, edi
00732FB2  0F 88 81 01 00 00               js 0x140733139
00732FB8  39 45 10                        cmp dword ptr [rbp + 0x10], eax
00732FBB  7D 0D                           jge 0x140732fca
00732FBD  33 D2                           xor edx, edx
00732FBF  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00732FC3  E8 B8 77 CF FF                  call 0x14042a780
00732FC8  33 C0                           xor eax, eax
00732FCA  48 39 45 A8                     cmp qword ptr [rbp - 0x58], rax
00732FCE  48 8D 45 A0                     lea rax, [rbp - 0x60]
00732FD2  75 04                           jne 0x140732fd8
00732FD4  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
00732FD8  0F 10 08                        movups xmm1, xmmword ptr [rax]
00732FDB  F3 0F 7E 40 08                  movq xmm0, qword ptr [rax + 8]
00732FE0  66 0F 7E 4C 24 70               movd dword ptr [rsp + 0x70], xmm1
00732FE6  66 0F D6 45 D0                  movq qword ptr [rbp - 0x30], xmm0
00732FEB  41 83 CF 02                     or r15d, 2
00732FEF  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00732FF4  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00732FF8  48 85 C0                        test rax, rax
00732FFB  74 2F                           je 0x14073302c
00732FFD  0F B7 93 A0 00 00 00            movzx edx, word ptr [rbx + 0xa0]
00733004  4C 8B C0                        mov r8, rax
00733007  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
0073300D  48 8B 8B A8 00 00 00            mov rcx, qword ptr [rbx + 0xa8]
00733014  49 D1 E9                        shr r9, 1
00733017  48 D1 EA                        shr rdx, 1
0073301A  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0073301F  E8 BC F7 23 00                  call 0x1409727e0
00733024  85 C0                           test eax, eax
00733026  75 04                           jne 0x14073302c
00733028  41 83 CE 02                     or r14d, 2
0073302C  F6 83 B4 00 00 00 02            test byte ptr [rbx + 0xb4], 2
00733033  0F 95 C1                        setne cl
00733036  41 F6 C6 02                     test r14b, 2
0073303A  0F 94 C0                        sete al
0073303D  84 C8                           test al, cl
0073303F  74 04                           je 0x140733045
00733041  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00733045  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
00733049  48 2B 45 50                     sub rax, qword ptr [rbp + 0x50]
0073304D  75 08                           jne 0x140733057
0073304F  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
00733053  48 2B 45 58                     sub rax, qword ptr [rbp + 0x58]
00733057  48 85 C0                        test rax, rax
0073305A  75 06                           jne 0x140733062
0073305C  41 83 CE 01                     or r14d, 1
00733060  EB 0E                           jmp 0x140733070
00733062  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
00733068  A8 01                           test al, 1
0073306A  74 04                           je 0x140733070
0073306C  83 4B 10 01                     or dword ptr [rbx + 0x10], 1
00733070  0F B7 4C 24 68                  movzx ecx, word ptr [rsp + 0x68]
00733075  0F B7 44 24 6A                  movzx eax, word ptr [rsp + 0x6a]
0073307A  48 C1 E1 10                     shl rcx, 0x10
0073307E  48 0B C8                        or rcx, rax
00733081  48 C1 E1 10                     shl rcx, 0x10
00733085  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
0073308C  41 0F BA E6 1C                  bt r14d, 0x1c
00733091  72 14                           jb 0x1407330a7
00733093  48 B8 00 00 00 00 00 00 00 F0   movabs rax, 0xf000000000000000
0073309D  48 0B C8                        or rcx, rax
007330A0  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
007330A7  41 0F BA E6 09                  bt r14d, 9
007330AC  72 0E                           jb 0x1407330bc
007330AE  48 81 C9 00 F0 00 00            or rcx, 0xf000
007330B5  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
007330BC  B8 00 01 00 00                  mov eax, 0x100
007330C1  44 85 F0                        test eax, r14d
007330C4  75 0A                           jne 0x1407330d0
007330C6  48 0B C8                        or rcx, rax
007330C9  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
007330D0  41 F6 C6 20                     test r14b, 0x20
007330D4  75 0B                           jne 0x1407330e1
007330D6  48 83 C9 20                     or rcx, 0x20
007330DA  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
007330E1  41 F6 C6 10                     test r14b, 0x10
007330E5  75 0B                           jne 0x1407330f2
007330E7  48 83 C9 10                     or rcx, 0x10
007330EB  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
007330F2  41 F6 C6 02                     test r14b, 2
007330F6  75 0B                           jne 0x140733103
007330F8  48 83 C9 02                     or rcx, 2
007330FC  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
00733103  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00733108  41 F6 C6 01                     test r14b, 1
0073310C  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
00733111  44 8B 7C 24 6C                  mov r15d, dword ptr [rsp + 0x6c]
00733116  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
0073311A  0F 85 5A FA FF FF               jne 0x140732b7a
00733120  48 83 C9 01                     or rcx, 1
00733124  48 89 8B B8 00 00 00            mov qword ptr [rbx + 0xb8], rcx
0073312B  E9 4A FA FF FF                  jmp 0x140732b7a
00733130  BF 9A 00 00 C0                  mov edi, 0xc000009a
00733135  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00733139  45 33 ED                        xor r13d, r13d
0073313C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00733141  48 85 C9                        test rcx, rcx
00733144  74 07                           je 0x14073314d
00733146  33 D2                           xor edx, edx
00733148  E8 23 F7 44 00                  call 0x140b82870
0073314D  85 FF                           test edi, edi
0073314F  0F 88 66 01 00 00               js 0x1407332bb
00733155  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0073315A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0073315F  48 3B C1                        cmp rax, rcx
00733162  0F 84 4E 01 00 00               je 0x1407332b6
00733168  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0073316F  48 83 F9 FF                     cmp rcx, -1
00733173  74 45                           je 0x1407331ba
00733175  48 85 F6                        test rsi, rsi
00733178  74 3D                           je 0x1407331b7
0073317A  48 39 8E B8 00 00 00            cmp qword ptr [rsi + 0xb8], rcx
00733181  77 34                           ja 0x1407331b7
00733183  75 35                           jne 0x1407331ba
00733185  44 38 2D B9 30 73 00            cmp byte ptr [rip + 0x7330b9], r13b
0073318C  74 12                           je 0x1407331a0
0073318E  44 39 A8 B0 00 00 00            cmp dword ptr [rax + 0xb0], r13d
00733195  74 09                           je 0x1407331a0
00733197  44 39 AE B0 00 00 00            cmp dword ptr [rsi + 0xb0], r13d
0073319E  74 17                           je 0x1407331b7
007331A0  83 4E 10 02                     or dword ptr [rsi + 0x10], 2
007331A4  83 48 10 02                     or dword ptr [rax + 0x10], 2
007331A8  EB 10                           jmp 0x1407331ba
007331AA  45 33 ED                        xor r13d, r13d
007331AD  41 8B FD                        mov edi, r13d
007331B0  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
007331B5  EB 85                           jmp 0x14073313c
007331B7  48 8B F0                        mov rsi, rax
007331BA  48 8B 00                        mov rax, qword ptr [rax]
007331BD  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007331C2  48 3B C1                        cmp rax, rcx
007331C5  75 A1                           jne 0x140733168
007331C7  48 85 F6                        test rsi, rsi
007331CA  0F 84 E6 00 00 00               je 0x1407332b6
007331D0  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
007331D3  A8 02                           test al, 2
007331D5  74 7F                           je 0x140733256
007331D7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
007331DC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007331E1  C7 44 24 74 01 00 00 00         mov dword ptr [rsp + 0x74], 1
007331E9  48 3B D8                        cmp rbx, rax
007331EC  0F 84 A2 00 00 00               je 0x140733294
007331F2  4C 8D 35 B7 C1 3C 00            lea r14, [rip + 0x3cc1b7]
007331F9  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
007331FC  A8 02                           test al, 2
007331FE  74 43                           je 0x140733243
00733200  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
00733207  48 39 83 B8 00 00 00            cmp qword ptr [rbx + 0xb8], rax
0073320E  75 33                           jne 0x140733243
00733210  C7 45 D8 12 00 14 00            mov dword ptr [rbp - 0x28], 0x140012
00733217  48 8D 44 24 74                  lea rax, [rsp + 0x74]
0073321C  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
00733220  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00733224  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00733228  41 B9 04 00 00 00               mov r9d, 4
0073322E  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00733236  45 33 C0                        xor r8d, r8d
00733239  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0073323E  E8 8D AA F7 FF                  call 0x1406adcd0
00733243  48 8B 1B                        mov rbx, qword ptr [rbx]
00733246  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0073324B  48 3B D8                        cmp rbx, rax
0073324E  75 A9                           jne 0x1407331f9
00733250  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00733254  EB 3E                           jmp 0x140733294
00733256  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0073325A  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
0073325F  45 33 C0                        xor r8d, r8d
00733262  48 8D 15 47 C1 3C 00            lea rdx, [rip + 0x3cc147]
00733269  E8 7E 5E 26 00                  call 0x1409990ec
0073326E  85 C0                           test eax, eax
00733270  78 22                           js 0x140733294
00733272  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00733277  E8 20 DE D9 FF                  call 0x1404d109c
0073327C  84 C0                           test al, al
0073327E  74 0D                           je 0x14073328d
00733280  8B 41 08                        mov eax, dword ptr [rcx + 8]
00733283  44 39 2C 08                     cmp dword ptr [rax + rcx], r13d
00733287  74 04                           je 0x14073328d
00733289  83 4E 10 02                     or dword ptr [rsi + 0x10], 2
0073328D  33 D2                           xor edx, edx
0073328F  E8 DC F5 44 00                  call 0x140b82870
00733294  48 8B 0E                        mov rcx, qword ptr [rsi]
00733297  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
0073329B  75 56                           jne 0x1407332f3
0073329D  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007332A1  48 39 30                        cmp qword ptr [rax], rsi
007332A4  75 4D                           jne 0x1407332f3
007332A6  48 89 08                        mov qword ptr [rax], rcx
007332A9  48 89 41 08                     mov qword ptr [rcx + 8], rax
007332AD  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
007332B1  48 89 30                        mov qword ptr [rax], rsi
007332B4  EB 05                           jmp 0x1407332bb
007332B6  BF 25 02 00 C0                  mov edi, 0xc0000225
007332BB  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007332C0  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007332C5  48 3B C8                        cmp rcx, rax
007332C8  74 30                           je 0x1407332fa
007332CA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007332CF  48 39 41 08                     cmp qword ptr [rcx + 8], rax
007332D3  75 1E                           jne 0x1407332f3
007332D5  48 8B 01                        mov rax, qword ptr [rcx]
007332D8  48 39 48 08                     cmp qword ptr [rax + 8], rcx
007332DC  75 15                           jne 0x1407332f3
007332DE  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007332E3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007332E8  48 89 50 08                     mov qword ptr [rax + 8], rdx
007332EC  E8 63 9A 28 00                  call 0x1409bcd54
007332F1  EB C8                           jmp 0x1407332bb
007332F3  B9 03 00 00 00                  mov ecx, 3
007332F8  CD 29                           int 0x29
007332FA  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007332FE  E8 FD D4 28 00                  call 0x1409c0800
00733303  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00733307  E8 F4 D4 28 00                  call 0x1409c0800
0073330C  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00733310  E8 EB D4 28 00                  call 0x1409c0800
00733315  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00733319  E8 E2 D4 28 00                  call 0x1409c0800
0073331E  8B C7                           mov eax, edi
00733320  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00733327  48 33 CC                        xor rcx, rsp
0073332A  E8 11 93 F7 FF                  call 0x1406ac640
0073332F  48 8B 9C 24 E8 01 00 00         mov rbx, qword ptr [rsp + 0x1e8]
00733337  48 81 C4 90 01 00 00            add rsp, 0x190
0073333E  41 5F                           pop r15
00733340  41 5E                           pop r14
00733342  41 5D                           pop r13
00733344  41 5C                           pop r12
00733346  5F                              pop rdi
00733347  5E                              pop rsi
00733348  5D                              pop rbp
00733349  C3                              ret
0073334A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgFindDeviceMigrationNode(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int16 v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned __int16 v_stack_m15E;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 7175674)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r15 = 0;
    v_stack_m80 = a5;
    result = 0;
    v_stack_m180 = a4;
    v_stack_mEC = 0;
    v_stack_m48 = 0;
    v_stack_m88 = a3;
    v_stack_m170 = v_stack_m178;
    v_stack_m118 = a2;
    v_stack_m178 = v_stack_m178;
    v_stack_m110 = a1;
    v_stack_m1A8 = v_stack_m168;
    v_stack_m150 = 0;
    v_stack_m194 = 0;
    v_stack_m160 = 0;
    v_stack_m164 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m130 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_m158 = 0;
    v_stack_mF8 = 0;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m154 = 0;
    v_stack_m168 = 0;
    result = NtQueryKey(a3, v_r15 + 4, v_stack_m68, v_r15 + 40);
    if (sign_flag) goto loc_007332BB;
    if (v_stack_m54 == 0) goto loc_007332B6;
    a1 = (unsigned int)(((unsigned int)(v_stack_m50)) + (13));
    v_stack_m190 = (unsigned int)((unsigned int)(v_stack_m4C) + a1 * 2);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C) + a1 * 2)), (unsigned int)(0x63647050ULL), v_r15 + 40);
    v_stack_m188 = result;
    if (result != 0) goto loc_00732A64;
    goto loc_007332BB;
loc_00732A64:
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_00732A85;
    result = RtlGUIDFromString(*(unsigned __int64 *)(a1 + 40), v_stack_m78, (unsigned int)(0x63647050ULL), v_r15 + 40);
    if (sign_flag) goto loc_007332BB;
loc_00732A85:
    v_stack_m1A0 = v_stack_m168;
    v_stack_m1A8 = (unsigned int)((unsigned int)(v_stack_m4C) + a1 * 2);
    v_stack_m15C = 0;
    result = ZwEnumerateValueKey(v_stack_m88, 0, 1, v_stack_m188);
    v_stack_m198 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_007331AA;
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_00732B04;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m188, a2, 1, v_stack_m188);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m168)) + (2));
    v_stack_m190 = (unsigned int)(v_rbx);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x63647050ULL), v_stack_m188);
    v_stack_m188 = result;
    if (result == 0) goto loc_00733130;
    v_r15 = (unsigned int)((v_r15) - 1);
    goto loc_00732B7E;
loc_00732B04:
    a2 = 0;
    if (sign_flag) goto loc_00733139;
    result = PnpValidateRegistryDword(v_stack_m188, a2, (unsigned int)(0x63647050ULL), v_stack_m188);
    v_r14 = (unsigned int)(a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(v_stack_m188 + 8);
        v_r14 = *(unsigned int *)(result + v_stack_m188 * 1);
    }
    result = ((unsigned int)(*(unsigned int *)(v_stack_m188 + 16))) >> (1);
    *(unsigned __int16 *)(v_stack_m188 + result * 2 + 20) = 0;
    result = CmIsRootEnumeratedDevice(v_stack_m188 + 20, a2, (unsigned int)(0x63647050ULL), v_stack_m188);
    if ((unsigned __int8)(result) != 0) goto loc_00732B75;
    result = PiDevCfgQueryDeviceMigrationNode(a1, v_stack_m188 + 20, v_stack_m150, v_stack_m188);
    v_stack_m198 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00732B86;
    result = 0;
    v_stack_m150 = 0;
    result = PiDevCfgClearDeviceMigrationNode(a1, v_stack_m188 + 20, v_stack_m150, v_stack_m188);
loc_00732B75:
loc_00732B7A:
loc_00732B7E:
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_00732A85;
loc_00732B86:
    v_r13 = 0;
    if (sign_flag) goto loc_0073313C;
    *(unsigned int *)(v_stack_m150 + 180) = (unsigned int)((unsigned int)(v_stack_m180));
    if ((*(unsigned __int64 *)(v_stack_m170)) != v_stack_m178) goto loc_007332F3;
    *(unsigned __int64 *)(v_stack_m150 + 8) = v_stack_m170;
    *(unsigned __int64 *)(v_stack_m150) = v_stack_m178;
    *(unsigned __int64 *)(v_stack_m170) = v_stack_m150;
    v_stack_m170 = v_stack_m150;
    result = wcsicmp(*(unsigned __int64 *)(v_stack_m150 + 32), *(unsigned __int64 *)(a2 + 8), v_stack_m150, v_stack_m188);
    result = (unsigned int)(-(result));
    v_r14 = (unsigned int)(~((unsigned int)(v_stack_m180)));
    v_r14 = (unsigned int)((v_r14) & ((unsigned int)((unsigned int)(0x10000000ULL))));
    a1 = (((*(unsigned int *)(v_stack_m150 + 180)) & ((unsigned int)((unsigned int)(0x10000000ULL)))) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    v_r13 = (v_stack_m118) - (v_stack_m150);
loc_00732C17:
    result = PiDevCfgGetMigrationDeviceIdScore(*(unsigned __int64 *)(v_stack_m150 + 56), *(unsigned __int64 *)(v_stack_m150 + 56 + v_r13 * 1 - 8), v_stack_m150, v_stack_m188);
    *(unsigned __int16 *)(v_stack_m160) = (unsigned __int16)(result);
    if (((unsigned __int16)(result)) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        v_r14 = (unsigned int)((v_r14) | (*(unsigned int *)(v_rip + 4293507)));
    }
    v_rdi = (v_stack_m150 + 56) + (16);
    v_r12 = (v_stack_m160) + (2);
    v_r15 = (v_rip + 4293507) + (4);
    v_rbx = (2) - (1);
    if (condition_is_not_equal) goto loc_00732C17;
    if (condition_is_above_or_equal) goto loc_00732C73;
    if (condition_is_above_or_equal) goto loc_00732C86;
    a1 = ((((unsigned int)(v_r14)) & (0x11000ULL)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    goto loc_00732C82;
loc_00732C73:
    a1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
loc_00732C82:
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    v_r13 = 0;
    if (*(unsigned __int64 *)(v_stack_m150 + 144) == 0) goto loc_00732CE0;
    if ((*(unsigned __int64 *)(v_stack_m118 + 80)) == 0) goto loc_00732CE0;
loc_00732CA4:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m150 + 144))) == 0) goto loc_00732CE0;
    result = PnpMultiSzContainsString(*(unsigned __int64 *)(v_stack_m118 + 80), *(unsigned __int64 *)(v_stack_m150 + 144), v_stack_m150, v_stack_m188);
    if (result != 0) goto loc_00732CD4;
    result = (result) | (-1);
loc_00732CC0:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m150 + 144) + result * 2)) != 0) goto loc_00732CC0;
    v_rdi = (*(unsigned __int64 *)(v_stack_m150 + 144) + result * 2) + (2);
    goto loc_00732CA4;
loc_00732CD4:
    *(unsigned __int64 *)(v_stack_m150 + 152) = v_rdi;
loc_00732CE0:
    a1 = (((*(unsigned int *)(v_stack_m150 + 180)) & (512)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    if ((*(unsigned __int64 *)(v_stack_m150 + 128)) == 0) goto loc_00732DC7;
    if ((*(unsigned __int64 *)(v_stack_m150 + 128)) < 0) goto loc_00732D95;
    a2 = 0;
    result = memset(v_stack_mD8, a2, a2 + 80, v_stack_m188);
    v_stack_mD8 = v_rip - 7434137;
    v_stack_mC8 = v_stack_m138;
    v_stack_m1A0 = 1;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 18;
    v_stack_mBC = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, *(unsigned __int64 *)(v_stack_m118 + 8), 1, *(unsigned __int64 *)(v_stack_m118 + 16));
    v_stack_m198 = (unsigned int)(result);
    if (sign_flag) goto loc_0073313C;
    if (v_stack_mB8 < 0) {
        a2 = 0;
        a1 = v_stack_m138;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(v_stack_m118 + 16));
    }
    v_stack_m194 = (unsigned int)((unsigned int)(v_stack_m194));
loc_00732D95:
    if (v_stack_m130 == 0) goto loc_00732DC7;
    a4 = (v_stack_m138) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_m150 + 120)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_m150 + 128), a2, v_stack_m130, a4);
    if ((unsigned int)(result) == 0) {
    }
    a1 = ((((unsigned int)(v_r14)) & (768)) == 0) ? 1 : 0;
    result = (((*(unsigned int *)(v_stack_m150 + 180)) & (256)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_m194))) & (48)) != 0) goto loc_00732E90;
    a2 = 0;
    result = memset(v_stack_mD8, a2, a2 + 80, a4);
    v_stack_mD8 = v_rip - 7465779;
    v_stack_mC8 = v_stack_m164;
    v_stack_mB0 = v_rip - 7385514;
    v_stack_mA0 = v_stack_m148;
    v_stack_m1A0 = 2;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 7;
    v_stack_mC0 = 4;
    v_stack_mA8 = 18;
    v_stack_m94 = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, *(unsigned __int64 *)(v_stack_m118 + 8), 1, *(unsigned __int64 *)(v_stack_m118 + 16));
    v_stack_m198 = (unsigned int)(result);
    if (sign_flag) goto loc_0073313C;
    if (v_stack_m90 < 0) {
        a2 = 0;
        a1 = v_stack_m148;
        result = RtlInitUnicodeString(a1, a2, 1, *(unsigned __int64 *)(v_stack_m118 + 16));
    }
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m194)) | (48));
    v_stack_m194 = (unsigned int)(v_r15);
loc_00732E90:
    result = (unsigned int)(((unsigned int)(v_stack_m164)) ^ (*(unsigned int *)(v_stack_m150 + 96)));
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00732EA1;
    v_r14 = (unsigned int)((v_r14) | (16));
    goto loc_00732EB6;
loc_00732EA1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m150 + 180)))) & (16)) != 0) goto loc_00732EB2;
    if (((v_stack_m164) & (16)) != 0) {
    }
    if ((*(unsigned __int64 *)(v_stack_m150 + 112)) == 0) goto loc_00732EE9;
    if (v_stack_m140 == 0) goto loc_00732EED;
    a4 = (v_stack_m148) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_m150 + 104)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_m150 + 112), a2, v_stack_m140, a4);
    if ((unsigned int)(result) == 0) goto loc_00732EF8;
loc_00732EE9:
loc_00732EED:
    if ((*(unsigned __int64 *)(v_stack_m150 + 112)) != 0) goto loc_00732EFC;
    if (v_stack_m140 == 0) {
        v_r14 = (unsigned int)((v_r14) | (32));
    }
    a1 = (((*(unsigned __int8 *)(v_stack_m150 + 180)) & (32)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_r14)) & (32)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    if ((*(unsigned __int64 *)(v_stack_m150 + 168)) == 0) goto loc_0073302C;
    if ((((unsigned __int8)(v_r15)) & (2)) != 0) goto loc_00732FF4;
    if (*(unsigned __int64 *)(v_stack_m110 + 48) == 0) goto loc_00732FEB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 48) + 8) == 0) goto loc_00732FEB;
    result = PiDevCfgGetDriverPackageId(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 48) + 8), v_stack_m108, v_stack_m140, a4);
    if (sign_flag) goto loc_00732FC8;
    a2 = 0;
    result = memset(v_stack_mD8, a2, a2 + 80, a4);
    v_stack_mD8 = v_rip - 7406169;
    a4 = 0;
    v_stack_m1A0 = 1;
    v_stack_mC8 = v_stack_m128;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 18;
    v_stack_mBC = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, v_stack_m100, a4 + 8, a4);
    v_stack_m198 = (unsigned int)(result);
    result = 0;
    if (sign_flag) goto loc_00733139;
    if (v_stack_mB8 >= 0) goto loc_00732FCA;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m128, a2, a4 + 8, a4);
loc_00732FC8:
    result = 0;
loc_00732FCA:
    result = v_stack_m128;
    if (v_stack_m120 == 0) {
        result = *(unsigned __int64 *)(v_stack_m110 + 48);
    }
    v_stack_m158 = v_xmm1;
    v_stack_mF8 = v_xmm0;
loc_00732FEB:
    v_r15 = (unsigned int)((v_r15) | (2));
    v_stack_m194 = (unsigned int)(v_r15);
loc_00732FF4:
    if (v_stack_mF8 == 0) goto loc_0073302C;
    a4 = (v_stack_m158) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_m150 + 160)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_m150 + 168), a2, v_stack_mF8, a4);
    if ((unsigned int)(result) == 0) {
        v_r14 = (unsigned int)((v_r14) | (2));
    }
    a1 = (((*(unsigned __int8 *)(v_stack_m150 + 180)) & (2)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_r14)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    result = (*(unsigned __int64 *)(v_stack_m150 + 80)) - (v_stack_m78);
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_m150 + 88);
        result = (result) - (v_stack_m70);
    }
    if (result != 0) goto loc_00733062;
    v_r14 = (unsigned int)((v_r14) | (1));
    goto loc_00733070;
loc_00733062:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m150 + 180)))) & (1)) != 0) {
    }
    a1 = (v_stack_m160) << (16);
    a1 = (a1) | (v_stack_m15E);
    a1 = (a1) << (16);
    *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    if (!(condition_is_below)) {
        a1 = (a1) | (v_stack_m15E);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if (!(condition_is_below)) {
        a1 = (a1) | (0xF000ULL);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if (((256) & ((unsigned int)(v_r14))) == 0) {
        a1 = (a1) | (256);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if ((((unsigned __int8)(v_r14)) & (32)) == 0) {
        a1 = (a1) | (32);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if ((((unsigned __int8)(v_r14)) & (16)) == 0) {
        a1 = (a1) | (16);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) {
        a1 = (a1) | (2);
        *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    }
    if ((((unsigned __int8)(v_r14)) & (1)) != 0) goto loc_00732B7A;
    a1 = (a1) | (1);
    *(unsigned __int64 *)(v_stack_m150 + 184) = a1;
    goto loc_00732B7A;
loc_00733130:
    v_stack_m198 = (unsigned int)((unsigned int)(0xC000009AULL));
loc_00733139:
    v_r13 = 0;
loc_0073313C:
    result = 256;
    if (v_stack_m188 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m188, a2, v_stack_mF8, a4);
    }
    if (sign_flag) goto loc_007332BB;
    if (v_stack_m178 == v_stack_m178) goto loc_007332B6;
loc_00733168:
    if ((*(unsigned __int64 *)(v_stack_m178 + 184)) == -1) goto loc_007331BA;
    if (0 == 0) goto loc_007331B7;
    if ((*(unsigned __int64 *)(0 + 184)) > (*(unsigned __int64 *)(v_stack_m178 + 184))) goto loc_007331B7;
    if ((*(unsigned __int64 *)(0 + 184)) != (*(unsigned __int64 *)(v_stack_m178 + 184))) goto loc_007331BA;
    if ((*(unsigned __int8 *)(v_rip + 7549113)) == 0) goto loc_007331A0;
    if ((*(unsigned int *)(v_stack_m178 + 176)) == 0) goto loc_007331A0;
    if ((*(unsigned int *)(0 + 176)) == 0) goto loc_007331B7;
loc_007331A0:
    goto loc_007331BA;
loc_007331AA:
    v_r13 = 0;
    v_stack_m198 = 0;
    goto loc_0073313C;
loc_007331B7:
loc_007331BA:
    if ((*(unsigned __int64 *)(v_stack_m178)) != v_stack_m178) goto loc_00733168;
    if (v_stack_m178 == 0) goto loc_007332B6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m178 + 16)))) & (2)) == 0) goto loc_00733256;
    v_stack_m154 = 1;
    if (v_stack_m178 == v_stack_m178) goto loc_00733294;
loc_007331F9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m178 + 16)))) & (2)) == 0) goto loc_00733243;
    result = *(unsigned __int64 *)(v_stack_m178 + 184);
    if ((*(unsigned __int64 *)(v_stack_m178 + 184)) == (*(unsigned __int64 *)(v_stack_m178 + 184))) {
        v_stack_mF0 = 0x140012ULL;
        result = v_stack_m154;
        v_stack_mE8 = v_rip + 3981751;
        a2 = v_stack_mF0;
        a1 = *(unsigned __int64 *)(v_stack_m178 + 40);
        a4 = 4;
        v_stack_m1A0 = 4;
        a3 = 0;
        v_stack_m1A8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(v_stack_m178)) != v_stack_m178) goto loc_007331F9;
    goto loc_00733294;
loc_00733256:
    a3 = 0;
    result = IopGetRegistryValue(*(unsigned __int64 *)(v_stack_m178 + 40), v_rip + 3981639, a3, v_stack_m188);
    if (sign_flag) goto loc_00733294;
    result = PnpValidateRegistryDword(v_stack_m188, v_rip + 3981639, a3, v_stack_m188);
    if ((unsigned __int8)(result) == 0) goto loc_0073328D;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m188 + 8)) + v_stack_m188 * 1)) != 0) {
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m188, a2, a3, v_stack_m188);
loc_00733294:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8)) != v_stack_m178) goto loc_007332F3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178 + 8))) != v_stack_m178) goto loc_007332F3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178 + 8)) = *(unsigned __int64 *)(v_stack_m178);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8) = *(unsigned __int64 *)(v_stack_m178 + 8);
    *(unsigned __int64 *)(v_stack_m80) = v_stack_m178;
    goto loc_007332BB;
loc_007332B6:
loc_007332BB:
    if (v_stack_m178 == v_stack_m178) goto loc_007332FA;
    if ((*(unsigned __int64 *)(v_stack_m178 + 8)) != v_stack_m178) goto loc_007332F3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8)) != v_stack_m178) goto loc_007332F3;
    v_stack_m178 = *(unsigned __int64 *)(v_stack_m178);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m178) + 8) = v_stack_m178;
    result = PiDevCfgFreeDeviceMigrationNode(v_stack_m178, v_stack_m178, a3, v_stack_m188);
    goto loc_007332BB;
loc_007332F3:
loc_007332FA:
    result = RtlFreeAnsiString(v_stack_m148, v_stack_m178, a3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m138, v_stack_m178, a3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m108, v_stack_m178, a3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m128, v_stack_m178, a3, v_stack_m188);
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m178, a3, v_stack_m188);
    v_rsp = (v_rsp) + (400);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgFindDeviceMigrationNode(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint16_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint16_t v_stack_m15E;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x6D7DFA)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r15 = 0;
    v_stack_m80 = Arg5;
    result = 0;
    v_stack_m180 = Arg4;
    v_stack_mEC = 0;
    v_stack_m48 = 0;
    v_stack_m88 = Arg3;
    v_stack_m170 = v_stack_m178;
    v_stack_m118 = Arg2;
    v_stack_m178 = v_stack_m178;
    v_stack_m110 = Arg1;
    v_stack_m1A8 = v_stack_m168;
    v_stack_m150 = 0;
    v_stack_m194 = 0;
    v_stack_m160 = 0;
    v_stack_m164 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m130 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_m158 = 0;
    v_stack_mF8 = 0;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m154 = 0;
    v_stack_m168 = 0;
    result = NtQueryKey(Arg3, local_r15 + 4, v_stack_m68, local_r15 + 40);
    if (sign_flag) goto loc_007332BB;
    if (v_stack_m54 == 0) goto loc_007332B6;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m50)) + (13));
    v_stack_m190 = (uint32_t)((uint32_t)(v_stack_m4C) + Arg1 * 2);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C) + Arg1 * 2)), (uint32_t)(0x63647050ULL), local_r15 + 40);
    v_stack_m188 = result;
    if (result != 0) goto loc_00732A64;
    goto loc_007332BB;
loc_00732A64:
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_00732A85;
    result = RtlGUIDFromString(*(uint64_t *)(arg1 + 0x28), v_stack_m78, (uint32_t)(0x63647050ULL), local_r15 + 40);
    if (sign_flag) goto loc_007332BB;
loc_00732A85:
    v_stack_m1A0 = v_stack_m168;
    v_stack_m1A8 = (uint32_t)((uint32_t)(v_stack_m4C) + Arg1 * 2);
    v_stack_m15C = 0;
    result = ZwEnumerateValueKey(v_stack_m88, 0, 1, v_stack_m188);
    v_stack_m198 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_007331AA;
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_00732B04;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m188, Arg2, 1, v_stack_m188);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m168)) + (2));
    v_stack_m190 = (uint32_t)(local_rbx);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x63647050ULL), v_stack_m188);
    v_stack_m188 = result;
    if (result == 0) goto loc_00733130;
    local_r15 = (uint32_t)((local_r15) - 1);
    goto loc_00732B7E;
loc_00732B04:
    Arg2 = 0;
    if (sign_flag) goto loc_00733139;
    result = PnpValidateRegistryDword(v_stack_m188, Arg2, (uint32_t)(0x63647050ULL), v_stack_m188);
    local_r14 = (uint32_t)(Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(v_stack_m188 + 0x8);
        local_r14 = *(uint32_t *)(result + v_stack_m188 * 1);
    }
    result = ((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x10))) >> (1);
    *(uint16_t *)(v_stack_m188 + result * 2 + 0x14) = 0;
    result = CmIsRootEnumeratedDevice(v_stack_m188 + 20, Arg2, (uint32_t)(0x63647050ULL), v_stack_m188);
    if ((uint8_t)(result) != 0) goto loc_00732B75;
    result = PiDevCfgQueryDeviceMigrationNode(Arg1, v_stack_m188 + 20, v_stack_m150, v_stack_m188);
    v_stack_m198 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00732B86;
    result = 0;
    v_stack_m150 = 0;
    result = PiDevCfgClearDeviceMigrationNode(Arg1, v_stack_m188 + 20, v_stack_m150, v_stack_m188);
loc_00732B75:
loc_00732B7A:
loc_00732B7E:
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_00732A85;
loc_00732B86:
    local_r13 = 0;
    if (sign_flag) goto loc_0073313C;
    *(uint32_t *)(v_stack_m150 + 0xB4) = (uint32_t)((uint32_t)(v_stack_m180));
    if ((*(uint64_t *)(v_stack_m170)) != v_stack_m178) goto loc_007332F3;
    *(uint64_t *)(v_stack_m150 + 0x8) = v_stack_m170;
    *(uint64_t *)(v_stack_m150) = v_stack_m178;
    *(uint64_t *)(v_stack_m170) = v_stack_m150;
    v_stack_m170 = v_stack_m150;
    result = wcsicmp(*(uint64_t *)(v_stack_m150 + 0x20), *(uint64_t *)(Arg2 + 0x8), v_stack_m150, v_stack_m188);
    result = (uint32_t)(-(result));
    local_r14 = (uint32_t)(~((uint32_t)(v_stack_m180)));
    local_r14 = (uint32_t)((local_r14) & ((uint32_t)((uint32_t)(0x10000000ULL))));
    Arg1 = (((*(uint32_t *)(v_stack_m150 + 0xB4)) & ((uint32_t)((uint32_t)(0x10000000ULL)))) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    local_r13 = (v_stack_m118) - (v_stack_m150);
loc_00732C17:
    result = PiDevCfgGetMigrationDeviceIdScore(*(uint64_t *)(v_stack_m150 + 0x38), *(uint64_t *)(v_stack_m150 + 0x38 + local_r13 * 1 - 0x8), v_stack_m150, v_stack_m188);
    *(uint16_t *)(v_stack_m160) = (uint16_t)(result);
    if (((uint16_t)(result)) != ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        local_r14 = (uint32_t)((local_r14) | (*(uint32_t *)(v_rip + 0x418383)));
    }
    local_rdi = (v_stack_m150 + 56) + (16);
    local_r12 = (v_stack_m160) + (2);
    local_r15 = (v_rip + 4293507) + (4);
    local_rbx = (2) - (1);
    if (condition_is_not_equal) goto loc_00732C17;
    if (condition_is_above_or_equal) goto loc_00732C73;
    if (condition_is_above_or_equal) goto loc_00732C86;
    Arg1 = ((((uint32_t)(local_r14)) & (0x11000ULL)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    goto loc_00732C82;
loc_00732C73:
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
loc_00732C82:
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    local_r13 = 0;
    if (*(uint64_t *)(v_stack_m150 + 0x90) == 0) goto loc_00732CE0;
    if ((*(uint64_t *)(v_stack_m118 + 0x50)) == 0) goto loc_00732CE0;
loc_00732CA4:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m150 + 0x90))) == 0) goto loc_00732CE0;
    result = PnpMultiSzContainsString(*(uint64_t *)(v_stack_m118 + 0x50), *(uint64_t *)(v_stack_m150 + 0x90), v_stack_m150, v_stack_m188);
    if (result != 0) goto loc_00732CD4;
    result = (result) | (-1);
loc_00732CC0:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m150 + 0x90) + result * 2)) != 0) goto loc_00732CC0;
    local_rdi = (*(uint64_t *)(v_stack_m150 + 0x90) + result * 2) + (2);
    goto loc_00732CA4;
loc_00732CD4:
    *(uint64_t *)(v_stack_m150 + 0x98) = local_rdi;
loc_00732CE0:
    Arg1 = (((*(uint32_t *)(v_stack_m150 + 0xB4)) & (512)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    if ((*(uint64_t *)(v_stack_m150 + 0x80)) == 0) goto loc_00732DC7;
    if ((*(uint64_t *)(v_stack_m150 + 0x80)) < 0) goto loc_00732D95;
    Arg2 = 0;
    result = memset(v_stack_mD8, Arg2, Arg2 + 80, v_stack_m188);
    v_stack_mD8 = v_rip - 7434137;
    v_stack_mC8 = v_stack_m138;
    v_stack_m1A0 = 1;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 18;
    v_stack_mBC = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, *(uint64_t *)(v_stack_m118 + 0x8), 1, *(uint64_t *)(v_stack_m118 + 0x10));
    v_stack_m198 = (uint32_t)(result);
    if (sign_flag) goto loc_0073313C;
    if (v_stack_mB8 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m138;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(v_stack_m118 + 0x10));
    }
    v_stack_m194 = (uint32_t)((uint32_t)(v_stack_m194));
loc_00732D95:
    if (v_stack_m130 == 0) goto loc_00732DC7;
    Arg4 = (v_stack_m138) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_m150 + 0x78)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_m150 + 0x80), Arg2, v_stack_m130, Arg4);
    if ((uint32_t)(result) == 0) {
    }
    Arg1 = ((((uint32_t)(local_r14)) & (768)) == 0) ? 1 : 0;
    result = (((*(uint32_t *)(v_stack_m150 + 0xB4)) & (256)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    if ((((uint8_t)((uint32_t)(v_stack_m194))) & (48)) != 0) goto loc_00732E90;
    Arg2 = 0;
    result = memset(v_stack_mD8, Arg2, Arg2 + 80, Arg4);
    v_stack_mD8 = v_rip - 7465779;
    v_stack_mC8 = v_stack_m164;
    v_stack_mB0 = v_rip - 7385514;
    v_stack_mA0 = v_stack_m148;
    v_stack_m1A0 = 2;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 7;
    v_stack_mC0 = 4;
    v_stack_mA8 = 18;
    v_stack_m94 = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, *(uint64_t *)(v_stack_m118 + 0x8), 1, *(uint64_t *)(v_stack_m118 + 0x10));
    v_stack_m198 = (uint32_t)(result);
    if (sign_flag) goto loc_0073313C;
    if (v_stack_m90 < 0) {
        Arg2 = 0;
        Arg1 = v_stack_m148;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, *(uint64_t *)(v_stack_m118 + 0x10));
    }
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m194)) | (48));
    v_stack_m194 = (uint32_t)(local_r15);
loc_00732E90:
    result = (uint32_t)(((uint32_t)(v_stack_m164)) ^ (*(uint32_t *)(v_stack_m150 + 0x60)));
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00732EA1;
    local_r14 = (uint32_t)((local_r14) | (16));
    goto loc_00732EB6;
loc_00732EA1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0xB4)))) & (16)) != 0) goto loc_00732EB2;
    if (((v_stack_m164) & (16)) != 0) {
    }
    if ((*(uint64_t *)(v_stack_m150 + 0x70)) == 0) goto loc_00732EE9;
    if (v_stack_m140 == 0) goto loc_00732EED;
    Arg4 = (v_stack_m148) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_m150 + 0x68)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_m150 + 0x70), Arg2, v_stack_m140, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00732EF8;
loc_00732EE9:
loc_00732EED:
    if ((*(uint64_t *)(v_stack_m150 + 0x70)) != 0) goto loc_00732EFC;
    if (v_stack_m140 == 0) {
        local_r14 = (uint32_t)((local_r14) | (32));
    }
    Arg1 = (((*(uint8_t *)(v_stack_m150 + 0xB4)) & (32)) != 0) ? 1 : 0;
    result = ((((uint8_t)(local_r14)) & (32)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    if ((*(uint64_t *)(v_stack_m150 + 0xA8)) == 0) goto loc_0073302C;
    if ((((uint8_t)(local_r15)) & (2)) != 0) goto loc_00732FF4;
    if (*(uint64_t *)(v_stack_m110 + 0x30) == 0) goto loc_00732FEB;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x30) + 0x8) == 0) goto loc_00732FEB;
    result = PiDevCfgGetDriverPackageId(*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x30) + 0x8), v_stack_m108, v_stack_m140, Arg4);
    if (sign_flag) goto loc_00732FC8;
    Arg2 = 0;
    result = memset(v_stack_mD8, Arg2, Arg2 + 80, Arg4);
    v_stack_mD8 = v_rip - 7406169;
    Arg4 = 0;
    v_stack_m1A0 = 1;
    v_stack_mC8 = v_stack_m128;
    v_stack_m1A8 = v_stack_mD8;
    v_stack_mD0 = 18;
    v_stack_mBC = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_mD8, v_stack_m100, Arg4 + 8, Arg4);
    v_stack_m198 = (uint32_t)(result);
    result = 0;
    if (sign_flag) goto loc_00733139;
    if (v_stack_mB8 >= 0) goto loc_00732FCA;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m128, Arg2, Arg4 + 8, Arg4);
loc_00732FC8:
    result = 0;
loc_00732FCA:
    result = v_stack_m128;
    if (v_stack_m120 == 0) {
        result = *(uint64_t *)(v_stack_m110 + 0x30);
    }
    v_stack_m158 = v_xmm1;
    v_stack_mF8 = v_xmm0;
loc_00732FEB:
    local_r15 = (uint32_t)((local_r15) | (2));
    v_stack_m194 = (uint32_t)(local_r15);
loc_00732FF4:
    if (v_stack_mF8 == 0) goto loc_0073302C;
    Arg4 = (v_stack_m158) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_m150 + 0xA0)) >> (1);
    v_stack_m1A8 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_m150 + 0xA8), Arg2, v_stack_mF8, Arg4);
    if ((uint32_t)(result) == 0) {
        local_r14 = (uint32_t)((local_r14) | (2));
    }
    Arg1 = (((*(uint8_t *)(v_stack_m150 + 0xB4)) & (2)) != 0) ? 1 : 0;
    result = ((((uint8_t)(local_r14)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    result = (*(uint64_t *)(v_stack_m150 + 0x50)) - (v_stack_m78);
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_m150 + 0x58);
        result = (result) - (v_stack_m70);
    }
    if (result != 0) goto loc_00733062;
    local_r14 = (uint32_t)((local_r14) | (1));
    goto loc_00733070;
loc_00733062:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0xB4)))) & (1)) != 0) {
    }
    Arg1 = (v_stack_m160) << (16);
    Arg1 = (Arg1) | (v_stack_m15E);
    Arg1 = (Arg1) << (16);
    *(void **)(v_stack_m150 + 0xB8) = Arg1;
    if (!(condition_is_below)) {
        Arg1 = (Arg1) | (v_stack_m15E);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if (!(condition_is_below)) {
        Arg1 = (Arg1) | (0xF000ULL);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if (((256) & ((uint32_t)(local_r14))) == 0) {
        Arg1 = (Arg1) | (256);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if ((((uint8_t)(local_r14)) & (32)) == 0) {
        Arg1 = (Arg1) | (32);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if ((((uint8_t)(local_r14)) & (16)) == 0) {
        Arg1 = (Arg1) | (16);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if ((((uint8_t)(local_r14)) & (2)) == 0) {
        Arg1 = (Arg1) | (2);
        *(void **)(v_stack_m150 + 0xB8) = Arg1;
    }
    if ((((uint8_t)(local_r14)) & (1)) != 0) goto loc_00732B7A;
    Arg1 = (Arg1) | (1);
    *(void **)(v_stack_m150 + 0xB8) = Arg1;
    goto loc_00732B7A;
loc_00733130:
    v_stack_m198 = (uint32_t)((uint32_t)(0xC000009AULL));
loc_00733139:
    local_r13 = 0;
loc_0073313C:
    result = 256;
    if (v_stack_m188 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m188, Arg2, v_stack_mF8, Arg4);
    }
    if (sign_flag) goto loc_007332BB;
    if (v_stack_m178 == v_stack_m178) goto loc_007332B6;
loc_00733168:
    if ((*(uint64_t *)(v_stack_m178 + 0xB8)) == -1) goto loc_007331BA;
    if (0 == 0) goto loc_007331B7;
    if ((*(uint64_t *)(0 + 0xB8)) > (*(uint64_t *)(v_stack_m178 + 0xB8))) goto loc_007331B7;
    if ((*(uint64_t *)(0 + 0xB8)) != (*(uint64_t *)(v_stack_m178 + 0xB8))) goto loc_007331BA;
    if ((*(uint8_t *)(v_rip + 0x7330B9)) == 0) goto loc_007331A0;
    if ((*(uint32_t *)(v_stack_m178 + 0xB0)) == 0) goto loc_007331A0;
    if ((*(uint32_t *)(0 + 0xB0)) == 0) goto loc_007331B7;
loc_007331A0:
    goto loc_007331BA;
loc_007331AA:
    local_r13 = 0;
    v_stack_m198 = 0;
    goto loc_0073313C;
loc_007331B7:
loc_007331BA:
    if ((*(uint64_t *)(v_stack_m178)) != v_stack_m178) goto loc_00733168;
    if (v_stack_m178 == 0) goto loc_007332B6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x10)))) & (2)) == 0) goto loc_00733256;
    v_stack_m154 = 1;
    if (v_stack_m178 == v_stack_m178) goto loc_00733294;
loc_007331F9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x10)))) & (2)) == 0) goto loc_00733243;
    result = *(uint64_t *)(v_stack_m178 + 0xB8);
    if ((*(uint64_t *)(v_stack_m178 + 0xB8)) == (*(uint64_t *)(v_stack_m178 + 0xB8))) {
        v_stack_mF0 = 0x140012ULL;
        result = v_stack_m154;
        v_stack_mE8 = v_rip + 3981751;
        Arg2 = v_stack_mF0;
        Arg1 = *(uint64_t *)(v_stack_m178 + 0x28);
        Arg4 = 4;
        v_stack_m1A0 = 4;
        Arg3 = 0;
        v_stack_m1A8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(v_stack_m178)) != v_stack_m178) goto loc_007331F9;
    goto loc_00733294;
loc_00733256:
    Arg3 = 0;
    result = IopGetRegistryValue(*(uint64_t *)(v_stack_m178 + 0x28), v_rip + 3981639, Arg3, v_stack_m188);
    if (sign_flag) goto loc_00733294;
    result = PnpValidateRegistryDword(v_stack_m188, v_rip + 3981639, Arg3, v_stack_m188);
    if ((uint8_t)(result) == 0) goto loc_0073328D;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x8)) + v_stack_m188 * 1)) != 0) {
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m188, Arg2, Arg3, v_stack_m188);
loc_00733294:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8)) != v_stack_m178) goto loc_007332F3;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m178 + 0x8))) != v_stack_m178) goto loc_007332F3;
    *(uint64_t *)(*(uint64_t *)(v_stack_m178 + 0x8)) = *(uint64_t *)(v_stack_m178);
    *(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8) = *(uint64_t *)(v_stack_m178 + 0x8);
    *(uint64_t *)(v_stack_m80) = v_stack_m178;
    goto loc_007332BB;
loc_007332B6:
loc_007332BB:
    if (v_stack_m178 == v_stack_m178) goto loc_007332FA;
    if ((*(uint64_t *)(v_stack_m178 + 0x8)) != v_stack_m178) goto loc_007332F3;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8)) != v_stack_m178) goto loc_007332F3;
    v_stack_m178 = *(uint64_t *)(v_stack_m178);
    *(uint64_t *)(*(uint64_t *)(v_stack_m178) + 0x8) = v_stack_m178;
    result = PiDevCfgFreeDeviceMigrationNode(v_stack_m178, v_stack_m178, Arg3, v_stack_m188);
    goto loc_007332BB;
loc_007332F3:
loc_007332FA:
    result = RtlFreeAnsiString(v_stack_m148, v_stack_m178, Arg3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m138, v_stack_m178, Arg3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m108, v_stack_m178, Arg3, v_stack_m188);
    result = RtlFreeAnsiString(v_stack_m128, v_stack_m178, Arg3, v_stack_m188);
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m178, Arg3, v_stack_m188);
    local_rsp = (local_rsp) + (400);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00732920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
