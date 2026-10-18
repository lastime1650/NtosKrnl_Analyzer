# sub_00AD777C

- RVA: `0x00AD777C`–`0x00AD7D59` (길이 `1,501` bytes)
- VA: `0x0000000140AD777C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEBC0`
- 디코드: `420`개 명령, `1,501/1,501` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AD78EA` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD7929` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD7949` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD79D0` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD7A0F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD7A2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD7B8D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD7BDF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD7C2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD7C3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A82C`

### Static image references
- `0x00AD7B4B` → RVA `0x00FD83E8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00AD78EA` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD7929` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD7949` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD79D0` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD7A0F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD7A2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD7B8D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD7BDF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD7C2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD7C3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD777C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AD7781  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00AD7786  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00AD778B  55                              push rbp
00AD778C  56                              push rsi
00AD778D  57                              push rdi
00AD778E  41 54                           push r12
00AD7790  41 55                           push r13
00AD7792  41 56                           push r14
00AD7794  41 57                           push r15
00AD7796  48 83 EC 60                     sub rsp, 0x60
00AD779A  33 FF                           xor edi, edi
00AD779C  4D 8B F1                        mov r14, r9
00AD779F  48 8B D9                        mov rbx, rcx
00AD77A2  8B F7                           mov esi, edi
00AD77A4  48 85 D2                        test rdx, rdx
00AD77A7  75 0A                           jne 0x140ad77b3
00AD77A9  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD77AE  E9 8B 05 00 00                  jmp 0x140ad7d3e
00AD77B3  4D 85 F6                        test r14, r14
00AD77B6  74 F1                           je 0x140ad77a9
00AD77B8  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AD77BC  48 85 C9                        test rcx, rcx
00AD77BF  74 E8                           je 0x140ad77a9
00AD77C1  83 3B 03                        cmp dword ptr [rbx], 3
00AD77C4  76 E3                           jbe 0x140ad77a9
00AD77C6  48 8B C1                        mov rax, rcx
00AD77C9  44 8B C7                        mov r8d, edi
00AD77CC  44 8B 08                        mov r9d, dword ptr [rax]
00AD77CF  48 8D 50 04                     lea rdx, [rax + 4]
00AD77D3  41 83 F8 03                     cmp r8d, 3
00AD77D7  73 1B                           jae 0x140ad77f4
00AD77D9  48 3B D0                        cmp rdx, rax
00AD77DC  0F 82 57 05 00 00               jb 0x140ad7d39
00AD77E2  4A 8D 04 0A                     lea rax, [rdx + r9]
00AD77E6  48 3B C2                        cmp rax, rdx
00AD77E9  0F 82 4A 05 00 00               jb 0x140ad7d39
00AD77EF  41 FF C0                        inc r8d
00AD77F2  EB D8                           jmp 0x140ad77cc
00AD77F4  48 3B D0                        cmp rdx, rax
00AD77F7  0F 82 3C 05 00 00               jb 0x140ad7d39
00AD77FD  45 85 C9                        test r9d, r9d
00AD7800  48 8B EF                        mov rbp, rdi
00AD7803  48 0F 45 EA                     cmovne rbp, rdx
00AD7807  41 83 F9 08                     cmp r9d, 8
00AD780B  75 50                           jne 0x140ad785d
00AD780D  83 3B 04                        cmp dword ptr [rbx], 4
00AD7810  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00AD7814  76 93                           jbe 0x140ad77a9
00AD7816  48 8B C1                        mov rax, rcx
00AD7819  44 8B C7                        mov r8d, edi
00AD781C  44 8B 08                        mov r9d, dword ptr [rax]
00AD781F  48 8D 50 04                     lea rdx, [rax + 4]
00AD7823  41 83 F8 04                     cmp r8d, 4
00AD7827  73 1B                           jae 0x140ad7844
00AD7829  48 3B D0                        cmp rdx, rax
00AD782C  0F 82 07 05 00 00               jb 0x140ad7d39
00AD7832  4A 8D 04 0A                     lea rax, [rdx + r9]
00AD7836  48 3B C2                        cmp rax, rdx
00AD7839  0F 82 FA 04 00 00               jb 0x140ad7d39
00AD783F  41 FF C0                        inc r8d
00AD7842  EB D8                           jmp 0x140ad781c
00AD7844  48 3B D0                        cmp rdx, rax
00AD7847  0F 82 EC 04 00 00               jb 0x140ad7d39
00AD784D  45 85 C9                        test r9d, r9d
00AD7850  48 8B C7                        mov rax, rdi
00AD7853  48 0F 45 C2                     cmovne rax, rdx
00AD7857  41 83 F9 04                     cmp r9d, 4
00AD785B  74 0A                           je 0x140ad7867
00AD785D  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD7862  E9 D7 04 00 00                  jmp 0x140ad7d3e
00AD7867  83 3B 05                        cmp dword ptr [rbx], 5
00AD786A  44 8B 28                        mov r13d, dword ptr [rax]
00AD786D  44 89 AC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r13d
00AD7875  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00AD787A  0F 86 29 FF FF FF               jbe 0x140ad77a9
00AD7880  44 8B CF                        mov r9d, edi
00AD7883  44 8B 01                        mov r8d, dword ptr [rcx]
00AD7886  48 8D 51 04                     lea rdx, [rcx + 4]
00AD788A  41 83 F9 05                     cmp r9d, 5
00AD788E  73 23                           jae 0x140ad78b3
00AD7890  48 3B D1                        cmp rdx, rcx
00AD7893  0F 82 A0 04 00 00               jb 0x140ad7d39
00AD7899  4A 8D 0C 02                     lea rcx, [rdx + r8]
00AD789D  44 89 AC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r13d
00AD78A5  48 3B CA                        cmp rcx, rdx
00AD78A8  0F 82 8B 04 00 00               jb 0x140ad7d39
00AD78AE  41 FF C1                        inc r9d
00AD78B1  EB D0                           jmp 0x140ad7883
00AD78B3  48 3B D1                        cmp rdx, rcx
00AD78B6  0F 82 7D 04 00 00               jb 0x140ad7d39
00AD78BC  45 85 C0                        test r8d, r8d
00AD78BF  4C 8B FF                        mov r15, rdi
00AD78C2  4C 0F 45 FA                     cmovne r15, rdx
00AD78C6  74 39                           je 0x140ad7901
00AD78C8  41 F6 C0 01                     test r8b, 1
00AD78CC  75 33                           jne 0x140ad7901
00AD78CE  49 8B C0                        mov rax, r8
00AD78D1  4D 8B D8                        mov r11, r8
00AD78D4  48 D1 E8                        shr rax, 1
00AD78D7  66 41 3B 7C 47 FE               cmp di, word ptr [r15 + rax*2 - 2]
00AD78DD  75 22                           jne 0x140ad7901
00AD78DF  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00AD78E4  49 8B D3                        mov rdx, r11
00AD78E7  49 8B CF                        mov rcx, r15
00AD78EA  E8 71 12 98 FF                  call 0x140458b60
00AD78EF  85 C0                           test eax, eax
00AD78F1  78 0E                           js 0x140ad7901
00AD78F3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AD78F8  48 8D 41 02                     lea rax, [rcx + 2]
00AD78FC  49 3B C3                        cmp rax, r11
00AD78FF  74 0A                           je 0x140ad790b
00AD7901  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD7906  E9 33 04 00 00                  jmp 0x140ad7d3e
00AD790B  48 D1 E9                        shr rcx, 1
00AD790E  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00AD7915  85 C9                           test ecx, ecx
00AD7917  74 E8                           je 0x140ad7901
00AD7919  44 8B E1                        mov r12d, ecx
00AD791C  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD7922  8B D1                           mov edx, ecx
00AD7924  B9 00 01 00 00                  mov ecx, 0x100
00AD7929  E8 C2 A7 0A 00                  call 0x140b820f0
00AD792E  48 8B F8                        mov rdi, rax
00AD7931  48 85 C0                        test rax, rax
00AD7934  75 0A                           jne 0x140ad7940
00AD7936  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD793B  E9 FE 03 00 00                  jmp 0x140ad7d3e
00AD7940  4D 8B C4                        mov r8, r12
00AD7943  49 8B D7                        mov rdx, r15
00AD7946  48 8B C8                        mov rcx, rax
00AD7949  E8 F2 EE BE FF                  call 0x1406c6840
00AD794E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AD7952  45 33 E4                        xor r12d, r12d
00AD7955  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00AD795A  48 85 C0                        test rax, rax
00AD795D  0F 84 96 01 00 00               je 0x140ad7af9
00AD7963  83 3B 06                        cmp dword ptr [rbx], 6
00AD7966  0F 86 8D 01 00 00               jbe 0x140ad7af9
00AD796C  45 8B C4                        mov r8d, r12d
00AD796F  8B 10                           mov edx, dword ptr [rax]
00AD7971  48 8D 48 04                     lea rcx, [rax + 4]
00AD7975  41 83 F8 06                     cmp r8d, 6
00AD7979  73 23                           jae 0x140ad799e
00AD797B  48 3B C8                        cmp rcx, rax
00AD797E  0F 82 95 02 00 00               jb 0x140ad7c19
00AD7984  48 8D 04 11                     lea rax, [rcx + rdx]
00AD7988  44 89 AC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r13d
00AD7990  48 3B C1                        cmp rax, rcx
00AD7993  0F 82 80 02 00 00               jb 0x140ad7c19
00AD7999  41 FF C0                        inc r8d
00AD799C  EB D1                           jmp 0x140ad796f
00AD799E  48 3B C8                        cmp rcx, rax
00AD79A1  0F 82 72 02 00 00               jb 0x140ad7c19
00AD79A7  85 D2                           test edx, edx
00AD79A9  4D 8B FC                        mov r15, r12
00AD79AC  4C 0F 45 F9                     cmovne r15, rcx
00AD79B0  74 35                           je 0x140ad79e7
00AD79B2  F6 C2 01                        test dl, 1
00AD79B5  75 30                           jne 0x140ad79e7
00AD79B7  48 8B C2                        mov rax, rdx
00AD79BA  4C 8B DA                        mov r11, rdx
00AD79BD  48 D1 E8                        shr rax, 1
00AD79C0  66 45 3B 64 47 FE               cmp r12w, word ptr [r15 + rax*2 - 2]
00AD79C6  75 1F                           jne 0x140ad79e7
00AD79C8  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00AD79CD  49 8B CF                        mov rcx, r15
00AD79D0  E8 8B 11 98 FF                  call 0x140458b60
00AD79D5  85 C0                           test eax, eax
00AD79D7  78 0E                           js 0x140ad79e7
00AD79D9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AD79DE  48 8D 41 02                     lea rax, [rcx + 2]
00AD79E2  49 3B C3                        cmp rax, r11
00AD79E5  74 0A                           je 0x140ad79f1
00AD79E7  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD79EC  E9 2D 02 00 00                  jmp 0x140ad7c1e
00AD79F1  48 D1 E9                        shr rcx, 1
00AD79F4  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00AD79FB  85 C9                           test ecx, ecx
00AD79FD  74 E8                           je 0x140ad79e7
00AD79FF  44 8B E1                        mov r12d, ecx
00AD7A02  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD7A08  8B D1                           mov edx, ecx
00AD7A0A  B9 00 01 00 00                  mov ecx, 0x100
00AD7A0F  E8 DC A6 0A 00                  call 0x140b820f0
00AD7A14  48 85 C0                        test rax, rax
00AD7A17  75 0A                           jne 0x140ad7a23
00AD7A19  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD7A1E  E9 FB 01 00 00                  jmp 0x140ad7c1e
00AD7A23  4D 8B C4                        mov r8, r12
00AD7A26  49 8B D7                        mov rdx, r15
00AD7A29  48 8B C8                        mov rcx, rax
00AD7A2C  48 8B F0                        mov rsi, rax
00AD7A2F  E8 0C EE BE FF                  call 0x1406c6840
00AD7A34  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AD7A38  45 33 E4                        xor r12d, r12d
00AD7A3B  48 85 D2                        test rdx, rdx
00AD7A3E  0F 84 B5 00 00 00               je 0x140ad7af9
00AD7A44  83 3B 07                        cmp dword ptr [rbx], 7
00AD7A47  0F 86 AC 00 00 00               jbe 0x140ad7af9
00AD7A4D  44 8B BC 24 B0 00 00 00         mov r15d, dword ptr [rsp + 0xb0]
00AD7A55  48 8B C2                        mov rax, rdx
00AD7A58  45 8B C4                        mov r8d, r12d
00AD7A5B  44 8B 28                        mov r13d, dword ptr [rax]
00AD7A5E  48 8D 48 04                     lea rcx, [rax + 4]
00AD7A62  41 83 F8 07                     cmp r8d, 7
00AD7A66  73 23                           jae 0x140ad7a8b
00AD7A68  48 3B C8                        cmp rcx, rax
00AD7A6B  0F 82 A8 01 00 00               jb 0x140ad7c19
00AD7A71  4A 8D 04 29                     lea rax, [rcx + r13]
00AD7A75  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
00AD7A7D  48 3B C1                        cmp rax, rcx
00AD7A80  0F 82 93 01 00 00               jb 0x140ad7c19
00AD7A86  41 FF C0                        inc r8d
00AD7A89  EB D0                           jmp 0x140ad7a5b
00AD7A8B  48 3B C8                        cmp rcx, rax
00AD7A8E  0F 82 85 01 00 00               jb 0x140ad7c19
00AD7A94  45 85 ED                        test r13d, r13d
00AD7A97  4D 8B DC                        mov r11, r12
00AD7A9A  4C 0F 45 D9                     cmovne r11, rcx
00AD7A9E  83 3B 08                        cmp dword ptr [rbx], 8
00AD7AA1  76 56                           jbe 0x140ad7af9
00AD7AA3  48 8B C2                        mov rax, rdx
00AD7AA6  45 8B C4                        mov r8d, r12d
00AD7AA9  44 8B 20                        mov r12d, dword ptr [rax]
00AD7AAC  48 8D 48 04                     lea rcx, [rax + 4]
00AD7AB0  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00AD7AB5  41 83 F8 08                     cmp r8d, 8
00AD7AB9  73 23                           jae 0x140ad7ade
00AD7ABB  48 3B C8                        cmp rcx, rax
00AD7ABE  0F 82 55 01 00 00               jb 0x140ad7c19
00AD7AC4  4A 8D 04 21                     lea rax, [rcx + r12]
00AD7AC8  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
00AD7AD0  48 3B C1                        cmp rax, rcx
00AD7AD3  0F 82 40 01 00 00               jb 0x140ad7c19
00AD7AD9  41 FF C0                        inc r8d
00AD7ADC  EB CB                           jmp 0x140ad7aa9
00AD7ADE  48 3B C8                        cmp rcx, rax
00AD7AE1  0F 82 32 01 00 00               jb 0x140ad7c19
00AD7AE7  45 33 C0                        xor r8d, r8d
00AD7AEA  45 85 E4                        test r12d, r12d
00AD7AED  41 8B C0                        mov eax, r8d
00AD7AF0  48 0F 45 C1                     cmovne rax, rcx
00AD7AF4  83 3B 09                        cmp dword ptr [rbx], 9
00AD7AF7  77 0A                           ja 0x140ad7b03
00AD7AF9  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD7AFE  E9 1B 01 00 00                  jmp 0x140ad7c1e
00AD7B03  45 8B D0                        mov r10d, r8d
00AD7B06  8B 1A                           mov ebx, dword ptr [rdx]
00AD7B08  48 8D 4A 04                     lea rcx, [rdx + 4]
00AD7B0C  41 83 FA 09                     cmp r10d, 9
00AD7B10  73 28                           jae 0x140ad7b3a
00AD7B12  48 3B CA                        cmp rcx, rdx
00AD7B15  0F 82 FE 00 00 00               jb 0x140ad7c19
00AD7B1B  48 8D 14 19                     lea rdx, [rcx + rbx]
00AD7B1F  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
00AD7B27  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00AD7B2C  48 3B D1                        cmp rdx, rcx
00AD7B2F  0F 82 E4 00 00 00               jb 0x140ad7c19
00AD7B35  41 FF C2                        inc r10d
00AD7B38  EB CC                           jmp 0x140ad7b06
00AD7B3A  48 3B CA                        cmp rcx, rdx
00AD7B3D  0F 82 D6 00 00 00               jb 0x140ad7c19
00AD7B43  45 33 D2                        xor r10d, r10d
00AD7B46  85 DB                           test ebx, ebx
00AD7B48  41 8B D2                        mov edx, r10d
00AD7B4B  4C 8B 15 96 08 50 00            mov r10, qword ptr [rip + 0x500896]
00AD7B52  48 0F 45 D1                     cmovne rdx, rcx
00AD7B56  4D 85 D2                        test r10, r10
00AD7B59  0F 84 D0 01 00 00               je 0x140ad7d2f
00AD7B5F  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00AD7B63  4D 8B CB                        mov r9, r11
00AD7B66  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00AD7B6A  4C 8B C6                        mov r8, rsi
00AD7B6D  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00AD7B72  48 8B D7                        mov rdx, rdi
00AD7B75  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00AD7B79  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
00AD7B80  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AD7B85  49 8B C2                        mov rax, r10
00AD7B88  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00AD7B8D  E8 3E 2F BE FF                  call 0x1406baad0
00AD7B92  8B D8                           mov ebx, eax
00AD7B94  85 C0                           test eax, eax
00AD7B96  0F 88 82 00 00 00               js 0x140ad7c1e
00AD7B9C  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00AD7BA4  8B 50 20                        mov edx, dword ptr [rax + 0x20]
00AD7BA7  8B 40 10                        mov eax, dword ptr [rax + 0x10]
00AD7BAA  83 C0 30                        add eax, 0x30
00AD7BAD  83 F8 30                        cmp eax, 0x30
00AD7BB0  72 67                           jb 0x140ad7c19
00AD7BB2  8D 48 04                        lea ecx, [rax + 4]
00AD7BB5  44 8B EB                        mov r13d, ebx
00AD7BB8  3B C8                           cmp ecx, eax
00AD7BBA  72 5D                           jb 0x140ad7c19
00AD7BBC  8D 04 11                        lea eax, [rcx + rdx]
00AD7BBF  3B C1                           cmp eax, ecx
00AD7BC1  1B DB                           sbb ebx, ebx
00AD7BC3  81 E3 95 00 00 C0               and ebx, 0xc0000095
00AD7BC9  78 53                           js 0x140ad7c1e
00AD7BCB  BA 14 00 00 00                  mov edx, 0x14
00AD7BD0  B9 00 01 00 00                  mov ecx, 0x100
00AD7BD5  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD7BDB  41 89 56 04                     mov dword ptr [r14 + 4], edx
00AD7BDF  E8 0C A5 0A 00                  call 0x140b820f0
00AD7BE4  33 DB                           xor ebx, ebx
00AD7BE6  48 85 C0                        test rax, rax
00AD7BE9  0F 84 2A FE FF FF               je 0x140ad7a19
00AD7BEF  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AD7BF3  41 0F BA ED 1C                  bts r13d, 0x1c
00AD7BF8  41 89 1E                        mov dword ptr [r14], ebx
00AD7BFB  48 8B D0                        mov rdx, rax
00AD7BFE  48 85 C0                        test rax, rax
00AD7C01  75 44                           jne 0x140ad7c47
00AD7C03  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00AD7C07  8D 48 08                        lea ecx, [rax + 8]
00AD7C0A  3B C8                           cmp ecx, eax
00AD7C0C  72 06                           jb 0x140ad7c14
00AD7C0E  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00AD7C12  EB 7F                           jmp 0x140ad7c93
00AD7C14  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00AD7C19  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD7C1E  33 ED                           xor ebp, ebp
00AD7C20  48 85 FF                        test rdi, rdi
00AD7C23  74 0A                           je 0x140ad7c2f
00AD7C25  33 D2                           xor edx, edx
00AD7C27  48 8B CF                        mov rcx, rdi
00AD7C2A  E8 41 AC 0A 00                  call 0x140b82870
00AD7C2F  48 85 F6                        test rsi, rsi
00AD7C32  0F 84 06 01 00 00               je 0x140ad7d3e
00AD7C38  33 D2                           xor edx, edx
00AD7C3A  48 8B CE                        mov rcx, rsi
00AD7C3D  E8 2E AC 0A 00                  call 0x140b82870
00AD7C42  E9 F7 00 00 00                  jmp 0x140ad7d3e
00AD7C47  8B CB                           mov ecx, ebx
00AD7C49  3B CB                           cmp ecx, ebx
00AD7C4B  73 1C                           jae 0x140ad7c69
00AD7C4D  8B 02                           mov eax, dword ptr [rdx]
00AD7C4F  83 C0 04                        add eax, 4
00AD7C52  83 F8 04                        cmp eax, 4
00AD7C55  72 C2                           jb 0x140ad7c19
00AD7C57  44 8B C0                        mov r8d, eax
00AD7C5A  4C 03 C2                        add r8, rdx
00AD7C5D  4C 3B C2                        cmp r8, rdx
00AD7C60  72 B7                           jb 0x140ad7c19
00AD7C62  49 8B D0                        mov rdx, r8
00AD7C65  FF C1                           inc ecx
00AD7C67  EB E0                           jmp 0x140ad7c49
00AD7C69  4C 8D 42 04                     lea r8, [rdx + 4]
00AD7C6D  4C 3B C2                        cmp r8, rdx
00AD7C70  72 A7                           jb 0x140ad7c19
00AD7C72  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD7C76  48 8D 42 08                     lea rax, [rdx + 8]
00AD7C7A  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD7C7E  48 3B C1                        cmp rax, rcx
00AD7C81  76 07                           jbe 0x140ad7c8a
00AD7C83  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD7C88  EB 94                           jmp 0x140ad7c1e
00AD7C8A  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD7C90  45 89 28                        mov dword ptr [r8], r13d
00AD7C93  41 FF 06                        inc dword ptr [r14]
00AD7C96  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AD7C9A  48 85 D2                        test rdx, rdx
00AD7C9D  75 2F                           jne 0x140ad7cce
00AD7C9F  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD7CA3  83 CA FF                        or edx, 0xffffffff
00AD7CA6  8D 41 0C                        lea eax, [rcx + 0xc]
00AD7CA9  3B C1                           cmp eax, ecx
00AD7CAB  0F 43 D0                        cmovae edx, eax
00AD7CAE  1B DB                           sbb ebx, ebx
00AD7CB0  81 E3 95 00 00 C0               and ebx, 0xc0000095
00AD7CB6  41 89 56 04                     mov dword ptr [r14 + 4], edx
00AD7CBA  3B C1                           cmp eax, ecx
00AD7CBC  0F 82 5C FF FF FF               jb 0x140ad7c1e
00AD7CC2  41 FF 06                        inc dword ptr [r14]
00AD7CC5  33 C9                           xor ecx, ecx
00AD7CC7  8B D9                           mov ebx, ecx
00AD7CC9  E9 50 FF FF FF                  jmp 0x140ad7c1e
00AD7CCE  45 8B 0E                        mov r9d, dword ptr [r14]
00AD7CD1  8B CB                           mov ecx, ebx
00AD7CD3  41 3B C9                        cmp ecx, r9d
00AD7CD6  73 24                           jae 0x140ad7cfc
00AD7CD8  8B 02                           mov eax, dword ptr [rdx]
00AD7CDA  83 C0 04                        add eax, 4
00AD7CDD  83 F8 04                        cmp eax, 4
00AD7CE0  0F 82 33 FF FF FF               jb 0x140ad7c19
00AD7CE6  44 8B C0                        mov r8d, eax
00AD7CE9  4C 03 C2                        add r8, rdx
00AD7CEC  4C 3B C2                        cmp r8, rdx
00AD7CEF  0F 82 24 FF FF FF               jb 0x140ad7c19
00AD7CF5  49 8B D0                        mov rdx, r8
00AD7CF8  FF C1                           inc ecx
00AD7CFA  EB D7                           jmp 0x140ad7cd3
00AD7CFC  4C 8D 42 04                     lea r8, [rdx + 4]
00AD7D00  4C 3B C2                        cmp r8, rdx
00AD7D03  0F 82 10 FF FF FF               jb 0x140ad7c19
00AD7D09  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD7D0D  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD7D11  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD7D15  48 3B C1                        cmp rax, rcx
00AD7D18  0F 87 65 FF FF FF               ja 0x140ad7c83
00AD7D1E  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD7D24  49 89 28                        mov qword ptr [r8], rbp
00AD7D27  41 FF 06                        inc dword ptr [r14]
00AD7D2A  E9 EF FE FF FF                  jmp 0x140ad7c1e
00AD7D2F  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AD7D34  E9 E5 FE FF FF                  jmp 0x140ad7c1e
00AD7D39  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD7D3E  8B C3                           mov eax, ebx
00AD7D40  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AD7D48  48 83 C4 60                     add rsp, 0x60
00AD7D4C  41 5F                           pop r15
00AD7D4E  41 5E                           pop r14
00AD7D50  41 5D                           pop r13
00AD7D52  41 5C                           pop r12
00AD7D54  5F                              pop rdi
00AD7D55  5E                              pop rsi
00AD7D56  5D                              pop rbp
00AD7D57  C3                              ret
00AD7D58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD777C(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (96);
    v_rdi = 0;
    if (a2 != 0) goto loc_00AD77B3;
loc_00AD77A9:
    goto loc_00AD7D3E;
loc_00AD77B3:
    if (a4 == 0) goto loc_00AD77A9;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD77A9;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 3) goto loc_00AD77A9;
