# MiDpcGangTarget

- RVA: `0x00697E60`–`0x00698185` (길이 `805` bytes)
- VA: `0x0000000140697E60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8AAC`
- 디코드: `233`개 명령, `805/805` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00697F1B` → [MiGetGangAssignment](../4F/MiGetGangAssignment_function_004F8080.md) (function, `0x004F8080`)
- `0x00697F63` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00697FA6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00697FB6` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x0069800A` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x00698032` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00698059` → [MiDoGangAssignment](../4D/MiDoGangAssignment_function_004DE270.md) (function, `0x004DE270`)
- `0x00698098` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x006980C8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x006980D8` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x0069812C` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x00698153` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00697F8B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00697F98` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00697FBF` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00697E60  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00697E65  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00697E6A  55                              push rbp
00697E6B  56                              push rsi
00697E6C  57                              push rdi
00697E6D  41 54                           push r12
00697E6F  41 55                           push r13
00697E71  41 56                           push r14
00697E73  41 57                           push r15
00697E75  48 8B EC                        mov rbp, rsp
00697E78  48 83 EC 30                     sub rsp, 0x30
00697E7C  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00697E85  45 33 E4                        xor r12d, r12d
00697E88  48 83 65 F8 00                  and qword ptr [rbp - 8], 0
00697E8D  49 8B D9                        mov rbx, r9
00697E90  4D 8B E8                        mov r13, r8
00697E93  48 8B FA                        mov rdi, rdx
00697E96  45 8D 54 24 01                  lea r10d, [r12 + 1]
00697E9B  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
00697EA2  0F B7 81 8A 00 00 00            movzx eax, word ptr [rcx + 0x8a]
00697EA9  44 38 A2 D4 00 00 00            cmp byte ptr [rdx + 0xd4], r12b
00697EB0  75 08                           jne 0x140697eba
00697EB2  3B 82 C0 00 00 00               cmp eax, dword ptr [rdx + 0xc0]
00697EB8  75 69                           jne 0x140697f23
00697EBA  44 39 92 BC 00 00 00            cmp dword ptr [rdx + 0xbc], r10d
00697EC1  75 0F                           jne 0x140697ed2
00697EC3  33 C0                           xor eax, eax
00697EC5  F0 44 0F B1 92 D0 00 00 00      lock cmpxchg dword ptr [rdx + 0xd0], r10d
00697ECE  75 53                           jne 0x140697f23
00697ED0  EB 42                           jmp 0x140697f14
00697ED2  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00697EDB  48 8B 8A E0 00 00 00            mov rcx, qword ptr [rdx + 0xe0]
00697EE2  33 D2                           xor edx, edx
00697EE4  44 0F B7 8F D6 00 00 00         movzx r9d, word ptr [rdi + 0xd6]
00697EEC  41 3B D1                        cmp edx, r9d
00697EEF  73 32                           jae 0x140697f23
00697EF1  41 0F B6 80 D0 00 00 00         movzx eax, byte ptr [r8 + 0xd0]
00697EF9  66 3B 41 08                     cmp ax, word ptr [rcx + 8]
00697EFD  74 09                           je 0x140697f08
00697EFF  41 03 D2                        add edx, r10d
00697F02  48 83 C1 10                     add rcx, 0x10
00697F06  EB E4                           jmp 0x140697eec
00697F08  49 8B 80 C8 00 00 00            mov rax, qword ptr [r8 + 0xc8]
00697F0F  48 85 01                        test qword ptr [rcx], rax
00697F12  74 0F                           je 0x140697f23
00697F14  48 8D 55 F8                     lea rdx, [rbp - 8]
00697F18  48 8B CF                        mov rcx, rdi
00697F1B  E8 60 01 E6 FF                  call 0x1404f8080
00697F20  44 8B E0                        mov r12d, eax
00697F23  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00697F29  41 BE 00 00 00 80               mov r14d, 0x80000000
00697F2F  A8 02                           test al, 2
00697F31  0F 84 16 01 00 00               je 0x14069804d
00697F37  83 C8 FF                        or eax, 0xffffffff
00697F3A  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
00697F3E  FF C8                           dec eax
00697F40  8B F0                           mov esi, eax
00697F42  F7 D6                           not esi
00697F44  41 23 F6                        and esi, r14d
00697F47  A9 FF FF FF 3F                  test eax, 0x3fffffff
00697F4C  75 1F                           jne 0x140697f6d
00697F4E  0B 73 04                        or esi, dword ptr [rbx + 4]
00697F51  87 33                           xchg dword ptr [rbx], esi
00697F53  89 75 48                        mov dword ptr [rbp + 0x48], esi
00697F56  0F BA E6 1E                     bt esi, 0x1e
00697F5A  0F 83 ED 00 00 00               jae 0x14069804d
00697F60  48 8B CB                        mov rcx, rbx
00697F63  E8 B8 FC B7 FF                  call 0x140217c20
00697F68  E9 E0 00 00 00                  jmp 0x14069804d
00697F6D  8B 03                           mov eax, dword ptr [rbx]
00697F6F  45 33 FF                        xor r15d, r15d
00697F72  41 23 C6                        and eax, r14d
00697F75  45 33 ED                        xor r13d, r13d
00697F78  3B C6                           cmp eax, esi
00697F7A  0F 84 C8 00 00 00               je 0x140698048
00697F80  EB 06                           jmp 0x140697f88
00697F82  41 BA 01 00 00 00               mov r10d, 1
00697F88  45 03 FA                        add r15d, r10d
00697F8B  44 85 3D 1A D3 92 00            test dword ptr [rip + 0x92d31a], r15d
00697F92  0F 85 A1 00 00 00               jne 0x140698039
00697F98  8B 05 1A EB 92 00               mov eax, dword ptr [rip + 0x92eb1a]
00697F9E  A8 40                           test al, 0x40
00697FA0  0F 84 93 00 00 00               je 0x140698039
00697FA6  E8 E5 74 C7 FF                  call 0x14030f490
00697FAB  84 C0                           test al, al
00697FAD  0F 84 86 00 00 00               je 0x140698039
00697FB3  41 FF C5                        inc r13d
00697FB6  E8 71 42 E6 FF                  call 0x1404fc22c
00697FBB  84 C0                           test al, al
00697FBD  74 70                           je 0x14069802f
00697FBF  F7 05 6F EB 92 00 00 00 02 00   test dword ptr [rip + 0x92eb6f], 0x20000
00697FC9  74 64                           je 0x14069802f
00697FCB  41 F6 C5 07                     test r13b, 7
00697FCF  75 5E                           jne 0x14069802f
00697FD1  8B 0B                           mov ecx, dword ptr [rbx]
00697FD3  8B C1                           mov eax, ecx
00697FD5  41 23 C6                        and eax, r14d
00697FD8  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
00697FDB  3B C6                           cmp eax, esi
00697FDD  74 5C                           je 0x14069803b
00697FDF  8B D1                           mov edx, ecx
00697FE1  44 8B C1                        mov r8d, ecx
00697FE4  0F BA E9 1E                     bts ecx, 0x1e
00697FE8  8B C2                           mov eax, edx
00697FEA  44 8B F1                        mov r14d, ecx
00697FED  F0 44 0F B1 33                  lock cmpxchg dword ptr [rbx], r14d
00697FF2  8B C8                           mov ecx, eax
00697FF4  41 3B C0                        cmp eax, r8d
00697FF7  75 1D                           jne 0x140698016
00697FF9  44 89 75 48                     mov dword ptr [rbp + 0x48], r14d
00697FFD  41 B8 04 00 00 00               mov r8d, 4
00698003  48 8D 55 48                     lea rdx, [rbp + 0x48]
00698007  48 8B CB                        mov rcx, rbx
0069800A  E8 2D 3A E6 FF                  call 0x1404fba3c
0069800F  8B 0B                           mov ecx, dword ptr [rbx]
00698011  41 3B CE                        cmp ecx, r14d
00698014  74 E7                           je 0x140697ffd
00698016  8B C1                           mov eax, ecx
00698018  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
0069801B  41 BE 00 00 00 80               mov r14d, 0x80000000
00698021  8B D1                           mov edx, ecx
00698023  41 23 C6                        and eax, r14d
00698026  44 8B C1                        mov r8d, ecx
00698029  3B C6                           cmp eax, esi
0069802B  75 B7                           jne 0x140697fe4
0069802D  EB 0C                           jmp 0x14069803b
0069802F  41 8B CF                        mov ecx, r15d
00698032  E8 29 74 C7 FF                  call 0x14030f460
00698037  EB 02                           jmp 0x14069803b
00698039  F3 90                           pause
0069803B  8B 03                           mov eax, dword ptr [rbx]
0069803D  41 23 C6                        and eax, r14d
00698040  3B C6                           cmp eax, esi
00698042  0F 85 3A FF FF FF               jne 0x140697f82
00698048  4C 8B 6D 50                     mov r13, qword ptr [rbp + 0x50]
0069804C  90                              nop
0069804D  45 85 E4                        test r12d, r12d
00698050  74 0C                           je 0x14069805e
00698052  48 8D 55 F8                     lea rdx, [rbp - 8]
00698056  48 8B CF                        mov rcx, rdi
00698059  E8 12 62 E4 FF                  call 0x1404de270
0069805E  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00698064  A8 02                           test al, 2
00698066  0F 84 FE 00 00 00               je 0x14069816a
0069806C  83 C8 FF                        or eax, 0xffffffff
0069806F  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
00698073  FF C8                           dec eax
00698075  8B F8                           mov edi, eax
00698077  F7 D7                           not edi
00698079  41 23 FE                        and edi, r14d
0069807C  A9 FF FF FF 3F                  test eax, 0x3fffffff
00698081  75 1F                           jne 0x1406980a2
00698083  0B 7B 04                        or edi, dword ptr [rbx + 4]
00698086  87 3B                           xchg dword ptr [rbx], edi
00698088  89 7D F0                        mov dword ptr [rbp - 0x10], edi
0069808B  0F BA E7 1E                     bt edi, 0x1e
0069808F  0F 83 D5 00 00 00               jae 0x14069816a
00698095  48 8B CB                        mov rcx, rbx
00698098  E8 83 FB B7 FF                  call 0x140217c20
0069809D  E9 C8 00 00 00                  jmp 0x14069816a
006980A2  33 F6                           xor esi, esi
006980A4  45 33 FF                        xor r15d, r15d
006980A7  E9 B0 00 00 00                  jmp 0x14069815c
006980AC  FF C6                           inc esi
006980AE  85 35 F8 D1 92 00               test dword ptr [rip + 0x92d1f8], esi
006980B4  0F 85 A0 00 00 00               jne 0x14069815a
006980BA  8B 05 F8 E9 92 00               mov eax, dword ptr [rip + 0x92e9f8]
006980C0  A8 40                           test al, 0x40
006980C2  0F 84 92 00 00 00               je 0x14069815a
006980C8  E8 C3 73 C7 FF                  call 0x14030f490
006980CD  84 C0                           test al, al
006980CF  0F 84 85 00 00 00               je 0x14069815a
006980D5  41 FF C7                        inc r15d
006980D8  E8 4F 41 E6 FF                  call 0x1404fc22c
006980DD  84 C0                           test al, al
006980DF  74 70                           je 0x140698151
006980E1  F7 05 4D EA 92 00 00 00 02 00   test dword ptr [rip + 0x92ea4d], 0x20000
006980EB  74 64                           je 0x140698151
006980ED  41 F6 C7 07                     test r15b, 7
006980F1  75 5E                           jne 0x140698151
006980F3  8B 0B                           mov ecx, dword ptr [rbx]
006980F5  8B C1                           mov eax, ecx
006980F7  41 23 C6                        and eax, r14d
006980FA  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
006980FD  3B C7                           cmp eax, edi
006980FF  74 5B                           je 0x14069815c
00698101  8B D1                           mov edx, ecx
00698103  44 8B C1                        mov r8d, ecx
00698106  0F BA E9 1E                     bts ecx, 0x1e
0069810A  8B C2                           mov eax, edx
0069810C  44 8B F1                        mov r14d, ecx
0069810F  F0 44 0F B1 33                  lock cmpxchg dword ptr [rbx], r14d
00698114  8B C8                           mov ecx, eax
00698116  41 3B C0                        cmp eax, r8d
00698119  75 1D                           jne 0x140698138
0069811B  44 89 75 F0                     mov dword ptr [rbp - 0x10], r14d
0069811F  41 B8 04 00 00 00               mov r8d, 4
00698125  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00698129  48 8B CB                        mov rcx, rbx
0069812C  E8 0B 39 E6 FF                  call 0x1404fba3c
00698131  8B 0B                           mov ecx, dword ptr [rbx]
00698133  41 3B CE                        cmp ecx, r14d
00698136  74 E7                           je 0x14069811f
00698138  8B C1                           mov eax, ecx
0069813A  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
0069813D  41 BE 00 00 00 80               mov r14d, 0x80000000
00698143  8B D1                           mov edx, ecx
00698145  41 23 C6                        and eax, r14d
00698148  44 8B C1                        mov r8d, ecx
0069814B  3B C7                           cmp eax, edi
0069814D  75 B7                           jne 0x140698106
0069814F  EB 0B                           jmp 0x14069815c
00698151  8B CE                           mov ecx, esi
00698153  E8 08 73 C7 FF                  call 0x14030f460
00698158  EB 02                           jmp 0x14069815c
0069815A  F3 90                           pause
0069815C  8B 03                           mov eax, dword ptr [rbx]
0069815E  41 23 C6                        and eax, r14d
00698161  3B C7                           cmp eax, edi
00698163  0F 85 43 FF FF FF               jne 0x1406980ac
00698169  90                              nop
0069816A  F0 41 FF 4D 00                  lock dec dword ptr [r13]
0069816F  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00698174  48 83 C4 30                     add rsp, 0x30
00698178  41 5F                           pop r15
0069817A  41 5E                           pop r14
0069817C  41 5D                           pop r13
0069817E  41 5C                           pop r12
00698180  5F                              pop rdi
00698181  5E                              pop rsi
00698182  5D                              pop rbp
00698183  C3                              ret
00698184  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDpcGangTarget(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    if ((*(unsigned __int8 *)(a2 + 212)) != 0) goto loc_00697EBA;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138))) != (*(unsigned int *)(a2 + 192))) goto loc_00697F23;
loc_00697EBA:
    if ((*(unsigned int *)(a2 + 188)) != ((unsigned int)(v_r12 + 1))) goto loc_00697ED2;
    result = 0;
    if (condition_is_not_equal) goto loc_00697F23;
    goto loc_00697F14;
