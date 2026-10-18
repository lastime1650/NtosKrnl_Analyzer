# MiClearPteAccessed

- RVA: `0x00290630`–`0x00290A0C` (길이 `988` bytes)
- VA: `0x0000000140290630`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006741C`
- 디코드: `234`개 명령, `988/988` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00290701` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x0029071D` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00290737` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00290755` → [MiInsertTbFlushEntry](MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x00290784` → [MiGetVaAge](../24/MiGetVaAge_function_00240AC0.md) (function, `0x00240AC0`)
- `0x002907A6` → [MiSetVaAgeList](MiSetVaAgeList_function_00290A20.md) (function, `0x00290A20`)
- `0x00290868` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00290936` → [MiLogPageAccess](../24/MiLogPageAccess_function_00240870.md) (function, `0x00240870`)
- `0x00290968` → [MiUnlockNestedPageTableWritePte](../23/MiUnlockNestedPageTableWritePte_function_0023F4E4.md) (function, `0x0023F4E4`)
- `0x00290980` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00290990` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002909E0` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002909F1` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00290A02` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)

### Direct callers
- [MiResetAccessBitPteWorker](../22/MiResetAccessBitPteWorker_function_0022A6B8.md) at `0x0022A74E`
- [sub_0028FDDD](../28/Unknown_function_0028FDDD.md) at `0x002900A6`
- [MiCrcStillIntact](../31/MiCrcStillIntact_function_00317028.md) at `0x00317239`

### Static image references
- `0x00290887` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00290972` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002909D9` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00290630  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00290635  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0029063A  55                              push rbp
0029063B  56                              push rsi
0029063C  57                              push rdi
0029063D  41 54                           push r12
0029063F  41 55                           push r13
00290641  41 56                           push r14
00290643  41 57                           push r15
00290645  48 83 EC 30                     sub rsp, 0x30
00290649  44 8B BC 24 90 00 00 00         mov r15d, dword ptr [rsp + 0x90]
00290651  48 8B DA                        mov rbx, rdx
00290654  BA 01 00 00 00                  mov edx, 1
00290659  49 8B E8                        mov rbp, r8
0029065C  48 8B F1                        mov rsi, rcx
0029065F  4D 85 C9                        test r9, r9
00290662  0F 84 0A 02 00 00               je 0x140290872
00290668  44 8B EA                        mov r13d, edx
0029066B  41 8B C7                        mov eax, r15d
0029066E  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00290678  45 33 E4                        xor r12d, r12d
0029067B  41 D1 EF                        shr r15d, 1
0029067E  44 21 A4 24 80 00 00 00         and dword ptr [rsp + 0x80], r12d
00290686  44 23 FA                        and r15d, edx
00290689  44 21 64 24 70                  and dword ptr [rsp + 0x70], r12d
0029068E  23 C2                           and eax, edx
00290690  48 8B FD                        mov rdi, rbp
00290693  44 89 BC 24 90 00 00 00         mov dword ptr [rsp + 0x90], r15d
0029069B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0029069F  48 C1 E7 19                     shl rdi, 0x19
002906A3  49 8B C0                        mov rax, r8
002906A6  48 C1 E0 19                     shl rax, 0x19
002906AA  41 B1 0F                        mov r9b, 0xf
002906AD  48 2B F8                        sub rdi, rax
002906B0  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
002906B6  48 C1 FF 10                     sar rdi, 0x10
002906BA  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
002906C4  41 84 C1                        test r9b, al
002906C7  0F 85 08 01 00 00               jne 0x1402907d5
002906CD  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
002906D3  49 BA FF FF FF FF FF FF FF 3F   movabs r10, 0x3fffffffffffffff
002906DD  41 84 C1                        test r9b, al
002906E0  0F 85 BF 01 00 00               jne 0x1402908a5
002906E6  45 33 F6                        xor r14d, r14d
002906E9  45 85 ED                        test r13d, r13d
002906EC  0F 85 D2 00 00 00               jne 0x1402907c4
002906F2  4C 8B F2                        mov r14, rdx
002906F5  EB 1E                           jmp 0x140290715
002906F7  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
002906FB  48 8B CE                        mov rcx, rsi
002906FE  48 8B D5                        mov rdx, rbp
00290701  E8 8A E1 FA FF                  call 0x14023e890
00290706  45 85 F6                        test r14d, r14d
00290709  0F 85 E2 00 00 00               jne 0x1402907f1
0029070F  41 BE 01 00 00 00               mov r14d, 1
00290715  45 85 ED                        test r13d, r13d
00290718  74 40                           je 0x14029075a
0029071A  48 8B CD                        mov rcx, rbp
0029071D  E8 7E 21 FF FF                  call 0x1402828a0
00290722  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
00290727  0F 85 25 02 00 00               jne 0x140290952
0029072D  48 83 E0 DF                     and rax, 0xffffffffffffffdf
00290731  48 8B CD                        mov rcx, rbp
00290734  48 8B D0                        mov rdx, rax
00290737  E8 D4 10 FF FF                  call 0x140281810
0029073C  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00290744  45 8B FE                        mov r15d, r14d
00290747  48 85 C9                        test rcx, rcx
0029074A  74 0E                           je 0x14029075a
0029074C  45 33 C9                        xor r9d, r9d
0029074F  4D 8B C6                        mov r8, r14
00290752  48 8B D7                        mov rdx, rdi
00290755  E8 16 2F 00 00                  call 0x140293670
0029075A  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00290762  74 18                           je 0x14029077c
00290764  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0029076E  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
00290773  45 85 E4                        test r12d, r12d
00290776  0F 85 7F 02 00 00               jne 0x1402909fb
0029077C  45 85 FF                        test r15d, r15d
0029077F  74 2A                           je 0x1402907ab
00290781  48 8B D7                        mov rdx, rdi
00290784  E8 37 03 FB FF                  call 0x140240ac0
00290789  83 7C 24 20 00                  cmp dword ptr [rsp + 0x20], 0
0029078E  8A D8                           mov bl, al
00290790  0F 85 91 01 00 00               jne 0x140290927
00290796  84 DB                           test bl, bl
00290798  75 11                           jne 0x1402907ab
0029079A  45 8A CE                        mov r9b, r14b
0029079D  45 8B C6                        mov r8d, r14d
002907A0  48 8B D7                        mov rdx, rdi
002907A3  48 8B CE                        mov rcx, rsi
002907A6  E8 75 02 00 00                  call 0x140290a20
002907AB  41 8B C6                        mov eax, r14d
002907AE  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
002907B3  48 83 C4 30                     add rsp, 0x30
002907B7  41 5F                           pop r15
002907B9  41 5E                           pop r14
002907BB  41 5D                           pop r13
002907BD  41 5C                           pop r12
002907BF  5F                              pop rdi
002907C0  5E                              pop rsi
002907C1  5D                              pop rbp
002907C2  C3                              ret
002907C3  CC                              int3
002907C4  49 8B C0                        mov rax, r8
002907C7  48 3B F8                        cmp rdi, rax
002907CA  0F 82 36 FF FF FF               jb 0x140290706
002907D0  E9 1B 01 00 00                  jmp 0x1402908f0
002907D5  49 8B C0                        mov rax, r8
002907D8  48 3B F8                        cmp rdi, rax
002907DB  0F 82 EC FE FF FF               jb 0x1402906cd
002907E1  48 8B C1                        mov rax, rcx
002907E4  48 3B F8                        cmp rdi, rax
002907E7  0F 87 E0 FE FF FF               ja 0x1402906cd
002907ED  33 C0                           xor eax, eax
002907EF  EB BD                           jmp 0x1402907ae
002907F1  45 85 E4                        test r12d, r12d
002907F4  0F 85 DF 01 00 00               jne 0x1402909d9
002907FA  41 BF 01 00 00 00               mov r15d, 1
00290800  45 33 F6                        xor r14d, r14d
00290803  44 89 BC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r15d
0029080B  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00290812  72 70                           jb 0x140290884
00290814  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00290818  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00290822  48 23 C1                        and rax, rcx
00290825  49 3B C7                        cmp rax, r15
00290828  44 8B BC 24 90 00 00 00         mov r15d, dword ptr [rsp + 0x90]
00290830  0F 86 CB 00 00 00               jbe 0x140290901
00290836  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0029083A  48 85 C0                        test rax, rax
0029083D  0F 88 BE 00 00 00               js 0x140290901
00290843  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0029084D  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
00290852  45 85 E4                        test r12d, r12d
00290855  0F 85 8F 01 00 00               jne 0x1402909ea
0029085B  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
00290860  74 8B                           je 0x1402907ed
00290862  48 8B D5                        mov rdx, rbp
00290865  48 8B CE                        mov rcx, rsi
00290868  E8 53 66 F8 FF                  call 0x140216ec0
0029086D  E9 7B FF FF FF                  jmp 0x1402907ed
00290872  41 F6 C7 04                     test r15b, 4
00290876  0F 85 EC FD FF FF               jne 0x140290668
0029087C  45 33 ED                        xor r13d, r13d
0029087F  E9 E7 FD FF FF                  jmp 0x14029066b
00290884  45 03 F7                        add r14d, r15d
00290887  44 85 35 1E 4A D3 00            test dword ptr [rip + 0xd34a1e], r14d
0029088E  0F 84 DE 00 00 00               je 0x140290972
00290894  F3 90                           pause
00290896  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0029089A  48 85 C0                        test rax, rax
0029089D  0F 89 68 FF FF FF               jns 0x14029080b
002908A3  EB DF                           jmp 0x140290884
002908A5  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002908A9  49 23 C2                        and rax, r10
002908AC  48 3B C2                        cmp rax, rdx
002908AF  0F 87 8B 00 00 00               ja 0x140290940
002908B5  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
002908BB  41 84 C1                        test r9b, al
002908BE  74 0C                           je 0x1402908cc
002908C0  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002908C3  66 3B C2                        cmp ax, dx
002908C6  0F 87 21 FF FF FF               ja 0x1402907ed
002908CC  44 8B F2                        mov r14d, edx
002908CF  45 85 ED                        test r13d, r13d
002908D2  0F 84 22 FF FF FF               je 0x1402907fa
002908D8  49 8B C0                        mov rax, r8
002908DB  48 3B F8                        cmp rdi, rax
002908DE  0F 82 E0 FE FF FF               jb 0x1402907c4
002908E4  48 8B C1                        mov rax, rcx
002908E7  48 3B F8                        cmp rdi, rax
002908EA  0F 86 AA 00 00 00               jbe 0x14029099a
002908F0  48 8B C1                        mov rax, rcx
002908F3  48 3B F8                        cmp rdi, rax
002908F6  0F 87 0A FE FF FF               ja 0x140290706
002908FC  E9 F6 FD FF FF                  jmp 0x1402906f7
00290901  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
00290907  41 BE 01 00 00 00               mov r14d, 1
0029090D  A8 0F                           test al, 0xf
0029090F  0F 84 00 FE FF FF               je 0x140290715
00290915  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00290918  66 41 3B C6                     cmp ax, r14w
0029091C  0F 87 21 FF FF FF               ja 0x140290843
00290922  E9 EE FD FF FF                  jmp 0x140290715
00290927  80 FB 07                        cmp bl, 7
0029092A  0F 84 7B FE FF FF               je 0x1402907ab
00290930  48 8B D5                        mov rdx, rbp
00290933  48 8B CE                        mov rcx, rsi
00290936  E8 35 FF FA FF                  call 0x140240870
0029093B  E9 56 FE FF FF                  jmp 0x140290796
00290940  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00290944  48 85 C0                        test rax, rax
00290947  0F 89 A0 FE FF FF               jns 0x1402907ed
0029094D  E9 63 FF FF FF                  jmp 0x1402908b5
00290952  49 B8 DF FF FF FF FF FF FF CF   movabs r8, 0xcfffffffffffffdf
0029095C  45 8B CC                        mov r9d, r12d
0029095F  4C 23 C0                        and r8, rax
00290962  48 8B D5                        mov rdx, rbp
00290965  48 8B CE                        mov rcx, rsi
00290968  E8 77 EB FA FF                  call 0x14023f4e4
0029096D  E9 CA FD FF FF                  jmp 0x14029073c
00290972  8B 05 40 61 D3 00               mov eax, dword ptr [rip + 0xd36140]
00290978  A8 40                           test al, 0x40
0029097A  0F 84 14 FF FF FF               je 0x140290894
00290980  E8 0B EB 07 00                  call 0x14030f490
00290985  84 C0                           test al, al
00290987  0F 84 07 FF FF FF               je 0x140290894
0029098D  41 8B CE                        mov ecx, r14d
00290990  E8 CB EA 07 00                  call 0x14030f460
00290995  E9 FC FE FF FF                  jmp 0x140290896
0029099A  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
002909A0  41 84 C1                        test r9b, al
002909A3  0F 84 4E FD FF FF               je 0x1402906f7
002909A9  48 8B CD                        mov rcx, rbp
002909AC  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002909B6  48 C1 E9 09                     shr rcx, 9
002909BA  48 23 C8                        and rcx, rax
002909BD  49 8B C0                        mov rax, r8
002909C0  48 03 C8                        add rcx, rax
002909C3  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
002909CD  48 3B C8                        cmp rcx, rax
002909D0  41 0F 94 C4                     sete r12b
002909D4  E9 1E FD FF FF                  jmp 0x1402906f7
002909D9  48 8D 0D E0 6A BA 00            lea rcx, [rip + 0xba6ae0]
002909E0  E8 9B 84 FB FF                  call 0x140248e80
002909E5  E9 10 FE FF FF                  jmp 0x1402907fa
002909EA  48 8D 0D CF 6A BA 00            lea rcx, [rip + 0xba6acf]
002909F1  E8 EA 8D FB FF                  call 0x1402497e0
002909F6  E9 60 FE FF FF                  jmp 0x14029085b
002909FB  48 8D 0D BE 6A BA 00            lea rcx, [rip + 0xba6abe]
00290A02  E8 D9 8D FB FF                  call 0x1402497e0
00290A07  E9 70 FD FF FF                  jmp 0x14029077c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiClearPteAccessed(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p70;
    unsigned int v_stack_p8;
    unsigned int v_stack_p80;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (48);
    if (a4 == 0) goto loc_00290872;
loc_00290668:
loc_0029066B:
    v_r12 = 0;
    v_r15 = (unsigned int)(((unsigned int)(a5)) >> (1));
    v_r15 = (unsigned int)((v_r15) & (1));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    v_stack_p28 = (unsigned int)(v_r15);
    v_stack_m48 = (unsigned int)(result);
    v_rdi = (a3) << (25);
    result = (a3) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    if (((15) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184))))) != 0) goto loc_002907D5;
loc_002906CD:
    if (((15) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184))))) != 0) goto loc_002908A5;
    v_r14 = 0;
    if (1 != 0) goto loc_002907C4;
    goto loc_00290715;
loc_002906F7:
    v_stack_p8 = 1;
    result = MiLockNestedPageTable(a1, a3, a3, 15);
loc_00290706:
    if (1 != 0) goto loc_002907F1;
loc_00290715:
    if (1 == 0) goto loc_0029075A;
    result = MI_READ_PTE_LOCK_FREE(a3, a3, a3, 15);
    if (v_stack_p8 != 0) goto loc_00290952;
    result = (result) & (-33);
    result = MiWriteValidPteNewProtection(a3, result, a3, 15);
loc_0029073C:
    if (v_stack_p20 != 0) {
        a4 = 0;
        a3 = 1;
        a2 = v_rdi;
        result = MiInsertTbFlushEntry(v_stack_p20, a2, a3, a4);
    }
    if (v_stack_p18 == 0) goto loc_0029077C;
    if (0 != 0) goto loc_002909FB;
loc_0029077C:
    if (1 == 0) goto loc_002907AB;
    result = MiGetVaAge(v_stack_p20, v_rdi, a3, a4);
    if (v_stack_m48 != 0) goto loc_00290927;
loc_00290796:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) {
        a4 = 1;
        a3 = 1;
        a2 = v_rdi;
        a1 = a1;
        result = MiSetVaAgeList(a1, a2, a3, a4);
    }
loc_002907AE:
    v_rsp = (v_rsp) + (48);
    return 1;
loc_002907C4:
    if (v_rdi < a3) goto loc_00290706;
    goto loc_002908F0;
loc_002907D5:
    if (v_rdi < a3) goto loc_002906CD;
    if (v_rdi > a1) goto loc_002906CD;
loc_002907ED:
    result = 0;
    goto loc_002907AE;
loc_002907F1:
    if (0 != 0) goto loc_002909D9;
loc_002907FA:
    v_r14 = 0;
    v_stack_p80 = 1;
loc_0029080B:
    if (condition_is_below) goto loc_00290884;
    result = (*(unsigned __int64 *)(v_stack_p10 + 24)) & (a1);
    if (result <= 1) goto loc_00290901;
    if (sign_flag) goto loc_00290901;
loc_00290843:
    if (0 != 0) goto loc_002909EA;
loc_0029085B:
    if (v_stack_p70 == 0) goto loc_002907ED;
    result = MiUnlockPageTable(a1, a3, a3, a4);
    goto loc_002907ED;
loc_00290872:
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) != 0) goto loc_00290668;
    v_r13 = 0;
    goto loc_0029066B;
loc_00290884:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)(a5))));
    if (((*(unsigned int *)(v_rip + 13847070)) & ((unsigned int)(v_r14))) == 0) goto loc_00290972;
loc_00290894:
loc_00290896:
    if (!sign_flag) goto loc_0029080B;
    goto loc_00290884;
loc_002908A5:
    result = (*(unsigned __int64 *)(v_stack_p10 + 24)) & (v_r10);
    if (result > a3) goto loc_00290940;
loc_002908B5:
    if ((((unsigned __int8)(a4)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184))))) == 0) goto loc_002908CC;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)))) > ((unsigned __int16)(a3))) goto loc_002907ED;
loc_002908CC:
    if (0 == 0) goto loc_002907FA;
    if (v_rdi < a3) goto loc_002907C4;
    if (v_rdi <= a1) goto loc_0029099A;
loc_002908F0:
    if (v_rdi > a1) goto loc_00290706;
    goto loc_002906F7;
loc_00290901:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) == 0) goto loc_00290715;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)))) > 1) goto loc_00290843;
    goto loc_00290715;
loc_00290927:
    if (((unsigned __int8)(v_stack_p10)) == 7) goto loc_002907AB;
    result = MiLogPageAccess(a1, a3, a3, a4);
    goto loc_00290796;
loc_00290940:
    if (!sign_flag) goto loc_002907ED;
    goto loc_002908B5;
loc_00290952:
    a3 = (a3) & (*(unsigned __int64 *)(v_stack_p10 + 40));
    result = MiUnlockNestedPageTableWritePte(a1, a3, a3, 0);
    goto loc_0029073C;
loc_00290972:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13852992)))) & (64)) == 0) goto loc_00290894;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a3, a3, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00290894;
    result = HvlNotifyLongSpinWait(1, a3, a3, 0);
    goto loc_00290896;
loc_0029099A:
    if (((0) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184))))) == 0) goto loc_002906F7;
    a1 = (a3) >> (9);
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(a1 + 184)));
    a1 = (a1) + (a3);
    v_r12 = (a1 == a3) ? 1 : 0;
    goto loc_002906F7;
loc_002909D9:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12217056, a3, a3, 0);
    goto loc_002907FA;
loc_002909EA:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12217039, a3, a3, 0);
    goto loc_0029085B;
loc_002909FB:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12217022, a3, a3, 0);
    goto loc_0029077C;
}
```

