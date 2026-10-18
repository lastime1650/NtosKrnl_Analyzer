# sub_0092CDFD

- RVA: `0x0092CDFD`–`0x0092D445` (길이 `1,608` bytes)
- VA: `0x000000014092CDFD`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DB8C`
- 디코드: `472`개 명령, `1,608/1,608` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0092D149` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092D16F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092D19C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092D208` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D252` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D2A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D2F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D34C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D398` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D3E3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092D414` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0092CE02` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x0092D149` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092D16F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092D19C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092D208` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D252` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D2A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D2F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D34C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D398` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D3E3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092D414` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092CDFD  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0092CE02  48 8D 0D F7 31 6D FF            lea rcx, [rip - 0x92ce09]
0092CE09  4D 85 F6                        test r14, r14
0092CE0C  0F 84 96 00 00 00               je 0x14092cea8
0092CE12  45 0F B7 5E 04                  movzx r11d, word ptr [r14 + 4]
0092CE17  4D 8D 56 08                     lea r10, [r14 + 8]
0092CE1B  41 8B DC                        mov ebx, r12d
0092CE1E  66 45 3B E3                     cmp r12w, r11w
0092CE22  0F 83 80 00 00 00               jae 0x14092cea8
0092CE28  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0092CE30  41 0F B6 02                     movzx eax, byte ptr [r10]
0092CE34  45 0F B7 CB                     movzx r9d, r11w
0092CE38  83 C0 FE                        add eax, -2
0092CE3B  83 F8 0E                        cmp eax, 0xe
0092CE3E  77 52                           ja 0x14092ce92
0092CE40  48 98                           cdqe
0092CE42  8B 8C 81 48 D4 92 00            mov ecx, dword ptr [rcx + rax*4 + 0x92d448]
0092CE49  48 8D 05 B0 31 6D FF            lea rax, [rip - 0x92ce50]
0092CE50  48 03 C8                        add rcx, rax
0092CE53  FF E1                           jmp rcx
0092CE55  CC                              int3
0092CE56  CC                              int3
0092CE57  CC                              int3
0092CE58  CC                              int3
0092CE59  41 0F B7 4A 02                  movzx ecx, word ptr [r10 + 2]
0092CE5E  03 CA                           add ecx, edx
0092CE60  3B CA                           cmp ecx, edx
0092CE62  0F 82 B6 05 00 00               jb 0x14092d41e
0092CE68  8B D1                           mov edx, ecx
0092CE6A  4D 85 C0                        test r8, r8
0092CE6D  74 09                           je 0x14092ce78
0092CE6F  41 83 08 08                     or dword ptr [r8], 8
0092CE73  45 0F B7 4E 04                  movzx r9d, word ptr [r14 + 4]
0092CE78  41 0F B6 06                     movzx eax, byte ptr [r14]
0092CE7C  48 8D 0D 7D 31 6D FF            lea rcx, [rip - 0x92ce83]
0092CE83  3B C7                           cmp eax, edi
0092CE85  76 0B                           jbe 0x14092ce92
0092CE87  8B F8                           mov edi, eax
0092CE89  EB 07                           jmp 0x14092ce92
0092CE8B  48 8D 0D 6E 31 6D FF            lea rcx, [rip - 0x92ce92]
0092CE92  41 0F B7 42 02                  movzx eax, word ptr [r10 + 2]
0092CE97  FF C3                           inc ebx
0092CE99  4C 03 D0                        add r10, rax
0092CE9C  45 0F B7 D9                     movzx r11d, r9w
0092CEA0  41 0F B7 C1                     movzx eax, r9w
0092CEA4  3B D8                           cmp ebx, eax
0092CEA6  72 88                           jb 0x14092ce30
0092CEA8  4D 85 ED                        test r13, r13
0092CEAB  74 62                           je 0x14092cf0f
0092CEAD  45 0F B7 55 04                  movzx r10d, word ptr [r13 + 4]
0092CEB2  4D 8D 4D 08                     lea r9, [r13 + 8]
0092CEB6  45 8B DC                        mov r11d, r12d
0092CEB9  66 45 3B E2                     cmp r12w, r10w
0092CEBD  73 50                           jae 0x14092cf0f
0092CEBF  90                              nop
0092CEC0  41 80 39 11                     cmp byte ptr [r9], 0x11
0092CEC4  41 0F B7 CA                     movzx ecx, r10w
0092CEC8  75 2E                           jne 0x14092cef8
0092CECA  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
0092CECF  03 CA                           add ecx, edx
0092CED1  3B CA                           cmp ecx, edx
0092CED3  0F 82 45 05 00 00               jb 0x14092d41e
0092CED9  8B D1                           mov edx, ecx
0092CEDB  41 0F B7 CA                     movzx ecx, r10w
0092CEDF  4D 85 C0                        test r8, r8
0092CEE2  74 09                           je 0x14092ceed
0092CEE4  41 83 08 10                     or dword ptr [r8], 0x10
0092CEE8  41 0F B7 4D 04                  movzx ecx, word ptr [r13 + 4]
0092CEED  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0092CEF2  3B C7                           cmp eax, edi
0092CEF4  76 02                           jbe 0x14092cef8
0092CEF6  8B F8                           mov edi, eax
0092CEF8  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
0092CEFD  41 FF C3                        inc r11d
0092CF00  4C 03 C8                        add r9, rax
0092CF03  44 0F B7 D1                     movzx r10d, cx
0092CF07  0F B7 C1                        movzx eax, cx
0092CF0A  44 3B D8                        cmp r11d, eax
0092CF0D  72 B1                           jb 0x14092cec0
0092CF0F  48 85 F6                        test rsi, rsi
0092CF12  74 61                           je 0x14092cf75
0092CF14  44 0F B7 56 04                  movzx r10d, word ptr [rsi + 4]
0092CF19  4C 8D 4E 08                     lea r9, [rsi + 8]
0092CF1D  45 8B DC                        mov r11d, r12d
0092CF20  66 45 3B E2                     cmp r12w, r10w
0092CF24  73 4F                           jae 0x14092cf75
0092CF26  41 80 39 14                     cmp byte ptr [r9], 0x14
0092CF2A  41 0F B7 CA                     movzx ecx, r10w
0092CF2E  75 2E                           jne 0x14092cf5e
0092CF30  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
0092CF35  03 CA                           add ecx, edx
0092CF37  3B CA                           cmp ecx, edx
0092CF39  0F 82 DF 04 00 00               jb 0x14092d41e
0092CF3F  8B D1                           mov edx, ecx
0092CF41  41 0F B7 CA                     movzx ecx, r10w
0092CF45  4D 85 C0                        test r8, r8
0092CF48  74 0B                           je 0x14092cf55
0092CF4A  41 81 08 80 00 00 00            or dword ptr [r8], 0x80
0092CF51  0F B7 4E 04                     movzx ecx, word ptr [rsi + 4]
0092CF55  0F B6 06                        movzx eax, byte ptr [rsi]
0092CF58  3B C7                           cmp eax, edi
0092CF5A  76 02                           jbe 0x14092cf5e
0092CF5C  8B F8                           mov edi, eax
0092CF5E  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
0092CF63  41 FF C3                        inc r11d
0092CF66  4C 03 C8                        add r9, rax
0092CF69  44 0F B7 D1                     movzx r10d, cx
0092CF6D  0F B7 C1                        movzx eax, cx
0092CF70  44 3B D8                        cmp r11d, eax
0092CF73  72 B1                           jb 0x14092cf26
0092CF75  48 85 ED                        test rbp, rbp
0092CF78  74 66                           je 0x14092cfe0
0092CF7A  44 0F B7 55 04                  movzx r10d, word ptr [rbp + 4]
0092CF7F  4C 8D 4D 08                     lea r9, [rbp + 8]
0092CF83  45 8B DC                        mov r11d, r12d
0092CF86  66 45 3B E2                     cmp r12w, r10w
0092CF8A  73 54                           jae 0x14092cfe0
0092CF8C  0F 1F 40 00                     nop dword ptr [rax]
0092CF90  41 80 39 15                     cmp byte ptr [r9], 0x15
0092CF94  41 0F B7 CA                     movzx ecx, r10w
0092CF98  75 2F                           jne 0x14092cfc9
0092CF9A  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
0092CF9F  03 CA                           add ecx, edx
0092CFA1  3B CA                           cmp ecx, edx
0092CFA3  0F 82 75 04 00 00               jb 0x14092d41e
0092CFA9  8B D1                           mov edx, ecx
0092CFAB  41 0F B7 CA                     movzx ecx, r10w
0092CFAF  4D 85 C0                        test r8, r8
0092CFB2  74 0B                           je 0x14092cfbf
0092CFB4  41 81 08 00 01 00 00            or dword ptr [r8], 0x100
0092CFBB  0F B7 4D 04                     movzx ecx, word ptr [rbp + 4]
0092CFBF  0F B6 45 00                     movzx eax, byte ptr [rbp]
0092CFC3  3B C7                           cmp eax, edi
0092CFC5  76 02                           jbe 0x14092cfc9
0092CFC7  8B F8                           mov edi, eax
0092CFC9  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
0092CFCE  41 FF C3                        inc r11d
0092CFD1  4C 03 C8                        add r9, rax
0092CFD4  44 0F B7 D1                     movzx r10d, cx
0092CFD8  0F B7 C1                        movzx eax, cx
0092CFDB  44 3B D8                        cmp r11d, eax
0092CFDE  72 B0                           jb 0x14092cf90
0092CFE0  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
0092CFE8  48 85 F6                        test rsi, rsi
0092CFEB  74 6A                           je 0x14092d057
0092CFED  44 0F B7 5E 04                  movzx r11d, word ptr [rsi + 4]
0092CFF2  4C 8D 56 08                     lea r10, [rsi + 8]
0092CFF6  41 8B DC                        mov ebx, r12d
0092CFF9  66 45 3B E3                     cmp r12w, r11w
0092CFFD  73 58                           jae 0x14092d057
0092CFFF  90                              nop
0092D000  45 0F B6 0A                     movzx r9d, byte ptr [r10]
0092D004  41 0F B7 CB                     movzx ecx, r11w
0092D008  41 83 E9 16                     sub r9d, 0x16
0092D00C  74 06                           je 0x14092d014
0092D00E  41 83 F9 01                     cmp r9d, 1
0092D012  75 2E                           jne 0x14092d042
0092D014  41 0F B7 4A 02                  movzx ecx, word ptr [r10 + 2]
0092D019  03 CA                           add ecx, edx
0092D01B  3B CA                           cmp ecx, edx
0092D01D  0F 82 FB 03 00 00               jb 0x14092d41e
0092D023  8B D1                           mov edx, ecx
0092D025  41 0F B7 CB                     movzx ecx, r11w
0092D029  4D 85 C0                        test r8, r8
0092D02C  74 0B                           je 0x14092d039
0092D02E  41 81 08 00 02 00 00            or dword ptr [r8], 0x200
0092D035  0F B7 4E 04                     movzx ecx, word ptr [rsi + 4]
0092D039  0F B6 06                        movzx eax, byte ptr [rsi]
0092D03C  3B C7                           cmp eax, edi
0092D03E  76 02                           jbe 0x14092d042
0092D040  8B F8                           mov edi, eax
0092D042  41 0F B7 42 02                  movzx eax, word ptr [r10 + 2]
0092D047  FF C3                           inc ebx
0092D049  4C 03 D0                        add r10, rax
0092D04C  44 0F B7 D9                     movzx r11d, cx
0092D050  0F B7 C1                        movzx eax, cx
0092D053  3B D8                           cmp ebx, eax
0092D055  72 A9                           jb 0x14092d000
0092D057  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0092D05C  48 85 DB                        test rbx, rbx
0092D05F  74 5E                           je 0x14092d0bf
0092D061  44 0F B7 53 04                  movzx r10d, word ptr [rbx + 4]
0092D066  4C 8D 4B 08                     lea r9, [rbx + 8]
0092D06A  45 8B DC                        mov r11d, r12d
0092D06D  66 45 3B E2                     cmp r12w, r10w
0092D071  73 4C                           jae 0x14092d0bf
0092D073  41 80 39 12                     cmp byte ptr [r9], 0x12
0092D077  41 0F B7 CA                     movzx ecx, r10w
0092D07B  75 2B                           jne 0x14092d0a8
0092D07D  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
0092D082  03 CA                           add ecx, edx
0092D084  3B CA                           cmp ecx, edx
0092D086  0F 82 92 03 00 00               jb 0x14092d41e
0092D08C  8B D1                           mov edx, ecx
0092D08E  41 0F B7 CA                     movzx ecx, r10w
0092D092  4D 85 C0                        test r8, r8
0092D095  74 08                           je 0x14092d09f
0092D097  41 83 08 20                     or dword ptr [r8], 0x20
0092D09B  0F B7 4B 04                     movzx ecx, word ptr [rbx + 4]
0092D09F  0F B6 03                        movzx eax, byte ptr [rbx]
0092D0A2  3B C7                           cmp eax, edi
0092D0A4  76 02                           jbe 0x14092d0a8
0092D0A6  8B F8                           mov edi, eax
0092D0A8  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
0092D0AD  41 FF C3                        inc r11d
0092D0B0  4C 03 C8                        add r9, rax
0092D0B3  44 0F B7 D1                     movzx r10d, cx
0092D0B7  0F B7 C1                        movzx eax, cx
0092D0BA  44 3B D8                        cmp r11d, eax
0092D0BD  72 B4                           jb 0x14092d073
0092D0BF  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0092D0C4  48 85 DB                        test rbx, rbx
0092D0C7  74 63                           je 0x14092d12c
0092D0C9  44 0F B7 53 04                  movzx r10d, word ptr [rbx + 4]
0092D0CE  4C 8D 4B 08                     lea r9, [rbx + 8]
0092D0D2  45 8B DC                        mov r11d, r12d
0092D0D5  66 45 3B E2                     cmp r12w, r10w
0092D0D9  73 51                           jae 0x14092d12c
0092D0DB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0092D0E0  41 80 39 13                     cmp byte ptr [r9], 0x13
0092D0E4  41 0F B7 CA                     movzx ecx, r10w
0092D0E8  75 2B                           jne 0x14092d115
0092D0EA  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
0092D0EF  03 CA                           add ecx, edx
0092D0F1  3B CA                           cmp ecx, edx
0092D0F3  0F 82 25 03 00 00               jb 0x14092d41e
0092D0F9  8B D1                           mov edx, ecx
0092D0FB  41 0F B7 CA                     movzx ecx, r10w
0092D0FF  4D 85 C0                        test r8, r8
0092D102  74 08                           je 0x14092d10c
0092D104  41 83 08 40                     or dword ptr [r8], 0x40
0092D108  0F B7 4B 04                     movzx ecx, word ptr [rbx + 4]
0092D10C  0F B6 03                        movzx eax, byte ptr [rbx]
0092D10F  3B C7                           cmp eax, edi
0092D111  76 02                           jbe 0x14092d115
0092D113  8B F8                           mov edi, eax
0092D115  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
0092D11A  41 FF C3                        inc r11d
0092D11D  4C 03 C8                        add r9, rax
0092D120  44 0F B7 D1                     movzx r10d, cx
0092D124  0F B7 C1                        movzx eax, cx
0092D127  44 3B D8                        cmp r11d, eax
0092D12A  72 B4                           jb 0x14092d0e0
0092D12C  8D 5A 03                        lea ebx, [rdx + 3]
0092D12F  3B DA                           cmp ebx, edx
0092D131  0F 82 E7 02 00 00               jb 0x14092d41e
0092D137  83 E3 FC                        and ebx, 0xfffffffc
0092D13A  41 B8 53 65 53 64               mov r8d, 0x64536553
0092D140  8B D3                           mov edx, ebx
0092D142  B9 00 01 00 00                  mov ecx, 0x100
0092D147  8B F3                           mov esi, ebx
0092D149  E8 A2 4F 25 00                  call 0x140b820f0
0092D14E  4C 8B F8                        mov r15, rax
0092D151  48 85 C0                        test rax, rax
0092D154  75 0A                           jne 0x14092d160
0092D156  BF 17 00 00 C0                  mov edi, 0xc0000017
0092D15B  E9 C3 02 00 00                  jmp 0x14092d423
0092D160  83 FB 08                        cmp ebx, 8
0092D163  73 17                           jae 0x14092d17c
0092D165  33 D2                           xor edx, edx
0092D167  49 8B CF                        mov rcx, r15
0092D16A  BF 23 00 00 C0                  mov edi, 0xc0000023
0092D16F  E8 FC 56 25 00                  call 0x140b82870
0092D174  4D 8B FC                        mov r15, r12
0092D177  E9 A7 02 00 00                  jmp 0x14092d423
0092D17C  8D 47 FE                        lea eax, [rdi - 2]
0092D17F  83 F8 02                        cmp eax, 2
0092D182  0F 87 82 02 00 00               ja 0x14092d40a
0092D188  81 FB FC FF 00 00               cmp ebx, 0xfffc
0092D18E  0F 87 76 02 00 00               ja 0x14092d40a
0092D194  4C 8B C6                        mov r8, rsi
0092D197  33 D2                           xor edx, edx
0092D199  49 8B CF                        mov rcx, r15
0092D19C  E8 9F 9A D9 FF                  call 0x1406c6c40
0092D1A1  0F B7 C3                        movzx eax, bx
0092D1A4  49 8D 5F 08                     lea rbx, [r15 + 8]
0092D1A8  66 41 89 47 02                  mov word ptr [r15 + 2], ax
0092D1AD  49 03 C7                        add rax, r15
0092D1B0  48 3B D8                        cmp rbx, rax
0092D1B3  41 88 3F                        mov byte ptr [r15], dil
0092D1B6  45 88 67 01                     mov byte ptr [r15 + 1], r12b
0092D1BA  41 8B FC                        mov edi, r12d
0092D1BD  49 0F 47 DC                     cmova rbx, r12
0092D1C1  45 89 67 04                     mov dword ptr [r15 + 4], r12d
0092D1C5  4D 85 F6                        test r14, r14
0092D1C8  74 64                           je 0x14092d22e
0092D1CA  49 8D 76 08                     lea rsi, [r14 + 8]
0092D1CE  41 8B EC                        mov ebp, r12d
0092D1D1  66 45 3B 66 04                  cmp r12w, word ptr [r14 + 4]
0092D1D6  73 56                           jae 0x14092d22e
0092D1D8  48 8D 3D 21 2E 6D FF            lea rdi, [rip - 0x92d1df]
0092D1DF  90                              nop
0092D1E0  0F B6 06                        movzx eax, byte ptr [rsi]
0092D1E3  83 C0 FE                        add eax, -2
0092D1E6  83 F8 0E                        cmp eax, 0xe
0092D1E9  77 2E                           ja 0x14092d219
0092D1EB  48 98                           cdqe
0092D1ED  8B 8C 87 84 D4 92 00            mov ecx, dword ptr [rdi + rax*4 + 0x92d484]
0092D1F4  48 03 CF                        add rcx, rdi
0092D1F7  FF E1                           jmp rcx
0092D1F9  CC                              int3
0092D1FA  CC                              int3
0092D1FB  CC                              int3
0092D1FC  CC                              int3
0092D1FD  44 0F B7 46 02                  movzx r8d, word ptr [rsi + 2]
0092D202  48 8B D6                        mov rdx, rsi
0092D205  48 8B CB                        mov rcx, rbx
0092D208  E8 33 96 D9 FF                  call 0x1406c6840
0092D20D  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D212  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0092D216  48 03 D8                        add rbx, rax
0092D219  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0092D21D  FF C5                           inc ebp
0092D21F  48 03 F0                        add rsi, rax
0092D222  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
0092D227  3B E8                           cmp ebp, eax
0092D229  72 B5                           jb 0x14092d1e0
0092D22B  41 8B FC                        mov edi, r12d
0092D22E  4D 85 ED                        test r13, r13
0092D231  74 44                           je 0x14092d277
0092D233  49 8D 6D 08                     lea rbp, [r13 + 8]
0092D237  45 8B F4                        mov r14d, r12d
0092D23A  66 45 3B 65 04                  cmp r12w, word ptr [r13 + 4]
0092D23F  73 36                           jae 0x14092d277
0092D241  80 7D 00 11                     cmp byte ptr [rbp], 0x11
0092D245  75 1C                           jne 0x14092d263
0092D247  44 0F B7 45 02                  movzx r8d, word ptr [rbp + 2]
0092D24C  48 8B D5                        mov rdx, rbp
0092D24F  48 8B CB                        mov rcx, rbx
0092D252  E8 E9 95 D9 FF                  call 0x1406c6840
0092D257  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D25C  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D260  48 03 D8                        add rbx, rax
0092D263  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D267  41 FF C6                        inc r14d
0092D26A  48 03 E8                        add rbp, rax
0092D26D  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
0092D272  44 3B F0                        cmp r14d, eax
0092D275  72 CA                           jb 0x14092d241
0092D277  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
0092D27F  4D 85 ED                        test r13, r13
0092D282  74 44                           je 0x14092d2c8
0092D284  49 8D 6D 08                     lea rbp, [r13 + 8]
0092D288  45 8B F4                        mov r14d, r12d
0092D28B  66 45 3B 65 04                  cmp r12w, word ptr [r13 + 4]
0092D290  73 36                           jae 0x14092d2c8
0092D292  80 7D 00 14                     cmp byte ptr [rbp], 0x14
0092D296  75 1C                           jne 0x14092d2b4
0092D298  44 0F B7 45 02                  movzx r8d, word ptr [rbp + 2]
0092D29D  48 8B D5                        mov rdx, rbp
0092D2A0  48 8B CB                        mov rcx, rbx
0092D2A3  E8 98 95 D9 FF                  call 0x1406c6840
0092D2A8  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D2AD  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D2B1  48 03 D8                        add rbx, rax
0092D2B4  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D2B8  41 FF C6                        inc r14d
0092D2BB  48 03 E8                        add rbp, rax
0092D2BE  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
0092D2C3  44 3B F0                        cmp r14d, eax
0092D2C6  72 CA                           jb 0x14092d292
0092D2C8  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
0092D2D0  4D 85 ED                        test r13, r13
0092D2D3  74 44                           je 0x14092d319
0092D2D5  49 8D 6D 08                     lea rbp, [r13 + 8]
0092D2D9  45 8B F4                        mov r14d, r12d
0092D2DC  66 45 3B 65 04                  cmp r12w, word ptr [r13 + 4]
0092D2E1  73 36                           jae 0x14092d319
0092D2E3  80 7D 00 15                     cmp byte ptr [rbp], 0x15
0092D2E7  75 1C                           jne 0x14092d305
0092D2E9  44 0F B7 45 02                  movzx r8d, word ptr [rbp + 2]
0092D2EE  48 8B D5                        mov rdx, rbp
0092D2F1  48 8B CB                        mov rcx, rbx
0092D2F4  E8 47 95 D9 FF                  call 0x1406c6840
0092D2F9  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D2FE  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D302  48 03 D8                        add rbx, rax
0092D305  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D309  41 FF C6                        inc r14d
0092D30C  48 03 E8                        add rbp, rax
0092D30F  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
0092D314  44 3B F0                        cmp r14d, eax
0092D317  72 CA                           jb 0x14092d2e3
0092D319  4C 8B B4 24 90 00 00 00         mov r14, qword ptr [rsp + 0x90]
0092D321  4D 85 F6                        test r14, r14
0092D324  74 49                           je 0x14092d36f
0092D326  49 8D 76 08                     lea rsi, [r14 + 8]
0092D32A  41 8B EC                        mov ebp, r12d
0092D32D  66 45 3B 66 04                  cmp r12w, word ptr [r14 + 4]
0092D332  73 3B                           jae 0x14092d36f
0092D334  0F B6 0E                        movzx ecx, byte ptr [rsi]
0092D337  83 E9 16                        sub ecx, 0x16
0092D33A  74 05                           je 0x14092d341
0092D33C  83 F9 01                        cmp ecx, 1
0092D33F  75 1C                           jne 0x14092d35d
0092D341  44 0F B7 46 02                  movzx r8d, word ptr [rsi + 2]
0092D346  48 8B D6                        mov rdx, rsi
0092D349  48 8B CB                        mov rcx, rbx
0092D34C  E8 EF 94 D9 FF                  call 0x1406c6840
0092D351  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D356  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0092D35A  48 03 D8                        add rbx, rax
0092D35D  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0092D361  FF C5                           inc ebp
0092D363  48 03 F0                        add rsi, rax
0092D366  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
0092D36B  3B E8                           cmp ebp, eax
0092D36D  72 C5                           jb 0x14092d334
0092D36F  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0092D374  4D 85 ED                        test r13, r13
0092D377  74 44                           je 0x14092d3bd
0092D379  49 8D 6D 08                     lea rbp, [r13 + 8]
0092D37D  45 8B F4                        mov r14d, r12d
0092D380  66 45 3B 65 04                  cmp r12w, word ptr [r13 + 4]
0092D385  73 36                           jae 0x14092d3bd
0092D387  80 7D 00 12                     cmp byte ptr [rbp], 0x12
0092D38B  75 1C                           jne 0x14092d3a9
0092D38D  44 0F B7 45 02                  movzx r8d, word ptr [rbp + 2]
0092D392  48 8B D5                        mov rdx, rbp
0092D395  48 8B CB                        mov rcx, rbx
0092D398  E8 A3 94 D9 FF                  call 0x1406c6840
0092D39D  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D3A2  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D3A6  48 03 D8                        add rbx, rax
0092D3A9  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D3AD  41 FF C6                        inc r14d
0092D3B0  48 03 E8                        add rbp, rax
0092D3B3  41 0F B7 45 04                  movzx eax, word ptr [r13 + 4]
0092D3B8  44 3B F0                        cmp r14d, eax
0092D3BB  72 CA                           jb 0x14092d387
0092D3BD  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0092D3C2  4D 85 F6                        test r14, r14
0092D3C5  74 5C                           je 0x14092d423
0092D3C7  49 8D 6E 08                     lea rbp, [r14 + 8]
0092D3CB  66 45 3B 66 04                  cmp r12w, word ptr [r14 + 4]
0092D3D0  73 51                           jae 0x14092d423
0092D3D2  80 7D 00 13                     cmp byte ptr [rbp], 0x13
0092D3D6  75 1C                           jne 0x14092d3f4
0092D3D8  44 0F B7 45 02                  movzx r8d, word ptr [rbp + 2]
0092D3DD  48 8B D5                        mov rdx, rbp
0092D3E0  48 8B CB                        mov rcx, rbx
0092D3E3  E8 58 94 D9 FF                  call 0x1406c6840
0092D3E8  66 41 FF 47 04                  inc word ptr [r15 + 4]
0092D3ED  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D3F1  48 03 D8                        add rbx, rax
0092D3F4  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D3F8  41 FF C4                        inc r12d
0092D3FB  48 03 E8                        add rbp, rax
0092D3FE  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
0092D403  44 3B E0                        cmp r12d, eax
0092D406  72 CA                           jb 0x14092d3d2
0092D408  EB 19                           jmp 0x14092d423
0092D40A  33 D2                           xor edx, edx
0092D40C  49 8B CF                        mov rcx, r15
0092D40F  BF 0D 00 00 C0                  mov edi, 0xc000000d
0092D414  E8 57 54 25 00                  call 0x140b82870
0092D419  4D 8B FC                        mov r15, r12
0092D41C  EB 05                           jmp 0x14092d423
0092D41E  BF 95 00 00 C0                  mov edi, 0xc0000095
0092D423  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0092D42B  8B C7                           mov eax, edi
0092D42D  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0092D432  4C 89 39                        mov qword ptr [rcx], r15
0092D435  48 83 C4 20                     add rsp, 0x20
0092D439  41 5F                           pop r15
0092D43B  41 5E                           pop r14
0092D43D  41 5D                           pop r13
0092D43F  41 5C                           pop r12
0092D441  5F                              pop rdi
0092D442  5E                              pop rsi
0092D443  5D                              pop rbp
0092D444  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0092CDFD(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p68;

    v_stack_p68 = v_rbx;
    if (v_r14 == 0) goto loc_0092CEA8;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 4)))) goto loc_0092CEA8;