loc_00697ED2:
    a2 = 0;
loc_00697EEC:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a2 + 214)))) goto loc_00697F23;
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208))) == (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 224) + 8))) goto loc_00697F08;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    a1 = (*(unsigned __int64 *)(a2 + 224)) + (16);
    goto loc_00697EEC;
loc_00697F08:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 200);
    if (((*(unsigned __int64 *)(a1)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 200))) != 0) {
        a2 = v_stack_m40;
        a1 = a2;
        result = MiGetGangAssignment(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int16 *)(a2 + 214));
        v_r12 = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 184)))) & (2)) == 0) goto loc_0069804D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 184))) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rsi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_00697F6D;
    v_rsi = (unsigned int)((v_rsi) | (*(unsigned int *)(a4 + 4)));
    v_stack_p10 = (unsigned int)(v_rsi);
    if (condition_is_above_or_equal) goto loc_0069804D;
    result = KeWakeAddressAll(a4, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int16 *)(a2 + 214));
    goto loc_0069804D;
loc_00697F6D:
    v_r15 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_r13 = 0;
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi))) goto loc_00698048;
    goto loc_00697F88;
loc_00697F82:
loc_00697F88:
    v_r15 = (unsigned int)((v_r15) + (1));
    if (((*(unsigned int *)(v_rip + 9622298)) & ((unsigned int)(v_r15))) != 0) goto loc_00698039;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9628442)))) & (64)) == 0) goto loc_00698039;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int16 *)(a2 + 214));
    if ((unsigned __int8)(result) == 0) goto loc_00698039;
    v_r13 = (unsigned int)((v_r13) + 1);
    result = KeCanUseHaltOnAddress(a4, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int16 *)(a2 + 214));
    if ((unsigned __int8)(result) == 0) goto loc_0069802F;
    if (((*(unsigned int *)(v_rip + 9628527)) & (0x20000ULL)) == 0) goto loc_0069802F;
    if ((((unsigned __int8)(v_r13)) & (7)) != 0) goto loc_0069802F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi))) goto loc_0069803B;
