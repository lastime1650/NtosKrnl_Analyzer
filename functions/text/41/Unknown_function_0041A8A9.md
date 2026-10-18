# sub_0041A8A9

- RVA: `0x0041A8A9`–`0x0041AE2A` (길이 `1,409` bytes)
- VA: `0x000000014041A8A9`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009D400`
- 디코드: `356`개 명령, `1,409/1,409` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0041A8C4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0041AA19` → [RtlpMakeXpressCallback](RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0041A98B` → RVA `0x00013610` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0041AE28` → [sub_0041AE2A + 0x3B](Unknown_function_0041AE2A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041A8A9  4C 89 AC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r13
0041A8B1  33 D2                           xor edx, edx
0041A8B3  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0041A8BB  41 B8 00 00 04 00               mov r8d, 0x40000
0041A8C1  49 8B CD                        mov rcx, r13
0041A8C4  E8 77 C3 2A 00                  call 0x1406c6c40
0041A8C9  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0041A8D1  48 8D 57 FB                     lea rdx, [rdi - 5]
0041A8D5  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
0041A8DA  4C 8D 46 D7                     lea r8, [rsi - 0x29]
0041A8DE  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0041A8E3  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0041A8E8  48 85 C0                        test rax, rax
0041A8EB  74 0B                           je 0x14041a8f8
0041A8ED  8B BC 24 00 01 00 00            mov edi, dword ptr [rsp + 0x100]
0041A8F4  3B FB                           cmp edi, ebx
0041A8F6  76 09                           jbe 0x14041a901
0041A8F8  8B FB                           mov edi, ebx
0041A8FA  89 9C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ebx
0041A901  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0041A909  4D 8D 7E 05                     lea r15, [r14 + 5]
0041A90D  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0041A912  48 8D 5D 01                     lea rbx, [rbp + 1]
0041A916  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0041A91E  41 B9 02 00 00 00               mov r9d, 2
0041A924  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0041A929  45 33 D2                        xor r10d, r10d
0041A92C  0F B6 45 00                     movzx eax, byte ptr [rbp]
0041A930  41 88 46 04                     mov byte ptr [r14 + 4], al
0041A934  4C 8B F5                        mov r14, rbp
0041A937  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
0041A93B  44 89 8C 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r9d
0041A943  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0041A948  49 8D 86 00 20 00 00            lea rax, [r14 + 0x2000]
0041A94F  4C 8B DA                        mov r11, rdx
0041A952  48 3B C2                        cmp rax, rdx
0041A955  4C 0F 46 D8                     cmovbe r11, rax
0041A959  8B C7                           mov eax, edi
0041A95B  48 03 C3                        add rax, rbx
0041A95E  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0041A963  4C 3B D8                        cmp r11, rax
0041A966  49 0F 42 C3                     cmovb rax, r11
0041A96A  41 81 E2 FF 3F 00 00            and r10d, 0x3fff
0041A971  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0041A976  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0041A97B  4D 3B F3                        cmp r14, r11
0041A97E  73 71                           jae 0x14041a9f1
0041A980  4E 8D 04 D5 00 00 04 00         lea r8, [r10*8 + 0x40000]
0041A988  4D 03 C5                        add r8, r13
0041A98B  4C 8D 0D 7E 8C BF FF            lea r9, [rip - 0x407382]
0041A992  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
0041A997  4D 8D 40 08                     lea r8, [r8 + 8]
0041A99B  49 FF C2                        inc r10
0041A99E  41 0F B7 94 41 00 02 00 00      movzx edx, word ptr [r9 + rax*2 + 0x200]
0041A9A7  41 0F B6 46 02                  movzx eax, byte ptr [r14 + 2]
0041A9AC  41 0F B7 84 41 00 04 00 00      movzx eax, word ptr [r9 + rax*2 + 0x400]
0041A9B5  48 33 D0                        xor rdx, rax
0041A9B8  41 0F B6 06                     movzx eax, byte ptr [r14]
0041A9BC  41 0F B7 0C 41                  movzx ecx, word ptr [r9 + rax*2]
0041A9C1  48 33 D1                        xor rdx, rcx
0041A9C4  49 8B 44 D5 00                  mov rax, qword ptr [r13 + rdx*8]
0041A9C9  49 89 40 F8                     mov qword ptr [r8 - 8], rax
0041A9CD  4D 89 74 D5 00                  mov qword ptr [r13 + rdx*8], r14
0041A9D2  49 FF C6                        inc r14
0041A9D5  4D 3B F3                        cmp r14, r11
0041A9D8  72 B8                           jb 0x14041a992
0041A9DA  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
0041A9E2  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0041A9E7  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0041A9EC  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0041A9F1  BF 00 20 00 00                  mov edi, 0x2000
0041A9F6  48 8D B3 00 E0 FF FF            lea rsi, [rbx - 0x2000]
0041A9FD  48 2B FD                        sub rdi, rbp
0041AA00  48 3B D8                        cmp rbx, rax
0041AA03  72 30                           jb 0x14041aa35
0041AA05  49 3B DB                        cmp rbx, r11
0041AA08  0F 83 E6 03 00 00               jae 0x14041adf4
0041AA0E  4C 8B C3                        mov r8, rbx
0041AA11  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
0041AA16  49 8B D3                        mov rdx, r11
0041AA19  E8 D2 FD FF FF                  call 0x14041a7f0
0041AA1E  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
0041AA26  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
0041AA2B  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0041AA30  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0041AA35  48 8D 0C 37                     lea rcx, [rdi + rsi]
0041AA39  81 E1 FF 3F 00 00               and ecx, 0x3fff
0041AA3F  49 8B 8C CD 00 00 04 00         mov rcx, qword ptr [r13 + rcx*8 + 0x40000]
0041AA47  44 8B 2B                        mov r13d, dword ptr [rbx]
0041AA4A  48 3B CE                        cmp rcx, rsi
0041AA4D  72 73                           jb 0x14041aac2
0041AA4F  41 8B D5                        mov edx, r13d
0041AA52  33 11                           xor edx, dword ptr [rcx]
0041AA54  0F 84 F9 00 00 00               je 0x14041ab53
0041AA5A  F7 C2 FF FF FF 00               test edx, 0xffffff
0041AA60  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
0041AA68  0F 84 C4 00 00 00               je 0x14041ab32
0041AA6E  48 2B CD                        sub rcx, rbp
0041AA71  81 E1 FF 3F 00 00               and ecx, 0x3fff
0041AA77  48 8B 8C CA 00 00 04 00         mov rcx, qword ptr [rdx + rcx*8 + 0x40000]
0041AA7F  48 3B CE                        cmp rcx, rsi
0041AA82  72 3E                           jb 0x14041aac2
0041AA84  41 8B C5                        mov eax, r13d
0041AA87  33 01                           xor eax, dword ptr [rcx]
0041AA89  0F 84 C4 00 00 00               je 0x14041ab53
0041AA8F  A9 FF FF FF 00                  test eax, 0xffffff
0041AA94  0F 84 98 00 00 00               je 0x14041ab32
0041AA9A  48 2B CD                        sub rcx, rbp
0041AA9D  81 E1 FF 3F 00 00               and ecx, 0x3fff
0041AAA3  48 8B 8C CA 00 00 04 00         mov rcx, qword ptr [rdx + rcx*8 + 0x40000]
0041AAAB  48 3B CE                        cmp rcx, rsi
0041AAAE  72 12                           jb 0x14041aac2
0041AAB0  41 8B C5                        mov eax, r13d
0041AAB3  33 01                           xor eax, dword ptr [rcx]
0041AAB5  0F 84 98 00 00 00               je 0x14041ab53
0041AABB  A9 FF FF FF 00                  test eax, 0xffffff
0041AAC0  74 70                           je 0x14041ab32
0041AAC2  45 88 2F                        mov byte ptr [r15], r13b
0041AAC5  43 8D 04 09                     lea eax, [r9 + r9]
0041AAC9  49 FF C7                        inc r15
0041AACC  48 FF C3                        inc rbx
0041AACF  48 FF C6                        inc rsi
0041AAD2  49 8B CF                        mov rcx, r15
0041AAD5  45 85 C9                        test r9d, r9d
0041AAD8  7E 1C                           jle 0x14041aaf6
0041AADA  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0041AAE2  44 8B C8                        mov r9d, eax
0041AAE5  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0041AAEC  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0041AAF1  E9 0A FF FF FF                  jmp 0x14041aa00
0041AAF6  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
0041AAFB  49 83 C7 04                     add r15, 4
0041AAFF  41 B9 01 00 00 00               mov r9d, 1
0041AB05  4C 8B D1                        mov r10, rcx
0041AB08  44 89 8C 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r9d
0041AB10  89 02                           mov dword ptr [rdx], eax
0041AB12  4D 3B F8                        cmp r15, r8
0041AB15  0F 83 F8 02 00 00               jae 0x14041ae13
0041AB1B  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0041AB23  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0041AB28  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0041AB2D  E9 CE FE FF FF                  jmp 0x14041aa00
0041AB32  4C 8B E3                        mov r12, rbx
0041AB35  48 8D B3 00 E0 FF FF            lea rsi, [rbx - 0x2000]
0041AB3C  4C 2B E1                        sub r12, rcx
0041AB3F  33 C0                           xor eax, eax
0041AB41  8B E8                           mov ebp, eax
0041AB43  8D 78 03                        lea edi, [rax + 3]
0041AB46  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0041AB4E  E9 88 01 00 00                  jmp 0x14041acdb
0041AB53  33 C0                           xor eax, eax
0041AB55  8B E8                           mov ebp, eax
0041AB57  8D 78 03                        lea edi, [rax + 3]
0041AB5A  4C 8B DB                        mov r11, rbx
0041AB5D  48 83 C3 04                     add rbx, 4
0041AB61  48 83 C1 04                     add rcx, 4
0041AB65  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0041AB6A  4C 8D 53 20                     lea r10, [rbx + 0x20]
0041AB6E  4D 3B D0                        cmp r10, r8
0041AB71  0F 83 D7 00 00 00               jae 0x14041ac4e
0041AB77  8B 03                           mov eax, dword ptr [rbx]
0041AB79  8B 11                           mov edx, dword ptr [rcx]
0041AB7B  3B C2                           cmp eax, edx
0041AB7D  0F 85 99 00 00 00               jne 0x14041ac1c
0041AB83  8B 43 04                        mov eax, dword ptr [rbx + 4]
0041AB86  8B 51 04                        mov edx, dword ptr [rcx + 4]
0041AB89  3B C2                           cmp eax, edx
0041AB8B  0F 85 83 00 00 00               jne 0x14041ac14
0041AB91  8B 43 08                        mov eax, dword ptr [rbx + 8]
0041AB94  8B 51 08                        mov edx, dword ptr [rcx + 8]
0041AB97  3B C2                           cmp eax, edx
0041AB99  75 6F                           jne 0x14041ac0a
0041AB9B  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0041AB9E  8B 51 0C                        mov edx, dword ptr [rcx + 0xc]
0041ABA1  3B C2                           cmp eax, edx
0041ABA3  75 5B                           jne 0x14041ac00
0041ABA5  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0041ABA8  8B 51 10                        mov edx, dword ptr [rcx + 0x10]
0041ABAB  3B C2                           cmp eax, edx
0041ABAD  75 47                           jne 0x14041abf6
0041ABAF  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0041ABB2  8B 51 14                        mov edx, dword ptr [rcx + 0x14]
0041ABB5  3B C2                           cmp eax, edx
0041ABB7  75 33                           jne 0x14041abec
0041ABB9  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0041ABBC  8B 51 18                        mov edx, dword ptr [rcx + 0x18]
0041ABBF  3B C2                           cmp eax, edx
0041ABC1  75 1F                           jne 0x14041abe2
0041ABC3  8B 51 1C                        mov edx, dword ptr [rcx + 0x1c]
0041ABC6  48 8D 43 1C                     lea rax, [rbx + 0x1c]
0041ABCA  48 8B D8                        mov rbx, rax
0041ABCD  8B 00                           mov eax, dword ptr [rax]
0041ABCF  3B C2                           cmp eax, edx
0041ABD1  75 09                           jne 0x14041abdc
0041ABD3  49 8B DA                        mov rbx, r10
0041ABD6  48 83 C1 20                     add rcx, 0x20
0041ABDA  EB 89                           jmp 0x14041ab65
0041ABDC  48 83 C1 1C                     add rcx, 0x1c
0041ABE0  EB 3A                           jmp 0x14041ac1c
0041ABE2  48 83 C3 18                     add rbx, 0x18
0041ABE6  48 83 C1 18                     add rcx, 0x18
0041ABEA  EB 30                           jmp 0x14041ac1c
0041ABEC  48 83 C3 14                     add rbx, 0x14
0041ABF0  48 83 C1 14                     add rcx, 0x14
0041ABF4  EB 26                           jmp 0x14041ac1c
0041ABF6  48 83 C3 10                     add rbx, 0x10
0041ABFA  48 83 C1 10                     add rcx, 0x10
0041ABFE  EB 1C                           jmp 0x14041ac1c
0041AC00  48 83 C3 0C                     add rbx, 0xc
0041AC04  48 83 C1 0C                     add rcx, 0xc
0041AC08  EB 12                           jmp 0x14041ac1c
0041AC0A  48 83 C3 08                     add rbx, 8
0041AC0E  48 83 C1 08                     add rcx, 8
0041AC12  EB 08                           jmp 0x14041ac1c
0041AC14  48 83 C3 04                     add rbx, 4
0041AC18  48 83 C1 04                     add rcx, 4
0041AC1C  3A C2                           cmp al, dl
0041AC1E  75 45                           jne 0x14041ac65
0041AC20  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0041AC24  38 43 01                        cmp byte ptr [rbx + 1], al
0041AC27  74 08                           je 0x14041ac31
0041AC29  48 FF C3                        inc rbx
0041AC2C  48 FF C1                        inc rcx
0041AC2F  EB 34                           jmp 0x14041ac65
0041AC31  0F B6 41 02                     movzx eax, byte ptr [rcx + 2]
0041AC35  38 43 02                        cmp byte ptr [rbx + 2], al
0041AC38  74 0A                           je 0x14041ac44
0041AC3A  48 83 C3 02                     add rbx, 2
0041AC3E  48 83 C1 02                     add rcx, 2
0041AC42  EB 21                           jmp 0x14041ac65
0041AC44  48 83 C3 03                     add rbx, 3
0041AC48  48 83 C1 03                     add rcx, 3
0041AC4C  EB 17                           jmp 0x14041ac65
0041AC4E  49 3B D8                        cmp rbx, r8
0041AC51  73 12                           jae 0x14041ac65
0041AC53  0F B6 01                        movzx eax, byte ptr [rcx]
0041AC56  38 03                           cmp byte ptr [rbx], al
0041AC58  75 0B                           jne 0x14041ac65
0041AC5A  48 FF C3                        inc rbx
0041AC5D  48 FF C1                        inc rcx
0041AC60  49 3B D8                        cmp rbx, r8
0041AC63  72 EE                           jb 0x14041ac53
0041AC65  48 8B C3                        mov rax, rbx
0041AC68  49 2B C3                        sub rax, r11
0041AC6B  48 3B C7                        cmp rax, rdi
0041AC6E  76 41                           jbe 0x14041acb1
0041AC70  4C 8B E3                        mov r12, rbx
0041AC73  48 8B F8                        mov rdi, rax
0041AC76  4C 2B E1                        sub r12, rcx
0041AC79  49 3B CB                        cmp rcx, r11
0041AC7C  76 36                           jbe 0x14041acb4
0041AC7E  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
0041AC86  49 8B DB                        mov rbx, r11
0041AC89  48 8D 4F FD                     lea rcx, [rdi - 3]
0041AC8D  48 03 DF                        add rbx, rdi
0041AC90  4E 8D 24 E5 F8 FF FF FF         lea r12, [r12*8 - 8]
0041AC98  48 8B C1                        mov rax, rcx
0041AC9B  48 83 F9 07                     cmp rcx, 7
0041AC9F  73 5A                           jae 0x14041acfb
0041ACA1  4C 03 E1                        add r12, rcx
0041ACA4  66 45 89 27                     mov word ptr [r15], r12w
0041ACA8  49 83 C7 02                     add r15, 2
0041ACAC  E9 E8 00 00 00                  jmp 0x14041ad99
0041ACB1  48 03 E8                        add rbp, rax
0041ACB4  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
0041ACBC  48 2B C8                        sub rcx, rax
0041ACBF  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0041ACC7  49 8B DB                        mov rbx, r11
0041ACCA  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
0041ACD2  48 FF C5                        inc rbp
0041ACD5  48 83 FD 18                     cmp rbp, 0x18
0041ACD9  73 AE                           jae 0x14041ac89
0041ACDB  48 2B C8                        sub rcx, rax
0041ACDE  81 E1 FF 3F 00 00               and ecx, 0x3fff
0041ACE4  48 8B 8C CA 00 00 04 00         mov rcx, qword ptr [rdx + rcx*8 + 0x40000]
0041ACEC  48 3B CE                        cmp rcx, rsi
0041ACEF  72 98                           jb 0x14041ac89
0041ACF1  44 3B 29                        cmp r13d, dword ptr [rcx]
0041ACF4  75 DC                           jne 0x14041acd2
0041ACF6  E9 5F FE FF FF                  jmp 0x14041ab5a
0041ACFB  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0041AD00  49 83 CC 07                     or r12, 7
0041AD04  66 45 89 27                     mov word ptr [r15], r12w
0041AD08  48 83 E8 07                     sub rax, 7
0041AD0C  49 83 C7 02                     add r15, 2
0041AD10  49 8B D7                        mov rdx, r15
0041AD13  4D 85 C0                        test r8, r8
0041AD16  75 1F                           jne 0x14041ad37
0041AD18  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0041AD1D  48 83 F8 0F                     cmp rax, 0xf
0041AD21  73 08                           jae 0x14041ad2b
0041AD23  41 88 07                        mov byte ptr [r15], al
0041AD26  49 FF C7                        inc r15
0041AD29  EB 6E                           jmp 0x14041ad99
0041AD2B  41 C6 07 0F                     mov byte ptr [r15], 0xf
0041AD2F  49 FF C7                        inc r15
0041AD32  45 33 C0                        xor r8d, r8d
0041AD35  EB 29                           jmp 0x14041ad60
0041AD37  41 0F B6 10                     movzx edx, byte ptr [r8]
0041AD3B  48 83 F8 0F                     cmp rax, 0xf
0041AD3F  73 11                           jae 0x14041ad52
0041AD41  C0 E0 04                        shl al, 4
0041AD44  0A C2                           or al, dl
0041AD46  41 88 00                        mov byte ptr [r8], al
0041AD49  33 C0                           xor eax, eax
0041AD4B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0041AD50  EB 47                           jmp 0x14041ad99
0041AD52  80 CA F0                        or dl, 0xf0
0041AD55  41 88 10                        mov byte ptr [r8], dl
0041AD58  45 33 C0                        xor r8d, r8d
0041AD5B  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0041AD60  48 83 E8 0F                     sub rax, 0xf
0041AD64  48 3D FF 00 00 00               cmp rax, 0xff
0041AD6A  73 08                           jae 0x14041ad74
0041AD6C  41 88 07                        mov byte ptr [r15], al
0041AD6F  49 FF C7                        inc r15
0041AD72  EB 25                           jmp 0x14041ad99
0041AD74  41 C6 07 FF                     mov byte ptr [r15], 0xff
0041AD78  48 81 F9 00 00 01 00            cmp rcx, 0x10000
0041AD7F  73 0B                           jae 0x14041ad8c
0041AD81  66 41 89 4F 01                  mov word ptr [r15 + 1], cx
0041AD86  49 83 C7 03                     add r15, 3
0041AD8A  EB 0D                           jmp 0x14041ad99
0041AD8C  66 45 89 47 01                  mov word ptr [r15 + 1], r8w
0041AD91  41 89 4F 03                     mov dword ptr [r15 + 3], ecx
0041AD95  49 83 C7 07                     add r15, 7
0041AD99  42 8D 04 4D 01 00 00 00         lea eax, [r9*2 + 1]
0041ADA1  45 85 C9                        test r9d, r9d
0041ADA4  7E 0C                           jle 0x14041adb2
0041ADA6  44 8B C8                        mov r9d, eax
0041ADA9  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0041ADB0  EB 1E                           jmp 0x14041add0
0041ADB2  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
0041ADB7  41 B9 01 00 00 00               mov r9d, 1
0041ADBD  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0041ADC2  49 83 C7 04                     add r15, 4
0041ADC6  44 89 8C 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r9d
0041ADCE  89 02                           mov dword ptr [rdx], eax
0041ADD0  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0041ADD5  4D 3B F8                        cmp r15, r8
0041ADD8  73 34                           jae 0x14041ae0e
0041ADDA  48 8B AC 24 C0 00 00 00         mov rbp, qword ptr [rsp + 0xc0]
0041ADE2  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0041ADEA  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
0041ADEF  E9 F8 FB FF FF                  jmp 0x14041a9ec
0041ADF4  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0041ADF9  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0041ADFE  8B BC 24 00 01 00 00            mov edi, dword ptr [rsp + 0x100]
0041AE05  48 3B DA                        cmp rbx, rdx
0041AE08  0F 82 3A FB FF FF               jb 0x14041a948
0041AE0E  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
0041AE13  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
0041AE18  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
0041AE20  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0041AE25  48 3B DF                        cmp rbx, rdi
0041AE28  73 3B                           jae 0x14041ae65
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0041A8A9(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, unsigned int a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, unsigned int a32)
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
    unsigned int v_stack_p100;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD8;

    v_stack_pD8 = v_r13;
    a2 = 0;
    result = memset(a29, a2, (unsigned int)(0x40000ULL), a4);
    v_stack_p60 = v_rdi - 5;
    v_stack_p38 = v_rsi - 41;
    v_stack_p28 = v_r15;
    if (a30 == 0) goto loc_0041A8F8;
    v_rdi = (unsigned int)(a32);
    if (((unsigned int)((unsigned int)(a32))) >= = ((unsigned int)(v_rbx))) {
        v_rdi = (unsigned int)(v_rbx);
        v_stack_p100 = (unsigned int)(v_rbx);
    }
    v_stack_p68 = a30;
    v_stack_p70 = a31;
    v_r10 = 0;
    *(unsigned __int8 *)(v_r14 + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rbp));
    v_stack_p78 = (unsigned int)(v_rdi);
    v_stack_pC8 = 2;
    v_stack_p20 = a26;
loc_0041A948:
    v_r11 = v_rdi - 5;
    if ((v_rbp + 8192) <= (v_rdi - 5)) { v_r11 = v_rbp + 8192; }
    result = ((unsigned int)((unsigned int)(v_rdi))) + (v_rbp + 1);
    v_stack_p40 = v_r11;
    if (v_r11 < result) { result = v_r11; }
    v_r10 = (unsigned int)((v_r10) & (0x3FFFULL));
    v_stack_p30 = result;
    v_stack_p48 = v_r10;
    if (v_rbp >= v_r11) goto loc_0041A9F1;
    a3 = (v_r10 * 8 + 262144) + (a29);
loc_0041A992:
    v_r10 = (v_r10) + 1;
    a2 = (*(unsigned __int16 *)(v_rip - 4223874 + *(unsigned __int8 *)(v_rbp + 1) * 2 + 512)) ^ (*(unsigned __int16 *)(v_rip - 4223874 + *(unsigned __int8 *)(v_rbp + 2) * 2 + 1024));
    a2 = (a2) ^ (*(unsigned __int16 *)(v_rip - 4223874 + *(unsigned __int8 *)(v_rbp) * 2));
    *(unsigned __int64 *)(a3 + 8 - 8) = *(unsigned __int64 *)(a29 + a2 * 8);
    *(unsigned __int64 *)(a29 + a2 * 8) = v_rbp;
    v_r14 = (v_rbp) + 1;
    if (v_r14 < v_r11) goto loc_0041A992;
    v_stack_p48 = v_r10;
loc_0041A9EC:
loc_0041A9F1:
    v_rdi = ((unsigned int)(0x2000ULL)) - (v_rbp);
loc_0041AA00:
    if ((v_rbp + 1) < a6) goto loc_0041AA35;
    if ((v_rbp + 1) >= v_r11) goto loc_0041ADF4;
    result = RtlpMakeXpressCallback(a13, v_r11, v_rbp + 1, (unsigned int)(a25));
    v_stack_p30 = result;
loc_0041AA35:
    a1 = (unsigned int)((v_rdi + v_rbp + 1 - 8192 * 1) & (0x3FFFULL));
    if ((*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) < (v_rbp + 1 - 8192)) goto loc_0041AAC2;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 1))))) ^ (*(unsigned int *)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144))));
    if (condition_is_equal) goto loc_0041AB53;
    if (((a2) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
    a1 = (*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) - (v_rbp);
    a1 = (unsigned int)((a1) & (0x3FFFULL));
    if ((*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) < (v_rbp + 1 - 8192)) goto loc_0041AAC2;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 1))))) ^ (*(unsigned int *)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144))));
    if (condition_is_equal) goto loc_0041AB53;
    if ((((unsigned int)(result)) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
    a1 = (*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) - (v_rbp);
    a1 = (unsigned int)((a1) & (0x3FFFULL));
    if ((*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) < (v_rbp + 1 - 8192)) goto loc_0041AAC2;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 1))))) ^ (*(unsigned int *)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144))));
    if (condition_is_equal) goto loc_0041AB53;
    if ((((unsigned int)(result)) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
loc_0041AAC2:
    *(unsigned __int8 *)(v_r14 + 5) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 1)));
    v_r15 = (v_r14 + 5) + 1;
    v_rbx = (v_rbp + 1) + 1;
    v_rsi = (v_rbp + 1 - 8192) + 1;
    if (condition_is_less_or_equal) goto loc_0041AAF6;
    v_stack_pC8 = (unsigned int)((unsigned int)(a25) + (unsigned int)(a25) * 1);
    goto loc_0041AA00;
