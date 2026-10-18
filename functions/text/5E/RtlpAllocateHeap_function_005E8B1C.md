# RtlpAllocateHeap

- RVA: `0x005E8B1C`–`0x005E949E` (길이 `2,434` bytes)
- VA: `0x00000001405E8B1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFB88`
- 디코드: `582`개 명령, `2,434/2,434` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005E8C8D` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (function, `0x00ACE530`)
- `0x005E8CB3` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x005E8CEF` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005E8D41` → [RtlpAnalyzeHeapFailure](../5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (function, `0x005F0F9C`)
- `0x005E8DD1` → [RtlpHeapRemoveListEntry](../5F/RtlpHeapRemoveListEntry_function_005F1B90.md) (function, `0x005F1B90`)
- `0x005E8E10` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E8E4A` → [RtlpExtendHeap](RtlpExtendHeap_function_005EA708.md) (function, `0x005EA708`)
- `0x005E8EDB` → [RtlpHeapRemoveListEntry](../5F/RtlpHeapRemoveListEntry_function_005F1B90.md) (function, `0x005F1B90`)
- `0x005E8F12` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E8F7F` → [RtlCompareMemoryUlong](../6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x005E8F9A` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005E8FDD` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E90B9` → [RtlpCreateSplitBlock](RtlpCreateSplitBlock_function_005E98F0.md) (function, `0x005E98F0`)
- `0x005E9140` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x005E9169` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E9186` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E92E8` → [RtlpHpHeapCheckCommitLimit](../45/RtlpHpHeapCheckCommitLimit_function_0045820C.md) (function, `0x0045820C`)
- `0x005E9384` → [RtlpHpAllocVirtBlockCommitFirst](RtlpHpAllocVirtBlockCommitFirst_function_005EB0FC.md) (function, `0x005EB0FC`)
- `0x005E945C` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005E9491` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- [sub_006DE680](../6D/Unknown_function_006DE680.md) at `0x006DE792`

