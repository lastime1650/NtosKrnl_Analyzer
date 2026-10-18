# MiMergeMemoryBlocks

- RVA: `0x007FA84C`–`0x007FAC1E` (길이 `978` bytes)
- VA: `0x00000001407FA84C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7A68`
- 디코드: `274`개 명령, `978/978` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007FA8DA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007FAB8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007FABB2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007FAC04` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [MiPerformMemoryChange](../../text/67/MiPerformMemoryChange_function_006733A8.md) at `0x006733E2`
- [MiPerformMemoryChange](../../text/67/MiPerformMemoryChange_function_006733A8.md) at `0x0067340E`

### Static image references
- `0x007FABBA` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x007FA8DA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007FAB8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007FABB2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007FAC04` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FA84C  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
007FA851  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
007FA856  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007FA85B  53                              push rbx
007FA85C  55                              push rbp
007FA85D  56                              push rsi
007FA85E  57                              push rdi
007FA85F  41 54                           push r12
007FA861  41 55                           push r13
007FA863  41 56                           push r14
007FA865  41 57                           push r15
007FA867  48 83 EC 68                     sub rsp, 0x68
007FA86B  4C 8D 6A 10                     lea r13, [rdx + 0x10]
007FA86F  45 33 F6                        xor r14d, r14d
007FA872  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
007FA876  48 8D 71 10                     lea rsi, [rcx + 0x10]
007FA87A  8B 16                           mov edx, dword ptr [rsi]
007FA87C  33 FF                           xor edi, edi
007FA87E  45 8B 65 00                     mov r12d, dword ptr [r13]
007FA882  33 DB                           xor ebx, ebx
007FA884  4D 8B C8                        mov r9, r8
007FA887  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
007FA88E  44 8B C2                        mov r8d, edx
007FA891  48 89 46 08                     mov qword ptr [rsi + 8], rax
007FA895  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007FA89A  39 9C 24 D0 00 00 00            cmp dword ptr [rsp + 0xd0], ebx
007FA8A1  74 19                           je 0x1407fa8bc
007FA8A3  41 8B 5D 00                     mov ebx, dword ptr [r13]
007FA8A7  48 8D 7A 01                     lea rdi, [rdx + 1]
007FA8AB  48 FF C3                        inc rbx
007FA8AE  48 C1 E7 04                     shl rdi, 4
007FA8B2  48 C1 E3 04                     shl rbx, 4
007FA8B6  49 03 DD                        add rbx, r13
007FA8B9  48 03 FE                        add rdi, rsi
007FA8BC  41 8B 49 10                     mov ecx, dword ptr [r9 + 0x10]
007FA8C0  42 8D 04 21                     lea eax, [rcx + r12]
007FA8C4  3B D0                           cmp edx, eax
007FA8C6  73 18                           jae 0x1407fa8e0
007FA8C8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007FA8CD  4D 8B CC                        mov r9, r12
007FA8D0  B9 1A 00 00 00                  mov ecx, 0x1a
007FA8D5  BA 00 0F 04 00                  mov edx, 0x40f00
007FA8DA  E8 81 2D D0 FF                  call 0x1404fd660
007FA8DF  CC                              int3
007FA8E0  4C 21 74 24 30                  and qword ptr [rsp + 0x30], r14
007FA8E5  4C 8D 56 10                     lea r10, [rsi + 0x10]
007FA8E9  49 8B 11                        mov rdx, qword ptr [r9]
007FA8EC  32 C0                           xor al, al
007FA8EE  45 33 DB                        xor r11d, r11d
007FA8F1  88 84 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], al
007FA8F8  45 33 FF                        xor r15d, r15d
007FA8FB  49 3B D1                        cmp rdx, r9
007FA8FE  0F 84 69 02 00 00               je 0x1407fab6d
007FA904  0F 10 42 10                     movups xmm0, xmmword ptr [rdx + 0x10]
007FA908  40 32 ED                        xor bpl, bpl
007FA90B  33 C9                           xor ecx, ecx
007FA90D  F3 0F 7F 44 24 38               movdqu xmmword ptr [rsp + 0x38], xmm0
007FA913  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
007FA918  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
007FA91D  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
007FA922  45 3B DC                        cmp r11d, r12d
007FA925  0F 83 28 01 00 00               jae 0x1407faa53
007FA92B  40 84 ED                        test bpl, bpl
007FA92E  74 05                           je 0x1407fa935
007FA930  40 32 ED                        xor bpl, bpl
007FA933  EB 2A                           jmp 0x1407fa95f
007FA935  41 8B C3                        mov eax, r11d
007FA938  48 FF C0                        inc rax
007FA93B  48 C1 E0 04                     shl rax, 4
007FA93F  49 03 C5                        add rax, r13
007FA942  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007FA947  0F 10 08                        movups xmm1, xmmword ptr [rax]
007FA94A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
007FA94E  8A 84 24 D0 00 00 00            mov al, byte ptr [rsp + 0xd0]
007FA955  0F 11 4C 24 48                  movups xmmword ptr [rsp + 0x48], xmm1
007FA95A  66 49 0F 7E CE                  movq r14, xmm1
007FA95F  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
007FA967  74 55                           je 0x1407fa9be
007FA969  4D 3B F1                        cmp r14, r9
007FA96C  0F 87 E1 00 00 00               ja 0x1407faa53
007FA972  0F 10 44 24 48                  movups xmm0, xmmword ptr [rsp + 0x48]
007FA977  F3 41 0F 7F 02                  movdqu xmmword ptr [r10], xmm0
007FA97C  48 85 FF                        test rdi, rdi
007FA97F  74 0A                           je 0x1407fa98b
007FA981  48 8B 03                        mov rax, qword ptr [rbx]
007FA984  48 89 07                        mov qword ptr [rdi], rax
007FA987  48 83 C7 08                     add rdi, 8
007FA98B  41 FF C7                        inc r15d
007FA98E  49 83 C2 10                     add r10, 0x10
007FA992  40 84 ED                        test bpl, bpl
007FA995  0F 84 81 00 00 00               je 0x1407faa1c
007FA99B  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
007FA9A0  4C 03 F1                        add r14, rcx
007FA9A3  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007FA9A8  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
007FA9AC  49 2B CE                        sub rcx, r14
007FA9AF  48 03 08                        add rcx, qword ptr [rax]
007FA9B2  8A 84 24 D0 00 00 00            mov al, byte ptr [rsp + 0xd0]
007FA9B9  E9 5F FF FF FF                  jmp 0x1407fa91d
007FA9BE  4D 3B CE                        cmp r9, r14
007FA9C1  72 AF                           jb 0x1407fa972
007FA9C3  49 8D 04 0E                     lea rax, [r14 + rcx]
007FA9C7  4C 3B C8                        cmp r9, rax
007FA9CA  73 A6                           jae 0x1407fa972
007FA9CC  49 8B C1                        mov rax, r9
007FA9CF  49 2B C6                        sub rax, r14
007FA9D2  74 0D                           je 0x1407fa9e1
007FA9D4  48 8B C8                        mov rcx, rax
007FA9D7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007FA9DC  40 B5 01                        mov bpl, 1
007FA9DF  EB 91                           jmp 0x1407fa972
007FA9E1  4C 3B C1                        cmp r8, rcx
007FA9E4  73 21                           jae 0x1407faa07
007FA9E6  49 2B C8                        sub rcx, r8
007FA9E9  C6 84 24 D0 00 00 00 01         mov byte ptr [rsp + 0xd0], 1
007FA9F1  4D 03 F0                        add r14, r8
007FA9F4  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
007FA9F9  4C 29 46 08                     sub qword ptr [rsi + 8], r8
007FA9FD  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007FAA02  E9 6B FF FF FF                  jmp 0x1407fa972
007FAA07  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007FAA0B  75 37                           jne 0x1407faa44
007FAA0D  49 2B C0                        sub rax, r8
007FAA10  C6 84 24 D0 00 00 00 01         mov byte ptr [rsp + 0xd0], 1
007FAA18  48 89 46 08                     mov qword ptr [rsi + 8], rax
007FAA1C  48 83 44 24 30 10               add qword ptr [rsp + 0x30], 0x10
007FAA22  48 8B C3                        mov rax, rbx
007FAA25  41 FF C3                        inc r11d
007FAA28  48 8D 5B 08                     lea rbx, [rbx + 8]
007FAA2C  48 85 C0                        test rax, rax
007FAA2F  48 0F 44 D8                     cmove rbx, rax
007FAA33  8A 84 24 D0 00 00 00            mov al, byte ptr [rsp + 0xd0]
007FAA3A  84 C0                           test al, al
007FAA3C  0F 84 E0 FE FF FF               je 0x1407fa922
007FAA42  EB 13                           jmp 0x1407faa57
007FAA44  48 2B C1                        sub rax, rcx
007FAA47  4C 03 C9                        add r9, rcx
007FAA4A  48 89 46 08                     mov qword ptr [rsi + 8], rax
007FAA4E  4C 2B C1                        sub r8, rcx
007FAA51  EB C9                           jmp 0x1407faa1c
007FAA53  84 C0                           test al, al
007FAA55  74 0E                           je 0x1407faa65
007FAA57  32 C0                           xor al, al
007FAA59  88 84 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], al
007FAA60  E9 F7 00 00 00                  jmp 0x1407fab5c
007FAA65  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
007FAA6D  0F 84 E9 00 00 00               je 0x1407fab5c
007FAA73  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
007FAA77  33 C9                           xor ecx, ecx
007FAA79  48 01 46 08                     add qword ptr [rsi + 8], rax
007FAA7D  45 33 C0                        xor r8d, r8d
007FAA80  48 8D 46 10                     lea rax, [rsi + 0x10]
007FAA84  4C 3B D0                        cmp r10, rax
007FAA87  74 28                           je 0x1407faab1
007FAA89  49 8D 4A F0                     lea rcx, [r10 - 0x10]
007FAA8D  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
007FAA91  48 03 01                        add rax, qword ptr [rcx]
007FAA94  48 3B 42 10                     cmp rax, qword ptr [rdx + 0x10]
007FAA98  75 15                           jne 0x1407faaaf
007FAA9A  48 85 DB                        test rbx, rbx
007FAA9D  74 12                           je 0x1407faab1
007FAA9F  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
007FAAA2  39 47 F8                        cmp dword ptr [rdi - 8], eax
007FAAA5  75 08                           jne 0x1407faaaf
007FAAA7  8A 42 24                        mov al, byte ptr [rdx + 0x24]
007FAAAA  38 47 FC                        cmp byte ptr [rdi - 4], al
007FAAAD  74 02                           je 0x1407faab1
007FAAAF  33 C9                           xor ecx, ecx
007FAAB1  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
007FAAB6  45 3B DC                        cmp r11d, r12d
007FAAB9  74 27                           je 0x1407faae2
007FAABB  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
007FAABF  4D 8B C1                        mov r8, r9
007FAAC2  48 03 42 18                     add rax, qword ptr [rdx + 0x18]
007FAAC6  49 3B 01                        cmp rax, qword ptr [r9]
007FAAC9  75 14                           jne 0x1407faadf
007FAACB  48 85 DB                        test rbx, rbx
007FAACE  74 12                           je 0x1407faae2
007FAAD0  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
007FAAD3  39 03                           cmp dword ptr [rbx], eax
007FAAD5  75 08                           jne 0x1407faadf
007FAAD7  8A 42 24                        mov al, byte ptr [rdx + 0x24]
007FAADA  38 43 04                        cmp byte ptr [rbx + 4], al
007FAADD  74 03                           je 0x1407faae2
007FAADF  45 33 C0                        xor r8d, r8d
007FAAE2  48 85 C9                        test rcx, rcx
007FAAE5  74 31                           je 0x1407fab18
007FAAE7  4D 85 C0                        test r8, r8
007FAAEA  75 0E                           jne 0x1407faafa
007FAAEC  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
007FAAF0  48 03 42 18                     add rax, qword ptr [rdx + 0x18]
007FAAF4  48 89 41 08                     mov qword ptr [rcx + 8], rax
007FAAF8  EB 5B                           jmp 0x1407fab55
007FAAFA  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
007FAAFE  41 FF C3                        inc r11d
007FAB01  48 03 41 08                     add rax, qword ptr [rcx + 8]
007FAB05  48 03 42 18                     add rax, qword ptr [rdx + 0x18]
007FAB09  48 89 41 08                     mov qword ptr [rcx + 8], rax
007FAB0D  48 85 DB                        test rbx, rbx
007FAB10  74 43                           je 0x1407fab55
007FAB12  48 83 C3 08                     add rbx, 8
007FAB16  EB 3D                           jmp 0x1407fab55
007FAB18  0F 10 42 10                     movups xmm0, xmmword ptr [rdx + 0x10]
007FAB1C  F3 41 0F 7F 02                  movdqu xmmword ptr [r10], xmm0
007FAB21  4D 85 C0                        test r8, r8
007FAB24  74 14                           je 0x1407fab3a
007FAB26  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
007FAB2A  41 FF C3                        inc r11d
007FAB2D  49 01 42 08                     add qword ptr [r10 + 8], rax
007FAB31  49 83 C1 10                     add r9, 0x10
007FAB35  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
007FAB3A  48 85 FF                        test rdi, rdi
007FAB3D  74 0F                           je 0x1407fab4e
007FAB3F  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
007FAB42  89 07                           mov dword ptr [rdi], eax
007FAB44  8A 42 24                        mov al, byte ptr [rdx + 0x24]
007FAB47  88 47 04                        mov byte ptr [rdi + 4], al
007FAB4A  48 83 C7 08                     add rdi, 8
007FAB4E  49 83 C2 10                     add r10, 0x10
007FAB52  41 FF C7                        inc r15d
007FAB55  8A 84 24 D0 00 00 00            mov al, byte ptr [rsp + 0xd0]
007FAB5C  48 8B 12                        mov rdx, qword ptr [rdx]
007FAB5F  48 3B 94 24 C0 00 00 00         cmp rdx, qword ptr [rsp + 0xc0]
007FAB67  0F 85 97 FD FF FF               jne 0x1407fa904
007FAB6D  45 2B E3                        sub r12d, r11d
007FAB70  74 48                           je 0x1407fabba
007FAB72  49 8D 53 01                     lea rdx, [r11 + 1]
007FAB76  45 8B C4                        mov r8d, r12d
007FAB79  48 C1 E2 04                     shl rdx, 4
007FAB7D  49 8B CA                        mov rcx, r10
007FAB80  49 03 D5                        add rdx, r13
007FAB83  49 C1 E0 04                     shl r8, 4
007FAB87  45 8B F3                        mov r14d, r11d
007FAB8A  E8 B1 BC EC FF                  call 0x1406c6840
007FAB8F  48 85 FF                        test rdi, rdi
007FAB92  74 23                           je 0x1407fabb7
007FAB94  41 8B 45 00                     mov eax, dword ptr [r13]
007FAB98  4E 8D 04 E5 00 00 00 00         lea r8, [r12*8]
007FABA0  48 8B CF                        mov rcx, rdi
007FABA3  49 8D 14 46                     lea rdx, [r14 + rax*2]
007FABA7  48 8D 14 D5 10 00 00 00         lea rdx, [rdx*8 + 0x10]
007FABAF  49 03 D5                        add rdx, r13
007FABB2  E8 89 BC EC FF                  call 0x1406c6840
007FABB7  45 03 FC                        add r15d, r12d
007FABBA  48 8D 0D 3F E1 63 00            lea rcx, [rip + 0x63e13f]
007FABC1  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
007FABC9  48 C7 40 08 01 00 00 00         mov qword ptr [rax + 8], 1
007FABD1  48 89 08                        mov qword ptr [rax], rcx
007FABD4  44 3B BC 24 B8 00 00 00         cmp r15d, dword ptr [rsp + 0xb8]
007FABDC  74 2B                           je 0x1407fac09
007FABDE  48 85 DB                        test rbx, rbx
007FABE1  74 26                           je 0x1407fac09
007FABE3  8B 16                           mov edx, dword ptr [rsi]
007FABE5  4E 8D 04 FD 00 00 00 00         lea r8, [r15*8]
007FABED  48 FF C2                        inc rdx
007FABF0  41 8B CF                        mov ecx, r15d
007FABF3  48 C1 E2 04                     shl rdx, 4
007FABF7  48 03 D6                        add rdx, rsi
007FABFA  48 FF C1                        inc rcx
007FABFD  48 C1 E1 04                     shl rcx, 4
007FAC01  48 03 CE                        add rcx, rsi
007FAC04  E8 37 BC EC FF                  call 0x1406c6840
007FAC09  44 89 3E                        mov dword ptr [rsi], r15d
007FAC0C  48 83 C4 68                     add rsp, 0x68
007FAC10  41 5F                           pop r15
007FAC12  41 5E                           pop r14
007FAC14  41 5D                           pop r13
007FAC16  41 5C                           pop r12
007FAC18  5F                              pop rdi
007FAC19  5E                              pop rsi
007FAC1A  5D                              pop rbp
007FAC1B  5B                              pop rbx
007FAC1C  C3                              ret
007FAC1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMergeMemoryBlocks(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5)
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
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    v_r14 = 0;
    v_rdi = 0;
    v_rbx = 0;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(a1 + 16 + 8) = *(unsigned __int64 *)(a2 + 16 + 8);
    v_stack_m60 = 0;
    if (a5 != 0) {
        v_rbx = *(unsigned int *)(a2 + 16);
        v_rdi = (unsigned int)(*(unsigned int *)(a1 + 16)) + 1;
        v_rbx = (v_rbx) + 1;
        v_rdi = (v_rdi) << (4);
        v_rbx = (v_rbx) << (4);
        v_rbx = (v_rbx) + (a2 + 16);
        v_rdi = (v_rdi) + (a1 + 16);
    }
    result = (unsigned int)(*(unsigned int *)(a3 + 16)) + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16)) + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1))) {
        v_stack_m88 = (unsigned int)(*(unsigned int *)(a3 + 16));
        a4 = (unsigned int)(*(unsigned int *)(a2 + 16));
        a1 = 26;
        a2 = 0x40F00ULL;
        result = KeBugCheckEx(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))), a4);
    }
    result = 0;
    v_r11 = 0;
    v_stack_p28 = 0;
    v_r15 = 0;
    if ((*(unsigned __int64 *)(a4)) == a4) goto loc_007FAB6D;
