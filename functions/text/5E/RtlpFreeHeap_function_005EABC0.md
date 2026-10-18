# RtlpFreeHeap

- RVA: `0x005EABC0`–`0x005EB0F6` (길이 `1,334` bytes)
- VA: `0x00000001405EABC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFB48`
- 디코드: `348`개 명령, `1,334/1,334` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005EAC13` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EAC4E` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x005EAC81` → [RtlpAnalyzeHeapFailure](../5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (function, `0x005F0F9C`)
- `0x005EACCF` → [RtlpAnalyzeHeapFailure](../5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (function, `0x005F0F9C`)
- `0x005EAD04` → [RtlpCoalesceFreeBlocks](RtlpCoalesceFreeBlocks_function_005E952C.md) (function, `0x005E952C`)
- `0x005EAD3F` → [RtlpDeCommitFreeBlock](RtlpDeCommitFreeBlock_function_005EA158.md) (function, `0x005EA158`)
- `0x005EAD81` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005EAE08` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EAEF9` → [RtlpFindEntry](../5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x005EAF80` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EAFD9` → [RtlpHeapAddListEntry](../5F/RtlpHeapAddListEntry_function_005F18C8.md) (function, `0x005F18C8`)
- `0x005EB00B` → [RtlpInsertFreeBlock](RtlpInsertFreeBlock_function_005EB4C0.md) (function, `0x005EB4C0`)
- `0x005EB090` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EB0A9` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x005EB0D5` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x005EB0E7` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- [sub_006F57DA](../6F/Unknown_function_006F57DA.md) at `0x006F5907`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EABC0  48 8B C4                        mov rax, rsp
005EABC3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
005EABC7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
005EABCB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005EABCF  48 89 48 08                     mov qword ptr [rax + 8], rcx
005EABD3  56                              push rsi
005EABD4  57                              push rdi
005EABD5  41 54                           push r12
005EABD7  41 56                           push r14
005EABD9  41 57                           push r15
005EABDB  48 81 EC 80 00 00 00            sub rsp, 0x80
005EABE2  49 8B F8                        mov rdi, r8
005EABE5  48 8B D9                        mov rbx, rcx
005EABE8  45 33 E4                        xor r12d, r12d
005EABEB  4C 89 60 20                     mov qword ptr [rax + 0x20], r12
005EABEF  45 8A F4                        mov r14b, r12b
005EABF2  44 88 60 88                     mov byte ptr [rax - 0x78], r12b
005EABF6  4C 89 60 A8                     mov qword ptr [rax - 0x58], r12
005EABFA  49 3B C8                        cmp rcx, r8
005EABFD  75 34                           jne 0x1405eac33
005EABFF  4C 89 60 80                     mov qword ptr [rax - 0x80], r12
005EAC03  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
005EAC08  45 33 C9                        xor r9d, r9d
005EAC0B  48 8B D1                        mov rdx, rcx
005EAC0E  41 8D 4C 24 09                  lea ecx, [r12 + 9]
005EAC13  E8 A4 0B D7 FF                  call 0x14035b7bc
005EAC18  33 C0                           xor eax, eax
005EAC1A  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
005EAC22  48 81 C4 80 00 00 00            add rsp, 0x80
005EAC29  41 5F                           pop r15
005EAC2B  41 5E                           pop r14
005EAC2D  41 5C                           pop r12
005EAC2F  5F                              pop rdi
005EAC30  5E                              pop rsi
005EAC31  C3                              ret
005EAC32  CC                              int3
005EAC33  0B 51 74                        or edx, dword ptr [rcx + 0x74]
005EAC36  44 8B FA                        mov r15d, edx
005EAC39  41 81 E7 60 0F 01 3C            and r15d, 0x3c010f60
005EAC40  F6 C2 01                        test dl, 1
005EAC43  75 5E                           jne 0x1405eaca3
005EAC45  B2 01                           mov dl, 1
005EAC47  48 8B 89 60 01 00 00            mov rcx, qword ptr [rcx + 0x160]
005EAC4E  E8 CD A1 C2 FF                  call 0x140214e20
005EAC53  41 B6 01                        mov r14b, 1
005EAC56  44 88 74 24 30                  mov byte ptr [rsp + 0x30], r14b
005EAC5B  44 39 63 7C                     cmp dword ptr [rbx + 0x7c], r12d
005EAC5F  74 25                           je 0x1405eac86
005EAC61  8B 8B 88 00 00 00               mov ecx, dword ptr [rbx + 0x88]
005EAC67  33 4F 08                        xor ecx, dword ptr [rdi + 8]
005EAC6A  89 4F 08                        mov dword ptr [rdi + 8], ecx
005EAC6D  8A 4F 0A                        mov cl, byte ptr [rdi + 0xa]
005EAC70  32 4F 09                        xor cl, byte ptr [rdi + 9]
005EAC73  32 4F 08                        xor cl, byte ptr [rdi + 8]
005EAC76  38 4F 0B                        cmp byte ptr [rdi + 0xb], cl
005EAC79  74 0B                           je 0x1405eac86
005EAC7B  48 8B D7                        mov rdx, rdi
005EAC7E  48 8B CB                        mov rcx, rbx
005EAC81  E8 16 63 00 00                  call 0x1405f0f9c
005EAC86  0F B7 57 08                     movzx edx, word ptr [rdi + 8]
005EAC8A  48 8B 8B 38 01 00 00            mov rcx, qword ptr [rbx + 0x138]
005EAC91  8B 41 08                        mov eax, dword ptr [rcx + 8]
005EAC94  48 3B D0                        cmp rdx, rax
005EAC97  72 3B                           jb 0x1405eacd4
005EAC99  48 8B 09                        mov rcx, qword ptr [rcx]
005EAC9C  48 85 C9                        test rcx, rcx
005EAC9F  74 33                           je 0x1405eacd4
005EACA1  EB EE                           jmp 0x1405eac91
005EACA3  44 39 61 7C                     cmp dword ptr [rcx + 0x7c], r12d
005EACA7  74 2B                           je 0x1405eacd4
005EACA9  8B 89 88 00 00 00               mov ecx, dword ptr [rcx + 0x88]
005EACAF  41 33 48 08                     xor ecx, dword ptr [r8 + 8]
005EACB3  41 89 48 08                     mov dword ptr [r8 + 8], ecx
005EACB7  41 8A 48 0A                     mov cl, byte ptr [r8 + 0xa]
005EACBB  41 32 48 09                     xor cl, byte ptr [r8 + 9]
005EACBF  41 32 48 08                     xor cl, byte ptr [r8 + 8]
005EACC3  41 38 48 0B                     cmp byte ptr [r8 + 0xb], cl
005EACC7  74 0B                           je 0x1405eacd4
005EACC9  48 8B D7                        mov rdx, rdi
005EACCC  48 8B CB                        mov rcx, rbx
005EACCF  E8 C8 62 00 00                  call 0x1405f0f9c
005EACD4  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
005EACD7  A8 08                           test al, 8
005EACD9  74 05                           je 0x1405eace0
005EACDB  24 F7                           and al, 0xf7
005EACDD  88 47 0A                        mov byte ptr [rdi + 0xa], al
005EACE0  80 7F 0F 04                     cmp byte ptr [rdi + 0xf], 4
005EACE4  0F 84 33 03 00 00               je 0x1405eb01d
005EACEA  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
005EACEE  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
005EACF6  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
005EACFE  48 8B D7                        mov rdx, rdi
005EAD01  48 8B CB                        mov rcx, rbx
005EAD04  E8 23 E8 FF FF                  call 0x1405e952c
005EAD09  48 8B F0                        mov rsi, rax
005EAD0C  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
005EAD14  4C 8B 84 24 C8 00 00 00         mov r8, qword ptr [rsp + 0xc8]
005EAD1C  4C 3B 83 B0 00 00 00            cmp r8, qword ptr [rbx + 0xb0]
005EAD23  72 24                           jb 0x1405ead49
005EAD25  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
005EAD2C  49 8D 0C 00                     lea rcx, [r8 + rax]
005EAD30  48 3B 8B B8 00 00 00            cmp rcx, qword ptr [rbx + 0xb8]
005EAD37  72 10                           jb 0x1405ead49
005EAD39  48 8B D6                        mov rdx, rsi
005EAD3C  48 8B CB                        mov rcx, rbx
005EAD3F  E8 14 F4 FF FF                  call 0x1405ea158
005EAD44  E9 C7 02 00 00                  jmp 0x1405eb010
005EAD49  49 81 F8 00 FF 00 00            cmp r8, 0xff00
005EAD50  0F 87 AF 02 00 00               ja 0x1405eb005
005EAD56  45 85 FF                        test r15d, r15d
005EAD59  45 0F B7 F8                     movzx r15d, r8w
005EAD5D  0F 85 F9 00 00 00               jne 0x1405eae5c
005EAD63  44 88 66 0A                     mov byte ptr [rsi + 0xa], r12b
005EAD67  44 88 66 0F                     mov byte ptr [rsi + 0xf], r12b
005EAD6B  48 8D BB 50 01 00 00            lea rdi, [rbx + 0x150]
005EAD72  4C 39 A3 38 01 00 00            cmp qword ptr [rbx + 0x138], r12
005EAD79  74 10                           je 0x1405ead8b
005EAD7B  41 8B D7                        mov edx, r15d
005EAD7E  48 8B CB                        mov rcx, rbx
005EAD81  E8 2E 6A 00 00                  call 0x1405f17b4
005EAD86  4C 8B C0                        mov r8, rax
005EAD89  EB 03                           jmp 0x1405ead8e
005EAD8B  4C 8B 07                        mov r8, qword ptr [rdi]
005EAD8E  49 3B F8                        cmp rdi, r8
005EAD91  74 43                           je 0x1405eadd6
005EAD93  44 39 63 7C                     cmp dword ptr [rbx + 0x7c], r12d
005EAD97  74 2B                           je 0x1405eadc4
005EAD99  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
005EAD9D  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
005EADA1  85 43 7C                        test dword ptr [rbx + 0x7c], eax
005EADA4  74 0A                           je 0x1405eadb0
005EADA6  33 83 88 00 00 00               xor eax, dword ptr [rbx + 0x88]
005EADAC  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
005EADB0  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
005EADB5  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
005EADBD  44 8A 74 24 30                  mov r14b, byte ptr [rsp + 0x30]
005EADC2  EB 05                           jmp 0x1405eadc9
005EADC4  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005EADC9  0F B7 C0                        movzx eax, ax
005EADCC  4C 3B F8                        cmp r15, rax
005EADCF  76 05                           jbe 0x1405eadd6
005EADD1  4D 8B 00                        mov r8, qword ptr [r8]
005EADD4  EB B8                           jmp 0x1405ead8e
005EADD6  48 8D 7E 10                     lea rdi, [rsi + 0x10]
005EADDA  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005EADDE  48 8B 08                        mov rcx, qword ptr [rax]
005EADE1  49 3B C8                        cmp rcx, r8
005EADE4  75 10                           jne 0x1405eadf6
005EADE6  4C 89 07                        mov qword ptr [rdi], r8
005EADE9  48 89 47 08                     mov qword ptr [rdi + 8], rax
005EADED  48 89 38                        mov qword ptr [rax], rdi
005EADF0  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005EADF4  EB 17                           jmp 0x1405eae0d
005EADF6  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
005EADFB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005EAE00  45 33 C9                        xor r9d, r9d
005EAE03  33 D2                           xor edx, edx
005EAE05  8D 4A 0D                        lea ecx, [rdx + 0xd]
005EAE08  E8 AF 09 D7 FF                  call 0x14035b7bc
005EAE0D  0F B7 46 08                     movzx eax, word ptr [rsi + 8]
005EAE11  48 03 83 C0 00 00 00            add rax, qword ptr [rbx + 0xc0]
005EAE18  48 89 83 C0 00 00 00            mov qword ptr [rbx + 0xc0], rax
005EAE1F  48 8B 93 38 01 00 00            mov rdx, qword ptr [rbx + 0x138]
005EAE26  48 85 D2                        test rdx, rdx
005EAE29  0F 84 AF 01 00 00               je 0x1405eafde
005EAE2F  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
005EAE34  0F B7 4E 08                     movzx ecx, word ptr [rsi + 8]
005EAE38  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005EAE3C  49 3B C8                        cmp rcx, r8
005EAE3F  72 0C                           jb 0x1405eae4d
005EAE41  48 8B 02                        mov rax, qword ptr [rdx]
005EAE44  48 85 C0                        test rax, rax
005EAE47  75 0E                           jne 0x1405eae57
005EAE49  41 8D 48 FF                     lea ecx, [r8 - 1]
005EAE4D  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
005EAE52  E9 6F 01 00 00                  jmp 0x1405eafc6
005EAE57  48 8B D0                        mov rdx, rax
005EAE5A  EB DC                           jmp 0x1405eae38
005EAE5C  8A 46 0A                        mov al, byte ptr [rsi + 0xa]
005EAE5F  24 F0                           and al, 0xf0
005EAE61  88 46 0A                        mov byte ptr [rsi + 0xa], al
005EAE64  44 88 66 0F                     mov byte ptr [rsi + 0xf], r12b
005EAE68  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
005EAE6B  A8 40                           test al, 0x40
005EAE6D  74 74                           je 0x1405eaee3
005EAE6F  49 8B D7                        mov rdx, r15
005EAE72  48 C1 E2 04                     shl rdx, 4
005EAE76  48 83 EA 20                     sub rdx, 0x20
005EAE7A  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
005EAE7F  4C 8D 46 20                     lea r8, [rsi + 0x20]
005EAE83  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
005EAE88  48 C1 EA 02                     shr rdx, 2
005EAE8C  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
005EAE91  48 85 D2                        test rdx, rdx
005EAE94  74 45                           je 0x1405eaedb
005EAE96  41 F6 C0 04                     test r8b, 4
005EAE9A  74 1B                           je 0x1405eaeb7
005EAE9C  41 C7 00 EE FE EE FE            mov dword ptr [r8], 0xfeeefeee
005EAEA3  48 83 EA 01                     sub rdx, 1
005EAEA7  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
005EAEAC  74 2D                           je 0x1405eaedb
005EAEAE  49 83 C0 04                     add r8, 4
005EAEB2  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
005EAEB7  48 8B CA                        mov rcx, rdx
005EAEBA  48 D1 E9                        shr rcx, 1
005EAEBD  48 B8 EE FE EE FE EE FE EE FE   movabs rax, 0xfeeefeeefeeefeee
005EAEC7  49 8B F8                        mov rdi, r8
005EAECA  F3 48 AB                        rep stosq qword ptr [rdi], rax
005EAECD  F6 C2 01                        test dl, 1
005EAED0  74 09                           je 0x1405eaedb
005EAED2  41 C7 44 90 FC EE FE EE FE      mov dword ptr [r8 + rdx*4 - 4], 0xfeeefeee
005EAEDB  8A 46 0A                        mov al, byte ptr [rsi + 0xa]
005EAEDE  0C 04                           or al, 4
005EAEE0  88 46 0A                        mov byte ptr [rsi + 0xa], al
005EAEE3  48 8D BB 50 01 00 00            lea rdi, [rbx + 0x150]
005EAEEA  4C 39 A3 38 01 00 00            cmp qword ptr [rbx + 0x138], r12
005EAEF1  74 10                           je 0x1405eaf03
005EAEF3  49 8B D7                        mov rdx, r15
005EAEF6  48 8B CB                        mov rcx, rbx
005EAEF9  E8 B6 68 00 00                  call 0x1405f17b4
005EAEFE  4C 8B C0                        mov r8, rax
005EAF01  EB 03                           jmp 0x1405eaf06
005EAF03  4C 8B 07                        mov r8, qword ptr [rdi]
005EAF06  49 3B F8                        cmp rdi, r8
005EAF09  74 43                           je 0x1405eaf4e
005EAF0B  44 39 63 7C                     cmp dword ptr [rbx + 0x7c], r12d
005EAF0F  74 2B                           je 0x1405eaf3c
005EAF11  41 8B 48 F8                     mov ecx, dword ptr [r8 - 8]
005EAF15  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
005EAF19  85 4B 7C                        test dword ptr [rbx + 0x7c], ecx
005EAF1C  74 0A                           je 0x1405eaf28
005EAF1E  33 8B 88 00 00 00               xor ecx, dword ptr [rbx + 0x88]
005EAF24  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
005EAF28  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
005EAF2D  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
005EAF35  44 8A 74 24 30                  mov r14b, byte ptr [rsp + 0x30]
005EAF3A  EB 05                           jmp 0x1405eaf41
005EAF3C  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
005EAF41  0F B7 C0                        movzx eax, ax
005EAF44  4C 3B F8                        cmp r15, rax
005EAF47  76 05                           jbe 0x1405eaf4e
005EAF49  4D 8B 00                        mov r8, qword ptr [r8]
005EAF4C  EB B8                           jmp 0x1405eaf06
005EAF4E  48 8D 7E 10                     lea rdi, [rsi + 0x10]
005EAF52  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005EAF56  48 8B 08                        mov rcx, qword ptr [rax]
005EAF59  49 3B C8                        cmp rcx, r8
005EAF5C  75 10                           jne 0x1405eaf6e
005EAF5E  4C 89 07                        mov qword ptr [rdi], r8
005EAF61  48 89 47 08                     mov qword ptr [rdi + 8], rax
005EAF65  48 89 38                        mov qword ptr [rax], rdi
005EAF68  49 89 78 08                     mov qword ptr [r8 + 8], rdi
005EAF6C  EB 17                           jmp 0x1405eaf85
005EAF6E  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
005EAF73  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005EAF78  45 33 C9                        xor r9d, r9d
005EAF7B  33 D2                           xor edx, edx
005EAF7D  8D 4A 0D                        lea ecx, [rdx + 0xd]
005EAF80  E8 37 08 D7 FF                  call 0x14035b7bc
005EAF85  0F B7 46 08                     movzx eax, word ptr [rsi + 8]
005EAF89  48 03 83 C0 00 00 00            add rax, qword ptr [rbx + 0xc0]
005EAF90  48 89 83 C0 00 00 00            mov qword ptr [rbx + 0xc0], rax
005EAF97  48 8B 93 38 01 00 00            mov rdx, qword ptr [rbx + 0x138]
005EAF9E  48 85 D2                        test rdx, rdx
005EAFA1  74 3B                           je 0x1405eafde
005EAFA3  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
005EAFA8  0F B7 4E 08                     movzx ecx, word ptr [rsi + 8]
005EAFAC  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
005EAFB0  49 3B C8                        cmp rcx, r8
005EAFB3  72 0C                           jb 0x1405eafc1
005EAFB5  48 8B 02                        mov rax, qword ptr [rdx]
005EAFB8  48 85 C0                        test rax, rax
005EAFBB  75 43                           jne 0x1405eb000
005EAFBD  41 8D 48 FF                     lea ecx, [r8 - 1]
005EAFC1  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
005EAFC6  0F B7 46 08                     movzx eax, word ptr [rsi + 8]
005EAFCA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005EAFCF  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005EAFD3  4C 8B CF                        mov r9, rdi
005EAFD6  48 8B CB                        mov rcx, rbx
005EAFD9  E8 EA 68 00 00                  call 0x1405f18c8
005EAFDE  44 39 63 7C                     cmp dword ptr [rbx + 0x7c], r12d
005EAFE2  74 2C                           je 0x1405eb010
005EAFE4  8A 4E 0A                        mov cl, byte ptr [rsi + 0xa]
005EAFE7  32 4E 09                        xor cl, byte ptr [rsi + 9]
005EAFEA  32 4E 08                        xor cl, byte ptr [rsi + 8]
005EAFED  88 4E 0B                        mov byte ptr [rsi + 0xb], cl
005EAFF0  8B 46 08                        mov eax, dword ptr [rsi + 8]
005EAFF3  8B 8B 88 00 00 00               mov ecx, dword ptr [rbx + 0x88]
005EAFF9  33 C8                           xor ecx, eax
005EAFFB  89 4E 08                        mov dword ptr [rsi + 8], ecx
005EAFFE  EB 10                           jmp 0x1405eb010
005EB000  48 8B D0                        mov rdx, rax
005EB003  EB A7                           jmp 0x1405eafac
005EB005  48 8B D6                        mov rdx, rsi
005EB008  48 8B CB                        mov rcx, rbx
005EB00B  E8 B0 04 00 00                  call 0x1405eb4c0
005EB010  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
005EB018  E9 BE 00 00 00                  jmp 0x1405eb0db
005EB01D  4C 8D 47 D0                     lea r8, [rdi - 0x30]
005EB021  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
005EB026  49 8B 48 20                     mov rcx, qword ptr [r8 + 0x20]
005EB02A  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
005EB02F  49 8B C0                        mov rax, r8
005EB032  48 25 00 00 FF FF               and rax, 0xffffffffffff0000
005EB038  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005EB03D  48 8B 83 58 02 00 00            mov rax, qword ptr [rbx + 0x258]
005EB044  48 2B C1                        sub rax, rcx
005EB047  48 89 83 58 02 00 00            mov qword ptr [rbx + 0x258], rax
005EB04E  48 8B 8B 50 02 00 00            mov rcx, qword ptr [rbx + 0x250]
005EB055  49 2B 48 28                     sub rcx, qword ptr [r8 + 0x28]
005EB059  48 89 8B 50 02 00 00            mov qword ptr [rbx + 0x250], rcx
005EB060  49 8B 00                        mov rax, qword ptr [r8]
005EB063  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
005EB067  48 8B 11                        mov rdx, qword ptr [rcx]
005EB06A  4C 8B 48 08                     mov r9, qword ptr [rax + 8]
005EB06E  49 3B D1                        cmp rdx, r9
005EB071  75 0E                           jne 0x1405eb081
005EB073  49 3B D0                        cmp rdx, r8
005EB076  75 09                           jne 0x1405eb081
005EB078  48 89 01                        mov qword ptr [rcx], rax
005EB07B  48 89 48 08                     mov qword ptr [rax + 8], rcx
005EB07F  EB 14                           jmp 0x1405eb095
005EB081  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
005EB086  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
005EB08B  33 D2                           xor edx, edx
005EB08D  8D 4A 0D                        lea ecx, [rdx + 0xd]
005EB090  E8 27 07 D7 FF                  call 0x14035b7bc
005EB095  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
005EB09D  45 84 F6                        test r14b, r14b
005EB0A0  74 14                           je 0x1405eb0b6
005EB0A2  48 8B 8B 60 01 00 00            mov rcx, qword ptr [rbx + 0x160]
005EB0A9  E8 62 49 C7 FF                  call 0x14025fa10
005EB0AE  45 8A F4                        mov r14b, r12b
005EB0B1  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
005EB0B6  4C 89 A4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r12
005EB0BE  41 B9 00 80 00 00               mov r9d, 0x8000
005EB0C4  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
005EB0CC  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
005EB0D1  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005EB0D5  E8 B6 23 0C 00                  call 0x1406ad490
005EB0DA  90                              nop
005EB0DB  45 84 F6                        test r14b, r14b
005EB0DE  74 0C                           je 0x1405eb0ec
005EB0E0  48 8B 8B 60 01 00 00            mov rcx, qword ptr [rbx + 0x160]
005EB0E7  E8 24 49 C7 FF                  call 0x14025fa10
005EB0EC  B8 01 00 00 00                  mov eax, 1
005EB0F1  E9 24 FB FF FF                  jmp 0x1405eac1a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpFreeHeap(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p68;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp + 32) = 0;
    *(unsigned __int8 *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    if (a1 != a3) goto loc_005EAC33;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m88 = 0;
    a4 = 0;
    result = RtlpLogHeapFailure(v_r12 + 9, a1, a3, a4);
    result = 0;
loc_005EAC1A:
    v_rsp = (v_rsp) + (128);
    return result;
loc_005EAC33:
    a2 = (unsigned int)((a1) | (*(unsigned int *)(v_r12 + 9 + 116)));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (0x3C010F60ULL));
    if ((((unsigned __int8)(a2)) & (1)) != 0) goto loc_005EACA3;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_r12 + 9 + 352), 1, a3, a4);
    v_stack_p30 = 1;
    if ((*(unsigned int *)(v_stack_p10 + 124)) == 0) goto loc_005EAC86;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 136))) ^ (*(unsigned int *)(a3 + 8)));
    *(unsigned int *)(a3 + 8) = (unsigned int)(a1);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a3 + 10)) ^ (*(unsigned __int8 *)(a3 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(a3 + 8)));
    if ((*(unsigned __int8 *)(a3 + 11)) != ((unsigned __int8)(a1))) {
        a2 = a3;
        a1 = v_stack_p10;
        result = RtlpAnalyzeHeapFailure(a1, a2, a3, a4);
    }
