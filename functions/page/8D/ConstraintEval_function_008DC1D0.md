# ConstraintEval

- RVA: `0x008DC1D0`–`0x008DC566` (길이 `918` bytes)
- VA: `0x00000001408DC1D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000858E0`
- 디코드: `225`개 명령, `918/918` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008DC24A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DC270` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008DC2EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DC2FA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008DC40C` → [FilterEvalStrict](../8E/FilterEvalStrict_function_008E0ADC.md) (function, `0x008E0ADC`)
- `0x008DC45D` → [SimplifyFilter](SimplifyFilter_function_008DBD0C.md) (function, `0x008DBD0C`)
- `0x008DC4A2` → [FilterEvalImpliedAnd](FilterEvalImpliedAnd_function_008DE898.md) (function, `0x008DE898`)
- `0x008DC4E6` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x008DC554` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)

### Direct callers
- [PiDqObjectManagerEnumerateAndRegisterQuery](PiDqObjectManagerEnumerateAndRegisterQuery_function_008DCF74.md) at `0x008DD133`

### Static image references
- `0x008DC1EA` → RVA `0x00E0A740` (`.data`; read)
- `0x008DC3FC` → RVA `0x00A51A30` (`GetPropertyFromPropArray`; read)
- `0x008DC506` → RVA `0x00EEFFE2` (`.data`; read)
- `0x008DC50D` → RVA `0x00E0F120` (`.data`; read)
- `0x008DC524` → RVA `0x00EEFFE4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008DC24A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008DC270` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008DC2EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DC2FA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008DC4E6` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x008DC554` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008DC2D9` → [sub_00B1C8E2](../B1/Unknown_function_00B1C8E2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DC1D0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008DC1D5  55                              push rbp
008DC1D6  56                              push rsi
008DC1D7  57                              push rdi
008DC1D8  41 54                           push r12
008DC1DA  41 55                           push r13
008DC1DC  41 56                           push r14
008DC1DE  41 57                           push r15
008DC1E0  48 8B EC                        mov rbp, rsp
008DC1E3  48 81 EC 80 00 00 00            sub rsp, 0x80
008DC1EA  48 8B 05 4F E5 52 00            mov rax, qword ptr [rip + 0x52e54f]
008DC1F1  48 33 C4                        xor rax, rsp
008DC1F4  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008DC1F8  83 65 B4 00                     and dword ptr [rbp - 0x4c], 0
008DC1FC  0F 57 C0                        xorps xmm0, xmm0
008DC1FF  83 65 B0 00                     and dword ptr [rbp - 0x50], 0
008DC203  41 8B D9                        mov ebx, r9d
008DC206  4C 8B 6D 60                     mov r13, qword ptr [rbp + 0x60]
008DC20A  4D 8B F0                        mov r14, r8
008DC20D  44 8B F9                        mov r15d, ecx
008DC210  48 8B FA                        mov rdi, rdx
008DC213  4D 6B E7 38                     imul r12, r15, 0x38
008DC217  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
008DC21B  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
008DC21F  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
008DC223  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
008DC227  41 F7 C1 00 00 F0 0F            test r9d, 0xff00000
008DC22E  0F 85 78 02 00 00               jne 0x1408dc4ac
008DC234  85 C9                           test ecx, ecx
008DC236  0F 84 84 02 00 00               je 0x1408dc4c0
008DC23C  41 B8 46 4C 54 52               mov r8d, 0x52544c46
008DC242  49 8B D4                        mov rdx, r12
008DC245  B9 00 01 00 00                  mov ecx, 0x100
008DC24A  E8 A1 5E 2A 00                  call 0x140b820f0
008DC24F  48 8B F0                        mov rsi, rax
008DC252  48 85 C0                        test rax, rax
008DC255  0F 84 6F 02 00 00               je 0x1408dc4ca
008DC25B  F7 07 00 00 F0 0F               test dword ptr [rdi], 0xff00000
008DC261  48 8B D7                        mov rdx, rdi
008DC264  0F 85 E9 01 00 00               jne 0x1408dc453
008DC26A  4D 8B C4                        mov r8, r12
008DC26D  48 8B C8                        mov rcx, rax
008DC270  E8 CB A5 DE FF                  call 0x1406c6840
008DC275  33 FF                           xor edi, edi
008DC277  41 3B FF                        cmp edi, r15d
008DC27A  73 63                           jae 0x1408dc2df
008DC27C  8B C7                           mov eax, edi
008DC27E  48 6B D0 38                     imul rdx, rax, 0x38
008DC282  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
008DC286  39 44 32 18                     cmp dword ptr [rdx + rsi + 0x18], eax
008DC28A  0F 84 8B 00 00 00               je 0x1408dc31b
008DC290  FF C7                           inc edi
008DC292  EB E3                           jmp 0x1408dc277
008DC294  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
008DC298  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
008DC29C  75 08                           jne 0x1408dc2a6
008DC29E  48 8B 4A 10                     mov rcx, qword ptr [rdx + 0x10]
008DC2A2  48 2B 4F 10                     sub rcx, qword ptr [rdi + 0x10]
008DC2A6  48 85 C9                        test rcx, rcx
008DC2A9  0F 85 17 01 00 00               jne 0x1408dc3c6
008DC2AF  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
008DC2B2  39 42 1C                        cmp dword ptr [rdx + 0x1c], eax
008DC2B5  0F 85 0B 01 00 00               jne 0x1408dc3c6
008DC2BB  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
008DC2BF  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
008DC2C3  48 3B CA                        cmp rcx, rdx
008DC2C6  0F 85 76 02 00 00               jne 0x1408dc542
008DC2CC  8B C3                           mov eax, ebx
008DC2CE  48 6B C8 38                     imul rcx, rax, 0x38
008DC2D2  44 8B 34 31                     mov r14d, dword ptr [rcx + rsi]
008DC2D6  44 3B 37                        cmp r14d, dword ptr [rdi]
008DC2D9  0F 84 03 06 24 00               je 0x140b1c8e2
008DC2DF  BB 01 00 00 C0                  mov ebx, 0xc0000001
008DC2E4  BA 46 4C 54 52                  mov edx, 0x52544c46
008DC2E9  48 8B CE                        mov rcx, rsi
008DC2EC  E8 7F 65 2A 00                  call 0x140b82870
008DC2F1  8B C3                           mov eax, ebx
008DC2F3  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
008DC2F7  48 33 CC                        xor rcx, rsp
008DC2FA  E8 41 03 DD FF                  call 0x1406ac640
008DC2FF  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
008DC307  48 81 C4 80 00 00 00            add rsp, 0x80
008DC30E  41 5F                           pop r15
008DC310  41 5E                           pop r14
008DC312  41 5D                           pop r13
008DC314  41 5C                           pop r12
008DC316  5F                              pop rdi
008DC317  5E                              pop rsi
008DC318  5D                              pop rbp
008DC319  C3                              ret
008DC31A  CC                              int3
008DC31B  48 8B 4C 32 08                  mov rcx, qword ptr [rdx + rsi + 8]
008DC320  49 2B 0E                        sub rcx, qword ptr [r14]
008DC323  75 09                           jne 0x1408dc32e
008DC325  48 8B 4C 32 10                  mov rcx, qword ptr [rdx + rsi + 0x10]
008DC32A  49 2B 4E 08                     sub rcx, qword ptr [r14 + 8]
008DC32E  48 85 C9                        test rcx, rcx
008DC331  0F 85 59 FF FF FF               jne 0x1408dc290
008DC337  41 8B 46 14                     mov eax, dword ptr [r14 + 0x14]
008DC33B  39 44 32 1C                     cmp dword ptr [rdx + rsi + 0x1c], eax
008DC33F  0F 85 4B FF FF FF               jne 0x1408dc290
008DC345  48 8B 4C 32 20                  mov rcx, qword ptr [rdx + rsi + 0x20]
008DC34A  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
008DC34E  48 3B CA                        cmp rcx, rdx
008DC351  0F 85 7D 01 00 00               jne 0x1408dc4d4
008DC357  8B C7                           mov eax, edi
008DC359  48 6B C8 38                     imul rcx, rax, 0x38
008DC35D  39 1C 31                        cmp dword ptr [rcx + rsi], ebx
008DC360  0F 85 2A FF FF FF               jne 0x1408dc290
008DC366  8B C7                           mov eax, edi
008DC368  48 6B F8 38                     imul rdi, rax, 0x38
008DC36C  48 03 FE                        add rdi, rsi
008DC36F  0F 84 6A FF FF FF               je 0x1408dc2df
008DC375  41 BC 00 00 01 00               mov r12d, 0x10000
008DC37B  0F 10 47 08                     movups xmm0, xmmword ptr [rdi + 8]
008DC37F  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
008DC383  0F 10 4F 18                     movups xmm1, xmmword ptr [rdi + 0x18]
008DC387  0F 11 4D D8                     movups xmmword ptr [rbp - 0x28], xmm1
008DC38B  0F 10 47 28                     movups xmm0, xmmword ptr [rdi + 0x28]
008DC38F  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
008DC393  83 EB 01                        sub ebx, 1
008DC396  0F 84 88 01 00 00               je 0x1408dc524
008DC39C  83 EB 01                        sub ebx, 1
008DC39F  0F 85 C6 00 00 00               jne 0x1408dc46b
008DC3A5  33 DB                           xor ebx, ebx
008DC3A7  41 3B DF                        cmp ebx, r15d
008DC3AA  73 1E                           jae 0x1408dc3ca
008DC3AC  8B C3                           mov eax, ebx
008DC3AE  48 6B D0 38                     imul rdx, rax, 0x38
008DC3B2  48 03 D6                        add rdx, rsi
008DC3B5  48 3B D7                        cmp rdx, rdi
008DC3B8  74 0C                           je 0x1408dc3c6
008DC3BA  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008DC3BD  39 42 18                        cmp dword ptr [rdx + 0x18], eax
008DC3C0  0F 84 CE FE FF FF               je 0x1408dc294
008DC3C6  FF C3                           inc ebx
008DC3C8  EB DD                           jmp 0x1408dc3a7
008DC3CA  44 31 27                        xor dword ptr [rdi], r12d
008DC3CD  48 8D 45 C8                     lea rax, [rbp - 0x38]
008DC3D1  C7 45 B8 01 00 00 00            mov dword ptr [rbp - 0x48], 1
008DC3D8  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
008DC3DC  41 83 FF 01                     cmp r15d, 1
008DC3E0  0F 82 D0 00 00 00               jb 0x1408dc4b6
008DC3E6  F7 06 00 00 F0 0F               test dword ptr [rsi], 0xff00000
008DC3EC  48 8D 45 B0                     lea rax, [rbp - 0x50]
008DC3F0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DC3F5  48 8D 55 B8                     lea rdx, [rbp - 0x48]
008DC3F9  4C 8B CE                        mov r9, rsi
008DC3FC  48 8D 0D 2D 56 17 00            lea rcx, [rip + 0x17562d]
008DC403  45 8B C7                        mov r8d, r15d
008DC406  0F 84 96 00 00 00               je 0x1408dc4a2
008DC40C  E8 CB 46 00 00                  call 0x1408e0adc
008DC411  8B D8                           mov ebx, eax
008DC413  85 C0                           test eax, eax
008DC415  0F 88 C9 FE FF FF               js 0x1408dc2e4
008DC41B  83 7D B0 00                     cmp dword ptr [rbp - 0x50], 0
008DC41F  0F 85 BA FE FF FF               jne 0x1408dc2df
008DC425  0F 10 07                        movups xmm0, xmmword ptr [rdi]
008DC428  41 0F 11 45 00                  movups xmmword ptr [r13], xmm0
008DC42D  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
008DC431  41 0F 11 4D 10                  movups xmmword ptr [r13 + 0x10], xmm1
008DC436  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
008DC43A  41 0F 11 45 20                  movups xmmword ptr [r13 + 0x20], xmm0
008DC43F  F2 0F 10 4F 30                  movsd xmm1, qword ptr [rdi + 0x30]
008DC444  F2 41 0F 11 4D 30               movsd qword ptr [r13 + 0x30], xmm1
008DC44A  45 31 65 00                     xor dword ptr [r13], r12d
008DC44E  E9 91 FE FF FF                  jmp 0x1408dc2e4
008DC453  4C 8B CE                        mov r9, rsi
008DC456  4C 8D 45 B4                     lea r8, [rbp - 0x4c]
008DC45A  41 8B CF                        mov ecx, r15d
008DC45D  E8 AA F8 FF FF                  call 0x1408dbd0c
008DC462  44 8B 7D B4                     mov r15d, dword ptr [rbp - 0x4c]
008DC466  E9 0A FE FF FF                  jmp 0x1408dc275
008DC46B  41 2B DC                        sub ebx, r12d
008DC46E  0F 84 84 00 00 00               je 0x1408dc4f8
008DC474  41 3B DC                        cmp ebx, r12d
008DC477  0F 85 62 FE FF FF               jne 0x1408dc2df
008DC47D  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
008DC480  83 F8 12                        cmp eax, 0x12
008DC483  0F 84 1C FF FF FF               je 0x1408dc3a5
008DC489  83 F8 19                        cmp eax, 0x19
008DC48C  0F 84 13 FF FF FF               je 0x1408dc3a5
008DC492  3D 12 20 00 00                  cmp eax, 0x2012
008DC497  0F 84 08 FF FF FF               je 0x1408dc3a5
008DC49D  E9 3D FE FF FF                  jmp 0x1408dc2df
008DC4A2  E8 F1 23 00 00                  call 0x1408de898
008DC4A7  E9 65 FF FF FF                  jmp 0x1408dc411
008DC4AC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DC4B1  E9 3B FE FF FF                  jmp 0x1408dc2f1
008DC4B6  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008DC4BB  E9 24 FE FF FF                  jmp 0x1408dc2e4
008DC4C0  BB 01 00 00 C0                  mov ebx, 0xc0000001
008DC4C5  E9 27 FE FF FF                  jmp 0x1408dc2f1
008DC4CA  BB 17 00 00 C0                  mov ebx, 0xc0000017
008DC4CF  E9 1D FE FF FF                  jmp 0x1408dc2f1
008DC4D4  48 85 C9                        test rcx, rcx
008DC4D7  0F 84 B3 FD FF FF               je 0x1408dc290
008DC4DD  48 85 D2                        test rdx, rdx
008DC4E0  0F 84 AA FD FF FF               je 0x1408dc290
008DC4E6  E8 95 3B C2 FF                  call 0x140500080
008DC4EB  85 C0                           test eax, eax
008DC4ED  0F 85 9D FD FF FF               jne 0x1408dc290
008DC4F3  E9 5F FE FF FF                  jmp 0x1408dc357
008DC4F8  83 7D E8 11                     cmp dword ptr [rbp - 0x18], 0x11
008DC4FC  0F 85 DD FD FF FF               jne 0x1408dc2df
008DC502  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
008DC506  48 8D 0D D5 3A 61 00            lea rcx, [rip + 0x613ad5]
008DC50D  48 8D 15 0C 2C 53 00            lea rdx, [rip + 0x532c0c]
008DC514  80 38 FF                        cmp byte ptr [rax], 0xff
008DC517  48 0F 45 CA                     cmovne rcx, rdx
008DC51B  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
008DC51F  E9 81 FE FF FF                  jmp 0x1408dc3a5
008DC524  48 8D 05 B9 3A 61 00            lea rax, [rip + 0x613ab9]
008DC52B  C7 45 E8 07 00 00 00            mov dword ptr [rbp - 0x18], 7
008DC532  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
008DC536  C7 45 EC 04 00 00 00            mov dword ptr [rbp - 0x14], 4
008DC53D  E9 63 FE FF FF                  jmp 0x1408dc3a5
008DC542  48 85 C9                        test rcx, rcx
008DC545  0F 84 7B FE FF FF               je 0x1408dc3c6
008DC54B  48 85 D2                        test rdx, rdx
008DC54E  0F 84 72 FE FF FF               je 0x1408dc3c6
008DC554  E8 27 3B C2 FF                  call 0x140500080
008DC559  85 C0                           test eax, eax
008DC55B  0F 85 65 FE FF FF               jne 0x1408dc3c6
008DC561  E9 66 FD FF FF                  jmp 0x1408dc2cc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ConstraintEval(int a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 5432655)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = (v_r12) * ((unsigned int)(a1));
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m80 = v_xmm0;
    if (((a4) & (0xFF00000ULL)) != 0) goto loc_008DC4AC;
    if (a1 == 0) goto loc_008DC4C0;
    result = ExAllocatePool2(256, v_r12, (unsigned int)(0x52544C46ULL), a4);
    if (result == 0) goto loc_008DC4CA;
    if (((*(unsigned int *)(a2)) & (0xFF00000ULL)) != 0) goto loc_008DC453;
    result = memcpy(result, a2, v_r12, a4);
loc_008DC275:
    v_rdi = 0;
loc_008DC277:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_008DC2DF;
    a2 = (a2) * (0);
    if ((*(unsigned int *)(a2 + result * 1 + 24)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_008DC31B;
loc_008DC290:
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_008DC277;
loc_008DC294:
    a1 = (*(unsigned __int64 *)(a2 + 8)) - (*(unsigned __int64 *)(v_rdi + 8));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a2 + 16);
        a1 = (a1) - (*(unsigned __int64 *)(v_rdi + 16));
    }
    if (a1 != 0) goto loc_008DC3C6;
    if ((*(unsigned int *)(a2 + 28)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 28))))) goto loc_008DC3C6;
    if ((*(unsigned __int64 *)(a2 + 32)) != (*(unsigned __int64 *)(v_rdi + 32))) goto loc_008DC542;
