# PfTCreateTraceDump

- RVA: `0x0097B450`–`0x0097BC43` (길이 `2,035` bytes)
- VA: `0x000000014097B450`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096DCC`
- 디코드: `510`개 명령, `2,035/2,035` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0097B47E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0097B4CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0097B4E6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0097B64F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0097B757` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0097B883` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0097B894` → [PfTFreeBufferList](PfTFreeBufferList_function_0097BC4C.md) (function, `0x0097BC4C`)
- `0x0097B8A0` → [PfTFreeBufferList](PfTFreeBufferList_function_0097BC4C.md) (function, `0x0097BC4C`)

### Direct callers
- [PfTGenerateTrace](PfTGenerateTrace_function_0097B3CC.md) at `0x0097B3E4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x0097B47E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0097B4CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0097B4E6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0097B64F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0097B757` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0097B883` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097B450  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0097B455  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0097B45A  53                              push rbx
0097B45B  55                              push rbp
0097B45C  56                              push rsi
0097B45D  57                              push rdi
0097B45E  41 54                           push r12
0097B460  41 55                           push r13
0097B462  41 56                           push r14
0097B464  41 57                           push r15
0097B466  48 81 EC F8 00 00 00            sub rsp, 0xf8
0097B46D  33 D2                           xor edx, edx
0097B46F  4C 8B E9                        mov r13, rcx
0097B472  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
0097B47A  44 8D 42 60                     lea r8d, [rdx + 0x60]
0097B47E  E8 BD B7 D4 FF                  call 0x1406c6c40
0097B483  4D 8D A5 98 00 00 00            lea r12, [r13 + 0x98]
0097B48A  33 F6                           xor esi, esi
0097B48C  49 8B 6C 24 08                  mov rbp, qword ptr [r12 + 8]
0097B491  49 8D 45 70                     lea rax, [r13 + 0x70]
0097B495  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0097B49A  44 8B F6                        mov r14d, esi
0097B49D  49 8B 04 24                     mov rax, qword ptr [r12]
0097B4A1  8B DE                           mov ebx, esi
0097B4A3  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0097B4A8  44 8B C6                        mov r8d, esi
0097B4AB  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0097B4B0  49 3B C4                        cmp rax, r12
0097B4B3  0F 85 E7 05 00 00               jne 0x14097baa0
0097B4B9  41 8B F8                        mov edi, r8d
0097B4BC  B9 00 01 00 00                  mov ecx, 0x100
0097B4C1  48 03 FF                        add rdi, rdi
0097B4C4  41 B8 50 66 54 74               mov r8d, 0x74546650
0097B4CA  48 8B D7                        mov rdx, rdi
0097B4CD  E8 1E 6C 20 00                  call 0x140b820f0
0097B4D2  4C 8B F8                        mov r15, rax
0097B4D5  48 85 C0                        test rax, rax
0097B4D8  0F 84 40 07 00 00               je 0x14097bc1e
0097B4DE  4C 8B C7                        mov r8, rdi
0097B4E1  33 D2                           xor edx, edx
0097B4E3  48 8B C8                        mov rcx, rax
0097B4E6  E8 55 B7 D4 FF                  call 0x1406c6c40
0097B4EB  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0097B4F0  41 BB FF FF 00 00               mov r11d, 0xffff
0097B4F6  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0097B4FB  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
0097B500  4D 8B E8                        mov r13, r8
0097B503  44 0F B7 60 24                  movzx r12d, word ptr [rax + 0x24]
0097B508  4D 8B 6D 08                     mov r13, qword ptr [r13 + 8]
0097B50C  41 83 7D 10 00                  cmp dword ptr [r13 + 0x10], 0
0097B511  0F 86 09 01 00 00               jbe 0x14097b620
0097B517  49 8D 45 1F                     lea rax, [r13 + 0x1f]
0097B51B  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097B51F  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
0097B527  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0097B530  8B D6                           mov edx, esi
0097B532  48 C1 E2 04                     shl rdx, 4
0097B536  48 03 D0                        add rdx, rax
0097B539  48 8B 0A                        mov rcx, qword ptr [rdx]
0097B53C  0F B6 C1                        movzx eax, cl
0097B53F  24 03                           and al, 3
0097B541  3C 02                           cmp al, 2
0097B543  0F 83 7D 04 00 00               jae 0x14097b9c6
0097B549  41 FF C6                        inc r14d
0097B54C  0F 57 C0                        xorps xmm0, xmm0
0097B54F  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0097B554  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
0097B55C  F6 C1 03                        test cl, 3
0097B55F  0F 85 21 04 00 00               jne 0x14097b986
0097B565  44 0F B7 42 0A                  movzx r8d, word ptr [rdx + 0xa]
0097B56A  0F B7 42 08                     movzx eax, word ptr [rdx + 8]
0097B56E  66 41 3B C3                     cmp ax, r11w
0097B572  0F 85 44 03 00 00               jne 0x14097b8bc
0097B578  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0097B57D  66 45 3B C3                     cmp r8w, r11w
0097B581  75 0A                           jne 0x14097b58d
0097B583  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0097B58B  EB 40                           jmp 0x14097b5cd
0097B58D  0F B7 4D 24                     movzx ecx, word ptr [rbp + 0x24]
0097B591  66 44 3B C1                     cmp r8w, cx
0097B595  0F 82 61 05 00 00               jb 0x14097bafc
0097B59B  8B 55 20                        mov edx, dword ptr [rbp + 0x20]
0097B59E  03 D1                           add edx, ecx
0097B5A0  45 0F B7 D8                     movzx r11d, r8w
0097B5A4  44 3B DA                        cmp r11d, edx
0097B5A7  0F 83 4F 05 00 00               jae 0x14097bafc
0097B5AD  41 8B D3                        mov edx, r11d
0097B5B0  48 2B D1                        sub rdx, rcx
0097B5B3  48 8D 4D 2F                     lea rcx, [rbp + 0x2f]
0097B5B7  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
0097B5BB  48 8D 14 92                     lea rdx, [rdx + rdx*4]
0097B5BF  48 8D 14 D1                     lea rdx, [rcx + rdx*8]
0097B5C3  48 83 C2 08                     add rdx, 8
0097B5C7  41 BB FF FF 00 00               mov r11d, 0xffff
0097B5CD  4D 85 C9                        test r9, r9
0097B5D0  74 15                           je 0x14097b5e7
0097B5D2  66 41 2B C4                     sub ax, r12w
0097B5D6  0F B7 C8                        movzx ecx, ax
0097B5D9  66 45 39 1C 4F                  cmp word ptr [r15 + rcx*2], r11w
0097B5DE  74 07                           je 0x14097b5e7
0097B5E0  66 45 89 1C 4F                  mov word ptr [r15 + rcx*2], r11w
0097B5E5  FF C3                           inc ebx
0097B5E7  48 85 D2                        test rdx, rdx
0097B5EA  74 16                           je 0x14097b602
0097B5EC  66 45 2B C4                     sub r8w, r12w
0097B5F0  41 0F B7 C0                     movzx eax, r8w
0097B5F4  66 45 39 1C 47                  cmp word ptr [r15 + rax*2], r11w
0097B5F9  74 07                           je 0x14097b602
0097B5FB  66 45 89 1C 47                  mov word ptr [r15 + rax*2], r11w
0097B600  FF C3                           inc ebx
0097B602  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
0097B60A  FF C6                           inc esi
0097B60C  41 3B 75 10                     cmp esi, dword ptr [r13 + 0x10]
0097B610  0F 82 1A FF FF FF               jb 0x14097b530
0097B616  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0097B61B  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0097B620  4D 3B 28                        cmp r13, qword ptr [r8]
0097B623  0F 85 FF 05 00 00               jne 0x14097bc28
0097B629  45 85 F6                        test r14d, r14d
0097B62C  0F 84 FD 05 00 00               je 0x14097bc2f
0097B632  41 C1 E6 04                     shl r14d, 4
0097B636  B9 00 01 00 00                  mov ecx, 0x100
0097B63B  C1 E3 05                        shl ebx, 5
0097B63E  41 B8 50 66 54 44               mov r8d, 0x44546650
0097B644  41 8D 7E 3F                     lea edi, [r14 + 0x3f]
0097B648  83 E7 F8                        and edi, 0xfffffff8
0097B64B  03 FB                           add edi, ebx
0097B64D  8B D7                           mov edx, edi
0097B64F  E8 9C 6A 20 00                  call 0x140b820f0
0097B654  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097B659  4C 8B C0                        mov r8, rax
0097B65C  48 85 C0                        test rax, rax
0097B65F  0F 84 D4 05 00 00               je 0x14097bc39
0097B665  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0097B66A  4C 8D 68 20                     lea r13, [rax + 0x20]
0097B66E  0F 57 C0                        xorps xmm0, xmm0
0097B671  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
0097B675  33 C0                           xor eax, eax
0097B677  41 0F 11 45 00                  movups xmmword ptr [r13], xmm0
0097B67C  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
0097B680  8D 47 F0                        lea eax, [rdi - 0x10]
0097B683  41 89 40 18                     mov dword ptr [r8 + 0x18], eax
0097B687  33 FF                           xor edi, edi
0097B689  41 8D 46 18                     lea eax, [r14 + 0x18]
0097B68D  41 C7 40 10 2D 00 0D 00         mov dword ptr [r8 + 0x10], 0xd002d
0097B695  8D 0C 18                        lea ecx, [rax + rbx]
0097B698  44 8B C8                        mov r9d, eax
0097B69B  41 C7 40 14 41 53 43 43         mov dword ptr [r8 + 0x14], 0x43435341
0097B6A3  4D 03 CD                        add r9, r13
0097B6A6  41 89 78 1C                     mov dword ptr [r8 + 0x1c], edi
0097B6AA  8B D7                           mov edx, edi
0097B6AC  41 89 45 08                     mov dword ptr [r13 + 8], eax
0097B6B0  8B C1                           mov eax, ecx
0097B6B2  49 03 C5                        add rax, r13
0097B6B5  41 89 4D 10                     mov dword ptr [r13 + 0x10], ecx
0097B6B9  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0097B6BE  49 8B CA                        mov rcx, r10
0097B6C1  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0097B6C9  41 C7 45 00 18 00 00 00         mov dword ptr [r13], 0x18
0097B6D1  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0097B6D6  89 94 24 58 01 00 00            mov dword ptr [rsp + 0x158], edx
0097B6DD  66 89 BC 24 50 01 00 00         mov word ptr [rsp + 0x150], di
0097B6E5  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0097B6E9  44 8B F7                        mov r14d, edi
0097B6EC  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0097B6F1  83 79 10 00                     cmp dword ptr [rcx + 0x10], 0
0097B6F5  0F 86 4B 01 00 00               jbe 0x14097b846
0097B6FB  48 8D 41 1F                     lea rax, [rcx + 0x1f]
0097B6FF  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097B703  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0097B708  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0097B710  41 8B DE                        mov ebx, r14d
0097B713  49 8D 6D 18                     lea rbp, [r13 + 0x18]
0097B717  48 C1 E3 04                     shl rbx, 4
0097B71B  48 03 D8                        add rbx, rax
0097B71E  8B F2                           mov esi, edx
0097B720  48 C1 E6 04                     shl rsi, 4
0097B724  48 03 EE                        add rbp, rsi
0097B727  48 8B 3B                        mov rdi, qword ptr [rbx]
0097B72A  40 0F B6 C7                     movzx eax, dil
0097B72E  24 03                           and al, 3
0097B730  3C 02                           cmp al, 2
0097B732  0F 83 7A 02 00 00               jae 0x14097b9b2
0097B738  BF 01 00 00 00                  mov edi, 1
0097B73D  8B C7                           mov eax, edi
0097B73F  C1 E0 04                        shl eax, 4
0097B742  44 8B C0                        mov r8d, eax
0097B745  48 03 C5                        add rax, rbp
0097B748  49 3B C1                        cmp rax, r9
0097B74B  0F 87 EE 00 00 00               ja 0x14097b83f
0097B751  48 8B D3                        mov rdx, rbx
0097B754  48 8B CD                        mov rcx, rbp
0097B757  E8 E4 B0 D4 FF                  call 0x1406c6840
0097B75C  41 01 7D 04                     add dword ptr [r13 + 4], edi
0097B760  8B 94 24 58 01 00 00            mov edx, dword ptr [rsp + 0x158]
0097B767  8B 03                           mov eax, dword ptr [rbx]
0097B769  03 D7                           add edx, edi
0097B76B  24 03                           and al, 3
0097B76D  89 94 24 58 01 00 00            mov dword ptr [rsp + 0x158], edx
0097B774  3C 02                           cmp al, 2
0097B776  75 0B                           jne 0x14097b783
0097B778  48 83 C3 10                     add rbx, 0x10
0097B77C  49 8D 6D 28                     lea rbp, [r13 + 0x28]
0097B780  48 03 EE                        add rbp, rsi
0097B783  48 8B 0B                        mov rcx, qword ptr [rbx]
0097B786  0F B6 C1                        movzx eax, cl
0097B789  24 03                           and al, 3
0097B78B  3C 02                           cmp al, 2
0097B78D  0F 83 90 00 00 00               jae 0x14097b823
0097B793  0F 57 C0                        xorps xmm0, xmm0
0097B796  BF FF FF 00 00                  mov edi, 0xffff
0097B79B  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0097B7A0  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
0097B7A8  F6 C1 03                        test cl, 3
0097B7AB  0F 85 ED 01 00 00               jne 0x14097b99e
0097B7B1  44 0F B7 43 0A                  movzx r8d, word ptr [rbx + 0xa]
0097B7B6  0F B7 53 08                     movzx edx, word ptr [rbx + 8]
0097B7BA  66 3B D7                        cmp dx, di
0097B7BD  0F 85 37 01 00 00               jne 0x14097b8fa
0097B7C3  4C 8B 5C 24 70                  mov r11, qword ptr [rsp + 0x70]
0097B7C8  66 44 3B C7                     cmp r8w, di
0097B7CC  0F 85 6B 01 00 00               jne 0x14097b93d
0097B7D2  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0097B7DA  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
0097B7DF  4D 85 DB                        test r11, r11
0097B7E2  74 19                           je 0x14097b7fd
0097B7E4  66 41 2B D4                     sub dx, r12w
0097B7E8  0F B7 C2                        movzx eax, dx
0097B7EB  41 0F B7 0C 47                  movzx ecx, word ptr [r15 + rax*2]
0097B7F0  66 3B CF                        cmp cx, di
0097B7F3  0F 84 54 02 00 00               je 0x14097ba4d
0097B7F9  66 89 4D 08                     mov word ptr [rbp + 8], cx
0097B7FD  4D 85 C9                        test r9, r9
0097B800  74 1A                           je 0x14097b81c
0097B802  66 45 2B C4                     sub r8w, r12w
0097B806  41 0F B7 C0                     movzx eax, r8w
0097B80A  41 0F B7 0C 47                  movzx ecx, word ptr [r15 + rax*2]
0097B80F  66 3B CF                        cmp cx, di
0097B812  0F 84 E7 01 00 00               je 0x14097b9ff
0097B818  66 89 4D 0A                     mov word ptr [rbp + 0xa], cx
0097B81C  8B 94 24 58 01 00 00            mov edx, dword ptr [rsp + 0x158]
0097B823  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0097B828  41 FF C6                        inc r14d
0097B82B  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0097B830  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0097B835  44 3B 71 10                     cmp r14d, dword ptr [rcx + 0x10]
0097B839  0F 82 D1 FE FF FF               jb 0x14097b710
0097B83F  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0097B844  33 FF                           xor edi, edi
0097B846  49 3B 0A                        cmp rcx, qword ptr [r10]
0097B849  0F 85 96 FE FF FF               jne 0x14097b6e5
0097B84F  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
0097B856  0F B7 8C 24 E6 00 00 00         movzx ecx, word ptr [rsp + 0xe6]
0097B85E  41 2B 45 10                     sub eax, dword ptr [r13 + 0x10]
0097B862  41 2B C5                        sub eax, r13d
0097B865  66 41 89 4D 0E                  mov word ptr [r13 + 0xe], cx
0097B86A  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
0097B872  41 89 45 14                     mov dword ptr [r13 + 0x14], eax
0097B876  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0097B87B  48 89 01                        mov qword ptr [rcx], rax
0097B87E  33 D2                           xor edx, edx
0097B880  49 8B CF                        mov rcx, r15
0097B883  E8 E8 6F 20 00                  call 0x140b82870
0097B888  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
0097B890  49 8D 4D 58                     lea rcx, [r13 + 0x58]
0097B894  E8 B3 03 00 00                  call 0x14097bc4c
0097B899  49 8D 8D 80 00 00 00            lea rcx, [r13 + 0x80]
0097B8A0  E8 A7 03 00 00                  call 0x14097bc4c
0097B8A5  8B C7                           mov eax, edi
0097B8A7  48 81 C4 F8 00 00 00            add rsp, 0xf8
0097B8AE  41 5F                           pop r15
0097B8B0  41 5E                           pop r14
0097B8B2  41 5D                           pop r13
0097B8B4  41 5C                           pop r12
0097B8B6  5F                              pop rdi
0097B8B7  5E                              pop rsi
0097B8B8  5D                              pop rbp
0097B8B9  5B                              pop rbx
0097B8BA  C3                              ret
0097B8BB  CC                              int3
0097B8BC  0F B7 4D 24                     movzx ecx, word ptr [rbp + 0x24]
0097B8C0  66 3B C1                        cmp ax, cx
0097B8C3  0F 82 E9 01 00 00               jb 0x14097bab2
0097B8C9  8B 55 20                        mov edx, dword ptr [rbp + 0x20]
0097B8CC  03 D1                           add edx, ecx
0097B8CE  44 0F B7 D0                     movzx r10d, ax
0097B8D2  44 3B D2                        cmp r10d, edx
0097B8D5  0F 83 D7 01 00 00               jae 0x14097bab2
0097B8DB  41 8B D2                        mov edx, r10d
0097B8DE  48 2B D1                        sub rdx, rcx
0097B8E1  48 8D 4D 2F                     lea rcx, [rbp + 0x2f]
0097B8E5  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
0097B8E9  48 8D 14 92                     lea rdx, [rdx + rdx*4]
0097B8ED  4C 8D 0C D1                     lea r9, [rcx + rdx*8]
0097B8F1  49 83 C1 08                     add r9, 8
0097B8F5  E9 83 FC FF FF                  jmp 0x14097b57d
0097B8FA  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
0097B8FF  0F B7 43 24                     movzx eax, word ptr [rbx + 0x24]
0097B903  66 3B D0                        cmp dx, ax
0097B906  0F 82 3D 02 00 00               jb 0x14097bb49
0097B90C  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
0097B90F  03 C8                           add ecx, eax
0097B911  44 0F B7 D2                     movzx r10d, dx
0097B915  44 3B D1                        cmp r10d, ecx
0097B918  0F 83 2B 02 00 00               jae 0x14097bb49
0097B91E  41 8B CA                        mov ecx, r10d
0097B921  48 2B C8                        sub rcx, rax
0097B924  48 8D 43 2F                     lea rax, [rbx + 0x2f]
0097B928  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097B92C  48 8D 0C 89                     lea rcx, [rcx + rcx*4]
0097B930  4C 8D 0C C8                     lea r9, [rax + rcx*8]
0097B934  4D 8D 59 08                     lea r11, [r9 + 8]
0097B938  E9 8B FE FF FF                  jmp 0x14097b7c8
0097B93D  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
0097B942  0F B7 47 24                     movzx eax, word ptr [rdi + 0x24]
0097B946  66 44 3B C0                     cmp r8w, ax
0097B94A  0F 82 44 02 00 00               jb 0x14097bb94
0097B950  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
0097B953  03 C8                           add ecx, eax
0097B955  45 0F B7 D0                     movzx r10d, r8w
0097B959  44 3B D1                        cmp r10d, ecx
0097B95C  0F 83 32 02 00 00               jae 0x14097bb94
0097B962  41 8B CA                        mov ecx, r10d
0097B965  48 2B C8                        sub rcx, rax
0097B968  48 8D 47 2F                     lea rax, [rdi + 0x2f]
0097B96C  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097B970  48 8D 0C 89                     lea rcx, [rcx + rcx*4]
0097B974  4C 8D 0C C8                     lea r9, [rax + rcx*8]
0097B978  49 83 C1 08                     add r9, 8
0097B97C  BF FF FF 00 00                  mov edi, 0xffff
0097B981  E9 54 FE FF FF                  jmp 0x14097b7da
0097B986  0F B6 0A                        movzx ecx, byte ptr [rdx]
0097B989  41 8B C3                        mov eax, r11d
0097B98C  80 E1 18                        and cl, 0x18
0097B98F  80 F9 10                        cmp cl, 0x10
0097B992  75 5B                           jne 0x14097b9ef
0097B994  44 0F B7 42 0A                  movzx r8d, word ptr [rdx + 0xa]
0097B999  E9 D0 FB FF FF                  jmp 0x14097b56e
0097B99E  80 E1 18                        and cl, 0x18
0097B9A1  8B D7                           mov edx, edi
0097B9A3  80 F9 10                        cmp cl, 0x10
0097B9A6  75 4F                           jne 0x14097b9f7
0097B9A8  44 0F B7 43 0A                  movzx r8d, word ptr [rbx + 0xa]
0097B9AD  E9 08 FE FF FF                  jmp 0x14097b7ba
0097B9B2  C1 EF 02                        shr edi, 2
0097B9B5  41 FF CE                        dec r14d
0097B9B8  81 E7 FF 03 00 00               and edi, 0x3ff
0097B9BE  44 03 F7                        add r14d, edi
0097B9C1  E9 77 FD FF FF                  jmp 0x14097b73d
0097B9C6  8B C1                           mov eax, ecx
0097B9C8  FF CE                           dec esi
0097B9CA  C1 E8 02                        shr eax, 2
0097B9CD  80 E1 03                        and cl, 3
0097B9D0  25 FF 03 00 00                  and eax, 0x3ff
0097B9D5  44 03 F0                        add r14d, eax
0097B9D8  03 F0                           add esi, eax
0097B9DA  80 F9 02                        cmp cl, 2
0097B9DD  0F 85 1F FC FF FF               jne 0x14097b602
0097B9E3  8B 4A 10                        mov ecx, dword ptr [rdx + 0x10]
0097B9E6  48 83 C2 10                     add rdx, 0x10
0097B9EA  E9 5D FB FF FF                  jmp 0x14097b54c
0097B9EF  45 8B C3                        mov r8d, r11d
0097B9F2  E9 77 FB FF FF                  jmp 0x14097b56e
0097B9F7  44 8B C7                        mov r8d, edi
0097B9FA  E9 BB FD FF FF                  jmp 0x14097b7ba
0097B9FF  0F B7 8C 24 50 01 00 00         movzx ecx, word ptr [rsp + 0x150]
0097BA07  66 41 89 0C 47                  mov word ptr [r15 + rax*2], cx
0097BA0C  8D 51 01                        lea edx, [rcx + 1]
0097BA0F  66 89 94 24 50 01 00 00         mov word ptr [rsp + 0x150], dx
0097BA17  8B D1                           mov edx, ecx
0097BA19  48 C1 E2 05                     shl rdx, 5
0097BA1D  48 8D 42 20                     lea rax, [rdx + 0x20]
0097BA21  49 03 C2                        add rax, r10
0097BA24  48 3B 44 24 40                  cmp rax, qword ptr [rsp + 0x40]
0097BA29  0F 87 D2 01 00 00               ja 0x14097bc01
0097BA2F  41 0F 10 01                     movups xmm0, xmmword ptr [r9]
0097BA33  42 0F 11 04 12                  movups xmmword ptr [rdx + r10], xmm0
0097BA38  41 0F 10 49 10                  movups xmm1, xmmword ptr [r9 + 0x10]
0097BA3D  42 0F 11 4C 12 10               movups xmmword ptr [rdx + r10 + 0x10], xmm1
0097BA43  66 41 FF 45 0C                  inc word ptr [r13 + 0xc]
0097BA48  E9 CB FD FF FF                  jmp 0x14097b818
0097BA4D  0F B7 8C 24 50 01 00 00         movzx ecx, word ptr [rsp + 0x150]
0097BA55  66 41 89 0C 47                  mov word ptr [r15 + rax*2], cx
0097BA5A  49 8D 42 20                     lea rax, [r10 + 0x20]
0097BA5E  8D 51 01                        lea edx, [rcx + 1]
0097BA61  66 89 94 24 50 01 00 00         mov word ptr [rsp + 0x150], dx
0097BA69  8B D1                           mov edx, ecx
0097BA6B  48 C1 E2 05                     shl rdx, 5
0097BA6F  48 03 C2                        add rax, rdx
0097BA72  48 3B 44 24 40                  cmp rax, qword ptr [rsp + 0x40]
0097BA77  0F 87 77 01 00 00               ja 0x14097bbf4
0097BA7D  41 0F 10 03                     movups xmm0, xmmword ptr [r11]
0097BA81  42 0F 11 04 12                  movups xmmword ptr [rdx + r10], xmm0
0097BA86  41 0F 10 4B 10                  movups xmm1, xmmword ptr [r11 + 0x10]
0097BA8B  42 0F 11 4C 12 10               movups xmmword ptr [rdx + r10 + 0x10], xmm1
0097BA91  66 41 FF 45 0C                  inc word ptr [r13 + 0xc]
0097BA96  E9 5E FD FF FF                  jmp 0x14097b7f9
0097BA9B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0097BAA0  44 03 40 20                     add r8d, dword ptr [rax + 0x20]
0097BAA4  48 8B 00                        mov rax, qword ptr [rax]
0097BAA7  49 3B C4                        cmp rax, r12
0097BAAA  0F 84 09 FA FF FF               je 0x14097b4b9
0097BAB0  EB EE                           jmp 0x14097baa0
0097BAB2  4C 8B CD                        mov r9, rbp
0097BAB5  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
0097BAB9  4C 3B CF                        cmp r9, rdi
0097BABC  75 04                           jne 0x14097bac2
0097BABE  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
0097BAC2  4C 3B CD                        cmp r9, rbp
0097BAC5  0F 84 0F 01 00 00               je 0x14097bbda
0097BACB  41 0F B7 49 24                  movzx ecx, word ptr [r9 + 0x24]
0097BAD0  66 3B C1                        cmp ax, cx
0097BAD3  72 E0                           jb 0x14097bab5
0097BAD5  41 8B 51 20                     mov edx, dword ptr [r9 + 0x20]
0097BAD9  03 D1                           add edx, ecx
0097BADB  44 0F B7 D8                     movzx r11d, ax
0097BADF  44 3B DA                        cmp r11d, edx
0097BAE2  73 D1                           jae 0x14097bab5
0097BAE4  41 8B D3                        mov edx, r11d
0097BAE7  49 8B E9                        mov rbp, r9
0097BAEA  48 2B D1                        sub rdx, rcx
0097BAED  41 BB FF FF 00 00               mov r11d, 0xffff
0097BAF3  49 8D 49 2F                     lea rcx, [r9 + 0x2f]
0097BAF7  E9 E9 FD FF FF                  jmp 0x14097b8e5
0097BAFC  4C 8B D5                        mov r10, rbp
0097BAFF  4D 8B 52 08                     mov r10, qword ptr [r10 + 8]
0097BB03  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
0097BB08  4C 3B D1                        cmp r10, rcx
0097BB0B  75 04                           jne 0x14097bb11
0097BB0D  4C 8B 51 08                     mov r10, qword ptr [rcx + 8]
0097BB11  4C 3B D5                        cmp r10, rbp
0097BB14  0F 84 CE 00 00 00               je 0x14097bbe8
0097BB1A  41 0F B7 4A 24                  movzx ecx, word ptr [r10 + 0x24]
0097BB1F  66 44 3B C1                     cmp r8w, cx
0097BB23  72 DA                           jb 0x14097baff
0097BB25  41 8B 52 20                     mov edx, dword ptr [r10 + 0x20]
0097BB29  03 D1                           add edx, ecx
0097BB2B  41 0F B7 F8                     movzx edi, r8w
0097BB2F  3B FA                           cmp edi, edx
0097BB31  73 CC                           jae 0x14097baff
0097BB33  8B D7                           mov edx, edi
0097BB35  49 8B EA                        mov rbp, r10
0097BB38  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
0097BB3D  48 2B D1                        sub rdx, rcx
0097BB40  49 8D 4A 2F                     lea rcx, [r10 + 0x2f]
0097BB44  E9 6E FA FF FF                  jmp 0x14097b5b7
0097BB49  4C 8B CB                        mov r9, rbx
0097BB4C  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
0097BB50  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
0097BB55  4C 3B C8                        cmp r9, rax
0097BB58  75 04                           jne 0x14097bb5e
0097BB5A  4C 8B 48 08                     mov r9, qword ptr [rax + 8]
0097BB5E  4C 3B CB                        cmp r9, rbx
0097BB61  0F 84 A7 00 00 00               je 0x14097bc0e
0097BB67  41 0F B7 41 24                  movzx eax, word ptr [r9 + 0x24]
0097BB6C  66 3B D0                        cmp dx, ax
0097BB6F  72 DB                           jb 0x14097bb4c
0097BB71  41 8B 49 20                     mov ecx, dword ptr [r9 + 0x20]
0097BB75  03 C8                           add ecx, eax
0097BB77  44 0F B7 DA                     movzx r11d, dx
0097BB7B  44 3B D9                        cmp r11d, ecx
0097BB7E  73 CC                           jae 0x14097bb4c
0097BB80  41 8B CB                        mov ecx, r11d
0097BB83  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0097BB88  48 2B C8                        sub rcx, rax
0097BB8B  49 8D 41 2F                     lea rax, [r9 + 0x2f]
0097BB8F  E9 94 FD FF FF                  jmp 0x14097b928
0097BB94  4C 8B CF                        mov r9, rdi
0097BB97  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
0097BB9B  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
0097BBA0  4C 3B C8                        cmp r9, rax
0097BBA3  75 04                           jne 0x14097bba9
0097BBA5  4C 8B 48 08                     mov r9, qword ptr [rax + 8]
0097BBA9  4C 3B CF                        cmp r9, rdi
0097BBAC  74 68                           je 0x14097bc16
0097BBAE  41 0F B7 41 24                  movzx eax, word ptr [r9 + 0x24]
0097BBB3  66 44 3B C0                     cmp r8w, ax
0097BBB7  72 DE                           jb 0x14097bb97
0097BBB9  41 8B 49 20                     mov ecx, dword ptr [r9 + 0x20]
0097BBBD  03 C8                           add ecx, eax
0097BBBF  41 0F B7 D8                     movzx ebx, r8w
0097BBC3  3B D9                           cmp ebx, ecx
0097BBC5  73 D0                           jae 0x14097bb97
0097BBC7  8B CB                           mov ecx, ebx
0097BBC9  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0097BBCE  48 2B C8                        sub rcx, rax
0097BBD1  49 8D 41 2F                     lea rax, [r9 + 0x2f]
0097BBD5  E9 92 FD FF FF                  jmp 0x14097b96c
0097BBDA  45 33 C9                        xor r9d, r9d
0097BBDD  41 BB FF FF 00 00               mov r11d, 0xffff
0097BBE3  E9 95 F9 FF FF                  jmp 0x14097b57d
0097BBE8  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
0097BBED  33 D2                           xor edx, edx
0097BBEF  E9 D3 F9 FF FF                  jmp 0x14097b5c7
0097BBF4  66 89 8C 24 50 01 00 00         mov word ptr [rsp + 0x150], cx
0097BBFC  E9 F8 FB FF FF                  jmp 0x14097b7f9
0097BC01  66 89 8C 24 50 01 00 00         mov word ptr [rsp + 0x150], cx
0097BC09  E9 0A FC FF FF                  jmp 0x14097b818
0097BC0E  45 33 DB                        xor r11d, r11d
0097BC11  E9 B2 FB FF FF                  jmp 0x14097b7c8
0097BC16  45 33 C9                        xor r9d, r9d
0097BC19  E9 5E FD FF FF                  jmp 0x14097b97c
0097BC1E  BF 9A 00 00 C0                  mov edi, 0xc000009a
0097BC23  E9 68 FC FF FF                  jmp 0x14097b890
0097BC28  33 F6                           xor esi, esi
0097BC2A  E9 D9 F8 FF FF                  jmp 0x14097b508
0097BC2F  BF 1A 00 00 80                  mov edi, 0x8000001a
0097BC34  E9 45 FC FF FF                  jmp 0x14097b87e
0097BC39  BF 9A 00 00 C0                  mov edi, 0xc000009a
0097BC3E  E9 3B FC FF FF                  jmp 0x14097b87e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfTCreateTraceDump(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int16 v_stack_m52;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int16 v_stack_p150;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (248);
    a2 = 0;
    result = memset(v_stack_mA8, a2, a2 + 96, a4);
    v_rsi = 0;
    v_stack_m100 = a1 + 112;
    v_stack_m118 = a1 + 152;
    v_stack_m110 = *(unsigned __int64 *)(a1 + 152 + 8);
    if ((*(unsigned __int64 *)(a1 + 152)) != (a1 + 152)) goto loc_0097BAA0;
loc_0097B4B9:
    v_rdi = (0) + (0);
    result = ExAllocatePool2(256, v_rdi, (unsigned int)(0x74546650ULL), a4);
    if (result == 0) goto loc_0097BC1E;
    a2 = 0;
    result = memset(result, a2, v_rdi, a4);
loc_0097B508:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m100 + 8) + 16)) <= 0) goto loc_0097B620;
    result = (*(unsigned __int64 *)(v_stack_m100 + 8) + 31) & (-8);
    v_stack_p18 = result;
loc_0097B530:
    a2 = (0) << (4);
    a2 = (a2) + (result);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(a2))) & (3));
    if (((unsigned __int8)(result)) >= 2) goto loc_0097B9C6;
    v_r14 = (unsigned int)((0) + 1);
loc_0097B54C:
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (3)) != 0) goto loc_0097B986;
loc_0097B56E:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 8))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097B8BC;
loc_0097B57D:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 10))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097B58D;
    goto loc_0097B5CD;
loc_0097B58D:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 10))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36)))) goto loc_0097BAFC;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152 + 8) + 32))) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))));
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2 + 10)))) >= ((unsigned int)(a2))) goto loc_0097BAFC;
    a2 = ((unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2 + 10))))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36));
loc_0097B5B7:
    a1 = (*(unsigned __int64 *)(a1 + 152 + 8) + 47) & (-8);
    a2 = (a1 + a2 + a2 * 4 * 8) + (8);
loc_0097B5C7:
loc_0097B5CD:
    if (v_stack_mC8 == 0) goto loc_0097B5E7;
    result = (unsigned __int16)((*(unsigned __int16 *)(a2 + 8)) - ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))));
    v_rbx = 0;
    if ((*(unsigned __int16 *)(result + (unsigned __int16)(result) * 2)) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        *(unsigned __int16 *)(result + (unsigned __int16)(result) * 2) = (unsigned __int16)((unsigned int)(0xFFFFULL));
        v_rbx = (unsigned int)((0) + 1);
    }
    if (a2 == 0) goto loc_0097B602;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(a2 + 10)) - ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))));
    if ((*(unsigned __int16 *)(result + (unsigned __int16)(a3) * 2)) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        *(unsigned __int16 *)(result + (unsigned __int16)(a3) * 2) = (unsigned __int16)((unsigned int)(0xFFFFULL));
        v_rbx = (unsigned int)((v_rbx) + 1);
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m100 + 8) + 16))) goto loc_0097B530;
    v_stack_m110 = *(unsigned __int64 *)(a1 + 152 + 8);
loc_0097B620:
    if ((*(unsigned __int64 *)(v_stack_m100 + 8)) != (*(unsigned __int64 *)(v_stack_m100))) goto loc_0097BC28;
    if ((unsigned int)(v_r14) == 0) goto loc_0097BC2F;
    v_r14 = (unsigned int)((v_r14) << (4));
    v_rbx = (unsigned int)((v_rbx) << (5));
    v_rdi = (unsigned int)((v_r14 + 63) & (0xFFFFFFF8ULL));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rbx)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x44546650ULL), v_stack_mC8);
    v_stack_mE0 = result;
    if (result == 0) goto loc_0097BC39;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 32 + 16) = 0;
    *(unsigned int *)(result + 24) = (unsigned int)(v_rdi - 16);
    v_rdi = 0;
    *(unsigned int *)(result + 16) = 0xD002DULL;
    *(unsigned int *)(result + 20) = 0x43435341ULL;
    a4 = ((unsigned int)((unsigned int)(v_r14 + 24))) + (result + 32);
    *(unsigned int *)(result + 28) = 0;
    *(unsigned int *)(result + 32 + 8) = (unsigned int)(v_r14 + 24);
    result = ((unsigned int)((unsigned int)(v_r14 + 24 + v_rbx * 1))) + (result + 32);
    *(unsigned int *)(result + 32 + 16) = (unsigned int)(v_r14 + 24 + v_rbx * 1);
    v_stack_mF8 = result;
    v_stack_m60 = result;
    *(unsigned int *)(result + 32) = 24;
    v_stack_m108 = a4;
    v_stack_p20 = 0;
    v_stack_p18 = 0;
loc_0097B6E5:
    v_stack_mF0 = *(unsigned __int64 *)(v_stack_m100 + 8);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m100 + 8) + 16)) <= 0) goto loc_0097B846;
    result = (*(unsigned __int64 *)(v_stack_m100 + 8) + 31) & (-8);
    v_stack_mE8 = result;
loc_0097B710:
    v_rbx = (0) << (4);
    v_rbx = (v_rbx) + (result);
    v_rsi = (0) << (4);
    v_rbp = (result + 32 + 24) + (v_rsi);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (3));
    if (((unsigned __int8)(result)) >= 2) goto loc_0097B9B2;
loc_0097B73D:
    result = (unsigned int)((1) << (4));
    result = (result) + (v_rbp);
    if (result > a4) goto loc_0097B83F;
    result = memcpy(v_rbp, v_rbx, (unsigned int)((unsigned int)(result)), a4);
    a2 = (unsigned int)(((unsigned int)(v_stack_p20)) + (1));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rbx))) & (3));
    v_stack_p20 = (unsigned int)(a2);
    if (((unsigned __int8)(result)) == 2) {
        v_rbx = (v_rbx) + (16);
        v_rbp = result + 32 + 40;
        v_rbp = (v_rbp) + (v_rsi);
    }
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (3));
    if (((unsigned __int8)(result)) >= 2) goto loc_0097B823;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (3)) != 0) goto loc_0097B99E;
loc_0097B7BA:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 8))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097B8FA;
loc_0097B7C8:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 10))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097B93D;
loc_0097B7DA:
    if (v_stack_mC8 == 0) goto loc_0097B7FD;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 8)) - ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))));
    if (((unsigned __int16)(*(unsigned __int16 *)(result + (unsigned __int16)(a2) * 2))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097BA4D;
loc_0097B7F9:
    *(unsigned __int16 *)(v_rbp + 8) = (unsigned __int16)(*(unsigned __int16 *)(result + (unsigned __int16)(a2) * 2));
loc_0097B7FD:
    if (v_stack_mB0 == 0) goto loc_0097B81C;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 10)) - ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))));
    if (((unsigned __int16)(*(unsigned __int16 *)(result + (unsigned __int16)(a3) * 2))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097B9FF;
loc_0097B818:
    *(unsigned __int16 *)(v_rbp + 10) = (unsigned __int16)(*(unsigned __int16 *)(result + (unsigned __int16)(a3) * 2));
loc_0097B81C:
loc_0097B823:
    v_r14 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r14)) < (*(unsigned int *)(v_stack_mF0 + 16))) goto loc_0097B710;
loc_0097B83F:
    v_rdi = 0;
loc_0097B846:
    if (v_stack_mF0 != (*(unsigned __int64 *)(v_stack_m100))) goto loc_0097B6E5;
    result = (unsigned int)(((unsigned int)(v_stack_m60)) - (*(unsigned int *)(result + 32 + 16)));
    result = (unsigned int)((result) - ((unsigned int)(result + 32)));
    *(unsigned __int16 *)(result + 32 + 14) = (unsigned __int16)(v_stack_m52);
    *(unsigned int *)(result + 32 + 20) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_p10) = v_stack_mE0;
loc_0097B87E:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, v_stack_m108);
loc_0097B890:
    result = PfTFreeBufferList(v_stack_p8 + 88, a2, a3, v_stack_m108);
    result = PfTFreeBufferList(v_stack_p8 + 128, a2, a3, v_stack_m108);
    v_rsp = (v_rsp) + (248);
    return 0;
loc_0097B8BC:
    if (0 < ((unsigned __int16)(*(unsigned __int16 *)(v_rbp + 36)))) goto loc_0097BAB2;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 32))) + ((unsigned int)(*(unsigned __int16 *)(v_rbp + 36))));
    if (0 >= ((unsigned int)(a2))) goto loc_0097BAB2;
    a2 = (0) - (*(unsigned __int16 *)(v_rbp + 36));
loc_0097B8E5:
    a1 = (v_rbp + 47) & (-8);
    a4 = (a1 + a2 + a2 * 4 * 8) + (8);
    goto loc_0097B57D;
loc_0097B8FA:
    if (((unsigned __int16)(a2 + a2 * 4)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p28 + 36)))) goto loc_0097BB49;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p28 + 32))) + ((unsigned int)(*(unsigned __int16 *)(v_stack_p28 + 36))));
    if (((unsigned int)((unsigned __int16)(a2 + a2 * 4))) >= ((unsigned int)(a1))) goto loc_0097BB49;
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(a2 + a2 * 4)))) - (*(unsigned __int16 *)(v_stack_p28 + 36));
loc_0097B928:
    result = (v_stack_p28 + 47) & (-8);
    goto loc_0097B7C8;
loc_0097B93D:
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p28 + 36)))) goto loc_0097BB94;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p28 + 32))) + ((unsigned int)(*(unsigned __int16 *)(v_stack_p28 + 36))));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a1))) goto loc_0097BB94;
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(a3)))) - (*(unsigned __int16 *)(v_stack_p28 + 36));
loc_0097B96C:
    result = (v_stack_p28 + 47) & (-8);
    a4 = (result + a1 + a1 * 4 * 8) + (8);
loc_0097B97C:
    goto loc_0097B7DA;
loc_0097B986:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a2 + a2 * 4)) & (24));
    if (((unsigned __int8)(a1)) != 16) goto loc_0097B9EF;
    goto loc_0097B56E;
loc_0097B99E:
    a1 = (unsigned __int8)((a1) & (24));
    if (((unsigned __int8)(a1)) != 16) goto loc_0097B9F7;
    goto loc_0097B7BA;
loc_0097B9B2:
    v_rdi = (unsigned int)(((unsigned int)(0xFFFFULL)) >> (2));
    v_r14 = (unsigned int)((v_r14) - 1);
    v_rdi = (unsigned int)((v_rdi) & (0x3FFULL));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_rdi)));
    goto loc_0097B73D;
loc_0097B9C6:
    v_rsi = (unsigned int)((v_rsi) - 1);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) >> (2));
    a1 = (unsigned __int8)((a1) & (3));
    result = (unsigned int)((result) & (0x3FFULL));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    if (((unsigned __int8)(a1)) != 2) goto loc_0097B602;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0xFFFFULL)))) + (16);
    goto loc_0097B54C;
loc_0097B9EF:
    goto loc_0097B56E;
loc_0097B9F7:
    goto loc_0097B7BA;
loc_0097B9FF:
    *(unsigned __int16 *)(result + result * 2) = (unsigned __int16)(v_stack_p150);
    v_stack_p150 = (unsigned __int16)(v_stack_p150 + 1);
    a2 = ((unsigned int)((unsigned int)(v_stack_p150))) << (5);
    result = (a2 + 32) + ((unsigned __int16)(a3));
    if (result > v_stack_p40) goto loc_0097BC01;
    *(unsigned __int64 *)(a2 + (unsigned __int16)(a3) * 1) = v_xmm0;
    *(unsigned __int64 *)(a2 + (unsigned __int16)(a3) * 1 + 16) = v_xmm1;
    goto loc_0097B818;
loc_0097BA4D:
    *(unsigned __int16 *)(result + result * 2) = (unsigned __int16)(v_stack_p150);
    v_stack_p150 = (unsigned __int16)(v_stack_p150 + 1);
    a2 = ((unsigned int)((unsigned int)(v_stack_p150))) << (5);
    result = ((unsigned __int16)(a3) + 32) + (a2);
    if (result > v_stack_p40) goto loc_0097BBF4;
    *(unsigned __int64 *)(a2 + (unsigned __int16)(a3) * 1) = v_xmm0;
    *(unsigned __int64 *)(a2 + (unsigned __int16)(a3) * 1 + 16) = v_xmm1;
    goto loc_0097B7F9;
loc_0097BAA0:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + (*(unsigned int *)(result + 32)));
    if ((*(unsigned __int64 *)(result)) == (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152 + 8) + 36))) goto loc_0097B4B9;
    goto loc_0097BAA0;
loc_0097BAB2:
loc_0097BAB5:
    if ((*(unsigned __int64 *)(v_rbp + 8)) == v_rdi) {
        a4 = *(unsigned __int64 *)(v_rdi + 8);
    }
    if (a4 == v_rbp) goto loc_0097BBDA;
    if (((unsigned __int16)(*(unsigned __int64 *)(result))) < ((unsigned __int16)(*(unsigned __int16 *)(a4 + 36)))) goto loc_0097BAB5;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 32))) + ((unsigned int)(*(unsigned __int16 *)(a4 + 36))));
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result)))) >= ((unsigned int)(a2))) goto loc_0097BAB5;
    a2 = ((unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result))))) - (*(unsigned __int16 *)(a4 + 36));
    goto loc_0097B8E5;
loc_0097BAFC:
loc_0097BAFF:
    v_r10 = *(unsigned __int64 *)(a4 + 8);
    if ((*(unsigned __int64 *)(a4 + 8)) == v_stack_p20) {
        v_r10 = *(unsigned __int64 *)(v_stack_p20 + 8);
    }
    if (v_r10 == a4) goto loc_0097BBE8;
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(*(unsigned __int16 *)(v_r10 + 36)))) goto loc_0097BAFF;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + 32))) + ((unsigned int)(*(unsigned __int16 *)(v_r10 + 36))));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a2))) goto loc_0097BAFF;
    a2 = ((unsigned int)((unsigned int)((unsigned __int16)(a3)))) - (*(unsigned __int16 *)(v_r10 + 36));
    goto loc_0097B5B7;
loc_0097BB49:
loc_0097BB4C:
    if ((*(unsigned __int64 *)(v_stack_p28 + 8)) == v_stack_p20) {
        a4 = *(unsigned __int64 *)(v_stack_p20 + 8);
    }
    if (a4 == v_stack_p28) goto loc_0097BC0E;
    if (((unsigned __int16)(a2)) < ((unsigned __int16)(*(unsigned __int16 *)(a4 + 36)))) goto loc_0097BB4C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 32))) + ((unsigned int)(*(unsigned __int16 *)(a4 + 36))));
    if (((unsigned int)((unsigned __int16)(a2))) >= ((unsigned int)(a1))) goto loc_0097BB4C;
    v_stack_p28 = a4;
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(a2)))) - (*(unsigned __int16 *)(a4 + 36));
    goto loc_0097B928;
loc_0097BB94:
loc_0097BB97:
    if ((*(unsigned __int64 *)(v_stack_p20 + 8)) == v_stack_p20) {
        a4 = *(unsigned __int64 *)(v_stack_p20 + 8);
    }
    if (a4 == v_stack_p20) goto loc_0097BC16;
    if (((unsigned __int16)(a3)) < ((unsigned __int16)(*(unsigned __int16 *)(a4 + 36)))) goto loc_0097BB97;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 32))) + ((unsigned int)(*(unsigned __int16 *)(a4 + 36))));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a1))) goto loc_0097BB97;
    v_stack_p28 = a4;
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(a3)))) - (*(unsigned __int16 *)(a4 + 36));
    goto loc_0097B96C;
loc_0097BBDA:
    a4 = 0;
    goto loc_0097B57D;
loc_0097BBE8:
    a2 = 0;
    goto loc_0097B5C7;
loc_0097BBF4:
    v_stack_p150 = (unsigned __int16)(a1);
    goto loc_0097B7F9;
loc_0097BC01:
    v_stack_p150 = (unsigned __int16)(a1);
    goto loc_0097B818;
loc_0097BC0E:
    v_r11 = 0;
    goto loc_0097B7C8;
loc_0097BC16:
    a4 = 0;
    goto loc_0097B97C;
loc_0097BC1E:
    goto loc_0097B890;
loc_0097BC28:
    v_rsi = 0;
    goto loc_0097B508;
loc_0097BC2F:
    goto loc_0097B87E;
loc_0097BC39:
    goto loc_0097B87E;
}
```

