# Amd64ConfigureCounter

- RVA: `0x0056BE58`–`0x0056C203` (길이 `939` bytes)
- VA: `0x000000014056BE58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6CEC`
- 디코드: `277`개 명령, `939/939` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Amd64DisableMonitoring](Amd64DisableMonitoring_function_0056C210.md) at `0x0056C323`
- [Amd64EnableMonitoring](Amd64EnableMonitoring_function_0056C360.md) at `0x0056C4CC`
- [Amd64RestartProfilingInternal](../../pagelk/B6/Amd64RestartProfilingInternal_function_00B61E0C.md) at `0x00B61EA4`

### Static image references
- `0x0056BE75` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056BE58  48 8B C4                        mov rax, rsp
0056BE5B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0056BE5F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0056BE63  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0056BE67  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0056BE6B  41 56                           push r14
0056BE6D  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0056BE75  4C 8D 35 84 41 A9 FF            lea r14, [rip - 0x56be7c]
0056BE7C  44 8B D8                        mov r11d, eax
0056BE7F  41 8A F8                        mov dil, r8b
0056BE82  45 33 C0                        xor r8d, r8d
0056BE85  8B F1                           mov esi, ecx
0056BE87  49 8B E9                        mov rbp, r9
0056BE8A  49 8B 84 C6 40 8C FC 00         mov rax, qword ptr [r14 + rax*8 + 0xfc8c40]
0056BE92  4C 8B 50 58                     mov r10, qword ptr [rax + 0x58]
0056BE96  85 D2                           test edx, edx
0056BE98  74 26                           je 0x14056bec0
0056BE9A  83 EA 01                        sub edx, 1
0056BE9D  74 1B                           je 0x14056beba
0056BE9F  83 EA 63                        sub edx, 0x63
0056BEA2  74 10                           je 0x14056beb4
0056BEA4  83 FA 01                        cmp edx, 1
0056BEA7  74 05                           je 0x14056beae
0056BEA9  45 8B C8                        mov r9d, r8d
0056BEAC  EB 15                           jmp 0x14056bec3
0056BEAE  4D 8D 4A 48                     lea r9, [r10 + 0x48]
0056BEB2  EB 0F                           jmp 0x14056bec3
0056BEB4  4D 8D 4A 30                     lea r9, [r10 + 0x30]
0056BEB8  EB 09                           jmp 0x14056bec3
0056BEBA  4D 8D 4A 18                     lea r9, [r10 + 0x18]
0056BEBE  EB 03                           jmp 0x14056bec3
0056BEC0  4D 8B CA                        mov r9, r10
0056BEC3  41 8B 11                        mov edx, dword ptr [r9]
0056BEC6  49 8B 59 10                     mov rbx, qword ptr [r9 + 0x10]
0056BECA  85 D2                           test edx, edx
0056BECC  0F 85 BB 01 00 00               jne 0x14056c08d
0056BED2  48 8D 04 76                     lea rax, [rsi + rsi*2]
0056BED6  48 03 C0                        add rax, rax
0056BED9  48 8B 44 C3 10                  mov rax, qword ptr [rbx + rax*8 + 0x10]
0056BEDE  44 38 40 08                     cmp byte ptr [rax + 8], r8b
0056BEE2  0F 84 A5 01 00 00               je 0x14056c08d
0056BEE8  41 8B C8                        mov ecx, r8d
0056BEEB  40 84 FF                        test dil, dil
0056BEEE  0F 84 06 01 00 00               je 0x14056bffa
0056BEF4  8D 46 01                        lea eax, [rsi + 1]
0056BEF7  48 8D 04 40                     lea rax, [rax + rax*2]
0056BEFB  48 03 C0                        add rax, rax
0056BEFE  48 8B 44 C3 10                  mov rax, qword ptr [rbx + rax*8 + 0x10]
0056BF03  48 8B 38                        mov rdi, qword ptr [rax]
0056BF06  48 0F BA EF 16                  bts rdi, 0x16
0056BF0B  44 38 44 24 38                  cmp byte ptr [rsp + 0x38], r8b
0056BF10  74 07                           je 0x14056bf19
0056BF12  BB FF FF 00 00                  mov ebx, 0xffff
0056BF17  EB 44                           jmp 0x14056bf5d
0056BF19  49 8B D8                        mov rbx, r8
0056BF1C  83 EA 01                        sub edx, 1
0056BF1F  74 2E                           je 0x14056bf4f
0056BF21  83 EA 63                        sub edx, 0x63
0056BF24  74 16                           je 0x14056bf3c
0056BF26  83 FA 01                        cmp edx, 1
0056BF29  75 32                           jne 0x14056bf5d
0056BF2B  49 8D 4A 30                     lea rcx, [r10 + 0x30]
0056BF2F  48 85 C9                        test rcx, rcx
0056BF32  75 05                           jne 0x14056bf39
0056BF34  41 8B C8                        mov ecx, r8d
0056BF37  EB 03                           jmp 0x14056bf3c
0056BF39  8B 49 04                        mov ecx, dword ptr [rcx + 4]
0056BF3C  49 8D 42 18                     lea rax, [r10 + 0x18]
0056BF40  48 85 C0                        test rax, rax
0056BF43  75 05                           jne 0x14056bf4a
0056BF45  41 8B C0                        mov eax, r8d
0056BF48  EB 03                           jmp 0x14056bf4d
0056BF4A  8B 40 04                        mov eax, dword ptr [rax + 4]
0056BF4D  03 C8                           add ecx, eax
0056BF4F  41 8B C0                        mov eax, r8d
0056BF52  4D 85 D2                        test r10, r10
0056BF55  74 04                           je 0x14056bf5b
0056BF57  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0056BF5B  03 C8                           add ecx, eax
0056BF5D  8D 46 01                        lea eax, [rsi + 1]
0056BF60  48 8B D3                        mov rdx, rbx
0056BF63  03 C1                           add eax, ecx
0056BF65  48 C1 EA 20                     shr rdx, 0x20
0056BF69  41 8B 8C 86 C0 F8 F8 00         mov ecx, dword ptr [r14 + rax*4 + 0xf8f8c0]
0056BF71  48 8B C3                        mov rax, rbx
0056BF74  0F 30                           wrmsr
0056BF76  41 8B 09                        mov ecx, dword ptr [r9]
0056BF79  41 8B D0                        mov edx, r8d
0056BF7C  83 E9 01                        sub ecx, 1
0056BF7F  74 40                           je 0x14056bfc1
0056BF81  83 E9 63                        sub ecx, 0x63
0056BF84  74 1F                           je 0x14056bfa5
0056BF86  83 F9 01                        cmp ecx, 1
0056BF89  75 51                           jne 0x14056bfdc
0056BF8B  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056BF93  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056BF97  48 83 C2 30                     add rdx, 0x30
0056BF9B  75 05                           jne 0x14056bfa2
0056BF9D  41 8B D0                        mov edx, r8d
0056BFA0  EB 03                           jmp 0x14056bfa5
0056BFA2  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056BFA5  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056BFAD  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056BFB1  48 83 C0 18                     add rax, 0x18
0056BFB5  75 05                           jne 0x14056bfbc
0056BFB7  41 8B C0                        mov eax, r8d
0056BFBA  EB 03                           jmp 0x14056bfbf
0056BFBC  8B 40 04                        mov eax, dword ptr [rax + 4]
0056BFBF  03 D0                           add edx, eax
0056BFC1  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056BFC9  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056BFCD  48 85 C0                        test rax, rax
0056BFD0  75 05                           jne 0x14056bfd7
0056BFD2  41 8B C0                        mov eax, r8d
0056BFD5  EB 03                           jmp 0x14056bfda
0056BFD7  8B 40 04                        mov eax, dword ptr [rax + 4]
0056BFDA  03 D0                           add edx, eax
0056BFDC  8D 46 01                        lea eax, [rsi + 1]
0056BFDF  03 C2                           add eax, edx
0056BFE1  48 8B D7                        mov rdx, rdi
0056BFE4  48 C1 EA 20                     shr rdx, 0x20
0056BFE8  41 8B 8C 86 40 F9 F8 00         mov ecx, dword ptr [r14 + rax*4 + 0xf8f940]
0056BFF0  48 8B C7                        mov rax, rdi
0056BFF3  0F 30                           wrmsr
0056BFF5  E9 98 00 00 00                  jmp 0x14056c092
0056BFFA  83 EA 01                        sub edx, 1
0056BFFD  74 2E                           je 0x14056c02d
0056BFFF  83 EA 63                        sub edx, 0x63
0056C002  74 16                           je 0x14056c01a
0056C004  83 FA 01                        cmp edx, 1
0056C007  75 32                           jne 0x14056c03b
0056C009  49 8D 4A 30                     lea rcx, [r10 + 0x30]
0056C00D  48 85 C9                        test rcx, rcx
0056C010  75 05                           jne 0x14056c017
0056C012  41 8B C8                        mov ecx, r8d
0056C015  EB 03                           jmp 0x14056c01a
0056C017  8B 49 04                        mov ecx, dword ptr [rcx + 4]
0056C01A  49 8D 42 18                     lea rax, [r10 + 0x18]
0056C01E  48 85 C0                        test rax, rax
0056C021  75 05                           jne 0x14056c028
0056C023  41 8B C0                        mov eax, r8d
0056C026  EB 03                           jmp 0x14056c02b
0056C028  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C02B  03 C8                           add ecx, eax
0056C02D  41 8B C0                        mov eax, r8d
0056C030  4D 85 D2                        test r10, r10
0056C033  74 04                           je 0x14056c039
0056C035  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0056C039  03 C8                           add ecx, eax
0056C03B  8D 46 01                        lea eax, [rsi + 1]
0056C03E  03 C1                           add eax, ecx
0056C040  41 8B 8C 86 40 F9 F8 00         mov ecx, dword ptr [r14 + rax*4 + 0xf8f940]
0056C048  33 C0                           xor eax, eax
0056C04A  33 D2                           xor edx, edx
0056C04C  0F 30                           wrmsr
0056C04E  41 8B 09                        mov ecx, dword ptr [r9]
0056C051  41 8B D0                        mov edx, r8d
0056C054  83 E9 01                        sub ecx, 1
0056C057  0F 84 59 01 00 00               je 0x14056c1b6
0056C05D  83 E9 63                        sub ecx, 0x63
0056C060  0F 84 34 01 00 00               je 0x14056c19a
0056C066  83 F9 01                        cmp ecx, 1
0056C069  0F 85 62 01 00 00               jne 0x14056c1d1
0056C06F  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C077  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056C07B  48 83 C2 30                     add rdx, 0x30
0056C07F  0F 85 12 01 00 00               jne 0x14056c197
0056C085  41 8B D0                        mov edx, r8d
0056C088  E9 0D 01 00 00                  jmp 0x14056c19a
0056C08D  40 84 FF                        test dil, dil
0056C090  74 BC                           je 0x14056c04e
0056C092  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
0056C097  49 8B D8                        mov rbx, r8
0056C09A  49 0F BA EA 16                  bts r10, 0x16
0056C09F  44 38 44 24 38                  cmp byte ptr [rsp + 0x38], r8b
0056C0A4  74 08                           je 0x14056c0ae
0056C0A6  48 8B DD                        mov rbx, rbp
0056C0A9  49 0F BA EA 14                  bts r10, 0x14
0056C0AE  41 8B 09                        mov ecx, dword ptr [r9]
0056C0B1  41 8B D0                        mov edx, r8d
0056C0B4  83 E9 01                        sub ecx, 1
0056C0B7  74 40                           je 0x14056c0f9
0056C0B9  83 E9 63                        sub ecx, 0x63
0056C0BC  74 1F                           je 0x14056c0dd
0056C0BE  83 F9 01                        cmp ecx, 1
0056C0C1  75 51                           jne 0x14056c114
0056C0C3  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C0CB  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056C0CF  48 83 C2 30                     add rdx, 0x30
0056C0D3  75 05                           jne 0x14056c0da
0056C0D5  41 8B D0                        mov edx, r8d
0056C0D8  EB 03                           jmp 0x14056c0dd
0056C0DA  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056C0DD  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C0E5  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056C0E9  48 83 C0 18                     add rax, 0x18
0056C0ED  75 05                           jne 0x14056c0f4
0056C0EF  41 8B C0                        mov eax, r8d
0056C0F2  EB 03                           jmp 0x14056c0f7
0056C0F4  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C0F7  03 D0                           add edx, eax
0056C0F9  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C101  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056C105  48 85 C0                        test rax, rax
0056C108  75 05                           jne 0x14056c10f
0056C10A  41 8B C0                        mov eax, r8d
0056C10D  EB 03                           jmp 0x14056c112
0056C10F  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C112  03 D0                           add edx, eax
0056C114  8D 04 32                        lea eax, [rdx + rsi]
0056C117  48 F7 DB                        neg rbx
0056C11A  41 8B 8C 86 C0 F8 F8 00         mov ecx, dword ptr [r14 + rax*4 + 0xf8f8c0]
0056C122  48 8B D3                        mov rdx, rbx
0056C125  48 C1 EA 20                     shr rdx, 0x20
0056C129  48 8B C3                        mov rax, rbx
0056C12C  0F 30                           wrmsr
0056C12E  41 8B 09                        mov ecx, dword ptr [r9]
0056C131  41 8B D0                        mov edx, r8d
0056C134  83 E9 01                        sub ecx, 1
0056C137  74 44                           je 0x14056c17d
0056C139  83 E9 63                        sub ecx, 0x63
0056C13C  74 23                           je 0x14056c161
0056C13E  83 F9 01                        cmp ecx, 1
0056C141  0F 85 8D 00 00 00               jne 0x14056c1d4
0056C147  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C14F  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
0056C153  48 83 C2 30                     add rdx, 0x30
0056C157  75 05                           jne 0x14056c15e
0056C159  41 8B D0                        mov edx, r8d
0056C15C  EB 03                           jmp 0x14056c161
0056C15E  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056C161  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C169  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056C16D  48 83 C0 18                     add rax, 0x18
0056C171  75 05                           jne 0x14056c178
0056C173  41 8B C0                        mov eax, r8d
0056C176  EB 03                           jmp 0x14056c17b
0056C178  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C17B  03 D0                           add edx, eax
0056C17D  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C185  48 8B 48 58                     mov rcx, qword ptr [rax + 0x58]
0056C189  48 85 C9                        test rcx, rcx
0056C18C  74 04                           je 0x14056c192
0056C18E  44 8B 41 04                     mov r8d, dword ptr [rcx + 4]
0056C192  41 03 D0                        add edx, r8d
0056C195  EB 3D                           jmp 0x14056c1d4
0056C197  8B 52 04                        mov edx, dword ptr [rdx + 4]
0056C19A  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C1A2  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056C1A6  48 83 C0 18                     add rax, 0x18
0056C1AA  75 05                           jne 0x14056c1b1
0056C1AC  41 8B C0                        mov eax, r8d
0056C1AF  EB 03                           jmp 0x14056c1b4
0056C1B1  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C1B4  03 D0                           add edx, eax
0056C1B6  4B 8B 84 DE 40 8C FC 00         mov rax, qword ptr [r14 + r11*8 + 0xfc8c40]
0056C1BE  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0056C1C2  48 85 C0                        test rax, rax
0056C1C5  75 05                           jne 0x14056c1cc
0056C1C7  41 8B C0                        mov eax, r8d
0056C1CA  EB 03                           jmp 0x14056c1cf
0056C1CC  8B 40 04                        mov eax, dword ptr [rax + 4]
0056C1CF  03 D0                           add edx, eax
0056C1D1  4D 8B D0                        mov r10, r8
0056C1D4  8D 04 32                        lea eax, [rdx + rsi]
0056C1D7  49 8B D2                        mov rdx, r10
0056C1DA  41 8B 8C 86 40 F9 F8 00         mov ecx, dword ptr [r14 + rax*4 + 0xf8f940]
0056C1E2  49 8B C2                        mov rax, r10
0056C1E5  48 C1 EA 20                     shr rdx, 0x20
0056C1E9  0F 30                           wrmsr
0056C1EB  48 8B 5C 24 10                  mov rbx, qword ptr [rsp + 0x10]
0056C1F0  48 8B 6C 24 18                  mov rbp, qword ptr [rsp + 0x18]
0056C1F5  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
0056C1FA  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
0056C1FF  41 5E                           pop r14
0056C201  C3                              ret
0056C202  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64ConfigureCounter(int a1, int a2, int a3, __int64 a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    a3 = 0;
    if (a2 == 0) goto loc_0056BEC0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0056BEBA;
    a2 = (unsigned int)((a2) - (99));
    if (condition_is_equal) goto loc_0056BEB4;
    if (a2 == 1) goto loc_0056BEAE;
    goto loc_0056BEC3;
loc_0056BEAE:
    goto loc_0056BEC3;
loc_0056BEB4:
    goto loc_0056BEC3;
loc_0056BEBA:
    goto loc_0056BEC3;
loc_0056BEC0:
loc_0056BEC3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) != 0) goto loc_0056C08D;
    result = ((unsigned int)(a1) + (unsigned int)(a1) * 2) + ((unsigned int)(a1) + (unsigned int)(a1) * 2);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 16) + result * 8 + 16) + 8)) == 0) goto loc_0056C08D;
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_0056BFFA;
    result = ((unsigned int)(a1) + 1 + (unsigned int)(a1) + 1 * 2) + ((unsigned int)(a1) + 1 + (unsigned int)(a1) + 1 * 2);
    if (a6 == 0) goto loc_0056BF19;
    goto loc_0056BF5D;
