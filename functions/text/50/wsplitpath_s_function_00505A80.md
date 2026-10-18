# wsplitpath_s

- RVA: `0x00505A80`–`0x00505D2F` (길이 `687` bytes)
- VA: `0x0000000140505A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C28E4`
- 디코드: `204`개 명령, `687/687` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00505B67` → [wcsncpy_s](wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00505BE9` → [wcsncpy_s](wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00505C2F` → [wcsncpy_s](wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00505C5C` → [wcsncpy_s](wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00505C89` → [wcsncpy_s](wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00505D0F` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00505A80  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00505A85  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00505A8A  55                              push rbp
00505A8B  56                              push rsi
00505A8C  57                              push rdi
00505A8D  41 54                           push r12
00505A8F  41 55                           push r13
00505A91  41 56                           push r14
00505A93  41 57                           push r15
00505A95  48 83 EC 30                     sub rsp, 0x30
00505A99  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00505AA1  48 8B F9                        mov rdi, rcx
00505AA4  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
00505AAC  4C 8B E2                        mov r12, rdx
00505AAF  33 D2                           xor edx, edx
00505AB1  4D 8B E9                        mov r13, r9
00505AB4  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
00505AB8  49 8B F0                        mov rsi, r8
00505ABB  8B CA                           mov ecx, edx
00505ABD  48 85 FF                        test rdi, rdi
00505AC0  74 0A                           je 0x140505acc
00505AC2  4D 85 E4                        test r12, r12
00505AC5  75 0F                           jne 0x140505ad6
00505AC7  4D 85 C0                        test r8, r8
00505ACA  74 0F                           je 0x140505adb
00505ACC  B9 01 00 00 00                  mov ecx, 1
00505AD1  E9 D3 01 00 00                  jmp 0x140505ca9
00505AD6  48 85 F6                        test rsi, rsi
00505AD9  74 F1                           je 0x140505acc
00505ADB  4D 85 ED                        test r13, r13
00505ADE  75 0C                           jne 0x140505aec
00505AE0  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
00505AE8  75 E2                           jne 0x140505acc
00505AEA  EB 0A                           jmp 0x140505af6
00505AEC  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
00505AF4  74 D6                           je 0x140505acc
00505AF6  4D 85 FF                        test r15, r15
00505AF9  75 0C                           jne 0x140505b07
00505AFB  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
00505B03  75 C7                           jne 0x140505acc
00505B05  EB 0A                           jmp 0x140505b11
00505B07  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
00505B0F  74 BB                           je 0x140505acc
00505B11  4D 85 F6                        test r14, r14
00505B14  75 0C                           jne 0x140505b22
00505B16  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
00505B1E  75 AC                           jne 0x140505acc
00505B20  EB 0A                           jmp 0x140505b2c
00505B22  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
00505B2A  74 A0                           je 0x140505acc
00505B2C  B8 01 00 00 00                  mov eax, 1
00505B31  48 8B DF                        mov rbx, rdi
00505B34  66 39 13                        cmp word ptr [rbx], dx
00505B37  74 0A                           je 0x140505b43
00505B39  48 83 C3 02                     add rbx, 2
00505B3D  48 83 E8 01                     sub rax, 1
00505B41  75 F1                           jne 0x140505b34
00505B43  66 83 3B 3A                     cmp word ptr [rbx], 0x3a
00505B47  75 2F                           jne 0x140505b78
00505B49  4D 85 E4                        test r12, r12
00505B4C  74 24                           je 0x140505b72
00505B4E  48 83 FE 03                     cmp rsi, 3
00505B52  0F 82 56 01 00 00               jb 0x140505cae
00505B58  41 B9 02 00 00 00               mov r9d, 2
00505B5E  4C 8B C7                        mov r8, rdi
00505B61  48 8B D6                        mov rdx, rsi
00505B64  49 8B CC                        mov rcx, r12
00505B67  E8 E4 0A 00 00                  call 0x140506650
00505B6C  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00505B70  33 D2                           xor edx, edx
00505B72  48 8D 7B 02                     lea rdi, [rbx + 2]
00505B76  EB 0A                           jmp 0x140505b82
00505B78  4D 85 E4                        test r12, r12
00505B7B  74 05                           je 0x140505b82
00505B7D  66 41 89 14 24                  mov word ptr [r12], dx
00505B82  0F B7 07                        movzx eax, word ptr [rdi]
00505B85  48 8B EA                        mov rbp, rdx
00505B88  48 8B F2                        mov rsi, rdx
00505B8B  48 8B DF                        mov rbx, rdi
00505B8E  66 85 C0                        test ax, ax
00505B91  74 62                           je 0x140505bf5
00505B93  66 83 F8 2F                     cmp ax, 0x2f
00505B97  74 11                           je 0x140505baa
00505B99  66 83 F8 5C                     cmp ax, 0x5c
00505B9D  74 0B                           je 0x140505baa
00505B9F  66 83 F8 2E                     cmp ax, 0x2e
00505BA3  75 09                           jne 0x140505bae
00505BA5  48 8B F3                        mov rsi, rbx
00505BA8  EB 04                           jmp 0x140505bae
00505BAA  48 8D 6B 02                     lea rbp, [rbx + 2]
00505BAE  48 83 C3 02                     add rbx, 2
00505BB2  0F B7 03                        movzx eax, word ptr [rbx]
00505BB5  66 85 C0                        test ax, ax
00505BB8  75 D9                           jne 0x140505b93
00505BBA  48 85 ED                        test rbp, rbp
00505BBD  74 36                           je 0x140505bf5
00505BBF  4D 85 ED                        test r13, r13
00505BC2  74 2C                           je 0x140505bf0
00505BC4  4C 8B CD                        mov r9, rbp
00505BC7  4C 2B CF                        sub r9, rdi
00505BCA  49 D1 F9                        sar r9, 1
00505BCD  4C 39 8C 24 90 00 00 00         cmp qword ptr [rsp + 0x90], r9
00505BD5  0F 86 C6 00 00 00               jbe 0x140505ca1
00505BDB  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
00505BE3  4C 8B C7                        mov r8, rdi
00505BE6  49 8B CD                        mov rcx, r13
00505BE9  E8 62 0A 00 00                  call 0x140506650
00505BEE  33 D2                           xor edx, edx
00505BF0  48 8B FD                        mov rdi, rbp
00505BF3  EB 0A                           jmp 0x140505bff
00505BF5  4D 85 ED                        test r13, r13
00505BF8  74 05                           je 0x140505bff
00505BFA  66 41 89 55 00                  mov word ptr [r13], dx
00505BFF  48 85 F6                        test rsi, rsi
00505C02  74 5F                           je 0x140505c63
00505C04  48 3B F7                        cmp rsi, rdi
00505C07  72 5A                           jb 0x140505c63
00505C09  4D 85 FF                        test r15, r15
00505C0C  74 28                           je 0x140505c36
00505C0E  4C 8B CE                        mov r9, rsi
00505C11  4C 2B CF                        sub r9, rdi
00505C14  49 D1 F9                        sar r9, 1
00505C17  4C 39 8C 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], r9
00505C1F  76 7C                           jbe 0x140505c9d
00505C21  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00505C29  4C 8B C7                        mov r8, rdi
00505C2C  49 8B CF                        mov rcx, r15
00505C2F  E8 1C 0A 00 00                  call 0x140506650
00505C34  33 D2                           xor edx, edx
00505C36  4D 85 F6                        test r14, r14
00505C39  74 5E                           je 0x140505c99
00505C3B  48 2B DE                        sub rbx, rsi
00505C3E  48 D1 FB                        sar rbx, 1
00505C41  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
00505C49  76 52                           jbe 0x140505c9d
00505C4B  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
00505C53  4C 8B CB                        mov r9, rbx
00505C56  4C 8B C6                        mov r8, rsi
00505C59  49 8B CE                        mov rcx, r14
00505C5C  E8 EF 09 00 00                  call 0x140506650
00505C61  EB 36                           jmp 0x140505c99
00505C63  4D 85 FF                        test r15, r15
00505C66  74 28                           je 0x140505c90
00505C68  48 2B DF                        sub rbx, rdi
00505C6B  48 D1 FB                        sar rbx, 1
00505C6E  48 39 9C 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rbx
00505C76  76 25                           jbe 0x140505c9d
00505C78  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00505C80  4C 8B CB                        mov r9, rbx
00505C83  4C 8B C7                        mov r8, rdi
00505C86  49 8B CF                        mov rcx, r15
00505C89  E8 C2 09 00 00                  call 0x140506650
00505C8E  33 D2                           xor edx, edx
00505C90  4D 85 F6                        test r14, r14
00505C93  74 04                           je 0x140505c99
00505C95  66 41 89 16                     mov word ptr [r14], dx
00505C99  33 C0                           xor eax, eax
00505C9B  EB 7C                           jmp 0x140505d19
00505C9D  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00505CA1  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
00505CA9  4D 85 E4                        test r12, r12
00505CAC  74 0A                           je 0x140505cb8
00505CAE  48 85 F6                        test rsi, rsi
00505CB1  74 05                           je 0x140505cb8
00505CB3  66 41 89 14 24                  mov word ptr [r12], dx
00505CB8  4D 85 ED                        test r13, r13
00505CBB  74 0F                           je 0x140505ccc
00505CBD  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
00505CC5  76 05                           jbe 0x140505ccc
00505CC7  66 41 89 55 00                  mov word ptr [r13], dx
00505CCC  4D 85 FF                        test r15, r15
00505CCF  74 0E                           je 0x140505cdf
00505CD1  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
00505CD9  76 04                           jbe 0x140505cdf
00505CDB  66 41 89 17                     mov word ptr [r15], dx
00505CDF  4D 85 F6                        test r14, r14
00505CE2  74 0E                           je 0x140505cf2
00505CE4  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
00505CEC  76 04                           jbe 0x140505cf2
00505CEE  66 41 89 16                     mov word ptr [r14], dx
00505CF2  48 85 FF                        test rdi, rdi
00505CF5  74 09                           je 0x140505d00
00505CF7  85 C9                           test ecx, ecx
00505CF9  75 05                           jne 0x140505d00
00505CFB  8D 41 22                        lea eax, [rcx + 0x22]
00505CFE  EB 19                           jmp 0x140505d19
00505D00  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00505D05  45 33 C9                        xor r9d, r9d
00505D08  33 D2                           xor edx, edx
00505D0A  45 33 C0                        xor r8d, r8d
00505D0D  33 C9                           xor ecx, ecx
00505D0F  E8 3C 88 F9 FF                  call 0x14049e550
00505D14  B8 16 00 00 00                  mov eax, 0x16
00505D19  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00505D1E  48 83 C4 30                     add rsp, 0x30
00505D22  41 5F                           pop r15
00505D24  41 5E                           pop r14
00505D26  41 5D                           pop r13
00505D28  41 5C                           pop r12
00505D2A  5F                              pop rdi
00505D2B  5E                              pop rsi
00505D2C  5D                              pop rbp
00505D2D  C3                              ret
00505D2E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wsplitpath_s(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    a2 = 0;
    v_stack_p8 = 0;
    if (a1 == 0) goto loc_00505ACC;
    if (0 != 0) goto loc_00505AD6;
    if (a3 == 0) goto loc_00505ADB;
loc_00505ACC:
    goto loc_00505CA9;
loc_00505AD6:
    if (a3 == 0) goto loc_00505ACC;
loc_00505ADB:
    if (a4 != 0) goto loc_00505AEC;
    if (a5 != 0) goto loc_00505ACC;
    goto loc_00505AF6;
loc_00505AEC:
    if (a5 == 0) goto loc_00505ACC;
loc_00505AF6:
    if (a6 != 0) goto loc_00505B07;
    if (a7 != 0) goto loc_00505ACC;
    goto loc_00505B11;
loc_00505B07:
    if (a7 == 0) goto loc_00505ACC;
loc_00505B11:
    if (a8 != 0) goto loc_00505B22;
    if (a9 != 0) goto loc_00505ACC;
    goto loc_00505B2C;
loc_00505B22:
    if (a9 == 0) goto loc_00505ACC;
loc_00505B2C:
loc_00505B34:
    if ((*(unsigned __int16 *)(a1)) == 0) goto loc_00505B43;
    v_rbx = (a1) + (2);
    result = (1) - (1);
    if (condition_is_not_equal) goto loc_00505B34;
loc_00505B43:
    if ((*(unsigned __int16 *)(v_rbx)) != 58) goto loc_00505B78;
    if (0 == 0) goto loc_00505B72;
    if (a3 < 3) goto loc_00505CAE;
    result = wcsncpy_s(0, a3, a1, 2);
    a2 = 0;
loc_00505B72:
    goto loc_00505B82;
loc_00505B78:
    if (0 != 0) {
        *(unsigned __int16 *)(a2) = 0;
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2)) == 0) goto loc_00505BF5;
loc_00505B93:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2))) == 47) goto loc_00505BAA;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2))) == 92) goto loc_00505BAA;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2))) != 46) goto loc_00505BAE;
    goto loc_00505BAE;