loc_005EAC91:
    if ((*(unsigned __int16 *)(a3 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)))) goto loc_005EACD4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 312)) == 0) goto loc_005EACD4;
    goto loc_005EAC91;
loc_005EACA3:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 312)) + 124)) == 0) goto loc_005EACD4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 312)) + 136))) ^ (*(unsigned int *)(a3 + 8)));
    *(unsigned int *)(a3 + 8) = (unsigned int)(a1);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a3 + 10)) ^ (*(unsigned __int8 *)(a3 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(a3 + 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8));
    if ((*(unsigned __int8 *)(a3 + 11)) != ((unsigned __int8)(a1))) {
        a2 = a3;
        a1 = v_stack_p10;
        result = RtlpAnalyzeHeapFailure(a1, a2, a3, a4);
    }
    result = *(unsigned __int8 *)(a3 + 10);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3 + 10))) & (8)) != 0) {
        result = (unsigned __int8)((*(unsigned __int8 *)(a3 + 10)) & (247));
        *(unsigned __int8 *)(a3 + 10) = (unsigned __int8)(result);
    }
    if ((*(unsigned __int8 *)(a3 + 15)) == 4) goto loc_005EB01D;
    v_stack_pC8 = *(unsigned __int16 *)(a3 + 8);
    result = RtlpCoalesceFreeBlocks(v_stack_p10, a3, v_stack_pC8, a4);
    v_stack_pC0 = result;
    if (v_stack_pC8 < (*(unsigned __int64 *)(v_stack_p10 + 176))) goto loc_005EAD49;
    if ((v_stack_pC8 + *(unsigned __int64 *)(v_stack_p10 + 192) * 1) < (*(unsigned __int64 *)(v_stack_p10 + 184))) goto loc_005EAD49;
    result = RtlpDeCommitFreeBlock(v_stack_p10, result, v_stack_pC8, a4);
    goto loc_005EB010;