loc_0092CE30:
    result = (unsigned int)((*(unsigned __int8 *)(v_r14 + 8)) + (-2));
    if (((unsigned int)(result)) > 14) goto loc_0092CE92;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9621001 + result * 4 + 9622600))) + (v_rip - 9621072);
loc_0092CE92:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_r10 = (v_r14 + 8) + (*(unsigned __int16 *)(v_r14 + 8 + 2));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 4)))))) goto loc_0092CE30;
loc_0092CEA8:
    if (v_r13 == 0) goto loc_0092CF0F;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_r13 + 4)))) goto loc_0092CF0F;
loc_0092CEC0:
    if ((*(unsigned __int8 *)(v_r13 + 8)) != 17) goto loc_0092CEF8;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r13 + 8 + 2)) + (a2));
    if (((unsigned int)(a1)) < a2) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(v_r13 + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(v_r13))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(v_r13));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a4 = (v_r13 + 8) + (*(unsigned __int16 *)(v_r13 + 8 + 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092CEC0;
loc_0092CF0F:
    if (v_rsi == 0) goto loc_0092CF75;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rsi + 4)))) goto loc_0092CF75;
loc_0092CF26:
    if ((*(unsigned __int8 *)(v_rsi + 8)) != 20) goto loc_0092CF5E;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 8 + 2)) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(v_rsi + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(v_rsi))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(v_rsi));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a4 = (v_rsi + 8) + (*(unsigned __int16 *)(v_rsi + 8 + 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092CF26;
loc_0092CF75:
    if (v_rbp == 0) goto loc_0092CFE0;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rbp + 4)))) goto loc_0092CFE0;
