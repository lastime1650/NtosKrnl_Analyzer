# SPCallServerHandleGetAppPolicyValue

- RVA: `0x00A6CCD0`–`0x00A6D4A5` (길이 `2,005` bytes)
- VA: `0x0000000140A6CCD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B45F0`
- 디코드: `546`개 명령, `2,005/2,005` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A6CE4D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A6CE67` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A6CEB6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A6CFED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A6D007` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A6D0DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A6D249` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A6D347` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A6D49B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A1E9`

### Static image references
- `0x00A6D016` → RVA `0x00FD8398` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A6CE4D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A6CE67` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A6CEB6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A6CFED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A6D007` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A6D0DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A6D249` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A6D347` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A6D49B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00A6D2CC` → [sub_00B3F3B4](../B3/Unknown_function_00B3F3B4.md) (`tail-transfer`)
  - `0x00A6D2E5` → [sub_00B3F3B4 + 0x56](../B3/Unknown_function_00B3F3B4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A6CCD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A6CCD5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00A6CCDA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A6CCDF  55                              push rbp
00A6CCE0  56                              push rsi
00A6CCE1  57                              push rdi
00A6CCE2  41 54                           push r12
00A6CCE4  41 55                           push r13
00A6CCE6  41 56                           push r14
00A6CCE8  41 57                           push r15
00A6CCEA  48 8B EC                        mov rbp, rsp
00A6CCED  48 81 EC 80 00 00 00            sub rsp, 0x80
00A6CCF4  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00A6CCF8  33 DB                           xor ebx, ebx
00A6CCFA  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
00A6CCFE  4D 8B F1                        mov r14, r9
00A6CD01  89 5D E0                        mov dword ptr [rbp - 0x20], ebx
00A6CD04  4C 8B F9                        mov r15, rcx
00A6CD07  89 5D E4                        mov dword ptr [rbp - 0x1c], ebx
00A6CD0A  44 8B EB                        mov r13d, ebx
00A6CD0D  89 5D E8                        mov dword ptr [rbp - 0x18], ebx
00A6CD10  4D 85 C0                        test r8, r8
00A6CD13  0F 84 F2 06 00 00               je 0x140a6d40b
00A6CD19  83 39 03                        cmp dword ptr [rcx], 3
00A6CD1C  0F 86 E9 06 00 00               jbe 0x140a6d40b
00A6CD22  49 8B C0                        mov rax, r8
00A6CD25  8B D3                           mov edx, ebx
00A6CD27  44 8B 08                        mov r9d, dword ptr [rax]
00A6CD2A  48 8D 48 04                     lea rcx, [rax + 4]
00A6CD2E  83 FA 03                        cmp edx, 3
00A6CD31  73 35                           jae 0x140a6cd68
00A6CD33  48 3B C8                        cmp rcx, rax
00A6CD36  73 23                           jae 0x140a6cd5b
00A6CD38  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A6CD3D  8B C3                           mov eax, ebx
00A6CD3F  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00A6CD47  48 81 C4 80 00 00 00            add rsp, 0x80
00A6CD4E  41 5F                           pop r15
00A6CD50  41 5E                           pop r14
00A6CD52  41 5D                           pop r13
00A6CD54  41 5C                           pop r12
00A6CD56  5F                              pop rdi
00A6CD57  5E                              pop rsi
00A6CD58  5D                              pop rbp
00A6CD59  C3                              ret
00A6CD5A  CC                              int3
00A6CD5B  4A 8D 04 09                     lea rax, [rcx + r9]
00A6CD5F  48 3B C1                        cmp rax, rcx
00A6CD62  72 D4                           jb 0x140a6cd38
00A6CD64  FF C2                           inc edx
00A6CD66  EB BF                           jmp 0x140a6cd27
00A6CD68  48 3B C8                        cmp rcx, rax
00A6CD6B  72 CB                           jb 0x140a6cd38
00A6CD6D  45 85 C9                        test r9d, r9d
00A6CD70  4C 8B E3                        mov r12, rbx
00A6CD73  4C 0F 45 E1                     cmovne r12, rcx
00A6CD77  41 83 F9 08                     cmp r9d, 8
00A6CD7B  0F 85 CE 06 00 00               jne 0x140a6d44f
00A6CD81  41 83 3F 04                     cmp dword ptr [r15], 4
00A6CD85  4D 8B 24 24                     mov r12, qword ptr [r12]
00A6CD89  0F 86 7C 06 00 00               jbe 0x140a6d40b
00A6CD8F  8B CB                           mov ecx, ebx
00A6CD91  45 8B 08                        mov r9d, dword ptr [r8]
00A6CD94  49 8D 50 04                     lea rdx, [r8 + 4]
00A6CD98  83 F9 04                        cmp ecx, 4
00A6CD9B  73 12                           jae 0x140a6cdaf
00A6CD9D  49 3B D0                        cmp rdx, r8
00A6CDA0  72 96                           jb 0x140a6cd38
00A6CDA2  4E 8D 04 0A                     lea r8, [rdx + r9]
00A6CDA6  4C 3B C2                        cmp r8, rdx
00A6CDA9  72 8D                           jb 0x140a6cd38
00A6CDAB  FF C1                           inc ecx
00A6CDAD  EB E2                           jmp 0x140a6cd91
00A6CDAF  49 3B D0                        cmp rdx, r8
00A6CDB2  72 84                           jb 0x140a6cd38
00A6CDB4  45 85 C9                        test r9d, r9d
00A6CDB7  48 8B CB                        mov rcx, rbx
00A6CDBA  48 0F 45 CA                     cmovne rcx, rdx
00A6CDBE  0F 84 6F 06 00 00               je 0x140a6d433
00A6CDC4  41 F6 C1 01                     test r9b, 1
00A6CDC8  0F 85 65 06 00 00               jne 0x140a6d433
00A6CDCE  49 8B C1                        mov rax, r9
00A6CDD1  48 D1 E8                        shr rax, 1
00A6CDD4  66 3B 5C 41 FE                  cmp bx, word ptr [rcx + rax*2 - 2]
00A6CDD9  0F 85 54 06 00 00               jne 0x140a6d433
00A6CDDF  48 85 C9                        test rcx, rcx
00A6CDE2  0F 84 4B 06 00 00               je 0x140a6d433
00A6CDE8  48 8B D0                        mov rdx, rax
00A6CDEB  48 8B F1                        mov rsi, rcx
00A6CDEE  48 85 C0                        test rax, rax
00A6CDF1  0F 84 6C 06 00 00               je 0x140a6d463
00A6CDF7  66 39 19                        cmp word ptr [rcx], bx
00A6CDFA  74 0A                           je 0x140a6ce06
00A6CDFC  48 83 C1 02                     add rcx, 2
00A6CE00  48 83 E8 01                     sub rax, 1
00A6CE04  75 F1                           jne 0x140a6cdf7
00A6CE06  48 85 C0                        test rax, rax
00A6CE09  0F 84 54 06 00 00               je 0x140a6d463
00A6CE0F  48 2B D0                        sub rdx, rax
00A6CE12  48 85 C0                        test rax, rax
00A6CE15  0F 84 18 06 00 00               je 0x140a6d433
00A6CE1B  48 8D 0C 12                     lea rcx, [rdx + rdx]
00A6CE1F  48 8D 41 02                     lea rax, [rcx + 2]
00A6CE23  49 3B C1                        cmp rax, r9
00A6CE26  0F 85 07 06 00 00               jne 0x140a6d433
00A6CE2C  48 D1 E9                        shr rcx, 1
00A6CE2F  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00A6CE36  85 C9                           test ecx, ecx
00A6CE38  0F 84 F5 05 00 00               je 0x140a6d433
00A6CE3E  8B D9                           mov ebx, ecx
00A6CE40  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A6CE46  8B D1                           mov edx, ecx
00A6CE48  B9 00 01 00 00                  mov ecx, 0x100
00A6CE4D  E8 9E 52 11 00                  call 0x140b820f0
00A6CE52  48 8B F8                        mov rdi, rax
00A6CE55  48 85 C0                        test rax, rax
00A6CE58  0F 84 CD 02 00 00               je 0x140a6d12b
00A6CE5E  44 8B C3                        mov r8d, ebx
00A6CE61  48 8B D6                        mov rdx, rsi
00A6CE64  48 8B C8                        mov rcx, rax
00A6CE67  E8 D4 99 C5 FF                  call 0x1406c6840
00A6CE6C  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
00A6CE70  48 85 D2                        test rdx, rdx
00A6CE73  0F 84 88 05 00 00               je 0x140a6d401
00A6CE79  41 83 3F 05                     cmp dword ptr [r15], 5
00A6CE7D  0F 86 7E 05 00 00               jbe 0x140a6d401
00A6CE83  48 8B C2                        mov rax, rdx
00A6CE86  45 33 C0                        xor r8d, r8d
00A6CE89  8B 30                           mov esi, dword ptr [rax]
00A6CE8B  48 8D 48 04                     lea rcx, [rax + 4]
00A6CE8F  41 83 F8 05                     cmp r8d, 5
00A6CE93  73 39                           jae 0x140a6cece
00A6CE95  48 3B C8                        cmp rcx, rax
00A6CE98  73 26                           jae 0x140a6cec0
00A6CE9A  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A6CE9F  48 85 FF                        test rdi, rdi
00A6CEA2  0F 85 EE 05 00 00               jne 0x140a6d496
00A6CEA8  4D 85 ED                        test r13, r13
00A6CEAB  0F 84 8C FE FF FF               je 0x140a6cd3d
00A6CEB1  33 D2                           xor edx, edx
00A6CEB3  49 8B CD                        mov rcx, r13
00A6CEB6  E8 B5 59 11 00                  call 0x140b82870
00A6CEBB  E9 7D FE FF FF                  jmp 0x140a6cd3d
00A6CEC0  48 8D 04 31                     lea rax, [rcx + rsi]
00A6CEC4  48 3B C1                        cmp rax, rcx
00A6CEC7  72 D1                           jb 0x140a6ce9a
00A6CEC9  41 FF C0                        inc r8d
00A6CECC  EB BB                           jmp 0x140a6ce89
00A6CECE  48 3B C8                        cmp rcx, rax
00A6CED1  72 C7                           jb 0x140a6ce9a
00A6CED3  33 DB                           xor ebx, ebx
00A6CED5  85 F6                           test esi, esi
00A6CED7  48 0F 45 D9                     cmovne rbx, rcx
00A6CEDB  41 83 3F 06                     cmp dword ptr [r15], 6
00A6CEDF  0F 86 1C 05 00 00               jbe 0x140a6d401
00A6CEE5  48 8B C2                        mov rax, rdx
00A6CEE8  45 33 C0                        xor r8d, r8d
00A6CEEB  44 8B 10                        mov r10d, dword ptr [rax]
00A6CEEE  48 8D 48 04                     lea rcx, [rax + 4]
00A6CEF2  41 83 F8 06                     cmp r8d, 6
00A6CEF6  73 13                           jae 0x140a6cf0b
00A6CEF8  48 3B C8                        cmp rcx, rax
00A6CEFB  72 9D                           jb 0x140a6ce9a
00A6CEFD  4A 8D 04 11                     lea rax, [rcx + r10]
00A6CF01  48 3B C1                        cmp rax, rcx
00A6CF04  72 94                           jb 0x140a6ce9a
00A6CF06  41 FF C0                        inc r8d
00A6CF09  EB E0                           jmp 0x140a6ceeb
00A6CF0B  48 3B C8                        cmp rcx, rax
00A6CF0E  72 8A                           jb 0x140a6ce9a
00A6CF10  33 C0                           xor eax, eax
00A6CF12  45 85 D2                        test r10d, r10d
00A6CF15  48 0F 45 C1                     cmovne rax, rcx
00A6CF19  41 83 FA 04                     cmp r10d, 4
00A6CF1D  0F 85 36 05 00 00               jne 0x140a6d459
00A6CF23  41 83 3F 07                     cmp dword ptr [r15], 7
00A6CF27  44 8B 18                        mov r11d, dword ptr [rax]
00A6CF2A  44 89 5D 50                     mov dword ptr [rbp + 0x50], r11d
00A6CF2E  0F 86 CD 04 00 00               jbe 0x140a6d401
00A6CF34  48 8B C2                        mov rax, rdx
00A6CF37  45 33 C9                        xor r9d, r9d
00A6CF3A  44 8B 00                        mov r8d, dword ptr [rax]
00A6CF3D  48 8D 48 04                     lea rcx, [rax + 4]
00A6CF41  44 89 45 EC                     mov dword ptr [rbp - 0x14], r8d
00A6CF45  41 83 F9 07                     cmp r9d, 7
00A6CF49  73 1F                           jae 0x140a6cf6a
00A6CF4B  48 3B C8                        cmp rcx, rax
00A6CF4E  0F 82 46 FF FF FF               jb 0x140a6ce9a
00A6CF54  4A 8D 04 01                     lea rax, [rcx + r8]
00A6CF58  44 89 5D 50                     mov dword ptr [rbp + 0x50], r11d
00A6CF5C  48 3B C1                        cmp rax, rcx
00A6CF5F  0F 82 35 FF FF FF               jb 0x140a6ce9a
00A6CF65  41 FF C1                        inc r9d
00A6CF68  EB D0                           jmp 0x140a6cf3a
00A6CF6A  48 3B C8                        cmp rcx, rax
00A6CF6D  0F 82 27 FF FF FF               jb 0x140a6ce9a
00A6CF73  45 85 C0                        test r8d, r8d
00A6CF76  4C 0F 45 E9                     cmovne r13, rcx
00A6CF7A  41 83 3F 08                     cmp dword ptr [r15], 8
00A6CF7E  0F 86 9B 04 00 00               jbe 0x140a6d41f
00A6CF84  45 33 D2                        xor r10d, r10d
00A6CF87  8B 02                           mov eax, dword ptr [rdx]
00A6CF89  48 8D 4A 04                     lea rcx, [rdx + 4]
00A6CF8D  41 83 FA 08                     cmp r10d, 8
00A6CF91  73 29                           jae 0x140a6cfbc
00A6CF93  48 3B CA                        cmp rcx, rdx
00A6CF96  73 0E                           jae 0x140a6cfa6
00A6CF98  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A6CF9D  4C 8B 6D F0                     mov r13, qword ptr [rbp - 0x10]
00A6CFA1  E9 F9 FE FF FF                  jmp 0x140a6ce9f
00A6CFA6  48 8D 14 01                     lea rdx, [rcx + rax]
00A6CFAA  44 89 5D 50                     mov dword ptr [rbp + 0x50], r11d
00A6CFAE  44 89 45 EC                     mov dword ptr [rbp - 0x14], r8d
00A6CFB2  48 3B D1                        cmp rdx, rcx
00A6CFB5  72 E1                           jb 0x140a6cf98
00A6CFB7  41 FF C2                        inc r10d
00A6CFBA  EB CB                           jmp 0x140a6cf87
00A6CFBC  48 3B CA                        cmp rcx, rdx
00A6CFBF  72 D7                           jb 0x140a6cf98
00A6CFC1  45 33 FF                        xor r15d, r15d
00A6CFC4  85 C0                           test eax, eax
00A6CFC6  4C 0F 45 F9                     cmovne r15, rcx
00A6CFCA  83 F8 04                        cmp eax, 4
00A6CFCD  0F 85 42 04 00 00               jne 0x140a6d415
00A6CFD3  45 8B 3F                        mov r15d, dword ptr [r15]
00A6CFD6  45 85 FF                        test r15d, r15d
00A6CFD9  0F 84 99 04 00 00               je 0x140a6d478
00A6CFDF  41 8B D7                        mov edx, r15d
00A6CFE2  B9 00 01 00 00                  mov ecx, 0x100
00A6CFE7  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A6CFED  E8 FE 50 11 00                  call 0x140b820f0
00A6CFF2  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00A6CFF6  48 85 C0                        test rax, rax
00A6CFF9  0F 84 6C 04 00 00               je 0x140a6d46b
00A6CFFF  45 8B C7                        mov r8d, r15d
00A6D002  33 D2                           xor edx, edx
00A6D004  48 8B C8                        mov rcx, rax
00A6D007  E8 34 9C C5 FF                  call 0x1406c6c40
00A6D00C  44 8B 45 EC                     mov r8d, dword ptr [rbp - 0x14]
00A6D010  33 D2                           xor edx, edx
00A6D012  44 8B 5D 50                     mov r11d, dword ptr [rbp + 0x50]
00A6D016  48 8B 05 7B B3 56 00            mov rax, qword ptr [rip + 0x56b37b]
00A6D01D  48 85 C0                        test rax, rax
00A6D020  0F 85 DD 02 00 00               jne 0x140a6d303
00A6D026  41 BD BB 00 00 C0               mov r13d, 0xc00000bb
00A6D02C  41 8D 4F 04                     lea ecx, [r15 + 4]
00A6D030  41 BB 04 00 00 00               mov r11d, 4
00A6D036  41 3B CB                        cmp ecx, r11d
00A6D039  0F 82 59 FF FF FF               jb 0x140a6cf98
00A6D03F  83 C1 14                        add ecx, 0x14
00A6D042  83 F9 14                        cmp ecx, 0x14
00A6D045  0F 82 4D FF FF FF               jb 0x140a6cf98
00A6D04B  8D 41 08                        lea eax, [rcx + 8]
00A6D04E  3B C1                           cmp eax, ecx
00A6D050  0F 82 42 FF FF FF               jb 0x140a6cf98
00A6D056  8D 50 08                        lea edx, [rax + 8]
00A6D059  3B D0                           cmp edx, eax
00A6D05B  0F 82 37 FF FF FF               jb 0x140a6cf98
00A6D061  8D 4A 08                        lea ecx, [rdx + 8]
00A6D064  3B CA                           cmp ecx, edx
00A6D066  0F 82 2C FF FF FF               jb 0x140a6cf98
00A6D06C  8D 41 08                        lea eax, [rcx + 8]
00A6D06F  83 F8 08                        cmp eax, 8
00A6D072  0F 82 20 FF FF FF               jb 0x140a6cf98
00A6D078  48 8D 50 07                     lea rdx, [rax + 7]
00A6D07C  83 E2 F8                        and edx, 0xfffffff8
00A6D07F  3B D0                           cmp edx, eax
00A6D081  0F 82 11 FF FF FF               jb 0x140a6cf98
00A6D087  8D 42 08                        lea eax, [rdx + 8]
00A6D08A  3B C2                           cmp eax, edx
00A6D08C  0F 82 06 FF FF FF               jb 0x140a6cf98
00A6D092  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
00A6D096  41 03 C3                        add eax, r11d
00A6D099  45 8B 48 20                     mov r9d, dword ptr [r8 + 0x20]
00A6D09D  45 8B 40 10                     mov r8d, dword ptr [r8 + 0x10]
00A6D0A1  41 3B C3                        cmp eax, r11d
00A6D0A4  0F 83 AA 02 00 00               jae 0x140a6d354
00A6D0AA  BE 95 00 00 C0                  mov esi, 0xc0000095
00A6D0AF  8B DE                           mov ebx, esi
00A6D0B1  85 DB                           test ebx, ebx
00A6D0B3  0F 88 E4 FE FF FF               js 0x140a6cf9d
00A6D0B9  4D 85 F6                        test r14, r14
00A6D0BC  0F 84 5D 03 00 00               je 0x140a6d41f
00A6D0C2  33 DB                           xor ebx, ebx
00A6D0C4  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D0C8  85 C9                           test ecx, ecx
00A6D0CA  0F 84 B2 03 00 00               je 0x140a6d482
00A6D0D0  8B D1                           mov edx, ecx
00A6D0D2  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A6D0D8  B9 00 01 00 00                  mov ecx, 0x100
00A6D0DD  E8 0E 50 11 00                  call 0x140b820f0
00A6D0E2  44 8D 5B 04                     lea r11d, [rbx + 4]
00A6D0E6  48 85 C0                        test rax, rax
00A6D0E9  0F 84 9D 03 00 00               je 0x140a6d48c
00A6D0EF  49 89 46 08                     mov qword ptr [r14 + 8], rax
00A6D0F3  41 21 1E                        and dword ptr [r14], ebx
00A6D0F6  85 DB                           test ebx, ebx
00A6D0F8  0F 88 9F FE FF FF               js 0x140a6cf9d
00A6D0FE  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A6D102  41 0F BA ED 1C                  bts r13d, 0x1c
00A6D107  48 85 D2                        test rdx, rdx
00A6D10A  0F 84 8D 02 00 00               je 0x140a6d39d
00A6D110  45 8B 0E                        mov r9d, dword ptr [r14]
00A6D113  33 C9                           xor ecx, ecx
00A6D115  41 3B C9                        cmp ecx, r9d
00A6D118  73 1B                           jae 0x140a6d135
00A6D11A  8B 02                           mov eax, dword ptr [rdx]
00A6D11C  83 C0 04                        add eax, 4
00A6D11F  41 3B C3                        cmp eax, r11d
00A6D122  73 6B                           jae 0x140a6d18f
00A6D124  8B DE                           mov ebx, esi
00A6D126  E9 72 FE FF FF                  jmp 0x140a6cf9d
00A6D12B  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A6D130  E9 08 FC FF FF                  jmp 0x140a6cd3d
00A6D135  4C 8D 42 04                     lea r8, [rdx + 4]
00A6D139  4C 3B C2                        cmp r8, rdx
00A6D13C  72 E6                           jb 0x140a6d124
00A6D13E  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A6D142  48 8D 42 08                     lea rax, [rdx + 8]
00A6D146  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A6D14A  48 3B C1                        cmp rax, rcx
00A6D14D  0F 87 C2 02 00 00               ja 0x140a6d415
00A6D153  44 89 1A                        mov dword ptr [rdx], r11d
00A6D156  45 89 28                        mov dword ptr [r8], r13d
00A6D159  41 FF 06                        inc dword ptr [r14]
00A6D15C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A6D160  48 85 D2                        test rdx, rdx
00A6D163  0F 84 70 02 00 00               je 0x140a6d3d9
00A6D169  45 8B 0E                        mov r9d, dword ptr [r14]
00A6D16C  33 C9                           xor ecx, ecx
00A6D16E  41 3B C9                        cmp ecx, r9d
00A6D171  73 31                           jae 0x140a6d1a4
00A6D173  8B 02                           mov eax, dword ptr [rdx]
00A6D175  83 C0 04                        add eax, 4
00A6D178  41 3B C3                        cmp eax, r11d
00A6D17B  72 A7                           jb 0x140a6d124
00A6D17D  44 8B C0                        mov r8d, eax
00A6D180  4C 03 C2                        add r8, rdx
00A6D183  4C 3B C2                        cmp r8, rdx
00A6D186  72 9C                           jb 0x140a6d124
00A6D188  49 8B D0                        mov rdx, r8
00A6D18B  FF C1                           inc ecx
00A6D18D  EB DF                           jmp 0x140a6d16e
00A6D18F  44 8B C0                        mov r8d, eax
00A6D192  4C 03 C2                        add r8, rdx
00A6D195  4C 3B C2                        cmp r8, rdx
00A6D198  72 8A                           jb 0x140a6d124
00A6D19A  49 8B D0                        mov rdx, r8
00A6D19D  FF C1                           inc ecx
00A6D19F  E9 71 FF FF FF                  jmp 0x140a6d115
00A6D1A4  4C 8D 42 04                     lea r8, [rdx + 4]
00A6D1A8  4C 3B C2                        cmp r8, rdx
00A6D1AB  0F 82 73 FF FF FF               jb 0x140a6d124
00A6D1B1  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A6D1B5  48 8D 42 0C                     lea rax, [rdx + 0xc]
00A6D1B9  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A6D1BD  48 3B C1                        cmp rax, rcx
00A6D1C0  0F 87 4F 02 00 00               ja 0x140a6d415
00A6D1C6  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00A6D1CC  4D 89 20                        mov qword ptr [r8], r12
00A6D1CF  41 FF 06                        inc dword ptr [r14]
00A6D1D2  4C 8B 55 F0                     mov r10, qword ptr [rbp - 0x10]
00A6D1D6  4D 85 D2                        test r10, r10
00A6D1D9  0F 85 AB 01 00 00               jne 0x140a6d38a
00A6D1DF  45 85 FF                        test r15d, r15d
00A6D1E2  0F 85 AB 01 00 00               jne 0x140a6d393
00A6D1E8  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A6D1EC  48 85 D2                        test rdx, rdx
00A6D1EF  0F 84 C1 01 00 00               je 0x140a6d3b6
00A6D1F5  45 8B 0E                        mov r9d, dword ptr [r14]
00A6D1F8  33 C9                           xor ecx, ecx
00A6D1FA  41 3B C9                        cmp ecx, r9d
00A6D1FD  73 18                           jae 0x140a6d217
00A6D1FF  8B 02                           mov eax, dword ptr [rdx]
00A6D201  83 C0 04                        add eax, 4
00A6D204  41 3B C3                        cmp eax, r11d
00A6D207  0F 83 DD 00 00 00               jae 0x140a6d2ea
00A6D20D  8B DE                           mov ebx, esi
00A6D20F  4D 8B EA                        mov r13, r10
00A6D212  E9 88 FC FF FF                  jmp 0x140a6ce9f
00A6D217  4C 8D 4A 04                     lea r9, [rdx + 4]
00A6D21B  4C 3B CA                        cmp r9, rdx
00A6D21E  72 ED                           jb 0x140a6d20d
00A6D220  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A6D224  49 8D 47 04                     lea rax, [r15 + 4]
00A6D228  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A6D22C  48 03 C2                        add rax, rdx
00A6D22F  45 8B C7                        mov r8d, r15d
00A6D232  48 3B C1                        cmp rax, rcx
00A6D235  0F 87 EE 01 00 00               ja 0x140a6d429
00A6D23B  44 89 3A                        mov dword ptr [rdx], r15d
00A6D23E  4D 85 D2                        test r10, r10
00A6D241  74 0B                           je 0x140a6d24e
00A6D243  49 8B D2                        mov rdx, r10
00A6D246  49 8B C9                        mov rcx, r9
00A6D249  E8 F2 95 C5 FF                  call 0x1406c6840
00A6D24E  41 BB 04 00 00 00               mov r11d, 4
00A6D254  41 FF 06                        inc dword ptr [r14]
00A6D257  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A6D25B  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
00A6D25F  48 85 D2                        test rdx, rdx
00A6D262  0F 84 85 01 00 00               je 0x140a6d3ed
00A6D268  45 8B 16                        mov r10d, dword ptr [r14]
00A6D26B  33 C9                           xor ecx, ecx
00A6D26D  41 3B CA                        cmp ecx, r10d
00A6D270  73 24                           jae 0x140a6d296
00A6D272  8B 02                           mov eax, dword ptr [rdx]
00A6D274  83 C0 04                        add eax, 4
00A6D277  41 3B C3                        cmp eax, r11d
00A6D27A  0F 82 A4 FE FF FF               jb 0x140a6d124
00A6D280  44 8B C8                        mov r9d, eax
00A6D283  4C 03 CA                        add r9, rdx
00A6D286  4C 3B CA                        cmp r9, rdx
00A6D289  0F 82 95 FE FF FF               jb 0x140a6d124
00A6D28F  49 8B D1                        mov rdx, r9
00A6D292  FF C1                           inc ecx
00A6D294  EB D7                           jmp 0x140a6d26d
00A6D296  4C 8D 4A 04                     lea r9, [rdx + 4]
00A6D29A  4C 3B CA                        cmp r9, rdx
00A6D29D  0F 82 81 FE FF FF               jb 0x140a6d124
00A6D2A3  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A6D2A7  48 8D 42 08                     lea rax, [rdx + 8]
00A6D2AB  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A6D2AF  48 3B C1                        cmp rax, rcx
00A6D2B2  0F 87 5D 01 00 00               ja 0x140a6d415
00A6D2B8  44 89 1A                        mov dword ptr [rdx], r11d
00A6D2BB  45 89 01                        mov dword ptr [r9], r8d
00A6D2BE  41 FF 06                        inc dword ptr [r14]
00A6D2C1  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A6D2C5  44 8B 45 E4                     mov r8d, dword ptr [rbp - 0x1c]
00A6D2C9  48 85 D2                        test rdx, rdx
00A6D2CC  0F 85 E2 20 0D 00               jne 0x140b3f3b4
00A6D2D2  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A6D2D6  8D 48 08                        lea ecx, [rax + 8]
00A6D2D9  3B C8                           cmp ecx, eax
00A6D2DB  0F 82 CB 00 00 00               jb 0x140a6d3ac
00A6D2E1  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D2E5  E9 20 21 0D 00                  jmp 0x140b3f40a
00A6D2EA  44 8B C0                        mov r8d, eax
00A6D2ED  4C 03 C2                        add r8, rdx
00A6D2F0  4C 3B C2                        cmp r8, rdx
00A6D2F3  0F 82 14 FF FF FF               jb 0x140a6d20d
00A6D2F9  49 8B D0                        mov rdx, r8
00A6D2FC  FF C1                           inc ecx
00A6D2FE  E9 F7 FE FF FF                  jmp 0x140a6d1fa
00A6D303  33 C9                           xor ecx, ecx
00A6D305  45 8B CB                        mov r9d, r11d
00A6D308  85 D2                           test edx, edx
00A6D30A  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00A6D30E  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00A6D313  48 8D 55 E4                     lea rdx, [rbp - 0x1c]
00A6D317  48 0F 44 4D F0                  cmove rcx, qword ptr [rbp - 0x10]
00A6D31C  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00A6D321  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00A6D325  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00A6D32A  48 8B D3                        mov rdx, rbx
00A6D32D  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00A6D332  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A6D337  48 8B CF                        mov rcx, rdi
00A6D33A  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
00A6D33F  44 8B C6                        mov r8d, esi
00A6D342  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A6D347  E8 84 D7 C4 FF                  call 0x1406baad0
00A6D34C  44 8B E8                        mov r13d, eax
00A6D34F  E9 D8 FC FF FF                  jmp 0x140a6d02c
00A6D354  8D 50 04                        lea edx, [rax + 4]
00A6D357  3B D0                           cmp edx, eax
00A6D359  0F 82 4B FD FF FF               jb 0x140a6d0aa
00A6D35F  41 8D 04 10                     lea eax, [r8 + rdx]
00A6D363  3B C2                           cmp eax, edx
00A6D365  0F 82 3F FD FF FF               jb 0x140a6d0aa
00A6D36B  8D 50 04                        lea edx, [rax + 4]
00A6D36E  BE 95 00 00 C0                  mov esi, 0xc0000095
00A6D373  3B D0                           cmp edx, eax
00A6D375  0F 82 34 FD FF FF               jb 0x140a6d0af
00A6D37B  41 8D 04 11                     lea eax, [r9 + rdx]
00A6D37F  3B C2                           cmp eax, edx
00A6D381  1B DB                           sbb ebx, ebx
00A6D383  23 DE                           and ebx, esi
00A6D385  E9 27 FD FF FF                  jmp 0x140a6d0b1
00A6D38A  45 85 FF                        test r15d, r15d
00A6D38D  0F 85 55 FE FF FF               jne 0x140a6d1e8
00A6D393  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A6D398  E9 72 FE FF FF                  jmp 0x140a6d20f
00A6D39D  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A6D3A1  8D 48 08                        lea ecx, [rax + 8]
00A6D3A4  3B C8                           cmp ecx, eax
00A6D3A6  0F 83 91 00 00 00               jae 0x140a6d43d
00A6D3AC  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00A6D3B1  E9 6E FD FF FF                  jmp 0x140a6d124
00A6D3B6  41 83 C7 04                     add r15d, 4
00A6D3BA  45 3B FB                        cmp r15d, r11d
00A6D3BD  0F 82 4A FE FF FF               jb 0x140a6d20d
00A6D3C3  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A6D3C7  42 8D 0C 38                     lea ecx, [rax + r15]
00A6D3CB  3B C8                           cmp ecx, eax
00A6D3CD  73 77                           jae 0x140a6d446
00A6D3CF  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00A6D3D4  E9 34 FE FF FF                  jmp 0x140a6d20d
00A6D3D9  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A6D3DD  8D 48 0C                        lea ecx, [rax + 0xc]
00A6D3E0  3B C8                           cmp ecx, eax
00A6D3E2  72 C8                           jb 0x140a6d3ac
00A6D3E4  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D3E8  E9 E2 FD FF FF                  jmp 0x140a6d1cf
00A6D3ED  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A6D3F1  8D 48 08                        lea ecx, [rax + 8]
00A6D3F4  3B C8                           cmp ecx, eax
00A6D3F6  72 B4                           jb 0x140a6d3ac
00A6D3F8  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D3FC  E9 BD FE FF FF                  jmp 0x140a6d2be
00A6D401  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A6D406  E9 94 FA FF FF                  jmp 0x140a6ce9f
00A6D40B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A6D410  E9 28 F9 FF FF                  jmp 0x140a6cd3d
00A6D415  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A6D41A  E9 7E FB FF FF                  jmp 0x140a6cf9d
00A6D41F  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A6D424  E9 74 FB FF FF                  jmp 0x140a6cf9d
00A6D429  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A6D42E  E9 DC FD FF FF                  jmp 0x140a6d20f
00A6D433  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A6D438  E9 00 F9 FF FF                  jmp 0x140a6cd3d
00A6D43D  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D441  E9 13 FD FF FF                  jmp 0x140a6d159
00A6D446  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A6D44A  E9 05 FE FF FF                  jmp 0x140a6d254
00A6D44F  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A6D454  E9 E4 F8 FF FF                  jmp 0x140a6cd3d
00A6D459  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A6D45E  E9 3C FA FF FF                  jmp 0x140a6ce9f
00A6D463  48 8B D3                        mov rdx, rbx
00A6D466  E9 A7 F9 FF FF                  jmp 0x140a6ce12
00A6D46B  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A6D470  4C 8B E8                        mov r13, rax
00A6D473  E9 27 FA FF FF                  jmp 0x140a6ce9f
00A6D478  BA 01 00 00 00                  mov edx, 1
00A6D47D  E9 94 FB FF FF                  jmp 0x140a6d016
00A6D482  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A6D487  E9 6A FC FF FF                  jmp 0x140a6d0f6
00A6D48C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A6D491  E9 60 FC FF FF                  jmp 0x140a6d0f6
00A6D496  33 D2                           xor edx, edx
00A6D498  48 8B CF                        mov rcx, rdi
00A6D49B  E8 D0 53 11 00                  call 0x140b82870
00A6D4A0  E9 03 FA FF FF                  jmp 0x140a6cea8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SPCallServerHandleGetAppPolicyValue(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_rbx = 0;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    v_stack_m50 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A6D40B;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A6D40B;
loc_00A6CD27:
    if (0 >= 3) goto loc_00A6CD68;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A6CD5B;
loc_00A6CD38:
loc_00A6CD3D:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
loc_00A6CD5B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A6CD38;
    a2 = (unsigned int)((0) + 1);
    goto loc_00A6CD27;
loc_00A6CD68:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A6CD38;
    v_r12 = v_stack_p8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r12 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A6D44F;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00A6D40B;
loc_00A6CD91:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) >= 4) goto loc_00A6CDAF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A6CD38;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A6CD38;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) + 1);
    goto loc_00A6CD91;
