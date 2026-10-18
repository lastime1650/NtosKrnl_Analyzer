# MiViewMayContainPage

- RVA: `0x002E11F0`–`0x002E15F9` (길이 `1,033` bytes)
- VA: `0x00000001402E11F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070CD4`
- 디코드: `261`개 명령, `1,033/1,033` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002E12FE` → [MiStartingOffset](../34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x002E130B` → [MiEndingOffsetWithLock](../40/MiEndingOffsetWithLock_function_00404718.md) (function, `0x00404718`)
- `0x002E14BE` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x002E151E` → [ObpTraceObjectReferenceIfActive](../21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x002E1552` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x002E1586` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_002E087E](Unknown_function_002E087E.md) at `0x002E0A56`
- [sub_002E0B15](Unknown_function_002E0B15.md) at `0x002E0C33`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002E1586` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E11F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002E11F5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
002E11FA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
002E11FF  57                              push rdi
002E1200  41 54                           push r12
002E1202  41 55                           push r13
002E1204  41 56                           push r14
002E1206  41 57                           push r15
002E1208  48 83 EC 20                     sub rsp, 0x20
002E120C  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
002E1214  33 FF                           xor edi, edi
002E1216  49 8B 71 10                     mov rsi, qword ptr [r9 + 0x10]
002E121A  49 8B D9                        mov rbx, r9
002E121D  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
002E1222  48 8B C6                        mov rax, rsi
002E1225  83 E0 03                        and eax, 3
002E1228  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
002E1230  49 89 3F                        mov qword ptr [r15], rdi
002E1233  4C 8B E9                        mov r13, rcx
002E1236  48 83 F8 01                     cmp rax, 1
002E123A  0F 84 3C 01 00 00               je 0x1402e137c
002E1240  48 85 D2                        test rdx, rdx
002E1243  0F 85 F8 01 00 00               jne 0x1402e1441
002E1249  48 85 C0                        test rax, rax
002E124C  75 76                           jne 0x1402e12c4
002E124E  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
002E1252  49 8B 49 20                     mov rcx, qword ptr [r9 + 0x20]
002E1256  48 25 00 00 FF FF               and rax, 0xffffffffffff0000
002E125C  4C 8D 34 85 00 00 00 00         lea r14, [rax*4]
002E1264  48 8B C1                        mov rax, rcx
002E1267  48 C1 E8 3E                     shr rax, 0x3e
002E126B  3C 03                           cmp al, 3
002E126D  75 35                           jne 0x1402e12a4
002E126F  83 E1 3F                        and ecx, 0x3f
002E1272  0F 85 70 03 00 00               jne 0x1402e15e8
002E1278  B9 00 00 04 00                  mov ecx, 0x40000
002E127D  49 8B 71 10                     mov rsi, qword ptr [r9 + 0x10]
002E1281  49 8D 2C 0E                     lea rbp, [r14 + rcx]
002E1285  41 8B 45 38                     mov eax, dword ptr [r13 + 0x38]
002E1289  A8 20                           test al, 0x20
002E128B  0F 85 DA 02 00 00               jne 0x1402e156b
002E1291  4C 3B E5                        cmp r12, rbp
002E1294  73 0E                           jae 0x1402e12a4
002E1296  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
002E129B  49 3B D6                        cmp rdx, r14
002E129E  0F 87 E5 01 00 00               ja 0x1402e1489
002E12A4  33 C0                           xor eax, eax
002E12A6  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
002E12AB  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
002E12B0  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002E12B5  48 83 C4 20                     add rsp, 0x20
002E12B9  41 5F                           pop r15
002E12BB  41 5E                           pop r14
002E12BD  41 5D                           pop r13
002E12BF  41 5C                           pop r12
002E12C1  5F                              pop rdi
002E12C2  C3                              ret
002E12C3  CC                              int3
002E12C4  48 83 E8 01                     sub rax, 1
002E12C8  0F 84 AE 00 00 00               je 0x1402e137c
002E12CE  48 83 E8 01                     sub rax, 1
002E12D2  0F 84 B8 02 00 00               je 0x1402e1590
002E12D8  48 83 F8 01                     cmp rax, 1
002E12DC  75 C6                           jne 0x1402e12a4
002E12DE  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
002E12E2  4C 8D B1 80 00 00 00            lea r14, [rcx + 0x80]
002E12E9  48 8B EF                        mov rbp, rdi
002E12EC  4D 85 F6                        test r14, r14
002E12EF  74 B3                           je 0x1402e12a4
002E12F1  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
002E12F5  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002E12FB  49 8B CE                        mov rcx, r14
002E12FE  E8 DD 6F 06 00                  call 0x1403482e0
002E1303  49 8B CE                        mov rcx, r14
002E1306  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002E130B  E8 08 34 12 00                  call 0x140404718
002E1310  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002E1315  4C 3B E2                        cmp r12, rdx
002E1318  0F 82 A5 02 00 00               jb 0x1402e15c3
002E131E  4C 3B E0                        cmp r12, rax
002E1321  0F 83 9C 02 00 00               jae 0x1402e15c3
002E1327  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
002E132B  49 8B C4                        mov rax, r12
002E132E  48 2B C2                        sub rax, rdx
002E1331  48 C1 E8 0C                     shr rax, 0xc
002E1335  48 8D 14 C1                     lea rdx, [rcx + rax*8]
002E1339  41 8B 46 2C                     mov eax, dword ptr [r14 + 0x2c]
002E133D  48 8D 0C C1                     lea rcx, [rcx + rax*8]
002E1341  48 3B D1                        cmp rdx, rcx
002E1344  0F 83 5A FF FF FF               jae 0x1402e12a4
002E134A  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002E134E  0F BA E0 11                     bt eax, 0x11
002E1352  73 0E                           jae 0x1402e1362
002E1354  41 F7 45 38 00 00 00 08         test dword ptr [r13 + 0x38], 0x8000000
002E135C  0F 85 42 FF FF FF               jne 0x1402e12a4
002E1362  49 2B 95 88 00 00 00            sub rdx, qword ptr [r13 + 0x88]
002E1369  4C 8B F7                        mov r14, rdi
002E136C  48 C1 FA 03                     sar rdx, 3
002E1370  48 C1 E2 0C                     shl rdx, 0xc
002E1374  48 03 F2                        add rsi, rdx
002E1377  E9 09 FF FF FF                  jmp 0x1402e1285
002E137C  48 8B CE                        mov rcx, rsi
002E137F  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
002E1383  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002E138B  48 85 D2                        test rdx, rdx
002E138E  0F 85 38 02 00 00               jne 0x1402e15cc
002E1394  41 8B 45 38                     mov eax, dword ptr [r13 + 0x38]
002E1398  41 83 E0 20                     and r8d, 0x20
002E139C  49 8B 71 E8                     mov rsi, qword ptr [r9 - 0x18]
002E13A0  A8 20                           test al, 0x20
002E13A2  0F 85 83 01 00 00               jne 0x1402e152b
002E13A8  45 85 C0                        test r8d, r8d
002E13AB  0F 85 F7 01 00 00               jne 0x1402e15a8
002E13B1  4D 8B 71 F0                     mov r14, qword ptr [r9 - 0x10]
002E13B5  4C 8B 0E                        mov r9, qword ptr [rsi]
002E13B8  41 8B 41 38                     mov eax, dword ptr [r9 + 0x38]
002E13BC  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
002E13C0  A8 20                           test al, 0x20
002E13C2  0F 85 87 00 00 00               jne 0x1402e144f
002E13C8  48 85 D2                        test rdx, rdx
002E13CB  0F 84 20 02 00 00               je 0x1402e15f1
002E13D1  49 8B CE                        mov rcx, r14
002E13D4  48 2B CA                        sub rcx, rdx
002E13D7  48 C1 F9 03                     sar rcx, 3
002E13DB  48 C1 E1 0C                     shl rcx, 0xc
002E13DF  44 8B 76 20                     mov r14d, dword ptr [rsi + 0x20]
002E13E3  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002E13E6  41 81 E6 C0 FF 00 00            and r14d, 0xffc0
002E13ED  49 C1 E6 1A                     shl r14, 0x1a
002E13F1  4C 0B F0                        or r14, rax
002E13F4  49 C1 E6 0C                     shl r14, 0xc
002E13F8  4C 03 F1                        add r14, rcx
002E13FB  8B 43 BC                        mov eax, dword ptr [rbx - 0x44]
002E13FE  48 8D 53 C0                     lea rdx, [rbx - 0x40]
002E1402  0F B6 6B C1                     movzx ebp, byte ptr [rbx - 0x3f]
002E1406  4C 8D 43 B8                     lea r8, [rbx - 0x48]
002E140A  0F B6 0A                        movzx ecx, byte ptr [rdx]
002E140D  48 C1 E5 20                     shl rbp, 0x20
002E1411  48 0B E8                        or rbp, rax
002E1414  48 C1 E1 20                     shl rcx, 0x20
002E1418  41 8B 00                        mov eax, dword ptr [r8]
002E141B  48 0B C8                        or rcx, rax
002E141E  48 2B E9                        sub rbp, rcx
002E1421  48 FF C5                        inc rbp
002E1424  48 C1 E5 0C                     shl rbp, 0xc
002E1428  49 03 EE                        add rbp, r14
002E142B  0F B6 32                        movzx esi, byte ptr [rdx]
002E142E  41 8B 00                        mov eax, dword ptr [r8]
002E1431  48 C1 E6 20                     shl rsi, 0x20
002E1435  48 0B F0                        or rsi, rax
002E1438  48 C1 E6 0C                     shl rsi, 0xc
002E143C  E9 44 FE FF FF                  jmp 0x1402e1285
002E1441  39 7A 04                        cmp dword ptr [rdx + 4], edi
002E1444  0F 84 5A FE FF FF               je 0x1402e12a4
002E144A  E9 FA FD FF FF                  jmp 0x1402e1249
002E144F  4C 3B F2                        cmp r14, rdx
002E1452  0F 82 EF 00 00 00               jb 0x1402e1547
002E1458  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
002E145B  48 8D 0C C2                     lea rcx, [rdx + rax*8]
002E145F  4C 3B F1                        cmp r14, rcx
002E1462  0F 83 DF 00 00 00               jae 0x1402e1547
002E1468  48 C1 E2 09                     shl rdx, 9
002E146C  49 C1 E6 09                     shl r14, 9
002E1470  4C 2B F2                        sub r14, rdx
002E1473  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002E1476  49 81 E6 00 F0 FF FF            and r14, 0xfffffffffffff000
002E147D  48 C1 E0 09                     shl rax, 9
002E1481  4C 03 F0                        add r14, rax
002E1484  E9 72 FF FF FF                  jmp 0x1402e13fb
002E1489  49 8B FE                        mov rdi, r14
002E148C  4D 3B E6                        cmp r12, r14
002E148F  72 09                           jb 0x1402e149a
002E1491  49 8B FC                        mov rdi, r12
002E1494  4D 2B E6                        sub r12, r14
002E1497  49 03 F4                        add rsi, r12
002E149A  48 8B CA                        mov rcx, rdx
002E149D  4C 8B F5                        mov r14, rbp
002E14A0  48 2B CF                        sub rcx, rdi
002E14A3  4C 2B F7                        sub r14, rdi
002E14A6  48 3B D5                        cmp rdx, rbp
002E14A9  4C 0F 46 F1                     cmovbe r14, rcx
002E14AD  4C 03 F6                        add r14, rsi
002E14B0  BA 30 00 00 00                  mov edx, 0x30
002E14B5  41 B8 4D 69 56 61               mov r8d, 0x6156694d
002E14BB  8D 4A 10                        lea ecx, [rdx + 0x10]
002E14BE  E8 7D A0 07 00                  call 0x14035b540
002E14C3  48 8B E8                        mov rbp, rax
002E14C6  48 85 C0                        test rax, rax
002E14C9  0F 84 A8 00 00 00               je 0x1402e1577
002E14CF  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
002E14D7  48 89 48 08                     mov qword ptr [rax + 8], rcx
002E14DB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
002E14DF  4C 89 70 18                     mov qword ptr [rax + 0x18], r14
002E14E3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
002E14E7  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
002E14EA  83 E0 03                        and eax, 3
002E14ED  89 45 28                        mov dword ptr [rbp + 0x28], eax
002E14F0  48 85 C9                        test rcx, rcx
002E14F3  74 2E                           je 0x1402e1523
002E14F5  4C 8D 49 D0                     lea r9, [rcx - 0x30]
002E14F9  41 0F 0D 09                     prefetchw byte ptr [r9]
002E14FD  49 8B 01                        mov rax, qword ptr [r9]
002E1500  48 85 C0                        test rax, rax
002E1503  74 7C                           je 0x1402e1581
002E1505  48 8D 48 01                     lea rcx, [rax + 1]
002E1509  F0 49 0F B1 09                  lock cmpxchg qword ptr [r9], rcx
002E150E  75 F0                           jne 0x1402e1500
002E1510  BA 01 00 00 00                  mov edx, 1
002E1515  41 B8 4D 6D 56 77               mov r8d, 0x77566d4d
002E151B  49 8B C9                        mov rcx, r9
002E151E  E8 5D F2 F2 FF                  call 0x140210780
002E1523  49 89 2F                        mov qword ptr [r15], rbp
002E1526  E9 79 FD FF FF                  jmp 0x1402e12a4
002E152B  45 85 C0                        test r8d, r8d
002E152E  0F 85 70 FD FF FF               jne 0x1402e12a4
002E1534  4C 8B F7                        mov r14, rdi
002E1537  49 8D 51 C0                     lea rdx, [r9 - 0x40]
002E153B  48 8B EF                        mov rbp, rdi
002E153E  4D 8D 41 B8                     lea r8, [r9 - 0x48]
002E1542  E9 E4 FE FF FF                  jmp 0x1402e142b
002E1547  4C 8B C6                        mov r8, rsi
002E154A  BA FF FF FF FF                  mov edx, 0xffffffff
002E154F  49 8B C9                        mov rcx, r9
002E1552  E8 01 78 06 00                  call 0x140348d58
002E1557  49 C1 E6 09                     shl r14, 9
002E155B  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
002E155F  48 C1 E1 09                     shl rcx, 9
002E1563  4C 2B F1                        sub r14, rcx
002E1566  E9 08 FF FF FF                  jmp 0x1402e1473
002E156B  4C 8D B6 00 10 00 00            lea r14, [rsi + 0x1000]
002E1572  E9 39 FF FF FF                  jmp 0x1402e14b0
002E1577  B8 9A 00 00 C0                  mov eax, 0xc000009a
002E157C  E9 25 FD FF FF                  jmp 0x1402e12a6
002E1581  33 D2                           xor edx, edx
002E1583  48 8B CD                        mov rcx, rbp
002E1586  E8 E5 12 8A 00                  call 0x140b82870
002E158B  E9 14 FD FF FF                  jmp 0x1402e12a4
002E1590  4D 8B 71 D0                     mov r14, qword ptr [r9 - 0x30]
002E1594  48 83 E6 FD                     and rsi, 0xfffffffffffffffd
002E1598  49 8B 69 D8                     mov rbp, qword ptr [r9 - 0x28]
002E159C  49 C1 E6 0C                     shl r14, 0xc
002E15A0  49 03 EE                        add rbp, r14
002E15A3  E9 DD FC FF FF                  jmp 0x1402e1285
002E15A8  41 8B 41 D0                     mov eax, dword ptr [r9 - 0x30]
002E15AC  0F BA E0 09                     bt eax, 9
002E15B0  0F 83 EE FC FF FF               jae 0x1402e12a4
002E15B6  84 C0                           test al, al
002E15B8  0F 88 E6 FC FF FF               js 0x1402e12a4
002E15BE  E9 EE FD FF FF                  jmp 0x1402e13b1
002E15C3  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
002E15C7  E9 20 FD FF FF                  jmp 0x1402e12ec
002E15CC  39 7A 04                        cmp dword ptr [rdx + 4], edi
002E15CF  0F 85 BF FD FF FF               jne 0x1402e1394
002E15D5  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
002E15DB  39 02                           cmp dword ptr [rdx], eax
002E15DD  0F 84 B1 FD FF FF               je 0x1402e1394
002E15E3  E9 BC FC FF FF                  jmp 0x1402e12a4
002E15E8  48 C1 E1 0C                     shl rcx, 0xc
002E15EC  E9 8C FC FF FF                  jmp 0x1402e127d
002E15F1  48 8B CF                        mov rcx, rdi
002E15F4  E9 E6 FD FF FF                  jmp 0x1402e13df
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiViewMayContainPage(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    result = (unsigned int)((*(unsigned __int64 *)(a4 + 16)) & (3));
    v_stack_p38 = 0;
    *(unsigned __int64 *)(a7) = 0;
    if (result == 1) goto loc_002E137C;
    if (a2 != 0) goto loc_002E1441;
loc_002E1249:
    if (result != 0) goto loc_002E12C4;
    result = (*(unsigned __int64 *)(a4 + 32)) & (0xFFFFFFFFFFFF0000ULL);
    result = (*(unsigned __int64 *)(a4 + 32)) >> (62);
    if (((unsigned __int8)(result)) != 3) goto loc_002E12A4;
    a1 = (unsigned int)((*(unsigned __int64 *)(a4 + 32)) & (63));
    if (condition_is_not_equal) goto loc_002E15E8;
loc_002E127D:
loc_002E1285:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_002E156B;
    if (a5 >= (result * 4 + (unsigned int)(0x40000ULL) * 1)) goto loc_002E12A4;
    if (a6 > (result * 4)) goto loc_002E1489;
loc_002E12A4:
    result = 0;
loc_002E12A6:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002E12C4:
    result = (result) - (1);
    if (condition_is_equal) goto loc_002E137C;
    result = (result) - (1);
    if (condition_is_equal) goto loc_002E1590;
    if (result != 1) goto loc_002E12A4;
    v_rsi = (v_stack_p18) & (-4);
loc_002E12EC:
    if ((unsigned int)(0x40000ULL) + 128 == 0) goto loc_002E12A4;
    result = MiStartingOffset((unsigned int)(0x40000ULL) + 128, *(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8), (unsigned int)(0xFFFFFFFFULL), a4);
    v_stack_p68 = result;
    result = MiEndingOffsetWithLock((unsigned int)(0x40000ULL) + 128, *(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8), (unsigned int)(0xFFFFFFFFULL), a4);
    if (a5 < v_stack_p68) goto loc_002E15C3;
    if (a5 >= result) goto loc_002E15C3;
    result = (a5) - (v_stack_p68);
    result = (result) >> (12);
    if ((*(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8) + result * 8) >= (*(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8) + (unsigned int)(*(unsigned int *)((unsigned int)(0x40000ULL) + 128 + 44)) * 8)) goto loc_002E12A4;
    if ((*(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8) + result * 8) >= (*(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8) + (unsigned int)(*(unsigned int *)((unsigned int)(0x40000ULL) + 128 + 44)) * 8)) goto loc_002E1362;
    if (((*(unsigned int *)(a1 + 56)) & (0x8000000ULL)) != 0) goto loc_002E12A4;
loc_002E1362:
    a2 = (*(unsigned __int64 *)((unsigned int)(0x40000ULL) + 128 + 8) + result * 8) - (*(unsigned __int64 *)(a1 + 136));
    a2 = (a2) >> (3);
    a2 = (a2) << (12);
    v_rsi = (v_rsi) + (a2);
    goto loc_002E1285;
loc_002E137C:
    a1 = (v_rsi) & (-2);
    v_stack_p80 = a1;
    if (a2 != 0) goto loc_002E15CC;
loc_002E1394:
    a3 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) & (32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) != 0) goto loc_002E152B;
    if ((unsigned int)(a3) != 0) goto loc_002E15A8;
