# sub_0026A9FF

- RVA: `0x0026A9FF`–`0x0026B86F` (길이 `3,696` bytes)
- VA: `0x000000014026A9FF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000654A4`
- 디코드: `902`개 명령, `3,696/3,696` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0026ABB0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026ADC0` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0026B02A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026B4B6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026B7AE` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026B810` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026B84A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **14**
  - `0x0026AA11` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026AB46` → [sub_0026B87F](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026ADC9` → [sub_0026A4AD + 0x190](Unknown_function_0026A4AD.md) (`tail-transfer`)
  - `0x0026AE50` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026AF95` → [sub_0026B87F + 0x45](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026AFA1` → [sub_0026B87F + 0x45](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026AFF2` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B11C` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B275` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B31B` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B442` → [sub_0026B87F + 0xD](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B44E` → [sub_0026B87F + 0xD](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B75C` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)
  - `0x0026B76C` → [sub_0026B87F + 0x56](Unknown_function_0026B87F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0026A9FF  81 FB 0B 00 01 00               cmp ebx, 0x1000b
0026AA05  0F 8D 0A 09 00 00               jge 0x14026b315
0026AA0B  81 FB 00 00 00 7E               cmp ebx, 0x7e000000
0026AA11  0F 87 BE 0E 00 00               ja 0x14026b8d5
0026AA17  85 DB                           test ebx, ebx
0026AA19  0F 84 43 0D 00 00               je 0x14026b762
0026AA1F  8B 97 10 40 00 00               mov edx, dword ptr [rdi + 0x4010]
0026AA25  4D 8B CA                        mov r9, r10
0026AA28  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
0026AA30  4C 2B CA                        sub r9, rdx
0026AA33  48 83 BF 00 40 00 00 00         cmp qword ptr [rdi + 0x4000], 0
0026AA3B  49 8B EA                        mov rbp, r10
0026AA3E  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
0026AA46  49 8D 3C 1A                     lea rdi, [r10 + rbx]
0026AA4A  4C 8D 67 F5                     lea r12, [rdi - 0xb]
0026AA4E  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0026AA53  41 01 9E 18 40 00 00            add dword ptr [r14 + 0x4018], ebx
0026AA5A  8D 04 1A                        lea eax, [rdx + rbx]
0026AA5D  41 89 86 10 40 00 00            mov dword ptr [r14 + 0x4010], eax
0026AA64  4D 8B EC                        mov r13, r12
0026AA67  41 C7 86 14 40 00 00 03 00 00 00  mov dword ptr [r14 + 0x4014], 3
0026AA72  4C 8D 7F FB                     lea r15, [rdi - 5]
0026AA76  83 FB 0D                        cmp ebx, 0xd
0026AA79  0F 8C 0D 03 00 00               jl 0x14026ad8c
0026AA7F  41 69 0A B1 79 37 9E            imul ecx, dword ptr [r10], 0x9e3779b1
0026AA86  41 8B DB                        mov ebx, r11d
0026AA89  48 C1 E9 13                     shr rcx, 0x13
0026AA8D  66 41 89 14 4E                  mov word ptr [r14 + rcx*2], dx
0026AA92  41 69 4A 01 B1 79 37 9E         imul ecx, dword ptr [r10 + 1], 0x9e3779b1
0026AA9A  49 8D 52 01                     lea rdx, [r10 + 1]
0026AA9E  89 9C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ebx
0026AAA5  41 B8 01 00 00 00               mov r8d, 1
0026AAAB  C7 84 24 D8 00 00 00 40 00 00 00  mov dword ptr [rsp + 0xd8], 0x40
0026AAB6  C1 E9 13                        shr ecx, 0x13
0026AAB9  8B C2                           mov eax, edx
0026AABB  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0026AAC0  2B 44 24 28                     sub eax, dword ptr [rsp + 0x28]
0026AAC4  4C 8B D2                        mov r10, rdx
0026AAC7  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0026AACB  4D 8B F5                        mov r14, r13
0026AACE  8B C1                           mov eax, ecx
0026AAD0  4C 8B EF                        mov r13, rdi
0026AAD3  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0026AADB  48 8D 04 41                     lea rax, [rcx + rax*2]
0026AADF  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0026AAE6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0026AAEB  0F B7 00                        movzx eax, word ptr [rax]
0026AAEE  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0026AAF2  49 63 C0                        movsxd rax, r8d
0026AAF5  48 03 D0                        add rdx, rax
0026AAF8  8B C1                           mov eax, ecx
0026AAFA  C1 F8 06                        sar eax, 6
0026AAFD  FF C1                           inc ecx
0026AAFF  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
0026AB06  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
0026AB0D  49 3B D4                        cmp rdx, r12
0026AB10  0F 87 76 02 00 00               ja 0x14026ad8c
0026AB16  69 0A B1 79 37 9E               imul ecx, dword ptr [rdx], 0x9e3779b1
0026AB1C  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
0026AB21  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0026AB25  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
0026AB2A  4C 03 44 24 28                  add r8, qword ptr [rsp + 0x28]
0026AB2F  66 89 07                        mov word ptr [rdi], ax
0026AB32  49 8B FD                        mov rdi, r13
0026AB35  41 8B 02                        mov eax, dword ptr [r10]
0026AB38  4D 8B EE                        mov r13, r14
0026AB3B  C1 E9 13                        shr ecx, 0x13
0026AB3E  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0026AB43  41 39 00                        cmp dword ptr [r8], eax
0026AB46  0F 85 33 0D 00 00               jne 0x14026b87f
0026AB4C  48 8B D7                        mov rdx, rdi
0026AB4F  49 8B CC                        mov rcx, r12
0026AB52  4C 3B 84 24 C8 00 00 00         cmp r8, qword ptr [rsp + 0xc8]
0026AB5A  76 0F                           jbe 0x14026ab6b
0026AB5C  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026AB61  41 38 42 FF                     cmp byte ptr [r10 - 1], al
0026AB65  0F 84 9A 02 00 00               je 0x14026ae05
0026AB6B  41 8B CA                        mov ecx, r10d
0026AB6E  4C 8D 76 01                     lea r14, [rsi + 1]
0026AB72  2B CD                           sub ecx, ebp
0026AB74  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
0026AB7B  83 F9 0F                        cmp ecx, 0xf
0026AB7E  0F 82 74 02 00 00               jb 0x14026adf8
0026AB84  8D 51 F1                        lea edx, [rcx - 0xf]
0026AB87  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026AB8A  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
0026AB91  4D 8B CE                        mov r9, r14
0026AB94  81 FA FF 00 00 00               cmp edx, 0xff
0026AB9A  7C 4A                           jl 0x14026abe6
0026AB9C  B8 81 80 80 80                  mov eax, 0x80808081
0026ABA1  49 8B CE                        mov rcx, r14
0026ABA4  F7 E2                           mul edx
0026ABA6  C1 EA 07                        shr edx, 7
0026ABA9  8B DA                           mov ebx, edx
0026ABAB  44 8B C2                        mov r8d, edx
0026ABAE  B2 FF                           mov dl, 0xff
0026ABB0  E8 8B C0 45 00                  call 0x1406c6c40
0026ABB5  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
0026ABBC  4E 8D 0C 33                     lea r9, [rbx + r14]
0026ABC0  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
0026ABC7  4D 8B F1                        mov r14, r9
0026ABCA  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0026ABCF  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0026ABD4  69 C3 01 FF FF FF               imul eax, ebx, 0xffffff01
0026ABDA  8B 9C 24 E0 00 00 00            mov ebx, dword ptr [rsp + 0xe0]
0026ABE1  03 D0                           add edx, eax
0026ABE3  45 33 DB                        xor r11d, r11d
0026ABE6  41 88 16                        mov byte ptr [r14], dl
0026ABE9  4D 8D 71 01                     lea r14, [r9 + 1]
0026ABED  8B D1                           mov edx, ecx
0026ABEF  49 03 D6                        add rdx, r14
0026ABF2  49 2B EE                        sub rbp, r14
0026ABF5  49 8B 04 2E                     mov rax, qword ptr [r14 + rbp]
0026ABF9  49 89 06                        mov qword ptr [r14], rax
0026ABFC  49 83 C6 08                     add r14, 8
0026AC00  4C 3B F2                        cmp r14, rdx
0026AC03  72 F0                           jb 0x14026abf5
0026AC05  49 8D 6F F9                     lea rbp, [r15 - 7]
0026AC09  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0026AC0E  66 90                           nop
0026AC10  4D 8D 72 04                     lea r14, [r10 + 4]
0026AC14  41 0F B7 C2                     movzx eax, r10w
0026AC18  66 41 2B C0                     sub ax, r8w
0026AC1C  4C 8B CE                        mov r9, rsi
0026AC1F  66 89 02                        mov word ptr [rdx], ax
0026AC22  48 8D 72 02                     lea rsi, [rdx + 2]
0026AC26  49 8D 50 04                     lea rdx, [r8 + 4]
0026AC2A  49 8B CE                        mov rcx, r14
0026AC2D  4C 3B F5                        cmp r14, rbp
0026AC30  73 1B                           jae 0x14026ac4d
0026AC32  4D 8B 06                        mov r8, qword ptr [r14]
0026AC35  4C 33 02                        xor r8, qword ptr [rdx]
0026AC38  74 0B                           je 0x14026ac45
0026AC3A  F3 4D 0F BC C0                  tzcnt r8, r8
0026AC3F  41 C1 E8 03                     shr r8d, 3
0026AC43  EB 2E                           jmp 0x14026ac73
0026AC45  49 8D 4E 08                     lea rcx, [r14 + 8]
0026AC49  48 83 C2 08                     add rdx, 8
0026AC4D  48 3B 4C 24 30                  cmp rcx, qword ptr [rsp + 0x30]
0026AC52  0F 83 AB 00 00 00               jae 0x14026ad03
0026AC58  4C 8B 01                        mov r8, qword ptr [rcx]
0026AC5B  4C 33 02                        xor r8, qword ptr [rdx]
0026AC5E  0F 84 1F 01 00 00               je 0x14026ad83
0026AC64  F3 4D 0F BC C0                  tzcnt r8, r8
0026AC69  41 C1 E8 03                     shr r8d, 3
0026AC6D  45 2B C6                        sub r8d, r14d
0026AC70  44 03 C1                        add r8d, ecx
0026AC73  41 8B C0                        mov eax, r8d
0026AC76  49 83 C2 04                     add r10, 4
0026AC7A  4C 03 D0                        add r10, rax
0026AC7D  41 0F B6 01                     movzx eax, byte ptr [r9]
0026AC81  41 83 F8 0F                     cmp r8d, 0xf
0026AC85  0F 83 C2 00 00 00               jae 0x14026ad4d
0026AC8B  41 02 C0                        add al, r8b
0026AC8E  41 88 01                        mov byte ptr [r9], al
0026AC91  49 8B EA                        mov rbp, r10
0026AC94  4D 3B D5                        cmp r10, r13
0026AC97  0F 83 EF 00 00 00               jae 0x14026ad8c
0026AC9D  41 69 4A FE B1 79 37 9E         imul ecx, dword ptr [r10 - 2], 0x9e3779b1
0026ACA5  41 0F B7 D2                     movzx edx, r10w
0026ACA9  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0026ACAE  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
0026ACB6  66 41 2B D1                     sub dx, r9w
0026ACBA  66 83 EA 02                     sub dx, 2
0026ACBE  48 C1 E9 13                     shr rcx, 0x13
0026ACC2  66 41 89 14 48                  mov word ptr [r8 + rcx*2], dx
0026ACC7  41 8B D2                        mov edx, r10d
0026ACCA  41 69 02 B1 79 37 9E            imul eax, dword ptr [r10], 0x9e3779b1
0026ACD1  41 2B D1                        sub edx, r9d
0026ACD4  C1 E8 13                        shr eax, 0x13
0026ACD7  49 8D 0C 40                     lea rcx, [r8 + rax*2]
0026ACDB  45 0F B7 04 40                  movzx r8d, word ptr [r8 + rax*2]
0026ACE0  66 89 11                        mov word ptr [rcx], dx
0026ACE3  4D 03 C1                        add r8, r9
0026ACE6  41 8B 02                        mov eax, dword ptr [r10]
0026ACE9  41 39 00                        cmp dword ptr [r8], eax
0026ACEC  0F 85 A0 FD FF FF               jne 0x14026aa92
0026ACF2  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
0026ACF7  48 8D 56 01                     lea rdx, [rsi + 1]
0026ACFB  C6 06 00                        mov byte ptr [rsi], 0
0026ACFE  E9 0D FF FF FF                  jmp 0x14026ac10
0026AD03  49 8D 47 FD                     lea rax, [r15 - 3]
0026AD07  48 3B C8                        cmp rcx, rax
0026AD0A  73 0E                           jae 0x14026ad1a
0026AD0C  8B 01                           mov eax, dword ptr [rcx]
0026AD0E  39 02                           cmp dword ptr [rdx], eax
0026AD10  75 08                           jne 0x14026ad1a
0026AD12  48 83 C1 04                     add rcx, 4
0026AD16  48 83 C2 04                     add rdx, 4
0026AD1A  49 8D 47 FF                     lea rax, [r15 - 1]
0026AD1E  48 3B C8                        cmp rcx, rax
0026AD21  73 10                           jae 0x14026ad33
0026AD23  0F B7 01                        movzx eax, word ptr [rcx]
0026AD26  66 39 02                        cmp word ptr [rdx], ax
0026AD29  75 08                           jne 0x14026ad33
0026AD2B  48 83 C1 02                     add rcx, 2
0026AD2F  48 83 C2 02                     add rdx, 2
0026AD33  49 3B CF                        cmp rcx, r15
0026AD36  73 0A                           jae 0x14026ad42
0026AD38  0F B6 01                        movzx eax, byte ptr [rcx]
0026AD3B  38 02                           cmp byte ptr [rdx], al
0026AD3D  75 03                           jne 0x14026ad42
0026AD3F  48 FF C1                        inc rcx
0026AD42  41 2B CE                        sub ecx, r14d
0026AD45  44 8B C1                        mov r8d, ecx
0026AD48  E9 26 FF FF FF                  jmp 0x14026ac73
0026AD4D  04 0F                           add al, 0xf
0026AD4F  41 83 C0 F1                     add r8d, -0xf
0026AD53  41 88 01                        mov byte ptr [r9], al
0026AD56  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026AD5C  41 81 F8 FC 03 00 00            cmp r8d, 0x3fc
0026AD63  73 69                           jae 0x14026adce
0026AD65  B8 81 80 80 80                  mov eax, 0x80808081
0026AD6A  41 F7 E0                        mul r8d
0026AD6D  C1 EA 07                        shr edx, 7
0026AD70  48 8D 0C 32                     lea rcx, [rdx + rsi]
0026AD74  44 02 C2                        add r8b, dl
0026AD77  44 88 01                        mov byte ptr [rcx], r8b
0026AD7A  48 8D 71 01                     lea rsi, [rcx + 1]
0026AD7E  E9 0E FF FF FF                  jmp 0x14026ac91
0026AD83  48 83 C1 08                     add rcx, 8
0026AD87  E9 BD FE FF FF                  jmp 0x14026ac49
0026AD8C  48 2B FD                        sub rdi, rbp
0026AD8F  48 83 FF 0F                     cmp rdi, 0xf
0026AD93  0F 82 2C 0A 00 00               jb 0x14026b7c5
0026AD99  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026AD9C  4C 8D 77 F1                     lea r14, [rdi - 0xf]
0026ADA0  48 FF C6                        inc rsi
0026ADA3  49 81 FE FF 00 00 00            cmp r14, 0xff
0026ADAA  0F 83 E2 09 00 00               jae 0x14026b792
0026ADB0  44 88 36                        mov byte ptr [rsi], r14b
0026ADB3  48 8B D5                        mov rdx, rbp
0026ADB6  48 8D 5E 01                     lea rbx, [rsi + 1]
0026ADBA  4C 8B C7                        mov r8, rdi
0026ADBD  48 8B CB                        mov rcx, rbx
0026ADC0  E8 7B BA 45 00                  call 0x1406c6840
0026ADC5  44 8D 1C 3B                     lea r11d, [rbx + rdi]
0026ADC9  E9 6F F8 FF FF                  jmp 0x14026a63d
0026ADCE  B8 81 80 80 80                  mov eax, 0x80808081
0026ADD3  41 F7 E0                        mul r8d
0026ADD6  C1 EA 09                        shr edx, 9
0026ADD9  8B C2                           mov eax, edx
0026ADDB  48 83 C6 04                     add rsi, 4
0026ADDF  41 81 C0 04 FC FF FF            add r8d, 0xfffffc04
0026ADE6  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026ADEC  48 83 E8 01                     sub rax, 1
0026ADF0  0F 84 6F FF FF FF               je 0x14026ad65
0026ADF6  EB E3                           jmp 0x14026addb
0026ADF8  0F B6 C1                        movzx eax, cl
0026ADFB  C0 E0 04                        shl al, 4
0026ADFE  88 06                           mov byte ptr [rsi], al
0026AE00  E9 E8 FD FF FF                  jmp 0x14026abed
0026AE05  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0026AE0D  0F 1F 00                        nop dword ptr [rax]
0026AE10  49 FF CA                        dec r10
0026AE13  41 8B CB                        mov ecx, r11d
0026AE16  49 FF C8                        dec r8
0026AE19  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
0026AE1E  4C 3B D5                        cmp r10, rbp
0026AE21  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0026AE26  41 8B C3                        mov eax, r11d
0026AE29  0F 97 C1                        seta cl
0026AE2C  4C 3B C2                        cmp r8, rdx
0026AE2F  0F 97 C0                        seta al
0026AE32  85 C8                           test eax, ecx
0026AE34  0F 84 31 FD FF FF               je 0x14026ab6b
0026AE3A  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026AE3F  41 38 42 FF                     cmp byte ptr [r10 - 1], al
0026AE43  74 CB                           je 0x14026ae10
0026AE45  E9 21 FD FF FF                  jmp 0x14026ab6b
0026AE4A  81 FB 00 00 00 7E               cmp ebx, 0x7e000000
0026AE50  0F 87 7F 0A 00 00               ja 0x14026b8d5
0026AE56  8B 97 10 40 00 00               mov edx, dword ptr [rdi + 0x4010]
0026AE5C  48 8B C1                        mov rax, rcx
0026AE5F  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0026AE67  49 B8 00 00 00 BB DC BC 1B CF   movabs r8, 0xcf1bbcdcbb000000
0026AE71  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0026AE79  4D 8B CA                        mov r9, r10
0026AE7C  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
0026AE84  4C 2B CA                        sub r9, rdx
0026AE87  48 83 BF 00 40 00 00 00         cmp qword ptr [rdi + 0x4000], 0
0026AE8F  48 03 C6                        add rax, rsi
0026AE92  41 01 9F 18 40 00 00            add dword ptr [r15 + 0x4018], ebx
0026AE99  49 8D 3C 1A                     lea rdi, [r10 + rbx]
0026AE9D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0026AEA2  4C 8D 77 F5                     lea r14, [rdi - 0xb]
0026AEA6  8D 04 1A                        lea eax, [rdx + rbx]
0026AEA9  41 C7 87 14 40 00 00 02 00 00 00  mov dword ptr [r15 + 0x4014], 2
0026AEB4  41 89 87 10 40 00 00            mov dword ptr [r15 + 0x4010], eax
0026AEBB  48 8D 6F FB                     lea rbp, [rdi - 5]
0026AEBF  48 8B 01                        mov rax, qword ptr [rcx]
0026AEC2  4D 8B EA                        mov r13, r10
0026AEC5  49 0F AF C0                     imul rax, r8
0026AEC9  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0026AECE  4D 8B E6                        mov r12, r14
0026AED1  48 C1 E8 34                     shr rax, 0x34
0026AED5  45 8B D3                        mov r10d, r11d
0026AED8  41 89 14 87                     mov dword ptr [r15 + rax*4], edx
0026AEDC  48 8D 51 01                     lea rdx, [rcx + 1]
0026AEE0  48 8B 49 01                     mov rcx, qword ptr [rcx + 1]
0026AEE4  49 0F AF C8                     imul rcx, r8
0026AEE8  BB 01 00 00 00                  mov ebx, 1
0026AEED  48 C1 E9 34                     shr rcx, 0x34
0026AEF1  44 89 54 24 40                  mov dword ptr [rsp + 0x40], r10d
0026AEF6  44 8D 7B 3F                     lea r15d, [rbx + 0x3f]
0026AEFA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0026AF00  8B C2                           mov eax, edx
0026AF02  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0026AF07  41 2B C1                        sub eax, r9d
0026AF0A  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0026AF11  8B C1                           mov eax, ecx
0026AF13  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0026AF1B  48 8D 04 81                     lea rax, [rcx + rax*4]
0026AF1F  8B 08                           mov ecx, dword ptr [rax]
0026AF21  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0026AF26  48 63 C3                        movsxd rax, ebx
0026AF29  48 03 D0                        add rdx, rax
0026AF2C  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
0026AF33  41 8B C7                        mov eax, r15d
0026AF36  41 FF C7                        inc r15d
0026AF39  C1 F8 06                        sar eax, 6
0026AF3C  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
0026AF43  49 3B D6                        cmp rdx, r14
0026AF46  0F 87 FC 02 00 00               ja 0x14026b248
0026AF4C  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0026AF51  44 8B C1                        mov r8d, ecx
0026AF54  48 8B 0A                        mov rcx, qword ptr [rdx]
0026AF57  48 B8 00 00 00 BB DC BC 1B CF   movabs rax, 0xcf1bbcdcbb000000
0026AF61  4C 03 44 24 28                  add r8, qword ptr [rsp + 0x28]
0026AF66  48 0F AF C8                     imul rcx, rax
0026AF6A  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
0026AF71  41 89 01                        mov dword ptr [r9], eax
0026AF74  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
0026AF7B  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0026AF80  05 FF FF 00 00                  add eax, 0xffff
0026AF85  48 C1 E9 34                     shr rcx, 0x34
0026AF89  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0026AF8E  3B 84 24 E0 00 00 00            cmp eax, dword ptr [rsp + 0xe0]
0026AF95  0F 82 29 09 00 00               jb 0x14026b8c4
0026AF9B  41 8B 01                        mov eax, dword ptr [r9]
0026AF9E  41 39 00                        cmp dword ptr [r8], eax
0026AFA1  0F 85 1D 09 00 00               jne 0x14026b8c4
0026AFA7  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0026AFAF  48 8B CF                        mov rcx, rdi
0026AFB2  4C 3B C2                        cmp r8, rdx
0026AFB5  76 0F                           jbe 0x14026afc6
0026AFB7  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026AFBC  41 38 41 FF                     cmp byte ptr [r9 - 1], al
0026AFC0  0F 84 0B 03 00 00               je 0x14026b2d1
0026AFC6  B8 81 80 80 80                  mov eax, 0x80808081
0026AFCB  4C 8D 7E 01                     lea r15, [rsi + 1]
0026AFCF  41 8B C9                        mov ecx, r9d
0026AFD2  41 2B CD                        sub ecx, r13d
0026AFD5  F7 E1                           mul ecx
0026AFD7  8B D9                           mov ebx, ecx
0026AFD9  C1 EA 07                        shr edx, 7
0026AFDC  8B C2                           mov eax, edx
0026AFDE  48 83 C0 08                     add rax, 8
0026AFE2  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0026AFE7  48 03 C3                        add rax, rbx
0026AFEA  49 03 C7                        add rax, r15
0026AFED  48 3B 44 24 30                  cmp rax, qword ptr [rsp + 0x30]
0026AFF2  0F 87 DD 08 00 00               ja 0x14026b8d5
0026AFF8  83 F9 0F                        cmp ecx, 0xf
0026AFFB  0F 82 0A 03 00 00               jb 0x14026b30b
0026B001  83 C1 F1                        add ecx, -0xf
0026B004  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026B007  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
0026B00E  81 F9 FF 00 00 00               cmp ecx, 0xff
0026B014  7C 42                           jl 0x14026b058
0026B016  B8 81 80 80 80                  mov eax, 0x80808081
0026B01B  F7 E1                           mul ecx
0026B01D  49 8B CF                        mov rcx, r15
0026B020  C1 EA 07                        shr edx, 7
0026B023  8B DA                           mov ebx, edx
0026B025  44 8B C2                        mov r8d, edx
0026B028  B2 FF                           mov dl, 0xff
0026B02A  E8 11 BC 45 00                  call 0x1406c6c40
0026B02F  8B 8C 24 E0 00 00 00            mov ecx, dword ptr [rsp + 0xe0]
0026B036  4C 03 FB                        add r15, rbx
0026B039  4C 8B 44 24 20                  mov r8, qword ptr [rsp + 0x20]
0026B03E  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
0026B043  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0026B048  69 C3 01 FF FF FF               imul eax, ebx, 0xffffff01
0026B04E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0026B053  03 C8                           add ecx, eax
0026B055  45 33 DB                        xor r11d, r11d
0026B058  41 88 0F                        mov byte ptr [r15], cl
0026B05B  49 FF C7                        inc r15
0026B05E  4A 8D 14 3B                     lea rdx, [rbx + r15]
0026B062  4D 2B EF                        sub r13, r15
0026B065  4B 8B 04 2F                     mov rax, qword ptr [r15 + r13]
0026B069  49 89 07                        mov qword ptr [r15], rax
0026B06C  49 83 C7 08                     add r15, 8
0026B070  4C 3B FA                        cmp r15, rdx
0026B073  72 F0                           jb 0x14026b065
0026B075  48 8D 5D F9                     lea rbx, [rbp - 7]
0026B079  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0026B07E  66 90                           nop
0026B080  4D 8B E9                        mov r13, r9
0026B083  0F 1F 40 00                     nop dword ptr [rax]
0026B087  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0026B090  4D 8D 7D 04                     lea r15, [r13 + 4]
0026B094  41 0F B7 C5                     movzx eax, r13w
0026B098  66 41 2B C0                     sub ax, r8w
0026B09C  4C 8B CE                        mov r9, rsi
0026B09F  66 89 02                        mov word ptr [rdx], ax
0026B0A2  48 8D 72 02                     lea rsi, [rdx + 2]
0026B0A6  49 8D 50 04                     lea rdx, [r8 + 4]
0026B0AA  49 8B CF                        mov rcx, r15
0026B0AD  4C 3B FB                        cmp r15, rbx
0026B0B0  73 1B                           jae 0x14026b0cd
0026B0B2  4D 8B 07                        mov r8, qword ptr [r15]
0026B0B5  4C 33 02                        xor r8, qword ptr [rdx]
0026B0B8  74 0B                           je 0x14026b0c5
0026B0BA  F3 4D 0F BC C0                  tzcnt r8, r8
0026B0BF  41 C1 E8 03                     shr r8d, 3
0026B0C3  EB 2E                           jmp 0x14026b0f3
0026B0C5  49 8D 4F 08                     lea rcx, [r15 + 8]
0026B0C9  48 83 C2 08                     add rdx, 8
0026B0CD  48 3B 4C 24 20                  cmp rcx, qword ptr [rsp + 0x20]
0026B0D2  0F 83 E2 00 00 00               jae 0x14026b1ba
0026B0D8  4C 8B 01                        mov r8, qword ptr [rcx]
0026B0DB  4C 33 02                        xor r8, qword ptr [rdx]
0026B0DE  0F 84 5B 01 00 00               je 0x14026b23f
0026B0E4  F3 4D 0F BC C0                  tzcnt r8, r8
0026B0E9  41 C1 E8 03                     shr r8d, 3
0026B0ED  45 2B C7                        sub r8d, r15d
0026B0F0  44 03 C1                        add r8d, ecx
0026B0F3  41 8B C0                        mov eax, r8d
0026B0F6  41 8D 88 F0 00 00 00            lea ecx, [r8 + 0xf0]
0026B0FD  49 83 C5 04                     add r13, 4
0026B101  4C 03 E8                        add r13, rax
0026B104  B8 81 80 80 80                  mov eax, 0x80808081
0026B109  F7 E1                           mul ecx
0026B10B  C1 EA 07                        shr edx, 7
0026B10E  8B CA                           mov ecx, edx
0026B110  48 83 C1 06                     add rcx, 6
0026B114  48 03 CE                        add rcx, rsi
0026B117  48 3B 4C 24 30                  cmp rcx, qword ptr [rsp + 0x30]
0026B11C  0F 87 B3 07 00 00               ja 0x14026b8d5
0026B122  41 0F B6 01                     movzx eax, byte ptr [r9]
0026B126  41 83 F8 0F                     cmp r8d, 0xf
0026B12A  0F 83 D4 00 00 00               jae 0x14026b204
0026B130  41 02 C0                        add al, r8b
0026B133  41 88 01                        mov byte ptr [r9], al
0026B136  4D 3B EC                        cmp r13, r12
0026B139  0F 83 09 01 00 00               jae 0x14026b248
0026B13F  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0026B147  49 B8 00 00 00 BB DC BC 1B CF   movabs r8, 0xcf1bbcdcbb000000
0026B151  49 8B 45 FE                     mov rax, qword ptr [r13 - 2]
0026B155  41 8B D5                        mov edx, r13d
0026B158  2B 54 24 28                     sub edx, dword ptr [rsp + 0x28]
0026B15C  49 0F AF C0                     imul rax, r8
0026B160  8D 4A FE                        lea ecx, [rdx - 2]
0026B163  48 C1 E8 34                     shr rax, 0x34
0026B167  41 89 0C 81                     mov dword ptr [r9 + rax*4], ecx
0026B16B  49 8B C9                        mov rcx, r9
0026B16E  49 8B 45 00                     mov rax, qword ptr [r13]
0026B172  49 0F AF C0                     imul rax, r8
0026B176  48 C1 E8 34                     shr rax, 0x34
0026B17A  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
0026B17D  41 89 14 81                     mov dword ptr [r9 + rax*4], edx
0026B181  44 8B C1                        mov r8d, ecx
0026B184  4C 03 44 24 28                  add r8, qword ptr [rsp + 0x28]
0026B189  4C 8B CD                        mov r9, rbp
0026B18C  8D 81 FF FF 00 00               lea eax, [rcx + 0xffff]
0026B192  3B C2                           cmp eax, edx
0026B194  0F 83 D7 05 00 00               jae 0x14026b771
0026B19A  49 8B 4D 01                     mov rcx, qword ptr [r13 + 1]
0026B19E  49 8D 55 01                     lea rdx, [r13 + 1]
0026B1A2  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0026B1A7  48 B8 00 00 00 BB DC BC 1B CF   movabs rax, 0xcf1bbcdcbb000000
0026B1B1  48 0F AF C8                     imul rcx, rax
0026B1B5  E9 2E FD FF FF                  jmp 0x14026aee8
0026B1BA  48 8D 45 FD                     lea rax, [rbp - 3]
0026B1BE  48 3B C8                        cmp rcx, rax
0026B1C1  73 0E                           jae 0x14026b1d1
0026B1C3  8B 01                           mov eax, dword ptr [rcx]
0026B1C5  39 02                           cmp dword ptr [rdx], eax
0026B1C7  75 08                           jne 0x14026b1d1
0026B1C9  48 83 C1 04                     add rcx, 4
0026B1CD  48 83 C2 04                     add rdx, 4
0026B1D1  48 8D 45 FF                     lea rax, [rbp - 1]
0026B1D5  48 3B C8                        cmp rcx, rax
0026B1D8  73 10                           jae 0x14026b1ea
0026B1DA  0F B7 01                        movzx eax, word ptr [rcx]
0026B1DD  66 39 02                        cmp word ptr [rdx], ax
0026B1E0  75 08                           jne 0x14026b1ea
0026B1E2  48 83 C1 02                     add rcx, 2
0026B1E6  48 83 C2 02                     add rdx, 2
0026B1EA  48 3B CD                        cmp rcx, rbp
0026B1ED  73 0A                           jae 0x14026b1f9
0026B1EF  0F B6 01                        movzx eax, byte ptr [rcx]
0026B1F2  38 02                           cmp byte ptr [rdx], al
0026B1F4  75 03                           jne 0x14026b1f9
0026B1F6  48 FF C1                        inc rcx
0026B1F9  41 2B CF                        sub ecx, r15d
0026B1FC  44 8B C1                        mov r8d, ecx
0026B1FF  E9 EF FE FF FF                  jmp 0x14026b0f3
0026B204  04 0F                           add al, 0xf
0026B206  41 83 C0 F1                     add r8d, -0xf
0026B20A  41 88 01                        mov byte ptr [r9], al
0026B20D  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026B213  41 81 F8 FC 03 00 00            cmp r8d, 0x3fc
0026B21A  0F 83 87 00 00 00               jae 0x14026b2a7
0026B220  B8 81 80 80 80                  mov eax, 0x80808081
0026B225  41 F7 E0                        mul r8d
0026B228  C1 EA 07                        shr edx, 7
0026B22B  48 8D 04 32                     lea rax, [rdx + rsi]
0026B22F  8B CA                           mov ecx, edx
0026B231  41 02 C8                        add cl, r8b
0026B234  48 8D 70 01                     lea rsi, [rax + 1]
0026B238  88 08                           mov byte ptr [rax], cl
0026B23A  E9 F7 FE FF FF                  jmp 0x14026b136
0026B23F  48 83 C1 08                     add rcx, 8
0026B243  E9 81 FE FF FF                  jmp 0x14026b0c9
0026B248  49 2B FD                        sub rdi, r13
0026B24B  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
0026B255  49 8B C0                        mov rax, r8
0026B258  48 8D 8F F0 00 00 00            lea rcx, [rdi + 0xf0]
0026B25F  48 F7 E1                        mul rcx
0026B262  48 8D 46 01                     lea rax, [rsi + 1]
0026B266  48 C1 EA 07                     shr rdx, 7
0026B26A  48 03 D7                        add rdx, rdi
0026B26D  48 03 C2                        add rax, rdx
0026B270  48 3B 44 24 30                  cmp rax, qword ptr [rsp + 0x30]
0026B275  0F 87 5A 06 00 00               ja 0x14026b8d5
0026B27B  48 83 FF 0F                     cmp rdi, 0xf
0026B27F  0F 82 DC 05 00 00               jb 0x14026b861
0026B285  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026B288  48 8D 6F F1                     lea rbp, [rdi - 0xf]
0026B28C  48 FF C6                        inc rsi
0026B28F  48 81 FD FF 00 00 00            cmp rbp, 0xff
0026B296  0F 83 99 05 00 00               jae 0x14026b835
0026B29C  40 88 2E                        mov byte ptr [rsi], bpl
0026B29F  49 8B D5                        mov rdx, r13
0026B2A2  E9 0F FB FF FF                  jmp 0x14026adb6
0026B2A7  B8 81 80 80 80                  mov eax, 0x80808081
0026B2AC  41 F7 E0                        mul r8d
0026B2AF  C1 EA 09                        shr edx, 9
0026B2B2  8B C2                           mov eax, edx
0026B2B4  48 83 C6 04                     add rsi, 4
0026B2B8  41 81 C0 04 FC FF FF            add r8d, 0xfffffc04
0026B2BF  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026B2C5  48 83 E8 01                     sub rax, 1
0026B2C9  0F 84 51 FF FF FF               je 0x14026b220
0026B2CF  EB E3                           jmp 0x14026b2b4
0026B2D1  49 FF C9                        dec r9
0026B2D4  41 8B CB                        mov ecx, r11d
0026B2D7  49 FF C8                        dec r8
0026B2DA  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0026B2DF  4D 3B CD                        cmp r9, r13
0026B2E2  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0026B2E7  41 8B C3                        mov eax, r11d
0026B2EA  0F 97 C1                        seta cl
0026B2ED  4C 3B C2                        cmp r8, rdx
0026B2F0  0F 97 C0                        seta al
0026B2F3  85 C8                           test eax, ecx
0026B2F5  0F 84 CB FC FF FF               je 0x14026afc6
0026B2FB  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026B300  41 38 41 FF                     cmp byte ptr [r9 - 1], al
0026B304  74 CB                           je 0x14026b2d1
0026B306  E9 BB FC FF FF                  jmp 0x14026afc6
0026B30B  C0 E1 04                        shl cl, 4
0026B30E  88 0E                           mov byte ptr [rsi], cl
0026B310  E9 49 FD FF FF                  jmp 0x14026b05e
0026B315  81 FB 00 00 00 7E               cmp ebx, 0x7e000000
0026B31B  0F 87 B4 05 00 00               ja 0x14026b8d5
0026B321  8B 8F 10 40 00 00               mov ecx, dword ptr [rdi + 0x4010]
0026B327  49 B8 00 00 00 BB DC BC 1B CF   movabs r8, 0xcf1bbcdcbb000000
0026B331  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0026B339  4D 8B CA                        mov r9, r10
0026B33C  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0026B344  4C 2B C9                        sub r9, rcx
0026B347  48 83 BF 00 40 00 00 00         cmp qword ptr [rdi + 0x4000], 0
0026B34F  4D 8B E2                        mov r12, r10
0026B352  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
0026B35A  8D 04 19                        lea eax, [rcx + rbx]
0026B35D  41 01 9F 18 40 00 00            add dword ptr [r15 + 0x4018], ebx
0026B364  49 8D 3C 1A                     lea rdi, [r10 + rbx]
0026B368  41 89 87 10 40 00 00            mov dword ptr [r15 + 0x4010], eax
0026B36F  4C 8D 77 F5                     lea r14, [rdi - 0xb]
0026B373  41 C7 87 14 40 00 00 02 00 00 00  mov dword ptr [r15 + 0x4014], 2
0026B37E  48 8D 6F FB                     lea rbp, [rdi - 5]
0026B382  48 8B 02                        mov rax, qword ptr [rdx]
0026B385  4D 8B EE                        mov r13, r14
0026B388  49 0F AF C0                     imul rax, r8
0026B38C  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0026B391  45 8B D3                        mov r10d, r11d
0026B394  48 C1 E8 34                     shr rax, 0x34
0026B398  48 FF C2                        inc rdx
0026B39B  41 89 0C 87                     mov dword ptr [r15 + rax*4], ecx
0026B39F  48 8B 0A                        mov rcx, qword ptr [rdx]
0026B3A2  49 0F AF C8                     imul rcx, r8
0026B3A6  41 B8 01 00 00 00               mov r8d, 1
0026B3AC  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
0026B3B1  48 C1 E9 34                     shr rcx, 0x34
0026B3B5  45 8D 50 3F                     lea r10d, [r8 + 0x3f]
0026B3B9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0026B3C0  8B C1                           mov eax, ecx
0026B3C2  44 8B FA                        mov r15d, edx
0026B3C5  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0026B3CD  45 2B F9                        sub r15d, r9d
0026B3D0  4C 8B CA                        mov r9, rdx
0026B3D3  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0026B3D8  48 8D 04 81                     lea rax, [rcx + rax*4]
0026B3DC  8B 08                           mov ecx, dword ptr [rax]
0026B3DE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0026B3E3  49 63 C0                        movsxd rax, r8d
0026B3E6  48 03 D0                        add rdx, rax
0026B3E9  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
0026B3F0  41 8B C2                        mov eax, r10d
0026B3F3  41 FF C2                        inc r10d
0026B3F6  C1 F8 06                        sar eax, 6
0026B3F9  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0026B400  49 3B D6                        cmp rdx, r14
0026B403  0F 87 A9 02 00 00               ja 0x14026b6b2
0026B409  44 8B C1                        mov r8d, ecx
0026B40C  48 B8 00 00 00 BB DC BC 1B CF   movabs rax, 0xcf1bbcdcbb000000
0026B416  48 8B 0A                        mov rcx, qword ptr [rdx]
0026B419  4C 03 44 24 40                  add r8, qword ptr [rsp + 0x40]
0026B41E  48 0F AF C8                     imul rcx, rax
0026B422  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0026B427  48 C1 E9 34                     shr rcx, 0x34
0026B42B  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0026B430  44 89 38                        mov dword ptr [rax], r15d
0026B433  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
0026B43A  05 FF FF 00 00                  add eax, 0xffff
0026B43F  41 3B C7                        cmp eax, r15d
0026B442  0F 82 44 04 00 00               jb 0x14026b88c
0026B448  41 8B 01                        mov eax, dword ptr [r9]
0026B44B  41 39 00                        cmp dword ptr [r8], eax
0026B44E  0F 85 38 04 00 00               jne 0x14026b88c
0026B454  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0026B45C  4C 3B C2                        cmp r8, rdx
0026B45F  76 0F                           jbe 0x14026b470
0026B461  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026B466  41 38 41 FF                     cmp byte ptr [r9 - 1], al
0026B46A  0F 84 B0 02 00 00               je 0x14026b720
0026B470  41 8B C9                        mov ecx, r9d
0026B473  4C 8D 7E 01                     lea r15, [rsi + 1]
0026B477  41 2B CC                        sub ecx, r12d
0026B47A  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
0026B481  83 F9 0F                        cmp ecx, 0xf
0026B484  0F 82 7D 02 00 00               jb 0x14026b707
0026B48A  8D 51 F1                        lea edx, [rcx - 0xf]
0026B48D  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026B490  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
0026B497  4D 8B D7                        mov r10, r15
0026B49A  81 FA FF 00 00 00               cmp edx, 0xff
0026B4A0  7C 43                           jl 0x14026b4e5
0026B4A2  B8 81 80 80 80                  mov eax, 0x80808081
0026B4A7  49 8B CF                        mov rcx, r15
0026B4AA  F7 E2                           mul edx
0026B4AC  C1 EA 07                        shr edx, 7
0026B4AF  8B DA                           mov ebx, edx
0026B4B1  44 8B C2                        mov r8d, edx
0026B4B4  B2 FF                           mov dl, 0xff
0026B4B6  E8 85 B7 45 00                  call 0x1406c6c40
0026B4BB  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0026B4C2  4D 8D 14 1F                     lea r10, [r15 + rbx]
0026B4C6  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0026B4CB  4D 8B FA                        mov r15, r10
0026B4CE  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0026B4D5  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
0026B4DA  69 C3 01 FF FF FF               imul eax, ebx, 0xffffff01
0026B4E0  03 D0                           add edx, eax
0026B4E2  45 33 DB                        xor r11d, r11d
0026B4E5  41 88 17                        mov byte ptr [r15], dl
0026B4E8  4D 8D 7A 01                     lea r15, [r10 + 1]
0026B4EC  8B D1                           mov edx, ecx
0026B4EE  49 03 D7                        add rdx, r15
0026B4F1  4D 2B E7                        sub r12, r15
0026B4F4  4B 8B 04 27                     mov rax, qword ptr [r15 + r12]
0026B4F8  49 89 07                        mov qword ptr [r15], rax
0026B4FB  49 83 C7 08                     add r15, 8
0026B4FF  4C 3B FA                        cmp r15, rdx
0026B502  72 F0                           jb 0x14026b4f4
0026B504  48 8D 5D F9                     lea rbx, [rbp - 7]
0026B508  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0026B50D  0F 1F 00                        nop dword ptr [rax]
0026B510  44 8B 54 24 48                  mov r10d, dword ptr [rsp + 0x48]
0026B515  4D 8B E1                        mov r12, r9
0026B518  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0026B520  4D 8D 7C 24 04                  lea r15, [r12 + 4]
0026B525  41 0F B7 C4                     movzx eax, r12w
0026B529  66 41 2B C0                     sub ax, r8w
0026B52D  4C 8B CE                        mov r9, rsi
0026B530  66 89 02                        mov word ptr [rdx], ax
0026B533  48 8D 72 02                     lea rsi, [rdx + 2]
0026B537  49 8D 50 04                     lea rdx, [r8 + 4]
0026B53B  49 8B CF                        mov rcx, r15
0026B53E  4C 3B FB                        cmp r15, rbx
0026B541  73 1B                           jae 0x14026b55e
0026B543  4D 8B 07                        mov r8, qword ptr [r15]
0026B546  4C 33 02                        xor r8, qword ptr [rdx]
0026B549  74 0B                           je 0x14026b556
0026B54B  F3 4D 0F BC C0                  tzcnt r8, r8
0026B550  41 C1 E8 03                     shr r8d, 3
0026B554  EB 2E                           jmp 0x14026b584
0026B556  49 8D 4F 08                     lea rcx, [r15 + 8]
0026B55A  48 83 C2 08                     add rdx, 8
0026B55E  48 3B 4C 24 20                  cmp rcx, qword ptr [rsp + 0x20]
0026B563  0F 83 C0 00 00 00               jae 0x14026b629
0026B569  4C 8B 01                        mov r8, qword ptr [rcx]
0026B56C  4C 33 02                        xor r8, qword ptr [rdx]
0026B56F  0F 84 34 01 00 00               je 0x14026b6a9
0026B575  F3 4D 0F BC C0                  tzcnt r8, r8
0026B57A  41 C1 E8 03                     shr r8d, 3
0026B57E  45 2B C7                        sub r8d, r15d
0026B581  44 03 C1                        add r8d, ecx
0026B584  41 8B C0                        mov eax, r8d
0026B587  49 83 C4 04                     add r12, 4
0026B58B  4C 03 E0                        add r12, rax
0026B58E  41 0F B6 01                     movzx eax, byte ptr [r9]
0026B592  41 83 F8 0F                     cmp r8d, 0xf
0026B596  0F 83 D7 00 00 00               jae 0x14026b673
0026B59C  44 02 C0                        add r8b, al
0026B59F  45 88 01                        mov byte ptr [r9], r8b
0026B5A2  4D 3B E5                        cmp r12, r13
0026B5A5  0F 83 07 01 00 00               jae 0x14026b6b2
0026B5AB  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0026B5B3  49 B8 00 00 00 BB DC BC 1B CF   movabs r8, 0xcf1bbcdcbb000000
0026B5BD  49 8B 44 24 FE                  mov rax, qword ptr [r12 - 2]
0026B5C2  41 8B D4                        mov edx, r12d
0026B5C5  2B 54 24 40                     sub edx, dword ptr [rsp + 0x40]
0026B5C9  49 0F AF C0                     imul rax, r8
0026B5CD  8D 4A FE                        lea ecx, [rdx - 2]
0026B5D0  48 C1 E8 34                     shr rax, 0x34
0026B5D4  41 89 0C 81                     mov dword ptr [r9 + rax*4], ecx
0026B5D8  49 8B C9                        mov rcx, r9
0026B5DB  49 8B 04 24                     mov rax, qword ptr [r12]
0026B5DF  49 0F AF C0                     imul rax, r8
0026B5E3  48 C1 E8 34                     shr rax, 0x34
0026B5E7  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
0026B5EA  41 89 14 81                     mov dword ptr [r9 + rax*4], edx
0026B5EE  44 8B C1                        mov r8d, ecx
0026B5F1  4C 03 44 24 40                  add r8, qword ptr [rsp + 0x40]
0026B5F6  4C 8B CD                        mov r9, rbp
0026B5F9  8D 81 FF FF 00 00               lea eax, [rcx + 0xffff]
0026B5FF  3B C2                           cmp eax, edx
0026B601  0F 83 CC 01 00 00               jae 0x14026b7d3
0026B607  49 8B 4C 24 01                  mov rcx, qword ptr [r12 + 1]
0026B60C  49 8D 54 24 01                  lea rdx, [r12 + 1]
0026B611  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0026B616  48 B8 00 00 00 BB DC BC 1B CF   movabs rax, 0xcf1bbcdcbb000000
0026B620  48 0F AF C8                     imul rcx, rax
0026B624  E9 7D FD FF FF                  jmp 0x14026b3a6
0026B629  48 8D 45 FD                     lea rax, [rbp - 3]
0026B62D  48 3B C8                        cmp rcx, rax
0026B630  73 0E                           jae 0x14026b640
0026B632  8B 01                           mov eax, dword ptr [rcx]
0026B634  39 02                           cmp dword ptr [rdx], eax
0026B636  75 08                           jne 0x14026b640
0026B638  48 83 C1 04                     add rcx, 4
0026B63C  48 83 C2 04                     add rdx, 4
0026B640  48 8D 45 FF                     lea rax, [rbp - 1]
0026B644  48 3B C8                        cmp rcx, rax
0026B647  73 10                           jae 0x14026b659
0026B649  0F B7 01                        movzx eax, word ptr [rcx]
0026B64C  66 39 02                        cmp word ptr [rdx], ax
0026B64F  75 08                           jne 0x14026b659
0026B651  48 83 C1 02                     add rcx, 2
0026B655  48 83 C2 02                     add rdx, 2
0026B659  48 3B CD                        cmp rcx, rbp
0026B65C  73 0A                           jae 0x14026b668
0026B65E  0F B6 01                        movzx eax, byte ptr [rcx]
0026B661  38 02                           cmp byte ptr [rdx], al
0026B663  75 03                           jne 0x14026b668
0026B665  48 FF C1                        inc rcx
0026B668  41 2B CF                        sub ecx, r15d
0026B66B  44 8B C1                        mov r8d, ecx
0026B66E  E9 11 FF FF FF                  jmp 0x14026b584
0026B673  04 0F                           add al, 0xf
0026B675  41 83 C0 F1                     add r8d, -0xf
0026B679  41 88 01                        mov byte ptr [r9], al
0026B67C  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026B682  41 81 F8 FC 03 00 00            cmp r8d, 0x3fc
0026B689  73 56                           jae 0x14026b6e1
0026B68B  B8 81 80 80 80                  mov eax, 0x80808081
0026B690  41 F7 E0                        mul r8d
0026B693  C1 EA 07                        shr edx, 7
0026B696  48 8D 0C 32                     lea rcx, [rdx + rsi]
0026B69A  44 02 C2                        add r8b, dl
0026B69D  44 88 01                        mov byte ptr [rcx], r8b
0026B6A0  48 8D 71 01                     lea rsi, [rcx + 1]
0026B6A4  E9 F9 FE FF FF                  jmp 0x14026b5a2
0026B6A9  48 83 C1 08                     add rcx, 8
0026B6AD  E9 A8 FE FF FF                  jmp 0x14026b55a
0026B6B2  49 2B FC                        sub rdi, r12
0026B6B5  48 83 FF 0F                     cmp rdi, 0xf
0026B6B9  0F 82 68 01 00 00               jb 0x14026b827
0026B6BF  C6 06 F0                        mov byte ptr [rsi], 0xf0
0026B6C2  48 8D 6F F1                     lea rbp, [rdi - 0xf]
0026B6C6  48 FF C6                        inc rsi
0026B6C9  48 81 FD FF 00 00 00            cmp rbp, 0xff
0026B6D0  0F 83 1E 01 00 00               jae 0x14026b7f4
0026B6D6  40 88 2E                        mov byte ptr [rsi], bpl
0026B6D9  49 8B D4                        mov rdx, r12
0026B6DC  E9 D5 F6 FF FF                  jmp 0x14026adb6
0026B6E1  B8 81 80 80 80                  mov eax, 0x80808081
0026B6E6  41 F7 E0                        mul r8d
0026B6E9  C1 EA 09                        shr edx, 9
0026B6EC  8B C2                           mov eax, edx
0026B6EE  48 83 C6 04                     add rsi, 4
0026B6F2  41 81 C0 04 FC FF FF            add r8d, 0xfffffc04
0026B6F9  C7 06 FF FF FF FF               mov dword ptr [rsi], 0xffffffff
0026B6FF  48 83 E8 01                     sub rax, 1
0026B703  74 86                           je 0x14026b68b
0026B705  EB E7                           jmp 0x14026b6ee
0026B707  0F B6 C1                        movzx eax, cl
0026B70A  C0 E0 04                        shl al, 4
0026B70D  88 06                           mov byte ptr [rsi], al
0026B70F  E9 D8 FD FF FF                  jmp 0x14026b4ec
0026B714  0F 1F 40 00                     nop dword ptr [rax]
0026B718  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0026B720  49 FF C9                        dec r9
0026B723  41 8B CB                        mov ecx, r11d
0026B726  49 FF C8                        dec r8
0026B729  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0026B72E  4D 3B CC                        cmp r9, r12
0026B731  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0026B736  41 8B C3                        mov eax, r11d
0026B739  0F 97 C1                        seta cl
0026B73C  4C 3B C2                        cmp r8, rdx
0026B73F  0F 97 C0                        seta al
0026B742  85 C8                           test eax, ecx
0026B744  0F 84 26 FD FF FF               je 0x14026b470
0026B74A  41 0F B6 40 FF                  movzx eax, byte ptr [r8 - 1]
0026B74F  41 38 41 FF                     cmp byte ptr [r9 - 1], al
0026B753  74 CB                           je 0x14026b720
0026B755  E9 16 FD FF FF                  jmp 0x14026b470
0026B75A  85 C9                           test ecx, ecx
0026B75C  0F 8E 73 01 00 00               jle 0x14026b8d5
0026B762  41 C6 01 00                     mov byte ptr [r9], 0
0026B766  41 BB 01 00 00 00               mov r11d, 1
0026B76C  E9 64 01 00 00                  jmp 0x14026b8d5
0026B771  41 8B 45 00                     mov eax, dword ptr [r13]
0026B775  48 8B CF                        mov rcx, rdi
0026B778  41 39 00                        cmp dword ptr [r8], eax
0026B77B  0F 85 19 FA FF FF               jne 0x14026b19a
0026B781  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
0026B786  48 8D 56 01                     lea rdx, [rsi + 1]
0026B78A  C6 06 00                        mov byte ptr [rsi], 0
0026B78D  E9 FE F8 FF FF                  jmp 0x14026b090
0026B792  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
0026B79C  48 8B CE                        mov rcx, rsi
0026B79F  49 F7 E6                        mul r14
0026B7A2  48 8B DA                        mov rbx, rdx
0026B7A5  B2 FF                           mov dl, 0xff
0026B7A7  48 C1 EB 07                     shr rbx, 7
0026B7AB  4C 8B C3                        mov r8, rbx
0026B7AE  E8 8D B4 45 00                  call 0x1406c6c40
0026B7B3  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
0026B7BA  48 03 F3                        add rsi, rbx
0026B7BD  4C 03 F0                        add r14, rax
0026B7C0  E9 EB F5 FF FF                  jmp 0x14026adb0
0026B7C5  40 0F B6 C7                     movzx eax, dil
0026B7C9  C0 E0 04                        shl al, 4
0026B7CC  88 06                           mov byte ptr [rsi], al
0026B7CE  E9 E0 F5 FF FF                  jmp 0x14026adb3
0026B7D3  41 8B 04 24                     mov eax, dword ptr [r12]
0026B7D7  48 8B CF                        mov rcx, rdi
0026B7DA  41 39 00                        cmp dword ptr [r8], eax
0026B7DD  0F 85 24 FE FF FF               jne 0x14026b607
0026B7E3  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
0026B7E8  48 8D 56 01                     lea rdx, [rsi + 1]
0026B7EC  C6 06 00                        mov byte ptr [rsi], 0
0026B7EF  E9 2C FD FF FF                  jmp 0x14026b520
0026B7F4  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
0026B7FE  48 8B CE                        mov rcx, rsi
0026B801  48 F7 E5                        mul rbp
0026B804  48 8B DA                        mov rbx, rdx
0026B807  B2 FF                           mov dl, 0xff
0026B809  48 C1 EB 07                     shr rbx, 7
0026B80D  4C 8B C3                        mov r8, rbx
0026B810  E8 2B B4 45 00                  call 0x1406c6c40
0026B815  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
0026B81C  48 03 F3                        add rsi, rbx
0026B81F  48 03 E8                        add rbp, rax
0026B822  E9 AF FE FF FF                  jmp 0x14026b6d6
0026B827  40 0F B6 C7                     movzx eax, dil
0026B82B  C0 E0 04                        shl al, 4
0026B82E  88 06                           mov byte ptr [rsi], al
0026B830  E9 A4 FE FF FF                  jmp 0x14026b6d9
0026B835  49 8B C0                        mov rax, r8
0026B838  48 8B CE                        mov rcx, rsi
0026B83B  48 F7 E5                        mul rbp
0026B83E  48 8B DA                        mov rbx, rdx
0026B841  B2 FF                           mov dl, 0xff
0026B843  48 C1 EB 07                     shr rbx, 7
0026B847  4C 8B C3                        mov r8, rbx
0026B84A  E8 F1 B3 45 00                  call 0x1406c6c40
0026B84F  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
0026B856  48 03 F3                        add rsi, rbx
0026B859  48 03 E8                        add rbp, rax
0026B85C  E9 3B FA FF FF                  jmp 0x14026b29c
0026B861  40 0F B6 C7                     movzx eax, dil
0026B865  C0 E0 04                        shl al, 4
0026B868  88 06                           mov byte ptr [rsi], al
0026B86A  E9 30 FA FF FF                  jmp 0x14026b29f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0026A9FF(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, unsigned int a8, unsigned int a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, unsigned int a27, unsigned int a28, unsigned int a29)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned int v_stack_pE8;

    if (((unsigned int)(v_rbx)) >= 0x1000BULL) goto loc_0026B315;
    if ((unsigned int)(v_rbx) == 0) goto loc_0026B762;
    a4 = (v_r10) - ((unsigned int)(*(unsigned int *)(v_rdi + 16400)));
    v_stack_p28 = a4;
    *(unsigned int *)(a24 + 16400) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16400)) + v_rbx * 1);
    *(unsigned int *)(a24 + 16404) = 3;
    if (((unsigned int)(v_rbx)) < 13) goto loc_0026AD8C;
    a1 = (unsigned int)((a1) * (*(unsigned int *)(v_r10)));
    a1 = (a1) >> (19);
    *(unsigned __int16 *)(a24 + a1 * 2) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rdi + 16400)));