loc_00697FE4:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00698016;
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))));
loc_00697FFD:
    result = KiHaltOnAddress(a4, v_stack_p10, 4, *(unsigned __int16 *)(a2 + 214));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00697FFD;
loc_00698016:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rsi))) goto loc_00697FE4;
    goto loc_0069803B;
loc_0069802F:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    goto loc_0069803B;
loc_00698039:
loc_0069803B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rsi))) goto loc_00697F82;
loc_00698048:
loc_0069804D:
    if ((unsigned int)(v_r12) != 0) {
        a2 = v_stack_m40;
        a1 = a2;
        result = MiDoGangAssignment(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 184)))) & (2)) == 0) goto loc_0069816A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 184))) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_006980A2;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a4 + 4)));
    v_stack_m48 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_0069816A;
    result = KeWakeAddressAll(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    goto loc_0069816A;
loc_006980A2:
    v_rsi = 0;
    v_r15 = 0;
    goto loc_0069815C;
loc_006980AC:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 9622008)) & ((unsigned int)(v_rsi))) != 0) goto loc_0069815A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9628152)))) & (64)) == 0) goto loc_0069815A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    if ((unsigned __int8)(result) == 0) goto loc_0069815A;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    if ((unsigned __int8)(result) == 0) goto loc_00698151;
    if (((*(unsigned int *)(v_rip + 9628237)) & (0x20000ULL)) == 0) goto loc_00698151;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_00698151;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_0069815C;
