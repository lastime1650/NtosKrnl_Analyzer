# RegRtlCopyTreeInternal

- RVA: `0x008324C0`–`0x008329EC` (길이 `1,324` bytes)
- VA: `0x00000001408324C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DAB58`
- 디코드: `369`개 명령, `1,324/1,324` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00832543` → [IoGetStackLimits](../../text/41/IoGetStackLimits_function_0041FD70.md) (function, `0x0041FD70`)
- `0x00832586` → [_RegRtlOpenKeyTransacted](../8E/_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008325B0` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x008325EF` → [RegRtlGetKeySecurity](RegRtlGetKeySecurity_function_008329F4.md) (function, `0x008329F4`)
- `0x00832605` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00832618` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00832669` → [RegRtlCreateKeyTransacted](../93/RegRtlCreateKeyTransacted_function_0093207C.md) (function, `0x0093207C`)
- `0x00832696` → [RegRtlSetKeySecurity](RegRtlSetKeySecurity_function_00832CDC.md) (function, `0x00832CDC`)
- `0x008326BB` → [RegRtlQueryInfoKey](../99/RegRtlQueryInfoKey_function_0099463C.md) (function, `0x0099463C`)
- `0x00832708` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00832732` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00832774` → [RegRtlEnumKey](../99/RegRtlEnumKey_function_00992C00.md) (function, `0x00992C00`)
- `0x008327AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008327BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0083280B` → [RegRtlCopyTreeInternal](RegRtlCopyTreeInternal_function_008324C0.md) (function, `0x008324C0`)
- `0x00832873` → [RegRtlEnumValue](../99/RegRtlEnumValue_function_0099369C.md) (function, `0x0099369C`)
- `0x008328B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008328CA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008328FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083290F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00832954` → [RegRtlSetValue](../99/RegRtlSetValue_function_00991B28.md) (function, `0x00991B28`)
- `0x0083297F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083298E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083299C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008329AA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008329B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008329C7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PnpCtxRegCopyTree](../82/PnpCtxRegCopyTree_function_008291EC.md) at `0x00829238`
- [RegRtlCopyTreeInternal](RegRtlCopyTreeInternal_function_008324C0.md) at `0x0083280B`