loc_005EAD49:
    if (v_stack_pC8 > 0xFF00ULL) goto loc_005EB005;
    if ((unsigned int)(v_r15) != 0) goto loc_005EAE5C;
    *(unsigned __int8 *)(result + 10) = 0;
    *(unsigned __int8 *)(result + 15) = 0;
    if ((*(unsigned __int64 *)(v_stack_p10 + 312)) == 0) goto loc_005EAD8B;
    result = RtlpFindEntry(v_stack_p10, (unsigned int)((unsigned int)((unsigned __int16)(v_stack_pC8))), v_stack_pC8, a4);
    goto loc_005EAD8E;
loc_005EAD8B:
loc_005EAD8E:
    if ((v_stack_p10 + 336) == (*(unsigned __int64 *)(v_stack_p10 + 336))) goto loc_005EADD6;
    if ((*(unsigned int *)(v_stack_p10 + 124)) == 0) goto loc_005EADC4;
    v_stack_p68 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8));
    if (((*(unsigned int *)(v_stack_p10 + 124)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8))) ^ (*(unsigned int *)(v_stack_p10 + 136)));
        v_stack_p68 = (unsigned int)(result);
    }
    goto loc_005EADC9;
loc_005EADC4:
loc_005EADC9:
    if (((unsigned __int16)(v_stack_pC8)) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8)))) goto loc_005EADD6;
    goto loc_005EAD8E;