loc_0041AAF6:
    v_r15 = (v_r15) + (4);
    v_stack_pC8 = 1;
    *(unsigned int *)(v_stack_p20) = (unsigned int)(a6);
    if (v_r15 >= a7) goto loc_0041AE13;
    v_stack_p20 = v_r15;
    goto loc_0041AA00;
loc_0041AB32:
    v_r12 = (v_rbx) - (v_r15);
    result = 0;
    goto loc_0041ACDB;
loc_0041AB53:
    result = 0;
loc_0041AB5A:
    v_rbx = (v_rbx) + (4);
    a1 = (v_r15) + (4);
loc_0041AB65:
    if ((v_rbx + 32) >= a10) goto loc_0041AC4E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) goto loc_0041AC1C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_0041AC14;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) goto loc_0041AC0A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 12)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) goto loc_0041AC00;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_0041ABF6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 20)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))))) goto loc_0041ABEC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) goto loc_0041ABE2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 28)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28))))) goto loc_0041ABDC;
    a1 = (a1) + (32);
    goto loc_0041AB65;
loc_0041ABDC:
    a1 = (a1) + (28);
    goto loc_0041AC1C;
loc_0041ABE2:
    v_rbx = (v_rbx + 32) + (24);
    a1 = (a1) + (24);
    goto loc_0041AC1C;