loc_00A6CDAF:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A6CD38;
    a1 = v_stack_p8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a1 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) == 0) goto loc_00A6D433;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00A6D433;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (((unsigned __int16)(v_stack_p8)) != (*(unsigned __int16 *)(a1 + result * 2 - 2))) goto loc_00A6D433;
    if (a1 == 0) goto loc_00A6D433;
    if (result == 0) goto loc_00A6D463;
loc_00A6CDF7:
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(v_stack_p8))) goto loc_00A6CE06;
    a1 = (a1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A6CDF7;
loc_00A6CE06:
    if (result == 0) goto loc_00A6D463;
    a2 = (result) - (result);
loc_00A6CE12:
    if (result == 0) goto loc_00A6D433;
    if ((a2 + a2 * 1 + 2) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00A6D433;
    a1 = (a2 + a2 * 1) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00A6D433;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (result == 0) goto loc_00A6D12B;
    result = memcpy(result, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 * 2 + 2)))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A6D401;
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00A6D401;
    a3 = 0;
loc_00A6CE89:
    if (0 >= 5) goto loc_00A6CECE;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A6CEC0;
loc_00A6CE9A:
loc_00A6CE9F:
    if (result != 0) goto loc_00A6D496;
loc_00A6CEA8:
    if (0 == 0) goto loc_00A6CD3D;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    goto loc_00A6CD3D;