loc_005EADD6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)))) goto loc_005EADF6;
    *(unsigned __int64 *)(v_stack_pC0 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336));
    *(unsigned __int64 *)(v_stack_pC0 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8)) = v_stack_pC0 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8) = v_stack_pC0 + 16;
    goto loc_005EAE0D;
loc_005EADF6:
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8));
    a4 = 0;
    a2 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)), a4);
loc_005EAE0D:
    result = (*(unsigned __int16 *)(v_stack_pC0 + 8)) + (*(unsigned __int64 *)(v_stack_p10 + 192));
    *(unsigned __int64 *)(v_stack_p10 + 192) = result;
    if (*(unsigned __int64 *)(v_stack_p10 + 312) == 0) goto loc_005EAFDE;
    v_stack_p38 = 0;
loc_005EAE38:
    if ((*(unsigned __int16 *)(v_stack_pC0 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)))) goto loc_005EAE4D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 312)) != 0) goto loc_005EAE57;
loc_005EAE4D:
    v_stack_p38 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)) - 1;
    goto loc_005EAFC6;
loc_005EAE57:
    goto loc_005EAE38;
loc_005EAE5C:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_pC0 + 10)) & (240));
    *(unsigned __int8 *)(v_stack_pC0 + 10) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_stack_pC0 + 15) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 112)))) & (64)) == 0) goto loc_005EAEE3;
    a2 = ((unsigned __int16)(v_stack_pC8)) << (4);
    a2 = (a2) - (32);
    v_stack_p40 = a2;
    v_stack_p58 = v_stack_pC0 + 32;
    a2 = (a2) >> (2);
    v_stack_p40 = a2;
    if (a2 == 0) goto loc_005EAEDB;
    if ((((unsigned __int8)(v_stack_pC0 + 32)) & (4)) == 0) goto loc_005EAEB7;
    *(unsigned int *)(v_stack_pC0 + 32) = 0xFEEEFEEEULL;
    a2 = (a2) - (1);
    v_stack_p40 = a2;
    if (condition_is_equal) goto loc_005EAEDB;
    a3 = (v_stack_pC0 + 32) + (4);
    v_stack_p58 = a3;
