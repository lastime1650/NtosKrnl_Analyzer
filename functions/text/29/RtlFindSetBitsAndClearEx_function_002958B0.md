# RtlFindSetBitsAndClearEx

- RVA: `0x002958B0`–`0x00295C72` (길이 `962` bytes)
- VA: `0x00000001402958B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067860`
- 디코드: `276`개 명령, `962/962` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00295904` → [RtlClearBitsEx](RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)

### Direct callers
- [MiHotRemoveHugeRange](../67/MiHotRemoveHugeRange_function_00675DD0.md) at `0x006760D3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002958B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002958B5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002958BA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002958BF  57                              push rdi
002958C0  41 54                           push r12
002958C2  41 55                           push r13
002958C4  41 56                           push r14
002958C6  41 57                           push r15
002958C8  48 83 EC 20                     sub rsp, 0x20
002958CC  48 8B 29                        mov rbp, qword ptr [rcx]
002958CF  4D 8B E8                        mov r13, r8
002958D2  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
002958D6  4C 3B C5                        cmp r8, rbp
002958D9  4C 8B DA                        mov r11, rdx
002958DC  4C 8B E1                        mov r12, rcx
002958DF  48 1B DB                        sbb rbx, rbx
002958E2  49 83 CA FF                     or r10, 0xffffffffffffffff
002958E6  49 23 D8                        and rbx, r8
002958E9  4C 8D 4D FF                     lea r9, [rbp - 1]
002958ED  48 85 D2                        test rdx, rdx
002958F0  75 38                           jne 0x14029592a
002958F2  48 83 E3 F8                     and rbx, 0xfffffffffffffff8
002958F6  49 3B DA                        cmp rbx, r10
002958F9  74 0E                           je 0x140295909
002958FB  4D 8B C3                        mov r8, r11
002958FE  48 8B D3                        mov rdx, rbx
00295901  49 8B CC                        mov rcx, r12
00295904  E8 37 1E 00 00                  call 0x140297740
00295909  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0029590E  48 8B C3                        mov rax, rbx
00295911  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00295916  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0029591B  48 83 C4 20                     add rsp, 0x20
0029591F  41 5F                           pop r15
00295921  41 5E                           pop r14
00295923  41 5D                           pop r13
00295925  41 5C                           pop r12
00295927  5F                              pop rdi
00295928  C3                              ret
00295929  CC                              int3
0029592A  4C 8B FB                        mov r15, rbx
0029592D  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295932  49 8B C1                        mov rax, r9
00295935  49 2B C7                        sub rax, r15
00295938  BB 40 00 00 00                  mov ebx, 0x40
0029593D  48 FF C0                        inc rax
00295940  49 3B C3                        cmp rax, r11
00295943  72 5F                           jb 0x1402959a4
00295945  49 8B F1                        mov rsi, r9
00295948  44 8D 43 C1                     lea r8d, [rbx - 0x3f]
0029594C  49 2B F3                        sub rsi, r11
0029594F  41 8A CF                        mov cl, r15b
00295952  48 FF C6                        inc rsi
00295955  80 E1 3F                        and cl, 0x3f
00295958  49 D3 E0                        shl r8, cl
0029595B  48 8B C6                        mov rax, rsi
0029595E  48 C1 E8 06                     shr rax, 6
00295962  49 FF C8                        dec r8
00295965  49 8D 3C C6                     lea rdi, [r14 + rax*8]
00295969  49 8B C7                        mov rax, r15
0029596C  48 C1 E8 06                     shr rax, 6
00295970  49 8D 14 C6                     lea rdx, [r14 + rax*8]
00295974  48 8B 02                        mov rax, qword ptr [rdx]
00295977  48 F7 D0                        not rax
0029597A  4C 0B C0                        or r8, rax
0029597D  49 83 FB 7F                     cmp r11, 0x7f
00295981  0F 87 22 01 00 00               ja 0x140295aa9
00295987  4C 3B DB                        cmp r11, rbx
0029598A  0F 83 CF 00 00 00               jae 0x140295a5f
00295990  49 83 FB 01                     cmp r11, 1
00295994  77 60                           ja 0x1402959f6
00295996  4D 3B C2                        cmp r8, r10
00295999  75 33                           jne 0x1402959ce
0029599B  48 83 C2 08                     add rdx, 8
0029599F  48 3B D7                        cmp rdx, rdi
002959A2  76 22                           jbe 0x1402959c6
002959A4  49 8B DA                        mov rbx, r10
002959A7  4D 85 FF                        test r15, r15
002959AA  0F 84 46 FF FF FF               je 0x1402958f6
002959B0  4F 8D 0C 2B                     lea r9, [r11 + r13]
002959B4  4C 3B CD                        cmp r9, rbp
002959B7  4C 0F 47 CD                     cmova r9, rbp
002959BB  49 FF C9                        dec r9
002959BE  45 33 FF                        xor r15d, r15d
002959C1  E9 67 FF FF FF                  jmp 0x14029592d
002959C6  4C 8B 02                        mov r8, qword ptr [rdx]
002959C9  49 F7 D0                        not r8
002959CC  EB C8                           jmp 0x140295996
002959CE  49 F7 D0                        not r8
002959D1  48 8B DA                        mov rbx, rdx
002959D4  49 2B DE                        sub rbx, r14
002959D7  48 C1 FB 03                     sar rbx, 3
002959DB  49 0F BC C0                     bsf rax, r8
002959DF  48 C1 E3 06                     shl rbx, 6
002959E3  48 03 D8                        add rbx, rax
002959E6  48 3B DE                        cmp rbx, rsi
002959E9  77 B9                           ja 0x1402959a4
002959EB  49 3B DA                        cmp rbx, r10
002959EE  0F 85 07 FF FF FF               jne 0x1402958fb
002959F4  EB B1                           jmp 0x1402959a7
002959F6  45 33 D2                        xor r10d, r10d
002959F9  49 C1 E9 06                     shr r9, 6
002959FD  4B 8D 1C CE                     lea rbx, [r14 + r9*8]
00295A01  49 83 F8 FF                     cmp r8, -1
00295A05  74 7E                           je 0x140295a85
00295A07  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295A0C  B9 40 00 00 00                  mov ecx, 0x40
00295A11  49 0F BC C0                     bsf rax, r8
00295A15  0F 44 C1                        cmove eax, ecx
00295A18  41 8D 0C 02                     lea ecx, [r10 + rax]
00295A1C  49 3B CB                        cmp rcx, r11
00295A1F  73 5C                           jae 0x140295a7d
00295A21  4D 8B C8                        mov r9, r8
00295A24  45 8B D3                        mov r10d, r11d
00295A27  49 F7 D1                        not r9
00295A2A  49 8B C1                        mov rax, r9
00295A2D  41 8B CA                        mov ecx, r10d
00295A30  D1 E9                           shr ecx, 1
00295A32  48 D3 E8                        shr rax, cl
00295A35  4C 23 C8                        and r9, rax
00295A38  0F 84 5D 01 00 00               je 0x140295b9b
00295A3E  44 2B D1                        sub r10d, ecx
00295A41  41 83 FA 01                     cmp r10d, 1
00295A45  77 E3                           ja 0x140295a2a
00295A47  49 0F BC D9                     bsf rbx, r9
00295A4B  49 2B D6                        sub rdx, r14
00295A4E  48 C1 FA 03                     sar rdx, 3
00295A52  48 C1 E2 06                     shl rdx, 6
00295A56  48 03 DA                        add rbx, rdx
00295A59  49 83 CA FF                     or r10, 0xffffffffffffffff
00295A5D  EB 87                           jmp 0x1402959e6
00295A5F  4D 85 C0                        test r8, r8
00295A62  0F 89 6C 01 00 00               jns 0x140295bd4
00295A68  48 83 C2 08                     add rdx, 8
00295A6C  48 3B D7                        cmp rdx, rdi
00295A6F  0F 87 2F FF FF FF               ja 0x1402959a4
00295A75  4C 8B 02                        mov r8, qword ptr [rdx]
00295A78  49 F7 D0                        not r8
00295A7B  EB E2                           jmp 0x140295a5f
00295A7D  41 8B DA                        mov ebx, r10d
00295A80  48 F7 DB                        neg rbx
00295A83  EB C6                           jmp 0x140295a4b
00295A85  49 83 CA FF                     or r10, 0xffffffffffffffff
00295A89  48 83 C2 08                     add rdx, 8
00295A8D  48 3B D7                        cmp rdx, rdi
00295A90  0F 87 0E FF FF FF               ja 0x1402959a4
00295A96  4C 8B 02                        mov r8, qword ptr [rdx]
00295A99  49 F7 D0                        not r8
00295A9C  4D 3B C2                        cmp r8, r10
00295A9F  74 E8                           je 0x140295a89
00295AA1  45 33 D2                        xor r10d, r10d
00295AA4  E9 5E FF FF FF                  jmp 0x140295a07
00295AA9  40 F6 C6 3F                     test sil, 0x3f
00295AAD  4C 8D 4F 08                     lea r9, [rdi + 8]
00295AB1  4C 0F 44 CF                     cmove r9, rdi
00295AB5  4D 85 C0                        test r8, r8
00295AB8  0F 84 D6 00 00 00               je 0x140295b94
00295ABE  48 83 C2 08                     add rdx, 8
00295AC2  48 8B 02                        mov rax, qword ptr [rdx]
00295AC5  48 F7 D0                        not rax
00295AC8  48 85 C0                        test rax, rax
00295ACB  75 59                           jne 0x140295b26
00295ACD  21 44 24 50                     and dword ptr [rsp + 0x50], eax
00295AD1  49 0F BD C0                     bsr rax, r8
00295AD5  0F 84 89 01 00 00               je 0x140295c64
00295ADB  B9 3F 00 00 00                  mov ecx, 0x3f
00295AE0  2B C8                           sub ecx, eax
00295AE2  48 8B DA                        mov rbx, rdx
00295AE5  44 8B C1                        mov r8d, ecx
00295AE8  49 2B DE                        sub rbx, r14
00295AEB  48 C1 FB 03                     sar rbx, 3
00295AEF  48 C1 E3 06                     shl rbx, 6
00295AF3  49 2B D8                        sub rbx, r8
00295AF6  48 3B DE                        cmp rbx, rsi
00295AF9  0F 87 A5 FE FF FF               ja 0x1402959a4
00295AFF  49 8B C3                        mov rax, r11
00295B02  49 2B C0                        sub rax, r8
00295B05  48 C1 E8 06                     shr rax, 6
00295B09  4C 8D 04 C2                     lea r8, [rdx + rax*8]
00295B0D  48 83 C2 08                     add rdx, 8
00295B11  49 3B D0                        cmp rdx, r8
00295B14  74 4A                           je 0x140295b60
00295B16  48 8B 02                        mov rax, qword ptr [rdx]
00295B19  48 F7 D0                        not rax
00295B1C  48 85 C0                        test rax, rax
00295B1F  74 EC                           je 0x140295b0d
00295B21  BB 40 00 00 00                  mov ebx, 0x40
00295B26  48 8B CA                        mov rcx, rdx
00295B29  49 3B D1                        cmp rdx, r9
00295B2C  0F 87 72 FE FF FF               ja 0x1402959a4
00295B32  48 83 C2 08                     add rdx, 8
00295B36  48 8B 02                        mov rax, qword ptr [rdx]
00295B39  48 F7 D0                        not rax
00295B3C  48 85 C0                        test rax, rax
00295B3F  75 E5                           jne 0x140295b26
00295B41  48 8B 01                        mov rax, qword ptr [rcx]
00295B44  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295B49  48 F7 D0                        not rax
00295B4C  4C 0F BD C0                     bsr r8, rax
00295B50  0F 84 0E 01 00 00               je 0x140295c64
00295B56  B9 3F 00 00 00                  mov ecx, 0x3f
00295B5B  41 2B C8                        sub ecx, r8d
00295B5E  EB 82                           jmp 0x140295ae2
00295B60  45 8B C3                        mov r8d, r11d
00295B63  44 2B C1                        sub r8d, ecx
00295B66  41 83 E0 3F                     and r8d, 0x3f
00295B6A  0F 84 7B FE FF FF               je 0x1402959eb
00295B70  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295B75  48 8B 02                        mov rax, qword ptr [rdx]
00295B78  48 F7 D0                        not rax
00295B7B  48 0F BC C8                     bsf rcx, rax
00295B7F  B8 40 00 00 00                  mov eax, 0x40
00295B84  0F 44 C8                        cmove ecx, eax
00295B87  41 3B C8                        cmp ecx, r8d
00295B8A  0F 83 5B FE FF FF               jae 0x1402959eb
00295B90  8B D8                           mov ebx, eax
00295B92  EB 92                           jmp 0x140295b26
00295B94  33 C9                           xor ecx, ecx
00295B96  E9 47 FF FF FF                  jmp 0x140295ae2
00295B9B  48 3B D3                        cmp rdx, rbx
00295B9E  74 23                           je 0x140295bc3
00295BA0  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295BA5  49 0F BD C0                     bsr rax, r8
00295BA9  74 21                           je 0x140295bcc
00295BAB  41 BA 3F 00 00 00               mov r10d, 0x3f
00295BB1  44 2B D0                        sub r10d, eax
00295BB4  48 83 C2 08                     add rdx, 8
00295BB8  4C 8B 02                        mov r8, qword ptr [rdx]
00295BBB  49 F7 D0                        not r8
00295BBE  E9 3E FE FF FF                  jmp 0x140295a01
00295BC3  49 83 CA FF                     or r10, 0xffffffffffffffff
00295BC7  E9 D8 FD FF FF                  jmp 0x1402959a4
00295BCC  41 BA 40 00 00 00               mov r10d, 0x40
00295BD2  EB E0                           jmp 0x140295bb4
00295BD4  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295BD9  49 0F BD C8                     bsr rcx, r8
00295BDD  0F 84 88 00 00 00               je 0x140295c6b
00295BE3  B8 3F 00 00 00                  mov eax, 0x3f
00295BE8  2B C1                           sub eax, ecx
00295BEA  48 8B DA                        mov rbx, rdx
00295BED  44 8B C0                        mov r8d, eax
00295BF0  49 2B DE                        sub rbx, r14
00295BF3  48 C1 FB 03                     sar rbx, 3
00295BF7  48 FF C3                        inc rbx
00295BFA  48 C1 E3 06                     shl rbx, 6
00295BFE  49 2B D8                        sub rbx, r8
00295C01  48 3B DE                        cmp rbx, rsi
00295C04  0F 87 9A FD FF FF               ja 0x1402959a4
00295C0A  49 8B CB                        mov rcx, r11
00295C0D  49 2B C8                        sub rcx, r8
00295C10  0F 84 D5 FD FF FF               je 0x1402959eb
00295C16  48 83 C2 08                     add rdx, 8
00295C1A  41 B9 40 00 00 00               mov r9d, 0x40
00295C20  48 8B 02                        mov rax, qword ptr [rdx]
00295C23  48 F7 D0                        not rax
00295C26  4C 8B C0                        mov r8, rax
00295C29  49 3B C9                        cmp rcx, r9
00295C2C  72 18                           jb 0x140295c46
00295C2E  48 85 C0                        test rax, rax
00295C31  75 29                           jne 0x140295c5c
00295C33  49 2B C9                        sub rcx, r9
00295C36  0F 84 AF FD FF FF               je 0x1402959eb
00295C3C  48 83 C2 08                     add rdx, 8
00295C40  4C 8B 02                        mov r8, qword ptr [rdx]
00295C43  49 F7 D0                        not r8
00295C46  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00295C4B  49 0F BC C0                     bsf rax, r8
00295C4F  41 0F 44 C1                     cmove eax, r9d
00295C53  48 3B C1                        cmp rax, rcx
00295C56  0F 83 8F FD FF FF               jae 0x1402959eb
00295C5C  49 8B D9                        mov rbx, r9
00295C5F  E9 FB FD FF FF                  jmp 0x140295a5f
00295C64  8B CB                           mov ecx, ebx
00295C66  E9 77 FE FF FF                  jmp 0x140295ae2
00295C6B  8B C3                           mov eax, ebx
00295C6D  E9 78 FF FF FF                  jmp 0x140295bea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFindSetBitsAndClearEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r10 = (v_r10) | (-1);
    v_rbx = (v_rbx) & (a3);
    if (a2 != 0) goto loc_0029592A;
    v_rbx = (v_rbx) & (-8);