loc_00A6CEC0:
    if ((0 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < 0) goto loc_00A6CE9A;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00A6CE89;
loc_00A6CECE:
    if (0 < (0 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A6CE9A;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbx = 0; }
    if ((*(unsigned int *)(a1)) <= 6) goto loc_00A6D401;
    a3 = 0;
loc_00A6CEEB:
    if (0 >= 6) goto loc_00A6CF0B;
    if ((0 + 4) < 0) goto loc_00A6CE9A;
    if ((0 + 4 + (unsigned int)(*(unsigned int *)(0)) * 1) < (0 + 4)) goto loc_00A6CE9A;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00A6CEEB;
loc_00A6CF0B:
    if ((0 + 4) < (0 + 4 + (unsigned int)(*(unsigned int *)(0)) * 1)) goto loc_00A6CE9A;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0))) != 0) { result = 0 + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0)))) != 4) goto loc_00A6D459;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned int *)(a1)) <= 7) goto loc_00A6D401;
    a4 = 0;
loc_00A6CF3A:
    v_stack_m4C = (unsigned int)((unsigned int)(*(unsigned int *)(0)));
    if (0 >= 7) goto loc_00A6CF6A;
    if ((0 + 4) < 0) goto loc_00A6CE9A;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((0 + 4 + (unsigned int)(*(unsigned int *)(0)) * 1) < (0 + 4)) goto loc_00A6CE9A;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A6CF3A;