loc_002E13B1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 - 24)) + 56)))) & (32)) != 0) goto loc_002E144F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 - 24) + 8) == 0) goto loc_002E15F1;
    a1 = (*(unsigned __int64 *)(a4 - 16)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 - 24) + 8));
    a1 = (a1) >> (3);
    a1 = (a1) << (12);
loc_002E13DF:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 - 24) + 32))) & (0xFFC0ULL));
    v_r14 = (v_r14) << (26);
    v_r14 = (v_r14) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 - 24) + 36)));
    v_r14 = (v_r14) << (12);
    v_r14 = (v_r14) + (a1);
loc_002E13FB:
    v_rbp = (*(unsigned __int8 *)(v_stack_p8 - 63)) << (32);
    v_rbp = (v_rbp) | ((unsigned int)(*(unsigned int *)(v_stack_p8 - 68)));
    a1 = (*(unsigned __int8 *)(v_stack_p8 - 64)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_p8 - 72)));
    v_rbp = (v_rbp) - (a1);
    v_rbp = (v_rbp) + 1;
    v_rbp = (v_rbp) << (12);
    v_rbp = (v_rbp) + (v_r14);
loc_002E142B:
    v_rsi = (*(unsigned __int8 *)(v_stack_p8 - 64)) << (32);
    v_rsi = (v_rsi) | ((unsigned int)(*(unsigned int *)(v_stack_p8 - 72)));
    v_rsi = (v_rsi) << (12);
    goto loc_002E1285;
