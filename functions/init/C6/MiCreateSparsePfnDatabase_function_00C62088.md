# MiCreateSparsePfnDatabase

- RVA: `0x00C62088`–`0x00C62369` (길이 `737` bytes)
- VA: `0x0000000140C62088`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D79EC`
- 디코드: `209`개 명령, `737/737` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C6213B` → [MxMapPfnRange](MxMapPfnRange_function_00C63CC8.md) (function, `0x00C63CC8`)
- `0x00C6230A` → [MxMapPfnRange](MxMapPfnRange_function_00C63CC8.md) (function, `0x00C63CC8`)
- `0x00C62323` → [MxMapPfnRange](MxMapPfnRange_function_00C63CC8.md) (function, `0x00C63CC8`)
- `0x00C62349` → [MxMapPfnRange](MxMapPfnRange_function_00C63CC8.md) (function, `0x00C63CC8`)

### Direct callers
- [MiCreatePfnDatabase](../C5/MiCreatePfnDatabase_function_00C5F930.md) at `0x00C5FA6D`

### Static image references
- `0x00C6230F` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00C6232F` → RVA `0x00E35C00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C62088  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C6208D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00C62092  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00C62097  41 54                           push r12
00C62099  41 56                           push r14
00C6209B  41 57                           push r15
00C6209D  48 83 EC 20                     sub rsp, 0x20
00C620A1  45 33 F6                        xor r14d, r14d
00C620A4  48 8D 99 60 01 00 00            lea rbx, [rcx + 0x160]
00C620AB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00C620AF  49 83 C9 FF                     or r9, 0xffffffffffffffff
00C620B3  BE 03 00 00 00                  mov esi, 3
00C620B8  45 8B FE                        mov r15d, r14d
00C620BB  A8 01                           test al, 1
00C620BD  74 13                           je 0x140c620d2
00C620BF  48 83 F8 01                     cmp rax, 1
00C620C3  0F 84 46 02 00 00               je 0x140c6230f
00C620C9  48 83 CB 01                     or rbx, 1
00C620CD  48 33 D8                        xor rbx, rax
00C620D0  EB 03                           jmp 0x140c620d5
00C620D2  48 8B D8                        mov rbx, rax
00C620D5  48 85 DB                        test rbx, rbx
00C620D8  0F 84 31 02 00 00               je 0x140c6230f
00C620DE  41 BC FF FF FF 1F               mov r12d, 0x1fffffff
00C620E4  45 8D 44 24 01                  lea r8d, [r12 + 1]
00C620E9  8B 7B 18                        mov edi, dword ptr [rbx + 0x18]
00C620EC  8B CF                           mov ecx, edi
00C620EE  41 23 CC                        and ecx, r12d
00C620F1  83 F9 2C                        cmp ecx, 0x2c
00C620F4  0F 87 0B 01 00 00               ja 0x140c62205
00C620FA  48 BA 48 00 C0 C0 C5 15 00 00   movabs rdx, 0x15c5c0c00048
00C62104  48 0F A3 CA                     bt rdx, rcx
00C62108  0F 83 F7 00 00 00               jae 0x140c62205
00C6210E  49 83 F9 FF                     cmp r9, -1
00C62112  0F 84 8B 01 00 00               je 0x140c622a3
00C62118  41 85 F0                        test r8d, esi
00C6211B  74 15                           je 0x140c62132
00C6211D  8B C6                           mov eax, esi
00C6211F  41 23 C4                        and eax, r12d
00C62122  83 F8 02                        cmp eax, 2
00C62125  74 0B                           je 0x140c62132
00C62127  41 B8 01 00 00 00               mov r8d, 1
00C6212D  83 F8 18                        cmp eax, 0x18
00C62130  75 03                           jne 0x140c62135
00C62132  45 8B C6                        mov r8d, r14d
00C62135  49 8B D7                        mov rdx, r15
00C62138  49 8B C9                        mov rcx, r9
00C6213B  E8 88 1B 00 00                  call 0x140c63cc8
00C62140  8B C7                           mov eax, edi
00C62142  41 23 C4                        and eax, r12d
00C62145  83 F8 1E                        cmp eax, 0x1e
00C62148  0F 84 4B 01 00 00               je 0x140c62299
00C6214E  8B C7                           mov eax, edi
00C62150  41 23 C4                        and eax, r12d
00C62153  83 F8 1F                        cmp eax, 0x1f
00C62156  0F 84 3D 01 00 00               je 0x140c62299
00C6215C  8B C7                           mov eax, edi
00C6215E  41 23 C4                        and eax, r12d
00C62161  83 F8 06                        cmp eax, 6
00C62164  0F 84 2F 01 00 00               je 0x140c62299
00C6216A  8B C7                           mov eax, edi
00C6216C  41 23 C4                        and eax, r12d
00C6216F  83 F8 20                        cmp eax, 0x20
00C62172  0F 84 21 01 00 00               je 0x140c62299
00C62178  8B C7                           mov eax, edi
00C6217A  41 23 C4                        and eax, r12d
00C6217D  83 F8 22                        cmp eax, 0x22
00C62180  0F 84 13 01 00 00               je 0x140c62299
00C62186  8B C7                           mov eax, edi
00C62188  41 23 C4                        and eax, r12d
00C6218B  83 F8 17                        cmp eax, 0x17
00C6218E  0F 84 05 01 00 00               je 0x140c62299
00C62194  8B C7                           mov eax, edi
00C62196  41 23 C4                        and eax, r12d
00C62199  83 F8 03                        cmp eax, 3
00C6219C  0F 84 F7 00 00 00               je 0x140c62299
00C621A2  8B C7                           mov eax, edi
00C621A4  41 23 C4                        and eax, r12d
00C621A7  83 F8 16                        cmp eax, 0x16
00C621AA  0F 84 E9 00 00 00               je 0x140c62299
00C621B0  8B C7                           mov eax, edi
00C621B2  41 23 C4                        and eax, r12d
00C621B5  83 F8 2A                        cmp eax, 0x2a
00C621B8  0F 84 DB 00 00 00               je 0x140c62299
00C621BE  8B C7                           mov eax, edi
00C621C0  41 23 C4                        and eax, r12d
00C621C3  83 F8 26                        cmp eax, 0x26
00C621C6  0F 84 CD 00 00 00               je 0x140c62299
00C621CC  8B C7                           mov eax, edi
00C621CE  41 23 C4                        and eax, r12d
00C621D1  83 F8 27                        cmp eax, 0x27
00C621D4  0F 84 BF 00 00 00               je 0x140c62299
00C621DA  8B C7                           mov eax, edi
00C621DC  41 23 C4                        and eax, r12d
00C621DF  83 F8 2C                        cmp eax, 0x2c
00C621E2  0F 84 B1 00 00 00               je 0x140c62299
00C621E8  8B C7                           mov eax, edi
00C621EA  41 23 C4                        and eax, r12d
00C621ED  83 F8 28                        cmp eax, 0x28
00C621F0  0F 84 A3 00 00 00               je 0x140c62299
00C621F6  4C 8B 4B 20                     mov r9, qword ptr [rbx + 0x20]
00C621FA  8B F7                           mov esi, edi
00C621FC  4C 8B 7B 28                     mov r15, qword ptr [rbx + 0x28]
00C62200  E9 98 00 00 00                  jmp 0x140c6229d
00C62205  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00C62209  49 83 F9 FF                     cmp r9, -1
00C6220D  75 0E                           jne 0x140c6221d
00C6220F  4C 8B 7B 28                     mov r15, qword ptr [rbx + 0x28]
00C62213  4C 8B CA                        mov r9, rdx
00C62216  8B F7                           mov esi, edi
00C62218  E9 86 00 00 00                  jmp 0x140c622a3
00C6221D  4B 8D 04 39                     lea rax, [r9 + r15]
00C62221  48 3B C2                        cmp rax, rdx
00C62224  0F 85 EE FE FF FF               jne 0x140c62118
00C6222A  8B D6                           mov edx, esi
00C6222C  41 23 D0                        and edx, r8d
00C6222F  74 0F                           je 0x140c62240
00C62231  8B C6                           mov eax, esi
00C62233  41 23 C4                        and eax, r12d
00C62236  83 F8 02                        cmp eax, 2
00C62239  74 05                           je 0x140c62240
00C6223B  83 F8 18                        cmp eax, 0x18
00C6223E  75 17                           jne 0x140c62257
00C62240  41 85 F8                        test r8d, edi
00C62243  74 4E                           je 0x140c62293
00C62245  83 F9 02                        cmp ecx, 2
00C62248  74 49                           je 0x140c62293
00C6224A  83 F9 18                        cmp ecx, 0x18
00C6224D  74 44                           je 0x140c62293
00C6224F  85 D2                           test edx, edx
00C62251  0F 84 C1 FE FF FF               je 0x140c62118
00C62257  8B C6                           mov eax, esi
00C62259  41 23 C4                        and eax, r12d
00C6225C  83 F8 02                        cmp eax, 2
00C6225F  0F 84 B8 FE FF FF               je 0x140c6211d
00C62265  83 F8 18                        cmp eax, 0x18
00C62268  0F 84 AF FE FF FF               je 0x140c6211d
00C6226E  41 85 F8                        test r8d, edi
00C62271  0F 84 A6 FE FF FF               je 0x140c6211d
00C62277  8B C7                           mov eax, edi
00C62279  41 23 C4                        and eax, r12d
00C6227C  83 F8 02                        cmp eax, 2
00C6227F  0F 84 98 FE FF FF               je 0x140c6211d
00C62285  8B C7                           mov eax, edi
00C62287  41 23 C4                        and eax, r12d
00C6228A  83 F8 18                        cmp eax, 0x18
00C6228D  0F 84 8A FE FF FF               je 0x140c6211d
00C62293  4C 03 7B 28                     add r15, qword ptr [rbx + 0x28]
00C62297  EB 0A                           jmp 0x140c622a3
00C62299  49 83 C9 FF                     or r9, 0xffffffffffffffff
00C6229D  41 B8 00 00 00 20               mov r8d, 0x20000000
00C622A3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00C622A7  48 8B CB                        mov rcx, rbx
00C622AA  48 85 C0                        test rax, rax
00C622AD  74 23                           je 0x140c622d2
00C622AF  48 8B 08                        mov rcx, qword ptr [rax]
00C622B2  48 8B D8                        mov rbx, rax
00C622B5  48 85 C9                        test rcx, rcx
00C622B8  74 22                           je 0x140c622dc
00C622BA  48 8B 01                        mov rax, qword ptr [rcx]
00C622BD  48 8B D9                        mov rbx, rcx
00C622C0  48 8B C8                        mov rcx, rax
00C622C3  48 85 C0                        test rax, rax
00C622C6  75 F2                           jne 0x140c622ba
00C622C8  EB 12                           jmp 0x140c622dc
00C622CA  48 39 0B                        cmp qword ptr [rbx], rcx
00C622CD  74 0D                           je 0x140c622dc
00C622CF  48 8B CB                        mov rcx, rbx
00C622D2  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00C622D6  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00C622DA  75 EE                           jne 0x140c622ca
00C622DC  48 85 DB                        test rbx, rbx
00C622DF  0F 85 04 FE FF FF               jne 0x140c620e9
00C622E5  49 83 F9 FF                     cmp r9, -1
00C622E9  74 24                           je 0x140c6230f
00C622EB  41 85 F0                        test r8d, esi
00C622EE  74 11                           je 0x140c62301
00C622F0  41 23 F4                        and esi, r12d
00C622F3  83 FE 02                        cmp esi, 2
00C622F6  74 09                           je 0x140c62301
00C622F8  83 FE 18                        cmp esi, 0x18
00C622FB  74 04                           je 0x140c62301
00C622FD  44 8D 73 01                     lea r14d, [rbx + 1]
00C62301  45 8B C6                        mov r8d, r14d
00C62304  49 8B D7                        mov rdx, r15
00C62307  49 8B C9                        mov rcx, r9
00C6230A  E8 B9 19 00 00                  call 0x140c63cc8
00C6230F  48 8B 0D CA B9 1C 00            mov rcx, qword ptr [rip + 0x1cb9ca]
00C62316  41 B8 01 00 00 00               mov r8d, 1
00C6231C  48 FF C1                        inc rcx
00C6231F  48 83 CA FF                     or rdx, 0xffffffffffffffff
00C62323  E8 A0 19 00 00                  call 0x140c63cc8
00C62328  48 8B 05 B1 B9 1C 00            mov rax, qword ptr [rip + 0x1cb9b1]
00C6232F  48 8B 0D CA 38 1D 00            mov rcx, qword ptr [rip + 0x1d38ca]
00C62336  48 FF C0                        inc rax
00C62339  48 3B C8                        cmp rcx, rax
00C6233C  74 10                           je 0x140c6234e
00C6233E  BA 00 08 00 00                  mov edx, 0x800
00C62343  41 B8 01 00 00 00               mov r8d, 1
00C62349  E8 7A 19 00 00                  call 0x140c63cc8
00C6234E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00C62353  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00C62358  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00C6235D  48 83 C4 20                     add rsp, 0x20
00C62361  41 5F                           pop r15
00C62363  41 5E                           pop r14
00C62365  41 5C                           pop r12
00C62367  C3                              ret
00C62368  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreateSparsePfnDatabase(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    v_r14 = 0;
    a4 = (a4) | (-1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 352 + 8))) & (1)) == 0) goto loc_00C620D2;
    if ((*(unsigned __int64 *)(a1 + 352 + 8)) == 1) goto loc_00C6230F;
    v_rbx = (a1 + 352) | (1);
    v_rbx = (v_rbx) ^ (*(unsigned __int64 *)(a1 + 352 + 8));
    goto loc_00C620D5;