loc_007FA904:
    v_rbp = 0;
    a1 = 0;
    v_stack_m70 = v_xmm0;
loc_007FA91D:
    v_stack_m58 = 0;
loc_007FA922:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_007FAA53;
    if (0 == 0) goto loc_007FA935;
    v_rbp = 0;
    goto loc_007FA95F;
loc_007FA935:
    result = (0) + 1;
    result = (result) << (4);
    result = (result) + (a2 + 16);
    v_stack_m78 = result;
    v_stack_m60 = v_xmm1;
loc_007FA95F:
    if (v_stack_p20 == 0) goto loc_007FA9BE;
    if (0 > v_stack_m70) goto loc_007FAA53;
loc_007FA972:
    *(unsigned __int64 *)(a1 + 16 + 16) = v_xmm0;
    result = a5;
    if (v_rdi != 0) {
        result = *(unsigned __int64 *)(v_rbx);
        *(unsigned __int64 *)(v_rdi) = result;
        v_rdi = (v_rdi) + (8);
    }
    v_r15 = (unsigned int)((v_r15) + 1);
    v_r10 = (a1 + 16 + 16) + (16);
    if (0 == 0) goto loc_007FAA1C;
    v_r14 = (v_r14) + (*(unsigned __int64 *)(result + 8));
    v_stack_m60 = v_r14;
    a1 = (*(unsigned __int64 *)(v_stack_m78 + 8)) - (v_r14);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m78));
    goto loc_007FA91D;