loc_00A6CF6A:
    if ((0 + 4) < (0 + 4 + (unsigned int)(*(unsigned int *)(0)) * 1)) goto loc_00A6CE9A;
    v_r13 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0))) != 0) { v_r13 = 0 + 4; }
    if ((*(unsigned int *)(a1)) <= 8) goto loc_00A6D41F;
    v_r10 = 0;
loc_00A6CF87:
    if (0 >= 8) goto loc_00A6CFBC;
    if ((a2 + 4) >= 0) goto loc_00A6CFA6;
loc_00A6CF98:
loc_00A6CF9D:
    goto loc_00A6CE9F;
loc_00A6CFA6:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m4C = (unsigned int)((unsigned int)(*(unsigned int *)(0)));
    if ((a2 + 4 + (unsigned int)(*(unsigned int *)(a2)) * 1) < (a2 + 4)) goto loc_00A6CF98;
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_00A6CF87;
loc_00A6CFBC:
    if ((a2 + 4) < (a2 + 4 + (unsigned int)(*(unsigned int *)(a2)) * 1)) goto loc_00A6CF98;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) != 0) { v_r15 = a2 + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) != 4) goto loc_00A6D415;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))) == 0) goto loc_00A6D478;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))), (unsigned int)(0x20534C53ULL), a4);
    v_stack_m48 = result;
    if (result == 0) goto loc_00A6D46B;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))), a4);
    a2 = 0;