loc_0026AA92:
    a1 = (unsigned int)((a1) * (*(unsigned int *)(v_r10 + 1)));
    v_stack_pE0 = (unsigned int)((unsigned int)((unsigned int)(v_r11)));
    v_stack_pD8 = 64;
    a1 = (unsigned int)((a1) >> (19));
    v_stack_p50 = v_r10 + 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + 1))) - (a5));
    v_stack_p48 = (unsigned int)(result);
    v_stack_p20 = a24 + (unsigned int)((unsigned int)(a1)) * 2;
    v_stack_p40 = (unsigned int)(*(unsigned __int16 *)(a24 + (unsigned int)((unsigned int)(a1)) * 2));
    a2 = (v_r10 + 1) + ((int)(1));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a27)))) >> (6));
    a1 = (unsigned int)(((unsigned int)(a27)) + 1);
    v_stack_pE8 = (unsigned int)(result);
    v_stack_pD8 = (unsigned int)(a1);
    if (a2 > (v_r10 + v_rbx * 1 - 11)) goto loc_0026AD8C;
    a1 = (unsigned int)((a1) * (*(unsigned int *)(a2)));
    a3 = ((unsigned int)(a8)) + (a5);
    *(unsigned __int16 *)(v_stack_p20) = (unsigned __int16)((unsigned int)(a9));
    a1 = (unsigned int)((a1) >> (19));
    v_stack_p30 = a3;
    if (a3 <= a25) goto loc_0026AB6B;
    if ((*(unsigned __int8 *)(v_r10 + 1 - 1)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 - 1)))) goto loc_0026AE05;