loc_00505BAA:
loc_00505BAE:
    v_rbx = (v_rbx + 2) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) != 0) goto loc_00505B93;
    if (v_rbx + 2 + 2 == 0) goto loc_00505BF5;
    if (a4 == 0) goto loc_00505BF0;
    a4 = (v_rbx + 2 + 2) - (v_rbx + 2);
    a4 = (a4) >> (1);
    if (a5 <= a4) goto loc_00505CA1;
    result = wcsncpy_s(a4, a5, v_rbx + 2, a4);
    a2 = 0;
loc_00505BF0:
    goto loc_00505BFF;
loc_00505BF5:
    if (a4 != 0) {
        *(unsigned __int16 *)(a4) = 0;
    }
    if (v_rbx + 2 == 0) goto loc_00505C63;
    if ((v_rbx + 2) < (v_rbx + 2 + 2)) goto loc_00505C63;
    if (a6 == 0) goto loc_00505C36;
    a4 = (v_rbx + 2) - (v_rbx + 2 + 2);
    a4 = (a4) >> (1);
    if (a7 <= a4) goto loc_00505C9D;
    result = wcsncpy_s(a6, a7, v_rbx + 2 + 2, a4);
    a2 = 0;
loc_00505C36:
    if (a8 == 0) goto loc_00505C99;
    v_rbx = (v_rbx) - (v_rbx + 2);
    v_rbx = (v_rbx) >> (1);
    if (a9 <= v_rbx) goto loc_00505C9D;
    result = wcsncpy_s(a8, a9, v_rbx + 2, v_rbx);
    goto loc_00505C99;