loc_007FA9BE:
    if (v_stack_m70 < v_r14) goto loc_007FA972;
    if (v_stack_m70 >= (v_r14 + a1 * 1)) goto loc_007FA972;
    result = (v_stack_m70) - (v_r14);
    if (condition_is_equal) goto loc_007FA9E1;
    v_stack_m58 = result;
    goto loc_007FA972;
loc_007FA9E1:
    if (v_stack_m68 >= result) goto loc_007FAA07;
    a1 = (result) - (v_stack_m68);
    v_stack_p28 = 1;
    v_r14 = (v_r14) + (v_stack_m68);
    v_stack_m58 = a1;
    v_stack_m60 = v_r14;
    goto loc_007FA972;
loc_007FAA07:
    if (condition_is_not_equal) goto loc_007FAA44;
    result = (*(unsigned __int64 *)(a1 + 16 + 8)) - (v_stack_m68);
    v_stack_p28 = 1;
    *(unsigned __int64 *)(a1 + 16 + 8) = result;
loc_007FAA1C:
    v_r11 = (unsigned int)((v_r11) + 1);
    v_rbx = v_rbx + 8;
    if (v_rbx == 0) { v_rbx = v_rbx; }
    if (a5 == 0) goto loc_007FA922;
    goto loc_007FAA57;