loc_0092CF90:
    if ((*(unsigned __int8 *)(v_rbp + 8)) != 21) goto loc_0092CFC9;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbp + 8 + 2)) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(v_rbp + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(v_rbp))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(v_rbp));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a4 = (v_rbp + 8) + (*(unsigned __int16 *)(v_rbp + 8 + 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092CF90;
loc_0092CFE0:
    if (a18 == 0) goto loc_0092D057;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(a18 + 4)))) goto loc_0092D057;
loc_0092D000:
    a4 = (unsigned int)((*(unsigned __int8 *)(a18 + 8)) - (22));
    if (condition_is_equal) goto loc_0092D014;
    if (((unsigned int)(a4)) != 1) goto loc_0092D042;
loc_0092D014:
    a1 = (unsigned int)((*(unsigned __int16 *)(a18 + 8 + 2)) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(a18 + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(a18))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(a18));
    }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_r10 = (a18 + 8) + (*(unsigned __int16 *)(a18 + 8 + 2));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092D000;
loc_0092D057:
    if (a14 == 0) goto loc_0092D0BF;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(a14 + 4)))) goto loc_0092D0BF;
loc_0092D073:
    if ((*(unsigned __int8 *)(a14 + 8)) != 18) goto loc_0092D0A8;
    a1 = (unsigned int)((*(unsigned __int16 *)(a14 + 8 + 2)) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(a14 + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(a14))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(a14));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a4 = (a14 + 8) + (*(unsigned __int16 *)(a14 + 8 + 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092D073;
loc_0092D0BF:
    if (a15 == 0) goto loc_0092D12C;
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(*(unsigned __int16 *)(a15 + 4)))) goto loc_0092D12C;
loc_0092D0E0:
    if ((*(unsigned __int8 *)(a15 + 8)) != 19) goto loc_0092D115;
    a1 = (unsigned int)((*(unsigned __int16 *)(a15 + 8 + 2)) + ((unsigned int)((unsigned int)((unsigned int)(a1)))));
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    if (a3 != 0) {
        a1 = *(unsigned __int16 *)(a15 + 4);
    }
    if (((unsigned int)(*(unsigned __int8 *)(a15))) >= = ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)(*(unsigned __int8 *)(a15));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    a4 = (a15 + 8) + (*(unsigned __int16 *)(a15 + 8 + 2));
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0092D0E0;
loc_0092D12C:
    if (((unsigned int)((unsigned int)((unsigned int)(a1)) + 3)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_0092D41E;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1)) + 3) & (0xFFFFFFFCULL));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x64536553ULL), a4);
    if (result != 0) goto loc_0092D160;
    goto loc_0092D423;
