# AuthzBasepValidateSecurityAttributes

- RVA: `0x003A90EC`–`0x003A9396` (길이 `682` bytes)
- VA: `0x00000001403A90EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00089EF0`
- 디코드: `180`개 명령, `682/682` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AuthzBasepSetSecurityAttributesToken](AuthzBasepSetSecurityAttributesToken_function_003A8D1C.md) at `0x003A8D4C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003A9378` → [sub_006E6B16](../6E/Unknown_function_006E6B16.md) (`tail-transfer`)
  - `0x003A9389` → [sub_006E6B16](../6E/Unknown_function_006E6B16.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003A90EC  48 8B C4                        mov rax, rsp
003A90EF  48 89 58 08                     mov qword ptr [rax + 8], rbx
003A90F3  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
003A90F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
003A90FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
003A90FF  41 54                           push r12
003A9101  41 55                           push r13
003A9103  41 56                           push r14
003A9105  41 57                           push r15
003A9107  45 33 ED                        xor r13d, r13d
003A910A  4C 8B E2                        mov r12, rdx
003A910D  45 8B C5                        mov r8d, r13d
003A9110  41 8D 7D 01                     lea edi, [r13 + 1]
003A9114  66 39 39                        cmp word ptr [rcx], di
003A9117  0F 85 41 02 00 00               jne 0x1403a935e
003A911D  44 8B 3A                        mov r15d, dword ptr [rdx]
003A9120  66 44 39 69 02                  cmp word ptr [rcx + 2], r13w
003A9125  0F 85 33 02 00 00               jne 0x1403a935e
003A912B  8B 69 04                        mov ebp, dword ptr [rcx + 4]
003A912E  44 3B FF                        cmp r15d, edi
003A9131  0F 84 0E 02 00 00               je 0x1403a9345
003A9137  85 ED                           test ebp, ebp
003A9139  0F 84 1F 02 00 00               je 0x1403a935e
003A913F  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
003A9143  4D 85 C9                        test r9, r9
003A9146  0F 84 12 02 00 00               je 0x1403a935e
003A914C  45 8B F5                        mov r14d, r13d
003A914F  BA 0D 00 00 C0                  mov edx, 0xc000000d
003A9154  44 3B F5                        cmp r14d, ebp
003A9157  73 62                           jae 0x1403a91bb
003A9159  41 8B C6                        mov eax, r14d
003A915C  4C 8D 14 80                     lea r10, [rax + rax*4]
003A9160  66 47 39 2C D1                  cmp word ptr [r9 + r10*8], r13w
003A9165  74 51                           je 0x1403a91b8
003A9167  66 47 39 6C D1 02               cmp word ptr [r9 + r10*8 + 2], r13w
003A916D  74 49                           je 0x1403a91b8
003A916F  4F 39 6C D1 08                  cmp qword ptr [r9 + r10*8 + 8], r13
003A9174  74 42                           je 0x1403a91b8
003A9176  66 47 39 6C D1 12               cmp word ptr [r9 + r10*8 + 0x12], r13w
003A917C  75 3A                           jne 0x1403a91b8
003A917E  43 F7 44 D1 14 00 FF 00 00      test dword ptr [r9 + r10*8 + 0x14], 0xff00
003A9187  75 2F                           jne 0x1403a91b8
003A9189  45 85 F6                        test r14d, r14d
003A918C  0F 85 AC 00 00 00               jne 0x1403a923e
003A9192  44 3B FF                        cmp r15d, edi
003A9195  0F 84 7D 01 00 00               je 0x1403a9318
003A919B  43 0F B7 4C D1 10               movzx ecx, word ptr [r9 + r10*8 + 0x10]
003A91A1  83 E9 01                        sub ecx, 1
003A91A4  75 36                           jne 0x1403a91dc
003A91A6  47 39 6C D1 18                  cmp dword ptr [r9 + r10*8 + 0x18], r13d
003A91AB  0F 84 80 00 00 00               je 0x1403a9231
003A91B1  4F 39 6C D1 20                  cmp qword ptr [r9 + r10*8 + 0x20], r13
003A91B6  75 79                           jne 0x1403a9231
003A91B8  44 8B C2                        mov r8d, edx
003A91BB  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
003A91C0  41 8B C0                        mov eax, r8d
003A91C3  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
003A91C8  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003A91CD  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
003A91D2  41 5F                           pop r15
003A91D4  41 5E                           pop r14
003A91D6  41 5D                           pop r13
003A91D8  41 5C                           pop r12
003A91DA  C3                              ret
003A91DB  CC                              int3
003A91DC  83 E9 01                        sub ecx, 1
003A91DF  74 C5                           je 0x1403a91a6
003A91E1  83 E9 01                        sub ecx, 1
003A91E4  75 78                           jne 0x1403a925e
003A91E6  43 8B 7C D1 18                  mov edi, dword ptr [r9 + r10*8 + 0x18]
003A91EB  85 FF                           test edi, edi
003A91ED  0F 85 C0 00 00 00               jne 0x1403a92b3
003A91F3  41 8B C5                        mov eax, r13d
003A91F6  3B C7                           cmp eax, edi
003A91F8  73 32                           jae 0x1403a922c
003A91FA  4F 8B 5C D1 20                  mov r11, qword ptr [r9 + r10*8 + 0x20]
003A91FF  8B C8                           mov ecx, eax
003A9201  48 03 C9                        add rcx, rcx
003A9204  41 0F B7 34 CB                  movzx esi, word ptr [r11 + rcx*8]
003A9209  66 85 F6                        test si, si
003A920C  74 1B                           je 0x1403a9229
003A920E  41 0F B7 5C CB 02               movzx ebx, word ptr [r11 + rcx*8 + 2]
003A9214  66 85 DB                        test bx, bx
003A9217  74 10                           je 0x1403a9229
003A9219  66 3B F3                        cmp si, bx
003A921C  77 0B                           ja 0x1403a9229
003A921E  4D 39 6C CB 08                  cmp qword ptr [r11 + rcx*8 + 8], r13
003A9223  74 04                           je 0x1403a9229
003A9225  FF C0                           inc eax
003A9227  EB CD                           jmp 0x1403a91f6
003A9229  44 8B C2                        mov r8d, edx
003A922C  BF 01 00 00 00                  mov edi, 1
003A9231  45 85 C0                        test r8d, r8d
003A9234  78 85                           js 0x1403a91bb
003A9236  44 03 F7                        add r14d, edi
003A9239  E9 16 FF FF FF                  jmp 0x1403a9154
003A923E  44 3B FF                        cmp r15d, edi
003A9241  0F 84 54 FF FF FF               je 0x1403a919b
003A9247  41 8B C6                        mov eax, r14d
003A924A  41 8B 0C 84                     mov ecx, dword ptr [r12 + rax*4]
003A924E  3B CF                           cmp ecx, edi
003A9250  0F 84 62 FF FF FF               je 0x1403a91b8
003A9256  83 F9 02                        cmp ecx, 2
003A9259  E9 37 FF FF FF                  jmp 0x1403a9195
003A925E  83 E9 01                        sub ecx, 1
003A9261  74 60                           je 0x1403a92c3
003A9263  83 E9 01                        sub ecx, 1
003A9266  74 12                           je 0x1403a927a
003A9268  83 E9 01                        sub ecx, 1
003A926B  0F 84 00 01 00 00               je 0x1403a9371
003A9271  83 F9 0A                        cmp ecx, 0xa
003A9274  0F 85 3E FF FF FF               jne 0x1403a91b8
003A927A  47 8B 5C D1 18                  mov r11d, dword ptr [r9 + r10*8 + 0x18]
003A927F  45 85 DB                        test r11d, r11d
003A9282  0F 85 A0 00 00 00               jne 0x1403a9328
003A9288  41 8B C5                        mov eax, r13d
003A928B  41 3B C3                        cmp eax, r11d
003A928E  73 A1                           jae 0x1403a9231
003A9290  4B 8B 5C D1 20                  mov rbx, qword ptr [r9 + r10*8 + 0x20]
003A9295  8B C8                           mov ecx, eax
003A9297  48 03 C9                        add rcx, rcx
003A929A  44 39 6C CB 08                  cmp dword ptr [rbx + rcx*8 + 8], r13d
003A929F  0F 84 E9 00 00 00               je 0x1403a938e
003A92A5  4C 39 2C CB                     cmp qword ptr [rbx + rcx*8], r13
003A92A9  0F 84 DF 00 00 00               je 0x1403a938e
003A92AF  03 C7                           add eax, edi
003A92B1  EB D8                           jmp 0x1403a928b
003A92B3  4F 39 6C D1 20                  cmp qword ptr [r9 + r10*8 + 0x20], r13
003A92B8  0F 85 35 FF FF FF               jne 0x1403a91f3
003A92BE  E9 F5 FE FF FF                  jmp 0x1403a91b8
003A92C3  43 8B 7C D1 18                  mov edi, dword ptr [r9 + r10*8 + 0x18]
003A92C8  85 FF                           test edi, edi
003A92CA  75 6C                           jne 0x1403a9338
003A92CC  41 8B CD                        mov ecx, r13d
003A92CF  3B CF                           cmp ecx, edi
003A92D1  0F 83 55 FF FF FF               jae 0x1403a922c
003A92D7  8B C1                           mov eax, ecx
003A92D9  4C 8D 1C 40                     lea r11, [rax + rax*2]
003A92DD  4B 8B 44 D1 20                  mov rax, qword ptr [r9 + r10*8 + 0x20]
003A92E2  42 0F B7 74 D8 08               movzx esi, word ptr [rax + r11*8 + 8]
003A92E8  66 85 F6                        test si, si
003A92EB  0F 84 38 FF FF FF               je 0x1403a9229
003A92F1  42 0F B7 5C D8 0A               movzx ebx, word ptr [rax + r11*8 + 0xa]
003A92F7  66 85 DB                        test bx, bx
003A92FA  0F 84 29 FF FF FF               je 0x1403a9229
003A9300  66 3B F3                        cmp si, bx
003A9303  0F 87 20 FF FF FF               ja 0x1403a9229
003A9309  4E 39 6C D8 10                  cmp qword ptr [rax + r11*8 + 0x10], r13
003A930E  0F 84 15 FF FF FF               je 0x1403a9229
003A9314  FF C1                           inc ecx
003A9316  EB B7                           jmp 0x1403a92cf
003A9318  47 39 6C D1 18                  cmp dword ptr [r9 + r10*8 + 0x18], r13d
003A931D  0F 84 95 FE FF FF               je 0x1403a91b8
003A9323  E9 73 FE FF FF                  jmp 0x1403a919b
003A9328  4F 39 6C D1 20                  cmp qword ptr [r9 + r10*8 + 0x20], r13
003A932D  0F 85 55 FF FF FF               jne 0x1403a9288
003A9333  E9 80 FE FF FF                  jmp 0x1403a91b8
003A9338  4F 39 6C D1 20                  cmp qword ptr [r9 + r10*8 + 0x20], r13
003A933D  0F 84 75 FE FF FF               je 0x1403a91b8
003A9343  EB 87                           jmp 0x1403a92cc
003A9345  85 ED                           test ebp, ebp
003A9347  74 20                           je 0x1403a9369
003A9349  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
003A934D  4D 85 C9                        test r9, r9
003A9350  0F 85 F6 FD FF FF               jne 0x1403a914c
003A9356  85 ED                           test ebp, ebp
003A9358  0F 84 EE FD FF FF               je 0x1403a914c
003A935E  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
003A9364  E9 52 FE FF FF                  jmp 0x1403a91bb
003A9369  4C 39 69 08                     cmp qword ptr [rcx + 8], r13
003A936D  75 EF                           jne 0x1403a935e
003A936F  EB D8                           jmp 0x1403a9349
003A9371  43 8B 5C D1 18                  mov ebx, dword ptr [r9 + r10*8 + 0x18]
003A9376  85 DB                           test ebx, ebx
003A9378  0F 84 98 D7 33 00               je 0x1406e6b16
003A937E  4F 39 6C D1 20                  cmp qword ptr [r9 + r10*8 + 0x20], r13
003A9383  0F 84 2F FE FF FF               je 0x1403a91b8
003A9389  E9 88 D7 33 00                  jmp 0x1406e6b16
003A938E  44 8B C2                        mov r8d, edx
003A9391  E9 9B FE FF FF                  jmp 0x1403a9231
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepValidateSecurityAttributes(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_r13 = 0;
    if ((*(unsigned __int16 *)(a1)) != ((unsigned __int16)(v_r13 + 1))) goto loc_003A935E;
    if ((*(unsigned __int16 *)(a1 + 2)) != 0) goto loc_003A935E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == ((unsigned int)(v_r13 + 1))) goto loc_003A9345;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) == 0) goto loc_003A935E;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_003A935E;