loc_00AD77CC:
    if (0 >= 3) goto loc_00AD77F4;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD7D39;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD7D39;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD77CC;
loc_00AD77F4:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD7D39;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00AD785D;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 4) goto loc_00AD77A9;
loc_00AD781C:
    if (0 >= 4) goto loc_00AD7844;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD7D39;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD7D39;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD781C;
loc_00AD7844:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD7D39;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_00AD7867;
loc_00AD785D:
    goto loc_00AD7D3E;
loc_00AD7867:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m48 = 0;
    if ((*(unsigned int *)((unsigned int)(0xC0000023ULL))) <= 5) goto loc_00AD77A9;
loc_00AD7883:
    if (0 >= 5) goto loc_00AD78B3;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD7D39;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD7D39;
    a4 = (unsigned int)((0) + 1);
    goto loc_00AD7883;
loc_00AD78B3:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD7D39;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) == 0) goto loc_00AD7901;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00AD7901;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_r15 + result * 2 - 2))) goto loc_00AD7901;
    result = StringCbLengthW(v_r15, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), v_stack_m48, a4);
    if (sign_flag) goto loc_00AD7901;
    if ((v_stack_m48 + 2) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00AD790B;
loc_00AD7901:
    goto loc_00AD7D3E;
loc_00AD790B:
    a1 = (v_stack_m48) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00AD7901;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD7940;
    goto loc_00AD7D3E;
loc_00AD7940:
    result = memcpy(result, v_r15, (unsigned int)((unsigned int)(a1 * 2 + 2)), a4);
    v_r12 = 0;
    v_stack_m48 = 0;
    if (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) == 0) goto loc_00AD7AF9;
    if ((*(unsigned int *)((unsigned int)(0xC0000017ULL))) <= 6) goto loc_00AD7AF9;