loc_0026AB6B:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + 1))) - ((unsigned int)(v_r10)));
    v_stack_pE8 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < 15) goto loc_0026ADF8;
    *(unsigned __int8 *)(a26) = 240;
    v_stack_pD8 = (unsigned int)(a1 - 15);
    result = *(unsigned __int8 *)(a3 - 1);
    v_rbx = (unsigned int)((unsigned int)(v_r11));
    v_r10 = v_r10 + 1;
    v_r14 = a26 + 1;
    if (((unsigned int)(a1 - 15)) >= 255) {
        result = 0x80808081ULL;
        a1 = a26 + 1;
        a2 = (unsigned int)((a1 - 15) >> (7));
        v_rbx = (unsigned int)(a2);
        a3 = (unsigned int)(a2);
        a2 = 255;
        result = memset(a1, a2, a3, a26 + 1);
        a2 = a27;
        a4 = v_rbx + a26 + 1 * 1;
        a1 = a29;
        v_r14 = a4;
        a3 = a6;
        v_r10 = a10;
        result = (unsigned int)((result) * ((unsigned int)(v_rbx)));
        v_rbx = a28;
        a2 = (unsigned int)((a2) + ((unsigned int)(result)));
        v_r11 = 0;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a2);
loc_0026ABED:
    a2 = ((unsigned int)((unsigned int)(a1))) + (a4 + 1);
    v_rbp = (v_r10) - (a4 + 1);