loc_003A914C:
loc_003A9154:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_003A91BB;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8)) == 0) goto loc_003A91B8;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 2)) == 0) goto loc_003A91B8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 8)) == 0) goto loc_003A91B8;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 18)) != 0) goto loc_003A91B8;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 20)) & (0xFF00ULL)) != 0) goto loc_003A91B8;
    if (0 != 0) goto loc_003A923E;
loc_003A9195:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == ((unsigned int)(v_r13 + 1))) goto loc_003A9318;
loc_003A919B:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 16)) - (1));
    if (condition_is_not_equal) goto loc_003A91DC;
loc_003A91A6:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24)) == 0) goto loc_003A9231;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32)) != 0) goto loc_003A9231;
loc_003A91B8:
loc_003A91BB:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))));
loc_003A91DC:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_003A91A6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_003A925E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))) != 0) goto loc_003A92B3;
loc_003A91F3:
loc_003A91F6:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))))) goto loc_003A922C;
    a1 = (0) + (0);
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8)) == 0) goto loc_003A9229;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8 + 2)) == 0) goto loc_003A9229;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8))) > ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8 + 2)))) goto loc_003A9229;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8 + 8)) == 0) goto loc_003A9229;
    result = (unsigned int)((0) + 1);
    goto loc_003A91F6;