loc_0041ABEC:
    v_rbx = (v_rbx) + (20);
    a1 = (a1) + (20);
    goto loc_0041AC1C;
loc_0041ABF6:
    v_rbx = (v_rbx) + (16);
    a1 = (a1) + (16);
    goto loc_0041AC1C;
loc_0041AC00:
    v_rbx = (v_rbx) + (12);
    a1 = (a1) + (12);
    goto loc_0041AC1C;
loc_0041AC0A:
    v_rbx = (v_rbx) + (8);
    a1 = (a1) + (8);
    goto loc_0041AC1C;
loc_0041AC14:
    v_rbx = (v_rbx) + (4);
    a1 = (a1) + (4);
loc_0041AC1C:
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 28)))) != ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28))))) goto loc_0041AC65;
    if ((*(unsigned __int8 *)(v_rbx + 1)) == ((unsigned __int8)(*(unsigned __int8 *)(a1 + 1)))) goto loc_0041AC31;
    v_rbx = (v_rbx) + 1;
    a1 = (a1) + 1;
    goto loc_0041AC65;
loc_0041AC31:
    if ((*(unsigned __int8 *)(v_rbx + 2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1 + 2)))) goto loc_0041AC44;
    v_rbx = (v_rbx) + (2);
    a1 = (a1) + (2);
    goto loc_0041AC65;