loc_0056BF19:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056BF4F;
    a2 = (unsigned int)((a2) - (99));
    if (condition_is_equal) goto loc_0056BF3C;
    if (a2 != 1) goto loc_0056BF5D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 48 != 0) goto loc_0056BF39;
    goto loc_0056BF3C;
loc_0056BF39:
loc_0056BF3C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 24 != 0) goto loc_0056BF4A;
    goto loc_0056BF4D;
loc_0056BF4A:
loc_0056BF4D:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056BF4F:
    result = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 4);
    }
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
loc_0056BF5D:
    result = (unsigned int)(((unsigned int)(a1) + 1) + (a1));
    a2 = (0) >> (32);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056BFC1;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056BFA5;
    if (a1 != 1) goto loc_0056BFDC;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (48);
    if (condition_is_not_equal) goto loc_0056BFA2;
    goto loc_0056BFA5;
loc_0056BFA2:
loc_0056BFA5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (24);
    if (condition_is_not_equal) goto loc_0056BFBC;
    goto loc_0056BFBF;
loc_0056BFBC:
loc_0056BFBF:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056BFC1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) != 0) goto loc_0056BFD7;
    goto loc_0056BFDA;
loc_0056BFD7:
loc_0056BFDA:
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056BFDC:
    result = (unsigned int)(((unsigned int)(a1) + 1) + (a2));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 16) + result * 8 + 16))) >> (32);
    goto loc_0056C092;