loc_003A9229:
loc_003A922C:
loc_003A9231:
    if (sign_flag) goto loc_003A91BB;
    v_r14 = (unsigned int)((0) + (1));
    goto loc_003A9154;
loc_003A923E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == 1) goto loc_003A919B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)(v_r14)) * 4)))) == 1) goto loc_003A91B8;
    goto loc_003A9195;
loc_003A925E:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)(v_r14)) * 4))) - (1));
    if (condition_is_equal) goto loc_003A92C3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_003A927A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_003A9371;
    if (((unsigned int)(a1)) != 10) goto loc_003A91B8;
loc_003A927A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))) != 0) goto loc_003A9328;
loc_003A9288:
loc_003A928B:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))))) goto loc_003A9231;
    a1 = (0) + (0);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8 + 8)) == 0) goto loc_003A938E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + a1 * 8)) == 0) goto loc_003A938E;
    result = (unsigned int)((0) + (1));
    goto loc_003A928B;
loc_003A92B3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32)) != 0) goto loc_003A91F3;
    goto loc_003A91B8;
loc_003A92C3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))) != 0) goto loc_003A9338;
loc_003A92CC:
loc_003A92CF:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24))))) goto loc_003A922C;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + 0 + 0 * 2 * 8 + 8)) == 0) goto loc_003A9229;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + 0 + 0 * 2 * 8 + 10)) == 0) goto loc_003A9229;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + 0 + 0 * 2 * 8 + 8))) > ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + 0 + 0 * 2 * 8 + 10)))) goto loc_003A9229;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32) + 0 + 0 * 2 * 8 + 16)) == 0) goto loc_003A9229;
    a1 = (unsigned int)((0) + 1);
    goto loc_003A92CF;