loc_007FAA44:
    result = (a5) - (a1);
    a4 = (v_stack_m70) + (a1);
    *(unsigned __int64 *)(a1 + 16 + 8) = result;
    a3 = (v_stack_m68) - (a1);
    goto loc_007FAA1C;
loc_007FAA53:
    if ((unsigned __int8)(result) == 0) goto loc_007FAA65;
loc_007FAA57:
    result = 0;
    v_stack_p28 = 0;
    goto loc_007FAB5C;
loc_007FAA65:
    if (v_stack_p20 == 0) goto loc_007FAB5C;
    a1 = 0;
    a3 = 0;
    if (v_r10 == (a1 + 16 + 16)) goto loc_007FAAB1;
    result = (*(unsigned __int64 *)(v_r10 - 16 + 8)) + (*(unsigned __int64 *)(v_r10 - 16));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 16))) goto loc_007FAAAF;
    if (v_rbx == 0) goto loc_007FAAB1;
    if ((*(unsigned int *)(v_rdi - 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 32))))) goto loc_007FAAAF;
    if ((*(unsigned __int8 *)(v_rdi - 4)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4) + 36)))) {
        a1 = 0;
    }
    if (((unsigned int)(v_r11)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_007FAAE2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 16)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24));
    if (result != (*(unsigned __int64 *)(v_stack_m78))) goto loc_007FAADF;
    if (v_rbx == 0) goto loc_007FAAE2;
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 32))))) goto loc_007FAADF;
    if ((*(unsigned __int8 *)(v_rbx + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4) + 36)))) {
        a3 = 0;
    }
    if (0 == 0) goto loc_007FAB18;
    if (0 != 0) goto loc_007FAAFA;
    result = (*(unsigned __int64 *)(a1 + 8)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24));
    *(unsigned __int64 *)(a1 + 8) = result;
    goto loc_007FAB55;