loc_0056BFFA:
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0056C02D;
    a2 = (unsigned int)((a2) - (99));
    if (condition_is_equal) goto loc_0056C01A;
    if (a2 != 1) goto loc_0056C03B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 48 != 0) goto loc_0056C017;
    goto loc_0056C01A;
loc_0056C017:
loc_0056C01A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 24 != 0) goto loc_0056C028;
    goto loc_0056C02B;
loc_0056C028:
loc_0056C02B:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056C02D:
    result = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 4);
    }
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
loc_0056C03B:
    result = (unsigned int)(((unsigned int)(a1) + 1) + (a1));
    result = 0;
    a2 = 0;
loc_0056C04E:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056C1B6;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056C19A;
    if (a1 != 1) goto loc_0056C1D1;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (48);
    if (condition_is_not_equal) goto loc_0056C197;
    goto loc_0056C19A;
loc_0056C08D:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88) + 16) + result * 8 + 16))) == 0) goto loc_0056C04E;
loc_0056C092:
    v_rbx = 0;
    if (a6 != 0) {
        v_rbx = a4;
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056C0F9;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056C0DD;
    if (a1 != 1) goto loc_0056C114;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (48);
    if (condition_is_not_equal) goto loc_0056C0DA;
    goto loc_0056C0DD;
loc_0056C0DA:
loc_0056C0DD:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (24);
    if (condition_is_not_equal) goto loc_0056C0F4;
    goto loc_0056C0F7;
loc_0056C0F4:
loc_0056C0F7:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056C0F9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) != 0) goto loc_0056C10F;
    goto loc_0056C112;
