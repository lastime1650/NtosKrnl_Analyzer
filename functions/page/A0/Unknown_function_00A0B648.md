# sub_00A0B648

- RVA: `0x00A0B648`–`0x00A0BA6E` (길이 `1,062` bytes)
- VA: `0x0000000140A0B648`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8A38`
- 디코드: `295`개 명령, `1,062/1,062` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A0B7D1` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A0B7FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0B82B` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0B871` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)
- `0x00A0B897` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0B8A4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A0B8C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A0B9B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A0BA15` → [FsRtlKernelFsControlFile](FsRtlKernelFsControlFile_function_00A0CA70.md) (function, `0x00A0CA70`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x00969C54`

### Static image references
- `0x00A0B7AE` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00A0B7FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0B897` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0B8A4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A0B8C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A0B9B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0B648  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A0B64D  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00A0B652  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A0B657  55                              push rbp
00A0B658  56                              push rsi
00A0B659  57                              push rdi
00A0B65A  41 54                           push r12
00A0B65C  41 55                           push r13
00A0B65E  41 56                           push r14
00A0B660  41 57                           push r15
00A0B662  48 8B EC                        mov rbp, rsp
00A0B665  48 83 EC 50                     sub rsp, 0x50
00A0B669  0F 57 C0                        xorps xmm0, xmm0
00A0B66C  49 8B F9                        mov rdi, r9
00A0B66F  4C 8B C1                        mov r8, rcx
00A0B672  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00A0B676  48 85 C9                        test rcx, rcx
00A0B679  0F 84 87 03 00 00               je 0x140a0ba06
00A0B67F  4D 85 C9                        test r9, r9
00A0B682  0F 84 7E 03 00 00               je 0x140a0ba06
00A0B688  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A0B68C  48 85 C9                        test rcx, rcx
00A0B68F  0F 84 71 03 00 00               je 0x140a0ba06
00A0B695  41 83 38 03                     cmp dword ptr [r8], 3
00A0B699  0F 86 67 03 00 00               jbe 0x140a0ba06
00A0B69F  48 8B C1                        mov rax, rcx
00A0B6A2  45 33 C9                        xor r9d, r9d
00A0B6A5  44 8B 10                        mov r10d, dword ptr [rax]
00A0B6A8  48 8D 50 04                     lea rdx, [rax + 4]
00A0B6AC  41 83 F9 03                     cmp r9d, 3
00A0B6B0  73 33                           jae 0x140a0b6e5
00A0B6B2  48 3B D0                        cmp rdx, rax
00A0B6B5  73 20                           jae 0x140a0b6d7
00A0B6B7  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A0B6BC  8B C3                           mov eax, ebx
00A0B6BE  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00A0B6C6  48 83 C4 50                     add rsp, 0x50
00A0B6CA  41 5F                           pop r15
00A0B6CC  41 5E                           pop r14
00A0B6CE  41 5D                           pop r13
00A0B6D0  41 5C                           pop r12
00A0B6D2  5F                              pop rdi
00A0B6D3  5E                              pop rsi
00A0B6D4  5D                              pop rbp
00A0B6D5  C3                              ret
00A0B6D6  CC                              int3
00A0B6D7  4A 8D 04 12                     lea rax, [rdx + r10]
00A0B6DB  48 3B C2                        cmp rax, rdx
00A0B6DE  72 D7                           jb 0x140a0b6b7
00A0B6E0  41 FF C1                        inc r9d
00A0B6E3  EB C0                           jmp 0x140a0b6a5
00A0B6E5  48 3B D0                        cmp rdx, rax
00A0B6E8  72 CD                           jb 0x140a0b6b7
00A0B6EA  33 C0                           xor eax, eax
00A0B6EC  45 85 D2                        test r10d, r10d
00A0B6EF  48 0F 45 C2                     cmovne rax, rdx
00A0B6F3  41 83 FA 08                     cmp r10d, 8
00A0B6F7  0F 85 35 03 00 00               jne 0x140a0ba32
00A0B6FD  41 83 38 04                     cmp dword ptr [r8], 4
00A0B701  4C 8B 20                        mov r12, qword ptr [rax]
00A0B704  0F 86 FC 02 00 00               jbe 0x140a0ba06
00A0B70A  48 8B C1                        mov rax, rcx
00A0B70D  45 33 C9                        xor r9d, r9d
00A0B710  44 8B 18                        mov r11d, dword ptr [rax]
00A0B713  48 8D 50 04                     lea rdx, [rax + 4]
00A0B717  41 83 F9 04                     cmp r9d, 4
00A0B71B  73 13                           jae 0x140a0b730
00A0B71D  48 3B D0                        cmp rdx, rax
00A0B720  72 95                           jb 0x140a0b6b7
00A0B722  4A 8D 04 1A                     lea rax, [rdx + r11]
00A0B726  48 3B C2                        cmp rax, rdx
00A0B729  72 8C                           jb 0x140a0b6b7
00A0B72B  41 FF C1                        inc r9d
00A0B72E  EB E0                           jmp 0x140a0b710
00A0B730  48 3B D0                        cmp rdx, rax
00A0B733  72 82                           jb 0x140a0b6b7
00A0B735  45 33 D2                        xor r10d, r10d
00A0B738  45 85 DB                        test r11d, r11d
00A0B73B  4C 0F 45 D2                     cmovne r10, rdx
00A0B73F  41 83 FB 08                     cmp r11d, 8
00A0B743  0F 85 07 03 00 00               jne 0x140a0ba50
00A0B749  41 83 38 05                     cmp dword ptr [r8], 5
00A0B74D  4D 8B 12                        mov r10, qword ptr [r10]
00A0B750  0F 86 B0 02 00 00               jbe 0x140a0ba06
00A0B756  45 33 C0                        xor r8d, r8d
00A0B759  8B 01                           mov eax, dword ptr [rcx]
00A0B75B  48 8D 51 04                     lea rdx, [rcx + 4]
00A0B75F  41 83 F8 05                     cmp r8d, 5
00A0B763  73 1B                           jae 0x140a0b780
00A0B765  48 3B D1                        cmp rdx, rcx
00A0B768  0F 82 49 FF FF FF               jb 0x140a0b6b7
00A0B76E  48 8D 0C 02                     lea rcx, [rdx + rax]
00A0B772  48 3B CA                        cmp rcx, rdx
00A0B775  0F 82 3C FF FF FF               jb 0x140a0b6b7
00A0B77B  41 FF C0                        inc r8d
00A0B77E  EB D9                           jmp 0x140a0b759
00A0B780  48 3B D1                        cmp rdx, rcx
00A0B783  0F 82 2E FF FF FF               jb 0x140a0b6b7
00A0B789  33 F6                           xor esi, esi
00A0B78B  85 C0                           test eax, eax
00A0B78D  48 0F 45 F2                     cmovne rsi, rdx
00A0B791  83 F8 04                        cmp eax, 4
00A0B794  0F 85 98 02 00 00               jne 0x140a0ba32
00A0B79A  8B 36                           mov esi, dword ptr [rsi]
00A0B79C  83 FE 10                        cmp esi, 0x10
00A0B79F  0F 85 AB 02 00 00               jne 0x140a0ba50
00A0B7A5  4D 85 D2                        test r10, r10
00A0B7A8  0F 84 58 02 00 00               je 0x140a0ba06
00A0B7AE  4C 8B 05 2B B3 5B 00            mov r8, qword ptr [rip + 0x5bb32b]
00A0B7B5  48 8D 45 48                     lea rax, [rbp + 0x48]
00A0B7B9  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00A0B7BF  41 B1 01                        mov r9b, 1
00A0B7C2  48 83 65 48 00                  and qword ptr [rbp + 0x48], 0
00A0B7C7  33 D2                           xor edx, edx
00A0B7C9  49 8B CA                        mov rcx, r10
00A0B7CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0B7D1  E8 DA D5 E5 FF                  call 0x140868db0
00A0B7D6  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
00A0B7DA  8B D8                           mov ebx, eax
00A0B7DC  85 C0                           test eax, eax
00A0B7DE  0F 88 B8 00 00 00               js 0x140a0b89c
00A0B7E4  83 65 50 00                     and dword ptr [rbp + 0x50], 0
00A0B7E8  BB 48 02 00 00                  mov ebx, 0x248
00A0B7ED  8B D3                           mov edx, ebx
00A0B7EF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0B7F5  B9 00 01 00 00                  mov ecx, 0x100
00A0B7FA  E8 F1 68 17 00                  call 0x140b820f0
00A0B7FF  4C 8B F0                        mov r14, rax
00A0B802  48 85 C0                        test rax, rax
00A0B805  0F 84 4F 02 00 00               je 0x140a0ba5a
00A0B80B  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0B80F  45 33 C9                        xor r9d, r9d
00A0B812  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0B817  45 33 C0                        xor r8d, r8d
00A0B81A  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A0B81E  BA F4 00 09 00                  mov edx, 0x900f4
00A0B823  49 8B CF                        mov rcx, r15
00A0B826  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A0B82B  E8 40 12 00 00                  call 0x140a0ca70
00A0B830  8B D8                           mov ebx, eax
00A0B832  85 C0                           test eax, eax
00A0B834  78 5C                           js 0x140a0b892
00A0B836  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0B83A  0F 82 FC 01 00 00               jb 0x140a0ba3c
00A0B840  4D 8B 2E                        mov r13, qword ptr [r14]
00A0B843  48 8D 45 50                     lea rax, [rbp + 0x50]
00A0B847  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0B84C  45 33 C9                        xor r9d, r9d
00A0B84F  45 33 C0                        xor r8d, r8d
00A0B852  C7 44 24 28 48 02 00 00         mov dword ptr [rsp + 0x28], 0x248
00A0B85A  49 8B CF                        mov rcx, r15
00A0B85D  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A0B862  45 38 47 4B                     cmp byte ptr [r15 + 0x4b], r8b
00A0B866  0F 85 A4 01 00 00               jne 0x140a0ba10
00A0B86C  BA EB 00 09 00                  mov edx, 0x900eb
00A0B871  E8 FA 11 00 00                  call 0x140a0ca70
00A0B876  8B D8                           mov ebx, eax
00A0B878  85 C0                           test eax, eax
00A0B87A  78 16                           js 0x140a0b892
00A0B87C  83 7D 50 40                     cmp dword ptr [rbp + 0x50], 0x40
00A0B880  0F 82 B6 01 00 00               jb 0x140a0ba3c
00A0B886  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00A0B88A  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
00A0B88E  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A0B892  33 D2                           xor edx, edx
00A0B894  49 8B CE                        mov rcx, r14
00A0B897  E8 D4 6F 17 00                  call 0x140b82870
00A0B89C  4D 85 FF                        test r15, r15
00A0B89F  74 08                           je 0x140a0b8a9
00A0B8A1  49 8B CF                        mov rcx, r15
00A0B8A4  E8 A7 DA 8E FF                  call 0x1402f9350
00A0B8A9  85 DB                           test ebx, ebx
00A0B8AB  0F 88 0B FE FF FF               js 0x140a0b6bc
00A0B8B1  BA 20 00 00 00                  mov edx, 0x20
00A0B8B6  B9 00 01 00 00                  mov ecx, 0x100
00A0B8BB  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A0B8C1  89 57 04                        mov dword ptr [rdi + 4], edx
00A0B8C4  E8 27 68 17 00                  call 0x140b820f0
00A0B8C9  48 85 C0                        test rax, rax
00A0B8CC  0F 84 92 01 00 00               je 0x140a0ba64
00A0B8D2  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A0B8D6  83 27 00                        and dword ptr [rdi], 0
00A0B8D9  48 8B D0                        mov rdx, rax
00A0B8DC  48 85 C0                        test rax, rax
00A0B8DF  0F 84 0E 01 00 00               je 0x140a0b9f3
00A0B8E5  44 8B 0F                        mov r9d, dword ptr [rdi]
00A0B8E8  33 C9                           xor ecx, ecx
00A0B8EA  41 3B C9                        cmp ecx, r9d
00A0B8ED  73 24                           jae 0x140a0b913
00A0B8EF  8B 02                           mov eax, dword ptr [rdx]
00A0B8F1  83 C0 04                        add eax, 4
00A0B8F4  83 F8 04                        cmp eax, 4
00A0B8F7  0F 82 BA FD FF FF               jb 0x140a0b6b7
00A0B8FD  44 8B C0                        mov r8d, eax
00A0B900  4C 03 C2                        add r8, rdx
00A0B903  4C 3B C2                        cmp r8, rdx
00A0B906  0F 82 AB FD FF FF               jb 0x140a0b6b7
00A0B90C  49 8B D0                        mov rdx, r8
00A0B90F  FF C1                           inc ecx
00A0B911  EB D7                           jmp 0x140a0b8ea
00A0B913  4C 8D 42 04                     lea r8, [rdx + 4]
00A0B917  4C 3B C2                        cmp r8, rdx
00A0B91A  0F 82 97 FD FF FF               jb 0x140a0b6b7
00A0B920  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0B923  48 8D 42 0C                     lea rax, [rdx + 0xc]
00A0B927  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A0B92B  48 3B C1                        cmp rax, rcx
00A0B92E  0F 87 FE 00 00 00               ja 0x140a0ba32
00A0B934  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00A0B93A  4D 89 20                        mov qword ptr [r8], r12
00A0B93D  FF 07                           inc dword ptr [rdi]
00A0B93F  85 F6                           test esi, esi
00A0B941  0F 84 BF 00 00 00               je 0x140a0ba06
00A0B947  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A0B94B  48 85 D2                        test rdx, rdx
00A0B94E  74 6C                           je 0x140a0b9bc
00A0B950  44 8B 0F                        mov r9d, dword ptr [rdi]
00A0B953  33 C9                           xor ecx, ecx
00A0B955  41 3B C9                        cmp ecx, r9d
00A0B958  73 24                           jae 0x140a0b97e
00A0B95A  8B 02                           mov eax, dword ptr [rdx]
00A0B95C  83 C0 04                        add eax, 4
00A0B95F  83 F8 04                        cmp eax, 4
00A0B962  0F 82 4F FD FF FF               jb 0x140a0b6b7
00A0B968  44 8B C0                        mov r8d, eax
00A0B96B  4C 03 C2                        add r8, rdx
00A0B96E  4C 3B C2                        cmp r8, rdx
00A0B971  0F 82 40 FD FF FF               jb 0x140a0b6b7
00A0B977  49 8B D0                        mov rdx, r8
00A0B97A  FF C1                           inc ecx
00A0B97C  EB D7                           jmp 0x140a0b955
00A0B97E  4C 8D 4A 04                     lea r9, [rdx + 4]
00A0B982  4C 3B CA                        cmp r9, rdx
00A0B985  0F 82 2C FD FF FF               jb 0x140a0b6b7
00A0B98B  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A0B98E  48 8D 46 04                     lea rax, [rsi + 4]
00A0B992  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A0B996  48 03 C2                        add rax, rdx
00A0B999  33 DB                           xor ebx, ebx
00A0B99B  4C 8B C6                        mov r8, rsi
00A0B99E  48 3B C1                        cmp rax, rcx
00A0B9A1  0F 87 8B 00 00 00               ja 0x140a0ba32
00A0B9A7  89 32                           mov dword ptr [rdx], esi
00A0B9A9  49 8B C9                        mov rcx, r9
00A0B9AC  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00A0B9B0  E8 8B AE CB FF                  call 0x1406c6840
00A0B9B5  FF 07                           inc dword ptr [rdi]
00A0B9B7  E9 00 FD FF FF                  jmp 0x140a0b6bc
00A0B9BC  83 C6 04                        add esi, 4
00A0B9BF  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A0B9C4  83 FE 04                        cmp esi, 4
00A0B9C7  0F 82 EF FC FF FF               jb 0x140a0b6bc
00A0B9CD  8B 57 04                        mov edx, dword ptr [rdi + 4]
00A0B9D0  83 C8 FF                        or eax, 0xffffffff
00A0B9D3  8D 0C 32                        lea ecx, [rdx + rsi]
00A0B9D6  3B CA                           cmp ecx, edx
00A0B9D8  0F 43 C1                        cmovae eax, ecx
00A0B9DB  89 47 04                        mov dword ptr [rdi + 4], eax
00A0B9DE  1B C0                           sbb eax, eax
00A0B9E0  23 D8                           and ebx, eax
00A0B9E2  3B CA                           cmp ecx, edx
00A0B9E4  0F 82 D2 FC FF FF               jb 0x140a0b6bc
00A0B9EA  FF 07                           inc dword ptr [rdi]
00A0B9EC  33 DB                           xor ebx, ebx
00A0B9EE  E9 C9 FC FF FF                  jmp 0x140a0b6bc
00A0B9F3  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A0B9F6  8D 48 0C                        lea ecx, [rax + 0xc]
00A0B9F9  3B C8                           cmp ecx, eax
00A0B9FB  73 49                           jae 0x140a0ba46
00A0B9FD  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00A0BA01  E9 B1 FC FF FF                  jmp 0x140a0b6b7
00A0BA06  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A0BA0B  E9 AC FC FF FF                  jmp 0x140a0b6bc
00A0BA10  BA EF 00 09 00                  mov edx, 0x900ef
00A0BA15  E8 56 10 00 00                  call 0x140a0ca70
00A0BA1A  8B D8                           mov ebx, eax
00A0BA1C  85 C0                           test eax, eax
00A0BA1E  0F 88 6E FE FF FF               js 0x140a0b892
00A0BA24  83 7D 50 08                     cmp dword ptr [rbp + 0x50], 8
00A0BA28  72 12                           jb 0x140a0ba3c
00A0BA2A  49 8B 06                        mov rax, qword ptr [r14]
00A0BA2D  E9 58 FE FF FF                  jmp 0x140a0b88a
00A0BA32  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A0BA37  E9 80 FC FF FF                  jmp 0x140a0b6bc
00A0BA3C  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A0BA41  E9 4C FE FF FF                  jmp 0x140a0b892
00A0BA46  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A0BA49  FF 07                           inc dword ptr [rdi]
00A0BA4B  E9 F7 FE FF FF                  jmp 0x140a0b947
00A0BA50  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A0BA55  E9 62 FC FF FF                  jmp 0x140a0b6bc
00A0BA5A  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0BA5F  E9 38 FE FF FF                  jmp 0x140a0b89c
00A0BA64  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A0BA69  E9 4E FC FF FF                  jmp 0x140a0b6bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A0B648(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (80);
    v_stack_m48 = v_xmm0;
    if (a1 == 0) goto loc_00A0BA06;
    if (a4 == 0) goto loc_00A0BA06;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A0BA06;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A0BA06;
    a4 = 0;
loc_00A0B6A5:
    if (0 >= 3) goto loc_00A0B6E5;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0B6D7;
loc_00A0B6B7:
loc_00A0B6BC:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
loc_00A0B6D7:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0B6B7;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A0B6A5;
loc_00A0B6E5:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0B6B7;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A0BA32;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00A0BA06;
    a4 = 0;
loc_00A0B710:
    if (0 >= 4) goto loc_00A0B730;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0B6B7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0B6B7;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A0B710;
loc_00A0B730:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0B6B7;
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r10 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A0BA50;
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00A0BA06;
    a3 = 0;
loc_00A0B759:
    if (0 >= 5) goto loc_00A0B780;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A0B6B7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A0B6B7;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00A0B759;
loc_00A0B780:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A0B6B7;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 4) goto loc_00A0BA32;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) != 16) goto loc_00A0BA50;
    if (*(unsigned __int64 *)(v_r10) == 0) goto loc_00A0BA06;
    a2 = 0;
    v_stack_p20 = v_stack_p10;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_r10), a2, *(unsigned __int64 *)(v_rip + 6009643), 1);
    if (sign_flag) goto loc_00A0B89C;
    result = ExAllocatePool2(256, 584, (unsigned int)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0BA5A;
    a4 = 0;
    v_stack_p30 = v_stack_p18;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p10, (unsigned int)(0x900F4ULL), a3, a4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 64) goto loc_00A0BA3C;
    v_stack_p30 = v_stack_p18;
    a4 = 0;
    a3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    if ((*(unsigned __int8 *)(v_stack_p10 + 75)) != 0) goto loc_00A0BA10;
    result = FsRtlKernelFsControlFile(v_stack_p10, (unsigned int)(0x900EBULL), a3, a4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 64) goto loc_00A0BA3C;
loc_00A0B88A:
    v_stack_m48 = *(unsigned __int64 *)(result);
    v_stack_m40 = *(unsigned __int64 *)(result + 24);
loc_00A0B892:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_00A0B89C:
    if (v_stack_p10 != 0) {
        a1 = v_stack_p10;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_00A0B6BC;
    *(unsigned int *)(a4 + 4) = 32;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00A0BA64;
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result == 0) goto loc_00A0B9F3;
    a1 = 0;
loc_00A0B8EA:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A0B913;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0B6B7;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00A0B6B7;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A0B8EA;
loc_00A0B913:
    if ((a3 + 4) < a3) goto loc_00A0B6B7;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00A0BA32;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00A0BA06;
loc_00A0B947:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A0B9BC;
    a1 = 0;
loc_00A0B955:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A0B97E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A0B6B7;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A0B6B7;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A0B955;
loc_00A0B97E:
    if ((a3 + 4) < a3) goto loc_00A0B6B7;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = ((unsigned int)(*(unsigned int *)(v_rsi)) + 4) + (a3);
    v_rbx = 0;
    if (result > a1) goto loc_00A0BA32;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    result = memcpy(a3 + 4, v_stack_m48, (unsigned int)(*(unsigned int *)(v_rsi)), a3 + 4);
    goto loc_00A0B6BC;
loc_00A0B9BC:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) + (4));
    if (((unsigned int)(v_rsi)) < 4) goto loc_00A0B6BC;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rsi * 1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rsi * 1); }
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    v_rbx = (unsigned int)(((unsigned int)(0xC0000095ULL)) & ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rsi * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0B6BC;
    v_rbx = 0;
    goto loc_00A0B6BC;
loc_00A0B9F3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A0BA46;
    goto loc_00A0B6B7;
loc_00A0BA06:
    goto loc_00A0B6BC;
loc_00A0BA10:
    result = FsRtlKernelFsControlFile((unsigned int)(*(unsigned int *)(a4 + 4)) + 12, (unsigned int)(0x900EFULL), (unsigned int)(*(unsigned int *)(v_rsi)), a3 + 4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 8) goto loc_00A0BA3C;
    goto loc_00A0B88A;
loc_00A0BA32:
    goto loc_00A0B6BC;
loc_00A0BA3C:
    goto loc_00A0B892;
loc_00A0BA46:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_00A0B947;
loc_00A0BA50:
    goto loc_00A0B6BC;
loc_00A0BA5A:
    goto loc_00A0B89C;
loc_00A0BA64:
    goto loc_00A0B6BC;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A0B648(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (80);
    v_stack_m48 = v_xmm0;
    if (Arg1 == NULL) goto loc_00A0BA06;
    if (Arg4 == NULL) goto loc_00A0BA06;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A0BA06;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A0BA06;
    Arg4 = 0;
loc_00A0B6A5:
    if (0 >= 3) goto loc_00A0B6E5;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0B6D7;
loc_00A0B6B7:
loc_00A0B6BC:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
loc_00A0B6D7:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0B6B7;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A0B6A5;
loc_00A0B6E5:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0B6B7;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A0BA32;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00A0BA06;
    Arg4 = 0;
loc_00A0B710:
    if (0 >= 4) goto loc_00A0B730;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0B6B7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0B6B7;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A0B710;
loc_00A0B730:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0B6B7;
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r10 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A0BA50;
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00A0BA06;
    Arg3 = 0;
loc_00A0B759:
    if (0 >= 5) goto loc_00A0B780;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A0B6B7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A0B6B7;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00A0B759;
loc_00A0B780:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A0B6B7;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 4) goto loc_00A0BA32;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) != 16) goto loc_00A0BA50;
    if (*(uint64_t *)(local_r10) == 0) goto loc_00A0BA06;
    Arg2 = 0;
    v_stack_p20 = v_stack_p10;
    result = ObReferenceObjectByHandle(*(uint64_t *)(local_r10), Arg2, *(uint64_t *)(v_rip + 0x5BB32B), 1);
    if (sign_flag) goto loc_00A0B89C;
    result = ExAllocatePool2(256, 584, (uint32_t)(0x20534C53ULL), 1);
    if (result == 0) goto loc_00A0BA5A;
    Arg4 = 0;
    v_stack_p30 = v_stack_p18;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    result = FsRtlKernelFsControlFile(v_stack_p10, (uint32_t)(0x900F4ULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 64) goto loc_00A0BA3C;
    v_stack_p30 = v_stack_p18;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = 584;
    v_stack_p20 = result;
    if ((*(uint8_t *)(v_stack_p10 + 0x4B)) != 0) goto loc_00A0BA10;
    result = FsRtlKernelFsControlFile(v_stack_p10, (uint32_t)(0x900EBULL), Arg3, Arg4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 64) goto loc_00A0BA3C;
loc_00A0B88A:
    v_stack_m48 = *(uint64_t *)(result);
    v_stack_m40 = *(uint64_t *)(result + 0x18);
loc_00A0B892:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
loc_00A0B89C:
    if (v_stack_p10 != 0) {
        Arg1 = v_stack_p10;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_00A0B6BC;
    *(uint32_t *)(arg4 + 0x4) = 32;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00A0BA64;
    *(uint64_t *)(arg4 + 0x8) = result;
    if (result == 0) goto loc_00A0B9F3;
    Arg1 = 0;
loc_00A0B8EA:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A0B913;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0B6B7;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00A0B6B7;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A0B8EA;
loc_00A0B913:
    if ((Arg3 + 4) < Arg3) goto loc_00A0B6B7;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00A0BA32;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00A0BA06;
loc_00A0B947:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A0B9BC;
    Arg1 = 0;
loc_00A0B955:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A0B97E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A0B6B7;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A0B6B7;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A0B955;
loc_00A0B97E:
    if ((Arg3 + 4) < Arg3) goto loc_00A0B6B7;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    result = ((uint32_t)(*(uint32_t *)(local_rsi)) + 4) + (Arg3);
    local_rbx = 0;
    if (result > Arg1) goto loc_00A0BA32;
    *(uint32_t *)(Arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    result = memcpy(Arg3 + 4, v_stack_m48, (uint32_t)(*(uint32_t *)(local_rsi)), Arg3 + 4);
    goto loc_00A0B6BC;
loc_00A0B9BC:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) + (4));
    if (((uint32_t)(local_rsi)) < 4) goto loc_00A0B6BC;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + local_rsi * 1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + local_rsi * 1); }
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(0xC0000095ULL)) & ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + local_rsi * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0B6BC;
    local_rbx = 0;
    goto loc_00A0B6BC;
loc_00A0B9F3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A0BA46;
    goto loc_00A0B6B7;
loc_00A0BA06:
    goto loc_00A0B6BC;
loc_00A0BA10:
    result = FsRtlKernelFsControlFile((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12, (uint32_t)(0x900EFULL), (uint32_t)(*(uint32_t *)(local_rsi)), Arg3 + 4);
    if (sign_flag) goto loc_00A0B892;
    if (v_stack_p18 < 8) goto loc_00A0BA3C;
    goto loc_00A0B88A;
loc_00A0BA32:
    goto loc_00A0B6BC;
loc_00A0BA3C:
    goto loc_00A0B892;
loc_00A0BA46:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12);
    goto loc_00A0B947;
loc_00A0BA50:
    goto loc_00A0B6BC;
loc_00A0BA5A:
    goto loc_00A0B89C;
loc_00A0BA64:
    goto loc_00A0B6BC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0B648&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