loc_008DC2CC:
    a1 = (*(unsigned __int64 *)(a2 + 32)) * ((unsigned int)((unsigned int)((unsigned int)(a4))));
loc_008DC2DF:
loc_008DC2E4:
    result = ExFreePoolWithTag(result, (unsigned int)(0x52544C46ULL), v_r12, a4);
loc_008DC2F1:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x52544C46ULL), v_r12, a4);
    v_rsp = (v_rsp) + (128);
    return result;
loc_008DC31B:
    a1 = (*(unsigned __int64 *)((unsigned int)(0x52544C46ULL) + result * 1 + 8)) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + result * 1))));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)((unsigned int)(0x52544C46ULL) + result * 1 + 16);
        a1 = (a1) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + result * 1)) + 8));
    }
    if (a1 != 0) goto loc_008DC290;
    if ((*(unsigned int *)((unsigned int)(0x52544C46ULL) + result * 1 + 28)) != ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + result * 1)) + 20))))) goto loc_008DC290;
    if ((*(unsigned __int64 *)((unsigned int)(0x52544C46ULL) + result * 1 + 32)) != (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + result * 1)) + 24))) goto loc_008DC4D4;
loc_008DC357:
    a1 = (*(unsigned __int64 *)((unsigned int)(0x52544C46ULL) + result * 1 + 32)) * ((unsigned int)((unsigned int)(v_rdi)));
    if ((*(unsigned int *)(a1 + result * 1)) != ((unsigned int)(v_stack_p20))) goto loc_008DC290;
    v_rdi = (v_rdi) * ((unsigned int)((unsigned int)(v_rdi)));
    v_rdi = (v_rdi) + (result);
    if (condition_is_equal) goto loc_008DC2DF;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm0;
    v_rbx = (unsigned int)((v_stack_p20) - (1));
    if (condition_is_equal) goto loc_008DC524;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008DC46B;