## 5. (Beta) C Style

```c
int64_t MiClearPteAccessed(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p70;
    uint32_t v_stack_p8;
    uint32_t v_stack_p80;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (48);
    if (Arg4 == 0) goto loc_00290872;
loc_00290668:
loc_0029066B:
    local_r12 = 0;
    local_r15 = (uint32_t)(((uint32_t)(Arg5)) >> (1));
    local_r15 = (uint32_t)((local_r15) & (1));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    v_stack_p28 = (uint32_t)(local_r15);
    v_stack_m48 = (uint32_t)(result);
    local_rdi = (Arg3) << (25);
    result = (Arg3) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    if (((15) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8))))) != 0) goto loc_002907D5;
loc_002906CD:
    if (((15) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8))))) != 0) goto loc_002908A5;
    local_r14 = 0;
    if (1 != 0) goto loc_002907C4;
    goto loc_00290715;
loc_002906F7:
    v_stack_p8 = 1;
    result = MiLockNestedPageTable(Arg1, Arg3, Arg3, 15);
loc_00290706:
    if (1 != 0) goto loc_002907F1;
loc_00290715:
    if (1 == 0) goto loc_0029075A;
    result = MI_READ_PTE_LOCK_FREE(Arg3, Arg3, Arg3, 15);
    if (v_stack_p8 != 0) goto loc_00290952;
    result = (result) & (-33);
    result = MiWriteValidPteNewProtection(Arg3, result, Arg3, 15);
loc_0029073C:
    if (v_stack_p20 != 0) {
        Arg4 = 0;
        Arg3 = 1;
        Arg2 = local_rdi;
        result = MiInsertTbFlushEntry(v_stack_p20, Arg2, Arg3, Arg4);
    }
    if (v_stack_p18 == 0) goto loc_0029077C;
    if (0 != 0) goto loc_002909FB;
loc_0029077C:
    if (1 == 0) goto loc_002907AB;
    result = MiGetVaAge(v_stack_p20, local_rdi, Arg3, Arg4);
    if (v_stack_m48 != 0) goto loc_00290927;
loc_00290796:
    if ((uint8_t)((uint8_t)(result)) == 0) {
        Arg4 = 1;
        Arg3 = 1;
        Arg2 = local_rdi;
        Arg1 = Arg1;
        result = MiSetVaAgeList(Arg1, Arg2, Arg3, Arg4);
    }
loc_002907AE:
    local_rsp = (local_rsp) + (48);
    return 1;
loc_002907C4:
    if (local_rdi < Arg3) goto loc_00290706;
    goto loc_002908F0;
loc_002907D5:
    if (local_rdi < Arg3) goto loc_002906CD;
    if (local_rdi > Arg1) goto loc_002906CD;
loc_002907ED:
    result = 0;
    goto loc_002907AE;
loc_002907F1:
    if (0 != 0) goto loc_002909D9;
loc_002907FA:
    local_r14 = 0;
    v_stack_p80 = 1;
loc_0029080B:
    if (condition_is_below) goto loc_00290884;
    result = (*(uint64_t *)(v_stack_p10 + 0x18)) & (Arg1);
    if (result <= 1) goto loc_00290901;
    if (sign_flag) goto loc_00290901;
loc_00290843:
    if (0 != 0) goto loc_002909EA;
loc_0029085B:
    if (v_stack_p70 == 0) goto loc_002907ED;
    result = MiUnlockPageTable(Arg1, Arg3, Arg3, Arg4);
    goto loc_002907ED;
loc_00290872:
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) != 0) goto loc_00290668;
    local_r13 = 0;
    goto loc_0029066B;
loc_00290884:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)(Arg5))));
    if (((*(uint32_t *)(v_rip + 0xD34A1E)) & ((uint32_t)(local_r14))) == 0) goto loc_00290972;
loc_00290894:
loc_00290896:
    if (!sign_flag) goto loc_0029080B;
    goto loc_00290884;
loc_002908A5:
    result = (*(uint64_t *)(v_stack_p10 + 0x18)) & (local_r10);
    if (result > Arg3) goto loc_00290940;
loc_002908B5:
    if ((((uint8_t)(Arg4)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8))))) == 0) goto loc_002908CC;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)))) > ((uint16_t)(Arg3))) goto loc_002907ED;
loc_002908CC:
    if (0 == 0) goto loc_002907FA;
    if (local_rdi < Arg3) goto loc_002907C4;
    if (local_rdi <= Arg1) goto loc_0029099A;
loc_002908F0:
    if (local_rdi > Arg1) goto loc_00290706;
    goto loc_002906F7;
loc_00290901:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) == 0) goto loc_00290715;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)))) > 1) goto loc_00290843;
    goto loc_00290715;
loc_00290927:
    if (((uint8_t)(v_stack_p10)) == 7) goto loc_002907AB;
    result = MiLogPageAccess(Arg1, Arg3, Arg3, Arg4);
    goto loc_00290796;
loc_00290940:
    if (!sign_flag) goto loc_002907ED;
    goto loc_002908B5;
loc_00290952:
    Arg3 = (Arg3) & (*(uint64_t *)(v_stack_p10 + 0x28));
    result = MiUnlockNestedPageTableWritePte(Arg1, Arg3, Arg3, 0);
    goto loc_0029073C;
loc_00290972:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD36140)))) & (64)) == 0) goto loc_00290894;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg3, Arg3, 0);
    if ((uint8_t)(result) == 0) goto loc_00290894;
    result = HvlNotifyLongSpinWait(1, Arg3, Arg3, 0);
    goto loc_00290896;
loc_0029099A:
    if (((0) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8))))) == 0) goto loc_002906F7;
    Arg1 = (Arg3) >> (9);
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    Arg1 = (Arg1) + (Arg3);
    local_r12 = (Arg1 == Arg3) ? 1 : 0;
    goto loc_002906F7;
loc_002909D9:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12217056, Arg3, Arg3, 0);
    goto loc_002907FA;
loc_002909EA:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12217039, Arg3, Arg3, 0);
    goto loc_0029085B;
loc_002909FB:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12217022, Arg3, Arg3, 0);
    goto loc_0029077C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00290630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