loc_00698106:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00698138;
    v_stack_m48 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))));
loc_0069811F:
    result = KiHaltOnAddress(a4, v_stack_m48, 4, *(unsigned __int16 *)(a2 + 214));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_0069811F;
loc_00698138:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00698106;
    goto loc_0069815C;
loc_00698151:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), *(unsigned __int16 *)(a2 + 214));
    goto loc_0069815C;
loc_0069815A:
loc_0069815C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_006980AC;
loc_0069816A:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDpcGangTarget(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    if ((*(uint8_t *)(arg2 + 0xD4)) != 0) goto loc_00697EBA;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A))) != (*(uint32_t *)(arg2 + 0xC0))) goto loc_00697F23;
loc_00697EBA:
    if ((*(uint32_t *)(arg2 + 0xBC)) != ((uint32_t)(local_r12 + 1))) goto loc_00697ED2;
    result = 0;
    if (condition_is_not_equal) goto loc_00697F23;
    goto loc_00697F14;
loc_00697ED2:
    Arg2 = 0;
loc_00697EEC:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg2 + 0xD6)))) goto loc_00697F23;
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0))) == (*(uint16_t *)(*(uint64_t *)(arg2 + 0xE0) + 0x8))) goto loc_00697F08;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    Arg1 = (*(uint64_t *)(arg2 + 0xE0)) + (16);
    goto loc_00697EEC;