loc_005EAEB7:
    a1 = (a2) >> (1);
    if ((((unsigned __int8)(a2)) & (1)) != 0) {
        *(unsigned int *)(a3 + a2 * 4 - 4) = 0xFEEEFEEEULL;
    }
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_pC0 + 10)) | (4));
    *(unsigned __int8 *)(v_stack_pC0 + 10) = (unsigned __int8)(result);
loc_005EAEE3:
    if ((*(unsigned __int64 *)(v_stack_p10 + 312)) == 0) goto loc_005EAF03;
    result = RtlpFindEntry(v_stack_p10, (unsigned __int16)(v_stack_pC8), a3, a4);
    goto loc_005EAF06;
loc_005EAF03:
loc_005EAF06:
    if ((v_stack_p10 + 336) == (*(unsigned __int64 *)(v_stack_p10 + 336))) goto loc_005EAF4E;
    if ((*(unsigned int *)(v_stack_p10 + 124)) == 0) goto loc_005EAF3C;
    v_stack_p78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8)));
    if (((*(unsigned int *)(v_stack_p10 + 124)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8))))) != 0) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8))) ^ (*(unsigned int *)(v_stack_p10 + 136)));
        v_stack_p78 = (unsigned int)(a1);
    }
    goto loc_005EAF41;