loc_0041AC44:
    v_rbx = (v_rbx) + (3);
    a1 = (a1) + (3);
    goto loc_0041AC65;
loc_0041AC4E:
    if (v_rbx >= a10) goto loc_0041AC65;
loc_0041AC53:
    if ((*(unsigned __int8 *)(v_rbx)) != ((unsigned __int8)(*(unsigned __int8 *)(a1)))) goto loc_0041AC65;
    v_rbx = (v_rbx) + 1;
    a1 = (a1) + 1;
    if (v_rbx < a10) goto loc_0041AC53;
loc_0041AC65:
    result = (v_rbx) - (v_rbx);
    if (result <= (result + 3)) goto loc_0041ACB1;
    v_r12 = (v_rbx) - (a1);
    if (a1 <= v_rbx) goto loc_0041ACB4;
loc_0041AC89:
    v_rbx = (v_rbx) + (result);
    if ((result - 3) >= 7) goto loc_0041ACFB;
    v_r12 = (v_r12 * 8 - 8) + (result - 3);
    *(unsigned __int16 *)(v_r15) = (unsigned __int16)(v_r12);
    v_r15 = (v_r15) + (2);
    goto loc_0041AD99;
loc_0041ACB1:
    v_rbp = (0) + (result - 3);
loc_0041ACB4:
    a1 = (result - 3) - (result - 3);