loc_00AD796F:
    if (0 >= 6) goto loc_00AD799E;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD7C19;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD7C19;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD796F;
loc_00AD799E:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD7C19;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { v_r15 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) == 0) goto loc_00AD79E7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))) & (1)) != 0) goto loc_00AD79E7;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_r15 + result * 2 - 2))) goto loc_00AD79E7;
    result = StringCbLengthW(v_r15, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))), v_stack_m48, a4);
    if (sign_flag) goto loc_00AD79E7;
    if ((v_stack_m48 + 2) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))) goto loc_00AD79F1;
loc_00AD79E7:
    goto loc_00AD7C1E;
loc_00AD79F1:
    a1 = (v_stack_m48) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00AD79E7;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD7A23;
loc_00AD7A19:
    goto loc_00AD7C1E;
loc_00AD7A23:
    result = memcpy(result, v_r15, (unsigned int)((unsigned int)(a1 * 2 + 2)), a4);
    v_r12 = 0;
    if (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) == 0) goto loc_00AD7AF9;
    if ((*(unsigned int *)((unsigned int)(0xC0000017ULL))) <= 7) goto loc_00AD7AF9;
loc_00AD7A5B:
    if (0 >= 7) goto loc_00AD7A8B;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD7C19;
    v_stack_p18 = (unsigned int)((unsigned int)(v_stack_p18));
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD7C19;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD7A5B;
loc_00AD7A8B:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD7C19;
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { v_r11 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC0000017ULL))) <= 8) goto loc_00AD7AF9;
loc_00AD7AA9:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    if (0 >= 8) goto loc_00AD7ADE;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD7C19;
    v_stack_p18 = (unsigned int)((unsigned int)(v_stack_p18));
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD7C19;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD7AA9;
loc_00AD7ADE:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD7C19;
    a3 = 0;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { result = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC0000017ULL))) > 9) goto loc_00AD7B03;
