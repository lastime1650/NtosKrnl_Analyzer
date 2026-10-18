# IoSteerInterrupt

- RVA: `0x007270F0`–`0x007273E1` (길이 `753` bytes)
- VA: `0x00000001407270F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C832C`
- 디코드: `208`개 명령, `753/753` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0072712E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0072720A` → [KeIntSteerAssignCpuSet](../../text/5C/KeIntSteerAssignCpuSet_function_005C5668.md) (function, `0x005C5668`)
- `0x0072722F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00727245` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0072725D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00727272` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007272A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007272B2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007272BF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007272FE` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0072732A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00727387` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007273BB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007273D4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0072712E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0072720A` → [KeIntSteerAssignCpuSet](../../text/5C/KeIntSteerAssignCpuSet_function_005C5668.md) (`PAGE` → `.text`)
  - `0x0072722F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00727245` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0072725D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00727272` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007272A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007272B2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007272BF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007272FE` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0072732A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00727387` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007273BB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007273D4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007270F0  4C 8B DC                        mov r11, rsp
007270F3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007270F7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
007270FB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
007270FF  57                              push rdi
00727100  48 83 EC 30                     sub rsp, 0x30
00727104  48 8B D9                        mov rbx, rcx
00727107  41 B8 01 00 00 C0               mov r8d, 0xc0000001
0072710D  44 0F 20 C0                     mov rax, cr8
00727111  33 F6                           xor esi, esi
00727113  84 C0                           test al, al
00727115  74 1D                           je 0x140727134
00727117  44 0F 20 C0                     mov rax, cr8
0072711B  44 0F B6 C0                     movzx r8d, al
0072711F  8D 56 01                        lea edx, [rsi + 1]
00727122  45 33 C9                        xor r9d, r9d
00727125  49 89 73 E8                     mov qword ptr [r11 - 0x18], rsi
00727129  B9 21 01 00 00                  mov ecx, 0x121
0072712E  E8 2D 65 DD FF                  call 0x1404fd660
00727133  CC                              int3
00727134  48 85 DB                        test rbx, rbx
00727137  0F 84 9D 02 00 00               je 0x1407273da
0072713D  48 85 D2                        test rdx, rdx
00727140  0F 84 94 02 00 00               je 0x1407273da
00727146  39 31                           cmp dword ptr [rcx], esi
00727148  74 0B                           je 0x140727155
0072714A  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00727150  E9 BD 00 00 00                  jmp 0x140727212
00727155  44 8B 0A                        mov r9d, dword ptr [rdx]
00727158  BD 02 00 00 00                  mov ebp, 2
0072715D  44 3B CD                        cmp r9d, ebp
00727160  7D E8                           jge 0x14072714a
00727162  41 83 F9 01                     cmp r9d, 1
00727166  75 06                           jne 0x14072716e
00727168  48 39 72 10                     cmp qword ptr [rdx + 0x10], rsi
0072716C  74 DC                           je 0x14072714a
0072716E  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00727172  48 85 C9                        test rcx, rcx
00727175  0F 84 45 02 00 00               je 0x1407273c0
0072717B  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00727182  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00727186  48 85 C0                        test rax, rax
00727189  0F 84 9C 00 00 00               je 0x14072722b
0072718F  F7 80 8C 01 00 00 00 00 02 00   test dword ptr [rax + 0x18c], 0x20000
00727199  0F 85 8C 00 00 00               jne 0x14072722b
0072719F  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
007271A2  83 E9 01                        sub ecx, 1
007271A5  74 32                           je 0x1407271d9
007271A7  83 E9 01                        sub ecx, 1
007271AA  74 1C                           je 0x1407271c8
007271AC  83 E9 01                        sub ecx, 1
007271AF  74 0D                           je 0x1407271be
007271B1  83 F9 01                        cmp ecx, 1
007271B4  74 23                           je 0x1407271d9
007271B6  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
007271BC  EB 54                           jmp 0x140727212
007271BE  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
007271C2  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
007271C6  EB 15                           jmp 0x1407271dd
007271C8  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
007271CC  48 8B 80 28 01 00 00            mov rax, qword ptr [rax + 0x128]
007271D3  48 83 C0 70                     add rax, 0x70
007271D7  EB 04                           jmp 0x1407271dd
007271D9  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
007271DD  48 8B 88 88 01 00 00            mov rcx, qword ptr [rax + 0x188]
007271E4  8B 40 58                        mov eax, dword ptr [rax + 0x58]
007271E7  39 41 58                        cmp dword ptr [rcx + 0x58], eax
007271EA  0F 85 EA 01 00 00               jne 0x1407273da
007271F0  41 83 F9 01                     cmp r9d, 1
007271F4  75 0A                           jne 0x140727200
007271F6  4C 8B 42 10                     mov r8, qword ptr [rdx + 0x10]
007271FA  0F B7 52 08                     movzx edx, word ptr [rdx + 8]
007271FE  EB 0A                           jmp 0x14072720a
00727200  45 85 C9                        test r9d, r9d
00727203  75 0D                           jne 0x140727212
00727205  33 D2                           xor edx, edx
00727207  45 33 C0                        xor r8d, r8d
0072720A  E8 59 E4 E9 FF                  call 0x1405c5668
0072720F  44 8B C0                        mov r8d, eax
00727212  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00727217  41 8B C0                        mov eax, r8d
0072721A  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0072721F  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00727224  48 83 C4 30                     add rsp, 0x30
00727228  5F                              pop rdi
00727229  C3                              ret
0072722A  CC                              int3
0072722B  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
0072722F  E8 40 11 D0 FF                  call 0x140428374
00727234  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00727238  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0072723C  48 85 C9                        test rcx, rcx
0072723F  74 36                           je 0x140727277
00727241  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00727245  E8 2A 11 D0 FF                  call 0x140428374
0072724A  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0072724E  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00727252  48 83 C1 38                     add rcx, 0x38
00727256  66 39 31                        cmp word ptr [rcx], si
00727259  74 1C                           je 0x140727277
0072725B  8B D5                           mov edx, ebp
0072725D  E8 12 11 D0 FF                  call 0x140428374
00727262  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00727266  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0072726A  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
0072726E  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00727272  E8 FD 10 D0 FF                  call 0x140428374
00727277  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0072727B  48 85 C9                        test rcx, rcx
0072727E  0F 84 3C 01 00 00               je 0x1407273c0
00727284  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
0072728B  48 39 70 28                     cmp qword ptr [rax + 0x28], rsi
0072728F  0F 84 2B 01 00 00               je 0x1407273c0
00727295  48 8B 78 28                     mov rdi, qword ptr [rax + 0x28]
00727299  BA 88 03 00 00                  mov edx, 0x388
0072729E  48 8B CF                        mov rcx, rdi
007272A1  E8 CE 10 D0 FF                  call 0x140428374
007272A6  66 39 77 28                     cmp word ptr [rdi + 0x28], si
007272AA  74 18                           je 0x1407272c4
007272AC  8B D5                           mov edx, ebp
007272AE  48 8D 4F 28                     lea rcx, [rdi + 0x28]
007272B2  E8 BD 10 D0 FF                  call 0x140428374
007272B7  0F B7 57 28                     movzx edx, word ptr [rdi + 0x28]
007272BB  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
007272BF  E8 B0 10 D0 FF                  call 0x140428374
007272C4  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
007272C8  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
007272CF  48 85 D2                        test rdx, rdx
007272D2  74 09                           je 0x1407272dd
007272D4  48 8B 01                        mov rax, qword ptr [rcx]
007272D7  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
007272DB  EB 03                           jmp 0x1407272e0
007272DD  4C 8B C6                        mov r8, rsi
007272E0  66 41 39 70 38                  cmp word ptr [r8 + 0x38], si
007272E5  74 48                           je 0x14072732f
007272E7  48 85 D2                        test rdx, rdx
007272EA  74 09                           je 0x1407272f5
007272EC  48 8B 01                        mov rax, qword ptr [rcx]
007272EF  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007272F3  EB 03                           jmp 0x1407272f8
007272F5  48 8B CE                        mov rcx, rsi
007272F8  48 83 C1 38                     add rcx, 0x38
007272FC  8B D5                           mov edx, ebp
007272FE  E8 71 10 D0 FF                  call 0x140428374
00727303  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00727307  48 85 C9                        test rcx, rcx
0072730A  74 10                           je 0x14072731c
0072730C  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00727313  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
00727317  48 8B CA                        mov rcx, rdx
0072731A  EB 06                           jmp 0x140727322
0072731C  48 8B D6                        mov rdx, rsi
0072731F  48 8B CE                        mov rcx, rsi
00727322  0F B7 52 38                     movzx edx, word ptr [rdx + 0x38]
00727326  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
0072732A  E8 45 10 D0 FF                  call 0x140428374
0072732F  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00727333  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
0072733A  48 85 D2                        test rdx, rdx
0072733D  74 09                           je 0x140727348
0072733F  48 8B 01                        mov rax, qword ptr [rcx]
00727342  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00727346  EB 03                           jmp 0x14072734b
00727348  4C 8B C6                        mov r8, rsi
0072734B  49 39 70 10                     cmp qword ptr [r8 + 0x10], rsi
0072734F  74 6F                           je 0x1407273c0
00727351  48 85 D2                        test rdx, rdx
00727354  74 09                           je 0x14072735f
00727356  48 8B 01                        mov rax, qword ptr [rcx]
00727359  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0072735D  EB 03                           jmp 0x140727362
0072735F  48 8B C6                        mov rax, rsi
00727362  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00727366  66 39 70 38                     cmp word ptr [rax + 0x38], si
0072736A  74 54                           je 0x1407273c0
0072736C  48 85 D2                        test rdx, rdx
0072736F  74 09                           je 0x14072737a
00727371  48 8B 01                        mov rax, qword ptr [rcx]
00727374  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00727378  EB 03                           jmp 0x14072737d
0072737A  48 8B CE                        mov rcx, rsi
0072737D  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00727381  8B D5                           mov edx, ebp
00727383  48 83 C1 38                     add rcx, 0x38
00727387  E8 E8 0F D0 FF                  call 0x140428374
0072738C  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00727390  48 85 C9                        test rcx, rcx
00727393  74 10                           je 0x1407273a5
00727395  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
0072739C  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
007273A0  48 8B CA                        mov rcx, rdx
007273A3  EB 06                           jmp 0x1407273ab
007273A5  48 8B D6                        mov rdx, rsi
007273A8  48 8B CE                        mov rcx, rsi
007273AB  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
007273AF  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007273B3  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
007273B7  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
007273BB  E8 B4 0F D0 FF                  call 0x140428374
007273C0  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
007273C4  45 33 C9                        xor r9d, r9d
007273C7  48 8B D5                        mov rdx, rbp
007273CA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007273CF  B9 CA 00 00 00                  mov ecx, 0xca
007273D4  E8 87 62 DD FF                  call 0x1404fd660
007273D9  CC                              int3
007273DA  B9 05 00 00 00                  mov ecx, 5
007273DF  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSteerInterrupt(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rsi = 0;
    result = v_cr8;
    if ((unsigned __int8)(v_cr8) != 0) {
        result = v_cr8;
        a3 = (unsigned __int8)(result);
        a2 = v_rsi + 1;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 24) = 0;
        a1 = 289;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (a1 == 0) goto loc_007273DA;
    if (a2 == 0) goto loc_007273DA;
    if ((*(unsigned int *)(a1)) == 0) goto loc_00727155;
loc_0072714A:
    goto loc_00727212;
loc_00727155:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) >= 2) goto loc_0072714A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) != 1) goto loc_0072716E;
    if ((*(unsigned __int64 *)(a2 + 16)) == 0) goto loc_0072714A;