loc_008DC3A5:
    v_rbx = 0;
loc_008DC3A7:
    if (0 >= ((unsigned int)((unsigned int)(a1)))) goto loc_008DC3CA;
    a2 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + result * 1)) + 24)) * (0);
    a2 = (a2) + (result);
    if (a2 == v_rdi) goto loc_008DC3C6;
    if ((*(unsigned int *)(a2 + 24)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24))))) goto loc_008DC294;
loc_008DC3C6:
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_008DC3A7;
loc_008DC3CA:
    v_stack_m80 = 1;
    v_stack_m78 = v_stack_m70;
    if (((unsigned int)((unsigned int)(a1))) < 1) goto loc_008DC4B6;
    v_stack_p20 = v_stack_m88;
    if (((*(unsigned int *)(result)) & (0xFF00000ULL)) == 0) goto loc_008DC4A2;
    result = FilterEvalStrict(v_rip + 1529389, v_stack_m80, (unsigned int)((unsigned int)((unsigned int)(a1))), result);
loc_008DC411:
    if (sign_flag) goto loc_008DC2E4;
    if (v_stack_m88 != 0) goto loc_008DC2DF;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm1;
    *(unsigned __int64 *)(a5 + 32) = v_xmm0;
    *(unsigned __int64 *)(a5 + 48) = v_xmm1;
    goto loc_008DC2E4;