loc_002958F6:
    if (v_rbx != v_r10) {
        a3 = a2;
        a2 = v_rbx;
        a1 = a1;
        result = RtlClearBitsEx(a1, a2, a3, *(unsigned __int64 *)(a1) - 1);
    }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
loc_0029592A:
loc_0029592D:
    result = (*(unsigned __int64 *)(a1) - 1) - (v_stack_p10);
    result = (result) + 1;
    if (result < a2) goto loc_002959A4;
    v_rsi = (*(unsigned __int64 *)(a1) - 1) - (a2);
    v_rsi = (v_rsi) + 1;
    a1 = (unsigned __int8)(((unsigned __int8)(v_stack_p10)) & (63));
    a3 = (64 - 63) << ((unsigned __int8)(a1));
    result = (v_rsi) >> (6);
    a3 = (a3) - 1;
    result = (v_stack_p10) >> (6);
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + result * 8));
    a3 = (a3) | (result);
    if (a2 > 127) goto loc_00295AA9;
    if (a2 >= 64) goto loc_00295A5F;
    if (a2 > 1) goto loc_002959F6;
loc_00295996:
    if (a3 != v_r10) goto loc_002959CE;
    a2 = (*(unsigned __int64 *)(a1 + 8) + result * 8) + (8);
    if (a2 <= (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_002959C6;
loc_002959A4:
loc_002959A7:
    if (v_stack_p10 == 0) goto loc_002958F6;
    a4 = a2 + a3 * 1;
    if ((a2 + a3 * 1) > v_stack_p18) { a4 = v_stack_p18; }
    a4 = (a4) - 1;
    v_r15 = 0;
    goto loc_0029592D;
loc_002959C6:
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_00295996;
loc_002959CE:
    a3 = ~(a3);
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (result);
loc_002959E6:
    if (v_rbx > v_rsi) goto loc_002959A4;
loc_002959EB:
    if (v_rbx != v_r10) goto loc_002958FB;
    goto loc_002959A7;
loc_002959F6:
    v_r10 = 0;
    a4 = (a4) >> (6);
loc_00295A01:
    if (a3 == -1) goto loc_00295A85;
loc_00295A07:
    if (a3 == -1) { result = 64; }
    if ((v_r10 + result * 1) >= a2) goto loc_00295A7D;
    a4 = ~(a3);
loc_00295A2A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) >> (1));
    result = (a4) >> ((unsigned __int8)(a1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_00295B9B;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_00295A2A;
loc_00295A4B:
    a2 = (a2) - (*(unsigned __int64 *)(a1 + 8));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    v_rbx = (*(unsigned __int64 *)(a1 + 8) + a4 * 8) + (a2);
    v_r10 = (v_r10) | (-1);
    goto loc_002959E6;
loc_00295A5F:
    if (!sign_flag) goto loc_00295BD4;
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_002959A4;
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_00295A5F;
loc_00295A7D:
    v_rbx = -((unsigned int)((unsigned int)(v_r10)));
    goto loc_00295A4B;
loc_00295A85:
    v_r10 = (v_r10) | (-1);
loc_00295A89:
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_002959A4;
    a3 = ~(*(unsigned __int64 *)(a2));
    if (a3 == v_r10) goto loc_00295A89;
    v_r10 = 0;
    goto loc_00295A07;
loc_00295AA9:
    a4 = *(unsigned __int64 *)(a1 + 8) + result * 8 + 8;
    if ((((unsigned __int8)(v_rsi)) & (63)) == 0) { a4 = *(unsigned __int64 *)(a1 + 8) + result * 8; }
    if (a3 == 0) goto loc_00295B94;
    a2 = (a2) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (result != 0) goto loc_00295B26;
    if (result == 0) goto loc_00295C64;
    a1 = (unsigned int)((63) - ((unsigned int)(result)));
loc_00295AE2:
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(a1)));
    if (v_rbx > v_rsi) goto loc_002959A4;
    result = (a2) - ((unsigned int)((unsigned int)(a1)));
    result = (result) >> (6);