loc_0092D160:
    if (((unsigned int)(v_rbx)) >= 8) goto loc_0092D17C;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x64536553ULL), a4);
    goto loc_0092D423;
loc_0092D17C:
    if (((unsigned int)((unsigned int)(0xC0000023ULL) - 2)) > 2) goto loc_0092D40A;
    if (((unsigned int)(v_rbx)) > 0xFFFCULL) goto loc_0092D40A;
    a2 = 0;
    result = memset(v_r12, a2, (unsigned int)((unsigned int)(v_rbx)), a4);
    *(unsigned __int16 *)(v_r12 + 2) = (unsigned __int16)((unsigned __int16)(v_rbx));
    result = ((unsigned __int16)(v_rbx)) + (v_r12);
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)((unsigned int)(0xC0000023ULL));
    *(unsigned __int8 *)(v_r12 + 1) = (unsigned __int8)(v_r12);
    v_rbx = v_r12 + 8;
    if ((v_r12 + 8) > result) { v_rbx = v_r12; }
    *(unsigned int *)(v_r12 + 4) = (unsigned int)(v_r12);
    if (v_r14 == 0) goto loc_0092D22E;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(v_r14 + 4))) goto loc_0092D22E;
loc_0092D1E0:
    result = (unsigned int)((*(unsigned __int8 *)(v_r14 + 8)) + (-2));
    if (((unsigned int)(result)) > 14) goto loc_0092D219;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9621983 + result * 4 + 9622660))) + (v_rip - 9621983);