loc_0072716E:
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_007273C0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 312) + 40) == 0) goto loc_0072722B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 312) + 40) + 396)) & (0x20000ULL)) != 0) goto loc_0072722B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - (1));
    if (condition_is_equal) goto loc_007271D9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_007271C8;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_007271BE;
    if (((unsigned int)(a1)) == 1) goto loc_007271D9;
    goto loc_00727212;
loc_007271BE:
    goto loc_007271DD;
loc_007271C8:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 296)) + (112);
    goto loc_007271DD;
loc_007271D9:
loc_007271DD:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 392) + 88)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 88))))) goto loc_007273DA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) != 1) goto loc_00727200;
    goto loc_0072720A;
loc_00727200:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) != 0) goto loc_00727212;
    a2 = 0;
    a3 = 0;
loc_0072720A:
    result = KeIntSteerAssignCpuSet(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 392), a2, a3, (unsigned int)(*(unsigned int *)(a2)));
loc_00727212:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0072722B:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 392), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 392) + 2), (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 8) == 0) goto loc_00727277;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 8) + 2)), (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 8)) + (56);
    result = *(unsigned __int64 *)(v_stack_p8 + 16);
    if ((*(unsigned __int16 *)(a1)) != ((unsigned __int16)(v_stack_p18))) {
        a2 = (unsigned int)(v_stack_p10);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
        result = *(unsigned __int64 *)(v_stack_p8 + 16);
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
    }
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_007273C0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40)) == v_stack_p18) goto loc_007273C0;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40), 904, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40) + 40)) != ((unsigned __int16)(v_stack_p18))) {
        a2 = (unsigned int)(v_stack_p10);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 312) + 40) + 48);
        result = IoAddTriageDumpDataBlock(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a2)));
    }
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_007272DD;
    goto loc_007272E0;