loc_00A6D016:
    if (*(unsigned __int64 *)(v_rip + 5682043) != 0) goto loc_00A6D303;
loc_00A6D02C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)) + 4)) < 4) goto loc_00A6CF98;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15)) + 4) + (20));
    if (((unsigned int)(a1)) < 20) goto loc_00A6CF98;
    if (((unsigned int)(a1 + 8)) < ((unsigned int)(a1))) goto loc_00A6CF98;
    if (((unsigned int)(a1 + 8 + 8)) < ((unsigned int)(a1 + 8))) goto loc_00A6CF98;
    if (((unsigned int)(a1 + 8 + 8 + 8)) < ((unsigned int)(a1 + 8 + 8))) goto loc_00A6CF98;
    if (((unsigned int)(a1 + 8 + 8 + 8 + 8)) < 8) goto loc_00A6CF98;
    a2 = (unsigned int)((a1 + 8 + 8 + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(a1 + 8 + 8 + 8 + 8))) goto loc_00A6CF98;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_00A6CF98;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) >= 4) goto loc_00A6D354;
loc_00A6D0AA:
loc_00A6D0AF:
loc_00A6D0B1:
    if (sign_flag) goto loc_00A6CF9D;
    if (a4 == 0) goto loc_00A6D41F;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)(a1 + 8 + 8 + 8);
    if ((unsigned int)(a1 + 8 + 8 + 8) == 0) goto loc_00A6D482;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 + 8 + 8 + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    if (result == 0) goto loc_00A6D48C;
    *(unsigned __int64 *)(a4 + 8) = result;