loc_00C620D2:
loc_00C620D5:
    if (*(unsigned __int64 *)(a1 + 352 + 8) == 0) goto loc_00C6230F;
loc_00C620E9:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(a1)) > 44) goto loc_00C62205;
    if (((unsigned int)(a1)) >= 44) goto loc_00C62205;
    if (a4 == -1) goto loc_00C622A3;
loc_00C62118:
    if ((((unsigned int)((unsigned int)(0x1FFFFFFFULL) + 1)) & (3)) == 0) goto loc_00C62132;
loc_00C6211D:
    result = (unsigned int)((3) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 2) goto loc_00C62132;
    if (((unsigned int)(result)) == 24) {
        a3 = 0;
    }
    result = MxMapPfnRange(a4, 0, a3, a4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 30) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 31) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 6) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 32) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 34) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 23) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 3) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 22) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 42) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 38) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 39) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 44) goto loc_00C62299;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 40) goto loc_00C62299;
    goto loc_00C6229D;
loc_00C62205:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 32)) != -1) goto loc_00C6221D;
    goto loc_00C622A3;
loc_00C6221D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 32) + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 40) * 1) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 32))) goto loc_00C62118;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))))) & ((unsigned int)(a3)));
    if (condition_is_equal) goto loc_00C62240;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 2) goto loc_00C62240;
    if (((unsigned int)(result)) != 24) goto loc_00C62257;