### Static image references
- `0x005E8F93` → RVA `0x006CC9E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005E8F9F` → RVA `0x00F475F8` (`.data`; read)
- `0x005E921D` → RVA `0x00042F00` (`.rdata`; read)
- `0x005E930E` → RVA `0x00E28340` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005E8C8D` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E8B1C  4C 8B DC                        mov r11, rsp
005E8B1F  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
005E8B23  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
005E8B27  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
005E8B2B  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
005E8B2F  53                              push rbx
005E8B30  56                              push rsi
005E8B31  57                              push rdi
005E8B32  41 54                           push r12
005E8B34  41 55                           push r13
005E8B36  41 56                           push r14
005E8B38  41 57                           push r15
005E8B3A  48 81 EC F0 00 00 00            sub rsp, 0xf0
005E8B41  4D 8B F9                        mov r15, r9
005E8B44  44 8B E2                        mov r12d, edx
005E8B47  48 8B F1                        mov rsi, rcx
005E8B4A  33 C9                           xor ecx, ecx
005E8B4C  49 89 4B 98                     mov qword ptr [r11 - 0x68], rcx
005E8B50  49 89 8B 68 FF FF FF            mov qword ptr [r11 - 0x98], rcx
005E8B57  49 89 8B 78 FF FF FF            mov qword ptr [r11 - 0x88], rcx
005E8B5E  8D 51 01                        lea edx, [rcx + 1]
005E8B61  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
005E8B65  49 89 8B 58 FF FF FF            mov qword ptr [r11 - 0xa8], rcx
005E8B6C  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
005E8B70  49 89 4B 88                     mov qword ptr [r11 - 0x78], rcx
005E8B74  49 89 4B A0                     mov qword ptr [r11 - 0x60], rcx
005E8B78  41 88 4B 28                     mov byte ptr [r11 + 0x28], cl
005E8B7C  88 4C 24 40                     mov byte ptr [rsp + 0x40], cl
005E8B80  49 89 4B 90                     mov qword ptr [r11 - 0x70], rcx
005E8B84  44 8B F1                        mov r14d, ecx
005E8B87  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
005E8B8C  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005E8B90  49 89 4B B8                     mov qword ptr [r11 - 0x48], rcx
005E8B94  49 89 4B 80                     mov qword ptr [r11 - 0x80], rcx
005E8B98  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
005E8B9C  49 89 4B B0                     mov qword ptr [r11 - 0x50], rcx
005E8BA0  41 F7 C4 60 0F 01 3C            test r12d, 0x3c010f60
005E8BA7  75 3C                           jne 0x1405e8be5
005E8BA9  B8 00 00 00 80                  mov eax, 0x80000000
005E8BAE  4C 3B C0                        cmp r8, rax
005E8BB1  73 32                           jae 0x1405e8be5
005E8BB3  8A DA                           mov bl, dl
005E8BB5  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
005E8BB9  4D 8B E9                        mov r13, r9
005E8BBC  49 C1 ED 04                     shr r13, 4
005E8BC0  49 83 FD 02                     cmp r13, 2
005E8BC4  73 0C                           jae 0x1405e8bd2
005E8BC6  49 83 C7 10                     add r15, 0x10
005E8BCA  4D 89 7B 20                     mov qword ptr [r11 + 0x20], r15
005E8BCE  44 8D 69 02                     lea r13d, [rcx + 2]
005E8BD2  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
005E8BDA  C7 00 03 00 00 00               mov dword ptr [rax], 3
005E8BE0  E9 A1 00 00 00                  jmp 0x1405e8c86
005E8BE5  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
005E8BE9  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
005E8BF1  C7 00 04 00 00 00               mov dword ptr [rax], 4
005E8BF7  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
005E8C01  4C 3B C0                        cmp r8, rax
005E8C04  76 16                           jbe 0x1405e8c1c
005E8C06  33 C0                           xor eax, eax
005E8C08  48 81 C4 F0 00 00 00            add rsp, 0xf0
005E8C0F  41 5F                           pop r15
005E8C11  41 5E                           pop r14
005E8C13  41 5D                           pop r13
005E8C15  41 5C                           pop r12
005E8C17  5F                              pop rdi
005E8C18  5E                              pop rsi
005E8C19  5B                              pop rbx
005E8C1A  C3                              ret
005E8C1B  CC                              int3
005E8C1C  4D 8B F8                        mov r15, r8
005E8C1F  4D 85 C0                        test r8, r8
005E8C22  4C 0F 44 FA                     cmove r15, rdx
005E8C26  4C 03 BE 00 01 00 00            add r15, qword ptr [rsi + 0x100]
005E8C2D  4C 23 BE 08 01 00 00            and r15, qword ptr [rsi + 0x108]
005E8C34  B8 20 00 00 00                  mov eax, 0x20
005E8C39  4C 3B F8                        cmp r15, rax
005E8C3C  4C 0F 42 F8                     cmovb r15, rax
005E8C40  4C 89 BC 24 48 01 00 00         mov qword ptr [rsp + 0x148], r15
005E8C48  41 8B DC                        mov ebx, r12d
005E8C4B  C1 EB 04                        shr ebx, 4
005E8C4E  80 E3 E1                        and bl, 0xe1
005E8C51  0A DA                           or bl, dl
005E8C53  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
005E8C57  41 F7 C4 00 01 00 3C            test r12d, 0x3c000100
005E8C5E  75 0C                           jne 0x1405e8c6c
005E8C60  4D 8B EF                        mov r13, r15
005E8C63  48 39 8E 48 01 00 00            cmp qword ptr [rsi + 0x148], rcx
005E8C6A  74 16                           je 0x1405e8c82
005E8C6C  80 CB 02                        or bl, 2
005E8C6F  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
005E8C73  4D 8D 6F 10                     lea r13, [r15 + 0x10]
005E8C77  4D 8B FD                        mov r15, r13
005E8C7A  4C 89 AC 24 48 01 00 00         mov qword ptr [rsp + 0x148], r13
005E8C82  49 C1 ED 04                     shr r13, 4
005E8C86  41 0F BA E4 17                  bt r12d, 0x17
005E8C8B  73 12                           jae 0x1405e8c9f
005E8C8D  E8 9E 58 4E 00                  call 0x140ace530
005E8C92  0F BA E0 0B                     bt eax, 0xb
005E8C96  72 07                           jb 0x1405e8c9f
005E8C98  80 CB 08                        or bl, 8
005E8C9B  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
005E8C9F  BF 01 00 00 00                  mov edi, 1
005E8CA4  44 84 E7                        test dil, r12b
005E8CA7  75 22                           jne 0x1405e8ccb
005E8CA9  40 8A D7                        mov dl, dil
005E8CAC  48 8B 8E 60 01 00 00            mov rcx, qword ptr [rsi + 0x160]
005E8CB3  E8 68 C1 C2 FF                  call 0x140214e20
005E8CB8  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
005E8CBD  40 8A C7                        mov al, dil
005E8CC0  88 84 24 50 01 00 00            mov byte ptr [rsp + 0x150], al
005E8CC7  88 44 24 40                     mov byte ptr [rsp + 0x40], al
005E8CCB  8B 86 94 00 00 00               mov eax, dword ptr [rsi + 0x94]
005E8CD1  4C 3B E8                        cmp r13, rax
005E8CD4  0F 87 C5 05 00 00               ja 0x1405e929f
005E8CDA  48 8D BE 50 01 00 00            lea rdi, [rsi + 0x150]
005E8CE1  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
005E8CE9  49 8B D5                        mov rdx, r13
005E8CEC  48 8B CE                        mov rcx, rsi
005E8CEF  E8 C0 8A 00 00                  call 0x1405f17b4
005E8CF4  4C 8B E0                        mov r12, rax
005E8CF7  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
005E8CFF  48 3B F8                        cmp rdi, rax
005E8D02  0F 84 3C 01 00 00               je 0x1405e8e44
005E8D08  48 8D 58 F0                     lea rbx, [rax - 0x10]
005E8D0C  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
005E8D14  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E8D18  74 2C                           je 0x1405e8d46
005E8D1A  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
005E8D20  41 31 44 24 F8                  xor dword ptr [r12 - 8], eax
005E8D25  41 8A 4C 24 FA                  mov cl, byte ptr [r12 - 6]
005E8D2A  41 32 4C 24 F9                  xor cl, byte ptr [r12 - 7]
005E8D2F  41 32 4C 24 F8                  xor cl, byte ptr [r12 - 8]
005E8D34  41 38 4C 24 FB                  cmp byte ptr [r12 - 5], cl
005E8D39  74 0B                           je 0x1405e8d46
005E8D3B  48 8B D3                        mov rdx, rbx
005E8D3E  48 8B CE                        mov rcx, rsi
005E8D41  E8 56 82 00 00                  call 0x1405f0f9c
005E8D46  41 0F B7 4C 24 F8               movzx ecx, word ptr [r12 - 8]
005E8D4C  49 3B CD                        cmp rcx, r13
005E8D4F  0F 82 CA 00 00 00               jb 0x1405e8e1f
005E8D55  49 8B 3C 24                     mov rdi, qword ptr [r12]
005E8D59  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
005E8D5E  4D 8B 44 24 08                  mov r8, qword ptr [r12 + 8]
005E8D63  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
005E8D68  49 8B 00                        mov rax, qword ptr [r8]
005E8D6B  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
005E8D6F  49 3B C1                        cmp rax, r9
005E8D72  0F 85 82 00 00 00               jne 0x1405e8dfa
005E8D78  49 3B C4                        cmp rax, r12
005E8D7B  75 7D                           jne 0x1405e8dfa
005E8D7D  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
005E8D84  48 2B C1                        sub rax, rcx
005E8D87  48 89 86 C0 00 00 00            mov qword ptr [rsi + 0xc0], rax
005E8D8E  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E8D95  48 85 D2                        test rdx, rdx
005E8D98  74 46                           je 0x1405e8de0
005E8D9A  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
005E8DA0  41 0F B7 4C 24 F8               movzx ecx, word ptr [r12 - 8]
005E8DA6  8B 7A 08                        mov edi, dword ptr [rdx + 8]
005E8DA9  48 3B CF                        cmp rcx, rdi
005E8DAC  72 0B                           jb 0x1405e8db9
005E8DAE  48 8B 02                        mov rax, qword ptr [rdx]
005E8DB1  48 85 C0                        test rax, rax
005E8DB4  75 3F                           jne 0x1405e8df5
005E8DB6  8D 4F FF                        lea ecx, [rdi - 1]
005E8DB9  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
005E8DBE  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E8DC2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E8DC7  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005E8DCB  4D 8B CC                        mov r9, r12
005E8DCE  48 8B CE                        mov rcx, rsi
005E8DD1  E8 BA 8D 00 00                  call 0x1405f1b90
005E8DD6  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
005E8DDB  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005E8DE0  49 89 38                        mov qword ptr [r8], rdi
005E8DE3  4C 89 47 08                     mov qword ptr [rdi + 8], r8
005E8DE7  B9 01 00 00 00                  mov ecx, 1
005E8DEC  88 4C 24 42                     mov byte ptr [rsp + 0x42], cl
005E8DF0  E9 01 01 00 00                  jmp 0x1405e8ef6
005E8DF5  48 8B D0                        mov rdx, rax
005E8DF8  EB AC                           jmp 0x1405e8da6
005E8DFA  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E8E00  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005E8E05  4D 8B C4                        mov r8, r12
005E8E08  48 8B D6                        mov rdx, rsi
005E8E0B  B9 0D 00 00 00                  mov ecx, 0xd
005E8E10  E8 A7 29 D7 FF                  call 0x14035b7bc
005E8E15  C6 44 24 42 00                  mov byte ptr [rsp + 0x42], 0
005E8E1A  E9 FD 00 00 00                  jmp 0x1405e8f1c
005E8E1F  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E8E23  74 1F                           je 0x1405e8e44
005E8E25  41 8A 4C 24 FA                  mov cl, byte ptr [r12 - 6]
005E8E2A  41 32 4C 24 F9                  xor cl, byte ptr [r12 - 7]
005E8E2F  41 32 4C 24 F8                  xor cl, byte ptr [r12 - 8]
005E8E34  41 88 4C 24 FB                  mov byte ptr [r12 - 5], cl
005E8E39  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
005E8E3F  41 31 44 24 F8                  xor dword ptr [r12 - 8], eax
005E8E44  49 8B D7                        mov rdx, r15
005E8E47  48 8B CE                        mov rcx, rsi
005E8E4A  E8 B9 18 00 00                  call 0x1405ea708
005E8E4F  48 8B D8                        mov rbx, rax
005E8E52  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
005E8E5A  48 85 C0                        test rax, rax
005E8E5D  0F 84 2F 04 00 00               je 0x1405e9292
005E8E63  4C 8D 40 10                     lea r8, [rax + 0x10]
005E8E67  4D 8B 20                        mov r12, qword ptr [r8]
005E8E6A  48 8B 78 18                     mov rdi, qword ptr [rax + 0x18]
005E8E6E  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
005E8E73  48 8B 07                        mov rax, qword ptr [rdi]
005E8E76  4D 8B 4C 24 08                  mov r9, qword ptr [r12 + 8]
005E8E7B  49 3B C1                        cmp rax, r9
005E8E7E  75 7F                           jne 0x1405e8eff
005E8E80  49 3B C0                        cmp rax, r8
005E8E83  75 7A                           jne 0x1405e8eff
005E8E85  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E8E89  48 8B 8E C0 00 00 00            mov rcx, qword ptr [rsi + 0xc0]
005E8E90  48 2B C8                        sub rcx, rax
005E8E93  48 89 8E C0 00 00 00            mov qword ptr [rsi + 0xc0], rcx
005E8E9A  48 8B 96 38 01 00 00            mov rdx, qword ptr [rsi + 0x138]
005E8EA1  48 85 D2                        test rdx, rdx
005E8EA4  74 3F                           je 0x1405e8ee5
005E8EA6  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
005E8EAC  0F B7 4B 08                     movzx ecx, word ptr [rbx + 8]
005E8EB0  8B 7A 08                        mov edi, dword ptr [rdx + 8]
005E8EB3  48 3B CF                        cmp rcx, rdi
005E8EB6  72 0B                           jb 0x1405e8ec3
005E8EB8  48 8B 02                        mov rax, qword ptr [rdx]
005E8EBB  48 85 C0                        test rax, rax
005E8EBE  75 3A                           jne 0x1405e8efa
005E8EC0  8D 4F FF                        lea ecx, [rdi - 1]
005E8EC3  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
005E8EC8  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E8ECC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E8ED1  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005E8ED5  4D 8B C8                        mov r9, r8
005E8ED8  48 8B CE                        mov rcx, rsi
005E8EDB  E8 B0 8C 00 00                  call 0x1405f1b90
005E8EE0  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005E8EE5  4C 89 27                        mov qword ptr [rdi], r12
005E8EE8  49 89 7C 24 08                  mov qword ptr [r12 + 8], rdi
005E8EED  B9 01 00 00 00                  mov ecx, 1
005E8EF2  88 4C 24 43                     mov byte ptr [rsp + 0x43], cl
005E8EF6  8A C1                           mov al, cl
005E8EF8  EB 24                           jmp 0x1405e8f1e
005E8EFA  48 8B D0                        mov rdx, rax
005E8EFD  EB B1                           jmp 0x1405e8eb0
005E8EFF  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E8F05  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005E8F0A  48 8B D6                        mov rdx, rsi
005E8F0D  B9 0D 00 00 00                  mov ecx, 0xd
005E8F12  E8 A5 28 D7 FF                  call 0x14035b7bc
005E8F17  C6 44 24 43 00                  mov byte ptr [rsp + 0x43], 0
005E8F1C  32 C0                           xor al, al
005E8F1E  84 C0                           test al, al
005E8F20  0F 84 59 05 00 00               je 0x1405e947f
005E8F26  44 8A 63 0A                     mov r12b, byte ptr [rbx + 0xa]
005E8F2A  44 88 64 24 41                  mov byte ptr [rsp + 0x41], r12b
005E8F2F  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
005E8F33  85 FF                           test edi, edi
005E8F35  75 77                           jne 0x1405e8fae
005E8F37  41 F6 C4 04                     test r12b, 4
005E8F3B  74 71                           je 0x1405e8fae
005E8F3D  48 83 A4 24 88 00 00 00 00      and qword ptr [rsp + 0x88], 0
005E8F46  0F B7 7B 08                     movzx edi, word ptr [rbx + 8]
005E8F4A  48 C1 E7 04                     shl rdi, 4
005E8F4E  48 83 EF 20                     sub rdi, 0x20
005E8F52  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
005E8F5A  41 F6 C4 02                     test r12b, 2
005E8F5E  74 12                           je 0x1405e8f72
005E8F60  48 83 FF 04                     cmp rdi, 4
005E8F64  76 0C                           jbe 0x1405e8f72
005E8F66  48 83 EF 04                     sub rdi, 4
005E8F6A  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
005E8F72  48 8D 4B 20                     lea rcx, [rbx + 0x20]
005E8F76  41 B8 EE FE EE FE               mov r8d, 0xfeeefeee
005E8F7C  48 8B D7                        mov rdx, rdi
005E8F7F  E8 6C 17 0D 00                  call 0x1406ba6f0
005E8F84  48 3B C7                        cmp rax, rdi
005E8F87  74 21                           je 0x1405e8faa
005E8F89  4C 8D 40 20                     lea r8, [rax + 0x20]
005E8F8D  4C 03 C3                        add r8, rbx
005E8F90  48 8B D3                        mov rdx, rbx
005E8F93  48 8D 0D 46 3A 0E 00            lea rcx, [rip + 0xe3a46]
005E8F9A  E8 11 FD D6 FF                  call 0x140358cb0
005E8F9F  8A 05 53 E6 95 00               mov al, byte ptr [rip + 0x95e653]
005E8FA5  84 C0                           test al, al
005E8FA7  74 01                           je 0x1405e8faa
005E8FA9  CC                              int3
005E8FAA  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
005E8FAE  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
005E8FB6  8A 43 0A                        mov al, byte ptr [rbx + 0xa]
005E8FB9  41 BA 01 00 00 00               mov r10d, 1
005E8FBF  41 84 C2                        test r10b, al
005E8FC2  74 23                           je 0x1405e8fe7
005E8FC4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E8FCA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005E8FD0  45 33 C9                        xor r9d, r9d
005E8FD3  4C 8B C3                        mov r8, rbx
005E8FD6  48 8B D6                        mov rdx, rsi
005E8FD9  41 8D 4A 02                     lea ecx, [r10 + 2]
005E8FDD  E8 DA 27 D7 FF                  call 0x14035b7bc
005E8FE2  E9 98 04 00 00                  jmp 0x1405e947f
005E8FE7  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
005E8FEB  88 43 0A                        mov byte ptr [rbx + 0xa], al
005E8FEE  44 0F B7 4B 08                  movzx r9d, word ptr [rbx + 8]
005E8FF3  4D 2B CD                        sub r9, r13
005E8FF6  4C 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r9
005E8FFE  66 44 89 6B 08                  mov word ptr [rbx + 8], r13w
005E9003  49 8B C7                        mov rax, r15
005E9006  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
005E900E  48 2B C2                        sub rax, rdx
005E9011  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005E9016  49 8B CD                        mov rcx, r13
005E9019  48 C1 E1 04                     shl rcx, 4
005E901D  48 83 F8 3F                     cmp rax, 0x3f
005E9021  73 05                           jae 0x1405e9028
005E9023  88 43 0F                        mov byte ptr [rbx + 0xf], al
005E9026  EB 08                           jmp 0x1405e9030
005E9028  48 89 04 19                     mov qword ptr [rcx + rbx], rax
005E902C  C6 43 0F 3F                     mov byte ptr [rbx + 0xf], 0x3f
005E9030  C6 43 0B 00                     mov byte ptr [rbx + 0xb], 0
005E9034  4D 85 C9                        test r9, r9
005E9037  0F 84 9C 00 00 00               je 0x1405e90d9
005E903D  4D 3B CA                        cmp r9, r10
005E9040  75 32                           jne 0x1405e9074
005E9042  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9046  66 41 03 C2                     add ax, r10w
005E904A  66 89 43 08                     mov word ptr [rbx + 8], ax
005E904E  4C 2B FA                        sub r15, rdx
005E9051  49 83 C7 10                     add r15, 0x10
005E9055  4C 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r15
005E905D  49 83 FF 3F                     cmp r15, 0x3f
005E9061  73 06                           jae 0x1405e9069
005E9063  44 88 7B 0F                     mov byte ptr [rbx + 0xf], r15b
005E9067  EB 70                           jmp 0x1405e90d9
005E9069  4C 89 7C 19 10                  mov qword ptr [rcx + rbx + 0x10], r15
005E906E  C6 43 0F 3F                     mov byte ptr [rbx + 0xf], 0x3f
005E9072  EB 65                           jmp 0x1405e90d9
005E9074  41 33 FA                        xor edi, r10d
005E9077  0F B6 43 0E                     movzx eax, byte ptr [rbx + 0xe]
005E907B  84 C0                           test al, al
005E907D  74 18                           je 0x1405e9097
005E907F  49 8B D2                        mov rdx, r10
005E9082  48 2B D0                        sub rdx, rax
005E9085  48 C1 E2 10                     shl rdx, 0x10
005E9089  48 8B C3                        mov rax, rbx
005E908C  48 25 00 00 FF FF               and rax, 0xffffffffffff0000
005E9092  48 03 D0                        add rdx, rax
005E9095  EB 03                           jmp 0x1405e909a
005E9097  48 8B D6                        mov rdx, rsi
005E909A  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
005E909F  4C 8D 04 19                     lea r8, [rcx + rbx]
005E90A3  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
005E90A8  66 44 89 6C 24 28               mov word ptr [rsp + 0x28], r13w
005E90AE  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
005E90B3  45 8A CC                        mov r9b, r12b
005E90B6  48 8B CE                        mov rcx, rsi
005E90B9  E8 32 08 00 00                  call 0x1405e98f0
005E90BE  84 C0                           test al, al
005E90C0  0F 84 B9 03 00 00               je 0x1405e947f
005E90C6  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
005E90CB  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
005E90D3  41 BA 01 00 00 00               mov r10d, 1
005E90D9  4C 8D 73 10                     lea r14, [rbx + 0x10]
005E90DD  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005E90E2  0F B7 7B 08                     movzx edi, word ptr [rbx + 8]
005E90E6  48 C1 E7 04                     shl rdi, 4
005E90EA  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
005E90F2  4C 8B C7                        mov r8, rdi
005E90F5  8A 43 0F                        mov al, byte ptr [rbx + 0xf]
005E90F8  24 3F                           and al, 0x3f
005E90FA  3C 3F                           cmp al, 0x3f
005E90FC  75 0F                           jne 0x1405e910d
005E90FE  4C 8D 47 F8                     lea r8, [rdi - 8]
005E9102  49 8B F8                        mov rdi, r8
005E9105  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
005E910D  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
005E9112  74 5F                           je 0x1405e9173
005E9114  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E9118  74 15                           je 0x1405e912f
005E911A  8A 4B 0A                        mov cl, byte ptr [rbx + 0xa]
005E911D  32 4B 09                        xor cl, byte ptr [rbx + 9]
005E9120  32 4B 08                        xor cl, byte ptr [rbx + 8]
005E9123  88 4B 0B                        mov byte ptr [rbx + 0xb], cl
005E9126  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
005E912C  31 43 08                        xor dword ptr [rbx + 8], eax
005E912F  80 BC 24 50 01 00 00 00         cmp byte ptr [rsp + 0x150], 0
005E9137  74 19                           je 0x1405e9152
005E9139  48 8B 8E 60 01 00 00            mov rcx, qword ptr [rsi + 0x160]
005E9140  E8 CB 68 C7 FF                  call 0x14025fa10
005E9145  32 C0                           xor al, al
005E9147  88 84 24 50 01 00 00            mov byte ptr [rsp + 0x150], al
005E914E  88 44 24 40                     mov byte ptr [rsp + 0x40], al
005E9152  F6 84 24 38 01 00 00 08         test byte ptr [rsp + 0x138], 8
005E915A  0F 84 1F 03 00 00               je 0x1405e947f
005E9160  4C 8D 47 F8                     lea r8, [rdi - 8]
005E9164  33 D2                           xor edx, edx
005E9166  49 8B CE                        mov rcx, r14
005E9169  E8 D2 DA 0D 00                  call 0x1406c6c40
005E916E  E9 0C 03 00 00                  jmp 0x1405e947f
005E9173  F6 84 24 38 01 00 00 08         test byte ptr [rsp + 0x138], 8
005E917B  74 17                           je 0x1405e9194
005E917D  49 83 C0 F8                     add r8, -8
005E9181  33 D2                           xor edx, edx
005E9183  49 8B CE                        mov rcx, r14
005E9186  E8 B5 DA 0D 00                  call 0x1406c6c40
005E918B  48 8D 4E 70                     lea rcx, [rsi + 0x70]
005E918F  E9 83 00 00 00                  jmp 0x1405e9217
005E9194  4C 8D 46 70                     lea r8, [rsi + 0x70]
005E9198  49 8B C8                        mov rcx, r8
005E919B  41 8B 00                        mov eax, dword ptr [r8]
005E919E  A8 40                           test al, 0x40
005E91A0  74 75                           je 0x1405e9217
005E91A2  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
005E91A6  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
005E91AE  4D 8B CE                        mov r9, r14
005E91B1  4C 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r14
005E91B9  48 C1 EA 02                     shr rdx, 2
005E91BD  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
005E91C5  48 85 D2                        test rdx, rdx
005E91C8  74 4D                           je 0x1405e9217
005E91CA  41 F6 C6 04                     test r14b, 4
005E91CE  74 20                           je 0x1405e91f0
005E91D0  41 C7 06 0D F0 AD BA            mov dword ptr [r14], 0xbaadf00d
005E91D7  49 2B D2                        sub rdx, r10
005E91DA  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
005E91E2  74 33                           je 0x1405e9217
005E91E4  4D 8D 4E 04                     lea r9, [r14 + 4]
005E91E8  4C 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r9
005E91F0  48 8B CA                        mov rcx, rdx
005E91F3  48 D1 E9                        shr rcx, 1
005E91F6  48 B8 0D F0 AD BA 0D F0 AD BA   movabs rax, 0xbaadf00dbaadf00d
005E9200  49 8B F9                        mov rdi, r9
005E9203  F3 48 AB                        rep stosq qword ptr [rdi], rax
005E9206  49 8B C8                        mov rcx, r8
005E9209  41 84 D2                        test r10b, dl
005E920C  74 09                           je 0x1405e9217
005E920E  41 C7 44 91 FC 0D F0 AD BA      mov dword ptr [r9 + rdx*4 - 4], 0xbaadf00d
005E9217  8B 01                           mov eax, dword ptr [rcx]
005E9219  A8 20                           test al, 0x20
005E921B  74 1D                           je 0x1405e923a
005E921D  66 0F 6F 05 DB 9C A5 FF         movdqa xmm0, xmmword ptr [rip - 0x5a6325]
005E9225  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
005E922D  41 0F 11 04 16                  movups xmmword ptr [r14 + rdx], xmm0
005E9232  8A 43 0A                        mov al, byte ptr [rbx + 0xa]
005E9235  0C 04                           or al, 4
005E9237  88 43 0A                        mov byte ptr [rbx + 0xa], al
005E923A  C6 43 0B 00                     mov byte ptr [rbx + 0xb], 0
005E923E  8A 43 0A                        mov al, byte ptr [rbx + 0xa]
005E9241  A8 02                           test al, 2
005E9243  74 29                           je 0x1405e926e
005E9245  80 7B 0F 04                     cmp byte ptr [rbx + 0xf], 4
005E9249  75 06                           jne 0x1405e9251
005E924B  48 8D 43 E0                     lea rax, [rbx - 0x20]
005E924F  EB 0F                           jmp 0x1405e9260
005E9251  0F B7 43 08                     movzx eax, word ptr [rbx + 8]
005E9255  48 C1 E0 04                     shl rax, 4
005E9259  48 83 C0 F0                     add rax, -0x10
005E925D  48 03 C3                        add rax, rbx
005E9260  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
005E9268  0F 57 C0                        xorps xmm0, xmm0
005E926B  0F 11 00                        movups xmmword ptr [rax], xmm0
005E926E  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E9272  0F 84 07 02 00 00               je 0x1405e947f
005E9278  8A 4B 0A                        mov cl, byte ptr [rbx + 0xa]
005E927B  32 4B 09                        xor cl, byte ptr [rbx + 9]
005E927E  32 4B 08                        xor cl, byte ptr [rbx + 8]
005E9281  88 4B 0B                        mov byte ptr [rbx + 0xb], cl
005E9284  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
005E928A  31 43 08                        xor dword ptr [rbx + 8], eax
005E928D  E9 ED 01 00 00                  jmp 0x1405e947f
005E9292  C7 44 24 48 17 00 00 C0         mov dword ptr [rsp + 0x48], 0xc0000017
005E929A  E9 D8 01 00 00                  jmp 0x1405e9477
005E929F  8B 46 70                        mov eax, dword ptr [rsi + 0x70]
005E92A2  A8 02                           test al, 2
005E92A4  0F 84 C5 01 00 00               je 0x1405e946f
005E92AA  49 8D 47 30                     lea rax, [r15 + 0x30]
005E92AE  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
005E92B6  48 83 C0 08                     add rax, 8
005E92BA  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
005E92C2  48 8D 88 FF 0F 00 00            lea rcx, [rax + 0xfff]
005E92C9  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
005E92D0  48 8B 96 40 02 00 00            mov rdx, qword ptr [rsi + 0x240]
005E92D7  48 2B 96 A0 02 00 00            sub rdx, qword ptr [rsi + 0x2a0]
005E92DE  4C 8D 8E 78 01 00 00            lea r9, [rsi + 0x178]
005E92E5  4C 8B C6                        mov r8, rsi
005E92E8  E8 1F EF E6 FF                  call 0x14045820c
005E92ED  89 84 24 38 01 00 00            mov dword ptr [rsp + 0x138], eax
005E92F4  85 C0                           test eax, eax
005E92F6  75 0D                           jne 0x1405e9305
005E92F8  C7 44 24 48 2D 01 00 C0         mov dword ptr [rsp + 0x48], 0xc000012d
005E9300  E9 72 01 00 00                  jmp 0x1405e9477
005E9305  48 83 A4 24 50 01 00 00 00      and qword ptr [rsp + 0x150], 0
005E930E  48 8B 05 2B F0 83 00            mov rax, qword ptr [rip + 0x83f02b]
005E9315  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
005E931D  48 8B C8                        mov rcx, rax
005E9320  48 C1 E9 0C                     shr rcx, 0xc
005E9324  48 33 C8                        xor rcx, rax
005E9327  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
005E932F  48 8B D1                        mov rdx, rcx
005E9332  48 C1 E2 19                     shl rdx, 0x19
005E9336  48 33 D1                        xor rdx, rcx
005E9339  48 89 94 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdx
005E9341  48 8B CA                        mov rcx, rdx
005E9344  48 C1 E9 1B                     shr rcx, 0x1b
005E9348  48 33 CA                        xor rcx, rdx
005E934B  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
005E9353  F0 48 0F B1 0D E4 EF 83 00      lock cmpxchg qword ptr [rip + 0x83efe4], rcx
005E935C  74 02                           je 0x1405e9360
005E935E  EB B5                           jmp 0x1405e9315
005E9360  44 6B C1 FD                     imul r8d, ecx, -3
005E9364  41 83 E0 0F                     and r8d, 0xf
005E9368  49 C1 E0 0C                     shl r8, 0xc
005E936C  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
005E9374  4C 8D 8C 24 A8 00 00 00         lea r9, [rsp + 0xa8]
005E937C  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
005E9384  E8 73 1D 00 00                  call 0x1405eb0fc
005E9389  48 8B F8                        mov rdi, rax
005E938C  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
005E9394  48 85 C0                        test rax, rax
005E9397  75 1F                           jne 0x1405e93b8
005E9399  45 33 F6                        xor r14d, r14d
005E939C  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005E93A1  8B 86 80 02 00 00               mov eax, dword ptr [rsi + 0x280]
005E93A7  FF C0                           inc eax
005E93A9  89 86 80 02 00 00               mov dword ptr [rsi + 0x280], eax
005E93AF  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
005E93B3  E9 CE 00 00 00                  jmp 0x1405e9486
005E93B8  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
005E93C0  0F B7 C1                        movzx eax, cx
005E93C3  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
005E93CB  66 2B C2                        sub ax, dx
005E93CE  66 89 47 38                     mov word ptr [rdi + 0x38], ax
005E93D2  80 CB 02                        or bl, 2
005E93D5  88 5F 3A                        mov byte ptr [rdi + 0x3a], bl
005E93D8  48 89 4F 20                     mov qword ptr [rdi + 0x20], rcx
005E93DC  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
005E93E4  48 89 57 28                     mov qword ptr [rdi + 0x28], rdx
005E93E8  C6 47 3F 04                     mov byte ptr [rdi + 0x3f], 4
005E93EC  48 03 8E 58 02 00 00            add rcx, qword ptr [rsi + 0x258]
005E93F3  48 89 8E 58 02 00 00            mov qword ptr [rsi + 0x258], rcx
005E93FA  48 8B 8E 50 02 00 00            mov rcx, qword ptr [rsi + 0x250]
005E9401  48 03 CA                        add rcx, rdx
005E9404  48 89 8E 50 02 00 00            mov qword ptr [rsi + 0x250], rcx
005E940B  83 7E 7C 00                     cmp dword ptr [rsi + 0x7c], 0
005E940F  74 15                           je 0x1405e9426
005E9411  8A 4F 3A                        mov cl, byte ptr [rdi + 0x3a]
005E9414  32 4F 39                        xor cl, byte ptr [rdi + 0x39]
005E9417  32 4F 38                        xor cl, byte ptr [rdi + 0x38]
005E941A  88 4F 3B                        mov byte ptr [rdi + 0x3b], cl
005E941D  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
005E9423  31 47 38                        xor dword ptr [rdi + 0x38], eax
005E9426  4C 8D 86 10 01 00 00            lea r8, [rsi + 0x110]
005E942D  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005E9431  48 8B 08                        mov rcx, qword ptr [rax]
005E9434  49 3B C8                        cmp rcx, r8
005E9437  75 10                           jne 0x1405e9449
005E9439  4C 89 07                        mov qword ptr [rdi], r8
005E943C  48 89 47 08                     mov qword ptr [rdi + 8], rax
005E9440  48 89 38                        mov qword ptr [rax], rdi
005E9443  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005E9447  EB 18                           jmp 0x1405e9461
005E9449  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005E944F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E9454  45 33 C9                        xor r9d, r9d
005E9457  33 D2                           xor edx, edx
005E9459  8D 4A 0D                        lea ecx, [rdx + 0xd]
005E945C  E8 5B 23 D7 FF                  call 0x14035b7bc
005E9461  4C 8D 77 40                     lea r14, [rdi + 0x40]
005E9465  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005E946A  E9 40 FF FF FF                  jmp 0x1405e93af
005E946F  C7 44 24 48 23 00 00 C0         mov dword ptr [rsp + 0x48], 0xc0000023
005E9477  45 33 F6                        xor r14d, r14d
005E947A  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005E947F  8A 84 24 50 01 00 00            mov al, byte ptr [rsp + 0x150]
005E9486  84 C0                           test al, al
005E9488  74 0C                           je 0x1405e9496
005E948A  48 8B 8E 60 01 00 00            mov rcx, qword ptr [rsi + 0x160]
005E9491  E8 7A 65 C7 FF                  call 0x14025fa10
005E9496  49 8B C6                        mov rax, r14
005E9499  E9 6A F7 FF FF                  jmp 0x1405e8c08
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAllocateHeap(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned __int8 v_stack_p150;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned __int8 v_stack_p43;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (240);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 152) = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    v_stack_mE4 = (unsigned int)(a1 + 1);
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    v_stack_mE7 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    *(unsigned __int8 *)(v_rsp + 40) = 0;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_mD0 = 0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_mB8 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    if ((((unsigned int)((unsigned int)(a2))) & (0x3C010F60ULL)) != 0) goto loc_005E8BE5;
    if (a3 >= ((unsigned int)(0x80000000ULL))) goto loc_005E8BE5;
    v_stack_mD8 = (unsigned int)((unsigned __int8)(a1 + 1));
    v_r13 = (a4) >> (4);
    v_r15 = a4;
    if (v_r13 < 2) {
        v_r15 = (a4) + (16);
        *(unsigned __int64 *)(v_rsp + 32) = v_r15;
        v_r13 = a1 + 2;
    }
    *(unsigned int *)(a6) = 3;
    goto loc_005E8C86;
loc_005E8BE5:
    v_stack_mE4 = 0;
    *(unsigned int *)(a6) = 4;
    if (a3 <= a6) goto loc_005E8C1C;
    result = 0;
loc_005E8C08:
    v_rsp = (v_rsp) + (240);
    return result;
loc_005E8C1C:
    if (a3 == 0) { a3 = a1 + 1; }
    v_r15 = (a3) + (*(unsigned __int64 *)(a1 + 256));
    v_r15 = (v_r15) & (*(unsigned __int64 *)(a1 + 264));
    if (v_r15 < 32) { v_r15 = 32; }
    v_stack_p148 = v_r15;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (4));
    v_rbx = (unsigned __int8)((v_rbx) & (225));
    v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(a1 + 1)));
    v_stack_p50 = (unsigned int)(v_rbx);
    if ((((unsigned int)((unsigned int)(a2))) & (0x3C000100ULL)) != 0) goto loc_005E8C6C;
    v_r13 = v_r15;
    if ((*(unsigned __int64 *)(a1 + 328)) != 0) {
        v_rbx = (unsigned __int8)((v_rbx) | (2));
        v_stack_p50 = (unsigned int)(v_rbx);
        v_r13 = v_r15 + 16;
        v_r15 = v_r13;
        v_stack_p148 = v_r13;
    }
    v_r13 = (v_r13) >> (4);
loc_005E8C86:
    if (condition_is_above_or_equal) goto loc_005E8C9F;
    result = RtlGetNtGlobalFlags(a1, a1 + 1, a3, a4);
    if (!(condition_is_below)) {
        v_rbx = (unsigned __int8)((v_rbx) | (8));
        v_stack_p50 = (unsigned int)(v_rbx);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(a2)))) == 0) {
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExAcquireResourceExclusiveLite(a1, a2, a3, a4);
        result = 1;
        v_stack_p150 = (unsigned __int8)(result);
        v_stack_p40 = (unsigned __int8)(result);
    }
    if (v_r13 > ((unsigned int)(*(unsigned int *)(a1 + 148)))) goto loc_005E929F;
    v_stack_pB0 = a1 + 336;
    result = RtlpFindEntry(a1, v_r13, a3, a4);
    v_stack_pB8 = result;
    if ((a1 + 336) == result) goto loc_005E8E44;
    v_stack_p80 = result - 16;
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_005E8D46;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result - 6)) ^ (*(unsigned __int8 *)(result - 7)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result - 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + 136));
    if ((*(unsigned __int8 *)(result - 5)) != ((unsigned __int8)(a1))) {
        a2 = result - 16;
        a1 = a1;
        result = RtlpAnalyzeHeapFailure(a1, a2, a3, a4);
    }
    if ((*(unsigned __int16 *)(result - 8)) < v_r13) goto loc_005E8E1F;
    v_stack_p68 = *(unsigned __int64 *)(result);
    v_stack_p60 = *(unsigned __int64 *)(result + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8))) goto loc_005E8DFA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_005E8DFA;
    result = (*(unsigned __int64 *)(a1 + 192)) - (*(unsigned __int16 *)(result - 8));
    *(unsigned __int64 *)(a1 + 192) = result;
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E8DE0;
loc_005E8DA6:
    if ((*(unsigned __int16 *)(result - 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E8DB9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) != 0) goto loc_005E8DF5;
loc_005E8DB9:
    v_stack_p78 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1;
    v_stack_p28 = *(unsigned __int16 *)(result - 16 + 8);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
    result = RtlpHeapRemoveListEntry(a1, *(unsigned __int64 *)(a1 + 312), *(unsigned __int64 *)(result + 8), result);
loc_005E8DE0:
    *(unsigned __int64 *)(v_stack_p60) = v_stack_p68;
    *(unsigned __int64 *)(v_stack_p68 + 8) = v_stack_p60;
    v_stack_p42 = 1;
    goto loc_005E8EF6;
loc_005E8DF5:
    goto loc_005E8DA6;
loc_005E8DFA:
    v_stack_p20 = result;
    result = RtlpLogHeapFailure(13, a1, result, result);
    v_stack_p42 = 0;
    goto loc_005E8F1C;
loc_005E8E1F:
    if ((*(unsigned int *)(a1 + 124)) != 0) {
        a1 = *(unsigned __int8 *)(result - 6);
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result - 7)));
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result - 8)));
        *(unsigned __int8 *)(result - 5) = (unsigned __int8)(a1);
        result = *(unsigned int *)(a1 + 136);
    }
    result = RtlpExtendHeap(a1, v_r15, result, result);
    v_stack_p80 = result;
    if (result == 0) goto loc_005E9292;
    v_stack_p60 = *(unsigned __int64 *)(result + 24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8))) goto loc_005E8EFF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24))) != (result + 16)) goto loc_005E8EFF;
    a1 = (*(unsigned __int64 *)(a1 + 192)) - (*(unsigned __int16 *)(result + 8));
    *(unsigned __int64 *)(a1 + 192) = a1;
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_005E8EE5;
loc_005E8EB0:
    if ((*(unsigned __int16 *)(result + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_005E8EC3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) != 0) goto loc_005E8EFA;
loc_005E8EC3:
    v_stack_p68 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1;
    v_stack_p28 = *(unsigned __int16 *)(result + 8);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
    result = RtlpHeapRemoveListEntry(a1, *(unsigned __int64 *)(a1 + 312), result + 16, result + 16);
loc_005E8EE5:
    *(unsigned __int64 *)(v_stack_p60) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = v_stack_p60;
    v_stack_p43 = 1;
loc_005E8EF6:
    goto loc_005E8F1E;
loc_005E8EFA:
    goto loc_005E8EB0;
loc_005E8EFF:
    v_stack_p20 = 1;
    result = RtlpLogHeapFailure(13, a1, result + 16, result + 16);
    v_stack_p43 = 0;
loc_005E8F1C:
    result = 0;
loc_005E8F1E:
    if (0 == 0) goto loc_005E947F;
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(result + 10));
    if ((unsigned int)((unsigned int)(v_stack_p44)) != 0) goto loc_005E8FAE;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 10))) & (4)) == 0) goto loc_005E8FAE;
    v_rdi = (*(unsigned __int16 *)(result + 8)) << (4);
    v_rdi = (v_rdi) - (32);
    v_stack_p88 = v_rdi;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 10))) & (2)) == 0) goto loc_005E8F72;
    if (v_rdi >= = 4) {
        v_rdi = (v_rdi) - (4);
        v_stack_p88 = v_rdi;
    }
    result = RtlCompareMemoryUlong(result + 32, v_rdi, (unsigned int)(0xFEEEFEEEULL), result + 16);
    if (result == v_rdi) goto loc_005E8FAA;
    a3 = (result + 32) + (result);
    result = DbgPrint(v_rip + 932422, result, a3, result + 16);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 9823827)) != 0) {
    }
loc_005E8FAE:
    v_stack_pC0 = result;
    if (((1) & ((unsigned __int8)(*(unsigned __int8 *)(result + 10)))) == 0) goto loc_005E8FE7;
    a4 = 0;
    result = RtlpLogHeapFailure(1 + 2, a1, result, a4);
    goto loc_005E947F;
loc_005E8FE7:
    *(unsigned __int8 *)(result + 10) = (unsigned __int8)((unsigned int)(v_stack_p50));
    a4 = (*(unsigned __int16 *)(result + 8)) - (v_r13);
    v_stack_pC8 = a4;
    *(unsigned __int16 *)(result + 8) = (unsigned __int16)(v_r13);
    result = (v_r15) - (v_stack_p140);
    v_stack_p50 = result;
    a1 = (v_r13) << (4);
    if (result >= 63) goto loc_005E9028;
    *(unsigned __int8 *)(result + 15) = (unsigned __int8)(result);
    goto loc_005E9030;
loc_005E9028:
    *(unsigned __int64 *)(a1 + result * 1) = result;
    *(unsigned __int8 *)(result + 15) = 63;
loc_005E9030:
    *(unsigned __int8 *)(result + 11) = 0;
    if (a4 == 0) goto loc_005E90D9;
    if (a4 != 1) goto loc_005E9074;
    result = (unsigned __int16)((*(unsigned __int16 *)(result + 8)) + (1));
    *(unsigned __int16 *)(result + 8) = (unsigned __int16)(result);
    v_r15 = (v_r15) - (v_stack_p140);
    v_r15 = (v_r15) + (16);
    v_stack_pE8 = v_r15;
    if (v_r15 >= 63) goto loc_005E9069;
    *(unsigned __int8 *)(result + 15) = (unsigned __int8)(v_r15);
    goto loc_005E90D9;
loc_005E9069:
    *(unsigned __int64 *)(a1 + result * 1 + 16) = v_r15;
    *(unsigned __int8 *)(result + 15) = 63;
    goto loc_005E90D9;
loc_005E9074:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p44)) ^ (1));
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 14)) == 0) goto loc_005E9097;
    a2 = (1) - (*(unsigned __int8 *)(result + 14));
    a2 = (a2) << (16);
    result = (result) & (0xFFFFFFFFFFFF0000ULL);
    a2 = (a2) + (result);
    goto loc_005E909A;
loc_005E9097:
loc_005E909A:
    v_stack_p60 = a1;
    v_stack_p30 = a4;
    v_stack_p28 = (unsigned __int16)(v_r13);
    v_stack_p20 = (unsigned __int8)(v_rdi);
    result = RtlpCreateSplitBlock(a1, a1, a1 + result * 1, (unsigned __int8)(*(unsigned __int8 *)(result + 10)));
    if ((unsigned __int8)(result) == 0) goto loc_005E947F;
    v_stack_p41 = 0;
loc_005E90D9:
    v_stack_p58 = result + 16;
    v_rdi = (*(unsigned __int16 *)(result + 8)) << (4);
    v_stack_p90 = v_rdi;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 15)) & (63));
    if (((unsigned __int8)(result)) == 63) {
        a3 = v_rdi - 8;
        v_rdi = a3;
        v_stack_p90 = a3;
    }
    if (v_stack_p44 == 0) goto loc_005E9173;
    if ((*(unsigned int *)(a1 + 124)) != 0) {
        a1 = *(unsigned __int8 *)(result + 10);
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result + 9)));
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result + 8)));
        *(unsigned __int8 *)(result + 11) = (unsigned __int8)(a1);
        result = *(unsigned int *)(a1 + 136);
    }
    if (a5 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExReleaseResourceLite(a1, v_stack_p140, a3, (unsigned __int8)(*(unsigned __int8 *)(result + 10)));
        result = 0;
        v_stack_p150 = 0;
        v_stack_p40 = 0;
    }
    if (((v_stack_p138) & (8)) == 0) goto loc_005E947F;
    a2 = 0;
    result = memset(result + 16, a2, v_rdi - 8, (unsigned __int8)(*(unsigned __int8 *)(result + 10)));
    goto loc_005E947F;
loc_005E9173:
    if (((v_stack_p138) & (8)) == 0) goto loc_005E9194;
    a3 = (v_rdi - 8) + (-8);
    a2 = 0;
    result = memset(result + 16, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(result + 10)));
    goto loc_005E9217;
loc_005E9194:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (64)) == 0) goto loc_005E9217;
    a2 = (a2) & (-4);
    v_stack_p98 = a2;
    v_stack_pD0 = result + 16;
    a2 = (a2) >> (2);
    v_stack_p98 = a2;
    if (a2 == 0) goto loc_005E9217;
    if ((((unsigned __int8)(result + 16)) & (4)) == 0) goto loc_005E91F0;
    *(unsigned int *)(result + 16) = 0xBAADF00DULL;
    a2 = (a2) - (1);
    v_stack_p98 = a2;
    if (condition_is_equal) goto loc_005E9217;
    v_stack_pD0 = result + 16 + 4;
loc_005E91F0:
    a1 = (a2) >> (1);
    if (((1) & ((unsigned __int8)(a2))) != 0) {
        *(unsigned int *)(result + 16 + 4 + a2 * 4 - 4) = 0xBAADF00DULL;
    }
    result = (unsigned int)(*(unsigned int *)(a1 + 112));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (32)) != 0) {
        a2 = v_stack_p140;
        *(unsigned __int64 *)(result + 16 + a2 * 1) = v_xmm0;
        result = *(unsigned __int8 *)(result + 10);
        result = (unsigned __int8)((result) | (4));
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(result);
    }
    *(unsigned __int8 *)(result + 11) = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 10))) & (2)) == 0) goto loc_005E926E;
    if ((*(unsigned __int8 *)(result + 15)) != 4) goto loc_005E9251;
    goto loc_005E9260;
loc_005E9251:
    result = (*(unsigned __int16 *)(result + 8)) << (4);
    result = (result) + (-16);
    result = (result) + (result);
loc_005E9260:
    v_stack_pA0 = result;
    *(unsigned __int64 *)(result) = v_xmm0;
loc_005E926E:
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_005E947F;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 10)) ^ (*(unsigned __int8 *)(result + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result + 8)));
    *(unsigned __int8 *)(result + 11) = (unsigned __int8)(a1);
    goto loc_005E947F;
loc_005E9292:
    v_stack_p48 = 0xC0000017ULL;
    goto loc_005E9477;
loc_005E929F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (2)) == 0) goto loc_005E946F;
    v_stack_p148 = v_r15 + 48;
    result = (v_r15 + 48) + (8);
    v_stack_p148 = result;
    a1 = (result + 4095) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (*(unsigned __int64 *)(a1 + 576)) - (*(unsigned __int64 *)(a1 + 672));
    result = RtlpHpHeapCheckCommitLimit(a1, a2, a1, a1 + 376);
    v_stack_p138 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_005E9305;
    v_stack_p48 = 0xC000012DULL;
    goto loc_005E9477;
loc_005E9305:
loc_005E9315:
    v_stack_p150 = *(unsigned __int64 *)(v_rip + 8646699);
    a1 = (*(unsigned __int64 *)(v_rip + 8646699)) >> (12);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rip + 8646699));
    v_stack_p150 = a1;
    a2 = (a1) << (25);
    a2 = (a2) ^ (a1);
    v_stack_p150 = a2;
    a1 = (a2) >> (27);
    a1 = (a1) ^ (a2);
    v_stack_p150 = a1;
    if (condition_is_equal) goto loc_005E9360;
    goto loc_005E9315;
loc_005E9360:
    a3 = (unsigned int)((a1) * ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) & (15));
    a3 = (a3) << (12);
    v_stack_pD8 = a3;
    result = RtlpHpAllocVirtBlockCommitFirst(a1, v_stack_p148, a3, v_stack_pA8);
    v_stack_pE0 = result;
    if (result != 0) goto loc_005E93B8;
    v_r14 = 0;
    v_stack_p58 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 640))) + 1);
    *(unsigned int *)(a1 + 640) = (unsigned int)(result);
loc_005E93AF:
    goto loc_005E9486;
loc_005E93B8:
    result = (unsigned __int16)(((unsigned __int16)(v_stack_p148)) - ((unsigned __int16)(v_stack_p140)));
    *(unsigned __int16 *)(result + 56) = (unsigned __int16)(result);
    v_rbx = (unsigned __int8)((result) | (2));
    *(unsigned __int8 *)(result + 58) = (unsigned __int8)(v_rbx);
    *(unsigned __int64 *)(result + 32) = v_stack_p148;
    *(unsigned __int64 *)(result + 40) = v_stack_pA8;
    *(unsigned __int8 *)(result + 63) = 4;
    a1 = (v_stack_p148) + (*(unsigned __int64 *)(a1 + 600));
    *(unsigned __int64 *)(a1 + 600) = a1;
    a1 = (*(unsigned __int64 *)(a1 + 592)) + (v_stack_pA8);
    *(unsigned __int64 *)(a1 + 592) = a1;
    if ((*(unsigned int *)(a1 + 124)) != 0) {
        a1 = *(unsigned __int8 *)(result + 58);
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result + 57)));
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(result + 56)));
        *(unsigned __int8 *)(result + 59) = (unsigned __int8)(a1);
        result = *(unsigned int *)(a1 + 136);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 272 + 8))) != (a1 + 272)) goto loc_005E9449;
    *(unsigned __int64 *)(result) = a1 + 272;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 272 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 272 + 8)) = result;
    *(unsigned __int64 *)(a1 + 272 + 8) = result;
    goto loc_005E9461;
loc_005E9449:
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 272 + 8));
    a4 = 0;
    a2 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, a1 + 272, a4);
loc_005E9461:
    v_stack_p58 = result + 64;
    goto loc_005E93AF;
loc_005E946F:
    v_stack_p48 = 0xC0000023ULL;
loc_005E9477:
    v_r14 = 0;
    v_stack_p58 = 0;
loc_005E947F:
loc_005E9486:
    result = a5;
    if (a5 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExReleaseResourceLite(a1, a2, a1 + 272, a4);
    }
    goto loc_005E8C08;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAllocateHeap(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint32_t v_stack_p10;
    uint8_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint8_t v_stack_p150;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint8_t v_stack_p42;
    uint8_t v_stack_p43;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (240);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x98) = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    v_stack_mE4 = (uint32_t)(Arg1 + 1);
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    v_stack_mE7 = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    *(uint8_t *)(local_rsp + 0x28) = 0;
    v_stack_mE8 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_mD0 = 0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_mB8 = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    if ((((uint32_t)((uint32_t)(Arg2))) & (0x3C010F60ULL)) != 0) goto loc_005E8BE5;
    if (Arg3 >= ((uint32_t)(0x80000000ULL))) goto loc_005E8BE5;
    v_stack_mD8 = (uint32_t)((uint8_t)(Arg1 + 1));
    local_r13 = (Arg4) >> (4);
    local_r15 = Arg4;
    if (local_r13 < 2) {
        local_r15 = (Arg4) + (16);
        *(uint64_t *)(local_rsp + 0x20) = local_r15;
        local_r13 = Arg1 + 2;
    }
    *(uint32_t *)(arg6) = 3;
    goto loc_005E8C86;
loc_005E8BE5:
    v_stack_mE4 = 0;
    *(uint32_t *)(arg6) = 4;
    if (Arg3 <= Arg6) goto loc_005E8C1C;
    result = 0;
loc_005E8C08:
    local_rsp = (local_rsp) + (240);
    return result;
loc_005E8C1C:
    if (Arg3 == 0) { Arg3 = Arg1 + 1; }
    local_r15 = (Arg3) + (*(uint64_t *)(arg1 + 0x100));
    local_r15 = (local_r15) & (*(uint64_t *)(arg1 + 0x108));
    if (local_r15 < 32) { local_r15 = 32; }
    v_stack_p148 = local_r15;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (4));
    local_rbx = (uint8_t)((local_rbx) & (225));
    local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(Arg1 + 1)));
    v_stack_p50 = (uint32_t)(local_rbx);
    if ((((uint32_t)((uint32_t)(Arg2))) & (0x3C000100ULL)) != 0) goto loc_005E8C6C;
    local_r13 = local_r15;
    if ((*(uint64_t *)(arg1 + 0x148)) != 0) {
        local_rbx = (uint8_t)((local_rbx) | (2));
        v_stack_p50 = (uint32_t)(local_rbx);
        local_r13 = local_r15 + 16;
        local_r15 = local_r13;
        v_stack_p148 = local_r13;
    }
    local_r13 = (local_r13) >> (4);
loc_005E8C86:
    if (condition_is_above_or_equal) goto loc_005E8C9F;
    result = RtlGetNtGlobalFlags(Arg1, Arg1 + 1, Arg3, Arg4);
    if (!(condition_is_below)) {
        local_rbx = (uint8_t)((local_rbx) | (8));
        v_stack_p50 = (uint32_t)(local_rbx);
    }
    if (((1) & ((uint8_t)((uint32_t)(Arg2)))) == 0) {
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg1 + 0x160);
        result = ExAcquireResourceExclusiveLite(Arg1, Arg2, Arg3, Arg4);
        result = 1;
        v_stack_p150 = (uint8_t)(result);
        v_stack_p40 = (uint8_t)(result);
    }
    if (local_r13 > ((uint32_t)(*(uint32_t *)(arg1 + 0x94)))) goto loc_005E929F;
    v_stack_pB0 = Arg1 + 336;
    result = RtlpFindEntry(Arg1, local_r13, Arg3, Arg4);
    v_stack_pB8 = result;
    if ((Arg1 + 336) == result) goto loc_005E8E44;
    v_stack_p80 = result - 16;
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_005E8D46;
    Arg1 = (uint8_t)((*(uint8_t *)(result - 0x6)) ^ (*(uint8_t *)(result - 0x7)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result - 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x88));
    if ((*(uint8_t *)(result - 0x5)) != ((uint8_t)(Arg1))) {
        Arg2 = result - 16;
        Arg1 = Arg1;
        result = RtlpAnalyzeHeapFailure(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint16_t *)(result - 0x8)) < local_r13) goto loc_005E8E1F;
    v_stack_p68 = *(uint64_t *)(result);
    v_stack_p60 = *(uint64_t *)(result + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != (*(uint64_t *)(*(uint64_t *)(result) + 0x8))) goto loc_005E8DFA;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_005E8DFA;
    result = (*(uint64_t *)(arg1 + 0xC0)) - (*(uint16_t *)(result - 0x8));
    *(uint64_t *)(arg1 + 0xC0) = result;
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E8DE0;
loc_005E8DA6:
    if ((*(uint16_t *)(result - 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E8DB9;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) != 0) goto loc_005E8DF5;
loc_005E8DB9:
    v_stack_p78 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1;
    v_stack_p28 = *(uint16_t *)(result - 0x10 + 0x8);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
    result = RtlpHeapRemoveListEntry(Arg1, *(uint64_t *)(arg1 + 0x138), *(uint64_t *)(result + 0x8), result);
loc_005E8DE0:
    *(uint64_t *)(v_stack_p60) = v_stack_p68;
    *(uint64_t *)(v_stack_p68 + 0x8) = v_stack_p60;
    v_stack_p42 = 1;
    goto loc_005E8EF6;
loc_005E8DF5:
    goto loc_005E8DA6;
loc_005E8DFA:
    v_stack_p20 = result;
    result = RtlpLogHeapFailure(13, Arg1, result, result);
    v_stack_p42 = 0;
    goto loc_005E8F1C;
loc_005E8E1F:
    if ((*(uint32_t *)(arg1 + 0x7C)) != 0) {
        Arg1 = *(uint8_t *)(result - 0x6);
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result - 0x7)));
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result - 0x8)));
        *(uint8_t *)(result - 0x5) = (uint8_t)(Arg1);
        result = *(uint32_t *)(arg1 + 0x88);
    }
    result = RtlpExtendHeap(Arg1, local_r15, result, result);
    v_stack_p80 = result;
    if (result == 0) goto loc_005E9292;
    v_stack_p60 = *(uint64_t *)(result + 0x18);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x18))) != (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8))) goto loc_005E8EFF;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x18))) != (result + 16)) goto loc_005E8EFF;
    Arg1 = (*(uint64_t *)(arg1 + 0xC0)) - (*(uint16_t *)(result + 0x8));
    *(void **)(arg1 + 0xC0) = Arg1;
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_005E8EE5;
loc_005E8EB0:
    if ((*(uint16_t *)(result + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_005E8EC3;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) != 0) goto loc_005E8EFA;
loc_005E8EC3:
    v_stack_p68 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1;
    v_stack_p28 = *(uint16_t *)(result + 0x8);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
    result = RtlpHeapRemoveListEntry(Arg1, *(uint64_t *)(arg1 + 0x138), result + 16, result + 16);
loc_005E8EE5:
    *(uint64_t *)(v_stack_p60) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = v_stack_p60;
    v_stack_p43 = 1;
loc_005E8EF6:
    goto loc_005E8F1E;
loc_005E8EFA:
    goto loc_005E8EB0;
loc_005E8EFF:
    v_stack_p20 = 1;
    result = RtlpLogHeapFailure(13, Arg1, result + 16, result + 16);
    v_stack_p43 = 0;
loc_005E8F1C:
    result = 0;
loc_005E8F1E:
    if (0 == 0) goto loc_005E947F;
    v_stack_p41 = (uint8_t)(*(uint8_t *)(result + 0xA));
    if ((uint32_t)((uint32_t)(v_stack_p44)) != 0) goto loc_005E8FAE;
    if ((((uint8_t)(*(uint8_t *)(result + 0xA))) & (4)) == 0) goto loc_005E8FAE;
    local_rdi = (*(uint16_t *)(result + 0x8)) << (4);
    local_rdi = (local_rdi) - (32);
    v_stack_p88 = local_rdi;
    if ((((uint8_t)(*(uint8_t *)(result + 0xA))) & (2)) == 0) goto loc_005E8F72;
    if (local_rdi >= = 4) {
        local_rdi = (local_rdi) - (4);
        v_stack_p88 = local_rdi;
    }
    result = RtlCompareMemoryUlong(result + 32, local_rdi, (uint32_t)(0xFEEEFEEEULL), result + 16);
    if (result == local_rdi) goto loc_005E8FAA;
    Arg3 = (result + 32) + (result);
    result = DbgPrint(v_rip + 932422, result, Arg3, result + 16);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x95E653)) != 0) {
    }
loc_005E8FAE:
    v_stack_pC0 = result;
    if (((1) & ((uint8_t)(*(uint8_t *)(result + 0xA)))) == 0) goto loc_005E8FE7;
    Arg4 = 0;
    result = RtlpLogHeapFailure(1 + 2, Arg1, result, Arg4);
    goto loc_005E947F;
loc_005E8FE7:
    *(uint8_t *)(result + 0xA) = (uint8_t)((uint32_t)(v_stack_p50));
    Arg4 = (*(uint16_t *)(result + 0x8)) - (local_r13);
    v_stack_pC8 = Arg4;
    *(uint16_t *)(result + 0x8) = (uint16_t)(local_r13);
    result = (local_r15) - (v_stack_p140);
    v_stack_p50 = result;
    Arg1 = (local_r13) << (4);
    if (result >= 63) goto loc_005E9028;
    *(uint8_t *)(result + 0xF) = (uint8_t)(result);
    goto loc_005E9030;
loc_005E9028:
    *(uint64_t *)(arg1 + result * 1) = result;
    *(uint8_t *)(result + 0xF) = 63;
loc_005E9030:
    *(uint8_t *)(result + 0xB) = 0;
    if (Arg4 == 0) goto loc_005E90D9;
    if (Arg4 != 1) goto loc_005E9074;
    result = (uint16_t)((*(uint16_t *)(result + 0x8)) + (1));
    *(uint16_t *)(result + 0x8) = (uint16_t)(result);
    local_r15 = (local_r15) - (v_stack_p140);
    local_r15 = (local_r15) + (16);
    v_stack_pE8 = local_r15;
    if (local_r15 >= 63) goto loc_005E9069;
    *(uint8_t *)(result + 0xF) = (uint8_t)(local_r15);
    goto loc_005E90D9;
loc_005E9069:
    *(uint64_t *)(arg1 + result * 1 + 0x10) = local_r15;
    *(uint8_t *)(result + 0xF) = 63;
    goto loc_005E90D9;
loc_005E9074:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p44)) ^ (1));
    if ((uint8_t)(*(uint8_t *)(result + 0xE)) == 0) goto loc_005E9097;
    Arg2 = (1) - (*(uint8_t *)(result + 0xE));
    Arg2 = (Arg2) << (16);
    result = (result) & (0xFFFFFFFFFFFF0000ULL);
    Arg2 = (Arg2) + (result);
    goto loc_005E909A;
loc_005E9097:
loc_005E909A:
    v_stack_p60 = Arg1;
    v_stack_p30 = Arg4;
    v_stack_p28 = (uint16_t)(local_r13);
    v_stack_p20 = (uint8_t)(local_rdi);
    result = RtlpCreateSplitBlock(Arg1, Arg1, Arg1 + result * 1, (uint8_t)(*(uint8_t *)(result + 0xA)));
    if ((uint8_t)(result) == 0) goto loc_005E947F;
    v_stack_p41 = 0;
loc_005E90D9:
    v_stack_p58 = result + 16;
    local_rdi = (*(uint16_t *)(result + 0x8)) << (4);
    v_stack_p90 = local_rdi;
    result = (uint8_t)((*(uint8_t *)(result + 0xF)) & (63));
    if (((uint8_t)(result)) == 63) {
        Arg3 = local_rdi - 8;
        local_rdi = Arg3;
        v_stack_p90 = Arg3;
    }
    if (v_stack_p44 == 0) goto loc_005E9173;
    if ((*(uint32_t *)(arg1 + 0x7C)) != 0) {
        Arg1 = *(uint8_t *)(result + 0xA);
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result + 0x9)));
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result + 0x8)));
        *(uint8_t *)(result + 0xB) = (uint8_t)(Arg1);
        result = *(uint32_t *)(arg1 + 0x88);
    }
    if (Arg5 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x160);
        result = ExReleaseResourceLite(Arg1, v_stack_p140, Arg3, (uint8_t)(*(uint8_t *)(result + 0xA)));
        result = 0;
        v_stack_p150 = 0;
        v_stack_p40 = 0;
    }
    if (((v_stack_p138) & (8)) == 0) goto loc_005E947F;
    Arg2 = 0;
    result = memset(result + 16, Arg2, local_rdi - 8, (uint8_t)(*(uint8_t *)(result + 0xA)));
    goto loc_005E947F;
loc_005E9173:
    if (((v_stack_p138) & (8)) == 0) goto loc_005E9194;
    Arg3 = (local_rdi - 8) + (-8);
    Arg2 = 0;
    result = memset(result + 16, Arg2, Arg3, (uint8_t)(*(uint8_t *)(result + 0xA)));
    goto loc_005E9217;
loc_005E9194:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (64)) == 0) goto loc_005E9217;
    Arg2 = (Arg2) & (-4);
    v_stack_p98 = Arg2;
    v_stack_pD0 = result + 16;
    Arg2 = (Arg2) >> (2);
    v_stack_p98 = Arg2;
    if (Arg2 == 0) goto loc_005E9217;
    if ((((uint8_t)(result + 16)) & (4)) == 0) goto loc_005E91F0;
    *(uint32_t *)(result + 0x10) = 0xBAADF00DULL;
    Arg2 = (Arg2) - (1);
    v_stack_p98 = Arg2;
    if (condition_is_equal) goto loc_005E9217;
    v_stack_pD0 = result + 16 + 4;
loc_005E91F0:
    Arg1 = (Arg2) >> (1);
    if (((1) & ((uint8_t)(Arg2))) != 0) {
        *(uint32_t *)(result + 0x10 + 0x4 + Arg2 * 4 - 0x4) = 0xBAADF00DULL;
    }
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x70));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (32)) != 0) {
        Arg2 = v_stack_p140;
        *(uint64_t *)(result + 0x10 + Arg2 * 1) = v_xmm0;
        result = *(uint8_t *)(result + 0xA);
        result = (uint8_t)((result) | (4));
        *(uint8_t *)(result + 0xA) = (uint8_t)(result);
    }
    *(uint8_t *)(result + 0xB) = 0;
    if ((((uint8_t)(*(uint8_t *)(result + 0xA))) & (2)) == 0) goto loc_005E926E;
    if ((*(uint8_t *)(result + 0xF)) != 4) goto loc_005E9251;
    goto loc_005E9260;
loc_005E9251:
    result = (*(uint16_t *)(result + 0x8)) << (4);
    result = (result) + (-16);
    result = (result) + (result);
loc_005E9260:
    v_stack_pA0 = result;
    *(uint64_t *)(result) = v_xmm0;
loc_005E926E:
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_005E947F;
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0xA)) ^ (*(uint8_t *)(result + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result + 0x8)));
    *(uint8_t *)(result + 0xB) = (uint8_t)(Arg1);
    goto loc_005E947F;
loc_005E9292:
    v_stack_p48 = 0xC0000017ULL;
    goto loc_005E9477;
loc_005E929F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (2)) == 0) goto loc_005E946F;
    v_stack_p148 = local_r15 + 48;
    result = (local_r15 + 48) + (8);
    v_stack_p148 = result;
    Arg1 = (result + 4095) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (*(uint64_t *)(arg1 + 0x240)) - (*(uint64_t *)(arg1 + 0x2A0));
    result = RtlpHpHeapCheckCommitLimit(Arg1, Arg2, Arg1, Arg1 + 376);
    v_stack_p138 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_005E9305;
    v_stack_p48 = 0xC000012DULL;
    goto loc_005E9477;
loc_005E9305:
loc_005E9315:
    v_stack_p150 = *(uint64_t *)(v_rip + 0x83F02B);
    Arg1 = (*(uint64_t *)(v_rip + 0x83F02B)) >> (12);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_rip + 0x83F02B));
    v_stack_p150 = Arg1;
    Arg2 = (Arg1) << (25);
    Arg2 = (Arg2) ^ (Arg1);
    v_stack_p150 = Arg2;
    Arg1 = (Arg2) >> (27);
    Arg1 = (Arg1) ^ (Arg2);
    v_stack_p150 = Arg1;
    if (condition_is_equal) goto loc_005E9360;
    goto loc_005E9315;
loc_005E9360:
    Arg3 = (uint32_t)((Arg1) * ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) & (15));
    Arg3 = (Arg3) << (12);
    v_stack_pD8 = Arg3;
    result = RtlpHpAllocVirtBlockCommitFirst(Arg1, v_stack_p148, Arg3, v_stack_pA8);
    v_stack_pE0 = result;
    if (result != 0) goto loc_005E93B8;
    local_r14 = 0;
    v_stack_p58 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x280))) + 1);
    *(uint32_t *)(arg1 + 0x280) = (uint32_t)(result);
loc_005E93AF:
    goto loc_005E9486;
loc_005E93B8:
    result = (uint16_t)(((uint16_t)(v_stack_p148)) - ((uint16_t)(v_stack_p140)));
    *(uint16_t *)(result + 0x38) = (uint16_t)(result);
    local_rbx = (uint8_t)((result) | (2));
    *(uint8_t *)(result + 0x3A) = (uint8_t)(local_rbx);
    *(uint64_t *)(result + 0x20) = v_stack_p148;
    *(uint64_t *)(result + 0x28) = v_stack_pA8;
    *(uint8_t *)(result + 0x3F) = 4;
    Arg1 = (v_stack_p148) + (*(uint64_t *)(arg1 + 0x258));
    *(void **)(arg1 + 0x258) = Arg1;
    Arg1 = (*(uint64_t *)(arg1 + 0x250)) + (v_stack_pA8);
    *(void **)(arg1 + 0x250) = Arg1;
    if ((*(uint32_t *)(arg1 + 0x7C)) != 0) {
        Arg1 = *(uint8_t *)(result + 0x3A);
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result + 0x39)));
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(result + 0x38)));
        *(uint8_t *)(result + 0x3B) = (uint8_t)(Arg1);
        result = *(uint32_t *)(arg1 + 0x88);
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x110 + 0x8))) != (Arg1 + 272)) goto loc_005E9449;
    *(void **)(result) = Arg1 + 272;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x110 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x110 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x110 + 0x8) = result;
    goto loc_005E9461;
loc_005E9449:
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x110 + 0x8));
    Arg4 = 0;
    Arg2 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, Arg1 + 272, Arg4);
loc_005E9461:
    v_stack_p58 = result + 64;
    goto loc_005E93AF;
loc_005E946F:
    v_stack_p48 = 0xC0000023ULL;
loc_005E9477:
    local_r14 = 0;
    v_stack_p58 = 0;
loc_005E947F:
loc_005E9486:
    result = Arg5;
    if (Arg5 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x160);
        result = ExReleaseResourceLite(Arg1, Arg2, Arg1 + 272, Arg4);
    }
    goto loc_005E8C08;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x94` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `W` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x108` | `64` | `R` |
| `Arg1` | `+ 0x110` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x148` | `64` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x250` | `64` | `R` |
| `Arg1` | `+ 0x250` | `64` | `W` |
| `Arg1` | `+ 0x258` | `64` | `R` |
| `Arg1` | `+ 0x258` | `64` | `W` |
| `Arg1` | `+ 0x280` | `32` | `R` |
| `Arg1` | `+ 0x280` | `32` | `W` |
| `Arg1` | `+ 0x2A0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E8B1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