loc_00A6D0F6:
    if (sign_flag) goto loc_00A6CF9D;
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A6D39D;
    a1 = 0;
loc_00A6D115:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A6D135;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) >= ((unsigned int)(v_rbx + 4))) goto loc_00A6D18F;
loc_00A6D124:
    goto loc_00A6CF9D;
loc_00A6D12B:
    goto loc_00A6CD3D;
loc_00A6D135:
    if ((*(unsigned __int64 *)(a4 + 8) + 4) < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A6D124;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((*(unsigned __int64 *)(a4 + 8) + 8) > a1) goto loc_00A6D415;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)(v_rbx + 4);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_00A6D159:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A6D3D9;
    a1 = 0;
loc_00A6D16E:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A6D1A4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(v_rbx + 4))) goto loc_00A6D124;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A6D124;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A6D16E;
loc_00A6D18F:
    a3 = ((unsigned int)((unsigned int)(result))) + (a3);
    if (a3 < a3) goto loc_00A6D124;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A6D115;
loc_00A6D1A4:
    if ((a3 + 4) < a3) goto loc_00A6D124;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00A6D415;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_r12);
loc_00A6D1CF:
    if (v_stack_m48 != 0) goto loc_00A6D38A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))) != 0) goto loc_00A6D393;
loc_00A6D1E8:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A6D3B6;
    a1 = 0;
loc_00A6D1FA:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A6D217;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) >= ((unsigned int)(v_rbx + 4))) goto loc_00A6D2EA;
loc_00A6D20D:
loc_00A6D20F:
    goto loc_00A6CE9F;
loc_00A6D217:
    if ((*(unsigned __int64 *)(a4 + 8) + 4) < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A6D20D;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = ((unsigned int)(*(unsigned int *)(v_r15)) + 4) + (*(unsigned __int64 *)(a4 + 8));
    if (result > a1) goto loc_00A6D429;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15)));
    if (v_stack_m48 != 0) {
        a2 = v_stack_m48;
        a1 = *(unsigned __int64 *)(a4 + 8) + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))), *(unsigned __int64 *)(a4 + 8) + 4);
    }