### Static image references
- `0x008324D9` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00832543` → [IoGetStackLimits](../../text/41/IoGetStackLimits_function_0041FD70.md) (`PAGE` → `.text`)
  - `0x008325B0` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x00832605` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00832618` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00832708` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00832732` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008327AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008327BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008328B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008328CA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008328FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083290F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0083297F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083298E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083299C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008329AA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008329B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008329C7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008324C0  40 55                           push rbp
008324C2  53                              push rbx
008324C3  56                              push rsi
008324C4  57                              push rdi
008324C5  41 54                           push r12
008324C7  41 55                           push r13
008324C9  41 56                           push r14
008324CB  41 57                           push r15
008324CD  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
008324D2  48 81 EC D8 00 00 00            sub rsp, 0xd8
008324D9  48 8B 05 60 82 5D 00            mov rax, qword ptr [rip + 0x5d8260]
008324E0  48 33 C4                        xor rax, rsp
008324E3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008324E7  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
008324EB  4C 8B F1                        mov r14, rcx
008324EE  33 C9                           xor ecx, ecx
008324F0  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
008324F4  33 C0                           xor eax, eax
008324F6  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
008324FA  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
008324FE  44 8B F9                        mov r15d, ecx
00832501  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
00832504  8B F9                           mov edi, ecx
00832506  89 4D 9F                        mov dword ptr [rbp - 0x61], ecx
00832509  8B F1                           mov esi, ecx
0083250B  89 4D A3                        mov dword ptr [rbp - 0x5d], ecx
0083250E  44 8B E1                        mov r12d, ecx
00832511  89 4D 83                        mov dword ptr [rbp - 0x7d], ecx
00832514  48 8B DA                        mov rbx, rdx
00832517  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0083251B  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0083251F  89 4D 8F                        mov dword ptr [rbp - 0x71], ecx
00832522  4D 8B E9                        mov r13, r9
00832525  89 4D A7                        mov dword ptr [rbp - 0x59], ecx
00832528  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
0083252C  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00832530  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00832534  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00832538  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0083253C  89 45 E7                        mov dword ptr [rbp - 0x19], eax
0083253F  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
00832543  E8 28 D8 BE FF                  call 0x14041fd70
00832548  48 8D 45 C7                     lea rax, [rbp - 0x39]
0083254C  48 2B 45 CF                     sub rax, qword ptr [rbp - 0x31]
00832550  48 3D 00 04 00 00               cmp rax, 0x400
00832556  73 0A                           jae 0x140832562
00832558  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0083255D  E9 31 04 00 00                  jmp 0x140832993
00832562  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00832566  41 B9 19 00 02 00               mov r9d, 0x20019
0083256C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00832571  41 B8 08 00 00 00               mov r8d, 8
00832577  48 8D 45 97                     lea rax, [rbp - 0x69]
0083257B  48 8B D3                        mov rdx, rbx
0083257E  49 8B CE                        mov rcx, r14
00832581  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00832586  E8 85 D2 0B 00                  call 0x1408ef810
0083258B  8B D8                           mov ebx, eax
0083258D  85 C0                           test eax, eax
0083258F  0F 88 FE 03 00 00               js 0x140832993
00832595  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00832599  48 8D 45 B7                     lea rax, [rbp - 0x49]
0083259D  41 B9 0C 00 00 00               mov r9d, 0xc
008325A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008325A8  4C 8D 45 DF                     lea r8, [rbp - 0x21]
008325AC  41 8D 51 F9                     lea edx, [r9 - 7]
008325B0  E8 DB AD E7 FF                  call 0x1406ad390
008325B5  33 DB                           xor ebx, ebx
008325B7  B9 01 00 00 00                  mov ecx, 1
008325BC  85 C0                           test eax, eax
008325BE  75 16                           jne 0x1408325d6
008325C0  F6 45 E3 02                     test byte ptr [rbp - 0x1d], 2
008325C4  74 0A                           je 0x1408325d0
008325C6  BB 2D 00 00 80                  mov ebx, 0x8000002d
008325CB  E9 C3 03 00 00                  jmp 0x140832993
008325D0  84 4D E3                        test byte ptr [rbp - 0x1d], cl
008325D3  0F 45 F9                        cmovne edi, ecx
008325D6  44 8A 75 6F                     mov r14b, byte ptr [rbp + 0x6f]
008325DA  45 84 F6                        test r14b, r14b
008325DD  74 4B                           je 0x14083262a
008325DF  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
008325E3  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
008325E7  4D 8B C7                        mov r8, r15
008325EA  BA 04 00 00 00                  mov edx, 4
008325EF  E8 00 04 00 00                  call 0x1408329f4
008325F4  3D 23 00 00 C0                  cmp eax, 0xc0000023
008325F9  75 2F                           jne 0x14083262a
008325FB  4D 85 FF                        test r15, r15
008325FE  74 0A                           je 0x14083260a
00832600  33 D2                           xor edx, edx
00832602  49 8B CF                        mov rcx, r15
00832605  E8 66 02 35 00                  call 0x140b82870
0083260A  8B 55 9F                        mov edx, dword ptr [rbp - 0x61]
0083260D  B9 00 01 00 00                  mov ecx, 0x100
00832612  41 B8 52 45 47 4C               mov r8d, 0x4c474552
00832618  E8 D3 FA 34 00                  call 0x140b820f0
0083261D  4C 8B F8                        mov r15, rax
00832620  48 85 C0                        test rax, rax
00832623  75 BA                           jne 0x1408325df
00832625  E9 EB 00 00 00                  jmp 0x140832715
0083262A  41 8A C6                        mov al, r14b
0083262D  41 B9 1F 00 06 00               mov r9d, 0x6001f
00832633  F6 D8                           neg al
00832635  44 8B C7                        mov r8d, edi
00832638  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0083263C  49 8B D5                        mov rdx, r13
0083263F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00832644  48 1B C9                        sbb rcx, rcx
00832647  49 23 CF                        and rcx, r15
0083264A  48 8D 45 A3                     lea rax, [rbp - 0x5d]
0083264E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00832653  48 8D 45 AF                     lea rax, [rbp - 0x51]
00832657  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0083265C  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00832660  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00832665  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00832669  E8 0E FA 0F 00                  call 0x14093207c
0083266E  45 33 ED                        xor r13d, r13d
00832671  8B D8                           mov ebx, eax
00832673  85 C0                           test eax, eax
00832675  0F 88 18 03 00 00               js 0x140832993
0083267B  45 84 F6                        test r14b, r14b
0083267E  74 1B                           je 0x14083269b
00832680  4D 85 FF                        test r15, r15
00832683  74 16                           je 0x14083269b
00832685  83 7D A3 02                     cmp dword ptr [rbp - 0x5d], 2
00832689  75 10                           jne 0x14083269b
0083268B  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0083268F  41 8D 55 04                     lea edx, [r13 + 4]
00832693  4D 8B C7                        mov r8, r15
00832696  E8 41 06 00 00                  call 0x140832cdc
0083269B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0083269F  48 8D 45 8F                     lea rax, [rbp - 0x71]
008326A3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008326A8  4C 8D 45 83                     lea r8, [rbp - 0x7d]
008326AC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008326B1  45 33 C9                        xor r9d, r9d
008326B4  33 D2                           xor edx, edx
008326B6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008326BB  E8 7C 1F 16 00                  call 0x14099463c
008326C0  BA FF FF FF FF                  mov edx, 0xffffffff
008326C5  85 C0                           test eax, eax
008326C7  0F 85 87 00 00 00               jne 0x140832754
008326CD  8B 45 83                        mov eax, dword ptr [rbp - 0x7d]
008326D0  3B 44 24 50                     cmp eax, dword ptr [rsp + 0x50]
008326D4  0F 46 44 24 50                  cmovbe eax, dword ptr [rsp + 0x50]
008326D9  85 C0                           test eax, eax
008326DB  74 09                           je 0x1408326e6
008326DD  8D 48 01                        lea ecx, [rax + 1]
008326E0  3B C8                           cmp ecx, eax
008326E2  72 66                           jb 0x14083274a
008326E4  8B C1                           mov eax, ecx
008326E6  8B F8                           mov edi, eax
008326E8  48 03 FF                        add rdi, rdi
008326EB  48 3B FA                        cmp rdi, rdx
008326EE  77 5A                           ja 0x14083274a
008326F0  44 8B 75 8F                     mov r14d, dword ptr [rbp - 0x71]
008326F4  41 8B DD                        mov ebx, r13d
008326F7  85 FF                           test edi, edi
008326F9  74 24                           je 0x14083271f
008326FB  8B D7                           mov edx, edi
008326FD  B9 00 01 00 00                  mov ecx, 0x100
00832702  41 B8 52 45 47 4C               mov r8d, 0x4c474552
00832708  E8 E3 F9 34 00                  call 0x140b820f0
0083270D  48 8B F0                        mov rsi, rax
00832710  48 85 C0                        test rax, rax
00832713  75 0A                           jne 0x14083271f
00832715  BB 17 00 00 C0                  mov ebx, 0xc0000017
0083271A  E9 74 02 00 00                  jmp 0x140832993
0083271F  45 85 F6                        test r14d, r14d
00832722  74 3B                           je 0x14083275f
00832724  49 8B D6                        mov rdx, r14
00832727  B9 00 01 00 00                  mov ecx, 0x100
0083272C  41 B8 52 45 47 4C               mov r8d, 0x4c474552
00832732  E8 B9 F9 34 00                  call 0x140b820f0
00832737  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
0083273B  48 85 C0                        test rax, rax
0083273E  75 1C                           jne 0x14083275c
00832740  BB 17 00 00 C0                  mov ebx, 0xc0000017
00832745  E9 3A 02 00 00                  jmp 0x140832984
0083274A  BB 95 00 00 C0                  mov ebx, 0xc0000095
0083274F  E9 3F 02 00 00                  jmp 0x140832993
00832754  41 8B FD                        mov edi, r13d
00832757  45 8B F5                        mov r14d, r13d
0083275A  EB 03                           jmp 0x14083275f
0083275C  4C 8B E0                        mov r12, rax
0083275F  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00832763  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00832767  8B C7                           mov eax, edi
00832769  4C 8B C6                        mov r8, rsi
0083276C  D1 E8                           shr eax, 1
0083276E  41 8B D5                        mov edx, r13d
00832771  89 45 8F                        mov dword ptr [rbp - 0x71], eax
00832774  E8 87 04 16 00                  call 0x140992c00
00832779  3D 1A 00 00 80                  cmp eax, 0x8000001a
0083277E  0F 84 AB 00 00 00               je 0x14083282f
00832784  3D 23 00 00 C0                  cmp eax, 0xc0000023
00832789  75 4B                           jne 0x1408327d6
0083278B  8B 7D 8F                        mov edi, dword ptr [rbp - 0x71]
0083278E  B8 FF FF FF FF                  mov eax, 0xffffffff
00832793  48 03 FF                        add rdi, rdi
00832796  48 3B F8                        cmp rdi, rax
00832799  0F 87 84 00 00 00               ja 0x140832823
0083279F  33 C0                           xor eax, eax
008327A1  8B D8                           mov ebx, eax
008327A3  48 85 F6                        test rsi, rsi
008327A6  74 0A                           je 0x1408327b2
008327A8  33 D2                           xor edx, edx
008327AA  48 8B CE                        mov rcx, rsi
008327AD  E8 BE 00 35 00                  call 0x140b82870
008327B2  8B D7                           mov edx, edi
008327B4  B9 00 01 00 00                  mov ecx, 0x100
008327B9  41 B8 52 45 47 4C               mov r8d, 0x4c474552
008327BF  E8 2C F9 34 00                  call 0x140b820f0
008327C4  48 8B F0                        mov rsi, rax
008327C7  48 85 C0                        test rax, rax
008327CA  75 93                           jne 0x14083275f
008327CC  BB 17 00 00 C0                  mov ebx, 0xc0000017
008327D1  E9 9F 01 00 00                  jmp 0x140832975
008327D6  33 C9                           xor ecx, ecx
008327D8  85 C0                           test eax, eax
008327DA  75 51                           jne 0x14083282d
008327DC  8B C7                           mov eax, edi
008327DE  4C 8B CE                        mov r9, rsi
008327E1  48 D1 E8                        shr rax, 1
008327E4  48 8B D6                        mov rdx, rsi
008327E7  66 89 4C 46 FE                  mov word ptr [rsi + rax*2 - 2], cx
008327EC  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
008327EF  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
008327F3  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
008327F7  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008327FB  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008327FF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00832804  8A 45 6F                        mov al, byte ptr [rbp + 0x6f]
00832807  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0083280B  E8 B0 FC FF FF                  call 0x1408324c0
00832810  85 C0                           test eax, eax
00832812  74 07                           je 0x14083281b
00832814  3D 2D 00 00 80                  cmp eax, 0x8000002d
00832819  75 12                           jne 0x14083282d
0083281B  41 FF C5                        inc r13d
0083281E  E9 3C FF FF FF                  jmp 0x14083275f
00832823  BB 95 00 00 C0                  mov ebx, 0xc0000095
00832828  E9 48 01 00 00                  jmp 0x140832975
0083282D  8B D8                           mov ebx, eax
0083282F  45 33 ED                        xor r13d, r13d
00832832  85 DB                           test ebx, ebx
00832834  0F 88 3B 01 00 00               js 0x140832975
0083283A  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
0083283E  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00832843  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00832848  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0083284D  4C 8D 4D 83                     lea r9, [rbp - 0x7d]
00832851  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00832855  44 8B E7                        mov r12d, edi
00832858  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0083285D  4C 8B C6                        mov r8, rsi
00832860  48 8D 45 A7                     lea rax, [rbp - 0x59]
00832864  41 D1 EC                        shr r12d, 1
00832867  41 8B D5                        mov edx, r13d
0083286A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0083286F  44 89 65 83                     mov dword ptr [rbp - 0x7d], r12d
00832873  E8 24 0E 16 00                  call 0x14099369c
00832878  3D 1A 00 00 80                  cmp eax, 0x8000001a
0083287D  0F 84 EE 00 00 00               je 0x140832971
00832883  3D 23 00 00 C0                  cmp eax, 0xc0000023
00832888  0F 85 98 00 00 00               jne 0x140832926
0083288E  44 39 65 83                     cmp dword ptr [rbp - 0x7d], r12d
00832892  76 47                           jbe 0x1408328db
00832894  8B 7D 83                        mov edi, dword ptr [rbp - 0x7d]
00832897  B8 FF FF FF FF                  mov eax, 0xffffffff
0083289C  48 03 FF                        add rdi, rdi
0083289F  48 3B F8                        cmp rdi, rax
008328A2  0F 87 39 01 00 00               ja 0x1408329e1
008328A8  45 33 E4                        xor r12d, r12d
008328AB  41 8B DC                        mov ebx, r12d
008328AE  48 85 F6                        test rsi, rsi
008328B1  74 0A                           je 0x1408328bd
008328B3  33 D2                           xor edx, edx
008328B5  48 8B CE                        mov rcx, rsi
008328B8  E8 B3 FF 34 00                  call 0x140b82870
008328BD  8B D7                           mov edx, edi
008328BF  B9 00 01 00 00                  mov ecx, 0x100
008328C4  41 B8 52 45 47 4C               mov r8d, 0x4c474552
008328CA  E8 21 F8 34 00                  call 0x140b820f0
008328CF  48 8B F0                        mov rsi, rax
008328D2  48 85 C0                        test rax, rax
008328D5  0F 84 91 00 00 00               je 0x14083296c
008328DB  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
008328DF  44 39 74 24 50                  cmp dword ptr [rsp + 0x50], r14d
008328E4  0F 86 54 FF FF FF               jbe 0x14083283e
008328EA  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
008328EF  4C 8B E0                        mov r12, rax
008328F2  48 85 C0                        test rax, rax
008328F5  74 0A                           je 0x140832901
008328F7  33 D2                           xor edx, edx
008328F9  48 8B C8                        mov rcx, rax
008328FC  E8 6F FF 34 00                  call 0x140b82870
00832901  49 8B D6                        mov rdx, r14
00832904  B9 00 01 00 00                  mov ecx, 0x100
00832909  41 B8 52 45 47 4C               mov r8d, 0x4c474552
0083290F  E8 DC F7 34 00                  call 0x140b820f0
00832914  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00832918  48 85 C0                        test rax, rax
0083291B  0F 85 1D FF FF FF               jne 0x14083283e
00832921  E9 1A FE FF FF                  jmp 0x140832740
00832926  4C 8B 65 87                     mov r12, qword ptr [rbp - 0x79]
0083292A  33 C9                           xor ecx, ecx
0083292C  85 C0                           test eax, eax
0083292E  0F 85 B4 00 00 00               jne 0x1408329e8
00832934  44 8B 45 A7                     mov r8d, dword ptr [rbp - 0x59]
00832938  4D 8B CC                        mov r9, r12
0083293B  8B C7                           mov eax, edi
0083293D  48 8B D6                        mov rdx, rsi
00832940  48 D1 E8                        shr rax, 1
00832943  66 89 4C 46 FE                  mov word ptr [rsi + rax*2 - 2], cx
00832948  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0083294C  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00832950  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00832954  E8 CF F1 15 00                  call 0x140991b28
00832959  85 C0                           test eax, eax
0083295B  0F 85 87 00 00 00               jne 0x1408329e8
00832961  41 FF C5                        inc r13d
00832964  49 8B C4                        mov rax, r12
00832967  E9 D2 FE FF FF                  jmp 0x14083283e
0083296C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00832971  4C 8B 65 87                     mov r12, qword ptr [rbp - 0x79]
00832975  4D 85 E4                        test r12, r12
00832978  74 0A                           je 0x140832984
0083297A  33 D2                           xor edx, edx
0083297C  49 8B CC                        mov rcx, r12
0083297F  E8 EC FE 34 00                  call 0x140b82870
00832984  48 85 F6                        test rsi, rsi
00832987  74 0A                           je 0x140832993
00832989  33 D2                           xor edx, edx
0083298B  48 8B CE                        mov rcx, rsi
0083298E  E8 DD FE 34 00                  call 0x140b82870
00832993  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00832997  48 85 C9                        test rcx, rcx
0083299A  74 05                           je 0x1408329a1
0083299C  E8 0F A9 E7 FF                  call 0x1406ad2b0
008329A1  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
008329A5  48 85 C9                        test rcx, rcx
008329A8  74 05                           je 0x1408329af
008329AA  E8 01 A9 E7 FF                  call 0x1406ad2b0
008329AF  4D 85 FF                        test r15, r15
008329B2  74 0A                           je 0x1408329be
008329B4  33 D2                           xor edx, edx
008329B6  49 8B CF                        mov rcx, r15
008329B9  E8 B2 FE 34 00                  call 0x140b82870
008329BE  8B C3                           mov eax, ebx
008329C0  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
008329C4  48 33 CC                        xor rcx, rsp
008329C7  E8 74 9C E7 FF                  call 0x1406ac640
008329CC  48 81 C4 D8 00 00 00            add rsp, 0xd8
008329D3  41 5F                           pop r15
008329D5  41 5E                           pop r14
008329D7  41 5D                           pop r13
008329D9  41 5C                           pop r12
008329DB  5F                              pop rdi
008329DC  5E                              pop rsi
008329DD  5B                              pop rbx
008329DE  5D                              pop rbp
008329DF  C3                              ret
008329E0  CC                              int3
008329E1  BB 95 00 00 C0                  mov ebx, 0xc0000095
008329E6  EB 89                           jmp 0x140832971
008329E8  8B D8                           mov ebx, eax
008329EA  EB 89                           jmp 0x140832975
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RegRtlCopyTreeInternal(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int8 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (216);
    result = (*(unsigned __int64 *)(v_rip + 6128224)) ^ (v_rsp);
    v_stack_m58 = result;
    a1 = 0;
    v_stack_m88 = a6;
    result = 0;
    v_stack_mB0 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_mC4 = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mC0 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m70 = a3;
    result = IoGetStackLimits(v_stack_m78, v_stack_m80, a3, a4);
    result = (v_stack_m80) - (v_stack_m78);
    if (result >= 0x400ULL) goto loc_00832562;
    goto loc_00832993;
loc_00832562:
    v_stack_mF0 = v_stack_m88;
    v_stack_mF8 = v_stack_mB0;
    result = _RegRtlOpenKeyTransacted(0, (unsigned int)(0xC000009AULL), 8, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00832993;
    v_stack_mF8 = v_stack_m90;
    result = ZwQueryKey(v_stack_mB0, 12 - 7, v_stack_m68, 12);
    v_rbx = 0;
    if ((unsigned int)(result) != 0) goto loc_008325D6;
    if (((v_stack_m64) & (2)) == 0) goto loc_008325D0;
    goto loc_00832993;
loc_008325D0:
    v_rdi = 0;
    if (((v_stack_m64) & (1)) != 0) { v_rdi = 1; }
loc_008325D6:
    if (a5 == 0) goto loc_0083262A;
loc_008325DF:
    result = RegRtlGetKeySecurity(v_stack_mB0, 4, 0, v_stack_mA8);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0083262A;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 0, v_stack_mA8);
    }
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mA8), (unsigned int)(0x4C474552ULL), v_stack_mA8);
    if (result != 0) goto loc_008325DF;
    goto loc_00832715;
loc_0083262A:
    result = (unsigned __int8)(-(a5));
    v_stack_mD8 = v_stack_m88;
    a1 = (256) & (result);
    v_stack_mE0 = v_stack_mA4;
    v_stack_mE8 = v_stack_m98;
    v_stack_mF0 = (unsigned __int8)((unsigned int)(0x8000002DULL));
    v_stack_mF8 = a1;
    result = RegRtlCreateKeyTransacted(v_stack_m70, a4, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x6001FULL));
    v_r13 = 0;
    if (sign_flag) goto loc_00832993;
    if (a5 == 0) goto loc_0083269B;
    if (result == 0) goto loc_0083269B;
    if (v_stack_mA4 == 2) {
        a1 = v_stack_m98;
        a2 = v_r13 + 4;
        a3 = result;
        result = RegRtlSetKeySecurity(a1, a2, a3, (unsigned int)(0x6001FULL));
    }
    v_stack_mF0 = v_stack_mB8;
    a4 = 0;
    a2 = 0;
    v_stack_mF8 = v_stack_mC8;
    result = RegRtlQueryInfoKey(v_stack_mB0, a2, v_stack_mC4, a4);
    if ((unsigned int)(result) != 0) goto loc_00832754;
    result = (unsigned int)(v_stack_mC4);
    if (((unsigned int)((unsigned int)(v_stack_mC4))) <= v_stack_mC8) { result = v_stack_mC8; }
    if ((unsigned int)(result) == 0) goto loc_008326E6;
    if (((unsigned int)(result + 1)) < ((unsigned int)(result))) goto loc_0083274A;
loc_008326E6:
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 1))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 1)))));
    if (v_rdi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0083274A;
    if ((unsigned int)(v_rdi) == 0) goto loc_0083271F;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x4C474552ULL), a4);
    if (result != 0) goto loc_0083271F;
loc_00832715:
    goto loc_00832993;
loc_0083271F:
    if ((unsigned int)((unsigned int)(v_stack_mB8)) == 0) goto loc_0083275F;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mB8), (unsigned int)(0x4C474552ULL), a4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_0083275C;
loc_00832740:
    goto loc_00832984;
loc_0083274A:
    goto loc_00832993;
loc_00832754:
    goto loc_0083275F;
loc_0083275C:
loc_0083275F:
    result = (unsigned int)((0) >> (1));
    v_stack_mB8 = (unsigned int)(result);
    result = RegRtlEnumKey(v_stack_mB0, 0, result, v_stack_mB8);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_0083282F;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_008327D6;
    v_rdi = ((unsigned int)(v_stack_mB8)) + ((unsigned int)(v_stack_mB8));
    if (v_rdi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00832823;
    result = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, result, v_stack_mB8);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x4C474552ULL), v_stack_mB8);
    if (result != 0) goto loc_0083275F;
    goto loc_00832975;
loc_008327D6:
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_0083282D;
    result = ((unsigned int)((unsigned int)(v_rdi))) >> (1);
    *(unsigned __int16 *)(result + result * 2 - 2) = 0;
    v_stack_mE8 = a7;
    v_stack_mF0 = v_stack_m88;
    v_stack_mF8 = a5;
    result = RegRtlCopyTreeInternal(v_stack_mB0, result, v_stack_m98, result);
    if ((unsigned int)(result) == 0) goto loc_0083281B;
    if (((unsigned int)(result)) != 0x8000002DULL) goto loc_0083282D;
loc_0083281B:
    v_r13 = (unsigned int)((v_r13) + 1);
    goto loc_0083275F;
loc_00832823:
    goto loc_00832975;
loc_0083282D:
loc_0083282F:
    v_r13 = 0;
    if (sign_flag) goto loc_00832975;
loc_0083283E:
    v_stack_mC8 = 0;
    v_stack_mE8 = v_stack_mC8;
    v_stack_mF0 = v_stack_mC0;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (1));
    v_stack_mF8 = v_stack_mA0;
    v_stack_mC4 = (unsigned int)(v_r12);
    result = RegRtlEnumValue(v_stack_mB0, 0, result, v_stack_mC4);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_00832971;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00832926;
    if (v_stack_mC4 <= ((unsigned int)(v_r12))) goto loc_008328DB;
    v_rdi = ((unsigned int)(v_stack_mC4)) + ((unsigned int)(v_stack_mC4));
    if (v_rdi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_008329E1;
    v_r12 = 0;
    result = (unsigned int)(0xFFFFFFFFULL);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, v_stack_mC4);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x4C474552ULL), v_stack_mC4);
    if (result == 0) goto loc_0083296C;
loc_008328DB:
    if (v_stack_mC8 <= 0) goto loc_0083283E;
    result = v_stack_mC0;
    if (v_stack_mC0 != 0) {
        a2 = 0;
        a1 = v_stack_mC0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x4C474552ULL), v_stack_mC4);
    }
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mC8), (unsigned int)(0x4C474552ULL), v_stack_mC4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_0083283E;
    goto loc_00832740;
loc_00832926:
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_008329E8;
    result = ((unsigned int)((unsigned int)(v_rdi))) >> (1);
    *(unsigned __int16 *)(result + result * 2 - 2) = 0;
    v_stack_mF8 = (unsigned int)((unsigned int)(v_stack_mC8));
    result = RegRtlSetValue(v_stack_m98, result, (unsigned int)(v_stack_mA0), v_stack_mC0);
    if ((unsigned int)(result) != 0) goto loc_008329E8;
    v_r13 = (unsigned int)((v_r13) + 1);
    goto loc_0083283E;
loc_0083296C:
loc_00832971:
loc_00832975:
    result = v_stack_mC0;
    if (v_stack_mC0 != 0) {
        a2 = 0;
        a1 = v_stack_mC0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    }
    if (v_stack_mB0 != 0) {
        result = ZwClose(v_stack_mB0, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    }
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(v_stack_mA0), v_stack_mC0);
    v_rsp = (v_rsp) + (216);
    return result;
loc_008329E1:
    goto loc_00832971;
loc_008329E8:
    goto loc_00832975;
}
```