loc_007FAAFA:
    v_r11 = (unsigned int)((v_r11) + 1);
    result = (*(unsigned __int64 *)(a3 + 8)) + (*(unsigned __int64 *)(a1 + 8));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24));
    *(unsigned __int64 *)(a1 + 8) = result;
    if (v_rbx == 0) goto loc_007FAB55;
    v_rbx = (v_rbx) + (8);
    goto loc_007FAB55;
loc_007FAB18:
    *(unsigned __int64 *)(v_r10) = v_xmm0;
    if (0 != 0) {
        result = *(unsigned __int64 *)(a3 + 8);
        v_r11 = (unsigned int)((v_r11) + 1);
        a4 = (v_stack_m78) + (16);
        v_stack_m78 = a4;
    }
    if (v_rdi != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a4) + 32);
        *(unsigned int *)(v_rdi) = (unsigned int)(result);
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a4) + 36);
        *(unsigned __int8 *)(v_rdi + 4) = (unsigned __int8)(result);
        v_rdi = (v_rdi) + (8);
    }
    v_r10 = (v_r10) + (16);
    v_r15 = (unsigned int)((v_r15) + 1);
loc_007FAB55:
loc_007FAB5C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4))) != v_stack_p18) goto loc_007FA904;
loc_007FAB6D:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) - ((unsigned int)(v_r11)));
    if (condition_is_equal) goto loc_007FABBA;
    a2 = (v_r11 + 1) << (4);
    a2 = (a2) + (a2 + 16);
    a3 = ((unsigned int)((unsigned int)(v_r12))) << (4);
    result = memcpy(v_r10, a2, a3, a4);
    if (v_rdi != 0) {
        result = *(unsigned int *)(a2 + 16);
        a3 = v_r12 * 8;
        a1 = v_rdi;
        a2 = (unsigned int)((unsigned int)(v_r11)) + result * 2;
        a2 = a2 * 8 + 16;
        a2 = (a2) + (a2 + 16);
        result = memcpy(a1, a2, a3, a4);
    }
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_r12)));
loc_007FABBA:
    *(unsigned __int64 *)(v_stack_p8 + 8) = 1;
    *(unsigned __int64 *)(v_stack_p8) = v_rip + 6545727;
    if (((unsigned int)(v_r15)) == v_stack_p10) goto loc_007FAC09;
    result = v_stack_p8;
    if (v_rbx != 0) {
        a2 = *(unsigned int *)(a1 + 16);
        a3 = v_r15 * 8;
        a2 = (a2) + 1;
        a1 = (unsigned int)(v_r15);
        a2 = (a2) << (4);
        a2 = (a2) + (a1 + 16);
        a1 = (a1) + 1;
        a1 = (a1) << (4);
        a1 = (a1) + (a1 + 16);
        result = memcpy(a1, a2, a3, a4);
    }
    *(unsigned int *)(a1 + 16) = (unsigned int)(v_r15);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMergeMemoryBlocks(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    local_r14 = 0;
    local_rdi = 0;
    local_rbx = 0;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(arg1 + 0x10 + 0x8) = *(uint64_t *)(arg2 + 0x10 + 0x8);
    v_stack_m60 = 0;
    if (Arg5 != 0) {
        local_rbx = *(uint32_t *)(arg2 + 0x10);
        local_rdi = (uint32_t)(*(uint32_t *)(arg1 + 0x10)) + 1;
        local_rbx = (local_rbx) + 1;
        local_rdi = (local_rdi) << (4);
        local_rbx = (local_rbx) << (4);
        local_rbx = (local_rbx) + (Arg2 + 16);
        local_rdi = (local_rdi) + (Arg1 + 16);
    }
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x10)) + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10)) + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1))) {
        v_stack_m88 = (uint32_t)(*(uint32_t *)(arg3 + 0x10));
        Arg4 = (uint32_t)(*(uint32_t *)(arg2 + 0x10));
        Arg1 = 26;
        Arg2 = 0x40F00ULL;
        result = KeBugCheckEx(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))), Arg4);
    }
    result = 0;
    local_r11 = 0;
    v_stack_p28 = 0;
    local_r15 = 0;
    if ((*(uint64_t *)(Arg4)) == Arg4) goto loc_007FAB6D;