loc_0041ACD2:
    v_rbp = (v_rbp) + 1;
    if (v_rbp >= 24) goto loc_0041AC89;
loc_0041ACDB:
    a1 = (a1) - (a24);
    a1 = (unsigned int)((a1) & (0x3FFFULL));
    if ((*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) < (v_rbx - 8192)) goto loc_0041AC89;
    if (((unsigned int)(a29)) != (*(unsigned int *)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144)))) goto loc_0041ACD2;
    goto loc_0041AB5A;
loc_0041ACFB:
    v_r12 = (v_r12) | (7);
    *(unsigned __int16 *)(v_r15) = (unsigned __int16)(v_r12);
    result = (a24) - (7);
    v_r15 = (v_r15) + (2);
    if (a5 != 0) goto loc_0041AD37;
    v_stack_p28 = v_r15;
    if (result >= 15) goto loc_0041AD2B;
    *(unsigned __int8 *)(v_r15) = (unsigned __int8)(result);
    v_r15 = (v_r15) + 1;
    goto loc_0041AD99;
loc_0041AD2B:
    *(unsigned __int8 *)(v_r15) = 15;
    v_r15 = (v_r15) + 1;
    a3 = 0;
    goto loc_0041AD60;
loc_0041AD37:
    if (result >= 15) goto loc_0041AD52;
    result = (unsigned __int8)((result) << (4));
    result = (unsigned __int8)((result) | ((unsigned __int8)(*(unsigned __int8 *)(a3))));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    result = 0;
    v_stack_p28 = 0;
    goto loc_0041AD99;