loc_002E1441:
    if ((*(unsigned int *)(v_stack_p8 - 64 + 4)) == 0) goto loc_002E12A4;
    goto loc_002E1249;
loc_002E144F:
    if (v_r14 < (v_stack_p8 - 64)) goto loc_002E1547;
    if (v_r14 >= (v_stack_p8 - 64 + (unsigned int)(*(unsigned int *)(v_rsi + 44)) * 8)) goto loc_002E1547;
    a2 = (v_stack_p8 - 64) << (9);
    v_r14 = (v_r14) << (9);
    v_r14 = (v_r14) - (a2);
loc_002E1473:
    v_r14 = (v_r14) & (0xFFFFFFFFFFFFF000ULL);
    result = ((unsigned int)(*(unsigned int *)(v_rsi + 36))) << (9);
    v_r14 = (v_r14) + (result);
    goto loc_002E13FB;
loc_002E1489:
    v_rdi = v_r14;
    v_r12 = a5;
    if (a5 >= v_r14) {
        v_rdi = a5;
        v_r12 = (a5) - (v_r14);
        v_rsi = (v_rsi) + (v_r12);
    }
    a1 = (a2) - (v_rdi);
    v_r14 = (v_rbp) - (v_rdi);
    if (a2 <= v_rbp) { v_r14 = a1; }
    v_r14 = (v_r14) + (v_rsi);