loc_0092D219:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rsi = (v_r14 + 8) + (*(unsigned __int16 *)(v_r14 + 8 + 2));
    if (((unsigned int)(v_rbp)) < ((unsigned int)(*(unsigned __int16 *)(v_r14 + 4)))) goto loc_0092D1E0;
loc_0092D22E:
    if (v_r13 == 0) goto loc_0092D277;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(v_r13 + 4))) goto loc_0092D277;
loc_0092D241:
    result = *(unsigned __int16 *)(v_r14 + 4);
    if ((*(unsigned __int8 *)(v_r13 + 8)) == 17) {
        a3 = *(unsigned __int16 *)(v_r13 + 8 + 2);
        a2 = v_r13 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(v_r13 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rbp = (v_r13 + 8) + (*(unsigned __int16 *)(v_r13 + 8 + 2));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int16 *)(v_r13 + 4)))) goto loc_0092D241;
loc_0092D277:
    if (a16 == 0) goto loc_0092D2C8;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(a16 + 4))) goto loc_0092D2C8;
loc_0092D292:
    result = *(unsigned __int16 *)(v_r13 + 4);
    if ((*(unsigned __int8 *)(a16 + 8)) == 20) {
        a3 = *(unsigned __int16 *)(a16 + 8 + 2);
        a2 = a16 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(a16 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rbp = (a16 + 8) + (*(unsigned __int16 *)(a16 + 8 + 2));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int16 *)(a16 + 4)))) goto loc_0092D292;