loc_007FA904:
    local_rbp = 0;
    Arg1 = 0;
    v_stack_m70 = v_xmm0;
loc_007FA91D:
    v_stack_m58 = 0;
loc_007FA922:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_007FAA53;
    if (0 == 0) goto loc_007FA935;
    local_rbp = 0;
    goto loc_007FA95F;
loc_007FA935:
    result = (0) + 1;
    result = (result) << (4);
    result = (result) + (Arg2 + 16);
    v_stack_m78 = result;
    v_stack_m60 = v_xmm1;
loc_007FA95F:
    if (v_stack_p20 == 0) goto loc_007FA9BE;
    if (0 > v_stack_m70) goto loc_007FAA53;
loc_007FA972:
    *(uint64_t *)(arg1 + 0x10 + 0x10) = v_xmm0;
    result = Arg5;
    if (local_rdi != 0) {
        result = *(uint64_t *)(local_rbx);
        *(uint64_t *)(local_rdi) = result;
        local_rdi = (local_rdi) + (8);
    }
    local_r15 = (uint32_t)((local_r15) + 1);
    local_r10 = (Arg1 + 16 + 16) + (16);
    if (0 == 0) goto loc_007FAA1C;
    local_r14 = (local_r14) + (*(uint64_t *)(result + 0x8));
    v_stack_m60 = local_r14;
    Arg1 = (*(uint64_t *)(v_stack_m78 + 0x8)) - (local_r14);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m78));
    goto loc_007FA91D;