loc_00AD7AF9:
    goto loc_00AD7C1E;
loc_00AD7B03:
loc_00AD7B06:
    if (0 >= 9) goto loc_00AD7B3A;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD7C19;
    v_stack_p18 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD7C19;
    v_r10 = (unsigned int)((0) + 1);
    goto loc_00AD7B06;
loc_00AD7B3A:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD7C19;
    v_r10 = 0;
    a2 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { a2 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if (*(unsigned __int64 *)(v_rip + 5245078) == 0) goto loc_00AD7D2F;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    v_stack_m60 = a2;
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m48));
    v_stack_m70 = result;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    result = guard_dispatch_icall((unsigned int)(v_stack_p18), result, result, v_r11);
    if (sign_flag) goto loc_00AD7C1E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 16))) + (48));
    if (((unsigned int)(result)) < 48) goto loc_00AD7C19;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD7C19;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00AD7C1E;
    *(unsigned int *)(a4 + 4) = 20;
    result = ExAllocatePool2(256, 20, (unsigned int)(0x20534C53ULL), v_r11);
    v_rbx = 0;
    if (result == 0) goto loc_00AD7A19;
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result != 0) goto loc_00AD7C47;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD7C14;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD7C93;
loc_00AD7C14:
loc_00AD7C19:
loc_00AD7C1E:
    v_rbp = 0;
    result = (unsigned int)(*(unsigned int *)(a4 + 4));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x20534C53ULL), v_r11);
    }
    if (result == 0) goto loc_00AD7D3E;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20534C53ULL), v_r11);
    goto loc_00AD7D3E;
