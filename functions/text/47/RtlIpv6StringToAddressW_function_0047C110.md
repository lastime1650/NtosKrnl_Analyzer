# RtlIpv6StringToAddressW

- RVA: `0x0047C110`–`0x0047C53C` (길이 `1,068` bytes)
- VA: `0x000000014047C110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AD7AC`
- 디코드: `266`개 명령, `1,068/1,068` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0047C19B` → [iswctype](../50/iswctype_function_00502900.md) (function, `0x00502900`)
- `0x0047C1B0` → [iswctype](../50/iswctype_function_00502900.md) (function, `0x00502900`)
- `0x0047C209` → [wcstol](../50/wcstol_function_00502434.md) (function, `0x00502434`)
- `0x0047C250` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0047C262` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0047C2B6` → [iswctype](../50/iswctype_function_00502900.md) (function, `0x00502900`)
- `0x0047C2EF` → [iswctype](../50/iswctype_function_00502900.md) (function, `0x00502900`)
- `0x0047C387` → [wcstol](../50/wcstol_function_00502434.md) (function, `0x00502434`)
- `0x0047C48E` → [wcstol](../50/wcstol_function_00502434.md) (function, `0x00502434`)
- `0x0047C518` → [wcstol](../50/wcstol_function_00502434.md) (function, `0x00502434`)

### Direct callers
- [RtlIpv6StringToAddressExW](RtlIpv6StringToAddressExW_function_0047BEE0.md) at `0x0047BF3F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0047C17C` → [sub_006F4A5C + 0x11](../6F/Unknown_function_006F4A5C.md) (`tail-transfer`)
  - `0x0047C459` → [sub_006F4A5C](../6F/Unknown_function_006F4A5C.md) (`tail-transfer`)
  - `0x0047C468` → [sub_006F4A5C](../6F/Unknown_function_006F4A5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0047C110  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0047C115  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0047C11A  55                              push rbp
0047C11B  56                              push rsi
0047C11C  57                              push rdi
0047C11D  41 54                           push r12
0047C11F  41 55                           push r13
0047C121  41 56                           push r14
0047C123  41 57                           push r15
0047C125  48 83 EC 30                     sub rsp, 0x30
0047C129  33 C0                           xor eax, eax
0047C12B  4D 8B E8                        mov r13, r8
0047C12E  44 8A D8                        mov r11b, al
0047C131  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0047C136  48 8B F1                        mov rsi, rcx
0047C139  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0047C13D  44 8B E0                        mov r12d, eax
0047C140  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
0047C145  8D 48 01                        lea ecx, [rax + 1]
0047C148  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0047C14F  44 8B C8                        mov r9d, eax
0047C152  44 8A C0                        mov r8b, al
0047C155  8B F8                           mov edi, eax
0047C157  44 8B F0                        mov r14d, eax
0047C15A  44 8B F8                        mov r15d, eax
0047C15D  8B E8                           mov ebp, eax
0047C15F  44 8B D0                        mov r10d, eax
0047C162  0F B7 1E                        movzx ebx, word ptr [rsi]
0047C165  66 85 DB                        test bx, bx
0047C168  74 58                           je 0x14047c1c2
0047C16A  33 C0                           xor eax, eax
0047C16C  41 8B CC                        mov ecx, r12d
0047C16F  45 85 E4                        test r12d, r12d
0047C172  0F 85 25 01 00 00               jne 0x14047c29d
0047C178  66 83 FB 3A                     cmp bx, 0x3a
0047C17C  0F 84 EB 88 27 00               je 0x1406f4a6d
0047C182  83 FF 07                        cmp edi, 7
0047C185  0F 87 55 03 00 00               ja 0x14047c4e0
0047C18B  B8 80 00 00 00                  mov eax, 0x80
0047C190  66 3B D8                        cmp bx, ax
0047C193  73 28                           jae 0x14047c1bd
0047C195  8D 50 84                        lea edx, [rax - 0x7c]
0047C198  0F B7 CB                        movzx ecx, bx
0047C19B  E8 60 67 08 00                  call 0x140502900
0047C1A0  85 C0                           test eax, eax
0047C1A2  0F 85 14 02 00 00               jne 0x14047c3bc
0047C1A8  BA 80 00 00 00                  mov edx, 0x80
0047C1AD  0F B7 CB                        movzx ecx, bx
0047C1B0  E8 4B 67 08 00                  call 0x140502900
0047C1B5  85 C0                           test eax, eax
0047C1B7  0F 85 1E 02 00 00               jne 0x14047c3db
0047C1BD  B9 01 00 00 00                  mov ecx, 1
0047C1C2  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0047C1C7  48 89 30                        mov qword ptr [rax], rsi
0047C1CA  33 F6                           xor esi, esi
0047C1CC  45 85 F6                        test r14d, r14d
0047C1CF  0F 85 A0 00 00 00               jne 0x14047c275
0047C1D5  85 ED                           test ebp, ebp
0047C1D7  75 09                           jne 0x14047c1e2
0047C1D9  83 FF 07                        cmp edi, 7
0047C1DC  0F 85 9D 00 00 00               jne 0x14047c27f
0047C1E2  44 3B E1                        cmp r12d, ecx
0047C1E5  0F 85 D9 02 00 00               jne 0x14047c4c4
0047C1EB  45 85 F6                        test r14d, r14d
0047C1EE  0F 85 0F 03 00 00               jne 0x14047c503
0047C1F4  41 83 FF 04                     cmp r15d, 4
0047C1F8  0F 87 81 00 00 00               ja 0x14047c27f
0047C1FE  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0047C203  45 8D 46 10                     lea r8d, [r14 + 0x10]
0047C207  33 D2                           xor edx, edx
0047C209  E8 26 62 08 00                  call 0x140502434
0047C20E  8B 8C 24 88 00 00 00            mov ecx, dword ptr [rsp + 0x88]
0047C215  66 C1 C8 08                     ror ax, 8
0047C219  66 41 89 44 4D 00               mov word ptr [r13 + rcx*2], ax
0047C21F  85 ED                           test ebp, ebp
0047C221  74 44                           je 0x14047c267
0047C223  8B C5                           mov eax, ebp
0047C225  44 8B C7                        mov r8d, edi
0047C228  44 2B C5                        sub r8d, ebp
0047C22B  BE 08 00 00 00                  mov esi, 8
0047C230  2B EF                           sub ebp, edi
0047C232  4D 03 C0                        add r8, r8
0047C235  03 EE                           add ebp, esi
0047C237  48 8D 1C 45 00 00 00 00         lea rbx, [rax*2]
0047C23F  49 03 DD                        add rbx, r13
0047C242  48 8B D3                        mov rdx, rbx
0047C245  48 8D 0C 6D 00 00 00 00         lea rcx, [rbp*2]
0047C24D  49 03 CD                        add rcx, r13
0047C250  E8 EB A5 24 00                  call 0x1406c6840
0047C255  2B F7                           sub esi, edi
0047C257  33 D2                           xor edx, edx
0047C259  44 8B C6                        mov r8d, esi
0047C25C  48 8B CB                        mov rcx, rbx
0047C25F  4D 03 C0                        add r8, r8
0047C262  E8 D9 A9 24 00                  call 0x1406c6c40
0047C267  33 C0                           xor eax, eax
0047C269  EB 19                           jmp 0x14047c284
0047C26B  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0047C270  48 89 30                        mov qword ptr [rax], rsi
0047C273  33 F6                           xor esi, esi
0047C275  41 83 FE 03                     cmp r14d, 3
0047C279  0F 84 78 02 00 00               je 0x14047c4f7
0047C27F  B8 0D 00 00 C0                  mov eax, 0xc000000d
0047C284  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0047C28C  48 83 C4 30                     add rsp, 0x30
0047C290  41 5F                           pop r15
0047C292  41 5E                           pop r14
0047C294  41 5D                           pop r13
0047C296  41 5C                           pop r12
0047C298  5F                              pop rdi
0047C299  5E                              pop rsi
0047C29A  5D                              pop rbp
0047C29B  C3                              ret
0047C29C  CC                              int3
0047C29D  83 E9 01                        sub ecx, 1
0047C2A0  0F 85 4B 01 00 00               jne 0x14047c3f1
0047C2A6  B9 80 00 00 00                  mov ecx, 0x80
0047C2AB  66 3B D9                        cmp bx, cx
0047C2AE  73 7B                           jae 0x14047c32b
0047C2B0  8D 51 84                        lea edx, [rcx - 0x7c]
0047C2B3  0F B7 CB                        movzx ecx, bx
0047C2B6  E8 45 66 08 00                  call 0x140502900
0047C2BB  85 C0                           test eax, eax
0047C2BD  74 28                           je 0x14047c2e7
0047C2BF  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0047C2C4  B9 01 00 00 00                  mov ecx, 1
0047C2C9  44 03 F9                        add r15d, ecx
0047C2CC  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0047C2D1  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
0047C2D9  44 8B 5C 24 20                  mov r11d, dword ptr [rsp + 0x20]
0047C2DE  48 83 C6 02                     add rsi, 2
0047C2E2  E9 7B FE FF FF                  jmp 0x14047c162
0047C2E7  BA 80 00 00 00                  mov edx, 0x80
0047C2EC  0F B7 CB                        movzx ecx, bx
0047C2EF  E8 0C 66 08 00                  call 0x140502900
0047C2F4  85 C0                           test eax, eax
0047C2F6  74 1A                           je 0x14047c312
0047C2F8  B9 01 00 00 00                  mov ecx, 1
0047C2FD  44 03 F9                        add r15d, ecx
0047C300  45 85 F6                        test r14d, r14d
0047C303  0F 85 62 FF FF FF               jne 0x14047c26b
0047C309  44 8A C1                        mov r8b, cl
0047C30C  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
0047C310  EB BA                           jmp 0x14047c2cc
0047C312  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0047C317  33 C0                           xor eax, eax
0047C319  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0047C31E  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
0047C326  44 8B 5C 24 20                  mov r11d, dword ptr [rsp + 0x20]
0047C32B  66 83 FB 3A                     cmp bx, 0x3a
0047C32F  0F 85 04 01 00 00               jne 0x14047c439
0047C335  45 85 F6                        test r14d, r14d
0047C338  0F 85 2D FF FF FF               jne 0x14047c26b
0047C33E  83 FF 06                        cmp edi, 6
0047C341  0F 87 26 01 00 00               ja 0x14047c46d
0047C347  83 FF 07                        cmp edi, 7
0047C34A  0F 87 6D FE FF FF               ja 0x14047c1bd
0047C350  66 83 7E 02 3A                  cmp word ptr [rsi + 2], 0x3a
0047C355  0F 84 C1 00 00 00               je 0x14047c41c
0047C35B  FF C7                           inc edi
0047C35D  33 C0                           xor eax, eax
0047C35F  44 8B E0                        mov r12d, eax
0047C362  4D 85 C9                        test r9, r9
0047C365  0F 84 A7 00 00 00               je 0x14047c412
0047C36B  45 85 F6                        test r14d, r14d
0047C36E  0F 85 07 01 00 00               jne 0x14047c47b
0047C374  41 83 FF 04                     cmp r15d, 4
0047C378  0F 87 01 FF FF FF               ja 0x14047c27f
0047C37E  33 D2                           xor edx, edx
0047C380  45 8D 46 10                     lea r8d, [r14 + 0x10]
0047C384  49 8B C9                        mov rcx, r9
0047C387  E8 A8 60 08 00                  call 0x140502434
0047C38C  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
0047C394  41 8D 4E 01                     lea ecx, [r14 + 1]
0047C398  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0047C39D  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0047C3A2  66 C1 C8 08                     ror ax, 8
0047C3A6  66 43 89 44 55 00               mov word ptr [r13 + r10*2], ax
0047C3AC  44 03 D1                        add r10d, ecx
0047C3AF  44 89 94 24 88 00 00 00         mov dword ptr [rsp + 0x88], r10d
0047C3B7  E9 1D FF FF FF                  jmp 0x14047c2d9
0047C3BC  33 C0                           xor eax, eax
0047C3BE  44 8A C0                        mov r8b, al
0047C3C1  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0047C3C5  8D 48 01                        lea ecx, [rax + 1]
0047C3C8  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0047C3CD  4C 8B CE                        mov r9, rsi
0047C3D0  44 8B E1                        mov r12d, ecx
0047C3D3  44 8B F9                        mov r15d, ecx
0047C3D6  E9 F6 FE FF FF                  jmp 0x14047c2d1
0047C3DB  45 85 F6                        test r14d, r14d
0047C3DE  0F 85 87 FE FF FF               jne 0x14047c26b
0047C3E4  41 8D 4E 01                     lea ecx, [r14 + 1]
0047C3E8  44 8A C1                        mov r8b, cl
0047C3EB  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
0047C3EF  EB D7                           jmp 0x14047c3c8
0047C3F1  83 F9 01                        cmp ecx, 1
0047C3F4  0F 84 88 FD FF FF               je 0x14047c182
0047C3FA  BB 01 00 00 00                  mov ebx, 1
0047C3FF  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0047C404  44 88 44 24 70                  mov byte ptr [rsp + 0x70], r8b
0047C409  44 3B E3                        cmp r12d, ebx
0047C40C  0F 85 50 FF FF FF               jne 0x14047c362
0047C412  B9 01 00 00 00                  mov ecx, 1
0047C417  E9 BD FE FF FF                  jmp 0x14047c2d9
0047C41C  85 ED                           test ebp, ebp
0047C41E  0F 85 99 FD FF FF               jne 0x14047c1bd
0047C424  8D 6F 01                        lea ebp, [rdi + 1]
0047C427  41 BC 02 00 00 00               mov r12d, 2
0047C42D  83 C7 02                        add edi, 2
0047C430  48 83 C6 02                     add rsi, 2
0047C434  E9 29 FF FF FF                  jmp 0x14047c362
0047C439  66 83 FB 2E                     cmp bx, 0x2e
0047C43D  0F 85 7A FD FF FF               jne 0x14047c1bd
0047C443  45 84 C0                        test r8b, r8b
0047C446  0F 85 71 FD FF FF               jne 0x14047c1bd
0047C44C  41 83 FE 02                     cmp r14d, 2
0047C450  0F 87 15 FE FF FF               ja 0x14047c26b
0047C456  83 FF 06                        cmp edi, 6
0047C459  0F 86 FD 85 27 00               jbe 0x1406f4a5c
0047C45F  45 84 DB                        test r11b, r11b
0047C462  0F 84 55 FD FF FF               je 0x14047c1bd
0047C468  E9 EF 85 27 00                  jmp 0x1406f4a5c
0047C46D  45 84 DB                        test r11b, r11b
0047C470  0F 84 47 FD FF FF               je 0x14047c1bd
0047C476  E9 CC FE FF FF                  jmp 0x14047c347
0047C47B  41 83 FF 03                     cmp r15d, 3
0047C47F  0F 87 FA FD FF FF               ja 0x14047c27f
0047C485  33 D2                           xor edx, edx
0047C487  49 8B C9                        mov rcx, r9
0047C48A  44 8D 42 0A                     lea r8d, [rdx + 0xa]
0047C48E  E8 A1 5F 08 00                  call 0x140502434
0047C493  3D FF 00 00 00                  cmp eax, 0xff
0047C498  0F 87 E1 FD FF FF               ja 0x14047c27f
0047C49E  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
0047C4A6  44 8A 44 24 70                  mov r8b, byte ptr [rsp + 0x70]
0047C4AB  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0047C4B0  42 8D 0C 55 FF FF FF FF         lea ecx, [r10*2 - 1]
0047C4B8  41 03 CE                        add ecx, r14d
0047C4BB  42 88 04 29                     mov byte ptr [rcx + r13], al
0047C4BF  E9 4E FF FF FF                  jmp 0x14047c412
0047C4C4  41 83 FC 02                     cmp r12d, 2
0047C4C8  0F 85 B1 FD FF FF               jne 0x14047c27f
0047C4CE  8B 8C 24 88 00 00 00            mov ecx, dword ptr [rsp + 0x88]
0047C4D5  66 41 89 74 4D 00               mov word ptr [r13 + rcx*2], si
0047C4DB  E9 3F FD FF FF                  jmp 0x14047c21f
0047C4E0  83 FF 08                        cmp edi, 8
0047C4E3  0F 87 D4 FC FF FF               ja 0x14047c1bd
0047C4E9  45 84 DB                        test r11b, r11b
0047C4EC  0F 84 CB FC FF FF               je 0x14047c1bd
0047C4F2  E9 94 FC FF FF                  jmp 0x14047c18b
0047C4F7  B9 01 00 00 00                  mov ecx, 1
0047C4FC  03 F9                           add edi, ecx
0047C4FE  E9 D2 FC FF FF                  jmp 0x14047c1d5
0047C503  41 83 FF 03                     cmp r15d, 3
0047C507  0F 87 72 FD FF FF               ja 0x14047c27f
0047C50D  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0047C512  33 D2                           xor edx, edx
0047C514  44 8D 42 0A                     lea r8d, [rdx + 0xa]
0047C518  E8 17 5F 08 00                  call 0x140502434
0047C51D  3D FF 00 00 00                  cmp eax, 0xff
0047C522  0F 87 57 FD FF FF               ja 0x14047c27f
0047C528  8B 8C 24 88 00 00 00            mov ecx, dword ptr [rsp + 0x88]
0047C52F  41 8D 0C 4E                     lea ecx, [r14 + rcx*2]
0047C533  42 88 04 29                     mov byte ptr [rcx + r13], al
0047C537  E9 E3 FC FF FF                  jmp 0x14047c21f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlIpv6StringToAddressW(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p70;
    unsigned __int8 v_stack_p8;
    unsigned int v_stack_p88;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (48);
    result = 0;
    v_stack_m40 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
loc_0047C162:
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_0047C1C2;
    result = 0;
    if (0 != 0) goto loc_0047C29D;
loc_0047C182:
    if (0 > 7) goto loc_0047C4E0;
loc_0047C18B:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) >= 128) goto loc_0047C1BD;
    result = iswctype((unsigned __int16)(*(unsigned __int16 *)(a1)), 128 - 124, 0, 0);
    if ((unsigned int)(result) != 0) goto loc_0047C3BC;
    result = iswctype((unsigned __int16)(*(unsigned __int16 *)(a1)), 128, 0, 0);
    if ((unsigned int)(result) != 0) goto loc_0047C3DB;
loc_0047C1BD:
loc_0047C1C2:
    *(unsigned __int64 *)(v_stack_p10) = a1;
    v_rsi = 0;
    if (0 != 0) goto loc_0047C275;
loc_0047C1D5:
    if (0 != 0) goto loc_0047C1E2;
    if (0 != 7) goto loc_0047C27F;
loc_0047C1E2:
    if (0 != 1) goto loc_0047C4C4;
    if (0 != 0) goto loc_0047C503;
    if (0 > 4) goto loc_0047C27F;
    a2 = 0;
    result = wcstol(v_stack_m40, a2, 0 + 16, 0);
    *(unsigned __int16 *)(a3 + (unsigned int)(v_stack_p20) * 2) = (unsigned __int16)(result);
loc_0047C21F:
    v_rbx = *(unsigned __int16 *)(a1);
    v_rbp = 0;
    if (0 != 0) {
        result = 0;
        a3 = 0;
        a3 = (unsigned int)((a3) - (0));
        v_rsi = 8;
        v_rbp = (unsigned int)((0) - (0));
        a3 = (a3) + (a3);
        v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(v_rsi)));
        v_rbx = result * 2;
        v_rbx = (v_rbx) + (a3);
        a2 = v_rbx;
        a1 = v_rbp * 2;
        a1 = (a1) + (a3);
        result = memcpy(a1, a2, a3, 0);
        v_rsi = (unsigned int)((v_rsi) - (0));
        a2 = 0;
        a3 = (unsigned int)(v_rsi);
        a1 = v_rbx;
        a3 = (a3) + (a3);
        result = memset(a1, a2, a3, 0);
    }
    result = 0;
    goto loc_0047C284;
loc_0047C26B:
    *(unsigned __int64 *)(v_stack_p10) = v_rsi;
    v_rsi = 0;
loc_0047C275:
    if (0 == 3) goto loc_0047C4F7;
loc_0047C27F:
loc_0047C284:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(0xC000000DULL);
loc_0047C29D:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_0047C3F1;
    if (((unsigned __int16)(v_stack_p18)) >= 128) goto loc_0047C32B;
    result = iswctype((unsigned __int16)(v_stack_p18), 128 - 124, a3, 0);
    if ((unsigned int)(result) == 0) goto loc_0047C2E7;
    v_r15 = (unsigned int)((0) + (1));
loc_0047C2CC:
loc_0047C2D1:
loc_0047C2D9:
    v_rsi = (v_rsi) + (2);
    goto loc_0047C162;
loc_0047C2E7:
    result = iswctype((unsigned __int16)(v_stack_p18), 128, v_stack_p70, v_stack_p28);
    if ((unsigned int)(result) == 0) goto loc_0047C312;
    v_r15 = (unsigned int)((v_r15) + (1));
    if (0 != 0) goto loc_0047C26B;
    v_stack_p70 = 1;
    goto loc_0047C2CC;
loc_0047C312:
    result = 0;
loc_0047C32B:
    if (((unsigned __int16)(v_stack_p18)) != 58) goto loc_0047C439;
    if (0 != 0) goto loc_0047C26B;
    if (0 > 6) goto loc_0047C46D;
loc_0047C347:
    if (0 > 7) goto loc_0047C1BD;
    if ((*(unsigned __int16 *)(v_rsi + 2)) == 58) goto loc_0047C41C;
    v_rdi = (unsigned int)((0) + 1);
    result = 0;
loc_0047C362:
    if (v_stack_p28 == 0) goto loc_0047C412;
    if (0 != 0) goto loc_0047C47B;
    if (((unsigned int)(v_r15)) > 4) goto loc_0047C27F;
    a2 = 0;
    result = wcstol(v_stack_p28, a2, 0 + 16, v_stack_p28);
    *(unsigned __int16 *)(a3 + (unsigned int)(v_stack_p88) * 2) = (unsigned __int16)(result);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p88)) + ((unsigned int)(0 + 1)));
    v_stack_p88 = (unsigned int)(v_r10);
    goto loc_0047C2D9;
loc_0047C3BC:
    result = 0;
    v_stack_p70 = 0;
loc_0047C3C8:
    v_stack_p28 = v_rsi;
    goto loc_0047C2D1;
loc_0047C3DB:
    if (0 != 0) goto loc_0047C26B;
    v_stack_p70 = (unsigned __int8)(0 + 1);
    goto loc_0047C3C8;
loc_0047C3F1:
    if (((unsigned int)(0 + 1)) == 1) goto loc_0047C182;
    v_stack_p28 = v_rsi;
    v_stack_p70 = (unsigned __int8)((unsigned __int8)(0 + 1));
    if (((unsigned int)((unsigned int)((unsigned int)(result + 1)))) != 1) goto loc_0047C362;
loc_0047C412:
    goto loc_0047C2D9;
loc_0047C41C:
    if ((unsigned int)(v_rbp) != 0) goto loc_0047C1BD;
    v_rdi = (unsigned int)((v_rdi) + (2));
    v_rsi = (v_rsi) + (2);
    goto loc_0047C362;
loc_0047C439:
    if (1 != 46) goto loc_0047C1BD;
    if ((unsigned __int8)((unsigned __int8)(0 + 1)) != 0) goto loc_0047C1BD;
    if (0 > 2) goto loc_0047C26B;
    if ((unsigned __int8)((unsigned int)(v_stack_p20)) == 0) goto loc_0047C1BD;
loc_0047C46D:
    if ((unsigned __int8)((unsigned int)(v_stack_p20)) == 0) goto loc_0047C1BD;
    goto loc_0047C347;
loc_0047C47B:
    if (((unsigned int)((unsigned int)((unsigned int)(result + 1)))) > 3) goto loc_0047C27F;
    a2 = 0;
    result = wcstol(v_rsi, a2, a2 + 10, v_rsi);
    if (((unsigned int)(result)) > 255) goto loc_0047C27F;
    a1 = (unsigned int)(((unsigned int)(v_stack_p88) * 2 - 1) + (0));
    *(unsigned __int8 *)(a1 + a3 * 1) = (unsigned __int8)(result);
    goto loc_0047C412;
loc_0047C4C4:
    if (2 != 2) goto loc_0047C27F;
    *(unsigned __int16 *)(a3 + (unsigned int)(v_stack_p88) * 2) = (unsigned __int16)(v_rsi);
    goto loc_0047C21F;
loc_0047C4E0:
    if (((unsigned int)(v_rdi)) > 8) goto loc_0047C1BD;
    if ((unsigned __int8)((unsigned int)(v_stack_p20)) == 0) goto loc_0047C1BD;
    goto loc_0047C18B;
loc_0047C4F7:
    v_rdi = (unsigned int)((v_rdi) + (1));
    goto loc_0047C1D5;
loc_0047C503:
    if (((unsigned int)((unsigned int)((unsigned int)(result + 1)))) > 3) goto loc_0047C27F;
    a2 = 0;
    result = wcstol(v_stack_p28, a2, a2 + 10, v_stack_p28);
    if (((unsigned int)(result)) > 255) goto loc_0047C27F;
    *(unsigned __int8 *)(0 + (unsigned int)(v_stack_p88) * 2 + a3 * 1) = (unsigned __int8)(result);
    goto loc_0047C21F;
}
```