loc_0026ABF5:
    *(unsigned __int64 *)(a4 + 1) = *(unsigned __int64 *)(a4 + 1 + v_rbp * 1);
    v_r14 = (a4 + 1) + (8);
    if (v_r14 < a2) goto loc_0026ABF5;
    v_stack_p30 = v_r10 + v_rbx * 1 - 5 - 7;
loc_0026AC10:
    result = (unsigned __int16)(((unsigned __int16)(v_r10)) - ((unsigned __int16)(a3)));
    *(unsigned __int16 *)(a2) = (unsigned __int16)(result);
    if ((v_r10 + 4) >= (v_r10 + v_rbx * 1 - 5 - 7)) goto loc_0026AC4D;
    a3 = (*(unsigned __int64 *)(v_r10 + 4)) ^ (*(unsigned __int64 *)(a3 + 4));
    if (condition_is_equal) goto loc_0026AC45;
    a3 = (unsigned int)((a3) >> (3));
    goto loc_0026AC73;
loc_0026AC45:
loc_0026AC49:
    a2 = (a3 + 4) + (8);
loc_0026AC4D:
    if ((v_r10 + 4 + 8) >= a6) goto loc_0026AD03;
    a3 = (*(unsigned __int64 *)(v_r10 + 4 + 8)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_equal) goto loc_0026AD83;
    a3 = (unsigned int)((a3) >> (3));
    a3 = (unsigned int)((a3) - ((unsigned int)(v_r10 + 4)));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r10 + 4 + 8)));