loc_00505C63:
    if (a6 == 0) goto loc_00505C90;
    v_rbx = (v_rbx) - (v_rbx + 2 + 2);
    v_rbx = (v_rbx) >> (1);
    if (a7 <= v_rbx) goto loc_00505C9D;
    result = wcsncpy_s(a6, a7, v_rbx + 2 + 2, v_rbx);
    a2 = 0;
loc_00505C90:
    if (a8 != 0) {
        *(unsigned __int16 *)(a8) = 0;
    }
    result = 0;
    goto loc_00505D19;
loc_00505C9D:
loc_00505CA1:
loc_00505CA9:
    if (0 == 0) goto loc_00505CB8;
loc_00505CAE:
    if (v_stack_p18 != 0) {
        *(unsigned __int16 *)(a2) = 0;
    }
    if (a4 == 0) goto loc_00505CCC;
    if (a5 >= = 0) {
        *(unsigned __int16 *)(a4) = 0;
    }
    if (a6 == 0) goto loc_00505CDF;
    if (a7 >= = 0) {
        *(unsigned __int16 *)(a6) = 0;
    }
    if (a8 == 0) goto loc_00505CF2;
    if (a9 >= = 0) {
        *(unsigned __int16 *)(a8) = 0;
    }
    if (v_rbx + 2 + 2 == 0) goto loc_00505D00;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) goto loc_00505D00;
    goto loc_00505D19;