loc_002E14B0:
    result = MiAllocatePool(48 + 16, 48, (unsigned int)(0x6156694DULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a4 - 24)));
    if (result == 0) goto loc_002E1577;
    *(unsigned __int64 *)(result + 8) = a7;
    *(unsigned __int64 *)(result + 16) = v_rsi;
    *(unsigned __int64 *)(result + 24) = v_r14;
    *(unsigned __int64 *)(result + 32) = v_rdi;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) & (3));
    *(unsigned int *)(result + 40) = (unsigned int)(result);
    if (a7 == 0) goto loc_002E1523;
loc_002E1500:
    if (*(unsigned __int64 *)(a7 - 48) == 0) goto loc_002E1581;
    if (*(unsigned __int64 *)(a7 - 48) != 0) goto loc_002E1500;
    result = ObpTraceObjectReferenceIfActive(a7 - 48, 1, (unsigned int)(0x77566D4DULL), a7 - 48);
loc_002E1523:
    *(unsigned __int64 *)(a7) = result;
    goto loc_002E12A4;
loc_002E152B:
    if ((unsigned int)((unsigned int)(0x77566D4DULL)) != 0) goto loc_002E12A4;
    goto loc_002E142B;
loc_002E1547:
    result = MiGetSharedProtos(a7 - 48, (unsigned int)(0xFFFFFFFFULL), v_rsi, a7 - 48);
    v_r14 = (v_rdi) << (9);
    a1 = (*(unsigned __int64 *)(result + 72)) << (9);
    v_r14 = (v_r14) - (a1);
    goto loc_002E1473;
