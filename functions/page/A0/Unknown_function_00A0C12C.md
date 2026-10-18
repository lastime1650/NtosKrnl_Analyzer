# sub_00A0C12C

- RVA: `0x00A0C12C`–`0x00A0C66F` (길이 `1,347` bytes)
- VA: `0x0000000140A0C12C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8A74`
- 디코드: `360`개 명령, `1,347/1,347` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A0C277` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A0C29E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0C2F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0C353` → [FsRtlQueryKernelEaFile](FsRtlQueryKernelEaFile_function_00A0C680.md) (function, `0x00A0C680`)
- `0x00A0C3B5` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00A0C3DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0C412` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0C454` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0C47E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0C4B5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A0C4C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0C4D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0C4F8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x009698A4`

### Static image references
- `0x00A0C259` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x00A0C2D5` → RVA `0x00B4B428` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A0C29E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C2F9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C3B5` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00A0C3DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C47E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C4B5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A0C4C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C4D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0C4F8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0C12C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A0C131  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00A0C136  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A0C13B  55                              push rbp
00A0C13C  56                              push rsi
00A0C13D  57                              push rdi
00A0C13E  41 54                           push r12
00A0C140  41 55                           push r13
00A0C142  41 56                           push r14
00A0C144  41 57                           push r15
00A0C146  48 8B EC                        mov rbp, rsp
00A0C149  48 81 EC 80 00 00 00            sub rsp, 0x80
00A0C150  45 33 DB                        xor r11d, r11d
00A0C153  49 8B F9                        mov rdi, r9
00A0C156  4C 8B C1                        mov r8, rcx
00A0C159  45 8B F3                        mov r14d, r11d
00A0C15C  48 85 C9                        test rcx, rcx
00A0C15F  0F 84 B3 04 00 00               je 0x140a0c618
00A0C165  4D 85 C9                        test r9, r9
00A0C168  0F 84 AA 04 00 00               je 0x140a0c618
00A0C16E  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A0C172  48 85 C9                        test rcx, rcx
00A0C175  0F 84 9D 04 00 00               je 0x140a0c618
00A0C17B  41 8D 5B 03                     lea ebx, [r11 + 3]
00A0C17F  41 39 18                        cmp dword ptr [r8], ebx
00A0C182  0F 86 90 04 00 00               jbe 0x140a0c618
00A0C188  48 8B C1                        mov rax, rcx
00A0C18B  45 8B CB                        mov r9d, r11d
00A0C18E  44 8B 10                        mov r10d, dword ptr [rax]
00A0C191  48 8D 50 04                     lea rdx, [rax + 4]
00A0C195  44 3B CB                        cmp r9d, ebx
00A0C198  73 36                           jae 0x140a0c1d0
00A0C19A  48 3B D0                        cmp rdx, rax
00A0C19D  73 23                           jae 0x140a0c1c2
00A0C19F  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A0C1A4  8B C3                           mov eax, ebx
00A0C1A6  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A0C1AE  48 81 C4 80 00 00 00            add rsp, 0x80
00A0C1B5  41 5F                           pop r15
00A0C1B7  41 5E                           pop r14
00A0C1B9  41 5D                           pop r13
00A0C1BB  41 5C                           pop r12
00A0C1BD  5F                              pop rdi
00A0C1BE  5E                              pop rsi
00A0C1BF  5D                              pop rbp
00A0C1C0  C3                              ret
00A0C1C1  CC                              int3
00A0C1C2  4A 8D 04 12                     lea rax, [rdx + r10]
00A0C1C6  48 3B C2                        cmp rax, rdx
00A0C1C9  72 D4                           jb 0x140a0c19f
00A0C1CB  41 FF C1                        inc r9d
00A0C1CE  EB BE                           jmp 0x140a0c18e
00A0C1D0  48 3B D0                        cmp rdx, rax
00A0C1D3  72 CA                           jb 0x140a0c19f
00A0C1D5  45 85 D2                        test r10d, r10d
00A0C1D8  49 8B C3                        mov rax, r11
00A0C1DB  48 0F 45 C2                     cmovne rax, rdx
00A0C1DF  41 83 FA 08                     cmp r10d, 8
00A0C1E3  0F 85 4D 04 00 00               jne 0x140a0c636
00A0C1E9  41 83 38 04                     cmp dword ptr [r8], 4
00A0C1ED  4C 8B 28                        mov r13, qword ptr [rax]
00A0C1F0  0F 86 22 04 00 00               jbe 0x140a0c618
00A0C1F6  45 8B C3                        mov r8d, r11d
00A0C1F9  8B 01                           mov eax, dword ptr [rcx]
00A0C1FB  48 8D 51 04                     lea rdx, [rcx + 4]
00A0C1FF  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
00A0C203  41 83 F8 04                     cmp r8d, 4
00A0C207  73 13                           jae 0x140a0c21c
00A0C209  48 3B D1                        cmp rdx, rcx
00A0C20C  72 91                           jb 0x140a0c19f
00A0C20E  48 8D 0C 02                     lea rcx, [rdx + rax]
00A0C212  48 3B CA                        cmp rcx, rdx
00A0C215  72 88                           jb 0x140a0c19f
00A0C217  41 FF C0                        inc r8d
00A0C21A  EB DD                           jmp 0x140a0c1f9
00A0C21C  48 3B D1                        cmp rdx, rcx
00A0C21F  0F 82 7A FF FF FF               jb 0x140a0c19f
00A0C225  85 C0                           test eax, eax
00A0C227  49 8B CB                        mov rcx, r11
00A0C22A  48 0F 45 CA                     cmovne rcx, rdx
00A0C22E  83 F8 08                        cmp eax, 8
00A0C231  0F 85 24 04 00 00               jne 0x140a0c65b
00A0C237  48 8B 09                        mov rcx, qword ptr [rcx]
00A0C23A  4D 8B E3                        mov r12, r11
00A0C23D  44 89 5D 50                     mov dword ptr [rbp + 0x50], r11d
00A0C241  4D 8B FB                        mov r15, r11
00A0C244  4C 89 5D 40                     mov qword ptr [rbp + 0x40], r11
00A0C248  4C 89 5D D0                     mov qword ptr [rbp - 0x30], r11
00A0C24C  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
00A0C250  48 85 C9                        test rcx, rcx
00A0C253  0F 84 BF 03 00 00               je 0x140a0c618
00A0C259  4C 8B 05 80 A8 5B 00            mov r8, qword ptr [rip + 0x5ba880]
00A0C260  48 8D 45 48                     lea rax, [rbp + 0x48]
00A0C264  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
00A0C269  41 B1 01                        mov r9b, 1
00A0C26C  33 D2                           xor edx, edx
00A0C26E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0C273  4C 89 5D 48                     mov qword ptr [rbp + 0x48], r11
00A0C277  E8 34 CB E5 FF                  call 0x140868db0
00A0C27C  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
00A0C280  8B F0                           mov esi, eax
00A0C282  48 89 5D 48                     mov qword ptr [rbp + 0x48], rbx
00A0C286  85 C0                           test eax, eax
00A0C288  0F 88 1B 02 00 00               js 0x140a0c4a9
00A0C28E  BA 1F 00 00 00                  mov edx, 0x1f
00A0C293  B9 00 01 00 00                  mov ecx, 0x100
00A0C298  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0C29E  E8 4D 5E 17 00                  call 0x140b820f0
00A0C2A3  33 F6                           xor esi, esi
00A0C2A5  4C 8B E0                        mov r12, rax
00A0C2A8  48 85 C0                        test rax, rax
00A0C2AB  0F 84 71 03 00 00               je 0x140a0c622
00A0C2B1  48 89 70 05                     mov qword ptr [rax + 5], rsi
00A0C2B5  8D 56 3A                        lea edx, [rsi + 0x3a]
00A0C2B8  48 89 70 0D                     mov qword ptr [rax + 0xd], rsi
00A0C2BC  B9 00 01 00 00                  mov ecx, 0x100
00A0C2C1  48 89 70 15                     mov qword ptr [rax + 0x15], rsi
00A0C2C5  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0C2CB  66 89 70 1D                     mov word ptr [rax + 0x1d], si
00A0C2CF  C6 40 04 19                     mov byte ptr [rax + 4], 0x19
00A0C2D3  89 30                           mov dword ptr [rax], esi
00A0C2D5  48 8B 05 4C F1 13 00            mov rax, qword ptr [rip + 0x13f14c]
00A0C2DC  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A0C2DF  41 0F 11 44 24 05               movups xmmword ptr [r12 + 5], xmm0
00A0C2E5  F2 0F 10 48 10                  movsd xmm1, qword ptr [rax + 0x10]
00A0C2EA  F2 41 0F 11 4C 24 15            movsd qword ptr [r12 + 0x15], xmm1
00A0C2F1  8A 40 18                        mov al, byte ptr [rax + 0x18]
00A0C2F4  41 88 44 24 1D                  mov byte ptr [r12 + 0x1d], al
00A0C2F9  E8 F2 5D 17 00                  call 0x140b820f0
00A0C2FE  4C 8B F8                        mov r15, rax
00A0C301  48 85 C0                        test rax, rax
00A0C304  0F 84 18 03 00 00               je 0x140a0c622
00A0C30A  0F 57 C0                        xorps xmm0, xmm0
00A0C30D  44 8D 46 3A                     lea r8d, [rsi + 0x3a]
00A0C311  41 0F 11 07                     movups xmmword ptr [r15], xmm0
00A0C315  33 C0                           xor eax, eax
00A0C317  41 B1 01                        mov r9b, 1
00A0C31A  41 0F 11 47 10                  movups xmmword ptr [r15 + 0x10], xmm0
00A0C31F  49 8B D7                        mov rdx, r15
00A0C322  48 8B CB                        mov rcx, rbx
00A0C325  41 0F 11 47 20                  movups xmmword ptr [r15 + 0x20], xmm0
00A0C32A  49 89 47 30                     mov qword ptr [r15 + 0x30], rax
00A0C32E  66 41 89 47 38                  mov word ptr [r15 + 0x38], ax
00A0C333  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0C337  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A0C33C  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
00A0C341  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00A0C346  C7 44 24 28 1F 00 00 00         mov dword ptr [rsp + 0x28], 0x1f
00A0C34E  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00A0C353  E8 28 03 00 00                  call 0x140a0c680
00A0C358  8B F0                           mov esi, eax
00A0C35A  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0C35F  0F 84 DB 02 00 00               je 0x140a0c640
00A0C365  85 C0                           test eax, eax
00A0C367  0F 88 3C 01 00 00               js 0x140a0c4a9
00A0C36D  45 0F B6 47 05                  movzx r8d, byte ptr [r15 + 5]
00A0C372  41 0F B7 57 06                  movzx edx, word ptr [r15 + 6]
00A0C377  49 83 C0 09                     add r8, 9
00A0C37B  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00A0C37E  4D 03 C7                        add r8, r15
00A0C381  49 03 C7                        add rax, r15
00A0C384  4C 89 45 E8                     mov qword ptr [rbp - 0x18], r8
00A0C388  49 8D 0C 10                     lea rcx, [r8 + rdx]
00A0C38C  48 3B C8                        cmp rcx, rax
00A0C38F  0F 87 97 02 00 00               ja 0x140a0c62c
00A0C395  33 C0                           xor eax, eax
00A0C397  66 3B C2                        cmp ax, dx
00A0C39A  0F 84 A2 02 00 00               je 0x140a0c642
00A0C3A0  83 FA 18                        cmp edx, 0x18
00A0C3A3  0F 85 83 02 00 00               jne 0x140a0c62c
00A0C3A9  49 8D 48 10                     lea rcx, [r8 + 0x10]
00A0C3AD  44 8D 40 08                     lea r8d, [rax + 8]
00A0C3B1  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00A0C3B5  E8 B6 E2 CA FF                  call 0x1406ba670
00A0C3BA  48 83 F8 08                     cmp rax, 8
00A0C3BE  0F 85 68 02 00 00               jne 0x140a0c62c
00A0C3C4  33 C0                           xor eax, eax
00A0C3C6  BA 48 02 00 00                  mov edx, 0x248
00A0C3CB  B9 00 01 00 00                  mov ecx, 0x100
00A0C3D0  89 45 50                        mov dword ptr [rbp + 0x50], eax
00A0C3D3  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0C3D9  44 8D 70 02                     lea r14d, [rax + 2]
00A0C3DD  E8 0E 5D 17 00                  call 0x140b820f0
00A0C3E2  4C 8B E8                        mov r13, rax
00A0C3E5  48 85 C0                        test rax, rax
00A0C3E8  0F 84 B7 00 00 00               je 0x140a0c4a5
00A0C3EE  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0C3F2  45 33 C9                        xor r9d, r9d
00A0C3F5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0C3FA  45 33 C0                        xor r8d, r8d
00A0C3FD  C7 44 24 28 48 02 00 00         mov dword ptr [rsp + 0x28], 0x248
00A0C405  BA F4 00 09 00                  mov edx, 0x900f4
00A0C40A  48 8B CB                        mov rcx, rbx
00A0C40D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A0C412  E8 59 06 00 00                  call 0x140a0ca70
00A0C417  8B D8                           mov ebx, eax
00A0C419  85 C0                           test eax, eax
00A0C41B  78 5C                           js 0x140a0c479
00A0C41D  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0C421  0F 82 22 02 00 00               jb 0x140a0c649
00A0C427  49 8B 45 00                     mov rax, qword ptr [r13]
00A0C42B  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00A0C42F  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A0C434  45 33 C9                        xor r9d, r9d
00A0C437  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00A0C43B  45 33 C0                        xor r8d, r8d
00A0C43E  C7 44 24 28 48 02 00 00         mov dword ptr [rsp + 0x28], 0x248
00A0C446  BA EB 00 09 00                  mov edx, 0x900eb
00A0C44B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A0C450  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00A0C454  E8 17 06 00 00                  call 0x140a0ca70
00A0C459  8B D8                           mov ebx, eax
00A0C45B  85 C0                           test eax, eax
00A0C45D  78 1A                           js 0x140a0c479
00A0C45F  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0C463  0F 82 E0 01 00 00               jb 0x140a0c649
00A0C469  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00A0C46D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00A0C471  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00A0C475  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00A0C479  33 D2                           xor edx, edx
00A0C47B  49 8B CD                        mov rcx, r13
00A0C47E  E8 ED 63 17 00                  call 0x140b82870
00A0C483  85 DB                           test ebx, ebx
00A0C485  78 1E                           js 0x140a0c4a5
00A0C487  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00A0C48B  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00A0C48F  48 3B 08                        cmp rcx, qword ptr [rax]
00A0C492  75 11                           jne 0x140a0c4a5
00A0C494  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00A0C498  48 3B 48 08                     cmp rcx, qword ptr [rax + 8]
00A0C49C  B8 03 00 00 00                  mov eax, 3
00A0C4A1  44 0F 44 F0                     cmove r14d, eax
00A0C4A5  4C 8B 6D F0                     mov r13, qword ptr [rbp - 0x10]
00A0C4A9  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00A0C4AD  48 85 C0                        test rax, rax
00A0C4B0  74 08                           je 0x140a0c4ba
00A0C4B2  48 8B C8                        mov rcx, rax
00A0C4B5  E8 96 CE 8E FF                  call 0x1402f9350
00A0C4BA  4D 85 E4                        test r12, r12
00A0C4BD  74 0A                           je 0x140a0c4c9
00A0C4BF  33 D2                           xor edx, edx
00A0C4C1  49 8B CC                        mov rcx, r12
00A0C4C4  E8 A7 63 17 00                  call 0x140b82870
00A0C4C9  45 33 E4                        xor r12d, r12d
00A0C4CC  4D 85 FF                        test r15, r15
00A0C4CF  74 0A                           je 0x140a0c4db
00A0C4D1  33 D2                           xor edx, edx
00A0C4D3  49 8B CF                        mov rcx, r15
00A0C4D6  E8 95 63 17 00                  call 0x140b82870
00A0C4DB  8B DE                           mov ebx, esi
00A0C4DD  85 F6                           test esi, esi
00A0C4DF  0F 88 BF FC FF FF               js 0x140a0c1a4
00A0C4E5  BA 14 00 00 00                  mov edx, 0x14
00A0C4EA  B9 00 01 00 00                  mov ecx, 0x100
00A0C4EF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0C4F5  89 57 04                        mov dword ptr [rdi + 4], edx
00A0C4F8  E8 F3 5B 17 00                  call 0x140b820f0
00A0C4FD  48 85 C0                        test rax, rax
00A0C500  0F 84 5F 01 00 00               je 0x140a0c665
00A0C506  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A0C50A  44 89 27                        mov dword ptr [rdi], r12d
00A0C50D  48 8B D0                        mov rdx, rax
00A0C510  48 85 C0                        test rax, rax
00A0C513  0F 84 C0 00 00 00               je 0x140a0c5d9
00A0C519  41 8B CC                        mov ecx, r12d
00A0C51C  41 3B CC                        cmp ecx, r12d
00A0C51F  73 24                           jae 0x140a0c545
00A0C521  8B 02                           mov eax, dword ptr [rdx]
00A0C523  83 C0 04                        add eax, 4
00A0C526  83 F8 04                        cmp eax, 4
00A0C529  0F 82 70 FC FF FF               jb 0x140a0c19f
00A0C52F  44 8B C0                        mov r8d, eax
00A0C532  4C 03 C2                        add r8, rdx
00A0C535  4C 3B C2                        cmp r8, rdx
00A0C538  0F 82 61 FC FF FF               jb 0x140a0c19f
00A0C53E  49 8B D0                        mov rdx, r8
00A0C541  FF C1                           inc ecx
00A0C543  EB D7                           jmp 0x140a0c51c
00A0C545  4C 8D 42 04                     lea r8, [rdx + 4]
00A0C549  4C 3B C2                        cmp r8, rdx
00A0C54C  0F 82 4D FC FF FF               jb 0x140a0c19f
00A0C552  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0C555  48 8D 42 0C                     lea rax, [rdx + 0xc]
00A0C559  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A0C55D  48 3B C1                        cmp rax, rcx
00A0C560  0F 87 D0 00 00 00               ja 0x140a0c636
00A0C566  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00A0C56C  4D 89 28                        mov qword ptr [r8], r13
00A0C56F  FF 07                           inc dword ptr [rdi]
00A0C571  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A0C575  48 85 D2                        test rdx, rdx
00A0C578  74 72                           je 0x140a0c5ec
00A0C57A  44 8B 0F                        mov r9d, dword ptr [rdi]
00A0C57D  41 8B CC                        mov ecx, r12d
00A0C580  41 3B C9                        cmp ecx, r9d
00A0C583  73 24                           jae 0x140a0c5a9
00A0C585  8B 02                           mov eax, dword ptr [rdx]
00A0C587  83 C0 04                        add eax, 4
00A0C58A  83 F8 04                        cmp eax, 4
00A0C58D  0F 82 0C FC FF FF               jb 0x140a0c19f
00A0C593  44 8B C0                        mov r8d, eax
00A0C596  4C 03 C2                        add r8, rdx
00A0C599  4C 3B C2                        cmp r8, rdx
00A0C59C  0F 82 FD FB FF FF               jb 0x140a0c19f
00A0C5A2  49 8B D0                        mov rdx, r8
00A0C5A5  FF C1                           inc ecx
00A0C5A7  EB D7                           jmp 0x140a0c580
00A0C5A9  4C 8D 42 04                     lea r8, [rdx + 4]
00A0C5AD  4C 3B C2                        cmp r8, rdx
00A0C5B0  0F 82 E9 FB FF FF               jb 0x140a0c19f
00A0C5B6  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0C5B9  48 8D 42 08                     lea rax, [rdx + 8]
00A0C5BD  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A0C5C1  41 8B DC                        mov ebx, r12d
00A0C5C4  48 3B C1                        cmp rax, rcx
00A0C5C7  77 6D                           ja 0x140a0c636
00A0C5C9  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00A0C5CF  45 89 30                        mov dword ptr [r8], r14d
00A0C5D2  FF 07                           inc dword ptr [rdi]
00A0C5D4  E9 CB FB FF FF                  jmp 0x140a0c1a4
00A0C5D9  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A0C5DC  8D 48 0C                        lea ecx, [rax + 0xc]
00A0C5DF  3B C8                           cmp ecx, eax
00A0C5E1  73 70                           jae 0x140a0c653
00A0C5E3  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00A0C5E7  E9 B3 FB FF FF                  jmp 0x140a0c19f
00A0C5EC  8B 57 04                        mov edx, dword ptr [rdi + 4]
00A0C5EF  83 C8 FF                        or eax, 0xffffffff
00A0C5F2  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A0C5F7  8D 4A 08                        lea ecx, [rdx + 8]
00A0C5FA  3B CA                           cmp ecx, edx
00A0C5FC  0F 43 C1                        cmovae eax, ecx
00A0C5FF  89 47 04                        mov dword ptr [rdi + 4], eax
00A0C602  1B C0                           sbb eax, eax
00A0C604  23 D8                           and ebx, eax
00A0C606  3B CA                           cmp ecx, edx
00A0C608  0F 82 96 FB FF FF               jb 0x140a0c1a4
00A0C60E  FF 07                           inc dword ptr [rdi]
00A0C610  41 8B DC                        mov ebx, r12d
00A0C613  E9 8C FB FF FF                  jmp 0x140a0c1a4
00A0C618  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A0C61D  E9 82 FB FF FF                  jmp 0x140a0c1a4
00A0C622  BE 17 00 00 C0                  mov esi, 0xc0000017
00A0C627  E9 7D FE FF FF                  jmp 0x140a0c4a9
00A0C62C  BE 3E 00 00 C0                  mov esi, 0xc000003e
00A0C631  E9 73 FE FF FF                  jmp 0x140a0c4a9
00A0C636  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A0C63B  E9 64 FB FF FF                  jmp 0x140a0c1a4
00A0C640  33 C0                           xor eax, eax
00A0C642  8B F0                           mov esi, eax
00A0C644  E9 60 FE FF FF                  jmp 0x140a0c4a9
00A0C649  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A0C64E  E9 26 FE FF FF                  jmp 0x140a0c479
00A0C653  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A0C656  E9 14 FF FF FF                  jmp 0x140a0c56f
00A0C65B  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A0C660  E9 3F FB FF FF                  jmp 0x140a0c1a4
00A0C665  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0C66A  E9 35 FB FF FF                  jmp 0x140a0c1a4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A0C12C(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_r11 = 0;
    if (a1 == 0) goto loc_00A0C618;
    if (a4 == 0) goto loc_00A0C618;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A0C618;
    if ((*(unsigned int *)(a1)) <= ((unsigned int)(v_r11 + 3))) goto loc_00A0C618;
loc_00A0C18E:
    if (0 >= ((unsigned int)(v_r11 + 3))) goto loc_00A0C1D0;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0C1C2;
loc_00A0C19F:
loc_00A0C1A4:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
loc_00A0C1C2:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0C19F;
    a4 = (unsigned int)((0) + 1);
    goto loc_00A0C18E;
loc_00A0C1D0:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0C19F;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A0C636;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00A0C618;
loc_00A0C1F9:
    v_stack_m48 = *(unsigned __int64 *)(result);
    if (0 >= 4) goto loc_00A0C21C;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0C19F;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0C19F;
    a3 = (unsigned int)((0) + 1);
    goto loc_00A0C1F9;
loc_00A0C21C:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0C19F;
    a1 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a1 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A0C65B;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00A0C618;
    v_stack_p28 = 0;
    a2 = 0;
    v_stack_p20 = v_stack_p10;
    v_stack_p10 = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a1), a2, *(unsigned __int64 *)(v_rip + 6006912), 1);
    v_stack_p10 = v_stack_p10;
    if (sign_flag) goto loc_00A0C4A9;
    result = ExAllocatePool2(256, 31, (unsigned int)(0x20534C53ULL), 1);
    v_rsi = 0;
    if (result == 0) goto loc_00A0C622;
    *(unsigned __int64 *)(result + 5) = 0;
    *(unsigned __int64 *)(result + 13) = 0;
    *(unsigned __int64 *)(result + 21) = 0;
    *(unsigned __int16 *)(result + 29) = 0;
    *(unsigned __int8 *)(result + 4) = 25;
    *(unsigned int *)(result) = 0;
    *(unsigned __int64 *)(result + 5) = v_xmm0;
    *(unsigned __int64 *)(result + 21) = v_xmm1;
    *(unsigned __int8 *)(result + 29) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 1306956) + 24));
    result = ExAllocatePool2(256, v_rsi + 58, (unsigned int)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C622;
    *(unsigned __int64 *)(result) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = 0;
    *(unsigned __int16 *)(result + 56) = 0;
    v_stack_p40 = v_stack_p18;
    v_stack_p38 = 1;
    v_stack_p30 = 0;
    v_stack_p28 = 31;
    v_stack_p20 = 0;
    result = FsRtlQueryKernelEaFile(v_stack_p10, 0, v_rsi + 58, 1);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_00A0C640;
    if (sign_flag) goto loc_00A0C4A9;
    a3 = (*(unsigned __int8 *)(result + 5)) + (9);
    a3 = (a3) + (result);
    result = ((unsigned int)(v_stack_p18)) + (result);
    v_stack_m50 = a3;
    if ((a3 + *(unsigned __int16 *)(result + 6) * 1) > result) goto loc_00A0C62C;
    result = 0;
    if (0 == ((unsigned __int16)(*(unsigned __int16 *)(result + 6)))) goto loc_00A0C642;
    if (((unsigned int)(*(unsigned __int16 *)(result + 6))) != 24) goto loc_00A0C62C;
    result = RtlCompareMemory(a3 + 16, v_stack_m60, result + 8, 1);
    if (result != 8) goto loc_00A0C62C;
    result = 0;
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (unsigned int)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C4A5;
    a4 = 0;
    v_stack_p30 = v_stack_p18;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p10, (unsigned int)(0x900F4ULL), a3, a4);
    if (sign_flag) goto loc_00A0C479;
    if (v_stack_p18 < 64) goto loc_00A0C649;
    v_stack_p30 = v_stack_p18;
    a4 = 0;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    v_stack_m58 = *(unsigned __int64 *)(result);
    result = FsRtlKernelFsControlFile(v_stack_p10, (unsigned int)(0x900EBULL), a3, a4);
    if (sign_flag) goto loc_00A0C479;
    if (v_stack_p18 < 64) goto loc_00A0C649;
    v_stack_m68 = *(unsigned __int64 *)(result + 24);
    v_stack_p8 = v_stack_m58;
loc_00A0C479:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    if (sign_flag) goto loc_00A0C4A5;
    result = v_stack_m50;
    v_r14 = result + 2;
    if (v_stack_p8 == (*(unsigned __int64 *)(v_stack_m50))) {
        a1 = v_stack_m68;
        result = 3;
        v_r14 = result + 2;
        if (a1 == (*(unsigned __int64 *)(v_stack_m50 + 8))) { v_r14 = (unsigned int)(result); }
    }
loc_00A0C4A9:
    result = v_stack_p10;
    if (v_stack_p10 != 0) {
        a1 = v_stack_p10;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_r12 = 0;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_00A0C1A4;
    *(unsigned int *)(a4 + 4) = 20;
    result = ExAllocatePool2(256, 20, (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00A0C665;
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result == 0) goto loc_00A0C5D9;
loc_00A0C51C:
    if (0 >= 0) goto loc_00A0C545;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0C19F;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00A0C19F;
    a1 = (unsigned int)((0) + 1);
    goto loc_00A0C51C;
loc_00A0C545:
    if ((a3 + 4) < a3) goto loc_00A0C19F;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00A0C636;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = v_stack_m48;
loc_00A0C56F:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A0C5EC;
loc_00A0C580:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A0C5A9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0C19F;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A0C19F;
    a1 = (unsigned int)((0) + 1);
    goto loc_00A0C580;
loc_00A0C5A9:
    if ((a3 + 4) < a3) goto loc_00A0C19F;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00A0C636;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)(v_r14);
    goto loc_00A0C1A4;
loc_00A0C5D9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0C653;
    goto loc_00A0C19F;
loc_00A0C5EC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4))) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8); }
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    v_rbx = (unsigned int)(((unsigned int)(0xC0000095ULL)) & ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0C1A4;
    goto loc_00A0C1A4;
loc_00A0C618:
    goto loc_00A0C1A4;
loc_00A0C622:
    goto loc_00A0C4A9;
loc_00A0C62C:
    goto loc_00A0C4A9;
loc_00A0C636:
    goto loc_00A0C1A4;
loc_00A0C640:
    result = 0;
loc_00A0C642:
    goto loc_00A0C4A9;
loc_00A0C649:
    goto loc_00A0C479;
loc_00A0C653:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00A0C56F;
loc_00A0C65B:
    goto loc_00A0C1A4;
loc_00A0C665:
    goto loc_00A0C1A4;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A0C12C(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    local_r11 = 0;
    if (Arg1 == NULL) goto loc_00A0C618;
    if (Arg4 == NULL) goto loc_00A0C618;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A0C618;
    if ((*(uint32_t *)(arg1)) <= ((uint32_t)(local_r11 + 3))) goto loc_00A0C618;
loc_00A0C18E:
    if (0 >= ((uint32_t)(local_r11 + 3))) goto loc_00A0C1D0;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0C1C2;
loc_00A0C19F:
loc_00A0C1A4:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
loc_00A0C1C2:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0C19F;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00A0C18E;
loc_00A0C1D0:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0C19F;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A0C636;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00A0C618;
loc_00A0C1F9:
    v_stack_m48 = *(uint64_t *)(result);
    if (0 >= 4) goto loc_00A0C21C;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0C19F;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0C19F;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00A0C1F9;
loc_00A0C21C:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0C19F;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg1 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A0C65B;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (*(uint64_t *)(arg1) == 0) goto loc_00A0C618;
    v_stack_p28 = 0;
    Arg2 = 0;
    v_stack_p20 = v_stack_p10;
    v_stack_p10 = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(arg1), Arg2, *(uint64_t *)(v_rip + 0x5BA880), 1);
    v_stack_p10 = v_stack_p10;
    if (sign_flag) goto loc_00A0C4A9;
    result = ExAllocatePool2(256, 31, (uint32_t)(0x20534C53ULL), 1);
    local_rsi = 0;
    if (result == 0) goto loc_00A0C622;
    *(uint64_t *)(result + 0x5) = 0;
    *(uint64_t *)(result + 0xD) = 0;
    *(uint64_t *)(result + 0x15) = 0;
    *(uint16_t *)(result + 0x1D) = 0;
    *(uint8_t *)(result + 0x4) = 25;
    *(uint32_t *)(result) = 0;
    *(uint64_t *)(result + 0x5) = v_xmm0;
    *(uint64_t *)(result + 0x15) = v_xmm1;
    *(uint8_t *)(result + 0x1D) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x13F14C) + 0x18));
    result = ExAllocatePool2(256, local_rsi + 58, (uint32_t)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C622;
    *(uint64_t *)(result) = v_xmm0;
    result = 0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = 0;
    *(uint16_t *)(result + 0x38) = 0;
    v_stack_p40 = v_stack_p18;
    v_stack_p38 = 1;
    v_stack_p30 = 0;
    v_stack_p28 = 31;
    v_stack_p20 = 0;
    result = FsRtlQueryKernelEaFile(v_stack_p10, 0, local_rsi + 58, 1);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_00A0C640;
    if (sign_flag) goto loc_00A0C4A9;
    Arg3 = (*(uint8_t *)(result + 0x5)) + (9);
    Arg3 = (Arg3) + (result);
    result = ((uint32_t)(v_stack_p18)) + (result);
    v_stack_m50 = Arg3;
    if ((Arg3 + *(uint16_t *)(result + 0x6) * 1) > result) goto loc_00A0C62C;
    result = 0;
    if (0 == ((uint16_t)(*(uint16_t *)(result + 0x6)))) goto loc_00A0C642;
    if (((uint32_t)(*(uint16_t *)(result + 0x6))) != 24) goto loc_00A0C62C;
    result = RtlCompareMemory(Arg3 + 16, v_stack_m60, result + 8, 1);
    if (result != 8) goto loc_00A0C62C;
    result = 0;
    v_stack_p18 = 0;
    result = ExAllocatePool2(256, 584, (uint32_t)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0C4A5;
    Arg4 = 0;
    v_stack_p30 = v_stack_p18;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p10, (uint32_t)(0x900F4ULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0C479;
    if (v_stack_p18 < 64) goto loc_00A0C649;
    v_stack_p30 = v_stack_p18;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    v_stack_m58 = *(uint64_t *)(result);
    result = FsRtlKernelFsControlFile(v_stack_p10, (uint32_t)(0x900EBULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0C479;
    if (v_stack_p18 < 64) goto loc_00A0C649;
    v_stack_m68 = *(uint64_t *)(result + 0x18);
    v_stack_p8 = v_stack_m58;
loc_00A0C479:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00A0C4A5;
    result = v_stack_m50;
    local_r14 = result + 2;
    if (v_stack_p8 == (*(uint64_t *)(v_stack_m50))) {
        Arg1 = v_stack_m68;
        result = 3;
        local_r14 = result + 2;
        if (Arg1 == (*(uint64_t *)(v_stack_m50 + 0x8))) { local_r14 = (uint32_t)(result); }
    }
loc_00A0C4A9:
    result = v_stack_p10;
    if (v_stack_p10 != 0) {
        Arg1 = v_stack_p10;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_r12 = 0;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_00A0C1A4;
    *(uint32_t *)(arg4 + 0x4) = 20;
    result = ExAllocatePool2(256, 20, (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00A0C665;
    *(uint64_t *)(arg4 + 0x8) = result;
    *(uint32_t *)(arg4) = 0;
    if (result == 0) goto loc_00A0C5D9;
loc_00A0C51C:
    if (0 >= 0) goto loc_00A0C545;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0C19F;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00A0C19F;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00A0C51C;
loc_00A0C545:
    if ((Arg3 + 4) < Arg3) goto loc_00A0C19F;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00A0C636;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = v_stack_m48;
loc_00A0C56F:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A0C5EC;
loc_00A0C580:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A0C5A9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0C19F;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A0C19F;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00A0C580;
loc_00A0C5A9:
    if ((Arg3 + 4) < Arg3) goto loc_00A0C19F;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00A0C636;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)(local_r14);
    goto loc_00A0C1A4;
loc_00A0C5D9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0C653;
    goto loc_00A0C19F;
loc_00A0C5EC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x4))) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8); }
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(0xC0000095ULL)) & ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0C1A4;
    goto loc_00A0C1A4;
loc_00A0C618:
    goto loc_00A0C1A4;
loc_00A0C622:
    goto loc_00A0C4A9;
loc_00A0C62C:
    goto loc_00A0C4A9;
loc_00A0C636:
    goto loc_00A0C1A4;
loc_00A0C640:
    result = 0;
loc_00A0C642:
    goto loc_00A0C4A9;
loc_00A0C649:
    goto loc_00A0C479;
loc_00A0C653:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8);
    goto loc_00A0C56F;
loc_00A0C65B:
    goto loc_00A0C1A4;
loc_00A0C665:
    goto loc_00A0C1A4;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0C12C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