loc_00C62240:
    if ((((unsigned int)(a3)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) == 0) goto loc_00C62293;
    if (((unsigned int)(a4)) == 2) goto loc_00C62293;
    if (((unsigned int)(a4)) == 24) goto loc_00C62293;
    if ((unsigned int)(a2) == 0) goto loc_00C62118;
loc_00C62257:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 2) goto loc_00C6211D;
    if (((unsigned int)(result)) == 24) goto loc_00C6211D;
    if ((((unsigned int)(a3)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) == 0) goto loc_00C6211D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 2) goto loc_00C6211D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(result)) == 24) goto loc_00C6211D;
loc_00C62293:
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 40)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 40));
    goto loc_00C622A3;
loc_00C62299:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 32)) | (-1);
loc_00C6229D:
loc_00C622A3:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8) == 0) goto loc_00C622D2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8)) == 0) goto loc_00C622DC;
loc_00C622BA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8))) != 0) goto loc_00C622BA;
    goto loc_00C622DC;
loc_00C622CA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8))))) goto loc_00C622DC;
loc_00C622D2:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00C622CA;
loc_00C622DC:
    if (v_rbx != 0) goto loc_00C620E9;
    if (a4 == -1) goto loc_00C6230F;
    if ((((unsigned int)((unsigned int)(0x20000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))))) == 0) goto loc_00C62301;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 352 + 8) + 24))))) & ((unsigned int)((unsigned int)(0x1FFFFFFFULL))));
    if (((unsigned int)(v_rsi)) == 2) goto loc_00C62301;
    if (((unsigned int)(v_rsi)) != 24) {
        v_r14 = v_rbx + 1;
    }
    result = MxMapPfnRange(a4, v_r15, (unsigned int)((unsigned int)(v_r14)), a4);