loc_008DC453:
    result = SimplifyFilter((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_m80, v_stack_m84, result);
    goto loc_008DC275;
loc_008DC46B:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)((unsigned int)(0x10000ULL))));
    if (condition_is_equal) goto loc_008DC4F8;
    if (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_008DC2DF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 40)))) == 18) goto loc_008DC3A5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 40)))) == 25) goto loc_008DC3A5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 40)))) == 0x2012ULL) goto loc_008DC3A5;
    goto loc_008DC2DF;
loc_008DC4A2:
    result = FilterEvalImpliedAnd((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_m80, v_stack_m84, result);
    goto loc_008DC411;
loc_008DC4AC:
    goto loc_008DC2F1;
loc_008DC4B6:
    goto loc_008DC2E4;
loc_008DC4C0:
    goto loc_008DC2F1;
loc_008DC4CA:
    goto loc_008DC2F1;
loc_008DC4D4:
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) == 0) goto loc_008DC290;
    if (v_stack_m80 == 0) goto loc_008DC290;
    result = wcsicmp((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_m80, v_stack_m84, result);
    if ((unsigned int)(result) != 0) goto loc_008DC290;
    goto loc_008DC357;
loc_008DC4F8:
    if (v_stack_m50 != 17) goto loc_008DC2DF;
    a1 = v_rip + 6372053;
    if ((*(unsigned __int8 *)(v_stack_m48)) != 255) { a1 = v_rip + 5450764; }
    v_stack_m48 = a1;
    goto loc_008DC3A5;
loc_008DC524:
    v_stack_m50 = 7;
    v_stack_m48 = v_rip + 6372025;
    v_stack_m4C = 4;
    goto loc_008DC3A5;
loc_008DC542:
    if (a1 == 0) goto loc_008DC3C6;
    if (v_rip + 5450764 == 0) goto loc_008DC3C6;
    result = wcsicmp(a1, v_rip + 5450764, v_stack_m84, result);
    if ((unsigned int)(result) != 0) goto loc_008DC3C6;
    goto loc_008DC2CC;
}
```

## 5. (Beta) C Style

```c
int64_t ConstraintEval(int32_t Arg1, void *Arg2, void *Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x52E54F)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = (local_r12) * ((uint32_t)(Arg1));
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m80 = v_xmm0;
    if (((Arg4) & (0xFF00000ULL)) != 0) goto loc_008DC4AC;
    if (Arg1 == 0) goto loc_008DC4C0;
    result = ExAllocatePool2(256, local_r12, (uint32_t)(0x52544C46ULL), Arg4);
    if (result == 0) goto loc_008DC4CA;
    if (((*(uint32_t *)(arg2)) & (0xFF00000ULL)) != 0) goto loc_008DC453;
    result = memcpy(result, Arg2, local_r12, Arg4);