loc_005EAF3C:
loc_005EAF41:
    if (((unsigned __int16)(v_stack_pC8)) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 336) - 8)))) goto loc_005EAF4E;
    goto loc_005EAF06;
loc_005EAF4E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)))) goto loc_005EAF6E;
    *(unsigned __int64 *)(v_stack_pC0 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336));
    *(unsigned __int64 *)(v_stack_pC0 + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8)) = v_stack_pC0 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8) = v_stack_pC0 + 16;
    goto loc_005EAF85;
loc_005EAF6E:
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)) + 8));
    a4 = 0;
    a2 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 336)), a4);
loc_005EAF85:
    result = (*(unsigned __int16 *)(v_stack_pC0 + 8)) + (*(unsigned __int64 *)(v_stack_p10 + 192));
    *(unsigned __int64 *)(v_stack_p10 + 192) = result;
    if (*(unsigned __int64 *)(v_stack_p10 + 312) == 0) goto loc_005EAFDE;
    v_stack_p48 = 0;
loc_005EAFAC:
    if ((*(unsigned __int16 *)(v_stack_pC0 + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)))) goto loc_005EAFC1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 312)) != 0) goto loc_005EB000;
loc_005EAFC1:
    v_stack_p48 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)) - 1;
loc_005EAFC6:
    v_stack_p28 = *(unsigned __int16 *)(v_stack_pC0 + 8);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)) - 1);
    result = RtlpHeapAddListEntry(v_stack_p10, *(unsigned __int64 *)(v_stack_p10 + 312), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)), v_stack_pC0 + 16);
loc_005EAFDE:
    if ((*(unsigned int *)(v_stack_p10 + 124)) == 0) goto loc_005EB010;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_pC0 + 10)) ^ (*(unsigned __int8 *)(v_stack_pC0 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_stack_pC0 + 8)));
    *(unsigned __int8 *)(v_stack_pC0 + 11) = (unsigned __int8)(a1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 136))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pC0 + 8)))));
    *(unsigned int *)(v_stack_pC0 + 8) = (unsigned int)(a1);
    goto loc_005EB010;
loc_005EB000:
    goto loc_005EAFAC;
loc_005EB005:
    result = RtlpInsertFreeBlock(v_stack_p10, v_stack_pC0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 312) + 8)), v_stack_pC0 + 16);
loc_005EB010:
    v_stack_pC0 = 0;
    goto loc_005EB0DB;
loc_005EB01D:
    v_stack_p48 = v_stack_pC0 + 16 - 48;
    v_stack_p50 = *(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 32);
    result = (v_stack_pC0 + 16 - 48) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_p50 = result;
    result = (*(unsigned __int64 *)(v_stack_p10 + 600)) - (*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 32));
    *(unsigned __int64 *)(v_stack_p10 + 600) = result;
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 592)) - (*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 40));
    *(unsigned __int64 *)(v_stack_p10 + 592) = a1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48) + 8))) goto loc_005EB081;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 8))) != (v_stack_pC0 + 16 - 48)) goto loc_005EB081;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 8)) = *(unsigned __int64 *)(v_stack_pC0 + 16 - 48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48) + 8) = *(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 8);
    goto loc_005EB095;
loc_005EB081:
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48 + 8));
    a2 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, v_stack_pC0 + 16 - 48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48) + 8));
loc_005EB095:
    v_stack_pC0 = 0;
    v_r14 = v_stack_p30;
    if ((unsigned __int8)(v_stack_p30) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p10 + 352);
        result = ExReleaseResourceLite(a1, a2, v_stack_pC0 + 16 - 48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pC0 + 16 - 48) + 8));
        v_r14 = 0;
        v_stack_p30 = 0;
    }
    v_stack_pC8 = 0;
    a1 = (a1) | (-1);
    result = ZwFreeVirtualMemory(a1, v_stack_p50, v_stack_pC8, (unsigned int)(0x8000ULL));
loc_005EB0DB:
    if ((unsigned __int8)(v_r14) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p10 + 352);
        result = ExReleaseResourceLite(a1, v_stack_p50, v_stack_pC8, (unsigned int)(0x8000ULL));
    }
    goto loc_005EAC1A;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpFreeHeap(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p68;
    uint32_t v_stack_p78;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r12 = 0;
    *(uint64_t *)(local_rsp + 0x20) = 0;
    *(uint8_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    if (Arg1 != Arg3) goto loc_005EAC33;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m88 = 0;
    Arg4 = 0;
    result = RtlpLogHeapFailure(local_r12 + 9, Arg1, Arg3, Arg4);
    result = 0;
loc_005EAC1A:
    local_rsp = (local_rsp) + (128);
    return result;
loc_005EAC33:
    Arg2 = (uint32_t)((Arg1) | (*(uint32_t *)(local_r12 + 0x9 + 0x74)));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (0x3C010F60ULL));
    if ((((uint8_t)(Arg2)) & (1)) != 0) goto loc_005EACA3;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(local_r12 + 0x9 + 0x160), 1, Arg3, Arg4);
    v_stack_p30 = 1;
    if ((*(uint32_t *)(v_stack_p10 + 0x7C)) == 0) goto loc_005EAC86;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x88))) ^ (*(uint32_t *)(arg3 + 0x8)));
    *(uint32_t *)(arg3 + 0x8) = (uint32_t)(Arg1);
    Arg1 = (uint8_t)((*(uint8_t *)(arg3 + 0xA)) ^ (*(uint8_t *)(arg3 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(arg3 + 0x8)));
    if ((*(uint8_t *)(arg3 + 0xB)) != ((uint8_t)(Arg1))) {
        Arg2 = Arg3;
        Arg1 = v_stack_p10;
        result = RtlpAnalyzeHeapFailure(Arg1, Arg2, Arg3, Arg4);
    }
loc_005EAC91:
    if ((*(uint16_t *)(arg3 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)))) goto loc_005EACD4;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x138)) == 0) goto loc_005EACD4;
    goto loc_005EAC91;