loc_00C6230F:
    a1 = (*(unsigned __int64 *)(v_rip + 1882570)) + 1;
    a2 = (v_r15) | (-1);
    result = MxMapPfnRange(a1, a2, 1, a4);
    result = (*(unsigned __int64 *)(v_rip + 1882545)) + 1;
    if ((*(unsigned __int64 *)(v_rip + 1915082)) != result) {
        a2 = 0x800ULL;
        a3 = 1;
        result = MxMapPfnRange(*(unsigned __int64 *)(v_rip + 1915082), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreateSparsePfnDatabase(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    local_r14 = 0;
    Arg4 = (Arg4) | (-1);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x160 + 0x8))) & (1)) == 0) goto loc_00C620D2;
    if ((*(uint64_t *)(arg1 + 0x160 + 0x8)) == 1) goto loc_00C6230F;
    local_rbx = (Arg1 + 352) | (1);
    local_rbx = (local_rbx) ^ (*(uint64_t *)(arg1 + 0x160 + 0x8));
    goto loc_00C620D5;
loc_00C620D2:
loc_00C620D5:
    if (*(uint64_t *)(arg1 + 0x160 + 0x8) == 0) goto loc_00C6230F;
loc_00C620E9:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(Arg1)) > 44) goto loc_00C62205;
    if (((uint32_t)(Arg1)) >= 44) goto loc_00C62205;
    if (Arg4 == -1) goto loc_00C622A3;