loc_008DC275:
    local_rdi = 0;
loc_008DC277:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_008DC2DF;
    Arg2 = (Arg2) * (0);
    if ((*(uint32_t *)(arg2 + result * 1 + 0x18)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_008DC31B;
loc_008DC290:
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_008DC277;
loc_008DC294:
    Arg1 = (*(uint64_t *)(arg2 + 0x8)) - (*(uint64_t *)(local_rdi + 0x8));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg2 + 0x10);
        Arg1 = (Arg1) - (*(uint64_t *)(local_rdi + 0x10));
    }
    if (Arg1 != 0) goto loc_008DC3C6;
    if ((*(uint32_t *)(arg2 + 0x1C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x1C))))) goto loc_008DC3C6;
    if ((*(uint64_t *)(arg2 + 0x20)) != (*(uint64_t *)(local_rdi + 0x20))) goto loc_008DC542;
loc_008DC2CC:
    Arg1 = (*(uint64_t *)(arg2 + 0x20)) * ((uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_008DC2DF:
loc_008DC2E4:
    result = ExFreePoolWithTag(result, (uint32_t)(0x52544C46ULL), local_r12, Arg4);
loc_008DC2F1:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x52544C46ULL), local_r12, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
loc_008DC31B:
    Arg1 = (*(uint64_t *)((uint32_t)(0x52544C46ULL) + result * 1 + 0x8)) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + result * 1))));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)((uint32_t)(0x52544C46ULL) + result * 1 + 0x10);
        Arg1 = (Arg1) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + result * 1)) + 0x8));
    }
    if (Arg1 != 0) goto loc_008DC290;
    if ((*(uint32_t *)((uint32_t)(0x52544C46ULL) + result * 1 + 0x1C)) != ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg1 + result * 1)) + 0x14))))) goto loc_008DC290;
    if ((*(uint64_t *)((uint32_t)(0x52544C46ULL) + result * 1 + 0x20)) != (*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + result * 1)) + 0x18))) goto loc_008DC4D4;