loc_0026AC73:
    v_r10 = (v_r10) + (4);
    v_r10 = (v_r10) + ((unsigned int)((unsigned int)(a3)));
    if (((unsigned int)(a3)) >= 15) goto loc_0026AD4D;
    result = (unsigned __int8)((*(unsigned __int8 *)(a26)) + ((unsigned __int8)(a3)));
    *(unsigned __int8 *)(a26) = (unsigned __int8)(result);
loc_0026AC91:
    if (v_r10 >= (v_r10 + v_rbx * 1 - 11)) goto loc_0026AD8C;
    a1 = (unsigned int)((v_r10 + 4 + 8) * (*(unsigned int *)(v_r10 - 2)));
    a2 = (unsigned __int16)(((unsigned __int16)(v_r10)) - ((unsigned __int16)(a5)));
    a2 = (unsigned __int16)((a2) - (2));
    a1 = (a1) >> (19);
    *(unsigned __int16 *)(a24 + a1 * 2) = (unsigned __int16)(a2);
    result = (unsigned int)((result) * (*(unsigned int *)(v_r10)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (a5));
    result = (unsigned int)((result) >> (19));
    *(unsigned __int16 *)(a24 + result * 2) = (unsigned __int16)(a2);
    a3 = (*(unsigned __int16 *)(a24 + result * 2)) + (a5);
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10))))) goto loc_0026AA92;
    *(unsigned __int8 *)(a2 + 2) = 0;
    goto loc_0026AC10;