loc_00697F08:
    result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC8);
    if (((*(uint64_t *)(Arg1)) & (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC8))) != 0) {
        Arg2 = v_stack_m40;
        Arg1 = Arg2;
        result = MiGetGangAssignment(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint16_t *)(arg2 + 0xD6));
        local_r12 = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB8)))) & (2)) == 0) goto loc_0069804D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xB8))) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rsi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_00697F6D;
    local_rsi = (uint32_t)((local_rsi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_p10 = (uint32_t)(local_rsi);
    if (condition_is_above_or_equal) goto loc_0069804D;
    result = KeWakeAddressAll(Arg4, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint16_t *)(arg2 + 0xD6));
    goto loc_0069804D;
loc_00697F6D:
    local_r15 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    local_r13 = 0;
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi))) goto loc_00698048;
    goto loc_00697F88;
loc_00697F82:
loc_00697F88:
    local_r15 = (uint32_t)((local_r15) + (1));
    if (((*(uint32_t *)(v_rip + 0x92D31A)) & ((uint32_t)(local_r15))) != 0) goto loc_00698039;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92EB1A)))) & (64)) == 0) goto loc_00698039;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint16_t *)(arg2 + 0xD6));
    if ((uint8_t)(result) == 0) goto loc_00698039;
    local_r13 = (uint32_t)((local_r13) + 1);
    result = KeCanUseHaltOnAddress(Arg4, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint16_t *)(arg2 + 0xD6));
    if ((uint8_t)(result) == 0) goto loc_0069802F;
    if (((*(uint32_t *)(v_rip + 0x92EB6F)) & (0x20000ULL)) == 0) goto loc_0069802F;
    if ((((uint8_t)(local_r13)) & (7)) != 0) goto loc_0069802F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi))) goto loc_0069803B;