loc_008DC357:
    Arg1 = (*(uint64_t *)((uint32_t)(0x52544C46ULL) + result * 1 + 0x20)) * ((uint32_t)((uint32_t)(local_rdi)));
    if ((*(uint32_t *)(Arg1 + result * 1)) != ((uint32_t)(v_stack_p20))) goto loc_008DC290;
    local_rdi = (local_rdi) * ((uint32_t)((uint32_t)(local_rdi)));
    local_rdi = (local_rdi) + (result);
    if (condition_is_equal) goto loc_008DC2DF;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm0;
    local_rbx = (uint32_t)((v_stack_p20) - (1));
    if (condition_is_equal) goto loc_008DC524;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008DC46B;
loc_008DC3A5:
    local_rbx = 0;
loc_008DC3A7:
    if (0 >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_008DC3CA;
    Arg2 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + result * 1)) + 0x18)) * (0);
    Arg2 = (Arg2) + (result);
    if (Arg2 == local_rdi) goto loc_008DC3C6;
    if ((*(uint32_t *)(arg2 + 0x18)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18))))) goto loc_008DC294;
loc_008DC3C6:
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_008DC3A7;
loc_008DC3CA:
    v_stack_m80 = 1;
    v_stack_m78 = v_stack_m70;
    if (((uint32_t)((uint32_t)(Arg1))) < 1) goto loc_008DC4B6;
    v_stack_p20 = v_stack_m88;
    if (((*(uint32_t *)(result)) & (0xFF00000ULL)) == 0) goto loc_008DC4A2;
    result = FilterEvalStrict(v_rip + 1529389, v_stack_m80, (uint32_t)((uint32_t)((uint32_t)(Arg1))), result);
