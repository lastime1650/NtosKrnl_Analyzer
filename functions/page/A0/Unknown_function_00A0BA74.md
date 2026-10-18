# sub_00A0BA74

- RVA: `0x00A0BA74`–`0x00A0C125` (길이 `1,713` bytes)
- VA: `0x0000000140A0BA74`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8A54`
- 디코드: `459`개 명령, `1,713/1,713` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A0BC76` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A0BCA1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0BCD3` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0BD11` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0BD52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0BDC8` → [ObOpenObjectByPointer](../8B/ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x00A0BE0C` → [ZwSetCachedSigningLevel](../../text/6B/ZwSetCachedSigningLevel_function_006B03F0.md) (function, `0x006B03F0`)
- `0x00A0BE29` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0BE5C` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0BE96` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0BEC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0BEE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0BF4B` → [FsRtlSetKernelEaFile](FsRtlSetKernelEaFile_function_00A0C8B0.md) (function, `0x00A0C8B0`)
- `0x00A0BF5B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A0BF6A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A0BF79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0C012` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x00969C32`

### Static image references
- `0x00A0BC55` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x00A0BF17` → RVA `0x00B4B428` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00A0BCA1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0BD52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0BE0C` → [ZwSetCachedSigningLevel](../../text/6B/ZwSetCachedSigningLevel_function_006B03F0.md) (`PAGE` → `.text`)
  - `0x00A0BE29` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0BEC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0BEE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0BF5B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A0BF6A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A0BF79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C012` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0BA74  48 8B C4                        mov rax, rsp
00A0BA77  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
00A0BA7B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00A0BA7F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A0BA83  55                              push rbp
00A0BA84  56                              push rsi
00A0BA85  57                              push rdi
00A0BA86  41 54                           push r12
00A0BA88  41 55                           push r13
00A0BA8A  41 56                           push r14
00A0BA8C  41 57                           push r15
00A0BA8E  48 8B EC                        mov rbp, rsp
00A0BA91  48 81 EC 80 00 00 00            sub rsp, 0x80
00A0BA98  45 33 ED                        xor r13d, r13d
00A0BA9B  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
00A0BA9F  49 8B F9                        mov rdi, r9
00A0BAA2  48 8B D1                        mov rdx, rcx
00A0BAA5  48 85 C9                        test rcx, rcx
00A0BAA8  0F 84 17 05 00 00               je 0x140a0bfc5
00A0BAAE  4D 85 C9                        test r9, r9
00A0BAB1  0F 84 0E 05 00 00               je 0x140a0bfc5
00A0BAB7  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A0BABB  48 85 C9                        test rcx, rcx
00A0BABE  0F 84 01 05 00 00               je 0x140a0bfc5
00A0BAC4  83 3A 03                        cmp dword ptr [rdx], 3
00A0BAC7  0F 86 F8 04 00 00               jbe 0x140a0bfc5
00A0BACD  48 8B C1                        mov rax, rcx
00A0BAD0  45 8B CD                        mov r9d, r13d
00A0BAD3  44 8B 18                        mov r11d, dword ptr [rax]
00A0BAD6  4C 8D 40 04                     lea r8, [rax + 4]
00A0BADA  41 83 F9 03                     cmp r9d, 3
00A0BADE  73 3B                           jae 0x140a0bb1b
00A0BAE0  4C 3B C0                        cmp r8, rax
00A0BAE3  73 28                           jae 0x140a0bb0d
00A0BAE5  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A0BAEA  0F 28 74 24 70                  movaps xmm6, xmmword ptr [rsp + 0x70]
00A0BAEF  8B C3                           mov eax, ebx
00A0BAF1  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A0BAF9  48 81 C4 80 00 00 00            add rsp, 0x80
00A0BB00  41 5F                           pop r15
00A0BB02  41 5E                           pop r14
00A0BB04  41 5D                           pop r13
00A0BB06  41 5C                           pop r12
00A0BB08  5F                              pop rdi
00A0BB09  5E                              pop rsi
00A0BB0A  5D                              pop rbp
00A0BB0B  C3                              ret
00A0BB0C  CC                              int3
00A0BB0D  4B 8D 04 18                     lea rax, [r8 + r11]
00A0BB11  49 3B C0                        cmp rax, r8
00A0BB14  72 CF                           jb 0x140a0bae5
00A0BB16  41 FF C1                        inc r9d
00A0BB19  EB B8                           jmp 0x140a0bad3
00A0BB1B  4C 3B C0                        cmp r8, rax
00A0BB1E  72 C5                           jb 0x140a0bae5
00A0BB20  45 85 DB                        test r11d, r11d
00A0BB23  4D 8B D5                        mov r10, r13
00A0BB26  4D 0F 45 D0                     cmovne r10, r8
00A0BB2A  41 83 FB 08                     cmp r11d, 8
00A0BB2E  0F 85 B4 05 00 00               jne 0x140a0c0e8
00A0BB34  83 3A 04                        cmp dword ptr [rdx], 4
00A0BB37  4D 8B 12                        mov r10, qword ptr [r10]
00A0BB3A  0F 86 85 04 00 00               jbe 0x140a0bfc5
00A0BB40  48 8B C1                        mov rax, rcx
00A0BB43  45 8B CD                        mov r9d, r13d
00A0BB46  44 8B 18                        mov r11d, dword ptr [rax]
00A0BB49  4C 8D 40 04                     lea r8, [rax + 4]
00A0BB4D  41 83 F9 04                     cmp r9d, 4
00A0BB51  73 13                           jae 0x140a0bb66
00A0BB53  4C 3B C0                        cmp r8, rax
00A0BB56  72 8D                           jb 0x140a0bae5
00A0BB58  4B 8D 04 18                     lea rax, [r8 + r11]
00A0BB5C  49 3B C0                        cmp rax, r8
00A0BB5F  72 84                           jb 0x140a0bae5
00A0BB61  41 FF C1                        inc r9d
00A0BB64  EB E0                           jmp 0x140a0bb46
00A0BB66  4C 3B C0                        cmp r8, rax
00A0BB69  0F 82 76 FF FF FF               jb 0x140a0bae5
00A0BB6F  45 85 DB                        test r11d, r11d
00A0BB72  49 8B C5                        mov rax, r13
00A0BB75  49 0F 45 C0                     cmovne rax, r8
00A0BB79  41 83 FB 04                     cmp r11d, 4
00A0BB7D  0F 85 3E 05 00 00               jne 0x140a0c0c1
00A0BB83  83 3A 05                        cmp dword ptr [rdx], 5
00A0BB86  8B 18                           mov ebx, dword ptr [rax]
00A0BB88  89 5D 48                        mov dword ptr [rbp + 0x48], ebx
00A0BB8B  0F 86 34 04 00 00               jbe 0x140a0bfc5
00A0BB91  48 8B C1                        mov rax, rcx
00A0BB94  45 8B CD                        mov r9d, r13d
00A0BB97  44 8B 18                        mov r11d, dword ptr [rax]
00A0BB9A  4C 8D 40 04                     lea r8, [rax + 4]
00A0BB9E  41 83 F9 05                     cmp r9d, 5
00A0BBA2  73 1E                           jae 0x140a0bbc2
00A0BBA4  4C 3B C0                        cmp r8, rax
00A0BBA7  0F 82 38 FF FF FF               jb 0x140a0bae5
00A0BBAD  4B 8D 04 18                     lea rax, [r8 + r11]
00A0BBB1  89 5D 48                        mov dword ptr [rbp + 0x48], ebx
00A0BBB4  49 3B C0                        cmp rax, r8
00A0BBB7  0F 82 28 FF FF FF               jb 0x140a0bae5
00A0BBBD  41 FF C1                        inc r9d
00A0BBC0  EB D5                           jmp 0x140a0bb97
00A0BBC2  4C 3B C0                        cmp r8, rax
00A0BBC5  0F 82 1A FF FF FF               jb 0x140a0bae5
00A0BBCB  45 85 DB                        test r11d, r11d
00A0BBCE  49 8B F5                        mov rsi, r13
00A0BBD1  49 0F 45 F0                     cmovne rsi, r8
00A0BBD5  41 83 FB 04                     cmp r11d, 4
00A0BBD9  0F 85 E2 04 00 00               jne 0x140a0c0c1
00A0BBDF  8B 36                           mov esi, dword ptr [rsi]
00A0BBE1  45 8D 4B 02                     lea r9d, [r11 + 2]
00A0BBE5  44 39 0A                        cmp dword ptr [rdx], r9d
00A0BBE8  0F 86 D7 03 00 00               jbe 0x140a0bfc5
00A0BBEE  45 8B C5                        mov r8d, r13d
00A0BBF1  8B 01                           mov eax, dword ptr [rcx]
00A0BBF3  48 8D 51 04                     lea rdx, [rcx + 4]
00A0BBF7  45 3B C1                        cmp r8d, r9d
00A0BBFA  73 1E                           jae 0x140a0bc1a
00A0BBFC  48 3B D1                        cmp rdx, rcx
00A0BBFF  0F 82 E0 FE FF FF               jb 0x140a0bae5
00A0BC05  48 8D 0C 02                     lea rcx, [rdx + rax]
00A0BC09  89 5D 48                        mov dword ptr [rbp + 0x48], ebx
00A0BC0C  48 3B CA                        cmp rcx, rdx
00A0BC0F  0F 82 D0 FE FF FF               jb 0x140a0bae5
00A0BC15  41 FF C0                        inc r8d
00A0BC18  EB D7                           jmp 0x140a0bbf1
00A0BC1A  48 3B D1                        cmp rdx, rcx
00A0BC1D  0F 82 C2 FE FF FF               jb 0x140a0bae5
00A0BC23  85 C0                           test eax, eax
00A0BC25  4D 8B FD                        mov r15, r13
00A0BC28  4C 0F 45 FA                     cmovne r15, rdx
00A0BC2C  83 F8 10                        cmp eax, 0x10
00A0BC2F  0F 85 90 03 00 00               jne 0x140a0bfc5
00A0BC35  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00A0BC39  0F 57 F6                        xorps xmm6, xmm6
00A0BC3C  4D 8B E5                        mov r12, r13
00A0BC3F  0F 11 75 D8                     movups xmmword ptr [rbp - 0x28], xmm6
00A0BC43  4D 85 D2                        test r10, r10
00A0BC46  0F 84 79 03 00 00               je 0x140a0bfc5
00A0BC4C  4D 85 FF                        test r15, r15
00A0BC4F  0F 84 70 03 00 00               je 0x140a0bfc5
00A0BC55  4C 8B 05 84 AE 5B 00            mov r8, qword ptr [rip + 0x5bae84]
00A0BC5C  48 8D 45 40                     lea rax, [rbp + 0x40]
00A0BC60  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00A0BC65  41 B1 01                        mov r9b, 1
00A0BC68  33 D2                           xor edx, edx
00A0BC6A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0BC6F  49 8B CA                        mov rcx, r10
00A0BC72  4C 89 6D 40                     mov qword ptr [rbp + 0x40], r13
00A0BC76  E8 35 D1 E5 FF                  call 0x140868db0
00A0BC7B  8B D8                           mov ebx, eax
00A0BC7D  41 BE 3E 00 00 C0               mov r14d, 0xc000003e
00A0BC83  85 C0                           test eax, eax
00A0BC85  0F 88 C7 02 00 00               js 0x140a0bf52
00A0BC8B  BB 48 02 00 00                  mov ebx, 0x248
00A0BC90  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
00A0BC94  8B D3                           mov edx, ebx
00A0BC96  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0BC9C  B9 00 01 00 00                  mov ecx, 0x100
00A0BCA1  E8 4A 64 17 00                  call 0x140b820f0
00A0BCA6  4C 8B E8                        mov r13, rax
00A0BCA9  48 85 C0                        test rax, rax
00A0BCAC  0F 84 40 04 00 00               je 0x140a0c0f2
00A0BCB2  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BCB6  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0BCBA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0BCBF  45 33 C9                        xor r9d, r9d
00A0BCC2  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A0BCC6  45 33 C0                        xor r8d, r8d
00A0BCC9  BA F4 00 09 00                  mov edx, 0x900f4
00A0BCCE  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A0BCD3  E8 98 0D 00 00                  call 0x140a0ca70
00A0BCD8  8B D8                           mov ebx, eax
00A0BCDA  85 C0                           test eax, eax
00A0BCDC  78 5D                           js 0x140a0bd3b
00A0BCDE  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0BCE2  72 54                           jb 0x140a0bd38
00A0BCE4  49 8B 45 00                     mov rax, qword ptr [r13]
00A0BCE8  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00A0BCEC  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A0BCF1  45 33 C9                        xor r9d, r9d
00A0BCF4  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BCF8  45 33 C0                        xor r8d, r8d
00A0BCFB  C7 44 24 28 48 02 00 00         mov dword ptr [rsp + 0x28], 0x248
00A0BD03  BA EB 00 09 00                  mov edx, 0x900eb
00A0BD08  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A0BD0D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A0BD11  E8 5A 0D 00 00                  call 0x140a0ca70
00A0BD16  8B D8                           mov ebx, eax
00A0BD18  85 C0                           test eax, eax
00A0BD1A  78 1F                           js 0x140a0bd3b
00A0BD1C  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0BD20  72 16                           jb 0x140a0bd38
00A0BD22  4D 8B 65 18                     mov r12, qword ptr [r13 + 0x18]
00A0BD26  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A0BD2A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00A0BD2E  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00A0BD32  0F 10 75 D8                     movups xmm6, xmmword ptr [rbp - 0x28]
00A0BD36  EB 15                           jmp 0x140a0bd4d
00A0BD38  41 8B DE                        mov ebx, r14d
00A0BD3B  0F 57 C0                        xorps xmm0, xmm0
00A0BD3E  66 0F D6 75 C8                  movq qword ptr [rbp - 0x38], xmm6
00A0BD43  66 0F 73 D8 08                  psrldq xmm0, 8
00A0BD48  66 49 0F 7E C4                  movq r12, xmm0
00A0BD4D  33 D2                           xor edx, edx
00A0BD4F  49 8B CD                        mov rcx, r13
00A0BD52  E8 19 6B 17 00                  call 0x140b82870
00A0BD57  45 33 ED                        xor r13d, r13d
00A0BD5A  85 DB                           test ebx, ebx
00A0BD5C  0F 88 A0 03 00 00               js 0x140a0c102
00A0BD62  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00A0BD66  49 3B 07                        cmp rax, qword ptr [r15]
00A0BD69  0F 85 90 03 00 00               jne 0x140a0c0ff
00A0BD6F  4D 3B 67 08                     cmp r12, qword ptr [r15 + 8]
00A0BD73  0F 85 86 03 00 00               jne 0x140a0c0ff
00A0BD79  45 8D 7D 18                     lea r15d, [r13 + 0x18]
00A0BD7D  44 39 6D 48                     cmp dword ptr [rbp + 0x48], r13d
00A0BD81  74 1C                           je 0x140a0bd9f
00A0BD83  48 83 4D D8 FF                  or qword ptr [rbp - 0x28], 0xffffffffffffffff
00A0BD88  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00A0BD92  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00A0BD96  0F 10 75 D8                     movups xmm6, xmmword ptr [rbp - 0x28]
00A0BD9A  E9 34 01 00 00                  jmp 0x140a0bed3
00A0BD9F  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BDA3  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A0BDA7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0BDAC  45 8B CF                        mov r9d, r15d
00A0BDAF  48 8B 05 2A AD 5B 00            mov rax, qword ptr [rip + 0x5bad2a]
00A0BDB6  45 33 C0                        xor r8d, r8d
00A0BDB9  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00A0BDBE  BA 00 02 00 00                  mov edx, 0x200
00A0BDC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0BDC8  E8 53 B6 EA FF                  call 0x1408b7420
00A0BDCD  85 C0                           test eax, eax
00A0BDCF  78 40                           js 0x140a0be11
00A0BDD1  85 F6                           test esi, esi
00A0BDD3  0F 84 B6 02 00 00               je 0x140a0c08f
00A0BDD9  83 EE 01                        sub esi, 1
00A0BDDC  0F 84 AD 02 00 00               je 0x140a0c08f
00A0BDE2  83 EE 01                        sub esi, 1
00A0BDE5  74 09                           je 0x140a0bdf0
00A0BDE7  83 FE 01                        cmp esi, 1
00A0BDEA  0F 85 9F 02 00 00               jne 0x140a0c08f
00A0BDF0  BA 06 00 00 00                  mov edx, 6
00A0BDF5  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A0BDF9  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00A0BDFD  41 B9 01 00 00 00               mov r9d, 1
00A0BE03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0BE08  41 8D 49 01                     lea ecx, [r9 + 1]
00A0BE0C  E8 DF 45 CA FF                  call 0x1406b03f0
00A0BE11  41 BC 48 02 00 00               mov r12d, 0x248
00A0BE17  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
00A0BE1B  41 8B D4                        mov edx, r12d
00A0BE1E  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0BE24  B9 00 01 00 00                  mov ecx, 0x100
00A0BE29  E8 C2 62 17 00                  call 0x140b820f0
00A0BE2E  48 8B F0                        mov rsi, rax
00A0BE31  48 85 C0                        test rax, rax
00A0BE34  0F 84 D0 02 00 00               je 0x140a0c10a
00A0BE3A  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BE3E  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0BE42  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0BE47  45 33 C9                        xor r9d, r9d
00A0BE4A  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00A0BE4F  45 33 C0                        xor r8d, r8d
00A0BE52  BA F4 00 09 00                  mov edx, 0x900f4
00A0BE57  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A0BE5C  E8 0F 0C 00 00                  call 0x140a0ca70
00A0BE61  8B D8                           mov ebx, eax
00A0BE63  85 C0                           test eax, eax
00A0BE65  78 5A                           js 0x140a0bec1
00A0BE67  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0BE6B  0F 82 5A 02 00 00               jb 0x140a0c0cb
00A0BE71  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BE75  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0BE79  4C 8B 3E                        mov r15, qword ptr [rsi]
00A0BE7C  45 33 C9                        xor r9d, r9d
00A0BE7F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0BE84  45 33 C0                        xor r8d, r8d
00A0BE87  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00A0BE8C  BA EB 00 09 00                  mov edx, 0x900eb
00A0BE91  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A0BE96  E8 D5 0B 00 00                  call 0x140a0ca70
00A0BE9B  8B D8                           mov ebx, eax
00A0BE9D  85 C0                           test eax, eax
00A0BE9F  78 1A                           js 0x140a0bebb
00A0BEA1  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0BEA5  0F 82 66 02 00 00               jb 0x140a0c111
00A0BEAB  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00A0BEAF  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00A0BEB3  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00A0BEB7  0F 10 75 D8                     movups xmm6, xmmword ptr [rbp - 0x28]
00A0BEBB  41 BF 18 00 00 00               mov r15d, 0x18
00A0BEC1  33 D2                           xor edx, edx
00A0BEC3  48 8B CE                        mov rcx, rsi
00A0BEC6  E8 A5 69 17 00                  call 0x140b82870
00A0BECB  85 DB                           test ebx, ebx
00A0BECD  0F 88 2F 02 00 00               js 0x140a0c102
00A0BED3  BB 3A 00 00 00                  mov ebx, 0x3a
00A0BED8  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0BEDE  8B D3                           mov edx, ebx
00A0BEE0  B9 00 01 00 00                  mov ecx, 0x100
00A0BEE5  E8 06 62 17 00                  call 0x140b820f0
00A0BEEA  48 8B C8                        mov rcx, rax
00A0BEED  48 85 C0                        test rax, rax
00A0BEF0  0F 84 14 02 00 00               je 0x140a0c10a
00A0BEF6  0F 57 C0                        xorps xmm0, xmm0
00A0BEF9  33 C0                           xor eax, eax
00A0BEFB  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A0BEFE  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
00A0BF02  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00A0BF06  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
00A0BF0A  66 89 41 38                     mov word ptr [rcx + 0x38], ax
00A0BF0E  66 44 89 79 06                  mov word ptr [rcx + 6], r15w
00A0BF13  C6 41 05 19                     mov byte ptr [rcx + 5], 0x19
00A0BF17  48 8B 05 0A F5 13 00            mov rax, qword ptr [rip + 0x13f50a]
00A0BF1E  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A0BF21  0F 11 41 08                     movups xmmword ptr [rcx + 8], xmm0
00A0BF25  F2 0F 10 48 10                  movsd xmm1, qword ptr [rax + 0x10]
00A0BF2A  F2 0F 11 49 18                  movsd qword ptr [rcx + 0x18], xmm1
00A0BF2F  8A 40 18                        mov al, byte ptr [rax + 0x18]
00A0BF32  88 41 20                        mov byte ptr [rcx + 0x20], al
00A0BF35  F3 0F 7F 71 22                  movdqu xmmword ptr [rcx + 0x22], xmm6
00A0BF3A  4C 89 69 32                     mov qword ptr [rcx + 0x32], r13
00A0BF3E  4C 8B E1                        mov r12, rcx
00A0BF41  48 8B D1                        mov rdx, rcx
00A0BF44  44 8B C3                        mov r8d, ebx
00A0BF47  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BF4B  E8 60 09 00 00                  call 0x140a0c8b0
00A0BF50  8B D8                           mov ebx, eax
00A0BF52  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A0BF56  48 85 C9                        test rcx, rcx
00A0BF59  74 05                           je 0x140a0bf60
00A0BF5B  E8 50 13 CA FF                  call 0x1406ad2b0
00A0BF60  4C 39 6D 40                     cmp qword ptr [rbp + 0x40], r13
00A0BF64  74 09                           je 0x140a0bf6f
00A0BF66  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0BF6A  E8 E1 D3 8E FF                  call 0x1402f9350
00A0BF6F  4D 85 E4                        test r12, r12
00A0BF72  74 0A                           je 0x140a0bf7e
00A0BF74  33 D2                           xor edx, edx
00A0BF76  49 8B CC                        mov rcx, r12
00A0BF79  E8 F2 68 17 00                  call 0x140b82870
00A0BF7E  85 DB                           test ebx, ebx
00A0BF80  0F 88 64 FB FF FF               js 0x140a0baea
00A0BF86  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
00A0BF8A  4D 85 C0                        test r8, r8
00A0BF8D  0F 84 04 01 00 00               je 0x140a0c097
00A0BF93  44 8B 17                        mov r10d, dword ptr [rdi]
00A0BF96  49 8B D0                        mov rdx, r8
00A0BF99  41 8B CD                        mov ecx, r13d
00A0BF9C  41 3B CA                        cmp ecx, r10d
00A0BF9F  73 2E                           jae 0x140a0bfcf
00A0BFA1  8B 02                           mov eax, dword ptr [rdx]
00A0BFA3  83 C0 04                        add eax, 4
00A0BFA6  83 F8 04                        cmp eax, 4
00A0BFA9  0F 82 36 FB FF FF               jb 0x140a0bae5
00A0BFAF  44 8B C8                        mov r9d, eax
00A0BFB2  4C 03 CA                        add r9, rdx
00A0BFB5  4C 3B CA                        cmp r9, rdx
00A0BFB8  0F 82 27 FB FF FF               jb 0x140a0bae5
00A0BFBE  49 8B D1                        mov rdx, r9
00A0BFC1  FF C1                           inc ecx
00A0BFC3  EB D7                           jmp 0x140a0bf9c
00A0BFC5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A0BFCA  E9 1B FB FF FF                  jmp 0x140a0baea
00A0BFCF  4C 8D 4A 04                     lea r9, [rdx + 4]
00A0BFD3  4C 3B CA                        cmp r9, rdx
00A0BFD6  0F 82 09 FB FF FF               jb 0x140a0bae5
00A0BFDC  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0BFDF  48 8D 42 08                     lea rax, [rdx + 8]
00A0BFE3  49 03 C8                        add rcx, r8
00A0BFE6  48 3B C1                        cmp rax, rcx
00A0BFE9  0F 87 D2 00 00 00               ja 0x140a0c0c1
00A0BFEF  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00A0BFF5  45 89 29                        mov dword ptr [r9], r13d
00A0BFF8  FF 07                           inc dword ptr [rdi]
00A0BFFA  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A0BFFD  85 C0                           test eax, eax
00A0BFFF  0F 84 14 01 00 00               je 0x140a0c119
00A0C005  8B D0                           mov edx, eax
00A0C007  B9 00 01 00 00                  mov ecx, 0x100
00A0C00C  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0C012  E8 D9 60 17 00                  call 0x140b820f0
00A0C017  48 85 C0                        test rax, rax
00A0C01A  0F 84 FE 00 00 00               je 0x140a0c11e
00A0C020  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A0C024  44 89 2F                        mov dword ptr [rdi], r13d
00A0C027  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A0C02B  48 85 D2                        test rdx, rdx
00A0C02E  74 7A                           je 0x140a0c0aa
00A0C030  44 8B 0F                        mov r9d, dword ptr [rdi]
00A0C033  41 8B CD                        mov ecx, r13d
00A0C036  41 3B C9                        cmp ecx, r9d
00A0C039  73 24                           jae 0x140a0c05f
00A0C03B  8B 02                           mov eax, dword ptr [rdx]
00A0C03D  83 C0 04                        add eax, 4
00A0C040  83 F8 04                        cmp eax, 4
00A0C043  0F 82 9C FA FF FF               jb 0x140a0bae5
00A0C049  44 8B C0                        mov r8d, eax
00A0C04C  4C 03 C2                        add r8, rdx
00A0C04F  4C 3B C2                        cmp r8, rdx
00A0C052  0F 82 8D FA FF FF               jb 0x140a0bae5
00A0C058  49 8B D0                        mov rdx, r8
00A0C05B  FF C1                           inc ecx
00A0C05D  EB D7                           jmp 0x140a0c036
00A0C05F  4C 8D 42 04                     lea r8, [rdx + 4]
00A0C063  4C 3B C2                        cmp r8, rdx
00A0C066  0F 82 79 FA FF FF               jb 0x140a0bae5
00A0C06C  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0C06F  48 8D 42 08                     lea rax, [rdx + 8]
00A0C073  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A0C077  41 8B DD                        mov ebx, r13d
00A0C07A  48 3B C1                        cmp rax, rcx
00A0C07D  77 42                           ja 0x140a0c0c1
00A0C07F  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00A0C085  45 89 28                        mov dword ptr [r8], r13d
00A0C088  FF 07                           inc dword ptr [rdi]
00A0C08A  E9 5B FA FF FF                  jmp 0x140a0baea
00A0C08F  41 8A D5                        mov dl, r13b
00A0C092  E9 5E FD FF FF                  jmp 0x140a0bdf5
00A0C097  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A0C09A  8D 48 08                        lea ecx, [rax + 8]
00A0C09D  3B C8                           cmp ecx, eax
00A0C09F  73 32                           jae 0x140a0c0d3
00A0C0A1  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00A0C0A5  E9 3B FA FF FF                  jmp 0x140a0bae5
00A0C0AA  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A0C0AD  8D 48 08                        lea ecx, [rax + 8]
00A0C0B0  3B C8                           cmp ecx, eax
00A0C0B2  72 ED                           jb 0x140a0c0a1
00A0C0B4  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A0C0B7  41 8B DD                        mov ebx, r13d
00A0C0BA  FF 07                           inc dword ptr [rdi]
00A0C0BC  E9 29 FA FF FF                  jmp 0x140a0baea
00A0C0C1  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A0C0C6  E9 1F FA FF FF                  jmp 0x140a0baea
00A0C0CB  41 8B DE                        mov ebx, r14d
00A0C0CE  E9 EE FD FF FF                  jmp 0x140a0bec1
00A0C0D3  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A0C0D6  E9 1D FF FF FF                  jmp 0x140a0bff8
00A0C0DB  85 DB                           test ebx, ebx
00A0C0DD  0F 89 44 FF FF FF               jns 0x140a0c027
00A0C0E3  E9 02 FA FF FF                  jmp 0x140a0baea
00A0C0E8  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A0C0ED  E9 F8 F9 FF FF                  jmp 0x140a0baea
00A0C0F2  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0C0F7  45 33 ED                        xor r13d, r13d
00A0C0FA  E9 53 FE FF FF                  jmp 0x140a0bf52
00A0C0FF  41 8B DE                        mov ebx, r14d
00A0C102  4D 8B E5                        mov r12, r13
00A0C105  E9 48 FE FF FF                  jmp 0x140a0bf52
00A0C10A  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0C10F  EB F1                           jmp 0x140a0c102
00A0C111  41 8B DE                        mov ebx, r14d
00A0C114  E9 A2 FD FF FF                  jmp 0x140a0bebb
00A0C119  41 8B DE                        mov ebx, r14d
00A0C11C  EB BD                           jmp 0x140a0c0db
00A0C11E  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0C123  EB B6                           jmp 0x140a0c0db
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A0BA74(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (128);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    if (a1 == 0) goto loc_00A0BFC5;
    if (a4 == 0) goto loc_00A0BFC5;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A0BFC5;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A0BFC5;
loc_00A0BAD3:
    if (0 >= 3) goto loc_00A0BB1B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0BB0D;
loc_00A0BAE5:
loc_00A0BAEA:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
loc_00A0BB0D:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0BAE5;
    a4 = (unsigned int)((0) + 1);
    goto loc_00A0BAD3;
loc_00A0BB1B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0BAE5;
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r10 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A0C0E8;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00A0BFC5;
loc_00A0BB46:
    if (0 >= 4) goto loc_00A0BB66;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0BAE5;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0BAE5;
    a4 = (unsigned int)((0) + 1);
    goto loc_00A0BB46;
loc_00A0BB66:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0BAE5;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 4) goto loc_00A0C0C1;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00A0BFC5;
loc_00A0BB97:
    if (0 >= 5) goto loc_00A0BBC2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0BAE5;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0BAE5;
    a4 = (unsigned int)((0) + 1);
    goto loc_00A0BB97;
loc_00A0BBC2:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0BAE5;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 4) goto loc_00A0C0C1;
    if ((*(unsigned int *)(a1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) + 2))) goto loc_00A0BFC5;
loc_00A0BBF1:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) + 2))) goto loc_00A0BC1A;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0BAE5;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0BAE5;
    a3 = (unsigned int)((0) + 1);
    goto loc_00A0BBF1;
loc_00A0BC1A:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0BAE5;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 16) goto loc_00A0BFC5;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm6;
    if (*(unsigned __int64 *)(v_r10) == 0) goto loc_00A0BFC5;
    if (v_r15 == 0) goto loc_00A0BFC5;
    v_stack_p28 = 0;
    a2 = 0;
    v_stack_p20 = v_stack_p8;
    v_stack_p8 = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_r10), a2, *(unsigned __int64 *)(v_rip + 6008452), 1);
    if (sign_flag) goto loc_00A0BF52;
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (unsigned int)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C0F2;
    v_stack_p30 = v_stack_p18;
    a4 = 0;
    v_stack_p28 = 584;
    a3 = 0;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (unsigned int)(0x900F4ULL), a3, a4);
    if (sign_flag) goto loc_00A0BD3B;
    if (v_stack_p18 < 64) goto loc_00A0BD38;
    v_stack_p30 = v_stack_p18;
    a4 = 0;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    v_stack_m70 = *(unsigned __int64 *)(result);
    result = FsRtlKernelFsControlFile(v_stack_p8, (unsigned int)(0x900EBULL), a3, a4);
    if (sign_flag) goto loc_00A0BD3B;
    if (v_stack_p18 < 64) goto loc_00A0BD38;
    v_stack_m60 = v_stack_m70;
    v_stack_m58 = *(unsigned __int64 *)(result + 24);
    goto loc_00A0BD4D;
loc_00A0BD38:
loc_00A0BD3B:
    v_stack_m70 = v_xmm6;
loc_00A0BD4D:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    v_r13 = 0;
    if (sign_flag) goto loc_00A0C102;
    if (v_stack_m70 != (*(unsigned __int64 *)(v_r15))) goto loc_00A0C0FF;
    if ((*(unsigned __int64 *)(result + 24)) != (*(unsigned __int64 *)(v_r15 + 8))) goto loc_00A0C0FF;
    if (v_stack_p10 == 0) goto loc_00A0BD9F;
    v_stack_m58 = v_stack_m70;
    goto loc_00A0BED3;
loc_00A0BD9F:
    v_stack_p30 = v_stack_m68;
    a3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(v_rip + 6008106);
    result = ObOpenObjectByPointer(v_stack_p8, 512, a3, (unsigned int)((unsigned int)(v_r13 + 24)));
    if (sign_flag) goto loc_00A0BE11;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00A0C08F;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) - (1));
    if (condition_is_equal) goto loc_00A0C08F;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00A0BDF0;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00A0C08F;
loc_00A0BDF0:
loc_00A0BDF5:
    v_stack_p20 = v_stack_m68;
    result = ZwSetCachedSigningLevel(1 + 1, 6, v_stack_m68, 1);
loc_00A0BE11:
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (unsigned int)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C10A;
    v_stack_p30 = v_stack_p18;
    a4 = 0;
    v_stack_p28 = 584;
    a3 = 0;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (unsigned int)(0x900F4ULL), a3, a4);
    if (sign_flag) goto loc_00A0BEC1;
    if (v_stack_p18 < 64) goto loc_00A0C0CB;
    a4 = 0;
    v_stack_p30 = v_stack_p18;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (unsigned int)(0x900EBULL), a3, a4);
    if (sign_flag) goto loc_00A0BEBB;
    if (v_stack_p18 < 64) goto loc_00A0C111;
    v_stack_m58 = *(unsigned __int64 *)(result + 24);
    v_stack_m60 = *(unsigned __int64 *)(result);
loc_00A0BEBB:
loc_00A0BEC1:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    if (sign_flag) goto loc_00A0C102;
loc_00A0BED3:
    result = ExAllocatePool2(256, 58, (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00A0C10A;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = 0;
    *(unsigned __int16 *)(result + 56) = 0;
    *(unsigned __int16 *)(result + 6) = 24;
    *(unsigned __int8 *)(result + 5) = 25;
    *(unsigned __int64 *)(result + 8) = v_xmm0;
    *(unsigned __int64 *)(result + 24) = v_xmm1;
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 1307914) + 24));
    *(unsigned __int64 *)(result + 34) = v_xmm6;
    *(unsigned __int64 *)(result + 50) = 0;
    result = FsRtlSetKernelEaFile(v_stack_p8, 0, 58, a4);
loc_00A0BF52:
    if (v_stack_m68 != 0) {
        result = ZwClose(v_stack_m68, 0, 58, a4);
    }
    if (v_stack_p8 != 0) {
        a1 = v_stack_p8;
        result = ObfDereferenceObject(a1, 0, 58, a4);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 58, a4);
    }
    if (sign_flag) goto loc_00A0BAEA;
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A0C097;
loc_00A0BF9C:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A0BFCF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0BAE5;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A0BAE5;
    a1 = (unsigned int)((0) + 1);
    goto loc_00A0BF9C;
loc_00A0BFC5:
    goto loc_00A0BAEA;
loc_00A0BFCF:
    if ((a4 + 4) < a4) goto loc_00A0BAE5;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 8) > a1) goto loc_00A0C0C1;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = 0;
loc_00A0BFF8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))) == 0) goto loc_00A0C119;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))), (unsigned int)(0x20534C53ULL), a4 + 4);
    if (result == 0) goto loc_00A0C11E;
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
loc_00A0C027:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A0C0AA;
loc_00A0C036:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A0C05F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0BAE5;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A0BAE5;
    a1 = (unsigned int)((0) + 1);
    goto loc_00A0C036;
loc_00A0C05F:
    if ((a3 + 4) < a3) goto loc_00A0BAE5;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00A0C0C1;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = 0;
    goto loc_00A0BAEA;
loc_00A0C08F:
    goto loc_00A0BDF5;
loc_00A0C097:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0C0D3;
loc_00A0C0A1:
    goto loc_00A0BAE5;
loc_00A0C0AA:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0C0A1;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A0BAEA;
loc_00A0C0C1:
    goto loc_00A0BAEA;
loc_00A0C0CB:
    goto loc_00A0BEC1;
loc_00A0C0D3:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A0BFF8;
loc_00A0C0DB:
    if (!sign_flag) goto loc_00A0C027;
    goto loc_00A0BAEA;
loc_00A0C0E8:
    goto loc_00A0BAEA;
loc_00A0C0F2:
    v_r13 = 0;
    goto loc_00A0BF52;
loc_00A0C0FF:
loc_00A0C102:
    goto loc_00A0BF52;
loc_00A0C10A:
    goto loc_00A0C102;
loc_00A0C111:
    goto loc_00A0BEBB;
loc_00A0C119:
    goto loc_00A0C0DB;
loc_00A0C11E:
    goto loc_00A0C0DB;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A0BA74(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (128);
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    if (Arg1 == NULL) goto loc_00A0BFC5;
    if (Arg4 == NULL) goto loc_00A0BFC5;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A0BFC5;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A0BFC5;
loc_00A0BAD3:
    if (0 >= 3) goto loc_00A0BB1B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0BB0D;
loc_00A0BAE5:
loc_00A0BAEA:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
loc_00A0BB0D:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0BAE5;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00A0BAD3;
loc_00A0BB1B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0BAE5;
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r10 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A0C0E8;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00A0BFC5;
loc_00A0BB46:
    if (0 >= 4) goto loc_00A0BB66;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0BAE5;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0BAE5;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00A0BB46;
loc_00A0BB66:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0BAE5;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 4) goto loc_00A0C0C1;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00A0BFC5;
loc_00A0BB97:
    if (0 >= 5) goto loc_00A0BBC2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0BAE5;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0BAE5;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00A0BB97;
loc_00A0BBC2:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0BAE5;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 4) goto loc_00A0C0C1;
    if ((*(uint32_t *)(arg1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) + 2))) goto loc_00A0BFC5;
loc_00A0BBF1:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) + 2))) goto loc_00A0BC1A;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0BAE5;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0BAE5;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00A0BBF1;
loc_00A0BC1A:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0BAE5;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 16) goto loc_00A0BFC5;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm6;
    if (*(uint64_t *)(local_r10) == 0) goto loc_00A0BFC5;
    if (local_r15 == 0) goto loc_00A0BFC5;
    v_stack_p28 = 0;
    Arg2 = 0;
    v_stack_p20 = v_stack_p8;
    v_stack_p8 = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(local_r10), Arg2, *(uint64_t *)(v_rip + 0x5BAE84), 1);
    if (sign_flag) goto loc_00A0BF52;
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (uint32_t)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C0F2;
    v_stack_p30 = v_stack_p18;
    Arg4 = 0;
    v_stack_p28 = 584;
    Arg3 = 0;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (uint32_t)(0x900F4ULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0BD3B;
    if (v_stack_p18 < 64) goto loc_00A0BD38;
    v_stack_p30 = v_stack_p18;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    v_stack_m70 = *(uint64_t *)(result);
    result = FsRtlKernelFsControlFile(v_stack_p8, (uint32_t)(0x900EBULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0BD3B;
    if (v_stack_p18 < 64) goto loc_00A0BD38;
    v_stack_m60 = v_stack_m70;
    v_stack_m58 = *(uint64_t *)(result + 0x18);
    goto loc_00A0BD4D;
loc_00A0BD38:
loc_00A0BD3B:
    v_stack_m70 = v_xmm6;
loc_00A0BD4D:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    local_r13 = 0;
    if (sign_flag) goto loc_00A0C102;
    if (v_stack_m70 != (*(uint64_t *)(local_r15))) goto loc_00A0C0FF;
    if ((*(uint64_t *)(result + 0x18)) != (*(uint64_t *)(local_r15 + 0x8))) goto loc_00A0C0FF;
    if (v_stack_p10 == 0) goto loc_00A0BD9F;
    v_stack_m58 = v_stack_m70;
    goto loc_00A0BED3;
loc_00A0BD9F:
    v_stack_p30 = v_stack_m68;
    Arg3 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(v_rip + 0x5BAD2A);
    result = ObOpenObjectByPointer(v_stack_p8, 512, Arg3, (uint32_t)((uint32_t)(local_r13 + 24)));
    if (sign_flag) goto loc_00A0BE11;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00A0C08F;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) - (1));
    if (condition_is_equal) goto loc_00A0C08F;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00A0BDF0;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00A0C08F;
loc_00A0BDF0:
loc_00A0BDF5:
    v_stack_p20 = v_stack_m68;
    result = ZwSetCachedSigningLevel(1 + 1, 6, v_stack_m68, 1);
loc_00A0BE11:
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (uint32_t)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C10A;
    v_stack_p30 = v_stack_p18;
    Arg4 = 0;
    v_stack_p28 = 584;
    Arg3 = 0;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (uint32_t)(0x900F4ULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0BEC1;
    if (v_stack_p18 < 64) goto loc_00A0C0CB;
    Arg4 = 0;
    v_stack_p30 = v_stack_p18;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p8, (uint32_t)(0x900EBULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0BEBB;
    if (v_stack_p18 < 64) goto loc_00A0C111;
    v_stack_m58 = *(uint64_t *)(result + 0x18);
    v_stack_m60 = *(uint64_t *)(result);
loc_00A0BEBB:
loc_00A0BEC1:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00A0C102;
loc_00A0BED3:
    result = ExAllocatePool2(256, 58, (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00A0C10A;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = 0;
    *(uint16_t *)(result + 0x38) = 0;
    *(uint16_t *)(result + 0x6) = 24;
    *(uint8_t *)(result + 0x5) = 25;
    *(uint64_t *)(result + 0x8) = v_xmm0;
    *(uint64_t *)(result + 0x18) = v_xmm1;
    *(uint8_t *)(result + 0x20) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x13F50A) + 0x18));
    *(uint64_t *)(result + 0x22) = v_xmm6;
    *(uint64_t *)(result + 0x32) = 0;
    result = FsRtlSetKernelEaFile(v_stack_p8, 0, 58, Arg4);
loc_00A0BF52:
    if (v_stack_m68 != 0) {
        result = ZwClose(v_stack_m68, 0, 58, Arg4);
    }
    if (v_stack_p8 != 0) {
        Arg1 = v_stack_p8;
        result = ObfDereferenceObject(Arg1, 0, 58, Arg4);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 58, Arg4);
    }
    if (sign_flag) goto loc_00A0BAEA;
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A0C097;
loc_00A0BF9C:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A0BFCF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0BAE5;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A0BAE5;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00A0BF9C;
loc_00A0BFC5:
    goto loc_00A0BAEA;
loc_00A0BFCF:
    if ((Arg4 + 4) < Arg4) goto loc_00A0BAE5;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg4 + 8) > Arg1) goto loc_00A0C0C1;
    *(uint32_t *)(arg4) = 4;
    *(uint32_t *)(arg4 + 0x4) = 0;
loc_00A0BFF8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))) == 0) goto loc_00A0C119;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)))), (uint32_t)(0x20534C53ULL), Arg4 + 4);
    if (result == 0) goto loc_00A0C11E;
    *(uint64_t *)(arg4 + 0x8) = result;
    *(uint32_t *)(arg4) = 0;
loc_00A0C027:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A0C0AA;
loc_00A0C036:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A0C05F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0BAE5;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A0BAE5;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00A0C036;
loc_00A0C05F:
    if ((Arg3 + 4) < Arg3) goto loc_00A0BAE5;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00A0C0C1;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = 0;
    goto loc_00A0BAEA;
loc_00A0C08F:
    goto loc_00A0BDF5;
loc_00A0C097:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0C0D3;
loc_00A0C0A1:
    goto loc_00A0BAE5;
loc_00A0C0AA:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0C0A1;
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8);
    goto loc_00A0BAEA;
loc_00A0C0C1:
    goto loc_00A0BAEA;
loc_00A0C0CB:
    goto loc_00A0BEC1;
loc_00A0C0D3:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8);
    goto loc_00A0BFF8;
loc_00A0C0DB:
    if (!sign_flag) goto loc_00A0C027;
    goto loc_00A0BAEA;
loc_00A0C0E8:
    goto loc_00A0BAEA;
loc_00A0C0F2:
    local_r13 = 0;
    goto loc_00A0BF52;
loc_00A0C0FF:
loc_00A0C102:
    goto loc_00A0BF52;
loc_00A0C10A:
    goto loc_00A0C102;
loc_00A0C111:
    goto loc_00A0BEBB;
loc_00A0C119:
    goto loc_00A0C0DB;
loc_00A0C11E:
    goto loc_00A0C0DB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0BA74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