loc_0056C10F:
loc_0056C112:
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056C114:
    v_rbx = -(v_rbx);
    a2 = (v_rbx) >> (32);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 16550976) + 88)))) - (1));
    if (condition_is_equal) goto loc_0056C17D;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0056C161;
    if (a1 != 1) goto loc_0056C1D4;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (48);
    if (condition_is_not_equal) goto loc_0056C15E;
    goto loc_0056C161;
loc_0056C15E:
loc_0056C161:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (24);
    if (condition_is_not_equal) goto loc_0056C178;
    goto loc_0056C17B;
loc_0056C178:
loc_0056C17B:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
loc_0056C17D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) != 0) {
        a3 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) + 4);
    }
    a2 = (unsigned int)((a2) + (a3));
    goto loc_0056C1D4;
loc_0056C197:
loc_0056C19A:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88)) + (24);
    if (condition_is_not_equal) goto loc_0056C1B1;
    goto loc_0056C1B4;
loc_0056C1B1:
loc_0056C1B4:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) + ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a3) + 4)))));
loc_0056C1B6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 5684860 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 16550976) + 88) != 0) goto loc_0056C1CC;
    goto loc_0056C1CF;
loc_0056C1CC:
loc_0056C1CF:
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a3) + 4)))));
loc_0056C1D1:
loc_0056C1D4:
    a2 = (a3) >> (32);
    return a3;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64ConfigureCounter(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    Arg3 = 0;
    if (Arg2 == 0) goto loc_0056BEC0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0056BEBA;
    Arg2 = (uint32_t)((Arg2) - (99));
    if (condition_is_equal) goto loc_0056BEB4;
    if (Arg2 == 1) goto loc_0056BEAE;
    goto loc_0056BEC3;
loc_0056BEAE:
    goto loc_0056BEC3;
loc_0056BEB4:
    goto loc_0056BEC3;
loc_0056BEBA:
    goto loc_0056BEC3;
loc_0056BEC0:
loc_0056BEC3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) != 0) goto loc_0056C08D;
    result = ((uint32_t)(Arg1) + (uint32_t)(Arg1) * 2) + ((uint32_t)(Arg1) + (uint32_t)(Arg1) * 2);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x10) + result * 8 + 0x10) + 0x8)) == 0) goto loc_0056C08D;
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_0056BFFA;
    result = ((uint32_t)(Arg1) + 1 + (uint32_t)(Arg1) + 1 * 2) + ((uint32_t)(Arg1) + 1 + (uint32_t)(Arg1) + 1 * 2);
    if (Arg6 == 0) goto loc_0056BF19;
    goto loc_0056BF5D;