loc_00295B0D:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_00295B60;
    result = ~(*(unsigned __int64 *)(a2));
    if (result == 0) goto loc_00295B0D;
loc_00295B26:
    if (a2 > a4) goto loc_002959A4;
    a2 = (a2) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (result != 0) goto loc_00295B26;
    result = ~(*(unsigned __int64 *)(a2));
    if (result == 0) goto loc_00295C64;
    a1 = (unsigned int)((63) - ((unsigned int)(a2 + result * 8)));
    goto loc_00295AE2;
loc_00295B60:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) & (63));
    if (condition_is_equal) goto loc_002959EB;
    result = ~(*(unsigned __int64 *)(a2));
    if (condition_is_equal) { a1 = 64; }
    if (((unsigned int)(a1)) >= ((unsigned int)(a3))) goto loc_002959EB;
    goto loc_00295B26;
loc_00295B94:
    a1 = 0;
    goto loc_00295AE2;
loc_00295B9B:
    if (a2 == 64) goto loc_00295BC3;
    if (a2 == 64) goto loc_00295BCC;
    v_r10 = (unsigned int)((63) - (64));
loc_00295BB4:
    a2 = (a2) + (8);
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_00295A01;
loc_00295BC3:
    v_r10 = (v_r10) | (-1);
    goto loc_002959A4;