loc_00AD7C47:
loc_00AD7C49:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL))))) >= ((unsigned int)((unsigned int)(0xC0000095ULL)))) goto loc_00AD7C69;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD7C19;
    a3 = ((unsigned int)((unsigned int)(result))) + (0);
    if (a3 < 0) goto loc_00AD7C19;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)))) + 1);
    goto loc_00AD7C49;
loc_00AD7C69:
    if ((a3 + 4) < a3) goto loc_00AD7C19;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) <= a1) goto loc_00AD7C8A;
loc_00AD7C83:
    goto loc_00AD7C1E;
loc_00AD7C8A:
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00AD7C93:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD7CCE;
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    v_rbx = (unsigned int)(((unsigned int)(0xC0000023ULL)) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a2);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD7C1E;
    a1 = 0;
    goto loc_00AD7C1E;
loc_00AD7CCE:
loc_00AD7CD3:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD7CFC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD7C19;
    a3 = ((unsigned int)((unsigned int)(result))) + (a2);
    if (a3 < a2) goto loc_00AD7C19;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD7CD3;
loc_00AD7CFC:
    if ((a3 + 4) < a3) goto loc_00AD7C19;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00AD7C83;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = 0;
    goto loc_00AD7C1E;
loc_00AD7D2F:
    goto loc_00AD7C1E;