## 5. (Beta) C Style

```c
int64_t PfTCreateTraceDump(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint16_t v_stack_m52;
    uint64_t v_stack_m60;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint16_t v_stack_p150;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (248);
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, Arg2 + 96, a4);
    local_rsi = 0;
    v_stack_m100 = Arg1 + 112;
    v_stack_m118 = Arg1 + 152;
    v_stack_m110 = *(uint64_t *)(arg1 + 0x98 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x98)) != (Arg1 + 152)) goto loc_0097BAA0;
loc_0097B4B9:
    local_rdi = (0) + (0);
    result = ExAllocatePool2(256, local_rdi, (uint32_t)(0x74546650ULL), a4);
    if (result == 0) goto loc_0097BC1E;
    Arg2 = 0;
    result = memset(result, Arg2, local_rdi, a4);
loc_0097B508:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m100 + 0x8) + 0x10)) <= 0) goto loc_0097B620;
    result = (*(uint64_t *)(v_stack_m100 + 0x8) + 31) & (-8);
    v_stack_p18 = result;
loc_0097B530:
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (result);
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(Arg2))) & (3));
    if (((uint8_t)(result)) >= 2) goto loc_0097B9C6;
    local_r14 = (uint32_t)((0) + 1);
loc_0097B54C:
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if ((((uint8_t)(*(uint64_t *)(Arg2))) & (3)) != 0) goto loc_0097B986;
loc_0097B56E:
    if (((uint16_t)(*(uint16_t *)(Arg2 + 0x8))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097B8BC;
loc_0097B57D:
    if (((uint16_t)(*(uint16_t *)(Arg2 + 0xA))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097B58D;
    goto loc_0097B5CD;
loc_0097B58D:
    if (((uint16_t)(*(uint16_t *)(Arg2 + 0xA))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24)))) goto loc_0097BAFC;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x20))) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))));
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg2 + 0xA)))) >= ((uint32_t)(Arg2))) goto loc_0097BAFC;
    Arg2 = ((uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg2 + 0xA))))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24));
loc_0097B5B7:
    Arg1 = (*(uint64_t *)(arg1 + 0x98 + 0x8) + 47) & (-8);
    Arg2 = (Arg1 + Arg2 + Arg2 * 4 * 8) + (8);
loc_0097B5C7:
loc_0097B5CD:
    if (v_stack_mC8 == 0) goto loc_0097B5E7;
    result = (uint16_t)((*(uint16_t *)(Arg2 + 0x8)) - ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))));
    local_rbx = 0;
    if ((*(uint16_t *)(result + (uint16_t)(result) * 2)) != ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        *(uint16_t *)(result + (uint16_t)(result) * 2) = (uint16_t)((uint32_t)(0xFFFFULL));
        local_rbx = (uint32_t)((0) + 1);
    }
    if (Arg2 == 0) goto loc_0097B602;
    a3 = (uint16_t)((*(uint16_t *)(Arg2 + 0xA)) - ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))));
    if ((*(uint16_t *)(result + (uint16_t)(a3) * 2)) != ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        *(uint16_t *)(result + (uint16_t)(a3) * 2) = (uint16_t)((uint32_t)(0xFFFFULL));
        local_rbx = (uint32_t)((local_rbx) + 1);
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(v_stack_m100 + 0x8) + 0x10))) goto loc_0097B530;
    v_stack_m110 = *(uint64_t *)(arg1 + 0x98 + 0x8);
loc_0097B620:
    if ((*(uint64_t *)(v_stack_m100 + 0x8)) != (*(uint64_t *)(v_stack_m100))) goto loc_0097BC28;
    if ((uint32_t)(local_r14) == 0) goto loc_0097BC2F;
    local_r14 = (uint32_t)((local_r14) << (4));
    local_rbx = (uint32_t)((local_rbx) << (5));
    local_rdi = (uint32_t)((local_r14 + 63) & (0xFFFFFFF8ULL));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rbx)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x44546650ULL), v_stack_mC8);
    v_stack_mE0 = result;
    if (result == 0) goto loc_0097BC39;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    result = 0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x20 + 0x10) = 0;
    *(uint32_t *)(result + 0x18) = (uint32_t)(local_rdi - 16);
    local_rdi = 0;
    *(uint32_t *)(result + 0x10) = 0xD002DULL;
    *(uint32_t *)(result + 0x14) = 0x43435341ULL;
    a4 = ((uint32_t)((uint32_t)(local_r14 + 24))) + (result + 32);
    *(uint32_t *)(result + 0x1C) = 0;
    *(uint32_t *)(result + 0x20 + 0x8) = (uint32_t)(local_r14 + 24);
    result = ((uint32_t)((uint32_t)(local_r14 + 24 + local_rbx * 1))) + (result + 32);
    *(uint32_t *)(result + 0x20 + 0x10) = (uint32_t)(local_r14 + 24 + local_rbx * 1);
    v_stack_mF8 = result;
    v_stack_m60 = result;
    *(uint32_t *)(result + 0x20) = 24;
    v_stack_m108 = a4;
    v_stack_p20 = 0;
    v_stack_p18 = 0;
loc_0097B6E5:
    v_stack_mF0 = *(uint64_t *)(v_stack_m100 + 0x8);
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m100 + 0x8) + 0x10)) <= 0) goto loc_0097B846;
    result = (*(uint64_t *)(v_stack_m100 + 0x8) + 31) & (-8);
    v_stack_mE8 = result;
loc_0097B710:
    local_rbx = (0) << (4);
    local_rbx = (local_rbx) + (result);
    local_rsi = (0) << (4);
    local_rbp = (result + 32 + 24) + (local_rsi);
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_rbx))) & (3));
    if (((uint8_t)(result)) >= 2) goto loc_0097B9B2;
loc_0097B73D:
    result = (uint32_t)((1) << (4));
    result = (result) + (local_rbp);
    if (result > a4) goto loc_0097B83F;
    result = memcpy(local_rbp, local_rbx, (uint32_t)((uint32_t)(result)), a4);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p20)) + (1));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rbx))) & (3));
    v_stack_p20 = (uint32_t)(Arg2);
    if (((uint8_t)(result)) == 2) {
        local_rbx = (local_rbx) + (16);
        local_rbp = result + 32 + 40;
        local_rbp = (local_rbp) + (local_rsi);
    }
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_rbx))) & (3));
    if (((uint8_t)(result)) >= 2) goto loc_0097B823;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (3)) != 0) goto loc_0097B99E;
loc_0097B7BA:
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x8))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097B8FA;
loc_0097B7C8:
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0xA))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097B93D;
loc_0097B7DA:
    if (v_stack_mC8 == 0) goto loc_0097B7FD;
    Arg2 = (uint16_t)((*(uint16_t *)(local_rbx + 0x8)) - ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))));
    if (((uint16_t)(*(uint16_t *)(result + (uint16_t)(Arg2) * 2))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097BA4D;
loc_0097B7F9:
    *(uint16_t *)(local_rbp + 0x8) = (uint16_t)(*(uint16_t *)(result + (uint16_t)(Arg2) * 2));
loc_0097B7FD:
    if (v_stack_mB0 == 0) goto loc_0097B81C;
    a3 = (uint16_t)((*(uint16_t *)(local_rbx + 0xA)) - ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))));
    if (((uint16_t)(*(uint16_t *)(result + (uint16_t)(a3) * 2))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097B9FF;
loc_0097B818:
    *(uint16_t *)(local_rbp + 0xA) = (uint16_t)(*(uint16_t *)(result + (uint16_t)(a3) * 2));
loc_0097B81C:
loc_0097B823:
    local_r14 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r14)) < (*(uint32_t *)(v_stack_mF0 + 0x10))) goto loc_0097B710;
loc_0097B83F:
    local_rdi = 0;
loc_0097B846:
    if (v_stack_mF0 != (*(uint64_t *)(v_stack_m100))) goto loc_0097B6E5;
    result = (uint32_t)(((uint32_t)(v_stack_m60)) - (*(uint32_t *)(result + 0x20 + 0x10)));
    result = (uint32_t)((result) - ((uint32_t)(result + 32)));
    *(uint16_t *)(result + 0x20 + 0xE) = (uint16_t)(v_stack_m52);
    *(uint32_t *)(result + 0x20 + 0x14) = (uint32_t)(result);
    *(uint64_t *)(v_stack_p10) = v_stack_mE0;
loc_0097B87E:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, v_stack_m108);
loc_0097B890:
    result = PfTFreeBufferList(v_stack_p8 + 88, Arg2, a3, v_stack_m108);
    result = PfTFreeBufferList(v_stack_p8 + 128, Arg2, a3, v_stack_m108);
    local_rsp = (local_rsp) + (248);
    return 0;
loc_0097B8BC:
    if (0 < ((uint16_t)(*(uint16_t *)(local_rbp + 0x24)))) goto loc_0097BAB2;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x20))) + ((uint32_t)(*(uint16_t *)(local_rbp + 0x24))));
    if (0 >= ((uint32_t)(Arg2))) goto loc_0097BAB2;
    Arg2 = (0) - (*(uint16_t *)(local_rbp + 0x24));
loc_0097B8E5:
    Arg1 = (local_rbp + 47) & (-8);
    a4 = (Arg1 + Arg2 + Arg2 * 4 * 8) + (8);
    goto loc_0097B57D;
loc_0097B8FA:
    if (((uint16_t)(Arg2 + Arg2 * 4)) < ((uint16_t)(*(uint16_t *)(v_stack_p28 + 0x24)))) goto loc_0097BB49;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p28 + 0x20))) + ((uint32_t)(*(uint16_t *)(v_stack_p28 + 0x24))));
    if (((uint32_t)((uint16_t)(Arg2 + Arg2 * 4))) >= ((uint32_t)(Arg1))) goto loc_0097BB49;
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(Arg2 + Arg2 * 4)))) - (*(uint16_t *)(v_stack_p28 + 0x24));
loc_0097B928:
    result = (v_stack_p28 + 47) & (-8);
    goto loc_0097B7C8;
loc_0097B93D:
    if (((uint16_t)(a3)) < ((uint16_t)(*(uint16_t *)(v_stack_p28 + 0x24)))) goto loc_0097BB94;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p28 + 0x20))) + ((uint32_t)(*(uint16_t *)(v_stack_p28 + 0x24))));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg1))) goto loc_0097BB94;
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(a3)))) - (*(uint16_t *)(v_stack_p28 + 0x24));
loc_0097B96C:
    result = (v_stack_p28 + 47) & (-8);
    a4 = (result + Arg1 + Arg1 * 4 * 8) + (8);
loc_0097B97C:
    goto loc_0097B7DA;
loc_0097B986:
    Arg1 = (uint8_t)((*(uint8_t *)(Arg2 + Arg2 * 4)) & (24));
    if (((uint8_t)(Arg1)) != 16) goto loc_0097B9EF;
    goto loc_0097B56E;
loc_0097B99E:
    Arg1 = (uint8_t)((Arg1) & (24));
    if (((uint8_t)(Arg1)) != 16) goto loc_0097B9F7;
    goto loc_0097B7BA;
loc_0097B9B2:
    local_rdi = (uint32_t)(((uint32_t)(0xFFFFULL)) >> (2));
    local_r14 = (uint32_t)((local_r14) - 1);
    local_rdi = (uint32_t)((local_rdi) & (0x3FFULL));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_rdi)));
    goto loc_0097B73D;
loc_0097B9C6:
    local_rsi = (uint32_t)((local_rsi) - 1);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) >> (2));
    Arg1 = (uint8_t)((Arg1) & (3));
    result = (uint32_t)((result) & (0x3FFULL));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    if (((uint8_t)(Arg1)) != 2) goto loc_0097B602;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0xFFFFULL)))) + (16);
    goto loc_0097B54C;
loc_0097B9EF:
    goto loc_0097B56E;
loc_0097B9F7:
    goto loc_0097B7BA;
loc_0097B9FF:
    *(uint16_t *)(result + result * 2) = (uint16_t)(v_stack_p150);
    v_stack_p150 = (uint16_t)(v_stack_p150 + 1);
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p150))) << (5);
    result = (Arg2 + 32) + ((uint16_t)(a3));
    if (result > v_stack_p40) goto loc_0097BC01;
    *(uint64_t *)(Arg2 + (uint16_t)(a3) * 1) = v_xmm0;
    *(uint64_t *)(Arg2 + (uint16_t)(a3) * 1 + 0x10) = v_xmm1;
    goto loc_0097B818;
loc_0097BA4D:
    *(uint16_t *)(result + result * 2) = (uint16_t)(v_stack_p150);
    v_stack_p150 = (uint16_t)(v_stack_p150 + 1);
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p150))) << (5);
    result = ((uint16_t)(a3) + 32) + (Arg2);
    if (result > v_stack_p40) goto loc_0097BBF4;
    *(uint64_t *)(Arg2 + (uint16_t)(a3) * 1) = v_xmm0;
    *(uint64_t *)(Arg2 + (uint16_t)(a3) * 1 + 0x10) = v_xmm1;
    goto loc_0097B7F9;
loc_0097BAA0:
    a3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + (*(uint32_t *)(result + 0x20)));
    if ((*(uint64_t *)(result)) == (*(uint16_t *)(*(uint64_t *)(arg1 + 0x98 + 0x8) + 0x24))) goto loc_0097B4B9;
    goto loc_0097BAA0;
loc_0097BAB2:
loc_0097BAB5:
    if ((*(uint64_t *)(local_rbp + 0x8)) == local_rdi) {
        a4 = *(uint64_t *)(local_rdi + 0x8);
    }
    if (a4 == local_rbp) goto loc_0097BBDA;
    if (((uint16_t)(*(uint64_t *)(result))) < ((uint16_t)(*(uint16_t *)(a4 + 0x24)))) goto loc_0097BAB5;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + 0x20))) + ((uint32_t)(*(uint16_t *)(a4 + 0x24))));
    if (((uint32_t)((uint16_t)(*(uint64_t *)(result)))) >= ((uint32_t)(Arg2))) goto loc_0097BAB5;
    Arg2 = ((uint32_t)((uint32_t)((uint16_t)(*(uint64_t *)(result))))) - (*(uint16_t *)(a4 + 0x24));
    goto loc_0097B8E5;
loc_0097BAFC:
loc_0097BAFF:
    local_r10 = *(uint64_t *)(a4 + 0x8);
    if ((*(uint64_t *)(a4 + 0x8)) == v_stack_p20) {
        local_r10 = *(uint64_t *)(v_stack_p20 + 0x8);
    }
    if (local_r10 == a4) goto loc_0097BBE8;
    if (((uint16_t)(a3)) < ((uint16_t)(*(uint16_t *)(local_r10 + 0x24)))) goto loc_0097BAFF;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + 0x20))) + ((uint32_t)(*(uint16_t *)(local_r10 + 0x24))));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg2))) goto loc_0097BAFF;
    Arg2 = ((uint32_t)((uint32_t)((uint16_t)(a3)))) - (*(uint16_t *)(local_r10 + 0x24));
    goto loc_0097B5B7;
loc_0097BB49:
loc_0097BB4C:
    if ((*(uint64_t *)(v_stack_p28 + 0x8)) == v_stack_p20) {
        a4 = *(uint64_t *)(v_stack_p20 + 0x8);
    }
    if (a4 == v_stack_p28) goto loc_0097BC0E;
    if (((uint16_t)(Arg2)) < ((uint16_t)(*(uint16_t *)(a4 + 0x24)))) goto loc_0097BB4C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + 0x20))) + ((uint32_t)(*(uint16_t *)(a4 + 0x24))));
    if (((uint32_t)((uint16_t)(Arg2))) >= ((uint32_t)(Arg1))) goto loc_0097BB4C;
    v_stack_p28 = a4;
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(Arg2)))) - (*(uint16_t *)(a4 + 0x24));
    goto loc_0097B928;
loc_0097BB94:
loc_0097BB97:
    if ((*(uint64_t *)(v_stack_p20 + 0x8)) == v_stack_p20) {
        a4 = *(uint64_t *)(v_stack_p20 + 0x8);
    }
    if (a4 == v_stack_p20) goto loc_0097BC16;
    if (((uint16_t)(a3)) < ((uint16_t)(*(uint16_t *)(a4 + 0x24)))) goto loc_0097BB97;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + 0x20))) + ((uint32_t)(*(uint16_t *)(a4 + 0x24))));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg1))) goto loc_0097BB97;
    v_stack_p28 = a4;
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(a3)))) - (*(uint16_t *)(a4 + 0x24));
    goto loc_0097B96C;
loc_0097BBDA:
    a4 = 0;
    goto loc_0097B57D;
loc_0097BBE8:
    Arg2 = 0;
    goto loc_0097B5C7;
loc_0097BBF4:
    v_stack_p150 = (uint16_t)(Arg1);
    goto loc_0097B7F9;
loc_0097BC01:
    v_stack_p150 = (uint16_t)(Arg1);
    goto loc_0097B818;
loc_0097BC0E:
    local_r11 = 0;
    goto loc_0097B7C8;
loc_0097BC16:
    a4 = 0;
    goto loc_0097B97C;
loc_0097BC1E:
    goto loc_0097B890;
loc_0097BC28:
    local_rsi = 0;
    goto loc_0097B508;
loc_0097BC2F:
    goto loc_0097B87E;
loc_0097BC39:
    goto loc_0097B87E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097B450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