loc_00505D00:
    v_stack_m48 = 0;
    a4 = 0;
    a2 = 0;
    a3 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
loc_00505D19:
    v_rsp = (v_rsp) + (48);
    return 22;
}
```

## 5. (Beta) C Style

```c
int64_t wsplitpath_s(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    Arg2 = 0;
    v_stack_p8 = 0;
    if (Arg1 == 0) goto loc_00505ACC;
    if (0 != 0) goto loc_00505AD6;
    if (Arg3 == 0) goto loc_00505ADB;
loc_00505ACC:
    goto loc_00505CA9;
loc_00505AD6:
    if (Arg3 == 0) goto loc_00505ACC;
loc_00505ADB:
    if (Arg4 != 0) goto loc_00505AEC;
    if (Arg5 != 0) goto loc_00505ACC;
    goto loc_00505AF6;
loc_00505AEC:
    if (Arg5 == 0) goto loc_00505ACC;
loc_00505AF6:
    if (Arg6 != 0) goto loc_00505B07;
    if (Arg7 != 0) goto loc_00505ACC;
    goto loc_00505B11;
loc_00505B07:
    if (Arg7 == 0) goto loc_00505ACC;
loc_00505B11:
    if (Arg8 != 0) goto loc_00505B22;
    if (Arg9 != 0) goto loc_00505ACC;
    goto loc_00505B2C;
loc_00505B22:
    if (Arg9 == 0) goto loc_00505ACC;
loc_00505B2C:
loc_00505B34:
    if ((*(uint16_t *)(Arg1)) == 0) goto loc_00505B43;
    local_rbx = (Arg1) + (2);
    result = (1) - (1);
    if (condition_is_not_equal) goto loc_00505B34;
loc_00505B43:
    if ((*(uint16_t *)(local_rbx)) != 58) goto loc_00505B78;
    if (0 == 0) goto loc_00505B72;
    if (Arg3 < 3) goto loc_00505CAE;
    result = wcsncpy_s(0, Arg3, Arg1, 2);
    Arg2 = 0;
loc_00505B72:
    goto loc_00505B82;
loc_00505B78:
    if (0 != 0) {
        *(uint16_t *)(Arg2) = 0;
    }
    if ((uint16_t)(*(uint16_t *)(local_rbx + 0x2)) == 0) goto loc_00505BF5;
loc_00505B93:
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x2))) == 47) goto loc_00505BAA;
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x2))) == 92) goto loc_00505BAA;
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x2))) != 46) goto loc_00505BAE;
    goto loc_00505BAE;
