# BiConvertElementToRegistryData

- RVA: `0x00A400A8`–`0x00A404D4` (길이 `1,068` bytes)
- VA: `0x0000000140A400A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE930`
- 디코드: `294`개 명령, `1,068/1,068` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A40132` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A4014C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A401AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A4022A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A4023F` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00A4025D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00A40283` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A402B7` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00A402D6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A402F2` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00A40333` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A40369` → [BiConvertQualifiedPartitionToBootEnvironment](BiConvertQualifiedPartitionToBootEnvironment_function_00A41684.md) (function, `0x00A41684`)
- `0x00A4039C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A403C1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A403D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A40403` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A40425` → [BiConvertNtDeviceToBootEnvironment](BiConvertNtDeviceToBootEnvironment_function_00A41760.md) (function, `0x00A41760`)
- `0x00A4044D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A40463` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A40498` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x00A404CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [BcdSetElementDataWithFlags](../A3/BcdSetElementDataWithFlags_function_00A3F080.md) at `0x00A3F197`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00A40132` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A4014C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A401AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A4022A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A4025D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00A40283` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A402D6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A402F2` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00A40333` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A4039C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A403C1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A403D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A40403` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A4044D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A40463` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A404CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A400A8  48 8B C4                        mov rax, rsp
00A400AB  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A400AF  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00A400B3  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00A400B7  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00A400BB  55                              push rbp
00A400BC  41 54                           push r12
00A400BE  41 55                           push r13
00A400C0  41 56                           push r14
00A400C2  41 57                           push r15
00A400C4  48 8B EC                        mov rbp, rsp
00A400C7  48 83 EC 40                     sub rsp, 0x40
00A400CB  C1 E9 18                        shr ecx, 0x18
00A400CE  4C 8B EA                        mov r13, rdx
00A400D1  33 D2                           xor edx, edx
00A400D3  45 8B F0                        mov r14d, r8d
00A400D6  83 E1 0F                        and ecx, 0xf
00A400D9  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
00A400DD  0F 57 C0                        xorps xmm0, xmm0
00A400E0  8B FA                           mov edi, edx
00A400E2  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00A400E6  83 E9 01                        sub ecx, 1
00A400E9  0F 84 65 02 00 00               je 0x140a40354
00A400EF  83 E9 01                        sub ecx, 1
00A400F2  75 72                           jne 0x140a40166
00A400F4  44 8D 62 01                     lea r12d, [rdx + 1]
00A400F8  45 84 F4                        test r12b, r14b
00A400FB  0F 85 7C 03 00 00               jne 0x140a4047d
00A40101  41 8B C6                        mov eax, r14d
00A40104  49 8B CD                        mov rcx, r13
00A40107  D1 E8                           shr eax, 1
00A40109  85 C0                           test eax, eax
00A4010B  0F 84 2C 02 00 00               je 0x140a4033d
00A40111  66 39 11                        cmp word ptr [rcx], dx
00A40114  74 08                           je 0x140a4011e
00A40116  48 83 C1 02                     add rcx, 2
00A4011A  FF C8                           dec eax
00A4011C  EB EB                           jmp 0x140a40109
00A4011E  45 8B FE                        mov r15d, r14d
00A40121  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A40127  41 8B D7                        mov edx, r15d
00A4012A  B9 02 01 00 00                  mov ecx, 0x102
00A4012F  41 8B DF                        mov ebx, r15d
00A40132  E8 B9 1F 14 00                  call 0x140b820f0
00A40137  48 8B F0                        mov rsi, rax
00A4013A  48 85 C0                        test rax, rax
00A4013D  0F 84 2A 03 00 00               je 0x140a4046d
00A40143  4D 8B C6                        mov r8, r14
00A40146  49 8B D5                        mov rdx, r13
00A40149  48 8B C8                        mov rcx, rax
00A4014C  E8 EF 66 C8 FF                  call 0x1406c6840
00A40151  33 C0                           xor eax, eax
00A40153  45 84 E4                        test r12b, r12b
00A40156  0F 85 B9 01 00 00               jne 0x140a40315
00A4015C  66 89 44 33 FE                  mov word ptr [rbx + rsi - 2], ax
00A40161  E9 AF 01 00 00                  jmp 0x140a40315
00A40166  83 E9 01                        sub ecx, 1
00A40169  0F 84 18 03 00 00               je 0x140a40487
00A4016F  83 E9 01                        sub ecx, 1
00A40172  0F 84 8E 00 00 00               je 0x140a40206
00A40178  83 E9 01                        sub ecx, 1
00A4017B  0F 84 65 02 00 00               je 0x140a403e6
00A40181  83 E9 01                        sub ecx, 1
00A40184  0F 85 AD 02 00 00               jne 0x140a40437
00A4018A  41 8D 46 FF                     lea eax, [r14 - 1]
00A4018E  44 8D 61 01                     lea r12d, [rcx + 1]
00A40192  41 3B C4                        cmp eax, r12d
00A40195  0F 87 E2 02 00 00               ja 0x140a4047d
00A4019B  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A401A1  41 8B D4                        mov edx, r12d
00A401A4  B9 02 01 00 00                  mov ecx, 0x102
00A401A9  45 8B FC                        mov r15d, r12d
00A401AC  E8 3F 1F 14 00                  call 0x140b820f0
00A401B1  33 DB                           xor ebx, ebx
00A401B3  48 8B F0                        mov rsi, rax
00A401B6  48 85 C0                        test rax, rax
00A401B9  0F 84 AE 02 00 00               je 0x140a4046d
00A401BF  41 38 5D 00                     cmp byte ptr [r13], bl
00A401C3  0F 95 C0                        setne al
00A401C6  88 06                           mov byte ptr [rsi], al
00A401C8  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00A401CC  8B FB                           mov edi, ebx
00A401CE  48 89 30                        mov qword ptr [rax], rsi
00A401D1  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00A401D5  44 89 38                        mov dword ptr [rax], r15d
00A401D8  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A401DC  48 85 C9                        test rcx, rcx
00A401DF  0F 85 E0 02 00 00               jne 0x140a404c5
00A401E5  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
00A401EA  8B C7                           mov eax, edi
00A401EC  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00A401F0  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00A401F4  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00A401F8  49 8B E3                        mov rsp, r11
00A401FB  41 5F                           pop r15
00A401FD  41 5E                           pop r14
00A401FF  41 5D                           pop r13
00A40201  41 5C                           pop r12
00A40203  5D                              pop rbp
00A40204  C3                              ret
00A40205  CC                              int3
00A40206  41 F6 C6 0F                     test r14b, 0xf
00A4020A  0F 85 6D 02 00 00               jne 0x140a4047d
00A40210  41 C1 EE 04                     shr r14d, 4
00A40214  44 8B FA                        mov r15d, edx
00A40217  8B DA                           mov ebx, edx
00A40219  41 BC 01 00 00 00               mov r12d, 1
00A4021F  45 85 F6                        test r14d, r14d
00A40222  74 4D                           je 0x140a40271
00A40224  33 D2                           xor edx, edx
00A40226  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00A4022A  E8 51 A5 9E FF                  call 0x14042a780
00A4022F  8B CB                           mov ecx, ebx
00A40231  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00A40235  48 C1 E1 04                     shl rcx, 4
00A40239  45 8A C4                        mov r8b, r12b
00A4023C  49 03 CD                        add rcx, r13
00A4023F  E8 0C 52 ED FF                  call 0x140915450
00A40244  8B F8                           mov edi, eax
00A40246  85 C0                           test eax, eax
00A40248  78 8E                           js 0x140a401d8
00A4024A  0F B7 4D F0                     movzx ecx, word ptr [rbp - 0x10]
00A4024E  83 C1 02                        add ecx, 2
00A40251  44 03 F9                        add r15d, ecx
00A40254  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00A40258  48 85 C9                        test rcx, rcx
00A4025B  74 0C                           je 0x140a40269
00A4025D  E8 EE 25 14 00                  call 0x140b82850
00A40262  0F 57 C0                        xorps xmm0, xmm0
00A40265  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00A40269  41 03 DC                        add ebx, r12d
00A4026C  41 3B DE                        cmp ebx, r14d
00A4026F  72 B3                           jb 0x140a40224
00A40271  41 83 C7 02                     add r15d, 2
00A40275  B9 02 01 00 00                  mov ecx, 0x102
00A4027A  41 8B D7                        mov edx, r15d
00A4027D  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A40283  E8 68 1E 14 00                  call 0x140b820f0
00A40288  48 8B F0                        mov rsi, rax
00A4028B  48 85 C0                        test rax, rax
00A4028E  0F 84 D9 01 00 00               je 0x140a4046d
00A40294  33 D2                           xor edx, edx
00A40296  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A4029A  89 55 48                        mov dword ptr [rbp + 0x48], edx
00A4029D  48 8B C8                        mov rcx, rax
00A402A0  8B C2                           mov eax, edx
00A402A2  45 85 F6                        test r14d, r14d
00A402A5  74 69                           je 0x140a40310
00A402A7  8B C8                           mov ecx, eax
00A402A9  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00A402AD  48 C1 E1 04                     shl rcx, 4
00A402B1  45 8A C4                        mov r8b, r12b
00A402B4  49 03 CD                        add rcx, r13
00A402B7  E8 94 51 ED FF                  call 0x140915450
00A402BC  8B F8                           mov edi, eax
00A402BE  85 C0                           test eax, eax
00A402C0  78 69                           js 0x140a4032b
00A402C2  0F B7 45 F0                     movzx eax, word ptr [rbp - 0x10]
00A402C6  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
00A402CA  83 C0 02                        add eax, 2
00A402CD  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A402D1  44 8B C0                        mov r8d, eax
00A402D4  8B D8                           mov ebx, eax
00A402D6  E8 65 65 C8 FF                  call 0x1406c6840
00A402DB  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A402DF  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00A402E3  48 03 CB                        add rcx, rbx
00A402E6  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00A402EA  48 85 C0                        test rax, rax
00A402ED  74 13                           je 0x140a40302
00A402EF  48 8B C8                        mov rcx, rax
00A402F2  E8 59 25 14 00                  call 0x140b82850
00A402F7  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00A402FB  0F 57 C0                        xorps xmm0, xmm0
00A402FE  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00A40302  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
00A40305  41 03 C4                        add eax, r12d
00A40308  89 45 48                        mov dword ptr [rbp + 0x48], eax
00A4030B  41 3B C6                        cmp eax, r14d
00A4030E  72 97                           jb 0x140a402a7
00A40310  33 C0                           xor eax, eax
00A40312  66 89 01                        mov word ptr [rcx], ax
00A40315  33 DB                           xor ebx, ebx
00A40317  48 8B C6                        mov rax, rsi
00A4031A  85 FF                           test edi, edi
00A4031C  0F 89 A6 FE FF FF               jns 0x140a401c8
00A40322  48 85 C0                        test rax, rax
00A40325  0F 84 AD FE FF FF               je 0x140a401d8
00A4032B  BA 42 43 44 4B                  mov edx, 0x4b444342
00A40330  48 8B CE                        mov rcx, rsi
00A40333  E8 38 25 14 00                  call 0x140b82870
00A40338  E9 9B FE FF FF                  jmp 0x140a401d8
00A4033D  45 8D 7E 02                     lea r15d, [r14 + 2]
00A40341  45 3B FE                        cmp r15d, r14d
00A40344  0F 83 E5 00 00 00               jae 0x140a4042f
00A4034A  BF 95 00 00 C0                  mov edi, 0xc0000095
00A4034F  E9 91 FE FF FF                  jmp 0x140a401e5
00A40354  41 83 7D 00 06                  cmp dword ptr [r13], 6
00A40359  41 8B D6                        mov edx, r14d
00A4035C  49 8B CD                        mov rcx, r13
00A4035F  0F 85 B9 00 00 00               jne 0x140a4041e
00A40365  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00A40369  E8 16 13 00 00                  call 0x140a41684
00A4036E  8B F8                           mov edi, eax
00A40370  85 C0                           test eax, eax
00A40372  0F 88 60 FE FF FF               js 0x140a401d8
00A40378  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
00A4037C  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A4037F  83 C0 10                        add eax, 0x10
00A40382  44 8B F8                        mov r15d, eax
00A40385  83 F8 10                        cmp eax, 0x10
00A40388  0F 82 2D 01 00 00               jb 0x140a404bb
00A4038E  41 8B D7                        mov edx, r15d
00A40391  B9 02 01 00 00                  mov ecx, 0x102
00A40396  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A4039C  E8 4F 1D 14 00                  call 0x140b820f0
00A403A1  48 8B F0                        mov rsi, rax
00A403A4  48 85 C0                        test rax, rax
00A403A7  0F 84 C0 00 00 00               je 0x140a4046d
00A403AD  41 0F 10 45 04                  movups xmm0, xmmword ptr [r13 + 4]
00A403B2  48 8D 48 10                     lea rcx, [rax + 0x10]
00A403B6  48 8B D3                        mov rdx, rbx
00A403B9  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00A403BD  44 8B 43 08                     mov r8d, dword ptr [rbx + 8]
00A403C1  E8 7A 64 C8 FF                  call 0x1406c6840
00A403C6  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00A403CA  48 85 C9                        test rcx, rcx
00A403CD  74 10                           je 0x140a403df
00A403CF  BA 42 43 44 4B                  mov edx, 0x4b444342
00A403D4  E8 97 24 14 00                  call 0x140b82870
00A403D9  33 C0                           xor eax, eax
00A403DB  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00A403DF  33 DB                           xor ebx, ebx
00A403E1  E9 E2 FD FF FF                  jmp 0x140a401c8
00A403E6  41 BF 08 00 00 00               mov r15d, 8
00A403EC  45 3B F7                        cmp r14d, r15d
00A403EF  0F 85 88 00 00 00               jne 0x140a4047d
00A403F5  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A403FB  41 8B D7                        mov edx, r15d
00A403FE  B9 02 01 00 00                  mov ecx, 0x102
00A40403  E8 E8 1C 14 00                  call 0x140b820f0
00A40408  33 DB                           xor ebx, ebx
00A4040A  48 8B F0                        mov rsi, rax
00A4040D  48 85 C0                        test rax, rax
00A40410  74 5B                           je 0x140a4046d
00A40412  49 8B 45 00                     mov rax, qword ptr [r13]
00A40416  48 89 06                        mov qword ptr [rsi], rax
00A40419  E9 AA FD FF FF                  jmp 0x140a401c8
00A4041E  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00A40422  45 33 C0                        xor r8d, r8d
00A40425  E8 36 13 00 00                  call 0x140a41760
00A4042A  E9 3F FF FF FF                  jmp 0x140a4036e
00A4042F  44 8A E2                        mov r12b, dl
00A40432  E9 EA FC FF FF                  jmp 0x140a40121
00A40437  83 F9 01                        cmp ecx, 1
00A4043A  74 3B                           je 0x140a40477
00A4043C  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00A40442  49 8B D6                        mov rdx, r14
00A40445  B9 02 01 00 00                  mov ecx, 0x102
00A4044A  45 8B FE                        mov r15d, r14d
00A4044D  E8 9E 1C 14 00                  call 0x140b820f0
00A40452  48 8B F0                        mov rsi, rax
00A40455  48 85 C0                        test rax, rax
00A40458  74 13                           je 0x140a4046d
00A4045A  4D 8B C6                        mov r8, r14
00A4045D  49 8B D5                        mov rdx, r13
00A40460  48 8B C8                        mov rcx, rax
00A40463  E8 D8 63 C8 FF                  call 0x1406c6840
00A40468  E9 72 FF FF FF                  jmp 0x140a403df
00A4046D  BF 17 00 00 C0                  mov edi, 0xc0000017
00A40472  E9 61 FD FF FF                  jmp 0x140a401d8
00A40477  41 F6 C6 07                     test r14b, 7
00A4047B  74 BF                           je 0x140a4043c
00A4047D  BF 24 00 00 C0                  mov edi, 0xc0000024
00A40482  E9 5E FD FF FF                  jmp 0x140a401e5
00A40487  41 83 FE 10                     cmp r14d, 0x10
00A4048B  75 F0                           jne 0x140a4047d
00A4048D  45 8D 46 F1                     lea r8d, [r14 - 0xf]
00A40491  49 8B CD                        mov rcx, r13
00A40494  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00A40498  E8 B3 4F ED FF                  call 0x140915450
00A4049D  33 DB                           xor ebx, ebx
00A4049F  8B F8                           mov edi, eax
00A404A1  85 C0                           test eax, eax
00A404A3  0F 88 2F FD FF FF               js 0x140a401d8
00A404A9  44 0F B7 7D F0                  movzx r15d, word ptr [rbp - 0x10]
00A404AE  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00A404B2  41 83 C7 02                     add r15d, 2
00A404B6  E9 0D FD FF FF                  jmp 0x140a401c8
00A404BB  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A404C0  E9 13 FD FF FF                  jmp 0x140a401d8
00A404C5  BA 42 43 44 4B                  mov edx, 0x4b444342
00A404CA  E8 A1 23 14 00                  call 0x140b82870
00A404CF  E9 11 FD FF FF                  jmp 0x140a401e5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiConvertElementToRegistryData(int a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (64);
    a1 = (unsigned int)((a1) >> (24));
    a2 = 0;
    a1 = (unsigned int)((a1) & (15));
    v_stack_m48 = 0;
    v_stack_m38 = v_xmm0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A40354;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00A40166;
    if ((((unsigned __int8)(a2 + 1)) & ((unsigned __int8)((unsigned int)(a3)))) != 0) goto loc_00A4047D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (1));
loc_00A40109:
    if ((unsigned int)(result) == 0) goto loc_00A4033D;
    if ((*(unsigned __int16 *)(0)) == 0) goto loc_00A4011E;
    a1 = (0) + (2);
    result = (unsigned int)((result) - 1);
    goto loc_00A40109;
loc_00A4011E:
loc_00A40121:
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))), (unsigned int)(0x4B444342ULL), a4);
    if (result == 0) goto loc_00A4046D;
    result = memcpy(result, 0, (unsigned int)(a3), a4);
    result = 0;
    if ((unsigned __int8)(a2 + 1) != 0) goto loc_00A40315;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))))) + result * 1 - 2) = 0;
    goto loc_00A40315;
loc_00A40166:
    a1 = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A40487;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A40206;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A403E6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00A40437;
    if (((unsigned int)((unsigned int)(a3) - 1)) > ((unsigned int)(a1 + 1))) goto loc_00A4047D;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(a1 + 1)), (unsigned int)(0x4B444342ULL), a4);
    v_rbx = 0;
    if (result == 0) goto loc_00A4046D;
    result = ((*(unsigned __int8 *)(a2)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(result) = (unsigned __int8)(result);
loc_00A401C8:
    *(unsigned __int64 *)(a5) = result;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)((unsigned int)(a1 + 1)));
loc_00A401D8:
    if (v_stack_m48 != 0) goto loc_00A404C5;
loc_00A401E5:
    return 0;
loc_00A40206:
    if ((((unsigned __int8)((unsigned int)(a3))) & (15)) != 0) goto loc_00A4047D;
    v_r14 = (unsigned int)(((unsigned int)(a3)) >> (4));
    if ((unsigned int)(v_r14) == 0) goto loc_00A40271;
loc_00A40224:
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m38, a2, (unsigned int)(0x4B444342ULL), a4);
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 + 1))))))) << (4);
    a1 = (a1) + (0);
    result = RtlStringFromGUIDEx(a1, v_stack_m38, 1, a4);
    if (sign_flag) goto loc_00A401D8;
    a1 = (unsigned int)((v_stack_m38) + (2));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 + 1))))) + (a1));
    if (v_stack_m30 != 0) {
        result = ExFreePool(v_stack_m30, v_stack_m38, 1, a4);
        v_stack_m38 = v_xmm0;
    }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 + 1))))) + (1));
    if (((unsigned int)(v_rbx)) < ((unsigned int)(v_r14))) goto loc_00A40224;
loc_00A40271:
    v_r15 = (unsigned int)((v_r15) + (2));
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x4B444342ULL), a4);
    if (result == 0) goto loc_00A4046D;
    a2 = 0;
    v_stack_m40 = result;
    v_stack_p20 = 0;
    if ((unsigned int)(v_r14) == 0) goto loc_00A40310;
loc_00A402A7:
    a1 = (0) << (4);
    a1 = (a1) + (0);
    result = RtlStringFromGUIDEx(a1, v_stack_m38, 1, a4);
    if (sign_flag) goto loc_00A4032B;
    result = (unsigned int)((v_stack_m38) + (2));
    result = memcpy(v_stack_m40, v_stack_m30, (unsigned int)((unsigned int)(result)), a4);
    a1 = (v_stack_m40) + ((unsigned int)((unsigned int)(result)));
    v_stack_m40 = a1;
    result = v_stack_m30;
    if (v_stack_m30 != 0) {
        a1 = v_stack_m30;
        result = ExFreePool(a1, v_stack_m30, (unsigned int)((unsigned int)(result)), a4);
        a1 = v_stack_m40;
        v_stack_m38 = v_xmm0;
    }
    result = (unsigned int)(((unsigned int)(v_stack_p20)) + (1));
    v_stack_p20 = (unsigned int)(result);
    if (((unsigned int)(result)) < ((unsigned int)(v_r14))) goto loc_00A402A7;
loc_00A40310:
    result = 0;
    *(unsigned __int16 *)(a1) = 0;
loc_00A40315:
    v_rbx = 0;
    if (!sign_flag) goto loc_00A401C8;
    if (0 == 0) goto loc_00A401D8;
loc_00A4032B:
    result = ExFreePoolWithTag(0, (unsigned int)(0x4B444342ULL), (unsigned int)((unsigned int)(result)), a4);
    goto loc_00A401D8;
loc_00A4033D:
    if (((unsigned int)(v_r14 + 2)) >= ((unsigned int)(v_r14))) goto loc_00A4042F;
    goto loc_00A401E5;
loc_00A40354:
    if ((*(unsigned int *)(a2)) != 6) goto loc_00A4041E;
    result = BiConvertQualifiedPartitionToBootEnvironment(0, (unsigned int)((unsigned int)(v_r14)), v_stack_m48, a4);
loc_00A4036E:
    if (sign_flag) goto loc_00A401D8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 8))) + (16));
    if (((unsigned int)(result)) < 16) goto loc_00A404BB;
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x4B444342ULL), a4);
    if (result == 0) goto loc_00A4046D;
    *(unsigned __int64 *)(result) = v_xmm0;
    result = memcpy(result + 16, v_stack_m48, (unsigned int)(*(unsigned int *)(v_stack_m48 + 8)), a4);
    if (v_stack_m48 != 0) {
        a2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m48, a2, (unsigned int)(*(unsigned int *)(v_stack_m48 + 8)), a4);
        result = 0;
        v_stack_m48 = 0;
    }
    v_rbx = 0;
    goto loc_00A401C8;
loc_00A403E6:
    if (((unsigned int)(v_r14)) != 8) goto loc_00A4047D;
    result = ExAllocatePool2(258, 8, (unsigned int)(0x4B444342ULL), a4);
    v_rbx = 0;
    if (result == 0) goto loc_00A4046D;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a2);
    goto loc_00A401C8;
loc_00A4041E:
    a3 = 0;
    result = BiConvertNtDeviceToBootEnvironment(258, 8, a3, v_stack_m48);
    goto loc_00A4036E;
loc_00A4042F:
    goto loc_00A40121;
loc_00A40437:
    if (258 == 1) goto loc_00A40477;
loc_00A4043C:
    result = ExAllocatePool2(258, v_r14, (unsigned int)(0x4B444342ULL), v_stack_m48);
    if (result == 0) goto loc_00A4046D;
    result = memcpy(result, a2, v_r14, v_stack_m48);
    goto loc_00A403DF;
loc_00A4046D:
    goto loc_00A401D8;
loc_00A40477:
    if ((((unsigned __int8)(v_r14)) & (7)) == 0) goto loc_00A4043C;
loc_00A4047D:
    goto loc_00A401E5;
loc_00A40487:
    if (((unsigned int)(v_r14)) != 16) goto loc_00A4047D;
    result = RtlStringFromGUIDEx(a2, v_stack_m38, v_r14 - 15, v_stack_m48);
    v_rbx = 0;
    if (sign_flag) goto loc_00A401D8;
    v_r15 = (unsigned int)((v_stack_m38) + (2));
    goto loc_00A401C8;
loc_00A404BB:
    goto loc_00A401D8;
loc_00A404C5:
    result = ExFreePoolWithTag(a2, (unsigned int)(0x4B444342ULL), v_r14 - 15, v_stack_m48);
    goto loc_00A401E5;
}
```