loc_005EACA3:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x138)) + 0x7C)) == 0) goto loc_005EACD4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x138)) + 0x88))) ^ (*(uint32_t *)(arg3 + 0x8)));
    *(uint32_t *)(arg3 + 0x8) = (uint32_t)(Arg1);
    Arg1 = (uint8_t)((*(uint8_t *)(arg3 + 0xA)) ^ (*(uint8_t *)(arg3 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(arg3 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8));
    if ((*(uint8_t *)(arg3 + 0xB)) != ((uint8_t)(Arg1))) {
        Arg2 = Arg3;
        Arg1 = v_stack_p10;
        result = RtlpAnalyzeHeapFailure(Arg1, Arg2, Arg3, Arg4);
    }
    result = *(uint8_t *)(arg3 + 0xA);
    if ((((uint8_t)(*(uint8_t *)(arg3 + 0xA))) & (8)) != 0) {
        result = (uint8_t)((*(uint8_t *)(arg3 + 0xA)) & (247));
        *(uint8_t *)(arg3 + 0xA) = (uint8_t)(result);
    }
    if ((*(uint8_t *)(arg3 + 0xF)) == 4) goto loc_005EB01D;
    v_stack_pC8 = *(uint16_t *)(arg3 + 0x8);
    result = RtlpCoalesceFreeBlocks(v_stack_p10, Arg3, v_stack_pC8, Arg4);
    v_stack_pC0 = result;
    if (v_stack_pC8 < (*(uint64_t *)(v_stack_p10 + 0xB0))) goto loc_005EAD49;
    if ((v_stack_pC8 + *(uint64_t *)(v_stack_p10 + 0xC0) * 1) < (*(uint64_t *)(v_stack_p10 + 0xB8))) goto loc_005EAD49;
    result = RtlpDeCommitFreeBlock(v_stack_p10, result, v_stack_pC8, Arg4);
    goto loc_005EB010;
loc_005EAD49:
    if (v_stack_pC8 > 0xFF00ULL) goto loc_005EB005;
    if ((uint32_t)(local_r15) != 0) goto loc_005EAE5C;
    *(uint8_t *)(result + 0xA) = 0;
    *(uint8_t *)(result + 0xF) = 0;
    if ((*(uint64_t *)(v_stack_p10 + 0x138)) == 0) goto loc_005EAD8B;
    result = RtlpFindEntry(v_stack_p10, (uint32_t)((uint32_t)((uint16_t)(v_stack_pC8))), v_stack_pC8, Arg4);
    goto loc_005EAD8E;
loc_005EAD8B:
loc_005EAD8E:
    if ((v_stack_p10 + 336) == (*(uint64_t *)(v_stack_p10 + 0x150))) goto loc_005EADD6;
    if ((*(uint32_t *)(v_stack_p10 + 0x7C)) == 0) goto loc_005EADC4;
    v_stack_p68 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8));
    if (((*(uint32_t *)(v_stack_p10 + 0x7C)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8))) ^ (*(uint32_t *)(v_stack_p10 + 0x88)));
        v_stack_p68 = (uint32_t)(result);
    }
    goto loc_005EADC9;
loc_005EADC4:
loc_005EADC9:
    if (((uint16_t)(v_stack_pC8)) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8)))) goto loc_005EADD6;
    goto loc_005EAD8E;
loc_005EADD6:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)))) goto loc_005EADF6;
    *(uint64_t *)(v_stack_pC0 + 0x10) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150));
    *(uint64_t *)(v_stack_pC0 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8)) = v_stack_pC0 + 16;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8) = v_stack_pC0 + 16;
    goto loc_005EAE0D;
loc_005EADF6:
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8));
    Arg4 = 0;
    Arg2 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)), Arg4);
loc_005EAE0D:
    result = (*(uint16_t *)(v_stack_pC0 + 0x8)) + (*(uint64_t *)(v_stack_p10 + 0xC0));
    *(uint64_t *)(v_stack_p10 + 0xC0) = result;
    if (*(uint64_t *)(v_stack_p10 + 0x138) == 0) goto loc_005EAFDE;
    v_stack_p38 = 0;
loc_005EAE38:
    if ((*(uint16_t *)(v_stack_pC0 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)))) goto loc_005EAE4D;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x138)) != 0) goto loc_005EAE57;
loc_005EAE4D:
    v_stack_p38 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)) - 1;
    goto loc_005EAFC6;
loc_005EAE57:
    goto loc_005EAE38;
loc_005EAE5C:
    result = (uint8_t)((*(uint8_t *)(v_stack_pC0 + 0xA)) & (240));
    *(uint8_t *)(v_stack_pC0 + 0xA) = (uint8_t)(result);
    *(uint8_t *)(v_stack_pC0 + 0xF) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x70)))) & (64)) == 0) goto loc_005EAEE3;
    Arg2 = ((uint16_t)(v_stack_pC8)) << (4);
    Arg2 = (Arg2) - (32);
    v_stack_p40 = Arg2;
    v_stack_p58 = v_stack_pC0 + 32;
    Arg2 = (Arg2) >> (2);
    v_stack_p40 = Arg2;
    if (Arg2 == 0) goto loc_005EAEDB;
    if ((((uint8_t)(v_stack_pC0 + 32)) & (4)) == 0) goto loc_005EAEB7;
    *(uint32_t *)(v_stack_pC0 + 0x20) = 0xFEEEFEEEULL;
    Arg2 = (Arg2) - (1);
    v_stack_p40 = Arg2;
    if (condition_is_equal) goto loc_005EAEDB;
    Arg3 = (v_stack_pC0 + 32) + (4);
    v_stack_p58 = Arg3;