loc_002E156B:
    goto loc_002E14B0;
loc_002E1577:
    goto loc_002E12A6;
loc_002E1581:
    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, v_rsi, a7 - 48);
    goto loc_002E12A4;
loc_002E1590:
    v_rsi = (v_rsi) & (-3);
    v_r14 = (*(unsigned __int64 *)(a7 - 48 - 48)) << (12);
    v_rbp = (*(unsigned __int64 *)(a7 - 48 - 40)) + (v_r14);
    goto loc_002E1285;
loc_002E15A8:
    if (condition_is_above_or_equal) goto loc_002E12A4;
    if (sign_flag) goto loc_002E12A4;
    goto loc_002E13B1;
loc_002E15C3:
    goto loc_002E12EC;
loc_002E15CC:
    if ((*(unsigned int *)(a2 + 4)) != ((unsigned int)(v_rdi))) goto loc_002E1394;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 464))))) goto loc_002E1394;
    goto loc_002E12A4;
loc_002E15E8:
    a1 = (v_rdi) << (12);
    goto loc_002E127D;
loc_002E15F1:
    goto loc_002E13DF;
}
```

## 5. (Beta) C Style

```c
int64_t MiViewMayContainPage(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, int64_t Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p38;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    result = (uint32_t)((*(uint64_t *)(arg4 + 0x10)) & (3));
    v_stack_p38 = 0;
    *(uint64_t *)(arg7) = 0;
    if (result == 1) goto loc_002E137C;
    if (Arg2 != 0) goto loc_002E1441;
loc_002E1249:
    if (result != 0) goto loc_002E12C4;
    result = (*(uint64_t *)(arg4 + 0x20)) & (0xFFFFFFFFFFFF0000ULL);
    result = (*(uint64_t *)(arg4 + 0x20)) >> (62);
    if (((uint8_t)(result)) != 3) goto loc_002E12A4;
    Arg1 = (uint32_t)((*(uint64_t *)(arg4 + 0x20)) & (63));
    if (condition_is_not_equal) goto loc_002E15E8;
loc_002E127D:
loc_002E1285:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_002E156B;
    if (Arg5 >= (result * 4 + (uint32_t)(0x40000ULL) * 1)) goto loc_002E12A4;
    if (Arg6 > (result * 4)) goto loc_002E1489;
loc_002E12A4:
    result = 0;
loc_002E12A6:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002E12C4:
    result = (result) - (1);
    if (condition_is_equal) goto loc_002E137C;
    result = (result) - (1);
    if (condition_is_equal) goto loc_002E1590;
    if (result != 1) goto loc_002E12A4;
    local_rsi = (v_stack_p18) & (-4);
loc_002E12EC:
    if ((uint32_t)(0x40000ULL) + 128 == 0) goto loc_002E12A4;
    result = MiStartingOffset((uint32_t)(0x40000ULL) + 128, *(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8), (uint32_t)(0xFFFFFFFFULL), Arg4);
    v_stack_p68 = result;
    result = MiEndingOffsetWithLock((uint32_t)(0x40000ULL) + 128, *(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8), (uint32_t)(0xFFFFFFFFULL), Arg4);
    if (Arg5 < v_stack_p68) goto loc_002E15C3;
    if (Arg5 >= result) goto loc_002E15C3;
    result = (Arg5) - (v_stack_p68);
    result = (result) >> (12);
    if ((*(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8) + result * 8) >= (*(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8) + (uint32_t)(*(uint32_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x2C)) * 8)) goto loc_002E12A4;
    if ((*(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8) + result * 8) >= (*(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8) + (uint32_t)(*(uint32_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x2C)) * 8)) goto loc_002E1362;
    if (((*(uint32_t *)(arg1 + 0x38)) & (0x8000000ULL)) != 0) goto loc_002E12A4;
loc_002E1362:
    Arg2 = (*(uint64_t *)((uint32_t)(0x40000ULL) + 0x80 + 0x8) + result * 8) - (*(uint64_t *)(arg1 + 0x88));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (12);
    local_rsi = (local_rsi) + (Arg2);
    goto loc_002E1285;
loc_002E137C:
    Arg1 = (local_rsi) & (-2);
    v_stack_p80 = Arg1;
    if (Arg2 != 0) goto loc_002E15CC;
loc_002E1394:
    Arg3 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) & (32));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) != 0) goto loc_002E152B;
    if ((uint32_t)(Arg3) != 0) goto loc_002E15A8;