loc_00AD7D39:
loc_00AD7D3E:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD777C(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (96);
    local_rdi = 0;
    if (Arg2 != 0) goto loc_00AD77B3;
loc_00AD77A9:
    goto loc_00AD7D3E;
loc_00AD77B3:
    if (Arg4 == 0) goto loc_00AD77A9;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD77A9;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 3) goto loc_00AD77A9;
loc_00AD77CC:
    if (0 >= 3) goto loc_00AD77F4;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD7D39;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD7D39;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD77CC;
loc_00AD77F4:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD7D39;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00AD785D;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 4) goto loc_00AD77A9;
loc_00AD781C:
    if (0 >= 4) goto loc_00AD7844;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD7D39;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD7D39;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD781C;
loc_00AD7844:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD7D39;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_00AD7867;
loc_00AD785D:
    goto loc_00AD7D3E;
loc_00AD7867:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m48 = 0;
    if ((*(uint32_t *)((uint32_t)(0xC0000023ULL))) <= 5) goto loc_00AD77A9;
loc_00AD7883:
    if (0 >= 5) goto loc_00AD78B3;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD7D39;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD7D39;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00AD7883;
loc_00AD78B3:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD7D39;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) == 0) goto loc_00AD7901;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00AD7901;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_r15 + result * 2 - 0x2))) goto loc_00AD7901;
    result = StringCbLengthW(local_r15, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), v_stack_m48, Arg4);
    if (sign_flag) goto loc_00AD7901;
    if ((v_stack_m48 + 2) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00AD790B;
loc_00AD7901:
    goto loc_00AD7D3E;
loc_00AD790B:
    Arg1 = (v_stack_m48) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00AD7901;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD7940;
    goto loc_00AD7D3E;
loc_00AD7940:
    result = memcpy(result, local_r15, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), Arg4);
    local_r12 = 0;
    v_stack_m48 = 0;
    if (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) == 0) goto loc_00AD7AF9;
    if ((*(uint32_t *)((uint32_t)(0xC0000017ULL))) <= 6) goto loc_00AD7AF9;