loc_003A9318:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 24)) == 0) goto loc_003A91B8;
    goto loc_003A919B;
loc_003A9328:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32)) != 0) goto loc_003A9288;
    goto loc_003A91B8;
loc_003A9338:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32)) == 0) goto loc_003A91B8;
    goto loc_003A92CC;
loc_003A9345:
    if ((unsigned int)(v_stack_p10) == 0) goto loc_003A9369;
loc_003A9349:
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_003A914C;
    if ((unsigned int)(v_stack_p10) == 0) goto loc_003A914C;
loc_003A935E:
    goto loc_003A91BB;
loc_003A9369:
    if ((*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_003A935E;
    goto loc_003A9349;
loc_003A9371:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 0 + 0 * 4 * 8 + 32)) == 0) goto loc_003A91B8;
loc_003A938E:
    goto loc_003A9231;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepValidateSecurityAttributes(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_r13 = 0;
    if ((*(uint16_t *)(arg1)) != ((uint16_t)(local_r13 + 1))) goto loc_003A935E;
    if ((*(uint16_t *)(arg1 + 0x2)) != 0) goto loc_003A935E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) == ((uint32_t)(local_r13 + 1))) goto loc_003A9345;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) == 0) goto loc_003A935E;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_003A935E;
loc_003A914C:
loc_003A9154:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_003A91BB;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8)) == 0) goto loc_003A91B8;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x2)) == 0) goto loc_003A91B8;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x8)) == 0) goto loc_003A91B8;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x12)) != 0) goto loc_003A91B8;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x14)) & (0xFF00ULL)) != 0) goto loc_003A91B8;
    if (0 != 0) goto loc_003A923E;