loc_0056BF19:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056BF4F;
    Arg2 = (uint32_t)((Arg2) - (99));
    if (condition_is_equal) goto loc_0056BF3C;
    if (Arg2 != 1) goto loc_0056BF5D;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 48 != 0) goto loc_0056BF39;
    goto loc_0056BF3C;
loc_0056BF39:
loc_0056BF3C:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 24 != 0) goto loc_0056BF4A;
    goto loc_0056BF4D;
loc_0056BF4A:
loc_0056BF4D:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056BF4F:
    result = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
loc_0056BF5D:
    result = (uint32_t)(((uint32_t)(Arg1) + 1) + (Arg1));
    Arg2 = (0) >> (32);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056BFC1;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056BFA5;
    if (Arg1 != 1) goto loc_0056BFDC;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (condition_is_not_equal) goto loc_0056BFA2;
    goto loc_0056BFA5;
loc_0056BFA2:
loc_0056BFA5:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (condition_is_not_equal) goto loc_0056BFBC;
    goto loc_0056BFBF;
loc_0056BFBC:
loc_0056BFBF:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056BFC1:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) != 0) goto loc_0056BFD7;
    goto loc_0056BFDA;
loc_0056BFD7:
loc_0056BFDA:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056BFDC:
    result = (uint32_t)(((uint32_t)(Arg1) + 1) + (Arg2));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x10) + result * 8 + 0x10))) >> (32);
    goto loc_0056C092;