loc_007272DD:
loc_007272E0:
    if ((*(unsigned __int16 *)(v_stack_p18 + 56)) == ((unsigned __int16)(v_stack_p18))) goto loc_0072732F;
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_007272F5;
    goto loc_007272F8;
loc_007272F5:
loc_007272F8:
    a1 = (v_stack_p18) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_stack_p10)), v_stack_p18, (unsigned int)(*(unsigned int *)(a2)));
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_0072731C;
    goto loc_00727322;
loc_0072731C:
loc_00727322:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_stack_p18 + 64), *(unsigned __int16 *)(v_stack_p18 + 56), v_stack_p18, (unsigned int)(*(unsigned int *)(a2)));
loc_0072732F:
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_00727348;
    goto loc_0072734B;
loc_00727348:
loc_0072734B:
    if ((*(unsigned __int64 *)(v_stack_p18 + 16)) == v_stack_p18) goto loc_007273C0;
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_0072735F;
    goto loc_00727362;
loc_0072735F:
loc_00727362:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 16) + 56)) == ((unsigned __int16)(v_stack_p18))) goto loc_007273C0;
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_0072737A;
    goto loc_0072737D;
loc_0072737A:
loc_0072737D:
    a1 = (*(unsigned __int64 *)(v_stack_p18 + 16)) + (56);
    result = IoAddTriageDumpDataBlock(a1, (unsigned int)((unsigned int)(v_stack_p10)), v_stack_p18, (unsigned int)(*(unsigned int *)(a2)));
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_007273A5;
    goto loc_007273AB;