loc_00A6D254:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A6D3ED;
    a1 = 0;
loc_00A6D26D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A6D296;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A6D124;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A6D124;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A6D26D;
loc_00A6D296:
    if ((a4 + 4) < a4) goto loc_00A6D124;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 8) > a1) goto loc_00A6D415;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_m58));
loc_00A6D2BE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A6D3AC;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
loc_00A6D2EA:
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A6D20D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4)) + 8) + 1);
    goto loc_00A6D1FA;
loc_00A6D303:
    a1 = 0;
    v_stack_p50 = v_stack_m50;
    if (a3 == 0) { a1 = v_stack_m48; }
    v_stack_p48 = v_stack_m54;
    v_stack_p40 = v_stack_m58;
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15)));
    v_stack_p30 = a1;
    v_stack_p28 = a3;
    v_stack_p20 = v_stack_m48;
    result = guard_dispatch_icall(result, (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))), (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))), 4);
    goto loc_00A6D02C;
loc_00A6D354:
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00A6D0AA;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + result + 4 * 1)) < ((unsigned int)(result + 4))) goto loc_00A6D0AA;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + result + 4 * 1 + 4)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))) + result + 4 * 1))) goto loc_00A6D0AF;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    goto loc_00A6D0B1;
loc_00A6D38A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))) != 0) goto loc_00A6D1E8;
loc_00A6D393:
    goto loc_00A6D20F;
loc_00A6D39D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A6D43D;
loc_00A6D3AC:
    goto loc_00A6D124;
loc_00A6D3B6:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15))) + (4));
    if (((unsigned int)(v_r15)) < 4) goto loc_00A6D20D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_r15 * 1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A6D446;
    goto loc_00A6D20D;
loc_00A6D3D9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A6D3AC;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_00A6D1CF;
loc_00A6D3ED:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A6D3AC;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A6D2BE;
loc_00A6D401:
    goto loc_00A6CE9F;
loc_00A6D40B:
    goto loc_00A6CD3D;
loc_00A6D415:
    goto loc_00A6CF9D;
loc_00A6D41F:
    goto loc_00A6CF9D;
loc_00A6D429:
    goto loc_00A6D20F;
loc_00A6D433:
    goto loc_00A6CD3D;
loc_00A6D43D:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A6D159;
loc_00A6D446:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A6D254;
loc_00A6D44F:
    goto loc_00A6CD3D;
loc_00A6D459:
    goto loc_00A6CE9F;
loc_00A6D463:
    goto loc_00A6CE12;
loc_00A6D46B:
    goto loc_00A6CE9F;
loc_00A6D478:
    goto loc_00A6D016;
loc_00A6D482:
    goto loc_00A6D0F6;
loc_00A6D48C:
    goto loc_00A6D0F6;
loc_00A6D496:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))), 4);
    goto loc_00A6CEA8;
}
```

## 5. (Beta) C Style

```c
int64_t SPCallServerHandleGetAppPolicyValue(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    local_rbx = 0;
    v_stack_m48 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = 0;
    v_stack_m50 = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A6D40B;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A6D40B;
loc_00A6CD27:
    if (0 >= 3) goto loc_00A6CD68;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A6CD5B;
loc_00A6CD38:
loc_00A6CD3D:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
loc_00A6CD5B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A6CD38;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00A6CD27;
loc_00A6CD68:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A6CD38;
    local_r12 = v_stack_p8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r12 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A6D44F;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00A6D40B;
loc_00A6CD91:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) >= 4) goto loc_00A6CDAF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A6CD38;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A6CD38;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) + 1);
    goto loc_00A6CD91;
loc_00A6CDAF:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A6CD38;
    Arg1 = v_stack_p8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg1 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) == 0) goto loc_00A6D433;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00A6D433;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (((uint16_t)(v_stack_p8)) != (*(uint16_t *)(arg1 + result * 2 - 0x2))) goto loc_00A6D433;
    if (Arg1 == NULL) goto loc_00A6D433;
    if (result == 0) goto loc_00A6D463;
loc_00A6CDF7:
    if ((*(uint16_t *)(arg1)) == ((uint16_t)(v_stack_p8))) goto loc_00A6CE06;
    Arg1 = (Arg1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A6CDF7;
loc_00A6CE06:
    if (result == 0) goto loc_00A6D463;
    Arg2 = (result) - (result);
loc_00A6CE12:
    if (result == 0) goto loc_00A6D433;
    if ((Arg2 + Arg2 * 1 + 2) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00A6D433;
    Arg1 = (Arg2 + Arg2 * 1) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00A6D433;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (result == 0) goto loc_00A6D12B;
    result = memcpy(result, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 * 2 + 2)))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A6D401;
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00A6D401;
    Arg3 = 0;
loc_00A6CE89:
    if (0 >= 5) goto loc_00A6CECE;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A6CEC0;
loc_00A6CE9A:
loc_00A6CE9F:
    if (result != 0) goto loc_00A6D496;
loc_00A6CEA8:
    if (0 == 0) goto loc_00A6CD3D;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    goto loc_00A6CD3D;
loc_00A6CEC0:
    if ((0 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < 0) goto loc_00A6CE9A;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00A6CE89;
loc_00A6CECE:
    if (0 < (0 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A6CE9A;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbx = 0; }
    if ((*(uint32_t *)(arg1)) <= 6) goto loc_00A6D401;
    Arg3 = 0;
loc_00A6CEEB:
    if (0 >= 6) goto loc_00A6CF0B;
    if ((0 + 4) < 0) goto loc_00A6CE9A;
    if ((0 + 4 + (uint32_t)(*(uint32_t *)(0)) * 1) < (0 + 4)) goto loc_00A6CE9A;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00A6CEEB;
loc_00A6CF0B:
    if ((0 + 4) < (0 + 4 + (uint32_t)(*(uint32_t *)(0)) * 1)) goto loc_00A6CE9A;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0))) != 0) { result = 0 + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0)))) != 4) goto loc_00A6D459;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint32_t *)(arg1)) <= 7) goto loc_00A6D401;
    Arg4 = 0;
loc_00A6CF3A:
    v_stack_m4C = (uint32_t)((uint32_t)(*(uint32_t *)(0)));
    if (0 >= 7) goto loc_00A6CF6A;
    if ((0 + 4) < 0) goto loc_00A6CE9A;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((0 + 4 + (uint32_t)(*(uint32_t *)(0)) * 1) < (0 + 4)) goto loc_00A6CE9A;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A6CF3A;
loc_00A6CF6A:
    if ((0 + 4) < (0 + 4 + (uint32_t)(*(uint32_t *)(0)) * 1)) goto loc_00A6CE9A;
    local_r13 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0))) != 0) { local_r13 = 0 + 4; }
    if ((*(uint32_t *)(arg1)) <= 8) goto loc_00A6D41F;
    local_r10 = 0;
loc_00A6CF87:
    if (0 >= 8) goto loc_00A6CFBC;
    if ((Arg2 + 4) >= 0) goto loc_00A6CFA6;
loc_00A6CF98:
loc_00A6CF9D:
    goto loc_00A6CE9F;