loc_0056BFFA:
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0056C02D;
    Arg2 = (uint32_t)((Arg2) - (99));
    if (condition_is_equal) goto loc_0056C01A;
    if (Arg2 != 1) goto loc_0056C03B;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 48 != 0) goto loc_0056C017;
    goto loc_0056C01A;
loc_0056C017:
loc_0056C01A:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 24 != 0) goto loc_0056C028;
    goto loc_0056C02B;
loc_0056C028:
loc_0056C02B:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056C02D:
    result = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
loc_0056C03B:
    result = (uint32_t)(((uint32_t)(Arg1) + 1) + (Arg1));
    result = 0;
    Arg2 = 0;
loc_0056C04E:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056C1B6;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056C19A;
    if (Arg1 != 1) goto loc_0056C1D1;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (condition_is_not_equal) goto loc_0056C197;
    goto loc_0056C19A;
loc_0056C08D:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58) + 0x10) + result * 8 + 0x10))) == 0) goto loc_0056C04E;
loc_0056C092:
    local_rbx = 0;
    if (Arg6 != 0) {
        local_rbx = Arg4;
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056C0F9;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056C0DD;
    if (Arg1 != 1) goto loc_0056C114;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (condition_is_not_equal) goto loc_0056C0DA;
    goto loc_0056C0DD;
loc_0056C0DA:
loc_0056C0DD:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (condition_is_not_equal) goto loc_0056C0F4;
    goto loc_0056C0F7;
loc_0056C0F4:
loc_0056C0F7:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056C0F9:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) != 0) goto loc_0056C10F;
    goto loc_0056C112;