loc_002E13B1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg4 - 0x18)) + 0x38)))) & (32)) != 0) goto loc_002E144F;
    if (*(uint64_t *)(*(uint64_t *)(arg4 - 0x18) + 0x8) == 0) goto loc_002E15F1;
    Arg1 = (*(uint64_t *)(arg4 - 0x10)) - (*(uint64_t *)(*(uint64_t *)(arg4 - 0x18) + 0x8));
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) << (12);
loc_002E13DF:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 - 0x18) + 0x20))) & (0xFFC0ULL));
    local_r14 = (local_r14) << (26);
    local_r14 = (local_r14) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 - 0x18) + 0x24)));
    local_r14 = (local_r14) << (12);
    local_r14 = (local_r14) + (Arg1);
loc_002E13FB:
    local_rbp = (*(uint8_t *)(v_stack_p8 - 0x3F)) << (32);
    local_rbp = (local_rbp) | ((uint32_t)(*(uint32_t *)(v_stack_p8 - 0x44)));
    Arg1 = (*(uint8_t *)(v_stack_p8 - 0x40)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_p8 - 0x48)));
    local_rbp = (local_rbp) - (Arg1);
    local_rbp = (local_rbp) + 1;
    local_rbp = (local_rbp) << (12);
    local_rbp = (local_rbp) + (local_r14);