loc_0092D2C8:
    if (a17 == 0) goto loc_0092D319;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(a17 + 4))) goto loc_0092D319;
loc_0092D2E3:
    result = *(unsigned __int16 *)(a16 + 4);
    if ((*(unsigned __int8 *)(a17 + 8)) == 21) {
        a3 = *(unsigned __int16 *)(a17 + 8 + 2);
        a2 = a17 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(a17 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rbp = (a17 + 8) + (*(unsigned __int16 *)(a17 + 8 + 2));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int16 *)(a17 + 4)))) goto loc_0092D2E3;
loc_0092D319:
    if (a18 == 0) goto loc_0092D36F;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(a18 + 4))) goto loc_0092D36F;
loc_0092D334:
    a1 = (unsigned int)((*(unsigned __int8 *)(a18 + 8)) - (22));
    if (condition_is_equal) goto loc_0092D341;
    result = *(unsigned __int16 *)(a17 + 4);
    if (((unsigned int)(a1)) == 1) {
        a3 = *(unsigned __int16 *)(a18 + 8 + 2);
        a2 = a18 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(a18 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rsi = (a18 + 8) + (*(unsigned __int16 *)(a18 + 8 + 2));
    if (((unsigned int)(v_rbp)) < ((unsigned int)(*(unsigned __int16 *)(a18 + 4)))) goto loc_0092D334;
loc_0092D36F:
    if (a14 == 0) goto loc_0092D3BD;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(a14 + 4))) goto loc_0092D3BD;
loc_0092D387:
    result = *(unsigned __int16 *)(a18 + 4);
    if ((*(unsigned __int8 *)(a14 + 8)) == 18) {
        a3 = *(unsigned __int16 *)(a14 + 8 + 2);
        a2 = a14 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(a14 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    v_rbp = (a14 + 8) + (*(unsigned __int16 *)(a14 + 8 + 2));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int16 *)(a14 + 4)))) goto loc_0092D387;