## 5. (Beta) C Style

```c
int64_t RtlIpv6StringToAddressW(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p70;
    uint8_t v_stack_p8;
    uint32_t v_stack_p88;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (48);
    result = 0;
    v_stack_m40 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
loc_0047C162:
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_0047C1C2;
    result = 0;
    if (0 != 0) goto loc_0047C29D;
loc_0047C182:
    if (0 > 7) goto loc_0047C4E0;
loc_0047C18B:
    if (((uint16_t)(*(uint16_t *)(arg1))) >= 128) goto loc_0047C1BD;
    result = iswctype((uint16_t)(*(uint16_t *)(arg1)), 128 - 124, 0, 0);
    if ((uint32_t)(result) != 0) goto loc_0047C3BC;
    result = iswctype((uint16_t)(*(uint16_t *)(arg1)), 128, 0, 0);
    if ((uint32_t)(result) != 0) goto loc_0047C3DB;
loc_0047C1BD:
loc_0047C1C2:
    *(void **)(v_stack_p10) = Arg1;
    local_rsi = 0;
    if (0 != 0) goto loc_0047C275;
loc_0047C1D5:
    if (0 != 0) goto loc_0047C1E2;
    if (0 != 7) goto loc_0047C27F;
loc_0047C1E2:
    if (0 != 1) goto loc_0047C4C4;
    if (0 != 0) goto loc_0047C503;
    if (0 > 4) goto loc_0047C27F;
    Arg2 = 0;
    result = wcstol(v_stack_m40, Arg2, 0 + 16, 0);
    *(uint16_t *)(arg3 + (uint32_t)(v_stack_p20) * 2) = (uint16_t)(result);
loc_0047C21F:
    local_rbx = *(uint16_t *)(arg1);
    local_rbp = 0;
    if (0 != 0) {
        result = 0;
        Arg3 = 0;
        Arg3 = (uint32_t)((Arg3) - (0));
        local_rsi = 8;
        local_rbp = (uint32_t)((0) - (0));
        Arg3 = (Arg3) + (Arg3);
        local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(local_rsi)));
        local_rbx = result * 2;
        local_rbx = (local_rbx) + (Arg3);
        Arg2 = local_rbx;
        Arg1 = local_rbp * 2;
        Arg1 = (Arg1) + (Arg3);
        result = memcpy(Arg1, Arg2, Arg3, 0);
        local_rsi = (uint32_t)((local_rsi) - (0));
        Arg2 = 0;
        Arg3 = (uint32_t)(local_rsi);
        Arg1 = local_rbx;
        Arg3 = (Arg3) + (Arg3);
        result = memset(Arg1, Arg2, Arg3, 0);
    }
    result = 0;
    goto loc_0047C284;
loc_0047C26B:
    *(uint64_t *)(v_stack_p10) = local_rsi;
    local_rsi = 0;
loc_0047C275:
    if (0 == 3) goto loc_0047C4F7;
loc_0047C27F:
loc_0047C284:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(0xC000000DULL);
loc_0047C29D:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_0047C3F1;
    if (((uint16_t)(v_stack_p18)) >= 128) goto loc_0047C32B;
    result = iswctype((uint16_t)(v_stack_p18), 128 - 124, Arg3, 0);
    if ((uint32_t)(result) == 0) goto loc_0047C2E7;
    local_r15 = (uint32_t)((0) + (1));
loc_0047C2CC:
loc_0047C2D1:
loc_0047C2D9:
    local_rsi = (local_rsi) + (2);
    goto loc_0047C162;
loc_0047C2E7:
    result = iswctype((uint16_t)(v_stack_p18), 128, v_stack_p70, v_stack_p28);
    if ((uint32_t)(result) == 0) goto loc_0047C312;
    local_r15 = (uint32_t)((local_r15) + (1));
    if (0 != 0) goto loc_0047C26B;
    v_stack_p70 = 1;
    goto loc_0047C2CC;
loc_0047C312:
    result = 0;
loc_0047C32B:
    if (((uint16_t)(v_stack_p18)) != 58) goto loc_0047C439;
    if (0 != 0) goto loc_0047C26B;
    if (0 > 6) goto loc_0047C46D;
loc_0047C347:
    if (0 > 7) goto loc_0047C1BD;
    if ((*(uint16_t *)(local_rsi + 0x2)) == 58) goto loc_0047C41C;
    local_rdi = (uint32_t)((0) + 1);
    result = 0;
loc_0047C362:
    if (v_stack_p28 == 0) goto loc_0047C412;
    if (0 != 0) goto loc_0047C47B;
    if (((uint32_t)(local_r15)) > 4) goto loc_0047C27F;
    Arg2 = 0;
    result = wcstol(v_stack_p28, Arg2, 0 + 16, v_stack_p28);
    *(uint16_t *)(arg3 + (uint32_t)(v_stack_p88) * 2) = (uint16_t)(result);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p88)) + ((uint32_t)(0 + 1)));
    v_stack_p88 = (uint32_t)(local_r10);
    goto loc_0047C2D9;
loc_0047C3BC:
    result = 0;
    v_stack_p70 = 0;
loc_0047C3C8:
    v_stack_p28 = local_rsi;
    goto loc_0047C2D1;
loc_0047C3DB:
    if (0 != 0) goto loc_0047C26B;
    v_stack_p70 = (uint8_t)(0 + 1);
    goto loc_0047C3C8;
loc_0047C3F1:
    if (((uint32_t)(0 + 1)) == 1) goto loc_0047C182;
    v_stack_p28 = local_rsi;
    v_stack_p70 = (uint8_t)((uint8_t)(0 + 1));
    if (((uint32_t)((uint32_t)((uint32_t)(result + 1)))) != 1) goto loc_0047C362;
loc_0047C412:
    goto loc_0047C2D9;
loc_0047C41C:
    if ((uint32_t)(local_rbp) != 0) goto loc_0047C1BD;
    local_rdi = (uint32_t)((local_rdi) + (2));
    local_rsi = (local_rsi) + (2);
    goto loc_0047C362;
loc_0047C439:
    if (1 != 46) goto loc_0047C1BD;
    if ((uint8_t)((uint8_t)(0 + 1)) != 0) goto loc_0047C1BD;
    if (0 > 2) goto loc_0047C26B;
    if ((uint8_t)((uint32_t)(v_stack_p20)) == 0) goto loc_0047C1BD;
loc_0047C46D:
    if ((uint8_t)((uint32_t)(v_stack_p20)) == 0) goto loc_0047C1BD;
    goto loc_0047C347;
loc_0047C47B:
    if (((uint32_t)((uint32_t)((uint32_t)(result + 1)))) > 3) goto loc_0047C27F;
    Arg2 = 0;
    result = wcstol(local_rsi, Arg2, Arg2 + 10, local_rsi);
    if (((uint32_t)(result)) > 255) goto loc_0047C27F;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p88) * 2 - 1) + (0));
    *(uint8_t *)(arg1 + arg3 * 1) = (uint8_t)(result);
    goto loc_0047C412;
loc_0047C4C4:
    if (2 != 2) goto loc_0047C27F;
    *(uint16_t *)(arg3 + (uint32_t)(v_stack_p88) * 2) = (uint16_t)(local_rsi);
    goto loc_0047C21F;
loc_0047C4E0:
    if (((uint32_t)(local_rdi)) > 8) goto loc_0047C1BD;
    if ((uint8_t)((uint32_t)(v_stack_p20)) == 0) goto loc_0047C1BD;
    goto loc_0047C18B;
loc_0047C4F7:
    local_rdi = (uint32_t)((local_rdi) + (1));
    goto loc_0047C1D5;
loc_0047C503:
    if (((uint32_t)((uint32_t)((uint32_t)(result + 1)))) > 3) goto loc_0047C27F;
    Arg2 = 0;
    result = wcstol(v_stack_p28, Arg2, Arg2 + 10, v_stack_p28);
    if (((uint32_t)(result)) > 255) goto loc_0047C27F;
    *(uint8_t *)(0 + (uint32_t)(v_stack_p88) * 2 + arg3 * 1) = (uint8_t)(result);
    goto loc_0047C21F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg3` | `+ 0x0 + r10*2` | `16` | `W` |
| `Arg3` | `+ 0x0 + rcx*2` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047C110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