loc_0056C10F:
loc_0056C112:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056C114:
    local_rbx = -(local_rbx);
    Arg2 = (local_rbx) >> (32);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xFC8C40) + 0x58)))) - (1));
    if (condition_is_equal) goto loc_0056C17D;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0056C161;
    if (Arg1 != 1) goto loc_0056C1D4;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (48);
    if (condition_is_not_equal) goto loc_0056C15E;
    goto loc_0056C161;
loc_0056C15E:
loc_0056C161:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (condition_is_not_equal) goto loc_0056C178;
    goto loc_0056C17B;
loc_0056C178:
loc_0056C17B:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
loc_0056C17D:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) != 0) {
        Arg3 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) + 0x4);
    }
    Arg2 = (uint32_t)((Arg2) + (Arg3));
    goto loc_0056C1D4;
loc_0056C197:
loc_0056C19A:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58)) + (24);
    if (condition_is_not_equal) goto loc_0056C1B1;
    goto loc_0056C1B4;
loc_0056C1B1:
loc_0056C1B4:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x4))) + ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg3) + 0x4)))));
loc_0056C1B6:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x56BE7C + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xFC8C40) + 0x58) != 0) goto loc_0056C1CC;
    goto loc_0056C1CF;
loc_0056C1CC:
loc_0056C1CF:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg3) + 0x4)))));
loc_0056C1D1:
loc_0056C1D4:
    Arg2 = (Arg3) >> (32);
    return Arg3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg1` | `+ 0x0 + rsi*2` | `64` | `R` |
| `Arg1` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056BE58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