loc_0026AD03:
    if ((a24 + result * 2) >= (v_r10 + v_rbx * 1 - 5 - 3)) goto loc_0026AD1A;
    if ((*(unsigned int *)(a2 + 2 + 1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a24 + result * 2))))) {
        a1 = (a24 + result * 2) + (4);
        a2 = (a2 + 2 + 1) + (4);
    }
    if (a1 >= (v_r10 + v_rbx * 1 - 5 - 1)) goto loc_0026AD33;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= (v_r10 + v_rbx * 1 - 5)) goto loc_0026AD42;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 4)));
    goto loc_0026AC73;
loc_0026AD4D:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) + (15));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) + (-15));
    *(unsigned __int8 *)(a5) = (unsigned __int8)(result);
    *(unsigned int *)(a2 + 2) = 0xFFFFFFFFULL;
    if (((unsigned int)(a3)) >= 0x3FCULL) goto loc_0026ADCE;
loc_0026AD65:
    a2 = (unsigned int)((a2) >> (7));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(a2 + a2 + 2 * 1) = (unsigned __int8)(a3);
    goto loc_0026AC91;
loc_0026AD83:
    a1 = (a2 + a2 + 2 * 1) + (8);
    goto loc_0026AC49;
loc_0026AD8C:
    v_rdi = (v_r10 + v_rbx * 1) - (a6);
    if (v_rdi < 15) goto loc_0026B7C5;
    *(unsigned __int8 *)(a2 + a2 + 2 * 1 + 1) = 240;
    v_rsi = (a2 + a2 + 2 * 1 + 1) + 1;
    if ((v_rdi - 15) >= 255) goto loc_0026B792;
loc_0026ADB0:
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(v_rdi - 15);
loc_0026ADB3:
loc_0026ADB6:
    result = memcpy(v_rsi + 1, a6, v_rdi, a5);
loc_0026ADCE:
    a2 = (unsigned int)((a6) >> (9));
loc_0026ADDB:
    v_rsi = (v_rsi) + (4);
    a3 = (unsigned int)((v_rdi) + (0xFFFFFC04ULL));
    *(unsigned int *)(v_rsi) = 0xFFFFFFFFULL;
    result = ((unsigned int)((unsigned int)(a2))) - (1);
    if (condition_is_equal) goto loc_0026AD65;
    goto loc_0026ADDB;
loc_0026ADF8:
    result = (unsigned __int8)(((unsigned __int8)(v_rsi + 1)) << (4));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(result);
    goto loc_0026ABED;
loc_0026AE05:
loc_0026AE10:
    v_r10 = (v_r10) - 1;
    a3 = (a3) - 1;
    v_stack_p50 = v_r10;
    v_stack_p30 = a3;
    a1 = (v_r10 > a6) ? 1 : 0;
    result = (a3 > a25) ? 1 : 0;
    if ((((unsigned int)(result)) & ((unsigned int)(a1))) == 0) goto loc_0026AB6B;
    if ((*(unsigned __int8 *)(v_r10 - 1)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 - 1)))) goto loc_0026AE10;
    goto loc_0026AB6B;
loc_0026B315:
    a4 = (v_r10) - ((unsigned int)(*(unsigned int *)(v_rdi + 16400)));
    *(unsigned int *)(a24 + 16400) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16400)) + v_rsi + 1 * 1);
    *(unsigned int *)(a24 + 16404) = 2;
    result = (*(unsigned __int64 *)(a25)) * (a3);
    v_stack_p40 = a4;
    result = (result) >> (52);
    a2 = (a25) + 1;
    *(unsigned int *)(a24 + result * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16400)));
    a1 = (*(unsigned __int64 *)(a2)) * (a3);
loc_0026B3A6:
    v_stack_p48 = (unsigned int)((unsigned int)((unsigned int)(v_rsi + 1 + v_rdi * 1)));
    a1 = (a1) >> (52);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a4)));
    v_stack_p20 = a2;
    v_stack_p38 = a24 + (unsigned int)((unsigned int)(a1)) * 4;
    a2 = (a2) + ((int)(1));
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(a24 + (unsigned int)((unsigned int)(a1)) * 4)));
    v_r10 = (unsigned int)((1 + 63) + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)(1 + 63))) >> (6));
    v_stack_pD8 = (unsigned int)(result);
    if (a2 > (v_r10 + v_rsi + 1 * 1 - 11)) goto loc_0026B6B2;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a24 + (unsigned int)((unsigned int)(a1)) * 4))))) + (a8);
    a1 = (*(unsigned __int64 *)(a2)) * (result);
    a1 = (a1) >> (52);
    v_stack_p28 = a3;
    *(unsigned int *)(a7) = (unsigned int)(v_r15);
    result = (unsigned int)(((unsigned int)(a28)) + (0xFFFFULL));
    if (a3 <= a25) goto loc_0026B470;
    if ((*(unsigned __int8 *)(a2 - 1)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 - 1)))) goto loc_0026B720;
loc_0026B470:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(v_r10)));
    v_stack_pD8 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < 15) goto loc_0026B707;
    *(unsigned __int8 *)(a26) = 240;
    v_stack_pE0 = (unsigned int)(a1 - 15);
    result = *(unsigned __int8 *)(a3 - 1);
    v_rbx = v_rsi + 1;
    v_r10 = a26 + 1;
    v_r11 = v_rsi + 1 + v_rdi * 1;
    v_r15 = a26 + 1;
    if (((unsigned int)(a1 - 15)) >= 255) {
        result = 0x80808081ULL;
        a1 = a26 + 1;
        a2 = (unsigned int)((a1 - 15) >> (7));
        v_rbx = (unsigned int)(a2);
        a3 = (unsigned int)(a2);
        a2 = 255;
        result = memset(a1, a2, a3, a2);
        a2 = a28;
        v_r10 = a26 + 1 + v_rbx * 1;
        a3 = a5;
        v_r15 = v_r10;
        a1 = a27;
        a4 = v_stack_p20;
        result = (unsigned int)((result) * ((unsigned int)(v_rbx)));
        a2 = (unsigned int)((a2) + ((unsigned int)(result)));
        v_r11 = 0;
    }
    *(unsigned __int8 *)(v_r15) = (unsigned __int8)(a2);
loc_0026B4EC:
    a2 = ((unsigned int)((unsigned int)(a1))) + (v_r10 + 1);
    v_r12 = (v_r10) - (v_r10 + 1);
loc_0026B4F4:
    *(unsigned __int64 *)(v_r10 + 1) = *(unsigned __int64 *)(v_r10 + 1 + v_r12 * 1);
    v_r15 = (v_r10 + 1) + (8);
    if (v_r15 < a2) goto loc_0026B4F4;
    v_stack_p20 = v_r10 + v_rsi + 1 * 1 - 5 - 7;
loc_0026B520:
    result = (unsigned __int16)(((unsigned __int16)(a4)) - ((unsigned __int16)(a3)));
    *(unsigned __int16 *)(a2) = (unsigned __int16)(result);
    if ((a4 + 4) >= (v_r10 + v_rsi + 1 * 1 - 5 - 7)) goto loc_0026B55E;
    a3 = (*(unsigned __int64 *)(a4 + 4)) ^ (*(unsigned __int64 *)(a3 + 4));
    if (condition_is_equal) goto loc_0026B556;
    a3 = (unsigned int)((a3) >> (3));
    goto loc_0026B584;
loc_0026B556:
loc_0026B55A:
    a2 = (a3 + 4) + (8);
loc_0026B55E:
    if ((a4 + 4 + 8) >= v_stack_p20) goto loc_0026B629;
    a3 = (*(unsigned __int64 *)(a4 + 4 + 8)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_equal) goto loc_0026B6A9;
    a3 = (unsigned int)((a3) >> (3));
    a3 = (unsigned int)((a3) - ((unsigned int)(a4 + 4)));
    a3 = (unsigned int)((a3) + ((unsigned int)(a4 + 4 + 8)));
loc_0026B584:
    v_r12 = (a4) + (4);
    v_r12 = (v_r12) + ((unsigned int)((unsigned int)(a3)));
    if (((unsigned int)(a3)) >= 15) goto loc_0026B673;
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(*(unsigned __int8 *)(a26))));
    *(unsigned __int8 *)(a26) = (unsigned __int8)(a3);
loc_0026B5A2:
    if (v_r12 >= (v_r10 + v_rsi + 1 * 1 - 11)) goto loc_0026B6B2;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - (a8));
    result = (*(unsigned __int64 *)(v_r12 - 2)) * (a3);
    result = (result) >> (52);
    *(unsigned int *)(a24 + result * 4) = (unsigned int)(a2 - 2);
    result = (*(unsigned __int64 *)(v_r12)) * (a3);
    result = (result) >> (52);
    *(unsigned int *)(a24 + result * 4) = (unsigned int)(a2);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a24 + result * 4))))) + (a8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a24 + result * 4)) + 65535)) >= ((unsigned int)(a2))) goto loc_0026B7D3;
loc_0026B607:
    a1 = (*(unsigned __int64 *)(v_r12 + 1)) * ((unsigned int)(*(unsigned int *)(a24 + result * 4)) + 65535);
    goto loc_0026B3A6;
loc_0026B629:
    if (a1 >= (v_r10 + v_rsi + 1 * 1 - 5 - 3)) goto loc_0026B640;
    if ((*(unsigned int *)(v_r12 + 1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (v_r12 + 1) + (4);
    }
    if (a1 >= (v_r10 + v_rsi + 1 * 1 - 5 - 1)) goto loc_0026B659;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= (v_r10 + v_rsi + 1 * 1 - 5)) goto loc_0026B668;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(a4 + 4)));
    goto loc_0026B584;
loc_0026B673:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1)) + (15));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) + (-15));
    *(unsigned __int8 *)(a8) = (unsigned __int8)(result);
    *(unsigned int *)(a2 + 2) = 0xFFFFFFFFULL;
    if (((unsigned int)(a3)) >= 0x3FCULL) goto loc_0026B6E1;
loc_0026B68B:
    a2 = (unsigned int)((a2) >> (7));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(a2 + a2 + 2 * 1) = (unsigned __int8)(a3);
    goto loc_0026B5A2;
loc_0026B6A9:
    a1 = (a2 + a2 + 2 * 1) + (8);
    goto loc_0026B55A;
loc_0026B6B2:
    v_rdi = (v_r10 + v_rsi + 1 * 1) - (v_r12);
    if (v_rdi < 15) goto loc_0026B827;
    *(unsigned __int8 *)(a2 + a2 + 2 * 1 + 1) = 240;
    v_rsi = (a2 + a2 + 2 * 1 + 1) + 1;
    if ((v_rdi - 15) >= 255) goto loc_0026B7F4;