loc_00AD796F:
    if (0 >= 6) goto loc_00AD799E;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD7C19;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD7C19;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD796F;
loc_00AD799E:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD7C19;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { local_r15 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) == 0) goto loc_00AD79E7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))) & (1)) != 0) goto loc_00AD79E7;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_r15 + result * 2 - 0x2))) goto loc_00AD79E7;
    result = StringCbLengthW(local_r15, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))), v_stack_m48, Arg4);
    if (sign_flag) goto loc_00AD79E7;
    if ((v_stack_m48 + 2) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))) goto loc_00AD79F1;
loc_00AD79E7:
    goto loc_00AD7C1E;
loc_00AD79F1:
    Arg1 = (v_stack_m48) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00AD79E7;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD7A23;
loc_00AD7A19:
    goto loc_00AD7C1E;
loc_00AD7A23:
    result = memcpy(result, local_r15, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), Arg4);
    local_r12 = 0;
    if (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) == 0) goto loc_00AD7AF9;
    if ((*(uint32_t *)((uint32_t)(0xC0000017ULL))) <= 7) goto loc_00AD7AF9;
loc_00AD7A5B:
    if (0 >= 7) goto loc_00AD7A8B;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD7C19;
    v_stack_p18 = (uint32_t)((uint32_t)(v_stack_p18));
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD7C19;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD7A5B;
loc_00AD7A8B:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD7C19;
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { local_r11 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC0000017ULL))) <= 8) goto loc_00AD7AF9;
loc_00AD7AA9:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    if (0 >= 8) goto loc_00AD7ADE;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD7C19;
    v_stack_p18 = (uint32_t)((uint32_t)(v_stack_p18));
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD7C19;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD7AA9;
loc_00AD7ADE:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD7C19;
    Arg3 = 0;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { result = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC0000017ULL))) > 9) goto loc_00AD7B03;