loc_0041AD52:
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a3)) | (240));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = 0;
    v_stack_p28 = 0;
loc_0041AD60:
    result = (result) - (15);
    if (result >= 255) goto loc_0041AD74;
    *(unsigned __int8 *)(v_r15) = (unsigned __int8)(result);
    v_r15 = (v_r15) + 1;
    goto loc_0041AD99;
loc_0041AD74:
    *(unsigned __int8 *)(v_r15) = 255;
    if ((*(unsigned __int64 *)(a29 + a1 * 8 + 262144)) >= 0x10000ULL) goto loc_0041AD8C;
    *(unsigned __int16 *)(v_r15 + 1) = (unsigned __int16)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144));
    v_r15 = (v_r15) + (3);
    goto loc_0041AD99;
loc_0041AD8C:
    *(unsigned __int16 *)(v_r15 + 1) = 0;
    *(unsigned int *)(v_r15 + 3) = (unsigned int)(*(unsigned __int64 *)(a29 + a1 * 8 + 262144));
    v_r15 = (v_r15) + (7);
loc_0041AD99:
    if (condition_is_less_or_equal) goto loc_0041ADB2;
    v_stack_pC8 = (unsigned int)((unsigned int)(a25) * 2 + 1);
    goto loc_0041ADD0;
loc_0041ADB2:
    v_stack_p20 = v_r15;
    v_r15 = (v_r15) + (4);
    v_stack_pC8 = 1;
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(a25) * 2 + 1);
loc_0041ADD0:
    if (v_r15 >= a7) goto loc_0041AE0E;
    goto loc_0041A9EC;
loc_0041ADF4:
    if (v_rbx < a12) goto loc_0041A948;