## 5. (Beta) C Style

```c
int64_t BiConvertElementToRegistryData(int32_t Arg1, void *Arg2, void *Arg3, int32_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (64);
    Arg1 = (uint32_t)((Arg1) >> (24));
    Arg2 = 0;
    Arg1 = (uint32_t)((Arg1) & (15));
    v_stack_m48 = 0;
    v_stack_m38 = v_xmm0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A40354;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00A40166;
    if ((((uint8_t)(Arg2 + 1)) & ((uint8_t)((uint32_t)(Arg3)))) != 0) goto loc_00A4047D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (1));
loc_00A40109:
    if ((uint32_t)(result) == 0) goto loc_00A4033D;
    if ((*(uint16_t *)(0)) == 0) goto loc_00A4011E;
    Arg1 = (0) + (2);
    result = (uint32_t)((result) - 1);
    goto loc_00A40109;
loc_00A4011E:
loc_00A40121:
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))))), (uint32_t)(0x4B444342ULL), Arg4);
    if (result == 0) goto loc_00A4046D;
    result = memcpy(result, 0, (uint32_t)(Arg3), Arg4);
    result = 0;
    if ((uint8_t)(Arg2 + 1) != 0) goto loc_00A40315;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(arg3))))) + result * 1 - 0x2) = 0;
    goto loc_00A40315;
loc_00A40166:
    Arg1 = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A40487;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A40206;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A403E6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00A40437;
    if (((uint32_t)((uint32_t)(Arg3) - 1)) > ((uint32_t)(Arg1 + 1))) goto loc_00A4047D;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(Arg1 + 1)), (uint32_t)(0x4B444342ULL), Arg4);
    local_rbx = 0;
    if (result == 0) goto loc_00A4046D;
    result = ((*(uint8_t *)(arg2)) != 0) ? 1 : 0;
    *(uint8_t *)(result) = (uint8_t)(result);
loc_00A401C8:
    *(uint64_t *)(arg5) = result;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)((uint32_t)(Arg1 + 1)));
loc_00A401D8:
    if (v_stack_m48 != 0) goto loc_00A404C5;
loc_00A401E5:
    return 0;
loc_00A40206:
    if ((((uint8_t)((uint32_t)(Arg3))) & (15)) != 0) goto loc_00A4047D;
    local_r14 = (uint32_t)(((uint32_t)(Arg3)) >> (4));
    if ((uint32_t)(local_r14) == 0) goto loc_00A40271;
loc_00A40224:
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m38, Arg2, (uint32_t)(0x4B444342ULL), Arg4);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 + 1))))))) << (4);
    Arg1 = (Arg1) + (0);
    result = RtlStringFromGUIDEx(Arg1, v_stack_m38, 1, Arg4);
    if (sign_flag) goto loc_00A401D8;
    Arg1 = (uint32_t)((v_stack_m38) + (2));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 + 1))))) + (Arg1));
    if (v_stack_m30 != 0) {
        result = ExFreePool(v_stack_m30, v_stack_m38, 1, Arg4);
        v_stack_m38 = v_xmm0;
    }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 + 1))))) + (1));
    if (((uint32_t)(local_rbx)) < ((uint32_t)(local_r14))) goto loc_00A40224;
loc_00A40271:
    local_r15 = (uint32_t)((local_r15) + (2));
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x4B444342ULL), Arg4);
    if (result == 0) goto loc_00A4046D;
    Arg2 = 0;
    v_stack_m40 = result;
    v_stack_p20 = 0;
    if ((uint32_t)(local_r14) == 0) goto loc_00A40310;
loc_00A402A7:
    Arg1 = (0) << (4);
    Arg1 = (Arg1) + (0);
    result = RtlStringFromGUIDEx(Arg1, v_stack_m38, 1, Arg4);
    if (sign_flag) goto loc_00A4032B;
    result = (uint32_t)((v_stack_m38) + (2));
    result = memcpy(v_stack_m40, v_stack_m30, (uint32_t)((uint32_t)(result)), Arg4);
    Arg1 = (v_stack_m40) + ((uint32_t)((uint32_t)(result)));
    v_stack_m40 = Arg1;
    result = v_stack_m30;
    if (v_stack_m30 != 0) {
        Arg1 = v_stack_m30;
        result = ExFreePool(Arg1, v_stack_m30, (uint32_t)((uint32_t)(result)), Arg4);
        Arg1 = v_stack_m40;
        v_stack_m38 = v_xmm0;
    }
    result = (uint32_t)(((uint32_t)(v_stack_p20)) + (1));
    v_stack_p20 = (uint32_t)(result);
    if (((uint32_t)(result)) < ((uint32_t)(local_r14))) goto loc_00A402A7;
loc_00A40310:
    result = 0;
    *(uint16_t *)(Arg1) = 0;
loc_00A40315:
    local_rbx = 0;
    if (!sign_flag) goto loc_00A401C8;
    if (0 == 0) goto loc_00A401D8;
loc_00A4032B:
    result = ExFreePoolWithTag(0, (uint32_t)(0x4B444342ULL), (uint32_t)((uint32_t)(result)), Arg4);
    goto loc_00A401D8;
loc_00A4033D:
    if (((uint32_t)(local_r14 + 2)) >= ((uint32_t)(local_r14))) goto loc_00A4042F;
    goto loc_00A401E5;
loc_00A40354:
    if ((*(uint32_t *)(arg2)) != 6) goto loc_00A4041E;
    result = BiConvertQualifiedPartitionToBootEnvironment(0, (uint32_t)((uint32_t)(local_r14)), v_stack_m48, Arg4);
loc_00A4036E:
    if (sign_flag) goto loc_00A401D8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8))) + (16));
    if (((uint32_t)(result)) < 16) goto loc_00A404BB;
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x4B444342ULL), Arg4);
    if (result == 0) goto loc_00A4046D;
    *(uint64_t *)(result) = v_xmm0;
    result = memcpy(result + 16, v_stack_m48, (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8)), Arg4);
    if (v_stack_m48 != 0) {
        Arg2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m48, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m48 + 0x8)), Arg4);
        result = 0;
        v_stack_m48 = 0;
    }
    local_rbx = 0;
    goto loc_00A401C8;
loc_00A403E6:
    if (((uint32_t)(local_r14)) != 8) goto loc_00A4047D;
    result = ExAllocatePool2(258, 8, (uint32_t)(0x4B444342ULL), Arg4);
    local_rbx = 0;
    if (result == 0) goto loc_00A4046D;
    *(uint64_t *)(result) = *(uint64_t *)(arg2);
    goto loc_00A401C8;
loc_00A4041E:
    Arg3 = 0;
    result = BiConvertNtDeviceToBootEnvironment(258, 8, Arg3, v_stack_m48);
    goto loc_00A4036E;
loc_00A4042F:
    goto loc_00A40121;
loc_00A40437:
    if (258 == 1) goto loc_00A40477;
loc_00A4043C:
    result = ExAllocatePool2(258, local_r14, (uint32_t)(0x4B444342ULL), v_stack_m48);
    if (result == 0) goto loc_00A4046D;
    result = memcpy(result, Arg2, local_r14, v_stack_m48);
    goto loc_00A403DF;
loc_00A4046D:
    goto loc_00A401D8;
loc_00A40477:
    if ((((uint8_t)(local_r14)) & (7)) == 0) goto loc_00A4043C;
loc_00A4047D:
    goto loc_00A401E5;
loc_00A40487:
    if (((uint32_t)(local_r14)) != 16) goto loc_00A4047D;
    result = RtlStringFromGUIDEx(Arg2, v_stack_m38, local_r14 - 15, v_stack_m48);
    local_rbx = 0;
    if (sign_flag) goto loc_00A401D8;
    local_r15 = (uint32_t)((v_stack_m38) + (2));
    goto loc_00A401C8;
loc_00A404BB:
    goto loc_00A401D8;
loc_00A404C5:
    result = ExFreePoolWithTag(Arg2, (uint32_t)(0x4B444342ULL), local_r14 - 15, v_stack_m48);
    goto loc_00A401E5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x4` | `128` | `R` |
| `Arg3` | `- 0x1` | `32` | `R` |
| `Arg3` | `+ 0x2` | `32` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A400A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