loc_00505BAA:
loc_00505BAE:
    local_rbx = (local_rbx + 2) + (2);
    if ((uint16_t)(*(uint16_t *)(local_rbx)) != 0) goto loc_00505B93;
    if (local_rbx + 2 + 2 == 0) goto loc_00505BF5;
    if (Arg4 == 0) goto loc_00505BF0;
    Arg4 = (local_rbx + 2 + 2) - (local_rbx + 2);
    Arg4 = (Arg4) >> (1);
    if (Arg5 <= Arg4) goto loc_00505CA1;
    result = wcsncpy_s(Arg4, Arg5, local_rbx + 2, Arg4);
    Arg2 = 0;
loc_00505BF0:
    goto loc_00505BFF;
loc_00505BF5:
    if (Arg4 != 0) {
        *(uint16_t *)(Arg4) = 0;
    }
    if (local_rbx + 2 == 0) goto loc_00505C63;
    if ((local_rbx + 2) < (local_rbx + 2 + 2)) goto loc_00505C63;
    if (Arg6 == 0) goto loc_00505C36;
    Arg4 = (local_rbx + 2) - (local_rbx + 2 + 2);
    Arg4 = (Arg4) >> (1);
    if (Arg7 <= Arg4) goto loc_00505C9D;
    result = wcsncpy_s(Arg6, Arg7, local_rbx + 2 + 2, Arg4);
    Arg2 = 0;
loc_00505C36:
    if (Arg8 == 0) goto loc_00505C99;
    local_rbx = (local_rbx) - (local_rbx + 2);
    local_rbx = (local_rbx) >> (1);
    if (Arg9 <= local_rbx) goto loc_00505C9D;
    result = wcsncpy_s(Arg8, Arg9, local_rbx + 2, local_rbx);
    goto loc_00505C99;
loc_00505C63:
    if (Arg6 == 0) goto loc_00505C90;
    local_rbx = (local_rbx) - (local_rbx + 2 + 2);
    local_rbx = (local_rbx) >> (1);
    if (Arg7 <= local_rbx) goto loc_00505C9D;
    result = wcsncpy_s(Arg6, Arg7, local_rbx + 2 + 2, local_rbx);
    Arg2 = 0;
loc_00505C90:
    if (Arg8 != 0) {
        *(uint16_t *)(Arg8) = 0;
    }
    result = 0;
    goto loc_00505D19;
loc_00505C9D:
loc_00505CA1:
loc_00505CA9:
    if (0 == 0) goto loc_00505CB8;
loc_00505CAE:
    if (v_stack_p18 != 0) {
        *(uint16_t *)(Arg2) = 0;
    }
    if (Arg4 == 0) goto loc_00505CCC;
    if (Arg5 >= = 0) {
        *(uint16_t *)(Arg4) = 0;
    }
    if (Arg6 == 0) goto loc_00505CDF;
    if (Arg7 >= = 0) {
        *(uint16_t *)(Arg6) = 0;
    }
    if (Arg8 == 0) goto loc_00505CF2;
    if (Arg9 >= = 0) {
        *(uint16_t *)(Arg8) = 0;
    }
    if (local_rbx + 2 + 2 == 0) goto loc_00505D00;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) goto loc_00505D00;
    goto loc_00505D19;
loc_00505D00:
    v_stack_m48 = 0;
    Arg4 = 0;
    Arg2 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
loc_00505D19:
    local_rsp = (local_rsp) + (48);
    return 22;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00505A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