loc_00295BCC:
    goto loc_00295BB4;
loc_00295BD4:
    if (condition_is_equal) goto loc_00295C6B;
    result = (unsigned int)((63) - (0));
loc_00295BEA:
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) + 1;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(result)));
    if (v_rbx > v_rsi) goto loc_002959A4;
    a1 = (a2) - ((unsigned int)((unsigned int)(result)));
    if (condition_is_equal) goto loc_002959EB;
    a2 = (a2) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (a1 < 64) goto loc_00295C46;
    if (result != 0) goto loc_00295C5C;
    a1 = (a1) - (64);
    if (condition_is_equal) goto loc_002959EB;
    a2 = (a2) + (8);
    a3 = ~(*(unsigned __int64 *)(a2));
loc_00295C46:
    if (condition_is_equal) { result = 64; }
    if (result >= a1) goto loc_002959EB;
loc_00295C5C:
    goto loc_00295A5F;
loc_00295C64:
    goto loc_00295AE2;
loc_00295C6B:
    goto loc_00295BEA;
}
```

## 5. (Beta) C Style

```c
int64_t RtlFindSetBitsAndClearEx(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r10 = (local_r10) | (-1);
    local_rbx = (local_rbx) & (Arg3);
    if (Arg2 != 0) goto loc_0029592A;
    local_rbx = (local_rbx) & (-8);
loc_002958F6:
    if (local_rbx != local_r10) {
        Arg3 = Arg2;
        Arg2 = local_rbx;
        Arg1 = Arg1;
        result = RtlClearBitsEx(Arg1, Arg2, Arg3, *(uint64_t *)(arg1) - 1);
    }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
loc_0029592A:
loc_0029592D:
    result = (*(uint64_t *)(arg1) - 1) - (v_stack_p10);
    result = (result) + 1;
    if (result < Arg2) goto loc_002959A4;
    local_rsi = (*(uint64_t *)(arg1) - 1) - (Arg2);
    local_rsi = (local_rsi) + 1;
    Arg1 = (uint8_t)(((uint8_t)(v_stack_p10)) & (63));
    Arg3 = (64 - 63) << ((uint8_t)(Arg1));
    result = (local_rsi) >> (6);
    Arg3 = (Arg3) - 1;
    result = (v_stack_p10) >> (6);
    result = ~(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + result * 8));
    Arg3 = (Arg3) | (result);
    if (Arg2 > 127) goto loc_00295AA9;
    if (Arg2 >= 64) goto loc_00295A5F;
    if (Arg2 > 1) goto loc_002959F6;
