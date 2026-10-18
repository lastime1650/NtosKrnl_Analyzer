# PiSwValidateCreateData

- RVA: `0x008DB958`–`0x008DBC7C` (길이 `804` bytes)
- VA: `0x00000001408DB958`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008584C`
- 디코드: `224`개 명령, `804/804` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DBA7B` → [PnpValidateMultiSz](PnpValidateMultiSz_function_008DC56C.md) (function, `0x008DC56C`)
- `0x008DBAF9` → [PnpValidateMultiSz](PnpValidateMultiSz_function_008DC56C.md) (function, `0x008DC56C`)
- `0x008DBBAC` → [PiSwValidatePropertyArray](../8F/PiSwValidatePropertyArray_function_008F75F4.md) (function, `0x008F75F4`)
- `0x008DBC35` → [SeValidSecurityDescriptor](../8B/SeValidSecurityDescriptor_function_008BED60.md) (function, `0x008BED60`)

### Direct callers
- [PiSwIrpStartCreateWorker](PiSwIrpStartCreateWorker_function_008DB398.md) at `0x008DB3DC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DB958  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DB95D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
008DB962  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008DB967  57                              push rdi
008DB968  48 83 EC 20                     sub rsp, 0x20
008DB96C  33 ED                           xor ebp, ebp
008DB96E  48 8B D9                        mov rbx, rcx
008DB971  BE 0D 00 00 C0                  mov esi, 0xc000000d
008DB976  48 85 C9                        test rcx, rcx
008DB979  74 71                           je 0x1408db9ec
008DB97B  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
008DB97F  48 85 C9                        test rcx, rcx
008DB982  74 68                           je 0x1408db9ec
008DB984  66 39 29                        cmp word ptr [rcx], bp
008DB987  74 63                           je 0x1408db9ec
008DB989  48 83 CF FF                     or rdi, 0xffffffffffffffff
008DB98D  48 8B C7                        mov rax, rdi
008DB990  48 FF C0                        inc rax
008DB993  66 39 2C 41                     cmp word ptr [rcx + rax*2], bp
008DB997  75 F7                           jne 0x1408db990
008DB999  41 BA C7 00 00 00               mov r10d, 0xc7
008DB99F  49 3B C2                        cmp rax, r10
008DB9A2  77 48                           ja 0x1408db9ec
008DB9A4  4C 8B 03                        mov r8, qword ptr [rbx]
008DB9A7  4D 85 C0                        test r8, r8
008DB9AA  74 40                           je 0x1408db9ec
008DB9AC  41 0F B7 08                     movzx ecx, word ptr [r8]
008DB9B0  66 85 C9                        test cx, cx
008DB9B3  74 37                           je 0x1408db9ec
008DB9B5  49 8B D0                        mov rdx, r8
008DB9B8  66 85 C9                        test cx, cx
008DB9BB  74 1E                           je 0x1408db9db
008DB9BD  8D 41 DF                        lea eax, [rcx - 0x21]
008DB9C0  66 83 F8 5E                     cmp ax, 0x5e
008DB9C4  77 26                           ja 0x1408db9ec
008DB9C6  66 83 F9 2C                     cmp cx, 0x2c
008DB9CA  74 20                           je 0x1408db9ec
008DB9CC  66 83 F9 5C                     cmp cx, 0x5c
008DB9D0  74 1A                           je 0x1408db9ec
008DB9D2  48 83 C2 02                     add rdx, 2
008DB9D6  0F B7 0A                        movzx ecx, word ptr [rdx]
008DB9D9  EB DD                           jmp 0x1408db9b8
008DB9DB  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
008DB9DF  48 85 D2                        test rdx, rdx
008DB9E2  74 08                           je 0x1408db9ec
008DB9E4  0F B7 0A                        movzx ecx, word ptr [rdx]
008DB9E7  66 85 C9                        test cx, cx
008DB9EA  75 18                           jne 0x1408dba04
008DB9EC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008DB9F1  8B C6                           mov eax, esi
008DB9F3  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
008DB9F8  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
008DB9FD  48 83 C4 20                     add rsp, 0x20
008DBA01  5F                              pop rdi
008DBA02  C3                              ret
008DBA03  CC                              int3
008DBA04  4C 8B CA                        mov r9, rdx
008DBA07  66 85 C9                        test cx, cx
008DBA0A  74 1F                           je 0x1408dba2b
008DBA0C  8D 41 DF                        lea eax, [rcx - 0x21]
008DBA0F  66 83 F8 5E                     cmp ax, 0x5e
008DBA13  77 D7                           ja 0x1408db9ec
008DBA15  66 83 F9 2C                     cmp cx, 0x2c
008DBA19  74 D1                           je 0x1408db9ec
008DBA1B  66 83 F9 5C                     cmp cx, 0x5c
008DBA1F  74 CB                           je 0x1408db9ec
008DBA21  49 83 C1 02                     add r9, 2
008DBA25  41 0F B7 09                     movzx ecx, word ptr [r9]
008DBA29  EB DC                           jmp 0x1408dba07
008DBA2B  48 8B CF                        mov rcx, rdi
008DBA2E  48 FF C1                        inc rcx
008DBA31  66 39 2C 4A                     cmp word ptr [rdx + rcx*2], bp
008DBA35  75 F7                           jne 0x1408dba2e
008DBA37  48 8B C7                        mov rax, rdi
008DBA3A  48 FF C0                        inc rax
008DBA3D  66 41 39 2C 40                  cmp word ptr [r8 + rax*2], bp
008DBA42  75 F6                           jne 0x1408dba3a
008DBA44  48 83 C0 05                     add rax, 5
008DBA48  48 03 C1                        add rax, rcx
008DBA4B  49 3B C2                        cmp rax, r10
008DBA4E  77 9C                           ja 0x1408db9ec
008DBA50  F7 43 40 F0 FF FF FF            test dword ptr [rbx + 0x40], 0xfffffff0
008DBA57  75 93                           jne 0x1408db9ec
008DBA59  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
008DBA5C  3D FF 03 00 00                  cmp eax, 0x3ff
008DBA61  77 89                           ja 0x1408db9ec
008DBA63  85 C0                           test eax, eax
008DBA65  0F 84 6D 01 00 00               je 0x1408dbbd8
008DBA6B  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008DBA6F  48 85 C9                        test rcx, rcx
008DBA72  0F 84 6F 01 00 00               je 0x1408dbbe7
008DBA78  48 8B D0                        mov rdx, rax
008DBA7B  E8 EC 0A 00 00                  call 0x1408dc56c
008DBA80  85 C0                           test eax, eax
008DBA82  0F 88 64 FF FF FF               js 0x1408db9ec
008DBA88  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
008DBA8C  0F B7 0A                        movzx ecx, word ptr [rdx]
008DBA8F  66 85 C9                        test cx, cx
008DBA92  74 3F                           je 0x1408dbad3
008DBA94  4C 8B C2                        mov r8, rdx
008DBA97  66 85 C9                        test cx, cx
008DBA9A  74 21                           je 0x1408dbabd
008DBA9C  8D 41 DF                        lea eax, [rcx - 0x21]
008DBA9F  66 83 F8 5E                     cmp ax, 0x5e
008DBAA3  0F 87 43 FF FF FF               ja 0x1408db9ec
008DBAA9  66 83 F9 2C                     cmp cx, 0x2c
008DBAAD  0F 84 39 FF FF FF               je 0x1408db9ec
008DBAB3  49 83 C0 02                     add r8, 2
008DBAB7  41 0F B7 08                     movzx ecx, word ptr [r8]
008DBABB  EB DA                           jmp 0x1408dba97
008DBABD  48 8B C7                        mov rax, rdi
008DBAC0  48 FF C0                        inc rax
008DBAC3  66 39 2C 42                     cmp word ptr [rdx + rax*2], bp
008DBAC7  75 F7                           jne 0x1408dbac0
008DBAC9  48 8D 14 42                     lea rdx, [rdx + rax*2]
008DBACD  48 83 C2 02                     add rdx, 2
008DBAD1  EB B9                           jmp 0x1408dba8c
008DBAD3  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008DBAD6  3D FF 03 00 00                  cmp eax, 0x3ff
008DBADB  0F 87 0B FF FF FF               ja 0x1408db9ec
008DBAE1  85 C0                           test eax, eax
008DBAE3  0F 84 0B 01 00 00               je 0x1408dbbf4
008DBAE9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
008DBAED  48 85 C9                        test rcx, rcx
008DBAF0  0F 84 0D 01 00 00               je 0x1408dbc03
008DBAF6  48 8B D0                        mov rdx, rax
008DBAF9  E8 6E 0A 00 00                  call 0x1408dc56c
008DBAFE  85 C0                           test eax, eax
008DBB00  0F 88 E6 FE FF FF               js 0x1408db9ec
008DBB06  48 8B 53 30                     mov rdx, qword ptr [rbx + 0x30]
008DBB0A  0F B7 0A                        movzx ecx, word ptr [rdx]
008DBB0D  66 85 C9                        test cx, cx
008DBB10  74 3F                           je 0x1408dbb51
008DBB12  4C 8B C2                        mov r8, rdx
008DBB15  66 85 C9                        test cx, cx
008DBB18  74 21                           je 0x1408dbb3b
008DBB1A  8D 41 DF                        lea eax, [rcx - 0x21]
008DBB1D  66 83 F8 5E                     cmp ax, 0x5e
008DBB21  0F 87 C5 FE FF FF               ja 0x1408db9ec
008DBB27  66 83 F9 2C                     cmp cx, 0x2c
008DBB2B  0F 84 BB FE FF FF               je 0x1408db9ec
008DBB31  49 83 C0 02                     add r8, 2
008DBB35  41 0F B7 08                     movzx ecx, word ptr [r8]
008DBB39  EB DA                           jmp 0x1408dbb15
008DBB3B  48 8B C7                        mov rax, rdi
008DBB3E  48 FF C0                        inc rax
008DBB41  66 39 2C 42                     cmp word ptr [rdx + rax*2], bp
008DBB45  75 F7                           jne 0x1408dbb3e
008DBB47  48 8D 14 42                     lea rdx, [rdx + rax*2]
008DBB4B  48 83 C2 02                     add rdx, 2
008DBB4F  EB B9                           jmp 0x1408dbb0a
008DBB51  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
008DBB55  BA FE 7F 00 00                  mov edx, 0x7ffe
008DBB5A  48 85 C9                        test rcx, rcx
008DBB5D  75 59                           jne 0x1408dbbb8
008DBB5F  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
008DBB63  48 85 C0                        test rax, rax
008DBB66  0F 85 A4 00 00 00               jne 0x1408dbc10
008DBB6C  48 8B 53 60                     mov rdx, qword ptr [rbx + 0x60]
008DBB70  48 85 D2                        test rdx, rdx
008DBB73  74 59                           je 0x1408dbbce
008DBB75  8B 4B 58                        mov ecx, dword ptr [rbx + 0x58]
008DBB78  85 C9                           test ecx, ecx
008DBB7A  0F 84 A7 00 00 00               je 0x1408dbc27
008DBB80  48 85 D2                        test rdx, rdx
008DBB83  0F 85 AC 00 00 00               jne 0x1408dbc35
008DBB89  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
008DBB8C  A8 08                           test al, 8
008DBB8E  0F 85 B3 00 00 00               jne 0x1408dbc47
008DBB94  48 8B 4B 70                     mov rcx, qword ptr [rbx + 0x70]
008DBB98  48 85 C9                        test rcx, rcx
008DBB9B  0F 84 BF 00 00 00               je 0x1408dbc60
008DBBA1  8B 53 68                        mov edx, dword ptr [rbx + 0x68]
008DBBA4  85 D2                           test edx, edx
008DBBA6  0F 84 C2 00 00 00               je 0x1408dbc6e
008DBBAC  E8 43 BA 01 00                  call 0x1408f75f4
008DBBB1  8B F0                           mov esi, eax
008DBBB3  E9 34 FE FF FF                  jmp 0x1408db9ec
008DBBB8  48 8B C7                        mov rax, rdi
008DBBBB  48 FF C0                        inc rax
008DBBBE  66 39 2C 41                     cmp word ptr [rcx + rax*2], bp
008DBBC2  75 F7                           jne 0x1408dbbbb
008DBBC4  48 3B C2                        cmp rax, rdx
008DBBC7  76 96                           jbe 0x1408dbb5f
008DBBC9  E9 1E FE FF FF                  jmp 0x1408db9ec
008DBBCE  39 6B 58                        cmp dword ptr [rbx + 0x58], ebp
008DBBD1  74 A2                           je 0x1408dbb75
008DBBD3  E9 14 FE FF FF                  jmp 0x1408db9ec
008DBBD8  48 39 6B 20                     cmp qword ptr [rbx + 0x20], rbp
008DBBDC  0F 85 0A FE FF FF               jne 0x1408db9ec
008DBBE2  E9 84 FE FF FF                  jmp 0x1408dba6b
008DBBE7  85 C0                           test eax, eax
008DBBE9  0F 85 FD FD FF FF               jne 0x1408db9ec
008DBBEF  E9 DF FE FF FF                  jmp 0x1408dbad3
008DBBF4  48 39 6B 30                     cmp qword ptr [rbx + 0x30], rbp
008DBBF8  0F 85 EE FD FF FF               jne 0x1408db9ec
008DBBFE  E9 E6 FE FF FF                  jmp 0x1408dbae9
008DBC03  85 C0                           test eax, eax
008DBC05  0F 85 E1 FD FF FF               jne 0x1408db9ec
008DBC0B  E9 41 FF FF FF                  jmp 0x1408dbb51
008DBC10  48 FF C7                        inc rdi
008DBC13  66 39 2C 78                     cmp word ptr [rax + rdi*2], bp
008DBC17  75 F7                           jne 0x1408dbc10
008DBC19  48 3B FA                        cmp rdi, rdx
008DBC1C  0F 87 CA FD FF FF               ja 0x1408db9ec
008DBC22  E9 45 FF FF FF                  jmp 0x1408dbb6c
008DBC27  48 85 D2                        test rdx, rdx
008DBC2A  0F 85 BC FD FF FF               jne 0x1408db9ec
008DBC30  E9 4B FF FF FF                  jmp 0x1408dbb80
008DBC35  E8 26 31 FE FF                  call 0x1408bed60
008DBC3A  84 C0                           test al, al
008DBC3C  0F 84 AA FD FF FF               je 0x1408db9ec
008DBC42  E9 42 FF FF FF                  jmp 0x1408dbb89
008DBC47  48 39 6B 20                     cmp qword ptr [rbx + 0x20], rbp
008DBC4B  0F 85 43 FF FF FF               jne 0x1408dbb94
008DBC51  48 39 6B 30                     cmp qword ptr [rbx + 0x30], rbp
008DBC55  0F 84 91 FD FF FF               je 0x1408db9ec
008DBC5B  E9 34 FF FF FF                  jmp 0x1408dbb94
008DBC60  39 6B 68                        cmp dword ptr [rbx + 0x68], ebp
008DBC63  0F 85 83 FD FF FF               jne 0x1408db9ec
008DBC69  E9 33 FF FF FF                  jmp 0x1408dbba1
008DBC6E  48 85 C9                        test rcx, rcx
008DBC71  0F 85 75 FD FF FF               jne 0x1408db9ec
008DBC77  E9 30 FF FF FF                  jmp 0x1408dbbac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwValidateCreateData(__int64 a1)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbp = 0;
    if (a1 == 0) goto loc_008DB9EC;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_008DB9EC;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) == 0) goto loc_008DB9EC;
    v_rdi = (v_rdi) | (-1);
loc_008DB990:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + result * 2)) != 0) goto loc_008DB990;
    if (result > 199) goto loc_008DB9EC;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_008DB9EC;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1))) == 0) goto loc_008DB9EC;
loc_008DB9B8:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1))) == 0) goto loc_008DB9DB;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1)) - 33)) > 94) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1)))) == 44) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1)))) == 92) goto loc_008DB9EC;
    a2 = (*(unsigned __int64 *)(a1)) + (2);
    goto loc_008DB9B8;
loc_008DB9DB:
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_008DB9EC;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16))) != 0) goto loc_008DBA04;
loc_008DB9EC:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_008DBA04:
loc_008DBA07:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16))) == 0) goto loc_008DBA2B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16)) - 33)) > 94) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16)))) == 44) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16)))) == 92) goto loc_008DB9EC;
    a4 = (*(unsigned __int64 *)(a1 + 16)) + (2);
    goto loc_008DBA07;
loc_008DBA2B:
loc_008DBA2E:
    a1 = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16) + a1 * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBA2E;
loc_008DBA3A:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + result * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBA3A;
    result = (result) + (5);
    result = (result) + (a1);
    if (result > 199) goto loc_008DB9EC;
    if (((*(unsigned int *)(v_stack_p8 + 64)) & (0xFFFFFFF0ULL)) != 0) goto loc_008DB9EC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 24)))) > 0x3FFULL) goto loc_008DB9EC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 24))) == 0) goto loc_008DBBD8;
loc_008DBA6B:
    if (*(unsigned __int64 *)(v_stack_p8 + 32) == 0) goto loc_008DBBE7;
    result = PnpValidateMultiSz(*(unsigned __int64 *)(v_stack_p8 + 32), (unsigned int)(*(unsigned int *)(v_stack_p8 + 24)), *(unsigned __int64 *)(a1), a4);
    if (sign_flag) goto loc_008DB9EC;
loc_008DBA8C:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32))) == 0) goto loc_008DBAD3;
loc_008DBA97:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32))) == 0) goto loc_008DBABD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32)) - 33)) > 94) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32)))) == 44) goto loc_008DB9EC;
    a3 = (*(unsigned __int64 *)(v_stack_p8 + 32)) + (2);
    goto loc_008DBA97;
loc_008DBABD:
loc_008DBAC0:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 32) + result * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBAC0;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 32) + result * 2) + (2);
    goto loc_008DBA8C;
loc_008DBAD3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 40)))) > 0x3FFULL) goto loc_008DB9EC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 40))) == 0) goto loc_008DBBF4;
loc_008DBAE9:
    if (*(unsigned __int64 *)(v_stack_p8 + 48) == 0) goto loc_008DBC03;
    result = PnpValidateMultiSz(*(unsigned __int64 *)(v_stack_p8 + 48), (unsigned int)(*(unsigned int *)(v_stack_p8 + 40)), a3, a4);
    if (sign_flag) goto loc_008DB9EC;
loc_008DBB0A:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 48))) == 0) goto loc_008DBB51;
loc_008DBB15:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 48))) == 0) goto loc_008DBB3B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 48)) - 33)) > 94) goto loc_008DB9EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 48)))) == 44) goto loc_008DB9EC;
    a3 = (*(unsigned __int64 *)(v_stack_p8 + 48)) + (2);
    goto loc_008DBB15;
loc_008DBB3B:
loc_008DBB3E:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 48) + result * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBB3E;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 48) + result * 2) + (2);
    goto loc_008DBB0A;
loc_008DBB51:
    if (*(unsigned __int64 *)(v_stack_p8 + 72) != 0) goto loc_008DBBB8;
loc_008DBB5F:
    if (*(unsigned __int64 *)(v_stack_p8 + 80) != 0) goto loc_008DBC10;
loc_008DBB6C:
    if (*(unsigned __int64 *)(v_stack_p8 + 96) == 0) goto loc_008DBBCE;
loc_008DBB75:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 88))) == 0) goto loc_008DBC27;
loc_008DBB80:
    if (*(unsigned __int64 *)(v_stack_p8 + 96) != 0) goto loc_008DBC35;
loc_008DBB89:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 64)))) & (8)) != 0) goto loc_008DBC47;
loc_008DBB94:
    if (*(unsigned __int64 *)(v_stack_p8 + 112) == 0) goto loc_008DBC60;
loc_008DBBA1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 104))) == 0) goto loc_008DBC6E;
loc_008DBBAC:
    result = PiSwValidatePropertyArray(*(unsigned __int64 *)(v_stack_p8 + 112), (unsigned int)(*(unsigned int *)(v_stack_p8 + 104)), a3, a4);
    goto loc_008DB9EC;
loc_008DBBB8:
loc_008DBBBB:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 112) + result * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBBBB;
    if (result <= ((unsigned int)(*(unsigned int *)(v_stack_p8 + 104)))) goto loc_008DBB5F;
    goto loc_008DB9EC;
loc_008DBBCE:
    if ((*(unsigned int *)(v_stack_p8 + 88)) == ((unsigned int)(v_stack_p10))) goto loc_008DBB75;
    goto loc_008DB9EC;
loc_008DBBD8:
    if ((*(unsigned __int64 *)(v_stack_p8 + 32)) != v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBA6B;
loc_008DBBE7:
    if ((unsigned int)(result) != 0) goto loc_008DB9EC;
    goto loc_008DBAD3;
loc_008DBBF4:
    if ((*(unsigned __int64 *)(v_stack_p8 + 48)) != v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBAE9;
loc_008DBC03:
    if ((unsigned int)(result) != 0) goto loc_008DB9EC;
    goto loc_008DBB51;
loc_008DBC10:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(result + v_rdi * 2)) != ((unsigned __int16)(v_stack_p10))) goto loc_008DBC10;
    if (v_rdi > ((unsigned int)(*(unsigned int *)(v_stack_p8 + 104)))) goto loc_008DB9EC;
    goto loc_008DBB6C;
loc_008DBC27:
    if ((unsigned int)(*(unsigned int *)(v_stack_p8 + 104)) != 0) goto loc_008DB9EC;
    goto loc_008DBB80;
loc_008DBC35:
    result = SeValidSecurityDescriptor(*(unsigned __int64 *)(v_stack_p8 + 112), (unsigned int)(*(unsigned int *)(v_stack_p8 + 104)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008DB9EC;
    goto loc_008DBB89;
loc_008DBC47:
    if ((*(unsigned __int64 *)(v_stack_p8 + 32)) != v_stack_p10) goto loc_008DBB94;
    if ((*(unsigned __int64 *)(v_stack_p8 + 48)) == v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBB94;
loc_008DBC60:
    if ((*(unsigned int *)(v_stack_p8 + 104)) != ((unsigned int)(v_stack_p10))) goto loc_008DB9EC;
    goto loc_008DBBA1;
loc_008DBC6E:
    if (*(unsigned __int64 *)(v_stack_p8 + 112) != 0) goto loc_008DB9EC;
    goto loc_008DBBAC;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwValidateCreateData(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbp = 0;
    if (Arg1 == NULL) goto loc_008DB9EC;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_008DB9EC;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) == 0) goto loc_008DB9EC;
    local_rdi = (local_rdi) | (-1);
loc_008DB990:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + result * 2)) != 0) goto loc_008DB990;
    if (result > 199) goto loc_008DB9EC;
    if (*(uint64_t *)(arg1) == 0) goto loc_008DB9EC;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1))) == 0) goto loc_008DB9EC;
loc_008DB9B8:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1))) == 0) goto loc_008DB9DB;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1)) - 33)) > 94) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1)))) == 44) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1)))) == 92) goto loc_008DB9EC;
    a2 = (*(uint64_t *)(arg1)) + (2);
    goto loc_008DB9B8;
loc_008DB9DB:
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_008DB9EC;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10))) != 0) goto loc_008DBA04;
loc_008DB9EC:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_008DBA04:
loc_008DBA07:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10))) == 0) goto loc_008DBA2B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10)) - 33)) > 94) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10)))) == 44) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10)))) == 92) goto loc_008DB9EC;
    a4 = (*(uint64_t *)(arg1 + 0x10)) + (2);
    goto loc_008DBA07;
loc_008DBA2B:
loc_008DBA2E:
    Arg1 = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x10) + arg1 * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBA2E;
loc_008DBA3A:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1) + result * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBA3A;
    result = (result) + (5);
    result = (result) + (Arg1);
    if (result > 199) goto loc_008DB9EC;
    if (((*(uint32_t *)(v_stack_p8 + 0x40)) & (0xFFFFFFF0ULL)) != 0) goto loc_008DB9EC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)))) > 0x3FFULL) goto loc_008DB9EC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18))) == 0) goto loc_008DBBD8;
loc_008DBA6B:
    if (*(uint64_t *)(v_stack_p8 + 0x20) == 0) goto loc_008DBBE7;
    result = PnpValidateMultiSz(*(uint64_t *)(v_stack_p8 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)), *(uint64_t *)(arg1), a4);
    if (sign_flag) goto loc_008DB9EC;
loc_008DBA8C:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20))) == 0) goto loc_008DBAD3;
loc_008DBA97:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20))) == 0) goto loc_008DBABD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20)) - 33)) > 94) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20)))) == 44) goto loc_008DB9EC;
    a3 = (*(uint64_t *)(v_stack_p8 + 0x20)) + (2);
    goto loc_008DBA97;
loc_008DBABD:
loc_008DBAC0:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x20) + result * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBAC0;
    a2 = (*(uint64_t *)(v_stack_p8 + 0x20) + result * 2) + (2);
    goto loc_008DBA8C;
loc_008DBAD3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28)))) > 0x3FFULL) goto loc_008DB9EC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28))) == 0) goto loc_008DBBF4;
loc_008DBAE9:
    if (*(uint64_t *)(v_stack_p8 + 0x30) == 0) goto loc_008DBC03;
    result = PnpValidateMultiSz(*(uint64_t *)(v_stack_p8 + 0x30), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28)), a3, a4);
    if (sign_flag) goto loc_008DB9EC;
loc_008DBB0A:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x30))) == 0) goto loc_008DBB51;
loc_008DBB15:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x30))) == 0) goto loc_008DBB3B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x30)) - 33)) > 94) goto loc_008DB9EC;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x30)))) == 44) goto loc_008DB9EC;
    a3 = (*(uint64_t *)(v_stack_p8 + 0x30)) + (2);
    goto loc_008DBB15;
loc_008DBB3B:
loc_008DBB3E:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x30) + result * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBB3E;
    a2 = (*(uint64_t *)(v_stack_p8 + 0x30) + result * 2) + (2);
    goto loc_008DBB0A;
loc_008DBB51:
    if (*(uint64_t *)(v_stack_p8 + 0x48) != 0) goto loc_008DBBB8;
loc_008DBB5F:
    if (*(uint64_t *)(v_stack_p8 + 0x50) != 0) goto loc_008DBC10;
loc_008DBB6C:
    if (*(uint64_t *)(v_stack_p8 + 0x60) == 0) goto loc_008DBBCE;
loc_008DBB75:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58))) == 0) goto loc_008DBC27;
loc_008DBB80:
    if (*(uint64_t *)(v_stack_p8 + 0x60) != 0) goto loc_008DBC35;
loc_008DBB89:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40)))) & (8)) != 0) goto loc_008DBC47;
loc_008DBB94:
    if (*(uint64_t *)(v_stack_p8 + 0x70) == 0) goto loc_008DBC60;
loc_008DBBA1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68))) == 0) goto loc_008DBC6E;
loc_008DBBAC:
    result = PiSwValidatePropertyArray(*(uint64_t *)(v_stack_p8 + 0x70), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68)), a3, a4);
    goto loc_008DB9EC;
loc_008DBBB8:
loc_008DBBBB:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + result * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBBBB;
    if (result <= ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68)))) goto loc_008DBB5F;
    goto loc_008DB9EC;
loc_008DBBCE:
    if ((*(uint32_t *)(v_stack_p8 + 0x58)) == ((uint32_t)(v_stack_p10))) goto loc_008DBB75;
    goto loc_008DB9EC;
loc_008DBBD8:
    if ((*(uint64_t *)(v_stack_p8 + 0x20)) != v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBA6B;
loc_008DBBE7:
    if ((uint32_t)(result) != 0) goto loc_008DB9EC;
    goto loc_008DBAD3;
loc_008DBBF4:
    if ((*(uint64_t *)(v_stack_p8 + 0x30)) != v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBAE9;
loc_008DBC03:
    if ((uint32_t)(result) != 0) goto loc_008DB9EC;
    goto loc_008DBB51;
loc_008DBC10:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(result + local_rdi * 2)) != ((uint16_t)(v_stack_p10))) goto loc_008DBC10;
    if (local_rdi > ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68)))) goto loc_008DB9EC;
    goto loc_008DBB6C;
loc_008DBC27:
    if ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68)) != 0) goto loc_008DB9EC;
    goto loc_008DBB80;
loc_008DBC35:
    result = SeValidSecurityDescriptor(*(uint64_t *)(v_stack_p8 + 0x70), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x68)), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_008DB9EC;
    goto loc_008DBB89;
loc_008DBC47:
    if ((*(uint64_t *)(v_stack_p8 + 0x20)) != v_stack_p10) goto loc_008DBB94;
    if ((*(uint64_t *)(v_stack_p8 + 0x30)) == v_stack_p10) goto loc_008DB9EC;
    goto loc_008DBB94;
loc_008DBC60:
    if ((*(uint32_t *)(v_stack_p8 + 0x68)) != ((uint32_t)(v_stack_p10))) goto loc_008DB9EC;
    goto loc_008DBBA1;
loc_008DBC6E:
    if (*(uint64_t *)(v_stack_p8 + 0x70) != 0) goto loc_008DB9EC;
    goto loc_008DBBAC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DB958&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