loc_0041AE0E:
loc_0041AE13:
}
```

## 5. (Beta) C Style

```c
int64_t sub_0041A8A9(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, int64_t Arg24, uint32_t Arg25, int64_t Arg26, int64_t Arg27, uint64_t Arg28, void *Arg29, int64_t Arg30, int64_t Arg31, uint32_t Arg32)
{
    uint8_t *arg29 = (uint8_t *)Arg29;

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
    uint32_t v_stack_p100;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD8;

    v_stack_pD8 = local_r13;
    Arg2 = 0;
    result = memset(Arg29, Arg2, (uint32_t)(0x40000ULL), Arg4);
    v_stack_p60 = local_rdi - 5;
    v_stack_p38 = local_rsi - 41;
    v_stack_p28 = local_r15;
    if (Arg30 == 0) goto loc_0041A8F8;
    local_rdi = (uint32_t)(Arg32);
    if (((uint32_t)((uint32_t)(Arg32))) >= = ((uint32_t)(local_rbx))) {
        local_rdi = (uint32_t)(local_rbx);
        v_stack_p100 = (uint32_t)(local_rbx);
    }
    v_stack_p68 = Arg30;
    v_stack_p70 = Arg31;
    local_r10 = 0;
    *(uint8_t *)(local_r14 + 0x4) = (uint8_t)(*(uint8_t *)(local_rbp));
    v_stack_p78 = (uint32_t)(local_rdi);
    v_stack_pC8 = 2;
    v_stack_p20 = Arg26;
loc_0041A948:
    local_r11 = local_rdi - 5;
    if ((local_rbp + 8192) <= (local_rdi - 5)) { local_r11 = local_rbp + 8192; }
    result = ((uint32_t)((uint32_t)(local_rdi))) + (local_rbp + 1);
    v_stack_p40 = local_r11;
    if (local_r11 < result) { result = local_r11; }
    local_r10 = (uint32_t)((local_r10) & (0x3FFFULL));
    v_stack_p30 = result;
    v_stack_p48 = local_r10;
    if (local_rbp >= local_r11) goto loc_0041A9F1;
    Arg3 = (local_r10 * 8 + 262144) + (Arg29);
loc_0041A992:
    local_r10 = (local_r10) + 1;
    Arg2 = (*(uint16_t *)(v_rip - 0x407382 + *(uint8_t *)(local_rbp + 0x1) * 2 + 0x200)) ^ (*(uint16_t *)(v_rip - 0x407382 + *(uint8_t *)(local_rbp + 0x2) * 2 + 0x400));
    Arg2 = (Arg2) ^ (*(uint16_t *)(v_rip - 0x407382 + *(uint8_t *)(local_rbp) * 2));
    *(uint64_t *)(Arg3 + 0x8 - 0x8) = *(uint64_t *)(arg29 + Arg2 * 8);
    *(uint64_t *)(arg29 + Arg2 * 8) = local_rbp;
    local_r14 = (local_rbp) + 1;
    if (local_r14 < local_r11) goto loc_0041A992;
    v_stack_p48 = local_r10;
loc_0041A9EC:
loc_0041A9F1:
    local_rdi = ((uint32_t)(0x2000ULL)) - (local_rbp);
loc_0041AA00:
    if ((local_rbp + 1) < Arg6) goto loc_0041AA35;
    if ((local_rbp + 1) >= local_r11) goto loc_0041ADF4;
    result = RtlpMakeXpressCallback(Arg13, local_r11, local_rbp + 1, (uint32_t)(Arg25));
    v_stack_p30 = result;
loc_0041AA35:
    Arg1 = (uint32_t)((local_rdi + local_rbp + 1 - 8192 * 1) & (0x3FFFULL));
    if ((*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) < (local_rbp + 1 - 8192)) goto loc_0041AAC2;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1))))) ^ (*(uint32_t *)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000))));
    if (condition_is_equal) goto loc_0041AB53;
    if (((Arg2) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
    Arg1 = (*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) - (local_rbp);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFULL));
    if ((*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) < (local_rbp + 1 - 8192)) goto loc_0041AAC2;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1))))) ^ (*(uint32_t *)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000))));
    if (condition_is_equal) goto loc_0041AB53;
    if ((((uint32_t)(result)) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
    Arg1 = (*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) - (local_rbp);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFULL));
    if ((*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) < (local_rbp + 1 - 8192)) goto loc_0041AAC2;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1))))) ^ (*(uint32_t *)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000))));
    if (condition_is_equal) goto loc_0041AB53;
    if ((((uint32_t)(result)) & (0xFFFFFFULL)) == 0) goto loc_0041AB32;
loc_0041AAC2:
    *(uint8_t *)(local_r14 + 0x5) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x1)));
    local_r15 = (local_r14 + 5) + 1;
    local_rbx = (local_rbp + 1) + 1;
    local_rsi = (local_rbp + 1 - 8192) + 1;
    if (condition_is_less_or_equal) goto loc_0041AAF6;
    v_stack_pC8 = (uint32_t)((uint32_t)(Arg25) + (uint32_t)(Arg25) * 1);
    goto loc_0041AA00;
loc_0041AAF6:
    local_r15 = (local_r15) + (4);
    v_stack_pC8 = 1;
    *(uint32_t *)(v_stack_p20) = (uint32_t)(Arg6);
    if (local_r15 >= Arg7) goto loc_0041AE13;
    v_stack_p20 = local_r15;
    goto loc_0041AA00;
loc_0041AB32:
    local_r12 = (local_rbx) - (local_r15);
    result = 0;
    goto loc_0041ACDB;
loc_0041AB53:
    result = 0;
loc_0041AB5A:
    local_rbx = (local_rbx) + (4);
    Arg1 = (local_r15) + (4);
loc_0041AB65:
    if ((local_rbx + 32) >= Arg10) goto loc_0041AC4E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) goto loc_0041AC1C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4))))) goto loc_0041AC14;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8))))) goto loc_0041AC0A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC))))) goto loc_0041AC00;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10))))) goto loc_0041ABF6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x14)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14))))) goto loc_0041ABEC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x18))))) goto loc_0041ABE2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x1C)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x1C))))) goto loc_0041ABDC;
    Arg1 = (Arg1) + (32);
    goto loc_0041AB65;
loc_0041ABDC:
    Arg1 = (Arg1) + (28);
    goto loc_0041AC1C;
loc_0041ABE2:
    local_rbx = (local_rbx + 32) + (24);
    Arg1 = (Arg1) + (24);
    goto loc_0041AC1C;
loc_0041ABEC:
    local_rbx = (local_rbx) + (20);
    Arg1 = (Arg1) + (20);
    goto loc_0041AC1C;
loc_0041ABF6:
    local_rbx = (local_rbx) + (16);
    Arg1 = (Arg1) + (16);
    goto loc_0041AC1C;
loc_0041AC00:
    local_rbx = (local_rbx) + (12);
    Arg1 = (Arg1) + (12);
    goto loc_0041AC1C;