loc_00295996:
    if (Arg3 != local_r10) goto loc_002959CE;
    Arg2 = (*(uint64_t *)(arg1 + 0x8) + result * 8) + (8);
    if (Arg2 <= (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_002959C6;
loc_002959A4:
loc_002959A7:
    if (v_stack_p10 == 0) goto loc_002958F6;
    a4 = Arg2 + Arg3 * 1;
    if ((Arg2 + Arg3 * 1) > v_stack_p18) { a4 = v_stack_p18; }
    a4 = (a4) - 1;
    local_r15 = 0;
    goto loc_0029592D;
loc_002959C6:
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_00295996;
loc_002959CE:
    Arg3 = ~(Arg3);
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (result);
loc_002959E6:
    if (local_rbx > local_rsi) goto loc_002959A4;
loc_002959EB:
    if (local_rbx != local_r10) goto loc_002958FB;
    goto loc_002959A7;
loc_002959F6:
    local_r10 = 0;
    a4 = (a4) >> (6);
loc_00295A01:
    if (Arg3 == -1) goto loc_00295A85;
loc_00295A07:
    if (Arg3 == -1) { result = 64; }
    if ((local_r10 + result * 1) >= Arg2) goto loc_00295A7D;
    a4 = ~(Arg3);
loc_00295A2A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) >> (1));
    result = (a4) >> ((uint8_t)(Arg1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_00295B9B;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_00295A2A;
loc_00295A4B:
    Arg2 = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    local_rbx = (*(uint64_t *)(arg1 + 0x8) + a4 * 8) + (Arg2);
    local_r10 = (local_r10) | (-1);
    goto loc_002959E6;
loc_00295A5F:
    if (!sign_flag) goto loc_00295BD4;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_002959A4;
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_00295A5F;
loc_00295A7D:
    local_rbx = -((uint32_t)((uint32_t)(local_r10)));
    goto loc_00295A4B;
loc_00295A85:
    local_r10 = (local_r10) | (-1);
loc_00295A89:
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_002959A4;
    Arg3 = ~(*(uint64_t *)(Arg2));
    if (Arg3 == local_r10) goto loc_00295A89;
    local_r10 = 0;
    goto loc_00295A07;
loc_00295AA9:
    a4 = *(uint64_t *)(arg1 + 0x8) + result * 8 + 8;
    if ((((uint8_t)(local_rsi)) & (63)) == 0) { a4 = *(uint64_t *)(arg1 + 0x8) + result * 8; }
    if (Arg3 == 0) goto loc_00295B94;
    Arg2 = (Arg2) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (result != 0) goto loc_00295B26;
    if (result == 0) goto loc_00295C64;
    Arg1 = (uint32_t)((63) - ((uint32_t)(result)));
loc_00295AE2:
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(Arg1)));
    if (local_rbx > local_rsi) goto loc_002959A4;
    result = (Arg2) - ((uint32_t)((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_00295B0D:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_00295B60;
    result = ~(*(uint64_t *)(Arg2));
    if (result == 0) goto loc_00295B0D;
loc_00295B26:
    if (Arg2 > a4) goto loc_002959A4;
    Arg2 = (Arg2) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (result != 0) goto loc_00295B26;
    result = ~(*(uint64_t *)(Arg2));
    if (result == 0) goto loc_00295C64;
    Arg1 = (uint32_t)((63) - ((uint32_t)(Arg2 + result * 8)));
    goto loc_00295AE2;
loc_00295B60:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) & (63));
    if (condition_is_equal) goto loc_002959EB;
    result = ~(*(uint64_t *)(Arg2));
    if (condition_is_equal) { Arg1 = 64; }
    if (((uint32_t)(Arg1)) >= ((uint32_t)(Arg3))) goto loc_002959EB;
    goto loc_00295B26;
loc_00295B94:
    Arg1 = 0;
    goto loc_00295AE2;
loc_00295B9B:
    if (Arg2 == 64) goto loc_00295BC3;
    if (Arg2 == 64) goto loc_00295BCC;
    local_r10 = (uint32_t)((63) - (64));
loc_00295BB4:
    Arg2 = (Arg2) + (8);
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_00295A01;
loc_00295BC3:
    local_r10 = (local_r10) | (-1);
    goto loc_002959A4;
loc_00295BCC:
    goto loc_00295BB4;
loc_00295BD4:
    if (condition_is_equal) goto loc_00295C6B;
    result = (uint32_t)((63) - (0));
loc_00295BEA:
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) + 1;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(result)));
    if (local_rbx > local_rsi) goto loc_002959A4;
    Arg1 = (Arg2) - ((uint32_t)((uint32_t)(result)));
    if (condition_is_equal) goto loc_002959EB;
    Arg2 = (Arg2) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (Arg1 < 64) goto loc_00295C46;
    if (result != 0) goto loc_00295C5C;
    Arg1 = (Arg1) - (64);
    if (condition_is_equal) goto loc_002959EB;
    Arg2 = (Arg2) + (8);
    Arg3 = ~(*(uint64_t *)(Arg2));
loc_00295C46:
    if (condition_is_equal) { result = 64; }
    if (result >= Arg1) goto loc_002959EB;
loc_00295C5C:
    goto loc_00295A5F;
loc_00295C64:
    goto loc_00295AE2;
loc_00295C6B:
    goto loc_00295BEA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002958B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