## 5. (Beta) C Style

```c
int64_t RegRtlCopyTreeInternal(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6, uint8_t Arg7)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint8_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (216);
    result = (*(uint64_t *)(v_rip + 0x5D8260)) ^ (local_rsp);
    v_stack_m58 = result;
    Arg1 = 0;
    v_stack_m88 = Arg6;
    result = 0;
    v_stack_mB0 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_mC4 = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mC0 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m70 = Arg3;
    result = IoGetStackLimits(v_stack_m78, v_stack_m80, Arg3, Arg4);
    result = (v_stack_m80) - (v_stack_m78);
    if (result >= 0x400ULL) goto loc_00832562;
    goto loc_00832993;
loc_00832562:
    v_stack_mF0 = v_stack_m88;
    v_stack_mF8 = v_stack_mB0;
    result = _RegRtlOpenKeyTransacted(0, (uint32_t)(0xC000009AULL), 8, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00832993;
    v_stack_mF8 = v_stack_m90;
    result = ZwQueryKey(v_stack_mB0, 12 - 7, v_stack_m68, 12);
    local_rbx = 0;
    if ((uint32_t)(result) != 0) goto loc_008325D6;
    if (((v_stack_m64) & (2)) == 0) goto loc_008325D0;
    goto loc_00832993;
loc_008325D0:
    local_rdi = 0;
    if (((v_stack_m64) & (1)) != 0) { local_rdi = 1; }
loc_008325D6:
    if (Arg5 == 0) goto loc_0083262A;
loc_008325DF:
    result = RegRtlGetKeySecurity(v_stack_mB0, 4, 0, v_stack_mA8);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0083262A;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, v_stack_mA8);
    }
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mA8), (uint32_t)(0x4C474552ULL), v_stack_mA8);
    if (result != 0) goto loc_008325DF;
    goto loc_00832715;
loc_0083262A:
    result = (uint8_t)(-(Arg5));
    v_stack_mD8 = v_stack_m88;
    Arg1 = (256) & (result);
    v_stack_mE0 = v_stack_mA4;
    v_stack_mE8 = v_stack_m98;
    v_stack_mF0 = (uint8_t)((uint32_t)(0x8000002DULL));
    v_stack_mF8 = Arg1;
    result = RegRtlCreateKeyTransacted(v_stack_m70, Arg4, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x6001FULL));
    local_r13 = 0;
    if (sign_flag) goto loc_00832993;
    if (Arg5 == 0) goto loc_0083269B;
    if (result == 0) goto loc_0083269B;
    if (v_stack_mA4 == 2) {
        Arg1 = v_stack_m98;
        Arg2 = local_r13 + 4;
        Arg3 = result;
        result = RegRtlSetKeySecurity(Arg1, Arg2, Arg3, (uint32_t)(0x6001FULL));
    }
    v_stack_mF0 = v_stack_mB8;
    Arg4 = 0;
    Arg2 = 0;
    v_stack_mF8 = v_stack_mC8;
    result = RegRtlQueryInfoKey(v_stack_mB0, Arg2, v_stack_mC4, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00832754;
    result = (uint32_t)(v_stack_mC4);
    if (((uint32_t)((uint32_t)(v_stack_mC4))) <= v_stack_mC8) { result = v_stack_mC8; }
    if ((uint32_t)(result) == 0) goto loc_008326E6;
    if (((uint32_t)(result + 1)) < ((uint32_t)(result))) goto loc_0083274A;
loc_008326E6:
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 1))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 1)))));
    if (local_rdi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0083274A;
    if ((uint32_t)(local_rdi) == 0) goto loc_0083271F;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x4C474552ULL), Arg4);
    if (result != 0) goto loc_0083271F;
loc_00832715:
    goto loc_00832993;
loc_0083271F:
    if ((uint32_t)((uint32_t)(v_stack_mB8)) == 0) goto loc_0083275F;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mB8), (uint32_t)(0x4C474552ULL), Arg4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_0083275C;
loc_00832740:
    goto loc_00832984;
loc_0083274A:
    goto loc_00832993;
loc_00832754:
    goto loc_0083275F;
loc_0083275C:
loc_0083275F:
    result = (uint32_t)((0) >> (1));
    v_stack_mB8 = (uint32_t)(result);
    result = RegRtlEnumKey(v_stack_mB0, 0, result, v_stack_mB8);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_0083282F;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_008327D6;
    local_rdi = ((uint32_t)(v_stack_mB8)) + ((uint32_t)(v_stack_mB8));
    if (local_rdi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00832823;
    result = 0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, result, v_stack_mB8);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x4C474552ULL), v_stack_mB8);
    if (result != 0) goto loc_0083275F;
    goto loc_00832975;
loc_008327D6:
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_0083282D;
    result = ((uint32_t)((uint32_t)(local_rdi))) >> (1);
    *(uint16_t *)(result + result * 2 - 0x2) = 0;
    v_stack_mE8 = Arg7;
    v_stack_mF0 = v_stack_m88;
    v_stack_mF8 = Arg5;
    result = RegRtlCopyTreeInternal(v_stack_mB0, result, v_stack_m98, result);
    if ((uint32_t)(result) == 0) goto loc_0083281B;
    if (((uint32_t)(result)) != 0x8000002DULL) goto loc_0083282D;
loc_0083281B:
    local_r13 = (uint32_t)((local_r13) + 1);
    goto loc_0083275F;
loc_00832823:
    goto loc_00832975;
loc_0083282D:
loc_0083282F:
    local_r13 = 0;
    if (sign_flag) goto loc_00832975;
loc_0083283E:
    v_stack_mC8 = 0;
    v_stack_mE8 = v_stack_mC8;
    v_stack_mF0 = v_stack_mC0;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (1));
    v_stack_mF8 = v_stack_mA0;
    v_stack_mC4 = (uint32_t)(local_r12);
    result = RegRtlEnumValue(v_stack_mB0, 0, result, v_stack_mC4);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_00832971;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00832926;
    if (v_stack_mC4 <= ((uint32_t)(local_r12))) goto loc_008328DB;
    local_rdi = ((uint32_t)(v_stack_mC4)) + ((uint32_t)(v_stack_mC4));
    if (local_rdi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_008329E1;
    local_r12 = 0;
    result = (uint32_t)(0xFFFFFFFFULL);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, v_stack_mC4);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x4C474552ULL), v_stack_mC4);
    if (result == 0) goto loc_0083296C;
loc_008328DB:
    if (v_stack_mC8 <= 0) goto loc_0083283E;
    result = v_stack_mC0;
    if (v_stack_mC0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mC0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x4C474552ULL), v_stack_mC4);
    }
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mC8), (uint32_t)(0x4C474552ULL), v_stack_mC4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_0083283E;
    goto loc_00832740;
loc_00832926:
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_008329E8;
    result = ((uint32_t)((uint32_t)(local_rdi))) >> (1);
    *(uint16_t *)(result + result * 2 - 0x2) = 0;
    v_stack_mF8 = (uint32_t)((uint32_t)(v_stack_mC8));
    result = RegRtlSetValue(v_stack_m98, result, (uint32_t)(v_stack_mA0), v_stack_mC0);
    if ((uint32_t)(result) != 0) goto loc_008329E8;
    local_r13 = (uint32_t)((local_r13) + 1);
    goto loc_0083283E;
loc_0083296C:
loc_00832971:
loc_00832975:
    result = v_stack_mC0;
    if (v_stack_mC0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mC0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    }
    if (v_stack_mB0 != 0) {
        result = ZwClose(v_stack_mB0, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    }
    if (v_stack_m98 != 0) {
        result = ZwClose(v_stack_m98, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    }
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(v_stack_mA0), v_stack_mC0);
    local_rsp = (local_rsp) + (216);
    return result;
loc_008329E1:
    goto loc_00832971;
loc_008329E8:
    goto loc_00832975;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008324C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
