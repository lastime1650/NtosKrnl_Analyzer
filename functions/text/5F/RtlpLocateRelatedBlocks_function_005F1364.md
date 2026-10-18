# RtlpLocateRelatedBlocks

- RVA: `0x005F1364`–`0x005F1632` (길이 `718` bytes)
- VA: `0x00000001405F1364`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F874`
- 디코드: `196`개 명령, `718/718` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpHeapHandleError](RtlpHpHeapHandleError_function_005F12F4.md) at `0x005F1340`

### Static image references
- `0x005F146F` → RVA `0x00E0C608` (`.data`; write)
- `0x005F1476` → RVA `0x00E0C610` (`.data`; write)
- `0x005F14D9` → RVA `0x00E0C5D8` (`.data`; write)
- `0x005F153B` → RVA `0x00E0C618` (`.data`; write)
- `0x005F1578` → RVA `0x00E0C620` (`.data`; write)
- `0x005F15AB` → RVA `0x00E0C618` (`.data`; read)
- `0x005F15D1` → RVA `0x00E0C620` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F1364  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005F1369  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005F136E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005F1373  57                              push rdi
005F1374  48 83 EC 50                     sub rsp, 0x50
005F1378  4C 8B D2                        mov r10, rdx
005F137B  4C 8B C1                        mov r8, rcx
005F137E  48 8D 91 20 01 00 00            lea rdx, [rcx + 0x120]
005F1385  48 8B 02                        mov rax, qword ptr [rdx]
005F1388  48 3B C2                        cmp rax, rdx
005F138B  0F 84 55 02 00 00               je 0x1405f15e6
005F1391  48 8D 48 E8                     lea rcx, [rax - 0x18]
005F1395  4C 39 51 30                     cmp qword ptr [rcx + 0x30], r10
005F1399  77 06                           ja 0x1405f13a1
005F139B  4C 39 51 48                     cmp qword ptr [rcx + 0x48], r10
005F139F  77 05                           ja 0x1405f13a6
005F13A1  48 8B 00                        mov rax, qword ptr [rax]
005F13A4  EB E2                           jmp 0x1405f1388
005F13A6  33 ED                           xor ebp, ebp
005F13A8  48 8D 79 60                     lea rdi, [rcx + 0x60]
005F13AC  48 8B 17                        mov rdx, qword ptr [rdi]
005F13AF  44 8B CD                        mov r9d, ebp
005F13B2  44 8B DD                        mov r11d, ebp
005F13B5  EB 2E                           jmp 0x1405f13e5
005F13B7  48 8B 72 10                     mov rsi, qword ptr [rdx + 0x10]
005F13BB  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
005F13BF  48 03 C6                        add rax, rsi
005F13C2  49 3B C2                        cmp rax, r10
005F13C5  73 07                           jae 0x1405f13ce
005F13C7  49 3B C1                        cmp rax, r9
005F13CA  4C 0F 47 C8                     cmova r9, rax
005F13CE  49 3B F2                        cmp rsi, r10
005F13D1  76 0F                           jbe 0x1405f13e2
005F13D3  4D 85 DB                        test r11, r11
005F13D6  74 06                           je 0x1405f13de
005F13D8  49 3B 73 20                     cmp rsi, qword ptr [r11 + 0x20]
005F13DC  73 04                           jae 0x1405f13e2
005F13DE  4C 8D 5A F0                     lea r11, [rdx - 0x10]
005F13E2  48 8B 12                        mov rdx, qword ptr [rdx]
005F13E5  48 3B D7                        cmp rdx, rdi
005F13E8  75 CD                           jne 0x1405f13b7
005F13EA  4D 85 C9                        test r9, r9
005F13ED  48 8B DD                        mov rbx, rbp
005F13F0  49 0F 45 C9                     cmovne rcx, r9
005F13F4  4C 8B CD                        mov r9, rbp
005F13F7  49 3B CA                        cmp rcx, r10
005F13FA  73 44                           jae 0x1405f1440
005F13FC  41 8B 50 7C                     mov edx, dword ptr [r8 + 0x7c]
005F1400  4C 8B C9                        mov r9, rcx
005F1403  85 D2                           test edx, edx
005F1405  74 21                           je 0x1405f1428
005F1407  8B 41 08                        mov eax, dword ptr [rcx + 8]
005F140A  41 8B 50 7C                     mov edx, dword ptr [r8 + 0x7c]
005F140E  89 44 24 08                     mov dword ptr [rsp + 8], eax
005F1412  85 D0                           test eax, edx
005F1414  74 0B                           je 0x1405f1421
005F1416  41 33 80 88 00 00 00            xor eax, dword ptr [r8 + 0x88]
005F141D  89 44 24 08                     mov dword ptr [rsp + 8], eax
005F1421  0F B7 44 24 08                  movzx eax, word ptr [rsp + 8]
005F1426  EB 04                           jmp 0x1405f142c
005F1428  0F B7 41 08                     movzx eax, word ptr [rcx + 8]
005F142C  66 85 C0                        test ax, ax
005F142F  74 0F                           je 0x1405f1440
005F1431  0F B7 C0                        movzx eax, ax
005F1434  48 C1 E0 04                     shl rax, 4
005F1438  48 03 C8                        add rcx, rax
005F143B  49 3B CA                        cmp rcx, r10
005F143E  72 C0                           jb 0x1405f1400
005F1440  49 8D 4B F0                     lea rcx, [r11 - 0x10]
005F1444  49 3B CA                        cmp rcx, r10
005F1447  76 26                           jbe 0x1405f146f
005F1449  41 0F B7 90 8C 00 00 00         movzx edx, word ptr [r8 + 0x8c]
005F1451  0F B7 C2                        movzx eax, dx
005F1454  48 8B D9                        mov rbx, rcx
005F1457  66 33 41 0C                     xor ax, word ptr [rcx + 0xc]
005F145B  74 12                           je 0x1405f146f
005F145D  0F B7 C0                        movzx eax, ax
005F1460  48 F7 D8                        neg rax
005F1463  48 C1 E0 04                     shl rax, 4
005F1467  48 03 C8                        add rcx, rax
005F146A  49 3B CA                        cmp rcx, r10
005F146D  77 E2                           ja 0x1405f1451
005F146F  4C 89 0D 92 B1 81 00            mov qword ptr [rip + 0x81b192], r9
005F1476  48 89 1D 93 B1 81 00            mov qword ptr [rip + 0x81b193], rbx
005F147D  4D 85 C9                        test r9, r9
005F1480  74 66                           je 0x1405f14e8
005F1482  48 85 DB                        test rbx, rbx
005F1485  74 61                           je 0x1405f14e8
005F1487  41 39 68 7C                     cmp dword ptr [r8 + 0x7c], ebp
005F148B  74 21                           je 0x1405f14ae
005F148D  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
005F1491  89 4C 24 18                     mov dword ptr [rsp + 0x18], ecx
005F1495  41 85 48 7C                     test dword ptr [r8 + 0x7c], ecx
005F1499  74 0B                           je 0x1405f14a6
005F149B  41 33 88 88 00 00 00            xor ecx, dword ptr [r8 + 0x88]
005F14A2  89 4C 24 18                     mov dword ptr [rsp + 0x18], ecx
005F14A6  44 0F B7 54 24 18               movzx r10d, word ptr [rsp + 0x18]
005F14AC  EB 05                           jmp 0x1405f14b3
005F14AE  45 0F B7 51 08                  movzx r10d, word ptr [r9 + 8]
005F14B3  41 0F B7 80 8C 00 00 00         movzx eax, word ptr [r8 + 0x8c]
005F14BB  0F B7 4B 0C                     movzx ecx, word ptr [rbx + 0xc]
005F14BF  48 33 C8                        xor rcx, rax
005F14C2  41 0F B7 C2                     movzx eax, r10w
005F14C6  48 6B D1 F0                     imul rdx, rcx, -0x10
005F14CA  48 C1 E0 04                     shl rax, 4
005F14CE  48 03 D3                        add rdx, rbx
005F14D1  49 03 C1                        add rax, r9
005F14D4  48 3B C2                        cmp rax, rdx
005F14D7  74 0F                           je 0x1405f14e8
005F14D9  C7 05 F5 B0 81 00 04 00 00 00   mov dword ptr [rip + 0x81b0f5], 4
005F14E3  E9 34 01 00 00                  jmp 0x1405f161c
005F14E8  4D 8D 58 7C                     lea r11, [r8 + 0x7c]
005F14EC  41 8B 0B                        mov ecx, dword ptr [r11]
005F14EF  49 8B D3                        mov rdx, r11
005F14F2  85 C9                           test ecx, ecx
005F14F4  74 25                           je 0x1405f151b
005F14F6  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
005F14FA  41 8B 0B                        mov ecx, dword ptr [r11]
005F14FD  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
005F1501  85 C8                           test eax, ecx
005F1503  74 0F                           je 0x1405f1514
005F1505  41 33 80 88 00 00 00            xor eax, dword ptr [r8 + 0x88]
005F150C  49 8D 50 7C                     lea rdx, [r8 + 0x7c]
005F1510  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
005F1514  0F B7 44 24 28                  movzx eax, word ptr [rsp + 0x28]
005F1519  EB 05                           jmp 0x1405f1520
005F151B  41 0F B7 41 08                  movzx eax, word ptr [r9 + 8]
005F1520  44 0F B7 D0                     movzx r10d, ax
005F1524  4D 03 D2                        add r10, r10
005F1527  48 85 DB                        test rbx, rbx
005F152A  74 19                           je 0x1405f1545
005F152C  0F B7 4B 0C                     movzx ecx, word ptr [rbx + 0xc]
005F1530  41 0F B7 80 8C 00 00 00         movzx eax, word ptr [r8 + 0x8c]
005F1538  48 33 C8                        xor rcx, rax
005F153B  48 89 0D D6 B0 81 00            mov qword ptr [rip + 0x81b0d6], rcx
005F1542  41 8B 0B                        mov ecx, dword ptr [r11]
005F1545  4D 85 C9                        test r9, r9
005F1548  74 35                           je 0x1405f157f
005F154A  85 C9                           test ecx, ecx
005F154C  74 22                           je 0x1405f1570
005F154E  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
005F1552  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005F1556  85 02                           test dword ptr [rdx], eax
005F1558  74 0B                           je 0x1405f1565
005F155A  41 33 80 88 00 00 00            xor eax, dword ptr [r8 + 0x88]
005F1561  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005F1565  0F B7 44 24 38                  movzx eax, word ptr [rsp + 0x38]
005F156A  49 8D 50 7C                     lea rdx, [r8 + 0x7c]
005F156E  EB 05                           jmp 0x1405f1575
005F1570  41 0F B7 41 08                  movzx eax, word ptr [r9 + 8]
005F1575  0F B7 C0                        movzx eax, ax
005F1578  48 89 05 A1 B0 81 00            mov qword ptr [rip + 0x81b0a1], rax
005F157F  39 2A                           cmp dword ptr [rdx], ebp
005F1581  74 1F                           je 0x1405f15a2
005F1583  43 8B 44 D1 08                  mov eax, dword ptr [r9 + r10*8 + 8]
005F1588  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005F158C  85 02                           test dword ptr [rdx], eax
005F158E  74 0B                           je 0x1405f159b
005F1590  41 33 80 88 00 00 00            xor eax, dword ptr [r8 + 0x88]
005F1597  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005F159B  0F B7 44 24 48                  movzx eax, word ptr [rsp + 0x48]
005F15A0  EB 06                           jmp 0x1405f15a8
005F15A2  43 0F B7 44 D1 08               movzx eax, word ptr [r9 + r10*8 + 8]
005F15A8  0F B7 C0                        movzx eax, ax
005F15AB  48 39 05 66 B0 81 00            cmp qword ptr [rip + 0x81b066], rax
005F15B2  74 0C                           je 0x1405f15c0
005F15B4  C7 05 1A B0 81 00 06 00 00 00   mov dword ptr [rip + 0x81b01a], 6
005F15BE  EB 5C                           jmp 0x1405f161c
005F15C0  43 0F B7 4C D1 0C               movzx ecx, word ptr [r9 + r10*8 + 0xc]
005F15C6  41 0F B7 80 8C 00 00 00         movzx eax, word ptr [r8 + 0x8c]
005F15CE  48 33 C8                        xor rcx, rax
005F15D1  48 39 0D 48 B0 81 00            cmp qword ptr [rip + 0x81b048], rcx
005F15D8  74 42                           je 0x1405f161c
005F15DA  C7 05 F4 AF 81 00 07 00 00 00   mov dword ptr [rip + 0x81aff4], 7
005F15E4  EB 36                           jmp 0x1405f161c
005F15E6  49 81 C0 10 01 00 00            add r8, 0x110
005F15ED  49 8B 10                        mov rdx, qword ptr [r8]
005F15F0  EB 25                           jmp 0x1405f1617
005F15F2  48 8B CA                        mov rcx, rdx
005F15F5  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
005F15FC  49 3B CA                        cmp rcx, r10
005F15FF  77 13                           ja 0x1405f1614
005F1601  48 03 4A 28                     add rcx, qword ptr [rdx + 0x28]
005F1605  49 3B CA                        cmp rcx, r10
005F1608  76 0A                           jbe 0x1405f1614
005F160A  C7 05 C4 AF 81 00 05 00 00 00   mov dword ptr [rip + 0x81afc4], 5
005F1614  48 8B 12                        mov rdx, qword ptr [rdx]
005F1617  49 3B D0                        cmp rdx, r8
005F161A  75 D6                           jne 0x1405f15f2
005F161C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005F1621  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
005F1626  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
005F162B  48 83 C4 50                     add rsp, 0x50
005F162F  5F                              pop rdi
005F1630  C3                              ret
005F1631  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpLocateRelatedBlocks(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m20;
    unsigned int v_stack_m30;
    unsigned int v_stack_m40;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (80);
loc_005F1388:
    if ((*(unsigned __int64 *)(a1 + 288)) == (a1 + 288)) goto loc_005F15E6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 48)) > a2) goto loc_005F13A1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 72)) > a2) goto loc_005F13A6;
loc_005F13A1:
    goto loc_005F1388;
loc_005F13A6:
    v_rbp = 0;
    goto loc_005F13E5;
loc_005F13B7:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96) + 24)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96) + 16));
    if (result < a2) {
        a4 = 0;
        if (result > 0) { a4 = result; }
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96) + 16)) <= a2) goto loc_005F13E2;
    if (0 == 0) goto loc_005F13DE;
    v_r11 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96) + 16)) < (*(unsigned __int64 *)(0 + 32))) {
        v_r11 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96) - 16;
    }
loc_005F13E5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) - 24 + 96))) != (*(unsigned __int64 *)(a1 + 288) - 24 + 96)) goto loc_005F13B7;
    a1 = *(unsigned __int64 *)(a1 + 288) - 24;
    if (a4 != 0) { a1 = a4; }
    if (a1 >= a2) goto loc_005F1440;
loc_005F1400:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005F1428;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m50 = (unsigned int)(result);
    }
    goto loc_005F142C;
loc_005F1428:
loc_005F142C:
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 8)) == 0) goto loc_005F1440;
    result = ((unsigned __int16)(*(unsigned __int16 *)(a1 + 8))) << (4);
    a1 = (a1) + (result);
    if (a1 < a2) goto loc_005F1400;
loc_005F1440:
    if ((v_r11 - 16) <= a2) goto loc_005F146F;
loc_005F1451:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 140))) ^ (*(unsigned __int16 *)(v_r11 - 16 + 12)));
    if (condition_is_equal) goto loc_005F146F;
    result = -((unsigned __int16)(result));
    result = (result) << (4);
    a1 = (v_r11 - 16) + (result);
    if (a1 > a2) goto loc_005F1451;
loc_005F146F:
    *(unsigned __int64 *)(v_rip + 8499602) = a1;
    *(unsigned __int64 *)(v_rip + 8499603) = v_r11 - 16;
    if (a1 == 0) goto loc_005F14E8;
    if (v_r11 - 16 == 0) goto loc_005F14E8;
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_005F14AE;
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    if (((*(unsigned int *)(a1 + 124)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) != 0) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m40 = (unsigned int)(a1);
    }
    goto loc_005F14B3;
loc_005F14AE:
loc_005F14B3:
    a1 = (*(unsigned __int16 *)(v_r11 - 16 + 12)) ^ (*(unsigned __int16 *)(a1 + 140));
    a2 = (*(unsigned __int16 *)(a1 + 140)) * (a1);
    result = ((unsigned __int16)(*(unsigned __int16 *)(a1 + 8))) << (4);
    a2 = (a2) + (v_r11 - 16);
    result = (result) + (a1);
    if (result == a2) goto loc_005F14E8;
    *(unsigned int *)(v_rip + 8499445) = 4;
    goto loc_005F161C;
loc_005F14E8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_005F151B;
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + 8));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) ^ (*(unsigned int *)(a1 + 136)));
        a2 = a1 + 124;
        v_stack_m30 = (unsigned int)(result);
    }
    goto loc_005F1520;
loc_005F151B:
loc_005F1520:
    v_r10 = ((unsigned __int16)(*(unsigned __int16 *)(a1 + 8))) + ((unsigned __int16)(*(unsigned __int16 *)(a1 + 8)));
    result = *(unsigned __int16 *)(a1 + 8);
    if (v_r11 - 16 != 0) {
        a1 = *(unsigned __int16 *)(v_r11 - 16 + 12);
        result = *(unsigned __int16 *)(a1 + 140);
        a1 = (a1) ^ (result);
        *(unsigned __int64 *)(v_rip + 8499414) = a1;
        a1 = *(unsigned int *)(a1 + 124);
    }
    if (a1 == 0) goto loc_005F157F;
    if ((unsigned int)(a1) == 0) goto loc_005F1570;
    v_stack_m20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + 8));
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m20 = (unsigned int)(result);
    }
    goto loc_005F1575;
loc_005F1570:
loc_005F1575:
    *(unsigned __int64 *)(v_rip + 8499361) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 8));
loc_005F157F:
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_005F15A2;
    v_stack_m10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_r10 * 8 + 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + v_r10 * 8 + 8));
    if (((*(unsigned int *)(a1 + 124)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_r10 * 8 + 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + v_r10 * 8 + 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_m10 = (unsigned int)(result);
    }
    goto loc_005F15A8;
loc_005F15A2:
loc_005F15A8:
    if ((*(unsigned __int64 *)(v_rip + 8499302)) == ((unsigned __int16)(*(unsigned __int16 *)(a1 + v_r10 * 8 + 8)))) goto loc_005F15C0;
    *(unsigned int *)(v_rip + 8499226) = 6;
    goto loc_005F161C;
loc_005F15C0:
    a1 = (*(unsigned __int16 *)(a1 + v_r10 * 8 + 12)) ^ (*(unsigned __int16 *)(a1 + 140));
    if ((*(unsigned __int64 *)(v_rip + 8499272)) == a1) goto loc_005F161C;
    *(unsigned int *)(v_rip + 8499188) = 7;
    goto loc_005F161C;
loc_005F15E6:
    a3 = (a1) + (272);
    goto loc_005F1617;
loc_005F15F2:
    a1 = (*(unsigned __int64 *)(a3)) & (0xFFFFFFFFFFFF0000ULL);
    if (a1 > v_r10) goto loc_005F1614;
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 40));
    if (a1 >= = v_r10) {
        *(unsigned int *)(v_rip + 8499140) = 5;
    }
loc_005F1617:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3))) != a3) goto loc_005F15F2;
loc_005F161C:
    v_rsp = (v_rsp) + (80);
    return *(unsigned __int16 *)(a1 + 140);
}
```

