# BiBuildIdentifierList

- RVA: `0x00A3E584`–`0x00A3EBDC` (길이 `1,624` bytes)
- VA: `0x0000000140A3E584`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE748`
- 디코드: `427`개 명령, `1,624/1,624` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A3E632` → [BiOpenKey](BiOpenKey_function_00A3F60C.md) (function, `0x00A3F60C`)
- `0x00A3E64D` → [BiEnumerateSubKeys](BiEnumerateSubKeys_function_00A3FD24.md) (function, `0x00A3FD24`)
- `0x00A3E679` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A3E686` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00A3E69A` → [BcdOpenObject](../91/BcdOpenObject_function_00916704.md) (function, `0x00916704`)
- `0x00A3E6AE` → [BiGetObjectDescription](BiGetObjectDescription_function_00A3F2FC.md) (function, `0x00A3F2FC`)
- `0x00A3E6D1` → [BcdCloseObject](BcdCloseObject_function_00A3FB08.md) (function, `0x00A3FB08`)
- `0x00A3E70A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A3E78E` → [BcdGetElementData](BcdGetElementData_function_00A3E390.md) (function, `0x00A3E390`)
- `0x00A3E7A5` → [BiGetSavedBootEntry](../A4/BiGetSavedBootEntry_function_00A41248.md) (function, `0x00A41248`)
- `0x00A3E7C1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A3E7C9` → [BcdCloseObject](BcdCloseObject_function_00A3FB08.md) (function, `0x00A3FB08`)
- `0x00A3E7DB` → [BiEnumerateBootEntries](../A4/BiEnumerateBootEntries_function_00A4074C.md) (function, `0x00A4074C`)
- `0x00A3E80E` → [BiGetObjectReferenceFromEfiEntry](BiGetObjectReferenceFromEfiEntry_function_00A3FB4C.md) (function, `0x00A3FB4C`)
- `0x00A3E866` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A3E96E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A3E9AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A3E9C7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A3EAFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A3EB5C` → [BcdCloseObject](BcdCloseObject_function_00A3FB08.md) (function, `0x00A3FB08`)
- `0x00A3EB76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A3EB84` → [BiCloseKey](../91/BiCloseKey_function_00916A00.md) (function, `0x00916A00`)
- `0x00A3EB96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A3EBA4` → [BiFreeIdentifierList](../A4/BiFreeIdentifierList_function_00A40FD8.md) (function, `0x00A40FD8`)
- `0x00A3EBAD` → [BiFreeIdentifierList](../A4/BiFreeIdentifierList_function_00A40FD8.md) (function, `0x00A40FD8`)
- `0x00A3EBB6` → [BiFreeIdentifierList](../A4/BiFreeIdentifierList_function_00A40FD8.md) (function, `0x00A40FD8`)
- `0x00A3EBBE` → [BiFreeIdentifierList](../A4/BiFreeIdentifierList_function_00A40FD8.md) (function, `0x00A40FD8`)
- `0x00A3EBD2` → [BiLogMessage](BiLogMessage_function_00A3D3A8.md) (function, `0x00A3D3A8`)

### Direct callers
- [BiExportStoreAlterationsToEfi](../82/BiExportStoreAlterationsToEfi_function_00826C58.md) at `0x00826C97`
- [BiBindEfiNamespaceObjects](../A4/BiBindEfiNamespaceObjects_function_00A40EB4.md) at `0x00A40EEE`

### Static image references
- `0x00A3E5A0` → RVA `0x00E0A740` (`.data`; read)
- `0x00A3E5D7` → RVA `0x00B0A540` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A3EBC6` → RVA `0x00B0C9E0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00A3E679` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A3E70A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A3E7C1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A3E866` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A3E96E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A3E9AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A3E9C7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A3EAFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A3EB76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A3EB96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A3E584  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A3E589  55                              push rbp
00A3E58A  56                              push rsi
00A3E58B  57                              push rdi
00A3E58C  41 54                           push r12
00A3E58E  41 55                           push r13
00A3E590  41 56                           push r14
00A3E592  41 57                           push r15
00A3E594  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00A3E599  48 81 EC C0 00 00 00            sub rsp, 0xc0
00A3E5A0  48 8B 05 99 C1 3C 00            mov rax, qword ptr [rip + 0x3cc199]
00A3E5A7  48 33 C4                        xor rax, rsp
00A3E5AA  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00A3E5AE  45 33 F6                        xor r14d, r14d
00A3E5B1  4D 89 40 08                     mov qword ptr [r8 + 8], r8
00A3E5B5  0F 57 C0                        xorps xmm0, xmm0
00A3E5B8  4D 89 00                        mov qword ptr [r8], r8
00A3E5BB  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A3E5BF  4C 89 75 EF                     mov qword ptr [rbp - 0x11], r14
00A3E5C3  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00A3E5C7  4C 8D 4D CF                     lea r9, [rbp - 0x31]
00A3E5CB  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A3E5CF  44 89 75 8B                     mov dword ptr [rbp - 0x75], r14d
00A3E5D3  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00A3E5D7  48 8D 15 62 BF 0C 00            lea rdx, [rip + 0xcbf62]
00A3E5DE  48 8D 45 9F                     lea rax, [rbp - 0x61]
00A3E5E2  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
00A3E5E6  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00A3E5EA  49 8B F8                        mov rdi, r8
00A3E5ED  48 8D 45 9F                     lea rax, [rbp - 0x61]
00A3E5F1  4C 89 75 DF                     mov qword ptr [rbp - 0x21], r14
00A3E5F5  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00A3E5F9  41 B8 19 00 02 00               mov r8d, 0x20019
00A3E5FF  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A3E603  66 44 89 75 87                  mov word ptr [rbp - 0x79], r14w
00A3E608  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00A3E60C  4C 8B E1                        mov r12, rcx
00A3E60F  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A3E613  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
00A3E617  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
00A3E61B  41 8B F6                        mov esi, r14d
00A3E61E  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
00A3E622  4C 89 75 F7                     mov qword ptr [rbp - 9], r14
00A3E626  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A3E62A  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
00A3E62E  4C 89 75 BF                     mov qword ptr [rbp - 0x41], r14
00A3E632  E8 D5 0F 00 00                  call 0x140a3f60c
00A3E637  8B D8                           mov ebx, eax
00A3E639  85 C0                           test eax, eax
00A3E63B  0F 88 09 03 00 00               js 0x140a3e94a
00A3E641  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00A3E645  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00A3E649  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00A3E64D  E8 D2 16 00 00                  call 0x140a3fd24
00A3E652  8B D8                           mov ebx, eax
00A3E654  85 C0                           test eax, eax
00A3E656  0F 88 EA 02 00 00               js 0x140a3e946
00A3E65C  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
00A3E660  45 8B FE                        mov r15d, r14d
00A3E663  44 3B 7D C7                     cmp r15d, dword ptr [rbp - 0x39]
00A3E667  0F 83 66 01 00 00               jae 0x140a3e7d3
00A3E66D  41 8B D7                        mov edx, r15d
00A3E670  48 8D 4D FF                     lea rcx, [rbp - 1]
00A3E674  49 8B 54 D5 00                  mov rdx, qword ptr [r13 + rdx*8]
00A3E679  E8 02 C1 9E FF                  call 0x14042a780
00A3E67E  48 8D 55 0F                     lea rdx, [rbp + 0xf]
00A3E682  48 8D 4D FF                     lea rcx, [rbp - 1]
00A3E686  E8 65 38 EB FF                  call 0x1408f1ef0
00A3E68B  85 C0                           test eax, eax
00A3E68D  78 4A                           js 0x140a3e6d9
00A3E68F  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00A3E693  49 8B CC                        mov rcx, r12
00A3E696  48 8D 55 0F                     lea rdx, [rbp + 0xf]
00A3E69A  E8 65 80 ED FF                  call 0x140916704
00A3E69F  85 C0                           test eax, eax
00A3E6A1  78 36                           js 0x140a3e6d9
00A3E6A3  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
00A3E6A7  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00A3E6AB  48 8B CE                        mov rcx, rsi
00A3E6AE  E8 49 0C 00 00                  call 0x140a3f2fc
00A3E6B3  85 C0                           test eax, eax
00A3E6B5  0F 88 0B 01 00 00               js 0x140a3e7c6
00A3E6BB  44 8B 75 EB                     mov r14d, dword ptr [rbp - 0x15]
00A3E6BF  41 8B C6                        mov eax, r14d
00A3E6C2  25 00 00 00 F0                  and eax, 0xf0000000
00A3E6C7  3D 00 00 00 10                  cmp eax, 0x10000000
00A3E6CC  74 10                           je 0x140a3e6de
00A3E6CE  48 8B CE                        mov rcx, rsi
00A3E6D1  E8 32 14 00 00                  call 0x140a3fb08
00A3E6D6  45 33 F6                        xor r14d, r14d
00A3E6D9  41 FF C7                        inc r15d
00A3E6DC  EB 85                           jmp 0x140a3e663
00A3E6DE  41 8B C6                        mov eax, r14d
00A3E6E1  25 00 00 F0 00                  and eax, 0xf00000
00A3E6E6  3D 00 00 10 00                  cmp eax, 0x100000
00A3E6EB  75 E1                           jne 0x140a3e6ce
00A3E6ED  41 81 E6 FF FF 0F 00            and r14d, 0xfffff
00A3E6F4  41 83 FE 01                     cmp r14d, 1
00A3E6F8  74 D4                           je 0x140a3e6ce
00A3E6FA  BA 38 00 00 00                  mov edx, 0x38
00A3E6FF  B9 02 01 00 00                  mov ecx, 0x102
00A3E704  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A3E70A  E8 E1 39 14 00                  call 0x140b820f0
00A3E70F  48 8B D8                        mov rbx, rax
00A3E712  48 85 C0                        test rax, rax
00A3E715  0F 84 3E 04 00 00               je 0x140a3eb59
00A3E71B  0F 57 C0                        xorps xmm0, xmm0
00A3E71E  33 C0                           xor eax, eax
00A3E720  0F 11 03                        movups xmmword ptr [rbx], xmm0
00A3E723  0F 11 43 10                     movups xmmword ptr [rbx + 0x10], xmm0
00A3E727  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
00A3E72B  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00A3E72F  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00A3E732  0F 10 45 0F                     movups xmm0, xmmword ptr [rbp + 0xf]
00A3E736  83 C8 04                        or eax, 4
00A3E739  89 43 30                        mov dword ptr [rbx + 0x30], eax
00A3E73C  F3 0F 7F 43 10                  movdqu xmmword ptr [rbx + 0x10], xmm0
00A3E741  41 81 FE FF FF 0F 00            cmp r14d, 0xfffff
00A3E748  0F 85 C3 01 00 00               jne 0x140a3e911
00A3E74E  83 C8 08                        or eax, 8
00A3E751  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00A3E755  89 43 30                        mov dword ptr [rbx + 0x30], eax
00A3E758  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
00A3E75C  48 39 08                        cmp qword ptr [rax], rcx
00A3E75F  0F 85 62 01 00 00               jne 0x140a3e8c7
00A3E765  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A3E769  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00A3E76D  48 89 0B                        mov qword ptr [rbx], rcx
00A3E770  48 89 18                        mov qword ptr [rax], rbx
00A3E773  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
00A3E777  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00A3E77B  C7 45 D7 02 00 00 00            mov dword ptr [rbp - 0x29], 2
00A3E782  4C 8D 45 87                     lea r8, [rbp - 0x79]
00A3E786  BA 82 00 00 16                  mov edx, 0x16000082
00A3E78B  48 8B CE                        mov rcx, rsi
00A3E78E  E8 FD FB FF FF                  call 0x140a3e390
00A3E793  45 33 F6                        xor r14d, r14d
00A3E796  85 C0                           test eax, eax
00A3E798  0F 89 A8 03 00 00               jns 0x140a3eb46
00A3E79E  48 8D 55 EF                     lea rdx, [rbp - 0x11]
00A3E7A2  48 8B CE                        mov rcx, rsi
00A3E7A5  E8 9E 2A 00 00                  call 0x140a41248
00A3E7AA  85 C0                           test eax, eax
00A3E7AC  78 18                           js 0x140a3e7c6
00A3E7AE  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00A3E7B2  BA 42 43 44 4B                  mov edx, 0x4b444342
00A3E7B7  8B 41 08                        mov eax, dword ptr [rcx + 8]
00A3E7BA  83 4B 30 02                     or dword ptr [rbx + 0x30], 2
00A3E7BE  89 43 20                        mov dword ptr [rbx + 0x20], eax
00A3E7C1  E8 AA 40 14 00                  call 0x140b82870
00A3E7C6  48 8B CE                        mov rcx, rsi
00A3E7C9  E8 3A 13 00 00                  call 0x140a3fb08
00A3E7CE  E9 06 FF FF FF                  jmp 0x140a3e6d9
00A3E7D3  48 8D 55 8B                     lea rdx, [rbp - 0x75]
00A3E7D7  48 8D 4D F7                     lea rcx, [rbp - 9]
00A3E7DB  E8 6C 1F 00 00                  call 0x140a4074c
00A3E7E0  4C 8B 65 F7                     mov r12, qword ptr [rbp - 9]
00A3E7E4  8B D8                           mov ebx, eax
00A3E7E6  85 C0                           test eax, eax
00A3E7E8  0F 88 4F 01 00 00               js 0x140a3e93d
00A3E7EE  49 8B DE                        mov rbx, r14
00A3E7F1  49 8B F4                        mov rsi, r12
00A3E7F4  8B 4D 8B                        mov ecx, dword ptr [rbp - 0x75]
00A3E7F7  48 8B C6                        mov rax, rsi
00A3E7FA  49 2B C4                        sub rax, r12
00A3E7FD  48 3B C1                        cmp rax, rcx
00A3E800  0F 83 F1 01 00 00               jae 0x140a3e9f7
00A3E806  48 8D 55 0F                     lea rdx, [rbp + 0xf]
00A3E80A  48 8D 4E 04                     lea rcx, [rsi + 4]
00A3E80E  E8 39 13 00 00                  call 0x140a3fb4c
00A3E813  85 C0                           test eax, eax
00A3E815  78 3F                           js 0x140a3e856
00A3E817  44 8B 4E 0C                     mov r9d, dword ptr [rsi + 0xc]
00A3E81B  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00A3E81F  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A3E823  48 3B C8                        cmp rcx, rax
00A3E826  0F 84 A2 00 00 00               je 0x140a3e8ce
00A3E82C  44 8B 41 30                     mov r8d, dword ptr [rcx + 0x30]
00A3E830  41 F6 C0 04                     test r8b, 4
00A3E834  74 1B                           je 0x140a3e851
00A3E836  48 8B 55 0F                     mov rdx, qword ptr [rbp + 0xf]
00A3E83A  48 2B 51 10                     sub rdx, qword ptr [rcx + 0x10]
00A3E83E  75 08                           jne 0x140a3e848
00A3E840  48 8B 55 17                     mov rdx, qword ptr [rbp + 0x17]
00A3E844  48 2B 51 18                     sub rdx, qword ptr [rcx + 0x18]
00A3E848  48 85 D2                        test rdx, rdx
00A3E84B  0F 84 84 00 00 00               je 0x140a3e8d5
00A3E851  48 8B 09                        mov rcx, qword ptr [rcx]
00A3E854  EB C9                           jmp 0x140a3e81f
00A3E856  BA 38 00 00 00                  mov edx, 0x38
00A3E85B  B9 02 01 00 00                  mov ecx, 0x102
00A3E860  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A3E866  E8 85 38 14 00                  call 0x140b820f0
00A3E86B  48 8B D8                        mov rbx, rax
00A3E86E  48 85 C0                        test rax, rax
00A3E871  0F 84 BE 00 00 00               je 0x140a3e935
00A3E877  0F 57 C0                        xorps xmm0, xmm0
00A3E87A  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00A3E87E  0F 11 03                        movups xmmword ptr [rbx], xmm0
00A3E881  33 C0                           xor eax, eax
00A3E883  0F 11 43 10                     movups xmmword ptr [rbx + 0x10], xmm0
00A3E887  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
00A3E88B  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00A3E88F  83 4B 30 08                     or dword ptr [rbx + 0x30], 8
00A3E893  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00A3E897  48 39 08                        cmp qword ptr [rax], rcx
00A3E89A  75 2B                           jne 0x140a3e8c7
00A3E89C  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A3E8A0  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00A3E8A4  48 89 0B                        mov qword ptr [rbx], rcx
00A3E8A7  48 89 18                        mov qword ptr [rax], rbx
00A3E8AA  48 89 5D 97                     mov qword ptr [rbp - 0x69], rbx
00A3E8AE  E9 EA 00 00 00                  jmp 0x140a3e99d
00A3E8B3  48 89 01                        mov qword ptr [rcx], rax
00A3E8B6  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A3E8BA  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00A3E8BE  48 39 38                        cmp qword ptr [rax], rdi
00A3E8C1  0F 84 C8 00 00 00               je 0x140a3e98f
00A3E8C7  B9 03 00 00 00                  mov ecx, 3
00A3E8CC  CD 29                           int 0x29
00A3E8CE  B8 25 02 00 C0                  mov eax, 0xc0000225
00A3E8D3  EB 1A                           jmp 0x140a3e8ef
00A3E8D5  41 F6 C0 03                     test r8b, 3
00A3E8D9  0F 84 72 FF FF FF               je 0x140a3e851
00A3E8DF  44 39 49 20                     cmp dword ptr [rcx + 0x20], r9d
00A3E8E3  0F 85 68 FF FF FF               jne 0x140a3e851
00A3E8E9  48 8B D9                        mov rbx, rcx
00A3E8EC  41 8B C6                        mov eax, r14d
00A3E8EF  41 BE 20 00 00 00               mov r14d, 0x20
00A3E8F5  85 C0                           test eax, eax
00A3E8F7  0F 88 59 FF FF FF               js 0x140a3e856
00A3E8FD  48 8B 03                        mov rax, qword ptr [rbx]
00A3E900  48 39 58 08                     cmp qword ptr [rax + 8], rbx
00A3E904  75 C1                           jne 0x140a3e8c7
00A3E906  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00A3E90A  48 39 19                        cmp qword ptr [rcx], rbx
00A3E90D  75 B8                           jne 0x140a3e8c7
00A3E90F  EB A2                           jmp 0x140a3e8b3
00A3E911  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00A3E915  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00A3E919  48 39 08                        cmp qword ptr [rax], rcx
00A3E91C  75 A9                           jne 0x140a3e8c7
00A3E91E  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A3E922  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00A3E926  48 89 0B                        mov qword ptr [rbx], rcx
00A3E929  48 89 18                        mov qword ptr [rax], rbx
00A3E92C  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
00A3E930  E9 42 FE FF FF                  jmp 0x140a3e777
00A3E935  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A3E93A  45 33 F6                        xor r14d, r14d
00A3E93D  4D 85 E4                        test r12, r12
00A3E940  0F 85 28 02 00 00               jne 0x140a3eb6e
00A3E946  48 8B 75 BF                     mov rsi, qword ptr [rbp - 0x41]
00A3E94A  4C 39 75 CF                     cmp qword ptr [rbp - 0x31], r14
00A3E94E  0F 85 2C 02 00 00               jne 0x140a3eb80
00A3E954  48 85 F6                        test rsi, rsi
00A3E957  0F 85 31 02 00 00               jne 0x140a3eb8e
00A3E95D  85 DB                           test ebx, ebx
00A3E95F  0F 88 3B 02 00 00               js 0x140a3eba0
00A3E965  8B C3                           mov eax, ebx
00A3E967  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00A3E96B  48 33 CC                        xor rcx, rsp
00A3E96E  E8 CD DC C6 FF                  call 0x1406ac640
00A3E973  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
00A3E97B  48 81 C4 C0 00 00 00            add rsp, 0xc0
00A3E982  41 5F                           pop r15
00A3E984  41 5E                           pop r14
00A3E986  41 5D                           pop r13
00A3E988  41 5C                           pop r12
00A3E98A  5F                              pop rdi
00A3E98B  5E                              pop rsi
00A3E98C  5D                              pop rbp
00A3E98D  C3                              ret
00A3E98E  CC                              int3
00A3E98F  48 89 3B                        mov qword ptr [rbx], rdi
00A3E992  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A3E996  48 89 18                        mov qword ptr [rax], rbx
00A3E999  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
00A3E99D  8B 56 08                        mov edx, dword ptr [rsi + 8]
00A3E9A0  B9 02 01 00 00                  mov ecx, 0x102
00A3E9A5  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A3E9AB  E8 40 37 14 00                  call 0x140b820f0
00A3E9B0  4C 8B F8                        mov r15, rax
00A3E9B3  48 85 C0                        test rax, rax
00A3E9B6  0F 84 79 FF FF FF               je 0x140a3e935
00A3E9BC  44 8B 46 08                     mov r8d, dword ptr [rsi + 8]
00A3E9C0  48 8D 56 04                     lea rdx, [rsi + 4]
00A3E9C4  48 8B C8                        mov rcx, rax
00A3E9C7  E8 74 7E C8 FF                  call 0x1406c6840
00A3E9CC  4C 89 7B 28                     mov qword ptr [rbx + 0x28], r15
00A3E9D0  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A3E9D4  89 43 20                        mov dword ptr [rbx + 0x20], eax
00A3E9D7  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00A3E9DA  83 E0 DF                        and eax, 0xffffffdf
00A3E9DD  41 0B C6                        or eax, r14d
00A3E9E0  45 33 F6                        xor r14d, r14d
00A3E9E3  83 C8 01                        or eax, 1
00A3E9E6  89 43 30                        mov dword ptr [rbx + 0x30], eax
00A3E9E9  8B 06                           mov eax, dword ptr [rsi]
00A3E9EB  85 C0                           test eax, eax
00A3E9ED  74 08                           je 0x140a3e9f7
00A3E9EF  48 03 F0                        add rsi, rax
00A3E9F2  E9 FD FD FF FF                  jmp 0x140a3e7f4
00A3E9F7  48 8B 75 8F                     mov rsi, qword ptr [rbp - 0x71]
00A3E9FB  EB 0E                           jmp 0x140a3ea0b
00A3E9FD  48 89 3B                        mov qword ptr [rbx], rdi
00A3EA00  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A3EA04  48 89 18                        mov qword ptr [rax], rbx
00A3EA07  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
00A3EA0B  48 8D 45 8F                     lea rax, [rbp - 0x71]
00A3EA0F  48 3B F0                        cmp rsi, rax
00A3EA12  75 7D                           jne 0x140a3ea91
00A3EA14  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00A3EA18  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00A3EA1C  48 3B C1                        cmp rax, rcx
00A3EA1F  74 1A                           je 0x140a3ea3b
00A3EA21  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A3EA25  48 89 01                        mov qword ptr [rcx], rax
00A3EA28  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00A3EA2C  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A3EA30  48 89 38                        mov qword ptr [rax], rdi
00A3EA33  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00A3EA37  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A3EA3B  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00A3EA3F  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00A3EA43  48 3B C1                        cmp rax, rcx
00A3EA46  74 1A                           je 0x140a3ea62
00A3EA48  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A3EA4C  48 89 01                        mov qword ptr [rcx], rax
00A3EA4F  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
00A3EA53  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A3EA57  48 89 38                        mov qword ptr [rax], rdi
00A3EA5A  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00A3EA5E  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A3EA62  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00A3EA66  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00A3EA6A  48 3B C1                        cmp rax, rcx
00A3EA6D  74 1A                           je 0x140a3ea89
00A3EA6F  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A3EA73  48 89 02                        mov qword ptr [rdx], rax
00A3EA76  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00A3EA7A  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A3EA7E  48 89 38                        mov qword ptr [rax], rdi
00A3EA81  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00A3EA85  48 89 50 08                     mov qword ptr [rax + 8], rdx
00A3EA89  41 8B DE                        mov ebx, r14d
00A3EA8C  E9 AC FE FF FF                  jmp 0x140a3e93d
00A3EA91  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
00A3EA94  48 8B DE                        mov rbx, rsi
00A3EA97  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00A3EA9B  48 8D 45 9F                     lea rax, [rbp - 0x61]
00A3EA9F  48 3B C8                        cmp rcx, rax
00A3EAA2  0F 84 96 00 00 00               je 0x140a3eb3e
00A3EAA8  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00A3EAAB  A8 03                           test al, 3
00A3EAAD  0F 84 83 00 00 00               je 0x140a3eb36
00A3EAB3  39 51 20                        cmp dword ptr [rcx + 0x20], edx
00A3EAB6  75 7E                           jne 0x140a3eb36
00A3EAB8  48 8B 11                        mov rdx, qword ptr [rcx]
00A3EABB  48 8B 36                        mov rsi, qword ptr [rsi]
00A3EABE  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
00A3EAC2  0F 85 FF FD FF FF               jne 0x140a3e8c7
00A3EAC8  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00A3EACC  48 39 08                        cmp qword ptr [rax], rcx
00A3EACF  0F 85 F2 FD FF FF               jne 0x140a3e8c7
00A3EAD5  48 89 10                        mov qword ptr [rax], rdx
00A3EAD8  48 89 42 08                     mov qword ptr [rdx + 8], rax
00A3EADC  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00A3EADF  8B D0                           mov edx, eax
00A3EAE1  0F 10 41 10                     movups xmm0, xmmword ptr [rcx + 0x10]
00A3EAE5  F3 0F 7F 43 10                  movdqu xmmword ptr [rbx + 0x10], xmm0
00A3EAEA  33 51 30                        xor edx, dword ptr [rcx + 0x30]
00A3EAED  83 E2 02                        and edx, 2
00A3EAF0  33 D0                           xor edx, eax
00A3EAF2  89 53 30                        mov dword ptr [rbx + 0x30], edx
00A3EAF5  BA 42 43 44 4B                  mov edx, 0x4b444342
00A3EAFA  E8 71 3D 14 00                  call 0x140b82870
00A3EAFF  83 4B 30 04                     or dword ptr [rbx + 0x30], 4
00A3EB03  48 8B 0B                        mov rcx, qword ptr [rbx]
00A3EB06  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00A3EB0A  0F 85 B7 FD FF FF               jne 0x140a3e8c7
00A3EB10  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00A3EB14  48 39 18                        cmp qword ptr [rax], rbx
00A3EB17  0F 85 AA FD FF FF               jne 0x140a3e8c7
00A3EB1D  48 89 08                        mov qword ptr [rax], rcx
00A3EB20  48 89 41 08                     mov qword ptr [rcx + 8], rax
00A3EB24  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00A3EB28  48 39 38                        cmp qword ptr [rax], rdi
00A3EB2B  0F 85 96 FD FF FF               jne 0x140a3e8c7
00A3EB31  E9 C7 FE FF FF                  jmp 0x140a3e9fd
00A3EB36  48 8B 09                        mov rcx, qword ptr [rcx]
00A3EB39  E9 5D FF FF FF                  jmp 0x140a3ea9b
00A3EB3E  48 8B 36                        mov rsi, qword ptr [rsi]
00A3EB41  E9 C5 FE FF FF                  jmp 0x140a3ea0b
00A3EB46  44 38 75 87                     cmp byte ptr [rbp - 0x79], r14b
00A3EB4A  0F 84 4E FC FF FF               je 0x140a3e79e
00A3EB50  83 4B 30 10                     or dword ptr [rbx + 0x30], 0x10
00A3EB54  E9 45 FC FF FF                  jmp 0x140a3e79e
00A3EB59  48 8B CE                        mov rcx, rsi
00A3EB5C  E8 A7 0F 00 00                  call 0x140a3fb08
00A3EB61  45 33 F6                        xor r14d, r14d
00A3EB64  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A3EB69  E9 D8 FD FF FF                  jmp 0x140a3e946
00A3EB6E  BA 42 43 44 4B                  mov edx, 0x4b444342
00A3EB73  49 8B CC                        mov rcx, r12
00A3EB76  E8 F5 3C 14 00                  call 0x140b82870
00A3EB7B  E9 C6 FD FF FF                  jmp 0x140a3e946
00A3EB80  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00A3EB84  E8 77 7E ED FF                  call 0x140916a00
00A3EB89  E9 C6 FD FF FF                  jmp 0x140a3e954
00A3EB8E  BA 42 43 44 4B                  mov edx, 0x4b444342
00A3EB93  48 8B CE                        mov rcx, rsi
00A3EB96  E8 D5 3C 14 00                  call 0x140b82870
00A3EB9B  E9 BD FD FF FF                  jmp 0x140a3e95d
00A3EBA0  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00A3EBA4  E8 2F 24 00 00                  call 0x140a40fd8
00A3EBA9  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00A3EBAD  E8 26 24 00 00                  call 0x140a40fd8
00A3EBB2  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00A3EBB6  E8 1D 24 00 00                  call 0x140a40fd8
00A3EBBB  48 8B CF                        mov rcx, rdi
00A3EBBE  E8 15 24 00 00                  call 0x140a40fd8
00A3EBC3  44 8B C3                        mov r8d, ebx
00A3EBC6  48 8D 15 13 DE 0C 00            lea rdx, [rip + 0xcde13]
00A3EBCD  B9 04 00 00 00                  mov ecx, 4
00A3EBD2  E8 D1 E7 FF FF                  call 0x140a3d3a8
00A3EBD7  E9 89 FD FF FF                  jmp 0x140a3e965
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiBuildIdentifierList(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int16 v_stack_mD8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 3981721)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r14 = 0;
    *(unsigned __int64 *)(a3 + 8) = a3;
    *(unsigned __int64 *)(a3) = a3;
    v_stack_m70 = 0;
    v_stack_mA8 = v_stack_mB0;
    v_stack_mD4 = 0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_m78 = 0;
    v_stack_mB8 = v_stack_mC0;
    v_stack_m80 = 0;
    v_stack_mC0 = v_stack_mC0;
    v_stack_mD8 = 0;
    v_stack_mC8 = v_stack_mD0;
    v_stack_m98 = 0;
    v_stack_mD0 = v_stack_mD0;
    v_stack_m50 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m90 = 0;
    v_stack_mA0 = 0;
    result = BiOpenKey(a1, v_rip + 835426, (unsigned int)(0x20019ULL), v_stack_m90);
    if (sign_flag) goto loc_00A3E94A;
    result = BiEnumerateSubKeys(v_stack_m90, v_stack_mA0, v_stack_m98, v_stack_m90);
    if (sign_flag) goto loc_00A3E946;
loc_00A3E663:
    if (0 >= v_stack_m98) goto loc_00A3E7D3;
    result = RtlInitUnicodeString(v_stack_m60, *(unsigned __int64 *)(v_stack_mA0 + 0 * 8), v_stack_m98, v_stack_m90);
    result = RtlGUIDFromString(v_stack_m60, v_stack_m50, v_stack_m98, v_stack_m90);
    if (sign_flag) goto loc_00A3E6D9;
    result = BcdOpenObject(a1, v_stack_m50, v_stack_m80, v_stack_m90);
    if (sign_flag) goto loc_00A3E6D9;
    result = BiGetObjectDescription(v_stack_m80, v_stack_m78, v_stack_m80, v_stack_m90);
    if (sign_flag) goto loc_00A3E7C6;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) & (0xF0000000ULL));
    if (((unsigned int)(result)) == 0x10000000ULL) goto loc_00A3E6DE;
loc_00A3E6CE:
    result = BcdCloseObject(v_stack_m80, v_stack_m78, v_stack_m80, v_stack_m90);
    v_r14 = 0;
loc_00A3E6D9:
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00A3E663;
loc_00A3E6DE:
    result = (unsigned int)((0) & (0xF00000ULL));
    if (((unsigned int)(result)) != 0x100000ULL) goto loc_00A3E6CE;
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFULL));
    if (((unsigned int)(v_r14)) == 1) goto loc_00A3E6CE;
    result = ExAllocatePool2(258, 56, (unsigned int)(0x4B444342ULL), v_stack_m90);
    if (result == 0) goto loc_00A3EB59;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) | (4));
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    if (((unsigned int)(v_r14)) != 0xFFFFFULL) goto loc_00A3E911;
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(v_stack_mB8)) != v_stack_mC0) goto loc_00A3E8C7;
    *(unsigned __int64 *)(result + 8) = v_stack_mB8;
    *(unsigned __int64 *)(result) = v_stack_mC0;
    *(unsigned __int64 *)(v_stack_mB8) = result;
    v_stack_mB8 = result;
loc_00A3E777:
    v_stack_m88 = 2;
    result = BcdGetElementData(v_stack_m80, (unsigned int)(0x16000082ULL), v_stack_mD8, v_stack_m88);
    v_r14 = 0;
    if (!sign_flag) goto loc_00A3EB46;
loc_00A3E79E:
    result = BiGetSavedBootEntry(v_stack_m80, v_stack_m70, v_stack_mD8, v_stack_m88);
    if (!(sign_flag)) {
        a1 = v_stack_m70;
        a2 = 0x4B444342ULL;
        result = *(unsigned int *)(a1 + 8);
        *(unsigned int *)(result + 32) = (unsigned int)(result);
        result = ExFreePoolWithTag(a1, a2, v_stack_mD8, v_stack_m88);
    }
    result = BcdCloseObject(v_stack_m80, a2, v_stack_mD8, v_stack_m88);
    goto loc_00A3E6D9;
loc_00A3E7D3:
    result = BiEnumerateBootEntries(v_stack_m68, v_stack_mD4, v_stack_mD8, v_stack_m88);
    if (sign_flag) goto loc_00A3E93D;
loc_00A3E7F4:
    result = (v_stack_m68) - (v_stack_m68);
    if (result >= ((unsigned int)(v_stack_mD4))) goto loc_00A3E9F7;
    result = BiGetObjectReferenceFromEfiEntry(v_stack_m68 + 4, v_stack_m50, v_stack_mD8, v_stack_m88);
    if (sign_flag) goto loc_00A3E856;
loc_00A3E81F:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00A3E8CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 48)))) & (4)) == 0) goto loc_00A3E851;
    a2 = (v_stack_m50) - (*(unsigned __int64 *)(v_stack_mB0 + 16));
    if (!(condition_is_not_equal)) {
        a2 = v_stack_m48;
        a2 = (a2) - (*(unsigned __int64 *)(v_stack_mB0 + 24));
    }
    if (a2 == 0) goto loc_00A3E8D5;
loc_00A3E851:
    goto loc_00A3E81F;
loc_00A3E856:
    result = ExAllocatePool2(258, 56, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    if (result == 0) goto loc_00A3E935;
    *(unsigned __int64 *)(result) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = 0;
    if ((*(unsigned __int64 *)(v_stack_mC8)) != v_stack_mD0) goto loc_00A3E8C7;
    *(unsigned __int64 *)(result + 8) = v_stack_mC8;
    *(unsigned __int64 *)(result) = v_stack_mD0;
    *(unsigned __int64 *)(v_stack_mC8) = 0;
    v_stack_mC8 = 0;
    goto loc_00A3E99D;
loc_00A3E8B3:
    *(unsigned __int64 *)(v_stack_mD0) = v_stack_mC8;
    *(unsigned __int64 *)(v_stack_mC8 + 8) = v_stack_mD0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8))) == a3) goto loc_00A3E98F;
loc_00A3E8C7:
loc_00A3E8CE:
    goto loc_00A3E8EF;
loc_00A3E8D5:
    if ((((unsigned __int8)((unsigned int)(0x4B444342ULL))) & (3)) == 0) goto loc_00A3E851;
    if ((*(unsigned int *)(3 + 32)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + 12))))) goto loc_00A3E851;
loc_00A3E8EF:
    if (sign_flag) goto loc_00A3E856;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(3) + 8)) != 3) goto loc_00A3E8C7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(3 + 8))) != 3) goto loc_00A3E8C7;
    goto loc_00A3E8B3;
loc_00A3E911:
    if ((*(unsigned __int64 *)(v_stack_mA8)) != v_stack_mB0) goto loc_00A3E8C7;
    *(unsigned __int64 *)(3 + 8) = v_stack_mA8;
    *(unsigned __int64 *)(3) = v_stack_mB0;
    *(unsigned __int64 *)(v_stack_mA8) = 3;
    v_stack_mA8 = 3;
    goto loc_00A3E777;
loc_00A3E935:
    v_r14 = 0;
loc_00A3E93D:
    if (v_stack_m68 != 0) goto loc_00A3EB6E;
loc_00A3E946:
loc_00A3E94A:
    if (v_stack_m90 != 0) goto loc_00A3EB80;
loc_00A3E954:
    if (v_stack_mA0 != 0) goto loc_00A3EB8E;
loc_00A3E95D:
    if (sign_flag) goto loc_00A3EBA0;
loc_00A3E965:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, 56, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    v_rsp = (v_rsp) + (192);
    return result;
loc_00A3E98F:
    *(unsigned __int64 *)(v_stack_p10) = a3;
    *(unsigned __int64 *)(v_stack_p10 + 8) = result;
    *(unsigned __int64 *)(result) = v_stack_p10;
    *(unsigned __int64 *)(a3 + 8) = v_stack_p10;
loc_00A3E99D:
    result = ExAllocatePool2(258, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    if (result == 0) goto loc_00A3E935;
    result = memcpy(result, v_stack_mA0 + 4, (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    *(unsigned __int64 *)(v_stack_p10 + 40) = result;
    *(unsigned int *)(v_stack_p10 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 48))) & (0xFFFFFFDFULL));
    result = (unsigned int)((result) | (0));
    v_r14 = 0;
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(v_stack_p10 + 48) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0))) == 0) goto loc_00A3E9F7;
    v_rsi = (v_stack_mA0) + ((unsigned int)(*(unsigned int *)(v_stack_mA0)));
    goto loc_00A3E7F4;
loc_00A3E9F7:
    goto loc_00A3EA0B;
loc_00A3E9FD:
    *(unsigned __int64 *)(v_stack_p10) = a3;
    *(unsigned __int64 *)(v_stack_p10 + 8) = (unsigned int)(*(unsigned int *)(v_stack_mA0));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_mA0))) = v_stack_p10;
    *(unsigned __int64 *)(a3 + 8) = v_stack_p10;
loc_00A3EA0B:
    if (v_stack_mD0 != v_stack_mD0) goto loc_00A3EA91;
    result = v_stack_mB0;
    if (v_stack_mB0 != v_stack_mB0) {
        a1 = *(unsigned __int64 *)(a3 + 8);
        *(unsigned __int64 *)(a1) = v_stack_mB0;
        result = v_stack_mA8;
        *(unsigned __int64 *)(a3 + 8) = result;
        *(unsigned __int64 *)(result) = a3;
        result = v_stack_mB0;
        *(unsigned __int64 *)(result + 8) = a1;
    }
    result = v_stack_mC0;
    if (v_stack_mC0 != v_stack_mC0) {
        a1 = *(unsigned __int64 *)(a3 + 8);
        *(unsigned __int64 *)(a1) = v_stack_mC0;
        result = v_stack_mB8;
        *(unsigned __int64 *)(a3 + 8) = result;
        *(unsigned __int64 *)(result) = a3;
        result = v_stack_mC0;
        *(unsigned __int64 *)(result + 8) = a1;
    }
    result = v_stack_mD0;
    if (v_stack_mD0 != v_stack_mD0) {
        a2 = *(unsigned __int64 *)(a3 + 8);
        *(unsigned __int64 *)(a2) = v_stack_mD0;
        result = v_stack_mC8;
        *(unsigned __int64 *)(a3 + 8) = result;
        *(unsigned __int64 *)(result) = a3;
        result = v_stack_mD0;
        *(unsigned __int64 *)(result + 8) = a2;
    }
    goto loc_00A3E93D;
loc_00A3EA91:
loc_00A3EA9B:
    if (v_stack_mC0 == v_stack_mC0) goto loc_00A3EB3E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 48)))) & (3)) == 0) goto loc_00A3EB36;
    if ((*(unsigned int *)(v_stack_mC0 + 32)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 32))))) goto loc_00A3EB36;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC0) + 8)) != v_stack_mC0) goto loc_00A3E8C7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC0 + 8))) != v_stack_mC0) goto loc_00A3E8C7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC0 + 8)) = *(unsigned __int64 *)(v_stack_mC0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC0) + 8) = *(unsigned __int64 *)(v_stack_mC0 + 8);
    *(unsigned __int64 *)(v_stack_mD0 + 16) = v_xmm0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 48))))) ^ (*(unsigned int *)(v_stack_mC0 + 48)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 48)))));
    *(unsigned int *)(v_stack_mD0 + 48) = (unsigned int)(a2);
    result = ExFreePoolWithTag(v_stack_mC0, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0) + 8)) != v_stack_mD0) goto loc_00A3E8C7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 8))) != v_stack_mD0) goto loc_00A3E8C7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 8)) = *(unsigned __int64 *)(v_stack_mD0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0) + 8) = *(unsigned __int64 *)(v_stack_mD0 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8))) != a3) goto loc_00A3E8C7;
    goto loc_00A3E9FD;
loc_00A3EB36:
    goto loc_00A3EA9B;
loc_00A3EB3E:
    goto loc_00A3EA0B;
loc_00A3EB46:
    if (v_stack_mD8 == 0) goto loc_00A3E79E;
    goto loc_00A3E79E;
loc_00A3EB59:
    result = BcdCloseObject(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0)), (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    v_r14 = 0;
    goto loc_00A3E946;
loc_00A3EB6E:
    result = ExFreePoolWithTag(v_stack_m68, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    goto loc_00A3E946;
loc_00A3EB80:
    result = BiCloseKey(v_stack_m90, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    goto loc_00A3E954;
loc_00A3EB8E:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0)), (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    goto loc_00A3E95D;
loc_00A3EBA0:
    result = BiFreeIdentifierList(v_stack_mD0, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    result = BiFreeIdentifierList(v_stack_mC0, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    result = BiFreeIdentifierList(v_stack_mB0, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    result = BiFreeIdentifierList(a3, (unsigned int)(0x4B444342ULL), (unsigned int)(*(unsigned int *)(v_stack_mA0 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    result = BiLogMessage(4, v_rip + 843283, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)(*(unsigned int *)(v_stack_m68 + 12)));
    goto loc_00A3E965;
}
```