loc_002E142B:
    local_rsi = (*(uint8_t *)(v_stack_p8 - 0x40)) << (32);
    local_rsi = (local_rsi) | ((uint32_t)(*(uint32_t *)(v_stack_p8 - 0x48)));
    local_rsi = (local_rsi) << (12);
    goto loc_002E1285;
loc_002E1441:
    if ((*(uint32_t *)(v_stack_p8 - 0x40 + 0x4)) == 0) goto loc_002E12A4;
    goto loc_002E1249;
loc_002E144F:
    if (local_r14 < (v_stack_p8 - 64)) goto loc_002E1547;
    if (local_r14 >= (v_stack_p8 - 64 + (uint32_t)(*(uint32_t *)(local_rsi + 0x2C)) * 8)) goto loc_002E1547;
    Arg2 = (v_stack_p8 - 64) << (9);
    local_r14 = (local_r14) << (9);
    local_r14 = (local_r14) - (Arg2);
loc_002E1473:
    local_r14 = (local_r14) & (0xFFFFFFFFFFFFF000ULL);
    result = ((uint32_t)(*(uint32_t *)(local_rsi + 0x24))) << (9);
    local_r14 = (local_r14) + (result);
    goto loc_002E13FB;
loc_002E1489:
    local_rdi = local_r14;
    local_r12 = Arg5;
    if (Arg5 >= local_r14) {
        local_rdi = Arg5;
        local_r12 = (Arg5) - (local_r14);
        local_rsi = (local_rsi) + (local_r12);
    }
    Arg1 = (Arg2) - (local_rdi);
    local_r14 = (local_rbp) - (local_rdi);
    if (Arg2 <= local_rbp) { local_r14 = Arg1; }
    local_r14 = (local_r14) + (local_rsi);