loc_0041AC0A:
    local_rbx = (local_rbx) + (8);
    Arg1 = (Arg1) + (8);
    goto loc_0041AC1C;
loc_0041AC14:
    local_rbx = (local_rbx) + (4);
    Arg1 = (Arg1) + (4);
loc_0041AC1C:
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x1C)))) != ((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x1C))))) goto loc_0041AC65;
    if ((*(uint8_t *)(local_rbx + 0x1)) == ((uint8_t)(*(uint8_t *)(Arg1 + 0x1)))) goto loc_0041AC31;
    local_rbx = (local_rbx) + 1;
    Arg1 = (Arg1) + 1;
    goto loc_0041AC65;
loc_0041AC31:
    if ((*(uint8_t *)(local_rbx + 0x2)) == ((uint8_t)(*(uint8_t *)(Arg1 + 0x2)))) goto loc_0041AC44;
    local_rbx = (local_rbx) + (2);
    Arg1 = (Arg1) + (2);
    goto loc_0041AC65;
loc_0041AC44:
    local_rbx = (local_rbx) + (3);
    Arg1 = (Arg1) + (3);
    goto loc_0041AC65;
loc_0041AC4E:
    if (local_rbx >= Arg10) goto loc_0041AC65;
loc_0041AC53:
    if ((*(uint8_t *)(local_rbx)) != ((uint8_t)(*(uint8_t *)(Arg1)))) goto loc_0041AC65;
    local_rbx = (local_rbx) + 1;
    Arg1 = (Arg1) + 1;
    if (local_rbx < Arg10) goto loc_0041AC53;
loc_0041AC65:
    result = (local_rbx) - (local_rbx);
    if (result <= (result + 3)) goto loc_0041ACB1;
    local_r12 = (local_rbx) - (Arg1);
    if (Arg1 <= local_rbx) goto loc_0041ACB4;
loc_0041AC89:
    local_rbx = (local_rbx) + (result);
    if ((result - 3) >= 7) goto loc_0041ACFB;
    local_r12 = (local_r12 * 8 - 8) + (result - 3);
    *(uint16_t *)(local_r15) = (uint16_t)(local_r12);
    local_r15 = (local_r15) + (2);
    goto loc_0041AD99;
loc_0041ACB1:
    local_rbp = (0) + (result - 3);
loc_0041ACB4:
    Arg1 = (result - 3) - (result - 3);
loc_0041ACD2:
    local_rbp = (local_rbp) + 1;
    if (local_rbp >= 24) goto loc_0041AC89;
loc_0041ACDB:
    Arg1 = (Arg1) - (Arg24);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFULL));
    if ((*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) < (local_rbx - 8192)) goto loc_0041AC89;
    if (((uint32_t)(Arg29)) != (*(uint32_t *)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)))) goto loc_0041ACD2;
    goto loc_0041AB5A;
loc_0041ACFB:
    local_r12 = (local_r12) | (7);
    *(uint16_t *)(local_r15) = (uint16_t)(local_r12);
    result = (Arg24) - (7);
    local_r15 = (local_r15) + (2);
    if (Arg5 != 0) goto loc_0041AD37;
    v_stack_p28 = local_r15;
    if (result >= 15) goto loc_0041AD2B;
    *(uint8_t *)(local_r15) = (uint8_t)(result);
    local_r15 = (local_r15) + 1;
    goto loc_0041AD99;
loc_0041AD2B:
    *(uint8_t *)(local_r15) = 15;
    local_r15 = (local_r15) + 1;
    Arg3 = 0;
    goto loc_0041AD60;
loc_0041AD37:
    if (result >= 15) goto loc_0041AD52;
    result = (uint8_t)((result) << (4));
    result = (uint8_t)((result) | ((uint8_t)(*(uint8_t *)(Arg3))));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
    result = 0;
    v_stack_p28 = 0;
    goto loc_0041AD99;
loc_0041AD52:
    Arg2 = (uint8_t)((*(uint8_t *)(Arg3)) | (240));
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = 0;
    v_stack_p28 = 0;
loc_0041AD60:
    result = (result) - (15);
    if (result >= 255) goto loc_0041AD74;
    *(uint8_t *)(local_r15) = (uint8_t)(result);
    local_r15 = (local_r15) + 1;
    goto loc_0041AD99;
loc_0041AD74:
    *(uint8_t *)(local_r15) = 255;
    if ((*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000)) >= 0x10000ULL) goto loc_0041AD8C;
    *(uint16_t *)(local_r15 + 0x1) = (uint16_t)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000));
    local_r15 = (local_r15) + (3);
    goto loc_0041AD99;
loc_0041AD8C:
    *(uint16_t *)(local_r15 + 0x1) = 0;
    *(uint32_t *)(local_r15 + 0x3) = (uint32_t)(*(uint64_t *)(arg29 + Arg1 * 8 + 0x40000));
    local_r15 = (local_r15) + (7);
loc_0041AD99:
    if (condition_is_less_or_equal) goto loc_0041ADB2;
    v_stack_pC8 = (uint32_t)((uint32_t)(Arg25) * 2 + 1);
    goto loc_0041ADD0;
loc_0041ADB2:
    v_stack_p20 = local_r15;
    local_r15 = (local_r15) + (4);
    v_stack_pC8 = 1;
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(Arg25) * 2 + 1);
loc_0041ADD0:
    if (local_r15 >= Arg7) goto loc_0041AE0E;
    goto loc_0041A9EC;
loc_0041ADF4:
    if (local_rbx < Arg12) goto loc_0041A948;
loc_0041AE0E:
loc_0041AE13:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg29` | `+ 0x0 + rdx*8` | `64` | `R` |
| `Arg29` | `+ 0x0 + rdx*8` | `64` | `W` |
| `Arg29` | `+ 0x40000 + rcx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041A8A9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