## 5. (Beta) C Style

```c
int64_t RtlpLocateRelatedBlocks(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbp;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m20;
    uint32_t v_stack_m30;
    uint32_t v_stack_m40;
    uint32_t v_stack_m50;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (80);
loc_005F1388:
    if ((*(uint64_t *)(arg1 + 0x120)) == (Arg1 + 288)) goto loc_005F15E6;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x30)) > Arg2) goto loc_005F13A1;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x48)) > Arg2) goto loc_005F13A6;
loc_005F13A1:
    goto loc_005F1388;
loc_005F13A6:
    local_rbp = 0;
    goto loc_005F13E5;
loc_005F13B7:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60) + 0x18)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60) + 0x10));
    if (result < Arg2) {
        a4 = 0;
        if (result > 0) { a4 = result; }
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60) + 0x10)) <= Arg2) goto loc_005F13E2;
    if (0 == 0) goto loc_005F13DE;
    local_r11 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60) + 0x10)) < (*(uint64_t *)(0 + 0x20))) {
        local_r11 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60) - 16;
    }
loc_005F13E5:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) - 0x18 + 0x60))) != (*(uint64_t *)(arg1 + 0x120) - 24 + 96)) goto loc_005F13B7;
    Arg1 = *(uint64_t *)(arg1 + 0x120) - 24;
    if (a4 != 0) { Arg1 = a4; }
    if (Arg1 >= Arg2) goto loc_005F1440;
loc_005F1400:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005F1428;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m50 = (uint32_t)(result);
    }
    goto loc_005F142C;
loc_005F1428:
loc_005F142C:
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x8)) == 0) goto loc_005F1440;
    result = ((uint16_t)(*(uint16_t *)(arg1 + 0x8))) << (4);
    Arg1 = (Arg1) + (result);
    if (Arg1 < Arg2) goto loc_005F1400;
loc_005F1440:
    if ((local_r11 - 16) <= Arg2) goto loc_005F146F;
loc_005F1451:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x8C))) ^ (*(uint16_t *)(local_r11 - 0x10 + 0xC)));
    if (condition_is_equal) goto loc_005F146F;
    result = -((uint16_t)(result));
    result = (result) << (4);
    Arg1 = (local_r11 - 16) + (result);
    if (Arg1 > Arg2) goto loc_005F1451;
loc_005F146F:
    *(void **)(v_rip + 0x81B192) = Arg1;
    *(uint64_t *)(v_rip + 0x81B193) = local_r11 - 16;
    if (Arg1 == NULL) goto loc_005F14E8;
    if (local_r11 - 16 == 0) goto loc_005F14E8;
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_005F14AE;
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if (((*(uint32_t *)(arg1 + 0x7C)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m40 = (uint32_t)(Arg1);
    }
    goto loc_005F14B3;
loc_005F14AE:
loc_005F14B3:
    Arg1 = (*(uint16_t *)(local_r11 - 0x10 + 0xC)) ^ (*(uint16_t *)(arg1 + 0x8C));
    Arg2 = (*(uint16_t *)(arg1 + 0x8C)) * (Arg1);
    result = ((uint16_t)(*(uint16_t *)(arg1 + 0x8))) << (4);
    Arg2 = (Arg2) + (local_r11 - 16);
    result = (result) + (Arg1);
    if (result == Arg2) goto loc_005F14E8;
    *(uint32_t *)(v_rip + 0x81B0F5) = 4;
    goto loc_005F161C;
loc_005F14E8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_005F151B;
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x8));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        Arg2 = Arg1 + 124;
        v_stack_m30 = (uint32_t)(result);
    }
    goto loc_005F1520;
loc_005F151B:
loc_005F1520:
    local_r10 = ((uint16_t)(*(uint16_t *)(arg1 + 0x8))) + ((uint16_t)(*(uint16_t *)(arg1 + 0x8)));
    result = *(uint16_t *)(arg1 + 0x8);
    if (local_r11 - 16 != 0) {
        Arg1 = *(uint16_t *)(local_r11 - 0x10 + 0xC);
        result = *(uint16_t *)(arg1 + 0x8C);
        Arg1 = (Arg1) ^ (result);
        *(void **)(v_rip + 0x81B0D6) = Arg1;
        Arg1 = *(uint32_t *)(arg1 + 0x7C);
    }
    if (Arg1 == NULL) goto loc_005F157F;
    if ((uint32_t)(Arg1) == 0) goto loc_005F1570;
    v_stack_m20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x8));
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m20 = (uint32_t)(result);
    }
    goto loc_005F1575;
loc_005F1570:
loc_005F1575:
    *(uint64_t *)(v_rip + 0x81B0A1) = (uint16_t)(*(uint16_t *)(arg1 + 0x8));
loc_005F157F:
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_005F15A2;
    v_stack_m10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + local_r10 * 8 + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + local_r10 * 8 + 0x8));
    if (((*(uint32_t *)(arg1 + 0x7C)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + local_r10 * 8 + 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + local_r10 * 8 + 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_m10 = (uint32_t)(result);
    }
    goto loc_005F15A8;
loc_005F15A2:
loc_005F15A8:
    if ((*(uint64_t *)(v_rip + 0x81B066)) == ((uint16_t)(*(uint16_t *)(arg1 + local_r10 * 8 + 0x8)))) goto loc_005F15C0;
    *(uint32_t *)(v_rip + 0x81B01A) = 6;
    goto loc_005F161C;
loc_005F15C0:
    Arg1 = (*(uint16_t *)(arg1 + local_r10 * 8 + 0xC)) ^ (*(uint16_t *)(arg1 + 0x8C));
    if ((*(uint64_t *)(v_rip + 0x81B048)) == Arg1) goto loc_005F161C;
    *(uint32_t *)(v_rip + 0x81AFF4) = 7;
    goto loc_005F161C;
loc_005F15E6:
    a3 = (Arg1) + (272);
    goto loc_005F1617;
loc_005F15F2:
    Arg1 = (*(uint64_t *)(a3)) & (0xFFFFFFFFFFFF0000ULL);
    if (Arg1 > local_r10) goto loc_005F1614;
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(a3) + 0x28));
    if (Arg1 >= = local_r10) {
        *(uint32_t *)(v_rip + 0x81AFC4) = 5;
    }
loc_005F1617:
    if ((*(uint64_t *)(*(uint64_t *)(a3))) != a3) goto loc_005F15F2;
loc_005F161C:
    local_rsp = (local_rsp) + (80);
    return *(uint16_t *)(arg1 + 0x8C);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `64` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x8C` | `16` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F1364&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