loc_007273A5:
loc_007273AB:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 16) + 56), v_stack_p18, (unsigned int)(*(unsigned int *)(a2)));
loc_007273C0:
    a4 = 0;
    v_stack_p20 = v_stack_p18;
    result = KeBugCheckEx(202, v_stack_p10, *(unsigned __int64 *)(v_stack_p8 + 16), a4);
loc_007273DA:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoSteerInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rsi = 0;
    result = v_cr8;
    if ((uint8_t)(v_cr8) != 0) {
        result = v_cr8;
        Arg3 = (uint8_t)(result);
        Arg2 = local_rsi + 1;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x18) = 0;
        Arg1 = 289;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg1 == 0) goto loc_007273DA;
    if (Arg2 == 0) goto loc_007273DA;
    if ((*(uint32_t *)(Arg1)) == 0) goto loc_00727155;
loc_0072714A:
    goto loc_00727212;
loc_00727155:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) >= 2) goto loc_0072714A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) != 1) goto loc_0072716E;
    if ((*(uint64_t *)(Arg2 + 0x10)) == 0) goto loc_0072714A;
loc_0072716E:
    if (*(uint64_t *)(Arg1 + 0x10) == 0) goto loc_007273C0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x10) + 0x138) + 0x28) == 0) goto loc_0072722B;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x10) + 0x138) + 0x28) + 0x18C)) & (0x20000ULL)) != 0) goto loc_0072722B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x8))) - (1));
    if (condition_is_equal) goto loc_007271D9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_007271C8;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_007271BE;
    if (((uint32_t)(Arg1)) == 1) goto loc_007271D9;
    goto loc_00727212;