loc_008DC411:
    if (sign_flag) goto loc_008DC2E4;
    if (v_stack_m88 != 0) goto loc_008DC2DF;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm1;
    *(uint64_t *)(arg5 + 0x20) = v_xmm0;
    *(uint64_t *)(arg5 + 0x30) = v_xmm1;
    goto loc_008DC2E4;
loc_008DC453:
    result = SimplifyFilter((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_m80, v_stack_m84, result);
    goto loc_008DC275;
loc_008DC46B:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)((uint32_t)(0x10000ULL))));
    if (condition_is_equal) goto loc_008DC4F8;
    if (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_008DC2DF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x28)))) == 18) goto loc_008DC3A5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x28)))) == 25) goto loc_008DC3A5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x28)))) == 0x2012ULL) goto loc_008DC3A5;
    goto loc_008DC2DF;
loc_008DC4A2:
    result = FilterEvalImpliedAnd((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_m80, v_stack_m84, result);
    goto loc_008DC411;
loc_008DC4AC:
    goto loc_008DC2F1;
loc_008DC4B6:
    goto loc_008DC2E4;
loc_008DC4C0:
    goto loc_008DC2F1;
loc_008DC4CA:
    goto loc_008DC2F1;
loc_008DC4D4:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) == 0) goto loc_008DC290;
    if (v_stack_m80 == 0) goto loc_008DC290;
    result = wcsicmp((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_m80, v_stack_m84, result);
    if ((uint32_t)(result) != 0) goto loc_008DC290;
    goto loc_008DC357;
loc_008DC4F8:
    if (v_stack_m50 != 17) goto loc_008DC2DF;
    Arg1 = v_rip + 6372053;
    if ((*(uint8_t *)(v_stack_m48)) != 255) { Arg1 = v_rip + 5450764; }
    v_stack_m48 = Arg1;
    goto loc_008DC3A5;
loc_008DC524:
    v_stack_m50 = 7;
    v_stack_m48 = v_rip + 6372025;
    v_stack_m4C = 4;
    goto loc_008DC3A5;
loc_008DC542:
    if (Arg1 == 0) goto loc_008DC3C6;
    if (v_rip + 5450764 == 0) goto loc_008DC3C6;
    result = wcsicmp(Arg1, v_rip + 5450764, v_stack_m84, result);
    if ((uint32_t)(result) != 0) goto loc_008DC3C6;
    goto loc_008DC2CC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x14` | `32` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x10` | `128` | `R` |
| `Arg5` | `+ 0x20` | `128` | `R` |
| `Arg5` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DC1D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