loc_002E14B0:
    result = MiAllocatePool(48 + 16, 48, (uint32_t)(0x6156694DULL), *(uint64_t *)(*(uint64_t *)(arg4 - 0x18)));
    if (result == 0) goto loc_002E1577;
    *(void **)(result + 0x8) = Arg7;
    *(uint64_t *)(result + 0x10) = local_rsi;
    *(uint64_t *)(result + 0x18) = local_r14;
    *(uint64_t *)(result + 0x20) = local_rdi;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) & (3));
    *(uint32_t *)(result + 0x28) = (uint32_t)(result);
    if (Arg7 == NULL) goto loc_002E1523;
loc_002E1500:
    if (*(uint64_t *)(arg7 - 0x30) == 0) goto loc_002E1581;
    if (*(uint64_t *)(arg7 - 0x30) != 0) goto loc_002E1500;
    result = ObpTraceObjectReferenceIfActive(Arg7 - 48, 1, (uint32_t)(0x77566D4DULL), Arg7 - 48);
loc_002E1523:
    *(uint64_t *)(arg7) = result;
    goto loc_002E12A4;
loc_002E152B:
    if ((uint32_t)((uint32_t)(0x77566D4DULL)) != 0) goto loc_002E12A4;
    goto loc_002E142B;
loc_002E1547:
    result = MiGetSharedProtos(Arg7 - 48, (uint32_t)(0xFFFFFFFFULL), local_rsi, Arg7 - 48);
    local_r14 = (local_rdi) << (9);
    Arg1 = (*(uint64_t *)(result + 0x48)) << (9);
    local_r14 = (local_r14) - (Arg1);
    goto loc_002E1473;
loc_002E156B:
    goto loc_002E14B0;
loc_002E1577:
    goto loc_002E12A6;
loc_002E1581:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, local_rsi, Arg7 - 48);
    goto loc_002E12A4;
loc_002E1590:
    local_rsi = (local_rsi) & (-3);
    local_r14 = (*(uint64_t *)(arg7 - 0x30 - 0x30)) << (12);
    local_rbp = (*(uint64_t *)(arg7 - 0x30 - 0x28)) + (local_r14);
    goto loc_002E1285;
loc_002E15A8:
    if (condition_is_above_or_equal) goto loc_002E12A4;
    if (sign_flag) goto loc_002E12A4;
    goto loc_002E13B1;
loc_002E15C3:
    goto loc_002E12EC;
loc_002E15CC:
    if ((*(uint32_t *)(Arg2 + 0x4)) != ((uint32_t)(local_rdi))) goto loc_002E1394;
    if ((*(uint32_t *)(Arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x1D0))))) goto loc_002E1394;
    goto loc_002E12A4;
loc_002E15E8:
    Arg1 = (local_rdi) << (12);
    goto loc_002E127D;
loc_002E15F1:
    goto loc_002E13DF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg4` | `- 0x48` | `64` | `R` |
| `Arg4` | `- 0x44` | `32` | `R` |
| `Arg4` | `- 0x40` | `64` | `R` |
| `Arg4` | `- 0x3F` | `8` | `R` |
| `Arg4` | `- 0x30` | `32` | `R` |
| `Arg4` | `- 0x30` | `64` | `R` |
| `Arg4` | `- 0x28` | `64` | `R` |
| `Arg4` | `- 0x18` | `64` | `R` |
| `Arg4` | `- 0x10` | `64` | `R` |
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E11F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