loc_0092D3BD:
    if (a15 == 0) goto loc_0092D423;
    if (((unsigned __int16)(v_r12)) >= (*(unsigned __int16 *)(a15 + 4))) goto loc_0092D423;
loc_0092D3D2:
    result = *(unsigned __int16 *)(a14 + 4);
    if ((*(unsigned __int8 *)(a15 + 8)) == 19) {
        a3 = *(unsigned __int16 *)(a15 + 8 + 2);
        a2 = a15 + 8;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned __int16 *)(a15 + 8 + 2);
        v_rbx = (v_rbx) + (result);
    }
    v_r12 = (unsigned int)((v_r12) + 1);
    v_rbp = (a15 + 8) + (*(unsigned __int16 *)(a15 + 8 + 2));
    if (((unsigned int)(v_r12)) < ((unsigned int)(*(unsigned __int16 *)(a15 + 4)))) goto loc_0092D3D2;
    goto loc_0092D423;
loc_0092D40A:
    a2 = 0;
    result = ExFreePoolWithTag(v_r12, a2, a3, a4);
    goto loc_0092D423;
loc_0092D41E:
loc_0092D423:
    *(unsigned __int64 *)(a19) = v_r12;
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0092CDFD(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16, int64_t Arg17, int64_t Arg18, void *Arg19)
{
    uint8_t *arg19 = (uint8_t *)Arg19;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p68;

    v_stack_p68 = local_rbx;
    if (local_r14 == 0) goto loc_0092CEA8;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(local_r14 + 0x4)))) goto loc_0092CEA8;
loc_0092CE30:
    result = (uint32_t)((*(uint8_t *)(local_r14 + 0x8)) + (-2));
    if (((uint32_t)(result)) > 14) goto loc_0092CE92;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x92CE09 + result * 4 + 0x92D448))) + (v_rip - 9621072);
loc_0092CE92:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_r10 = (local_r14 + 8) + (*(uint16_t *)(local_r14 + 0x8 + 0x2));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint16_t)((uint16_t)(*(uint16_t *)(local_r14 + 0x4)))))) goto loc_0092CE30;
loc_0092CEA8:
    if (local_r13 == 0) goto loc_0092CF0F;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(local_r13 + 0x4)))) goto loc_0092CF0F;
loc_0092CEC0:
    if ((*(uint8_t *)(local_r13 + 0x8)) != 17) goto loc_0092CEF8;
    Arg1 = (uint32_t)((*(uint16_t *)(local_r13 + 0x8 + 0x2)) + (Arg2));
    if (((uint32_t)(Arg1)) < Arg2) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(local_r13 + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(local_r13))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(local_r13));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg4 = (local_r13 + 8) + (*(uint16_t *)(local_r13 + 0x8 + 0x2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092CEC0;
loc_0092CF0F:
    if (local_rsi == 0) goto loc_0092CF75;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(local_rsi + 0x4)))) goto loc_0092CF75;
loc_0092CF26:
    if ((*(uint8_t *)(local_rsi + 0x8)) != 20) goto loc_0092CF5E;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x8 + 0x2)) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(local_rsi + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(local_rsi))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(local_rsi));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg4 = (local_rsi + 8) + (*(uint16_t *)(local_rsi + 0x8 + 0x2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092CF26;
loc_0092CF75:
    if (local_rbp == 0) goto loc_0092CFE0;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(local_rbp + 0x4)))) goto loc_0092CFE0;
loc_0092CF90:
    if ((*(uint8_t *)(local_rbp + 0x8)) != 21) goto loc_0092CFC9;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbp + 0x8 + 0x2)) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(local_rbp + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(local_rbp))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(local_rbp));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg4 = (local_rbp + 8) + (*(uint16_t *)(local_rbp + 0x8 + 0x2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092CF90;
loc_0092CFE0:
    if (Arg18 == 0) goto loc_0092D057;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(Arg18 + 0x4)))) goto loc_0092D057;
loc_0092D000:
    Arg4 = (uint32_t)((*(uint8_t *)(Arg18 + 0x8)) - (22));
    if (condition_is_equal) goto loc_0092D014;
    if (((uint32_t)(Arg4)) != 1) goto loc_0092D042;
loc_0092D014:
    Arg1 = (uint32_t)((*(uint16_t *)(Arg18 + 0x8 + 0x2)) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(Arg18 + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(Arg18))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(Arg18));
    }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_r10 = (Arg18 + 8) + (*(uint16_t *)(Arg18 + 0x8 + 0x2));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092D000;
loc_0092D057:
    if (Arg14 == 0) goto loc_0092D0BF;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(Arg14 + 0x4)))) goto loc_0092D0BF;
loc_0092D073:
    if ((*(uint8_t *)(Arg14 + 0x8)) != 18) goto loc_0092D0A8;
    Arg1 = (uint32_t)((*(uint16_t *)(Arg14 + 0x8 + 0x2)) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(Arg14 + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(Arg14))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(Arg14));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg4 = (Arg14 + 8) + (*(uint16_t *)(Arg14 + 0x8 + 0x2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092D073;
loc_0092D0BF:
    if (Arg15 == 0) goto loc_0092D12C;
    if (((uint16_t)(local_r12)) >= ((uint16_t)(*(uint16_t *)(Arg15 + 0x4)))) goto loc_0092D12C;
loc_0092D0E0:
    if ((*(uint8_t *)(Arg15 + 0x8)) != 19) goto loc_0092D115;
    Arg1 = (uint32_t)((*(uint16_t *)(Arg15 + 0x8 + 0x2)) + ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    if (Arg3 != 0) {
        Arg1 = *(uint16_t *)(Arg15 + 0x4);
    }
    if (((uint32_t)(*(uint8_t *)(Arg15))) >= = ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)(*(uint8_t *)(Arg15));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    Arg4 = (Arg15 + 8) + (*(uint16_t *)(Arg15 + 0x8 + 0x2));
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0092D0E0;
loc_0092D12C:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)) + 3)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_0092D41E;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1)) + 3) & (0xFFFFFFFCULL));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x64536553ULL), Arg4);
    if (result != 0) goto loc_0092D160;
    goto loc_0092D423;
loc_0092D160:
    if (((uint32_t)(local_rbx)) >= 8) goto loc_0092D17C;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x64536553ULL), Arg4);
    goto loc_0092D423;