## 5. (Beta) C Style

```c
int64_t BiBuildIdentifierList(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint16_t v_stack_mD8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x3CC199)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r14 = 0;
    *(void **)(arg3 + 0x8) = Arg3;
    *(void **)(arg3) = Arg3;
    v_stack_m70 = 0;
    v_stack_mA8 = v_stack_mB0;
    v_stack_mD4 = 0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_m78 = 0;
    v_stack_mB8 = v_stack_mC0;
    v_stack_m80 = 0;
    v_stack_mC0 = v_stack_mC0;
    v_stack_mD8 = 0;
    v_stack_mC8 = v_stack_mD0;
    v_stack_m98 = 0;
    v_stack_mD0 = v_stack_mD0;
    v_stack_m50 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m90 = 0;
    v_stack_mA0 = 0;
    result = BiOpenKey(Arg1, v_rip + 835426, (uint32_t)(0x20019ULL), v_stack_m90);
    if (sign_flag) goto loc_00A3E94A;
    result = BiEnumerateSubKeys(v_stack_m90, v_stack_mA0, v_stack_m98, v_stack_m90);
    if (sign_flag) goto loc_00A3E946;
loc_00A3E663:
    if (0 >= v_stack_m98) goto loc_00A3E7D3;
    result = RtlInitUnicodeString(v_stack_m60, *(uint64_t *)(v_stack_mA0 + 0x0 * 8), v_stack_m98, v_stack_m90);
    result = RtlGUIDFromString(v_stack_m60, v_stack_m50, v_stack_m98, v_stack_m90);
    if (sign_flag) goto loc_00A3E6D9;
    result = BcdOpenObject(Arg1, v_stack_m50, v_stack_m80, v_stack_m90);
    if (sign_flag) goto loc_00A3E6D9;
    result = BiGetObjectDescription(v_stack_m80, v_stack_m78, v_stack_m80, v_stack_m90);
    if (sign_flag) goto loc_00A3E7C6;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) & (0xF0000000ULL));
    if (((uint32_t)(result)) == 0x10000000ULL) goto loc_00A3E6DE;
loc_00A3E6CE:
    result = BcdCloseObject(v_stack_m80, v_stack_m78, v_stack_m80, v_stack_m90);
    local_r14 = 0;
loc_00A3E6D9:
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00A3E663;
loc_00A3E6DE:
    result = (uint32_t)((0) & (0xF00000ULL));
    if (((uint32_t)(result)) != 0x100000ULL) goto loc_00A3E6CE;
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFULL));
    if (((uint32_t)(local_r14)) == 1) goto loc_00A3E6CE;
    result = ExAllocatePool2(258, 56, (uint32_t)(0x4B444342ULL), v_stack_m90);
    if (result == 0) goto loc_00A3EB59;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) | (4));
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    *(uint64_t *)(result + 0x10) = v_xmm0;
    if (((uint32_t)(local_r14)) != 0xFFFFFULL) goto loc_00A3E911;
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    if ((*(uint64_t *)(v_stack_mB8)) != v_stack_mC0) goto loc_00A3E8C7;
    *(uint64_t *)(result + 0x8) = v_stack_mB8;
    *(uint64_t *)(result) = v_stack_mC0;
    *(uint64_t *)(v_stack_mB8) = result;
    v_stack_mB8 = result;
loc_00A3E777:
    v_stack_m88 = 2;
    result = BcdGetElementData(v_stack_m80, (uint32_t)(0x16000082ULL), v_stack_mD8, v_stack_m88);
    local_r14 = 0;
    if (!sign_flag) goto loc_00A3EB46;
loc_00A3E79E:
    result = BiGetSavedBootEntry(v_stack_m80, v_stack_m70, v_stack_mD8, v_stack_m88);
    if (!(sign_flag)) {
        Arg1 = v_stack_m70;
        Arg2 = 0x4B444342ULL;
        result = *(uint32_t *)(Arg1 + 0x8);
        *(uint32_t *)(result + 0x20) = (uint32_t)(result);
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_mD8, v_stack_m88);
    }
    result = BcdCloseObject(v_stack_m80, Arg2, v_stack_mD8, v_stack_m88);
    goto loc_00A3E6D9;
loc_00A3E7D3:
    result = BiEnumerateBootEntries(v_stack_m68, v_stack_mD4, v_stack_mD8, v_stack_m88);
    if (sign_flag) goto loc_00A3E93D;
loc_00A3E7F4:
    result = (v_stack_m68) - (v_stack_m68);
    if (result >= ((uint32_t)(v_stack_mD4))) goto loc_00A3E9F7;
    result = BiGetObjectReferenceFromEfiEntry(v_stack_m68 + 4, v_stack_m50, v_stack_mD8, v_stack_m88);
    if (sign_flag) goto loc_00A3E856;
loc_00A3E81F:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00A3E8CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x30)))) & (4)) == 0) goto loc_00A3E851;
    Arg2 = (v_stack_m50) - (*(uint64_t *)(v_stack_mB0 + 0x10));
    if (!(condition_is_not_equal)) {
        Arg2 = v_stack_m48;
        Arg2 = (Arg2) - (*(uint64_t *)(v_stack_mB0 + 0x18));
    }
    if (Arg2 == 0) goto loc_00A3E8D5;
loc_00A3E851:
    goto loc_00A3E81F;
loc_00A3E856:
    result = ExAllocatePool2(258, 56, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    if (result == 0) goto loc_00A3E935;
    *(uint64_t *)(result) = v_xmm0;
    result = 0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = 0;
    if ((*(uint64_t *)(v_stack_mC8)) != v_stack_mD0) goto loc_00A3E8C7;
    *(uint64_t *)(result + 0x8) = v_stack_mC8;
    *(uint64_t *)(result) = v_stack_mD0;
    *(uint64_t *)(v_stack_mC8) = 0;
    v_stack_mC8 = 0;
    goto loc_00A3E99D;
loc_00A3E8B3:
    *(uint64_t *)(v_stack_mD0) = v_stack_mC8;
    *(uint64_t *)(v_stack_mC8 + 0x8) = v_stack_mD0;
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0x8))) == Arg3) goto loc_00A3E98F;
loc_00A3E8C7:
loc_00A3E8CE:
    goto loc_00A3E8EF;
loc_00A3E8D5:
    if ((((uint8_t)((uint32_t)(0x4B444342ULL))) & (3)) == 0) goto loc_00A3E851;
    if ((*(uint32_t *)(3 + 0x20)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC))))) goto loc_00A3E851;
loc_00A3E8EF:
    if (sign_flag) goto loc_00A3E856;
    if ((*(uint64_t *)(*(uint64_t *)(3) + 0x8)) != 3) goto loc_00A3E8C7;
    if ((*(uint64_t *)(*(uint64_t *)(3 + 0x8))) != 3) goto loc_00A3E8C7;
    goto loc_00A3E8B3;
loc_00A3E911:
    if ((*(uint64_t *)(v_stack_mA8)) != v_stack_mB0) goto loc_00A3E8C7;
    *(uint64_t *)(3 + 0x8) = v_stack_mA8;
    *(uint64_t *)(3) = v_stack_mB0;
    *(uint64_t *)(v_stack_mA8) = 3;
    v_stack_mA8 = 3;
    goto loc_00A3E777;
loc_00A3E935:
    local_r14 = 0;
loc_00A3E93D:
    if (v_stack_m68 != 0) goto loc_00A3EB6E;
loc_00A3E946:
loc_00A3E94A:
    if (v_stack_m90 != 0) goto loc_00A3EB80;
loc_00A3E954:
    if (v_stack_mA0 != 0) goto loc_00A3EB8E;
loc_00A3E95D:
    if (sign_flag) goto loc_00A3EBA0;
loc_00A3E965:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 56, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    local_rsp = (local_rsp) + (192);
    return result;
loc_00A3E98F:
    *(void **)(v_stack_p10) = Arg3;
    *(uint64_t *)(v_stack_p10 + 0x8) = result;
    *(uint64_t *)(result) = v_stack_p10;
    *(uint64_t *)(arg3 + 0x8) = v_stack_p10;
loc_00A3E99D:
    result = ExAllocatePool2(258, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    if (result == 0) goto loc_00A3E935;
    result = memcpy(result, v_stack_mA0 + 4, (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    *(uint64_t *)(v_stack_p10 + 0x28) = result;
    *(uint32_t *)(v_stack_p10 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x30))) & (0xFFFFFFDFULL));
    result = (uint32_t)((result) | (0));
    local_r14 = 0;
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(v_stack_p10 + 0x30) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0))) == 0) goto loc_00A3E9F7;
    local_rsi = (v_stack_mA0) + ((uint32_t)(*(uint32_t *)(v_stack_mA0)));
    goto loc_00A3E7F4;
loc_00A3E9F7:
    goto loc_00A3EA0B;
loc_00A3E9FD:
    *(void **)(v_stack_p10) = Arg3;
    *(uint64_t *)(v_stack_p10 + 0x8) = (uint32_t)(*(uint32_t *)(v_stack_mA0));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_mA0))) = v_stack_p10;
    *(uint64_t *)(arg3 + 0x8) = v_stack_p10;
loc_00A3EA0B:
    if (v_stack_mD0 != v_stack_mD0) goto loc_00A3EA91;
    result = v_stack_mB0;
    if (v_stack_mB0 != v_stack_mB0) {
        Arg1 = *(uint64_t *)(arg3 + 0x8);
        *(uint64_t *)(Arg1) = v_stack_mB0;
        result = v_stack_mA8;
        *(uint64_t *)(arg3 + 0x8) = result;
        *(void **)(result) = Arg3;
        result = v_stack_mB0;
        *(uint64_t *)(result + 0x8) = Arg1;
    }
    result = v_stack_mC0;
    if (v_stack_mC0 != v_stack_mC0) {
        Arg1 = *(uint64_t *)(arg3 + 0x8);
        *(uint64_t *)(Arg1) = v_stack_mC0;
        result = v_stack_mB8;
        *(uint64_t *)(arg3 + 0x8) = result;
        *(void **)(result) = Arg3;
        result = v_stack_mC0;
        *(uint64_t *)(result + 0x8) = Arg1;
    }
    result = v_stack_mD0;
    if (v_stack_mD0 != v_stack_mD0) {
        Arg2 = *(uint64_t *)(arg3 + 0x8);
        *(uint64_t *)(Arg2) = v_stack_mD0;
        result = v_stack_mC8;
        *(uint64_t *)(arg3 + 0x8) = result;
        *(void **)(result) = Arg3;
        result = v_stack_mD0;
        *(uint64_t *)(result + 0x8) = Arg2;
    }
    goto loc_00A3E93D;
loc_00A3EA91:
loc_00A3EA9B:
    if (v_stack_mC0 == v_stack_mC0) goto loc_00A3EB3E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x30)))) & (3)) == 0) goto loc_00A3EB36;
    if ((*(uint32_t *)(v_stack_mC0 + 0x20)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x20))))) goto loc_00A3EB36;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mC0) + 0x8)) != v_stack_mC0) goto loc_00A3E8C7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mC0 + 0x8))) != v_stack_mC0) goto loc_00A3E8C7;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC0 + 0x8)) = *(uint64_t *)(v_stack_mC0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mC0) + 0x8) = *(uint64_t *)(v_stack_mC0 + 0x8);
    *(uint64_t *)(v_stack_mD0 + 0x10) = v_xmm0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x30))))) ^ (*(uint32_t *)(v_stack_mC0 + 0x30)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x30)))));
    *(uint32_t *)(v_stack_mD0 + 0x30) = (uint32_t)(Arg2);
    result = ExFreePoolWithTag(v_stack_mC0, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0) + 0x8)) != v_stack_mD0) goto loc_00A3E8C7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x8))) != v_stack_mD0) goto loc_00A3E8C7;
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x8)) = *(uint64_t *)(v_stack_mD0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0) + 0x8) = *(uint64_t *)(v_stack_mD0 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(arg3 + 0x8))) != Arg3) goto loc_00A3E8C7;
    goto loc_00A3E9FD;
loc_00A3EB36:
    goto loc_00A3EA9B;
loc_00A3EB3E:
    goto loc_00A3EA0B;
loc_00A3EB46:
    if (v_stack_mD8 == 0) goto loc_00A3E79E;
    goto loc_00A3E79E;
loc_00A3EB59:
    result = BcdCloseObject(*(uint64_t *)(*(uint64_t *)(v_stack_mD0)), (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    local_r14 = 0;
    goto loc_00A3E946;
loc_00A3EB6E:
    result = ExFreePoolWithTag(v_stack_m68, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    goto loc_00A3E946;
loc_00A3EB80:
    result = BiCloseKey(v_stack_m90, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    goto loc_00A3E954;
loc_00A3EB8E:
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_mD0)), (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    goto loc_00A3E95D;
loc_00A3EBA0:
    result = BiFreeIdentifierList(v_stack_mD0, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    result = BiFreeIdentifierList(v_stack_mC0, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    result = BiFreeIdentifierList(v_stack_mB0, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    result = BiFreeIdentifierList(Arg3, (uint32_t)(0x4B444342ULL), (uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    result = BiLogMessage(4, v_rip + 843283, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0xC)));
    goto loc_00A3E965;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A3E584&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
