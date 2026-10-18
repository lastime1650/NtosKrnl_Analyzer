# sub_0030E8E0

- RVA: `0x0030E8E0`–`0x0030EC39` (길이 `857` bytes)
- VA: `0x000000014030E8E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073F40`
- 디코드: `219`개 명령, `857/857` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0030E9C1` → [KiCheckVpBackingLongSpinWaitHypercall](KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0030E9CC` → [HvlNotifyLongSpinWait](HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0030EAE2` → [KiCheckVpBackingLongSpinWaitHypercall](KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0030EAED` → [HvlNotifyLongSpinWait](HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0030EB47` → [KiAcquirePrcbLocksForIsolationUnit](KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0030EB66` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0030EBE3` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0030EC0D` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0030EC25` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0030E8E8` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0030E9A2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0030E9B7` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0030EB05` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0030EB28` → [sub_006E0EAA](../6E/Unknown_function_006E0EAA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030E8E0  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0030E8E5  4C 8B F9                        mov r15, rcx
0030E8E8  4C 8D 0D 51 A3 CB 00            lea r9, [rip + 0xcba351]
0030E8EF  45 33 C0                        xor r8d, r8d
0030E8F2  41 0F B6 97 84 01 00 00         movzx edx, byte ptr [r15 + 0x184]
0030E8FA  4D 8B E8                        mov r13, r8
0030E8FD  88 94 24 80 00 00 00            mov byte ptr [rsp + 0x80], dl
0030E904  4D 8B E0                        mov r12, r8
0030E907  8B CA                           mov ecx, edx
0030E909  83 FA 03                        cmp edx, 3
0030E90C  0F 85 C1 00 00 00               jne 0x14030e9d3
0030E912  45 8B B7 18 02 00 00            mov r14d, dword ptr [r15 + 0x218]
0030E919  45 85 F6                        test r14d, r14d
0030E91C  78 D4                           js 0x14030e8f2
0030E91E  4F 8B 2C F1                     mov r13, qword ptr [r9 + r14*8]
0030E922  49 8B C5                        mov rax, r13
0030E925  48 83 C8 01                     or rax, 1
0030E929  48 89 45 00                     mov qword ptr [rbp], rax
0030E92D  49 8B 85 58 8E 00 00            mov rax, qword ptr [r13 + 0x8e58]
0030E934  0F B6 08                        movzx ecx, byte ptr [rax]
0030E937  48 8D 70 08                     lea rsi, [rax + 8]
0030E93B  84 C9                           test cl, cl
0030E93D  74 31                           je 0x14030e970
0030E93F  8B E9                           mov ebp, ecx
0030E941  48 8B 1E                        mov rbx, qword ptr [rsi]
0030E944  41 8B F8                        mov edi, r8d
0030E947  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
0030E94E  72 50                           jb 0x14030e9a0
0030E950  48 83 C6 08                     add rsi, 8
0030E954  41 B8 00 00 00 00               mov r8d, 0
0030E95A  48 83 ED 01                     sub rbp, 1
0030E95E  75 E1                           jne 0x14030e941
0030E960  0F B6 94 24 80 00 00 00         movzx edx, byte ptr [rsp + 0x80]
0030E968  48 8B AC 24 90 00 00 00         mov rbp, qword ptr [rsp + 0x90]
0030E970  4D 3B 7D 10                     cmp r15, qword ptr [r13 + 0x10]
0030E974  74 7B                           je 0x14030e9f1
0030E976  41 0F B6 87 84 01 00 00         movzx eax, byte ptr [r15 + 0x184]
0030E97E  3C 03                           cmp al, 3
0030E980  0F 85 DD 01 00 00               jne 0x14030eb63
0030E986  41 8B 87 18 02 00 00            mov eax, dword ptr [r15 + 0x218]
0030E98D  41 3B C6                        cmp eax, r14d
0030E990  0F 85 CD 01 00 00               jne 0x14030eb63
0030E996  B9 1E 00 00 00                  mov ecx, 0x1e
0030E99B  CD 29                           int 0x29
0030E99D  0F 1F 00                        nop dword ptr [rax]
0030E9A0  FF C7                           inc edi
0030E9A2  85 3D 04 69 CB 00               test dword ptr [rip + 0xcb6904], edi
0030E9A8  74 0D                           je 0x14030e9b7
0030E9AA  F3 90                           pause
0030E9AC  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0030E9B0  48 85 C0                        test rax, rax
0030E9B3  74 92                           je 0x14030e947
0030E9B5  EB E9                           jmp 0x14030e9a0
0030E9B7  8B 05 FB 80 CB 00               mov eax, dword ptr [rip + 0xcb80fb]
0030E9BD  A8 40                           test al, 0x40
0030E9BF  74 E9                           je 0x14030e9aa
0030E9C1  E8 CA 0A 00 00                  call 0x14030f490
0030E9C6  84 C0                           test al, al
0030E9C8  74 E0                           je 0x14030e9aa
0030E9CA  8B CF                           mov ecx, edi
0030E9CC  E8 8F 0A 00 00                  call 0x14030f460
0030E9D1  EB D9                           jmp 0x14030e9ac
0030E9D3  83 E9 01                        sub ecx, 1
0030E9D6  0F 84 18 01 00 00               je 0x14030eaf4
0030E9DC  83 E9 01                        sub ecx, 1
0030E9DF  74 4D                           je 0x14030ea2e
0030E9E1  83 F9 03                        cmp ecx, 3
0030E9E4  75 0B                           jne 0x14030e9f1
0030E9E6  41 0F B6 47 70                  movzx eax, byte ptr [r15 + 0x70]
0030E9EB  24 07                           and al, 7
0030E9ED  3C 01                           cmp al, 1
0030E9EF  75 2E                           jne 0x14030ea1f
0030E9F1  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0030E9F9  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0030E9FE  4C 89 28                        mov qword ptr [rax], r13
0030EA01  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0030EA09  4C 89 20                        mov qword ptr [rax], r12
0030EA0C  0F B6 C2                        movzx eax, dl
0030EA0F  48 83 C4 40                     add rsp, 0x40
0030EA13  41 5F                           pop r15
0030EA15  41 5D                           pop r13
0030EA17  41 5C                           pop r12
0030EA19  5F                              pop rdi
0030EA1A  5E                              pop rsi
0030EA1B  5D                              pop rbp
0030EA1C  5B                              pop rbx
0030EA1D  C3                              ret
0030EA1E  CC                              int3
0030EA1F  2C 03                           sub al, 3
0030EA21  3C 03                           cmp al, 3
0030EA23  76 CC                           jbe 0x14030e9f1
0030EA25  B2 02                           mov dl, 2
0030EA27  88 94 24 80 00 00 00            mov byte ptr [rsp + 0x80], dl
0030EA2E  45 8B B7 18 02 00 00            mov r14d, dword ptr [r15 + 0x218]
0030EA35  45 85 F6                        test r14d, r14d
0030EA38  0F 88 B4 FE FF FF               js 0x14030e8f2
0030EA3E  4F 8B 2C F1                     mov r13, qword ptr [r9 + r14*8]
0030EA42  49 8B C5                        mov rax, r13
0030EA45  48 83 C8 01                     or rax, 1
0030EA49  48 89 45 00                     mov qword ptr [rbp], rax
0030EA4D  49 8B 85 58 8E 00 00            mov rax, qword ptr [r13 + 0x8e58]
0030EA54  0F B6 08                        movzx ecx, byte ptr [rax]
0030EA57  48 8D 70 08                     lea rsi, [rax + 8]
0030EA5B  84 C9                           test cl, cl
0030EA5D  74 48                           je 0x14030eaa7
0030EA5F  8B E9                           mov ebp, ecx
0030EA61  48 8B 1E                        mov rbx, qword ptr [rsi]
0030EA64  41 8B F8                        mov edi, r8d
0030EA67  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
0030EA6E  73 17                           jae 0x14030ea87
0030EA70  FF C7                           inc edi
0030EA72  85 3D 34 68 CB 00               test dword ptr [rip + 0xcb6834], edi
0030EA78  74 5E                           je 0x14030ead8
0030EA7A  F3 90                           pause
0030EA7C  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0030EA80  48 85 C0                        test rax, rax
0030EA83  74 E2                           je 0x14030ea67
0030EA85  EB E9                           jmp 0x14030ea70
0030EA87  48 83 C6 08                     add rsi, 8
0030EA8B  41 B8 00 00 00 00               mov r8d, 0
0030EA91  48 83 ED 01                     sub rbp, 1
0030EA95  75 CA                           jne 0x14030ea61
0030EA97  0F B6 94 24 80 00 00 00         movzx edx, byte ptr [rsp + 0x80]
0030EA9F  48 8B AC 24 90 00 00 00         mov rbp, qword ptr [rsp + 0x90]
0030EAA7  4D 3B 7D 08                     cmp r15, qword ptr [r13 + 8]
0030EAAB  0F 84 40 FF FF FF               je 0x14030e9f1
0030EAB1  41 0F B6 87 84 01 00 00         movzx eax, byte ptr [r15 + 0x184]
0030EAB9  3C 02                           cmp al, 2
0030EABB  0F 85 A2 00 00 00               jne 0x14030eb63
0030EAC1  41 8B 87 18 02 00 00            mov eax, dword ptr [r15 + 0x218]
0030EAC8  41 3B C6                        cmp eax, r14d
0030EACB  0F 85 92 00 00 00               jne 0x14030eb63
0030EAD1  B9 4A 00 00 00                  mov ecx, 0x4a
0030EAD6  CD 29                           int 0x29
0030EAD8  8B 05 DA 7F CB 00               mov eax, dword ptr [rip + 0xcb7fda]
0030EADE  A8 40                           test al, 0x40
0030EAE0  74 98                           je 0x14030ea7a
0030EAE2  E8 A9 09 00 00                  call 0x14030f490
0030EAE7  84 C0                           test al, al
0030EAE9  74 8F                           je 0x14030ea7a
0030EAEB  8B CF                           mov ecx, edi
0030EAED  E8 6E 09 00 00                  call 0x14030f460
0030EAF2  EB 88                           jmp 0x14030ea7c
0030EAF4  41 8B 9F 18 02 00 00            mov ebx, dword ptr [r15 + 0x218]
0030EAFB  85 DB                           test ebx, ebx
0030EAFD  79 3C                           jns 0x14030eb3b
0030EAFF  8B C3                           mov eax, ebx
0030EB01  0F BA F0 1F                     btr eax, 0x1f
0030EB05  F7 05 29 80 CB 00 00 00 20 00   test dword ptr [rip + 0xcb8029], 0x200000
0030EB0F  49 8B 04 C1                     mov rax, qword ptr [r9 + rax*8]
0030EB13  4C 8B A0 48 8E 00 00            mov r12, qword ptr [rax + 0x8e48]
0030EB1A  75 54                           jne 0x14030eb70
0030EB1C  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0030EB21  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
0030EB28  0F 82 7C 23 3D 00               jb 0x1406e0eaa
0030EB2E  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
0030EB36  E9 EF 00 00 00                  jmp 0x14030ec2a
0030EB3B  4D 8B 2C D9                     mov r13, qword ptr [r9 + rbx*8]
0030EB3F  4C 8B C5                        mov r8, rbp
0030EB42  49 8B CD                        mov rcx, r13
0030EB45  33 D2                           xor edx, edx
0030EB47  E8 14 02 00 00                  call 0x14030ed60
0030EB4C  41 0F B6 87 84 01 00 00         movzx eax, byte ptr [r15 + 0x184]
0030EB54  3C 01                           cmp al, 1
0030EB56  75 0B                           jne 0x14030eb63
0030EB58  41 8B 87 18 02 00 00            mov eax, dword ptr [r15 + 0x218]
0030EB5F  3B C3                           cmp eax, ebx
0030EB61  74 47                           je 0x14030ebaa
0030EB63  48 8B CD                        mov rcx, rbp
0030EB66  E8 E5 B0 08 00                  call 0x140399c50
0030EB6B  E9 78 FD FF FF                  jmp 0x14030e8e8
0030EB70  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
0030EB78  48 8B D7                        mov rdx, rdi
0030EB7B  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0030EB7F  4C 89 07                        mov qword ptr [rdi], r8
0030EB82  90                              nop
0030EB83  49 87 14 24                     xchg qword ptr [r12], rdx
0030EB87  48 85 D2                        test rdx, rdx
0030EB8A  0F 85 92 00 00 00               jne 0x14030ec22
0030EB90  41 0F B6 87 84 01 00 00         movzx eax, byte ptr [r15 + 0x184]
0030EB98  3C 01                           cmp al, 1
0030EB9A  75 1B                           jne 0x14030ebb7
0030EB9C  41 8B 87 18 02 00 00            mov eax, dword ptr [r15 + 0x218]
0030EBA3  3B C3                           cmp eax, ebx
0030EBA5  75 10                           jne 0x14030ebb7
0030EBA7  4D 8B E8                        mov r13, r8
0030EBAA  0F B6 94 24 80 00 00 00         movzx edx, byte ptr [rsp + 0x80]
0030EBB2  E9 3A FE FF FF                  jmp 0x14030e9f1
0030EBB7  F7 05 77 7F CB 00 00 00 20 00   test dword ptr [rip + 0xcb7f77], 0x200000
0030EBC1  74 54                           je 0x14030ec17
0030EBC3  0F 0D 0F                        prefetchw byte ptr [rdi]
0030EBC6  48 8B 07                        mov rax, qword ptr [rdi]
0030EBC9  48 85 C0                        test rax, rax
0030EBCC  75 1D                           jne 0x14030ebeb
0030EBCE  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0030EBD2  48 8B C7                        mov rax, rdi
0030EBD5  F0 4C 0F B1 01                  lock cmpxchg qword ptr [rcx], r8
0030EBDA  0F 84 12 FD FF FF               je 0x14030e8f2
0030EBE0  48 8B CF                        mov rcx, rdi
0030EBE3  E8 B8 8E F0 FF                  call 0x140217aa0
0030EBE8  45 33 C0                        xor r8d, r8d
0030EBEB  48 8D 48 08                     lea rcx, [rax + 8]
0030EBEF  4C 89 07                        mov qword ptr [rdi], r8
0030EBF2  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0030EBF6  4C 8D 0D 43 A0 CB 00            lea r9, [rip + 0xcba043]
0030EBFD  48 8B C2                        mov rax, rdx
0030EC00  48 87 01                        xchg qword ptr [rcx], rax
0030EC03  32 C2                           xor al, dl
0030EC05  A8 04                           test al, 4
0030EC07  0F 84 E5 FC FF FF               je 0x14030e8f2
0030EC0D  E8 0E 90 F0 FF                  call 0x140217c20
0030EC12  E9 D1 FC FF FF                  jmp 0x14030e8e8
0030EC17  F0 49 83 24 24 00               lock and qword ptr [r12], 0
0030EC1D  E9 D0 FC FF FF                  jmp 0x14030e8f2
0030EC22  48 8B CF                        mov rcx, rdi
0030EC25  E8 86 92 F4 FF                  call 0x140257eb0
0030EC2A  4C 8D 0D 0F A0 CB 00            lea r9, [rip + 0xcba00f]
0030EC31  45 33 C0                        xor r8d, r8d
0030EC34  E9 57 FF FF FF                  jmp 0x14030eb90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0030E8E0(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, unsigned __int8 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p80;
    unsigned int v_stack_p98;
    unsigned __int8 v_stack_pF8;

    v_stack_p38 = v_r14;
loc_0030E8E8:
    a3 = 0;
loc_0030E8F2:
    v_stack_p80 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 388));
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 388))) != 3) goto loc_0030E9D3;
    if (sign_flag) goto loc_0030E8F2;
    result = (*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8)) | (1);
    *(unsigned __int64 *)(v_rbp) = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))) == 0) goto loc_0030E970;
loc_0030E941:
loc_0030E947:
    if (condition_is_below) goto loc_0030E9A0;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8) + (8);
    v_rbp = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0030E941;
loc_0030E970:
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16))) goto loc_0030E9F1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 3) goto loc_0030EB63;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0030EB63;
loc_0030E9A0:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13330692)) & ((unsigned int)(v_rdi))) == 0) goto loc_0030E9B7;
loc_0030E9AA:
loc_0030E9AC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8) + 48) == 0) goto loc_0030E947;
    goto loc_0030E9A0;
loc_0030E9B7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13336827)))) & (64)) == 0) goto loc_0030E9AA;
    result = KiCheckVpBackingLongSpinWaitHypercall(30, a16, 0, v_rip + 13345617);
    if ((unsigned __int8)(result) == 0) goto loc_0030E9AA;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a16, 0, v_rip + 13345617);
    goto loc_0030E9AC;
loc_0030E9D3:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (1));
    if (condition_is_equal) goto loc_0030EAF4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0030EA2E;
    if (((unsigned int)(a1)) != 3) goto loc_0030E9F1;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 112)) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_0030EA1F;
loc_0030E9F1:
    *(unsigned __int64 *)(a17) = *(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8);
    *(unsigned __int64 *)(a19) = 0;
    v_rsp = (v_rsp) + (64);
    return a16;
loc_0030EA1F:
    result = (unsigned __int8)((a16) - (3));
    if (((unsigned __int8)(result)) <= 3) goto loc_0030E9F1;
    v_stack_pF8 = 2;
loc_0030EA2E:
    if (sign_flag) goto loc_0030E8F2;
    result = (*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8)) | (1);
    *(unsigned __int64 *)(a18) = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))) == 0) goto loc_0030EAA7;
loc_0030EA61:
loc_0030EA67:
    if (condition_is_above_or_equal) goto loc_0030EA87;
loc_0030EA70:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13330484)) & ((unsigned int)(v_rdi))) == 0) goto loc_0030EAD8;
loc_0030EA7A:
loc_0030EA7C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8) + 48) == 0) goto loc_0030EA67;
    goto loc_0030EA70;
loc_0030EA87:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440) + 8) + (8);
    v_rbp = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0030EA61;
loc_0030EAA7:
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 8))) goto loc_0030E9F1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 2) goto loc_0030EB63;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0030EB63;
loc_0030EAD8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13336538)))) & (64)) == 0) goto loc_0030EA7A;
    result = KiCheckVpBackingLongSpinWaitHypercall(74, a16, 0, v_rip + 13345617);
    if ((unsigned __int8)(result) == 0) goto loc_0030EA7A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a16, 0, v_rip + 13345617);
    goto loc_0030EA7C;
loc_0030EAF4:
    if (!sign_flag) goto loc_0030EB3B;
    if (((*(unsigned int *)(v_rip + 13336617)) & (0x200000ULL)) != 0) goto loc_0030EB70;
    v_stack_p98 = 0;
    goto loc_0030EC2A;
loc_0030EB3B:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, a18, v_rip + 13345617);
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_0030EB63;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0030EBAA;
loc_0030EB63:
    result = KiReleasePrcbLocksForIsolationUnit(a18, a2, a18, v_rip + 13345617);
    goto loc_0030E8E8;
loc_0030EB70:
    *(unsigned __int64 *)(a20 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13345617 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424);
    *(unsigned __int64 *)(a20) = a18;
    if (a20 != 0) goto loc_0030EC22;
loc_0030EB90:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_0030EBB7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0030EBB7;
loc_0030EBAA:
    goto loc_0030E9F1;
loc_0030EBB7:
    if (((*(unsigned int *)(v_rip + 13336439)) & (0x200000ULL)) == 0) goto loc_0030EC17;
    if (*(unsigned __int64 *)(a20) != 0) goto loc_0030EBEB;
    if (*(unsigned __int64 *)(a20) == 0) goto loc_0030E8F2;
    result = KxWaitForLockChainValid(a20, a16, a18, v_rip + 13345617);
    a3 = 0;
loc_0030EBEB:
    *(unsigned __int64 *)(a20) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(a20 + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(a20 + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0030E8F2;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(a20 + 8), a3, v_rip + 13344835);
    goto loc_0030E8E8;
loc_0030EC17:
    goto loc_0030E8F2;
loc_0030EC22:
    result = KxWaitForLockOwnerShip(a20, *(unsigned __int64 *)(a20 + 8), a3, v_rip + 13344835);
loc_0030EC2A:
    a3 = 0;
    goto loc_0030EB90;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0030E8E0(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint8_t Arg16, void *Arg17, int64_t Arg18, void *Arg19, void *Arg20)
{
    uint8_t *arg17 = (uint8_t *)Arg17;
    uint8_t *arg19 = (uint8_t *)Arg19;
    uint8_t *arg20 = (uint8_t *)Arg20;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p38;
    uint8_t v_stack_p80;
    uint32_t v_stack_p98;
    uint8_t v_stack_pF8;

    v_stack_p38 = local_r14;
loc_0030E8E8:
    Arg3 = 0;
loc_0030E8F2:
    v_stack_p80 = (uint8_t)(*(uint8_t *)(Arg1 + 0x184));
    if (((uint32_t)(*(uint8_t *)(Arg1 + 0x184))) != 3) goto loc_0030E9D3;
    if (sign_flag) goto loc_0030E8F2;
    result = (*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8)) | (1);
    *(uint64_t *)(local_rbp) = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58))) == 0) goto loc_0030E970;
loc_0030E941:
loc_0030E947:
    if (condition_is_below) goto loc_0030E9A0;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58) + 8) + (8);
    local_rbp = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0030E941;
loc_0030E970:
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x10))) goto loc_0030E9F1;
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 3) goto loc_0030EB63;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0030EB63;
loc_0030E9A0:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xCB6904)) & ((uint32_t)(local_rdi))) == 0) goto loc_0030E9B7;
loc_0030E9AA:
loc_0030E9AC:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58) + 0x8) + 0x30) == 0) goto loc_0030E947;
    goto loc_0030E9A0;
loc_0030E9B7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB80FB)))) & (64)) == 0) goto loc_0030E9AA;
    result = KiCheckVpBackingLongSpinWaitHypercall(30, Arg16, 0, v_rip + 13345617);
    if ((uint8_t)(result) == 0) goto loc_0030E9AA;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg16, 0, v_rip + 13345617);
    goto loc_0030E9AC;
loc_0030E9D3:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (1));
    if (condition_is_equal) goto loc_0030EAF4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0030EA2E;
    if (((uint32_t)(Arg1)) != 3) goto loc_0030E9F1;
    result = (uint8_t)((*(uint8_t *)(Arg1 + 0x70)) & (7));
    if (((uint8_t)(result)) != 1) goto loc_0030EA1F;
loc_0030E9F1:
    *(uint64_t *)(arg17) = *(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8);
    *(uint64_t *)(arg19) = 0;
    local_rsp = (local_rsp) + (64);
    return Arg16;
loc_0030EA1F:
    result = (uint8_t)((Arg16) - (3));
    if (((uint8_t)(result)) <= 3) goto loc_0030E9F1;
    v_stack_pF8 = 2;
loc_0030EA2E:
    if (sign_flag) goto loc_0030E8F2;
    result = (*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8)) | (1);
    *(uint64_t *)(Arg18) = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58))) == 0) goto loc_0030EAA7;
loc_0030EA61:
loc_0030EA67:
    if (condition_is_above_or_equal) goto loc_0030EA87;
loc_0030EA70:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xCB6834)) & ((uint32_t)(local_rdi))) == 0) goto loc_0030EAD8;
loc_0030EA7A:
loc_0030EA7C:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58) + 0x8) + 0x30) == 0) goto loc_0030EA67;
    goto loc_0030EA70;
loc_0030EA87:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58) + 8) + (8);
    local_rbp = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0030EA61;
loc_0030EAA7:
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8))) goto loc_0030E9F1;
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 2) goto loc_0030EB63;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0030EB63;
loc_0030EAD8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB7FDA)))) & (64)) == 0) goto loc_0030EA7A;
    result = KiCheckVpBackingLongSpinWaitHypercall(74, Arg16, 0, v_rip + 13345617);
    if ((uint8_t)(result) == 0) goto loc_0030EA7A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg16, 0, v_rip + 13345617);
    goto loc_0030EA7C;
loc_0030EAF4:
    if (!sign_flag) goto loc_0030EB3B;
    if (((*(uint32_t *)(v_rip + 0xCB8029)) & (0x200000ULL)) != 0) goto loc_0030EB70;
    v_stack_p98 = 0;
    goto loc_0030EC2A;
loc_0030EB3B:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), Arg2, Arg18, v_rip + 13345617);
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 1) goto loc_0030EB63;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0030EBAA;
loc_0030EB63:
    result = KiReleasePrcbLocksForIsolationUnit(Arg18, Arg2, Arg18, v_rip + 13345617);
    goto loc_0030E8E8;
loc_0030EB70:
    *(uint64_t *)(arg20 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xCBA351 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) * 8) + 0x8E48);
    *(uint64_t *)(arg20) = Arg18;
    if (Arg20 != NULL) goto loc_0030EC22;
loc_0030EB90:
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 1) goto loc_0030EBB7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0030EBB7;
loc_0030EBAA:
    goto loc_0030E9F1;
loc_0030EBB7:
    if (((*(uint32_t *)(v_rip + 0xCB7F77)) & (0x200000ULL)) == 0) goto loc_0030EC17;
    if (*(uint64_t *)(arg20) != 0) goto loc_0030EBEB;
    if (*(uint64_t *)(arg20) == 0) goto loc_0030E8F2;
    result = KxWaitForLockChainValid(Arg20, Arg16, Arg18, v_rip + 13345617);
    Arg3 = 0;
loc_0030EBEB:
    *(uint64_t *)(arg20) = 0;
    result = (uint8_t)((*(uint64_t *)(arg20 + 0x8)) ^ ((uint8_t)(*(uint64_t *)(arg20 + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0030E8F2;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(arg20 + 0x8), Arg3, v_rip + 13344835);
    goto loc_0030E8E8;
loc_0030EC17:
    goto loc_0030E8F2;
loc_0030EC22:
    result = KxWaitForLockOwnerShip(Arg20, *(uint64_t *)(arg20 + 0x8), Arg3, v_rip + 13344835);
loc_0030EC2A:
    Arg3 = 0;
    goto loc_0030EB90;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg17` | `+ 0x0` | `64` | `W` |
| `Arg19` | `+ 0x0` | `64` | `W` |
| `Arg20` | `+ 0x0` | `8` | `R` |
| `Arg20` | `+ 0x0` | `64` | `R` |
| `Arg20` | `+ 0x0` | `64` | `W` |
| `Arg20` | `+ 0x8` | `64` | `R` |
| `Arg20` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030E8E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