loc_007271BE:
    goto loc_007271DD;
loc_007271C8:
    result = (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x128)) + (112);
    goto loc_007271DD;
loc_007271D9:
loc_007271DD:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x188) + 0x58)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x58))))) goto loc_007273DA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) != 1) goto loc_00727200;
    goto loc_0072720A;
loc_00727200:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) != 0) goto loc_00727212;
    Arg2 = 0;
    Arg3 = 0;
loc_0072720A:
    result = KeIntSteerAssignCpuSet(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x188), Arg2, Arg3, (uint32_t)(*(uint32_t *)(Arg2)));
loc_00727212:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0072722B:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x188), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x188) + 0x2), (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x8) == 0) goto loc_00727277;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x8) + 0x2)), (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x8)) + (56);
    result = *(uint64_t *)(v_stack_p8 + 0x10);
    if ((*(uint16_t *)(Arg1)) != ((uint16_t)(v_stack_p18))) {
        Arg2 = (uint32_t)(v_stack_p10);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
        result = *(uint64_t *)(v_stack_p8 + 0x10);
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = *(uint16_t *)(Arg1 + 0x38);
        Arg1 = *(uint64_t *)(Arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
    }
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_007273C0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28)) == v_stack_p18) goto loc_007273C0;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28), 904, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28) + 0x28)) != ((uint16_t)(v_stack_p18))) {
        Arg2 = (uint32_t)(v_stack_p10);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x138) + 0x28) + 0x30);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(Arg2)));
    }
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_007272DD;
    goto loc_007272E0;
loc_007272DD:
loc_007272E0:
    if ((*(uint16_t *)(v_stack_p18 + 0x38)) == ((uint16_t)(v_stack_p18))) goto loc_0072732F;
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_007272F5;
    goto loc_007272F8;
loc_007272F5:
loc_007272F8:
    Arg1 = (v_stack_p18) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(v_stack_p10)), v_stack_p18, (uint32_t)(*(uint32_t *)(Arg2)));
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_0072731C;
    goto loc_00727322;
loc_0072731C:
loc_00727322:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_stack_p18 + 0x40), *(uint16_t *)(v_stack_p18 + 0x38), v_stack_p18, (uint32_t)(*(uint32_t *)(Arg2)));
loc_0072732F:
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_00727348;
    goto loc_0072734B;
loc_00727348:
loc_0072734B:
    if ((*(uint64_t *)(v_stack_p18 + 0x10)) == v_stack_p18) goto loc_007273C0;
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_0072735F;
    goto loc_00727362;
loc_0072735F:
loc_00727362:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x10) + 0x38)) == ((uint16_t)(v_stack_p18))) goto loc_007273C0;
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_0072737A;
    goto loc_0072737D;
loc_0072737A:
loc_0072737D:
    Arg1 = (*(uint64_t *)(v_stack_p18 + 0x10)) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)((uint32_t)(v_stack_p10)), v_stack_p18, (uint32_t)(*(uint32_t *)(Arg2)));
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_007273A5;
    goto loc_007273AB;
loc_007273A5:
loc_007273AB:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x10) + 0x38), v_stack_p18, (uint32_t)(*(uint32_t *)(Arg2)));
loc_007273C0:
    Arg4 = 0;
    v_stack_p20 = v_stack_p18;
    result = KeBugCheckEx(202, v_stack_p10, *(uint64_t *)(v_stack_p8 + 0x10), Arg4);
loc_007273DA:
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007270F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