loc_007FA9BE:
    if (v_stack_m70 < local_r14) goto loc_007FA972;
    if (v_stack_m70 >= (local_r14 + Arg1 * 1)) goto loc_007FA972;
    result = (v_stack_m70) - (local_r14);
    if (condition_is_equal) goto loc_007FA9E1;
    v_stack_m58 = result;
    goto loc_007FA972;
loc_007FA9E1:
    if (v_stack_m68 >= result) goto loc_007FAA07;
    Arg1 = (result) - (v_stack_m68);
    v_stack_p28 = 1;
    local_r14 = (local_r14) + (v_stack_m68);
    v_stack_m58 = Arg1;
    v_stack_m60 = local_r14;
    goto loc_007FA972;
loc_007FAA07:
    if (condition_is_not_equal) goto loc_007FAA44;
    result = (*(uint64_t *)(arg1 + 0x10 + 0x8)) - (v_stack_m68);
    v_stack_p28 = 1;
    *(uint64_t *)(arg1 + 0x10 + 0x8) = result;
loc_007FAA1C:
    local_r11 = (uint32_t)((local_r11) + 1);
    local_rbx = local_rbx + 8;
    if (local_rbx == 0) { local_rbx = local_rbx; }
    if (Arg5 == 0) goto loc_007FA922;
    goto loc_007FAA57;
loc_007FAA44:
    result = (Arg5) - (Arg1);
    Arg4 = (v_stack_m70) + (Arg1);
    *(uint64_t *)(arg1 + 0x10 + 0x8) = result;
    Arg3 = (v_stack_m68) - (Arg1);
    goto loc_007FAA1C;
loc_007FAA53:
    if ((uint8_t)(result) == 0) goto loc_007FAA65;
loc_007FAA57:
    result = 0;
    v_stack_p28 = 0;
    goto loc_007FAB5C;