loc_0092D17C:
    if (((uint32_t)((uint32_t)(0xC0000023ULL) - 2)) > 2) goto loc_0092D40A;
    if (((uint32_t)(local_rbx)) > 0xFFFCULL) goto loc_0092D40A;
    Arg2 = 0;
    result = memset(local_r12, Arg2, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    *(uint16_t *)(local_r12 + 0x2) = (uint16_t)((uint16_t)(local_rbx));
    result = ((uint16_t)(local_rbx)) + (local_r12);
    *(uint8_t *)(local_r12) = (uint8_t)((uint32_t)(0xC0000023ULL));
    *(uint8_t *)(local_r12 + 0x1) = (uint8_t)(local_r12);
    local_rbx = local_r12 + 8;
    if ((local_r12 + 8) > result) { local_rbx = local_r12; }
    *(uint32_t *)(local_r12 + 0x4) = (uint32_t)(local_r12);
    if (local_r14 == 0) goto loc_0092D22E;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(local_r14 + 0x4))) goto loc_0092D22E;
loc_0092D1E0:
    result = (uint32_t)((*(uint8_t *)(local_r14 + 0x8)) + (-2));
    if (((uint32_t)(result)) > 14) goto loc_0092D219;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x92D1DF + result * 4 + 0x92D484))) + (v_rip - 9621983);
loc_0092D219:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rsi = (local_r14 + 8) + (*(uint16_t *)(local_r14 + 0x8 + 0x2));
    if (((uint32_t)(local_rbp)) < ((uint32_t)(*(uint16_t *)(local_r14 + 0x4)))) goto loc_0092D1E0;
loc_0092D22E:
    if (local_r13 == 0) goto loc_0092D277;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(local_r13 + 0x4))) goto loc_0092D277;
loc_0092D241:
    result = *(uint16_t *)(local_r14 + 0x4);
    if ((*(uint8_t *)(local_r13 + 0x8)) == 17) {
        Arg3 = *(uint16_t *)(local_r13 + 0x8 + 0x2);
        Arg2 = local_r13 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(local_r13 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rbp = (local_r13 + 8) + (*(uint16_t *)(local_r13 + 0x8 + 0x2));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint16_t *)(local_r13 + 0x4)))) goto loc_0092D241;
loc_0092D277:
    if (Arg16 == 0) goto loc_0092D2C8;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(Arg16 + 0x4))) goto loc_0092D2C8;
loc_0092D292:
    result = *(uint16_t *)(local_r13 + 0x4);
    if ((*(uint8_t *)(Arg16 + 0x8)) == 20) {
        Arg3 = *(uint16_t *)(Arg16 + 0x8 + 0x2);
        Arg2 = Arg16 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(Arg16 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rbp = (Arg16 + 8) + (*(uint16_t *)(Arg16 + 0x8 + 0x2));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint16_t *)(Arg16 + 0x4)))) goto loc_0092D292;
loc_0092D2C8:
    if (Arg17 == 0) goto loc_0092D319;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(Arg17 + 0x4))) goto loc_0092D319;
loc_0092D2E3:
    result = *(uint16_t *)(Arg16 + 0x4);
    if ((*(uint8_t *)(Arg17 + 0x8)) == 21) {
        Arg3 = *(uint16_t *)(Arg17 + 0x8 + 0x2);
        Arg2 = Arg17 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(Arg17 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rbp = (Arg17 + 8) + (*(uint16_t *)(Arg17 + 0x8 + 0x2));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint16_t *)(Arg17 + 0x4)))) goto loc_0092D2E3;
loc_0092D319:
    if (Arg18 == 0) goto loc_0092D36F;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(Arg18 + 0x4))) goto loc_0092D36F;
loc_0092D334:
    Arg1 = (uint32_t)((*(uint8_t *)(Arg18 + 0x8)) - (22));
    if (condition_is_equal) goto loc_0092D341;
    result = *(uint16_t *)(Arg17 + 0x4);
    if (((uint32_t)(Arg1)) == 1) {
        Arg3 = *(uint16_t *)(Arg18 + 0x8 + 0x2);
        Arg2 = Arg18 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(Arg18 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rsi = (Arg18 + 8) + (*(uint16_t *)(Arg18 + 0x8 + 0x2));
    if (((uint32_t)(local_rbp)) < ((uint32_t)(*(uint16_t *)(Arg18 + 0x4)))) goto loc_0092D334;
loc_0092D36F:
    if (Arg14 == 0) goto loc_0092D3BD;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(Arg14 + 0x4))) goto loc_0092D3BD;
loc_0092D387:
    result = *(uint16_t *)(Arg18 + 0x4);
    if ((*(uint8_t *)(Arg14 + 0x8)) == 18) {
        Arg3 = *(uint16_t *)(Arg14 + 0x8 + 0x2);
        Arg2 = Arg14 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(Arg14 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    local_rbp = (Arg14 + 8) + (*(uint16_t *)(Arg14 + 0x8 + 0x2));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint16_t *)(Arg14 + 0x4)))) goto loc_0092D387;
loc_0092D3BD:
    if (Arg15 == 0) goto loc_0092D423;
    if (((uint16_t)(local_r12)) >= (*(uint16_t *)(Arg15 + 0x4))) goto loc_0092D423;
loc_0092D3D2:
    result = *(uint16_t *)(Arg14 + 0x4);
    if ((*(uint8_t *)(Arg15 + 0x8)) == 19) {
        Arg3 = *(uint16_t *)(Arg15 + 0x8 + 0x2);
        Arg2 = Arg15 + 8;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = *(uint16_t *)(Arg15 + 0x8 + 0x2);
        local_rbx = (local_rbx) + (result);
    }
    local_r12 = (uint32_t)((local_r12) + 1);
    local_rbp = (Arg15 + 8) + (*(uint16_t *)(Arg15 + 0x8 + 0x2));
    if (((uint32_t)(local_r12)) < ((uint32_t)(*(uint16_t *)(Arg15 + 0x4)))) goto loc_0092D3D2;
    goto loc_0092D423;
loc_0092D40A:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r12, Arg2, Arg3, Arg4);
    goto loc_0092D423;
loc_0092D41E:
loc_0092D423:
    *(uint64_t *)(arg19) = local_r12;
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg19` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092CDFD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