loc_003A9195:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) == ((uint32_t)(local_r13 + 1))) goto loc_003A9318;
loc_003A919B:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x10)) - (1));
    if (condition_is_not_equal) goto loc_003A91DC;
loc_003A91A6:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18)) == 0) goto loc_003A9231;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20)) != 0) goto loc_003A9231;
loc_003A91B8:
loc_003A91BB:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
loc_003A91DC:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_003A91A6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_003A925E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))) != 0) goto loc_003A92B3;
loc_003A91F3:
loc_003A91F6:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))))) goto loc_003A922C;
    Arg1 = (0) + (0);
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8)) == 0) goto loc_003A9229;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8 + 0x2)) == 0) goto loc_003A9229;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8))) > ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8 + 0x2)))) goto loc_003A9229;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8 + 0x8)) == 0) goto loc_003A9229;
    result = (uint32_t)((0) + 1);
    goto loc_003A91F6;
loc_003A9229:
loc_003A922C:
loc_003A9231:
    if (sign_flag) goto loc_003A91BB;
    local_r14 = (uint32_t)((0) + (1));
    goto loc_003A9154;
loc_003A923E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) == 1) goto loc_003A919B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + (uint32_t)((uint32_t)(local_r14)) * 4)))) == 1) goto loc_003A91B8;
    goto loc_003A9195;
loc_003A925E:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + (uint32_t)((uint32_t)(local_r14)) * 4))) - (1));
    if (condition_is_equal) goto loc_003A92C3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_003A927A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_003A9371;
    if (((uint32_t)(Arg1)) != 10) goto loc_003A91B8;
loc_003A927A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))) != 0) goto loc_003A9328;
loc_003A9288:
loc_003A928B:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))))) goto loc_003A9231;
    Arg1 = (0) + (0);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8 + 0x8)) == 0) goto loc_003A938E;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + arg1 * 8)) == 0) goto loc_003A938E;
    result = (uint32_t)((0) + (1));
    goto loc_003A928B;
loc_003A92B3:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20)) != 0) goto loc_003A91F3;
    goto loc_003A91B8;
loc_003A92C3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))) != 0) goto loc_003A9338;
loc_003A92CC:
loc_003A92CF:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18))))) goto loc_003A922C;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x8)) == 0) goto loc_003A9229;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0xA)) == 0) goto loc_003A9229;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x8))) > ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0xA)))) goto loc_003A9229;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20) + 0x0 + 0x0 * 2 * 8 + 0x10)) == 0) goto loc_003A9229;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_003A92CF;
loc_003A9318:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x18)) == 0) goto loc_003A91B8;
    goto loc_003A919B;
loc_003A9328:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20)) != 0) goto loc_003A9288;
    goto loc_003A91B8;
loc_003A9338:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20)) == 0) goto loc_003A91B8;
    goto loc_003A92CC;
loc_003A9345:
    if ((uint32_t)(v_stack_p10) == 0) goto loc_003A9369;
loc_003A9349:
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_003A914C;
    if ((uint32_t)(v_stack_p10) == 0) goto loc_003A914C;
loc_003A935E:
    goto loc_003A91BB;
loc_003A9369:
    if ((*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_003A935E;
    goto loc_003A9349;
loc_003A9371:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 + 0x0 * 4 * 8 + 0x20)) == 0) goto loc_003A91B8;
loc_003A938E:
    goto loc_003A9231;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0 + rax*4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A90EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