loc_007FAA65:
    if (v_stack_p20 == 0) goto loc_007FAB5C;
    Arg1 = 0;
    Arg3 = 0;
    if (local_r10 == (Arg1 + 16 + 16)) goto loc_007FAAB1;
    result = (*(uint64_t *)(local_r10 - 0x10 + 0x8)) + (*(uint64_t *)(local_r10 - 0x10));
    if (result != (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x10))) goto loc_007FAAAF;
    if (local_rbx == 0) goto loc_007FAAB1;
    if ((*(uint32_t *)(local_rdi - 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4) + 0x20))))) goto loc_007FAAAF;
    if ((*(uint8_t *)(local_rdi - 0x4)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg4) + 0x24)))) {
        Arg1 = 0;
    }
    if (((uint32_t)(local_r11)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_007FAAE2;
    result = (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x10)) + (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x18));
    if (result != (*(uint64_t *)(v_stack_m78))) goto loc_007FAADF;
    if (local_rbx == 0) goto loc_007FAAE2;
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4) + 0x20))))) goto loc_007FAADF;
    if ((*(uint8_t *)(local_rbx + 0x4)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg4) + 0x24)))) {
        Arg3 = 0;
    }
    if (0 == 0) goto loc_007FAB18;
    if (0 != 0) goto loc_007FAAFA;
    result = (*(uint64_t *)(arg1 + 0x8)) + (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x18));
    *(uint64_t *)(arg1 + 0x8) = result;
    goto loc_007FAB55;
loc_007FAAFA:
    local_r11 = (uint32_t)((local_r11) + 1);
    result = (*(uint64_t *)(arg3 + 0x8)) + (*(uint64_t *)(arg1 + 0x8));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x18));
    *(uint64_t *)(arg1 + 0x8) = result;
    if (local_rbx == 0) goto loc_007FAB55;
    local_rbx = (local_rbx) + (8);
    goto loc_007FAB55;
loc_007FAB18:
    *(uint64_t *)(local_r10) = v_xmm0;
    if (0 != 0) {
        result = *(uint64_t *)(arg3 + 0x8);
        local_r11 = (uint32_t)((local_r11) + 1);
        Arg4 = (v_stack_m78) + (16);
        v_stack_m78 = Arg4;
    }
    if (local_rdi != 0) {
        result = *(uint32_t *)(*(uint64_t *)(Arg4) + 0x20);
        *(uint32_t *)(local_rdi) = (uint32_t)(result);
        result = *(uint8_t *)(*(uint64_t *)(Arg4) + 0x24);
        *(uint8_t *)(local_rdi + 0x4) = (uint8_t)(result);
        local_rdi = (local_rdi) + (8);
    }
    local_r10 = (local_r10) + (16);
    local_r15 = (uint32_t)((local_r15) + 1);
loc_007FAB55:
loc_007FAB5C:
    if ((*(uint64_t *)(*(uint64_t *)(Arg4))) != v_stack_p18) goto loc_007FA904;
loc_007FAB6D:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) - ((uint32_t)(local_r11)));
    if (condition_is_equal) goto loc_007FABBA;
    Arg2 = (local_r11 + 1) << (4);
    Arg2 = (Arg2) + (Arg2 + 16);
    Arg3 = ((uint32_t)((uint32_t)(local_r12))) << (4);
    result = memcpy(local_r10, Arg2, Arg3, Arg4);
    if (local_rdi != 0) {
        result = *(uint32_t *)(arg2 + 0x10);
        Arg3 = local_r12 * 8;
        Arg1 = local_rdi;
        Arg2 = (uint32_t)((uint32_t)(local_r11)) + result * 2;
        Arg2 = Arg2 * 8 + 16;
        Arg2 = (Arg2) + (Arg2 + 16);
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_r12)));
loc_007FABBA:
    *(uint64_t *)(v_stack_p8 + 0x8) = 1;
    *(uint64_t *)(v_stack_p8) = v_rip + 6545727;
    if (((uint32_t)(local_r15)) == v_stack_p10) goto loc_007FAC09;
    result = v_stack_p8;
    if (local_rbx != 0) {
        Arg2 = *(uint32_t *)(arg1 + 0x10);
        Arg3 = local_r15 * 8;
        Arg2 = (Arg2) + 1;
        Arg1 = (uint32_t)(local_r15);
        Arg2 = (Arg2) << (4);
        Arg2 = (Arg2) + (Arg1 + 16);
        Arg1 = (Arg1) + 1;
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) + (Arg1 + 16);
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)(local_r15);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FA84C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