loc_0026B6D6:
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(v_rdi - 15);
loc_0026B6D9:
    goto loc_0026ADB6;
loc_0026B6E1:
    a2 = (unsigned int)((v_r12) >> (9));
loc_0026B6EE:
    v_rsi = (v_rsi) + (4);
    a3 = (unsigned int)((a3) + (0xFFFFFC04ULL));
    *(unsigned int *)(v_rsi) = 0xFFFFFFFFULL;
    result = ((unsigned int)((unsigned int)(a2))) - (1);
    if (condition_is_equal) goto loc_0026B68B;
    goto loc_0026B6EE;
loc_0026B707:
    result = (unsigned __int8)(((unsigned __int8)(a1)) << (4));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(result);
    goto loc_0026B4EC;
loc_0026B720:
    a4 = (a8) - 1;
    a3 = (a3) - 1;
    v_stack_p20 = a4;
    v_stack_p28 = a3;
    a1 = (a4 > v_r12) ? 1 : 0;
    result = (a3 > a2) ? 1 : 0;
    if ((((unsigned int)(result)) & ((unsigned int)(a1))) == 0) goto loc_0026B470;
    if ((*(unsigned __int8 *)(a4 - 1)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 - 1)))) goto loc_0026B720;
    goto loc_0026B470;
loc_0026B762:
    *(unsigned __int8 *)(a4) = 0;
loc_0026B792:
    v_rbx = (a2) >> (7);
    result = memset(v_rsi, 255, v_rbx, a4);
    result = (result) * (v_rbx);
    v_rsi = (v_rsi) + (v_rbx);
    v_r14 = (v_r10 + v_rsi + 1 * 1 - 11) + (result);
    goto loc_0026ADB0;
loc_0026B7C5:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) << (4));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(result);
    goto loc_0026ADB3;
loc_0026B7D3:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_r12))))) goto loc_0026B607;
    *(unsigned __int8 *)(v_rsi) = 0;
    goto loc_0026B520;
loc_0026B7F4:
    v_rbx = (v_rsi + 1) >> (7);
    result = memset(v_rsi, 255, v_rbx, a4);
    result = (result) * (v_rbx);
    v_rsi = (v_rsi) + (v_rbx);
    v_rbp = (v_rdi - 15) + (result);
    goto loc_0026B6D6;
loc_0026B827:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) << (4));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(result);
    goto loc_0026B6D9;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0026A9FF(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7, void *Arg8, uint32_t Arg9, int64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, void *Arg24, void *Arg25, int64_t Arg26, uint32_t Arg27, uint32_t Arg28, uint32_t Arg29)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg24 = (uint8_t *)Arg24;
    uint8_t *arg25 = (uint8_t *)Arg25;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint32_t v_stack_pE8;

    if (((uint32_t)(local_rbx)) >= 0x1000BULL) goto loc_0026B315;
    if ((uint32_t)(local_rbx) == 0) goto loc_0026B762;
    Arg4 = (local_r10) - ((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)));
    v_stack_p28 = Arg4;
    *(uint32_t *)(arg24 + 0x4010) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)) + local_rbx * 1);
    *(uint32_t *)(arg24 + 0x4014) = 3;
    if (((uint32_t)(local_rbx)) < 13) goto loc_0026AD8C;
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(local_r10)));
    Arg1 = (Arg1) >> (19);
    *(uint16_t *)(arg24 + Arg1 * 2) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)));
loc_0026AA92:
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(local_r10 + 0x1)));
    v_stack_pE0 = (uint32_t)((uint32_t)((uint32_t)(local_r11)));
    v_stack_pD8 = 64;
    Arg1 = (uint32_t)((Arg1) >> (19));
    v_stack_p50 = local_r10 + 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + 1))) - (Arg5));
    v_stack_p48 = (uint32_t)(result);
    v_stack_p20 = Arg24 + (uint32_t)((uint32_t)(Arg1)) * 2;
    v_stack_p40 = (uint32_t)(*(uint16_t *)(arg24 + (uint32_t)((uint32_t)(Arg1)) * 2));
    Arg2 = (local_r10 + 1) + ((int32_t)(1));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg27)))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(Arg27)) + 1);
    v_stack_pE8 = (uint32_t)(result);
    v_stack_pD8 = (uint32_t)(Arg1);
    if (Arg2 > (local_r10 + local_rbx * 1 - 11)) goto loc_0026AD8C;
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(Arg2)));
    Arg3 = ((uint32_t)(Arg8)) + (Arg5);
    *(uint16_t *)(v_stack_p20) = (uint16_t)((uint32_t)(Arg9));
    Arg1 = (uint32_t)((Arg1) >> (19));
    v_stack_p30 = Arg3;
    if (Arg3 <= Arg25) goto loc_0026AB6B;
    if ((*(uint8_t *)(local_r10 + 0x1 - 0x1)) == ((uint8_t)(*(uint8_t *)(Arg3 - 0x1)))) goto loc_0026AE05;
loc_0026AB6B:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + 1))) - ((uint32_t)(local_r10)));
    v_stack_pE8 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < 15) goto loc_0026ADF8;
    *(uint8_t *)(Arg26) = 240;
    v_stack_pD8 = (uint32_t)(Arg1 - 15);
    result = *(uint8_t *)(Arg3 - 0x1);
    local_rbx = (uint32_t)((uint32_t)(local_r11));
    local_r10 = local_r10 + 1;
    local_r14 = Arg26 + 1;
    if (((uint32_t)(Arg1 - 15)) >= 255) {
        result = 0x80808081ULL;
        Arg1 = Arg26 + 1;
        Arg2 = (uint32_t)((Arg1 - 15) >> (7));
        local_rbx = (uint32_t)(Arg2);
        Arg3 = (uint32_t)(Arg2);
        Arg2 = 255;
        result = memset(Arg1, Arg2, Arg3, Arg26 + 1);
        Arg2 = Arg27;
        Arg4 = local_rbx + Arg26 + 1 * 1;
        Arg1 = Arg29;
        local_r14 = Arg4;
        Arg3 = Arg6;
        local_r10 = Arg10;
        result = (uint32_t)((result) * ((uint32_t)(local_rbx)));
        local_rbx = Arg28;
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
        local_r11 = 0;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg2);
loc_0026ABED:
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (Arg4 + 1);
    local_rbp = (local_r10) - (Arg4 + 1);
loc_0026ABF5:
    *(uint64_t *)(arg4 + 0x1) = *(uint64_t *)(arg4 + 0x1 + local_rbp * 1);
    local_r14 = (Arg4 + 1) + (8);
    if (local_r14 < Arg2) goto loc_0026ABF5;
    v_stack_p30 = local_r10 + local_rbx * 1 - 5 - 7;
loc_0026AC10:
    result = (uint16_t)(((uint16_t)(local_r10)) - ((uint16_t)(Arg3)));
    *(uint16_t *)(Arg2) = (uint16_t)(result);
    if ((local_r10 + 4) >= (local_r10 + local_rbx * 1 - 5 - 7)) goto loc_0026AC4D;
    Arg3 = (*(uint64_t *)(local_r10 + 0x4)) ^ (*(uint64_t *)(Arg3 + 0x4));
    if (condition_is_equal) goto loc_0026AC45;
    Arg3 = (uint32_t)((Arg3) >> (3));
    goto loc_0026AC73;
loc_0026AC45:
loc_0026AC49:
    Arg2 = (Arg3 + 4) + (8);
loc_0026AC4D:
    if ((local_r10 + 4 + 8) >= Arg6) goto loc_0026AD03;
    Arg3 = (*(uint64_t *)(local_r10 + 0x4 + 0x8)) ^ (*(uint64_t *)(Arg2));
    if (condition_is_equal) goto loc_0026AD83;
    Arg3 = (uint32_t)((Arg3) >> (3));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(local_r10 + 4)));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r10 + 4 + 8)));
loc_0026AC73:
    local_r10 = (local_r10) + (4);
    local_r10 = (local_r10) + ((uint32_t)((uint32_t)(Arg3)));
    if (((uint32_t)(Arg3)) >= 15) goto loc_0026AD4D;
    result = (uint8_t)((*(uint8_t *)(Arg26)) + ((uint8_t)(Arg3)));
    *(uint8_t *)(Arg26) = (uint8_t)(result);
loc_0026AC91:
    if (local_r10 >= (local_r10 + local_rbx * 1 - 11)) goto loc_0026AD8C;
    Arg1 = (uint32_t)((local_r10 + 4 + 8) * (*(uint32_t *)(local_r10 - 0x2)));
    Arg2 = (uint16_t)(((uint16_t)(local_r10)) - ((uint16_t)(Arg5)));
    Arg2 = (uint16_t)((Arg2) - (2));
    Arg1 = (Arg1) >> (19);
    *(uint16_t *)(arg24 + Arg1 * 2) = (uint16_t)(Arg2);
    result = (uint32_t)((result) * (*(uint32_t *)(local_r10)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (Arg5));
    result = (uint32_t)((result) >> (19));
    *(uint16_t *)(arg24 + result * 2) = (uint16_t)(Arg2);
    Arg3 = (*(uint16_t *)(arg24 + result * 2)) + (Arg5);
    if ((*(uint32_t *)(Arg3)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10))))) goto loc_0026AA92;
    *(uint8_t *)(Arg2 + 0x2) = 0;
    goto loc_0026AC10;
loc_0026AD03:
    if ((Arg24 + result * 2) >= (local_r10 + local_rbx * 1 - 5 - 3)) goto loc_0026AD1A;
    if ((*(uint32_t *)(Arg2 + 0x2 + 0x1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg24 + result * 2))))) {
        Arg1 = (Arg24 + result * 2) + (4);
        Arg2 = (Arg2 + 2 + 1) + (4);
    }
    if (Arg1 >= (local_r10 + local_rbx * 1 - 5 - 1)) goto loc_0026AD33;
    if ((*(uint16_t *)(Arg2)) == ((uint16_t)(*(uint16_t *)(Arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= (local_r10 + local_rbx * 1 - 5)) goto loc_0026AD42;
    if ((*(uint8_t *)(Arg2)) == ((uint8_t)(*(uint8_t *)(Arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 4)));
    goto loc_0026AC73;
loc_0026AD4D:
    result = (uint8_t)((*(uint8_t *)(Arg1)) + (15));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + (-15));
    *(uint8_t *)(Arg5) = (uint8_t)(result);
    *(uint32_t *)(Arg2 + 0x2) = 0xFFFFFFFFULL;
    if (((uint32_t)(Arg3)) >= 0x3FCULL) goto loc_0026ADCE;
loc_0026AD65:
    Arg2 = (uint32_t)((Arg2) >> (7));
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(Arg2)));
    *(uint8_t *)(Arg2 + Arg2 + 0x2 * 1) = (uint8_t)(Arg3);
    goto loc_0026AC91;
loc_0026AD83:
    Arg1 = (Arg2 + Arg2 + 2 * 1) + (8);
    goto loc_0026AC49;
loc_0026AD8C:
    local_rdi = (local_r10 + local_rbx * 1) - (Arg6);
    if (local_rdi < 15) goto loc_0026B7C5;
    *(uint8_t *)(Arg2 + Arg2 + 0x2 * 1 + 0x1) = 240;
    local_rsi = (Arg2 + Arg2 + 2 * 1 + 1) + 1;
    if ((local_rdi - 15) >= 255) goto loc_0026B792;
loc_0026ADB0:
    *(uint8_t *)(local_rsi) = (uint8_t)(local_rdi - 15);
loc_0026ADB3:
loc_0026ADB6:
    result = memcpy(local_rsi + 1, Arg6, local_rdi, Arg5);
loc_0026ADCE:
    Arg2 = (uint32_t)((Arg6) >> (9));
loc_0026ADDB:
    local_rsi = (local_rsi) + (4);
    Arg3 = (uint32_t)((local_rdi) + (0xFFFFFC04ULL));
    *(uint32_t *)(local_rsi) = 0xFFFFFFFFULL;
    result = ((uint32_t)((uint32_t)(Arg2))) - (1);
    if (condition_is_equal) goto loc_0026AD65;
    goto loc_0026ADDB;
loc_0026ADF8:
    result = (uint8_t)(((uint8_t)(local_rsi + 1)) << (4));
    *(uint8_t *)(local_rsi) = (uint8_t)(result);
    goto loc_0026ABED;
loc_0026AE05:
loc_0026AE10:
    local_r10 = (local_r10) - 1;
    Arg3 = (Arg3) - 1;
    v_stack_p50 = local_r10;
    v_stack_p30 = Arg3;
    Arg1 = (local_r10 > Arg6) ? 1 : 0;
    result = (Arg3 > Arg25) ? 1 : 0;
    if ((((uint32_t)(result)) & ((uint32_t)(Arg1))) == 0) goto loc_0026AB6B;
    if ((*(uint8_t *)(local_r10 - 0x1)) == ((uint8_t)(*(uint8_t *)(Arg3 - 0x1)))) goto loc_0026AE10;
    goto loc_0026AB6B;
loc_0026B315:
    Arg4 = (local_r10) - ((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)));
    *(uint32_t *)(arg24 + 0x4010) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)) + local_rsi + 1 * 1);
    *(uint32_t *)(arg24 + 0x4014) = 2;
    result = (*(uint64_t *)(arg25)) * (Arg3);
    v_stack_p40 = Arg4;
    result = (result) >> (52);
    Arg2 = (Arg25) + 1;
    *(uint32_t *)(arg24 + result * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4010)));
    Arg1 = (*(uint64_t *)(Arg2)) * (Arg3);