loc_00AD7AF9:
    goto loc_00AD7C1E;
loc_00AD7B03:
loc_00AD7B06:
    if (0 >= 9) goto loc_00AD7B3A;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD7C19;
    v_stack_p18 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD7C19;
    local_r10 = (uint32_t)((0) + 1);
    goto loc_00AD7B06;
loc_00AD7B3A:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD7C19;
    local_r10 = 0;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { Arg2 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if (*(uint64_t *)(v_rip + 0x500896) == 0) goto loc_00AD7D2F;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    v_stack_m60 = Arg2;
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m48));
    v_stack_m70 = result;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    result = guard_dispatch_icall((uint32_t)(v_stack_p18), result, result, local_r11);
    if (sign_flag) goto loc_00AD7C1E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10))) + (48));
    if (((uint32_t)(result)) < 48) goto loc_00AD7C19;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD7C19;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00AD7C1E;
    *(uint32_t *)(Arg4 + 0x4) = 20;
    result = ExAllocatePool2(256, 20, (uint32_t)(0x20534C53ULL), local_r11);
    local_rbx = 0;
    if (result == 0) goto loc_00AD7A19;
    *(uint64_t *)(Arg4 + 0x8) = result;
    *(uint32_t *)(Arg4) = 0;
    if (result != 0) goto loc_00AD7C47;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD7C14;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD7C93;
loc_00AD7C14:
loc_00AD7C19:
loc_00AD7C1E:
    local_rbp = 0;
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x4));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x20534C53ULL), local_r11);
    }
    if (result == 0) goto loc_00AD7D3E;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20534C53ULL), local_r11);
    goto loc_00AD7D3E;
loc_00AD7C47:
loc_00AD7C49:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL))))) >= ((uint32_t)((uint32_t)(0xC0000095ULL)))) goto loc_00AD7C69;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD7C19;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (0);
    if (Arg3 < 0) goto loc_00AD7C19;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)))) + 1);
    goto loc_00AD7C49;
loc_00AD7C69:
    if ((Arg3 + 4) < Arg3) goto loc_00AD7C19;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) <= Arg1) goto loc_00AD7C8A;
loc_00AD7C83:
    goto loc_00AD7C1E;
loc_00AD7C8A:
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00AD7C93:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD7CCE;
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    local_rbx = (uint32_t)(((uint32_t)(0xC0000023ULL)) & (0xC0000095ULL));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg2);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD7C1E;
    Arg1 = 0;
    goto loc_00AD7C1E;
loc_00AD7CCE:
loc_00AD7CD3:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD7CFC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD7C19;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (Arg2);
    if (Arg3 < Arg2) goto loc_00AD7C19;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD7CD3;
loc_00AD7CFC:
    if ((Arg3 + 4) < Arg3) goto loc_00AD7C19;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00AD7C83;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = 0;
    goto loc_00AD7C1E;
loc_00AD7D2F:
    goto loc_00AD7C1E;
loc_00AD7D39:
loc_00AD7D3E:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD777C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