loc_005EAEB7:
    Arg1 = (Arg2) >> (1);
    if ((((uint8_t)(Arg2)) & (1)) != 0) {
        *(uint32_t *)(arg3 + Arg2 * 4 - 0x4) = 0xFEEEFEEEULL;
    }
    result = (uint8_t)((*(uint8_t *)(v_stack_pC0 + 0xA)) | (4));
    *(uint8_t *)(v_stack_pC0 + 0xA) = (uint8_t)(result);
loc_005EAEE3:
    if ((*(uint64_t *)(v_stack_p10 + 0x138)) == 0) goto loc_005EAF03;
    result = RtlpFindEntry(v_stack_p10, (uint16_t)(v_stack_pC8), Arg3, Arg4);
    goto loc_005EAF06;
loc_005EAF03:
loc_005EAF06:
    if ((v_stack_p10 + 336) == (*(uint64_t *)(v_stack_p10 + 0x150))) goto loc_005EAF4E;
    if ((*(uint32_t *)(v_stack_p10 + 0x7C)) == 0) goto loc_005EAF3C;
    v_stack_p78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8)));
    if (((*(uint32_t *)(v_stack_p10 + 0x7C)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8))))) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8))) ^ (*(uint32_t *)(v_stack_p10 + 0x88)));
        v_stack_p78 = (uint32_t)(Arg1);
    }
    goto loc_005EAF41;
loc_005EAF3C:
loc_005EAF41:
    if (((uint16_t)(v_stack_pC8)) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x150) - 0x8)))) goto loc_005EAF4E;
    goto loc_005EAF06;
loc_005EAF4E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)))) goto loc_005EAF6E;
    *(uint64_t *)(v_stack_pC0 + 0x10) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150));
    *(uint64_t *)(v_stack_pC0 + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8)) = v_stack_pC0 + 16;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8) = v_stack_pC0 + 16;
    goto loc_005EAF85;
loc_005EAF6E:
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)) + 0x8));
    Arg4 = 0;
    Arg2 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x150)), Arg4);
loc_005EAF85:
    result = (*(uint16_t *)(v_stack_pC0 + 0x8)) + (*(uint64_t *)(v_stack_p10 + 0xC0));
    *(uint64_t *)(v_stack_p10 + 0xC0) = result;
    if (*(uint64_t *)(v_stack_p10 + 0x138) == 0) goto loc_005EAFDE;
    v_stack_p48 = 0;
loc_005EAFAC:
    if ((*(uint16_t *)(v_stack_pC0 + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)))) goto loc_005EAFC1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x138)) != 0) goto loc_005EB000;
loc_005EAFC1:
    v_stack_p48 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)) - 1;
loc_005EAFC6:
    v_stack_p28 = *(uint16_t *)(v_stack_pC0 + 0x8);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)) - 1);
    result = RtlpHeapAddListEntry(v_stack_p10, *(uint64_t *)(v_stack_p10 + 0x138), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)), v_stack_pC0 + 16);
loc_005EAFDE:
    if ((*(uint32_t *)(v_stack_p10 + 0x7C)) == 0) goto loc_005EB010;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_pC0 + 0xA)) ^ (*(uint8_t *)(v_stack_pC0 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_stack_pC0 + 0x8)));
    *(uint8_t *)(v_stack_pC0 + 0xB) = (uint8_t)(Arg1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x88))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pC0 + 0x8)))));
    *(uint32_t *)(v_stack_pC0 + 0x8) = (uint32_t)(Arg1);
    goto loc_005EB010;
loc_005EB000:
    goto loc_005EAFAC;
loc_005EB005:
    result = RtlpInsertFreeBlock(v_stack_p10, v_stack_pC0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x138) + 0x8)), v_stack_pC0 + 16);
loc_005EB010:
    v_stack_pC0 = 0;
    goto loc_005EB0DB;
loc_005EB01D:
    v_stack_p48 = v_stack_pC0 + 16 - 48;
    v_stack_p50 = *(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x20);
    result = (v_stack_pC0 + 16 - 48) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_p50 = result;
    result = (*(uint64_t *)(v_stack_p10 + 0x258)) - (*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x20));
    *(uint64_t *)(v_stack_p10 + 0x258) = result;
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x250)) - (*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x28));
    *(void **)(v_stack_p10 + 0x250) = Arg1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30) + 0x8))) goto loc_005EB081;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x8))) != (v_stack_pC0 + 16 - 48)) goto loc_005EB081;
    *(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x8)) = *(uint64_t *)(v_stack_pC0 + 0x10 - 0x30);
    *(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30) + 0x8) = *(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x8);
    goto loc_005EB095;
loc_005EB081:
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30 + 0x8));
    Arg2 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, v_stack_pC0 + 16 - 48, *(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30) + 0x8));
loc_005EB095:
    v_stack_pC0 = 0;
    local_r14 = v_stack_p30;
    if ((uint8_t)(v_stack_p30) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p10 + 0x160);
        result = ExReleaseResourceLite(Arg1, Arg2, v_stack_pC0 + 16 - 48, *(uint64_t *)(*(uint64_t *)(v_stack_pC0 + 0x10 - 0x30) + 0x8));
        local_r14 = 0;
        v_stack_p30 = 0;
    }
    v_stack_pC8 = 0;
    Arg1 = (Arg1) | (-1);
    result = ZwFreeVirtualMemory(Arg1, v_stack_p50, v_stack_pC8, (uint32_t)(0x8000ULL));
loc_005EB0DB:
    if ((uint8_t)(local_r14) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p10 + 0x160);
        result = ExReleaseResourceLite(Arg1, v_stack_p50, v_stack_pC8, (uint32_t)(0x8000ULL));
    }
    goto loc_005EAC1A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `W` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |
| `Arg1` | `+ 0x250` | `64` | `R` |
| `Arg1` | `+ 0x250` | `64` | `W` |
| `Arg1` | `+ 0x258` | `64` | `R` |
| `Arg1` | `+ 0x258` | `64` | `W` |
| `Arg3` | `- 0x30` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `8` | `R` |
| `Arg3` | `+ 0x8` | `16` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x8` | `32` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x9` | `8` | `R` |
| `Arg3` | `+ 0xA` | `8` | `R` |
| `Arg3` | `+ 0xA` | `8` | `W` |
| `Arg3` | `+ 0xB` | `8` | `R` |
| `Arg3` | `+ 0xF` | `8` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EABC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