loc_0026B3A6:
    v_stack_p48 = (uint32_t)((uint32_t)((uint32_t)(local_rsi + 1 + local_rdi * 1)));
    Arg1 = (Arg1) >> (52);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg4)));
    v_stack_p20 = Arg2;
    v_stack_p38 = Arg24 + (uint32_t)((uint32_t)(Arg1)) * 4;
    Arg2 = (Arg2) + ((int32_t)(1));
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg24 + (uint32_t)((uint32_t)(Arg1)) * 4)));
    local_r10 = (uint32_t)((1 + 63) + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)(1 + 63))) >> (6));
    v_stack_pD8 = (uint32_t)(result);
    if (Arg2 > (local_r10 + local_rsi + 1 * 1 - 11)) goto loc_0026B6B2;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg24 + (uint32_t)((uint32_t)(Arg1)) * 4))))) + (Arg8);
    Arg1 = (*(uint64_t *)(Arg2)) * (result);
    Arg1 = (Arg1) >> (52);
    v_stack_p28 = Arg3;
    *(uint32_t *)(arg7) = (uint32_t)(local_r15);
    result = (uint32_t)(((uint32_t)(Arg28)) + (0xFFFFULL));
    if (Arg3 <= Arg25) goto loc_0026B470;
    if ((*(uint8_t *)(Arg2 - 0x1)) == ((uint8_t)(*(uint8_t *)(Arg3 - 0x1)))) goto loc_0026B720;
loc_0026B470:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(local_r10)));
    v_stack_pD8 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < 15) goto loc_0026B707;
    *(uint8_t *)(Arg26) = 240;
    v_stack_pE0 = (uint32_t)(Arg1 - 15);
    result = *(uint8_t *)(Arg3 - 0x1);
    local_rbx = local_rsi + 1;
    local_r10 = Arg26 + 1;
    local_r11 = local_rsi + 1 + local_rdi * 1;
    local_r15 = Arg26 + 1;
    if (((uint32_t)(Arg1 - 15)) >= 255) {
        result = 0x80808081ULL;
        Arg1 = Arg26 + 1;
        Arg2 = (uint32_t)((Arg1 - 15) >> (7));
        local_rbx = (uint32_t)(Arg2);
        Arg3 = (uint32_t)(Arg2);
        Arg2 = 255;
        result = memset(Arg1, Arg2, Arg3, Arg2);
        Arg2 = Arg28;
        local_r10 = Arg26 + 1 + local_rbx * 1;
        Arg3 = Arg5;
        local_r15 = local_r10;
        Arg1 = Arg27;
        Arg4 = v_stack_p20;
        result = (uint32_t)((result) * ((uint32_t)(local_rbx)));
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
        local_r11 = 0;
    }
    *(uint8_t *)(local_r15) = (uint8_t)(Arg2);
loc_0026B4EC:
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (local_r10 + 1);
    local_r12 = (local_r10) - (local_r10 + 1);
loc_0026B4F4:
    *(uint64_t *)(local_r10 + 0x1) = *(uint64_t *)(local_r10 + 0x1 + local_r12 * 1);
    local_r15 = (local_r10 + 1) + (8);
    if (local_r15 < Arg2) goto loc_0026B4F4;
    v_stack_p20 = local_r10 + local_rsi + 1 * 1 - 5 - 7;
loc_0026B520:
    result = (uint16_t)(((uint16_t)(Arg4)) - ((uint16_t)(Arg3)));
    *(uint16_t *)(Arg2) = (uint16_t)(result);
    if ((Arg4 + 4) >= (local_r10 + local_rsi + 1 * 1 - 5 - 7)) goto loc_0026B55E;
    Arg3 = (*(uint64_t *)(arg4 + 0x4)) ^ (*(uint64_t *)(Arg3 + 0x4));
    if (condition_is_equal) goto loc_0026B556;
    Arg3 = (uint32_t)((Arg3) >> (3));
    goto loc_0026B584;
loc_0026B556:
loc_0026B55A:
    Arg2 = (Arg3 + 4) + (8);
loc_0026B55E:
    if ((Arg4 + 4 + 8) >= v_stack_p20) goto loc_0026B629;
    Arg3 = (*(uint64_t *)(arg4 + 0x4 + 0x8)) ^ (*(uint64_t *)(Arg2));
    if (condition_is_equal) goto loc_0026B6A9;
    Arg3 = (uint32_t)((Arg3) >> (3));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(Arg4 + 4)));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(Arg4 + 4 + 8)));
loc_0026B584:
    local_r12 = (Arg4) + (4);
    local_r12 = (local_r12) + ((uint32_t)((uint32_t)(Arg3)));
    if (((uint32_t)(Arg3)) >= 15) goto loc_0026B673;
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(*(uint8_t *)(Arg26))));
    *(uint8_t *)(Arg26) = (uint8_t)(Arg3);
loc_0026B5A2:
    if (local_r12 >= (local_r10 + local_rsi + 1 * 1 - 11)) goto loc_0026B6B2;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - (Arg8));
    result = (*(uint64_t *)(local_r12 - 0x2)) * (Arg3);
    result = (result) >> (52);
    *(uint32_t *)(arg24 + result * 4) = (uint32_t)(Arg2 - 2);
    result = (*(uint64_t *)(local_r12)) * (Arg3);
    result = (result) >> (52);
    *(uint32_t *)(arg24 + result * 4) = (uint32_t)(Arg2);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg24 + result * 4))))) + (Arg8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg24 + result * 4)) + 65535)) >= ((uint32_t)(Arg2))) goto loc_0026B7D3;
loc_0026B607:
    Arg1 = (*(uint64_t *)(local_r12 + 0x1)) * ((uint32_t)(*(uint32_t *)(arg24 + result * 4)) + 65535);
    goto loc_0026B3A6;
loc_0026B629:
    if (Arg1 >= (local_r10 + local_rsi + 1 * 1 - 5 - 3)) goto loc_0026B640;
    if ((*(uint32_t *)(local_r12 + 0x1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (local_r12 + 1) + (4);
    }
    if (Arg1 >= (local_r10 + local_rsi + 1 * 1 - 5 - 1)) goto loc_0026B659;
    if ((*(uint16_t *)(Arg2)) == ((uint16_t)(*(uint16_t *)(Arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= (local_r10 + local_rsi + 1 * 1 - 5)) goto loc_0026B668;
    if ((*(uint8_t *)(Arg2)) == ((uint8_t)(*(uint8_t *)(Arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg4 + 4)));
    goto loc_0026B584;
loc_0026B673:
    result = (uint8_t)((*(uint8_t *)(Arg1)) + (15));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + (-15));
    *(uint8_t *)(arg8) = (uint8_t)(result);
    *(uint32_t *)(Arg2 + 0x2) = 0xFFFFFFFFULL;
    if (((uint32_t)(Arg3)) >= 0x3FCULL) goto loc_0026B6E1;
loc_0026B68B:
    Arg2 = (uint32_t)((Arg2) >> (7));
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(Arg2)));
    *(uint8_t *)(Arg2 + Arg2 + 0x2 * 1) = (uint8_t)(Arg3);
    goto loc_0026B5A2;
loc_0026B6A9:
    Arg1 = (Arg2 + Arg2 + 2 * 1) + (8);
    goto loc_0026B55A;
loc_0026B6B2:
    local_rdi = (local_r10 + local_rsi + 1 * 1) - (local_r12);
    if (local_rdi < 15) goto loc_0026B827;
    *(uint8_t *)(Arg2 + Arg2 + 0x2 * 1 + 0x1) = 240;
    local_rsi = (Arg2 + Arg2 + 2 * 1 + 1) + 1;
    if ((local_rdi - 15) >= 255) goto loc_0026B7F4;
loc_0026B6D6:
    *(uint8_t *)(local_rsi) = (uint8_t)(local_rdi - 15);
loc_0026B6D9:
    goto loc_0026ADB6;
loc_0026B6E1:
    Arg2 = (uint32_t)((local_r12) >> (9));
loc_0026B6EE:
    local_rsi = (local_rsi) + (4);
    Arg3 = (uint32_t)((Arg3) + (0xFFFFFC04ULL));
    *(uint32_t *)(local_rsi) = 0xFFFFFFFFULL;
    result = ((uint32_t)((uint32_t)(Arg2))) - (1);
    if (condition_is_equal) goto loc_0026B68B;
    goto loc_0026B6EE;
loc_0026B707:
    result = (uint8_t)(((uint8_t)(Arg1)) << (4));
    *(uint8_t *)(local_rsi) = (uint8_t)(result);
    goto loc_0026B4EC;
loc_0026B720:
    Arg4 = (Arg8) - 1;
    Arg3 = (Arg3) - 1;
    v_stack_p20 = Arg4;
    v_stack_p28 = Arg3;
    Arg1 = (Arg4 > local_r12) ? 1 : 0;
    result = (Arg3 > Arg2) ? 1 : 0;
    if ((((uint32_t)(result)) & ((uint32_t)(Arg1))) == 0) goto loc_0026B470;
    if ((*(uint8_t *)(arg4 - 0x1)) == ((uint8_t)(*(uint8_t *)(Arg3 - 0x1)))) goto loc_0026B720;
    goto loc_0026B470;
loc_0026B762:
    *(uint8_t *)(arg4) = 0;
loc_0026B792:
    local_rbx = (Arg2) >> (7);
    result = memset(local_rsi, 255, local_rbx, Arg4);
    result = (result) * (local_rbx);
    local_rsi = (local_rsi) + (local_rbx);
    local_r14 = (local_r10 + local_rsi + 1 * 1 - 11) + (result);
    goto loc_0026ADB0;
loc_0026B7C5:
    result = (uint8_t)(((uint8_t)(local_rdi)) << (4));
    *(uint8_t *)(local_rsi) = (uint8_t)(result);
    goto loc_0026ADB3;
loc_0026B7D3:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_r12))))) goto loc_0026B607;
    *(uint8_t *)(local_rsi) = 0;
    goto loc_0026B520;
loc_0026B7F4:
    local_rbx = (local_rsi + 1) >> (7);
    result = memset(local_rsi, 255, local_rbx, Arg4);
    result = (result) * (local_rbx);
    local_rsi = (local_rsi) + (local_rbx);
    local_rbp = (local_rdi - 15) + (result);
    goto loc_0026B6D6;
loc_0026B827:
    result = (uint8_t)(((uint8_t)(local_rdi)) << (4));
    *(uint8_t *)(local_rsi) = (uint8_t)(result);
    goto loc_0026B6D9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `8` | `W` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg24` | `+ 0x0` | `16` | `R` |
| `Arg24` | `+ 0x0` | `16` | `W` |
| `Arg24` | `+ 0x0` | `32` | `R` |
| `Arg24` | `+ 0x0 + rax*2` | `16` | `R` |
| `Arg24` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg24` | `+ 0x0 + rax*4` | `32` | `R` |
| `Arg24` | `+ 0x0 + rax*4` | `32` | `W` |
| `Arg24` | `+ 0x0 + rax*4` | `64` | `R` |
| `Arg24` | `+ 0x0 + rcx*2` | `16` | `W` |
| `Arg24` | `+ 0x4010` | `32` | `W` |
| `Arg24` | `+ 0x4014` | `32` | `W` |
| `Arg24` | `+ 0x4018` | `32` | `R/W` |
| `Arg25` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026A9FF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