loc_00697FE4:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00698016;
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))));
loc_00697FFD:
    result = KiHaltOnAddress(Arg4, v_stack_p10, 4, *(uint16_t *)(arg2 + 0xD6));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00697FFD;
loc_00698016:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rsi))) goto loc_00697FE4;
    goto loc_0069803B;
loc_0069802F:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    goto loc_0069803B;
loc_00698039:
loc_0069803B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rsi))) goto loc_00697F82;
loc_00698048:
loc_0069804D:
    if ((uint32_t)(local_r12) != 0) {
        Arg2 = v_stack_m40;
        Arg1 = Arg2;
        result = MiDoGangAssignment(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB8)))) & (2)) == 0) goto loc_0069816A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xB8))) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_006980A2;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_m48 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_0069816A;
    result = KeWakeAddressAll(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    goto loc_0069816A;
loc_006980A2:
    local_rsi = 0;
    local_r15 = 0;
    goto loc_0069815C;
loc_006980AC:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0x92D1F8)) & ((uint32_t)(local_rsi))) != 0) goto loc_0069815A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92E9F8)))) & (64)) == 0) goto loc_0069815A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    if ((uint8_t)(result) == 0) goto loc_0069815A;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    if ((uint8_t)(result) == 0) goto loc_00698151;
    if (((*(uint32_t *)(v_rip + 0x92EA4D)) & (0x20000ULL)) == 0) goto loc_00698151;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_00698151;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_0069815C;
loc_00698106:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00698138;
    v_stack_m48 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))));
loc_0069811F:
    result = KiHaltOnAddress(Arg4, v_stack_m48, 4, *(uint16_t *)(arg2 + 0xD6));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_0069811F;
loc_00698138:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00698106;
    goto loc_0069815C;
loc_00698151:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), *(uint16_t *)(arg2 + 0xD6));
    goto loc_0069815C;
loc_0069815A:
loc_0069815C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_006980AC;
loc_0069816A:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xB8` | `32` | `R` |
| `Arg2` | `+ 0xBC` | `32` | `R` |
| `Arg2` | `+ 0xC0` | `32` | `R` |
| `Arg2` | `+ 0xD0` | `32` | `R` |
| `Arg2` | `+ 0xD4` | `8` | `R` |
| `Arg2` | `+ 0xD6` | `16` | `R` |
| `Arg2` | `+ 0xE0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00697E60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