loc_00C62118:
    if ((((uint32_t)((uint32_t)(0x1FFFFFFFULL) + 1)) & (3)) == 0) goto loc_00C62132;
loc_00C6211D:
    result = (uint32_t)((3) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 2) goto loc_00C62132;
    if (((uint32_t)(result)) == 24) {
        Arg3 = 0;
    }
    result = MxMapPfnRange(Arg4, 0, Arg3, Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 30) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 31) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 6) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 32) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 34) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 23) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 3) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 22) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 42) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 38) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 39) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 44) goto loc_00C62299;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 40) goto loc_00C62299;
    goto loc_00C6229D;
loc_00C62205:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x20)) != -1) goto loc_00C6221D;
    goto loc_00C622A3;
loc_00C6221D:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x20) + *(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x28) * 1) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x20))) goto loc_00C62118;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))))) & ((uint32_t)(Arg3)));
    if (condition_is_equal) goto loc_00C62240;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 2) goto loc_00C62240;
    if (((uint32_t)(result)) != 24) goto loc_00C62257;
loc_00C62240:
    if ((((uint32_t)(Arg3)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) == 0) goto loc_00C62293;
    if (((uint32_t)(Arg4)) == 2) goto loc_00C62293;
    if (((uint32_t)(Arg4)) == 24) goto loc_00C62293;
    if ((uint32_t)(Arg2) == 0) goto loc_00C62118;
loc_00C62257:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 2) goto loc_00C6211D;
    if (((uint32_t)(result)) == 24) goto loc_00C6211D;
    if ((((uint32_t)(Arg3)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) == 0) goto loc_00C6211D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 2) goto loc_00C6211D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(result)) == 24) goto loc_00C6211D;
loc_00C62293:
    local_r15 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x28)) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x28));
    goto loc_00C622A3;
loc_00C62299:
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x20)) | (-1);
loc_00C6229D:
loc_00C622A3:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8) == 0) goto loc_00C622D2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8)) == 0) goto loc_00C622DC;
loc_00C622BA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8))) != 0) goto loc_00C622BA;
    goto loc_00C622DC;
loc_00C622CA:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8))))) goto loc_00C622DC;
loc_00C622D2:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00C622CA;
loc_00C622DC:
    if (local_rbx != 0) goto loc_00C620E9;
    if (Arg4 == -1) goto loc_00C6230F;
    if ((((uint32_t)((uint32_t)(0x20000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))))) == 0) goto loc_00C62301;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x18))))) & ((uint32_t)((uint32_t)(0x1FFFFFFFULL))));
    if (((uint32_t)(local_rsi)) == 2) goto loc_00C62301;
    if (((uint32_t)(local_rsi)) != 24) {
        local_r14 = local_rbx + 1;
    }
    result = MxMapPfnRange(Arg4, local_r15, (uint32_t)((uint32_t)(local_r14)), Arg4);
loc_00C6230F:
    Arg1 = (*(uint64_t *)(v_rip + 0x1CB9CA)) + 1;
    Arg2 = (local_r15) | (-1);
    result = MxMapPfnRange(Arg1, Arg2, 1, Arg4);
    result = (*(uint64_t *)(v_rip + 0x1CB9B1)) + 1;
    if ((*(uint64_t *)(v_rip + 0x1D38CA)) != result) {
        Arg2 = 0x800ULL;
        Arg3 = 1;
        result = MxMapPfnRange(*(uint64_t *)(v_rip + 0x1D38CA), Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C62088&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