loc_00A6CFA6:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m4C = (uint32_t)((uint32_t)(*(uint32_t *)(0)));
    if ((Arg2 + 4 + (uint32_t)(*(uint32_t *)(Arg2)) * 1) < (Arg2 + 4)) goto loc_00A6CF98;
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_00A6CF87;
loc_00A6CFBC:
    if ((Arg2 + 4) < (Arg2 + 4 + (uint32_t)(*(uint32_t *)(Arg2)) * 1)) goto loc_00A6CF98;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) != 0) { local_r15 = Arg2 + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) != 4) goto loc_00A6D415;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))) == 0) goto loc_00A6D478;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))), (uint32_t)(0x20534C53ULL), Arg4);
    v_stack_m48 = result;
    if (result == 0) goto loc_00A6D46B;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))), Arg4);
    Arg2 = 0;
loc_00A6D016:
    if (*(uint64_t *)(v_rip + 0x56B37B) != 0) goto loc_00A6D303;
loc_00A6D02C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)) + 4)) < 4) goto loc_00A6CF98;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15)) + 4) + (20));
    if (((uint32_t)(Arg1)) < 20) goto loc_00A6CF98;
    if (((uint32_t)(Arg1 + 8)) < ((uint32_t)(Arg1))) goto loc_00A6CF98;
    if (((uint32_t)(Arg1 + 8 + 8)) < ((uint32_t)(Arg1 + 8))) goto loc_00A6CF98;
    if (((uint32_t)(Arg1 + 8 + 8 + 8)) < ((uint32_t)(Arg1 + 8 + 8))) goto loc_00A6CF98;
    if (((uint32_t)(Arg1 + 8 + 8 + 8 + 8)) < 8) goto loc_00A6CF98;
    Arg2 = (uint32_t)((Arg1 + 8 + 8 + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(Arg1 + 8 + 8 + 8 + 8))) goto loc_00A6CF98;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_00A6CF98;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) >= 4) goto loc_00A6D354;
loc_00A6D0AA:
loc_00A6D0AF:
loc_00A6D0B1:
    if (sign_flag) goto loc_00A6CF9D;
    if (Arg4 == 0) goto loc_00A6D41F;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg1 + 8 + 8 + 8);
    if ((uint32_t)(Arg1 + 8 + 8 + 8) == 0) goto loc_00A6D482;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 + 8 + 8 + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    if (result == 0) goto loc_00A6D48C;
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_00A6D0F6:
    if (sign_flag) goto loc_00A6CF9D;
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_00A6D39D;
    Arg1 = 0;
loc_00A6D115:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00A6D135;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) >= ((uint32_t)(local_rbx + 4))) goto loc_00A6D18F;
loc_00A6D124:
    goto loc_00A6CF9D;
loc_00A6D12B:
    goto loc_00A6CD3D;
loc_00A6D135:
    if ((*(uint64_t *)(Arg4 + 0x8) + 4) < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00A6D124;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((*(uint64_t *)(Arg4 + 0x8) + 8) > Arg1) goto loc_00A6D415;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)(local_rbx + 4);
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_00A6D159:
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_00A6D3D9;
    Arg1 = 0;
loc_00A6D16E:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00A6D1A4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(local_rbx + 4))) goto loc_00A6D124;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00A6D124;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A6D16E;
loc_00A6D18F:
    Arg3 = ((uint32_t)((uint32_t)(result))) + (Arg3);
    if (Arg3 < Arg3) goto loc_00A6D124;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A6D115;
loc_00A6D1A4:
    if ((Arg3 + 4) < Arg3) goto loc_00A6D124;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00A6D415;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_r12);
loc_00A6D1CF:
    if (v_stack_m48 != 0) goto loc_00A6D38A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))) != 0) goto loc_00A6D393;
loc_00A6D1E8:
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_00A6D3B6;
    Arg1 = 0;
loc_00A6D1FA:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00A6D217;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) >= ((uint32_t)(local_rbx + 4))) goto loc_00A6D2EA;
loc_00A6D20D:
loc_00A6D20F:
    goto loc_00A6CE9F;
loc_00A6D217:
    if ((*(uint64_t *)(Arg4 + 0x8) + 4) < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00A6D20D;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = ((uint32_t)(*(uint32_t *)(local_r15)) + 4) + (*(uint64_t *)(Arg4 + 0x8));
    if (result > Arg1) goto loc_00A6D429;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15)));
    if (v_stack_m48 != 0) {
        Arg2 = v_stack_m48;
        Arg1 = *(uint64_t *)(Arg4 + 0x8) + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))), *(uint64_t *)(Arg4 + 0x8) + 4);
    }
loc_00A6D254:
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_00A6D3ED;
    Arg1 = 0;
loc_00A6D26D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00A6D296;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A6D124;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00A6D124;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A6D26D;
loc_00A6D296:
    if ((Arg4 + 4) < Arg4) goto loc_00A6D124;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg4 + 8) > Arg1) goto loc_00A6D415;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_m58));
loc_00A6D2BE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00A6D3AC;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
loc_00A6D2EA:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00A6D20D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8) + 1);
    goto loc_00A6D1FA;
loc_00A6D303:
    Arg1 = 0;
    v_stack_p50 = v_stack_m50;
    if (Arg3 == 0) { Arg1 = v_stack_m48; }
    v_stack_p48 = v_stack_m54;
    v_stack_p40 = v_stack_m58;
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15)));
    v_stack_p30 = Arg1;
    v_stack_p28 = Arg3;
    v_stack_p20 = v_stack_m48;
    result = guard_dispatch_icall(result, (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))), (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))), 4);
    goto loc_00A6D02C;
loc_00A6D354:
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00A6D0AA;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + result + 4 * 1)) < ((uint32_t)(result + 4))) goto loc_00A6D0AA;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + result + 4 * 1 + 4)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))) + result + 4 * 1))) goto loc_00A6D0AF;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    goto loc_00A6D0B1;
loc_00A6D38A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))) != 0) goto loc_00A6D1E8;
loc_00A6D393:
    goto loc_00A6D20F;
loc_00A6D39D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00A6D43D;
loc_00A6D3AC:
    goto loc_00A6D124;
loc_00A6D3B6:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15))) + (4));
    if (((uint32_t)(local_r15)) < 4) goto loc_00A6D20D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_r15 * 1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00A6D446;
    goto loc_00A6D20D;
loc_00A6D3D9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00A6D3AC;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_00A6D1CF;
loc_00A6D3ED:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00A6D3AC;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00A6D2BE;
loc_00A6D401:
    goto loc_00A6CE9F;
loc_00A6D40B:
    goto loc_00A6CD3D;
loc_00A6D415:
    goto loc_00A6CF9D;
loc_00A6D41F:
    goto loc_00A6CF9D;
loc_00A6D429:
    goto loc_00A6D20F;
loc_00A6D433:
    goto loc_00A6CD3D;
loc_00A6D43D:
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00A6D159;
loc_00A6D446:
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00A6D254;
loc_00A6D44F:
    goto loc_00A6CD3D;
loc_00A6D459:
    goto loc_00A6CE9F;
loc_00A6D463:
    goto loc_00A6CE12;
loc_00A6D46B:
    goto loc_00A6CE9F;
loc_00A6D478:
    goto loc_00A6D016;
loc_00A6D482:
    goto loc_00A6D0F6;
loc_00A6D48C:
    goto loc_00A6D0F6;
loc_00A6D496:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))), 4);
    goto loc_00A6CEA8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6CCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
