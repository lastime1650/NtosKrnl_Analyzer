# HalpBuddyAllocatorAllocateLogicalAddress

- RVA: `0x00307EE0`–`0x0030828A` (길이 `938` bytes)
- VA: `0x0000000140307EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007399C`
- 디코드: `253`개 명령, `938/938` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00307F3C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00308013` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x0030802A` → [HalpBuddyAllocatorBltFindAndPop](../46/HalpBuddyAllocatorBltFindAndPop_function_0046746C.md) (function, `0x0046746C`)
- `0x0030807A` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x003080B9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003080E0` → [HalpBuddyAllocatorSplitNode](../3E/HalpBuddyAllocatorSplitNode_function_003E0BD0.md) (function, `0x003E0BD0`)
- `0x0030815B` → [HalpBuddyAllocatorBltAdd](../47/HalpBuddyAllocatorBltAdd_function_0047A968.md) (function, `0x0047A968`)
- `0x0030818D` → [HalpBuddyAllocatorDeleteSubtree](../47/HalpBuddyAllocatorDeleteSubtree_function_0047A890.md) (function, `0x0047A890`)
- `0x00308197` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x00308241` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x00308249` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0030825C` → [HalpBuddyAllocatorBltFindAndPop](../46/HalpBuddyAllocatorBltFindAndPop_function_0046746C.md) (function, `0x0046746C`)
- `0x00308269` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0030827A` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)

### Direct callers
- [IommuMapLogicalRangeEx](IommuMapLogicalRangeEx_function_003074B0.md) at `0x00307585`
- [IommuMapIdentityRangeEx](IommuMapIdentityRangeEx_function_00307C10.md) at `0x00307CFF`
- [HalpIommuDomainGetLogicalAddressRange](HalpIommuDomainGetLogicalAddressRange_function_00307E48.md) at `0x00307E9F`

### Static image references
- `0x00307EF7` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00307EE0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00307EE5  55                              push rbp
00307EE6  56                              push rsi
00307EE7  57                              push rdi
00307EE8  41 54                           push r12
00307EEA  41 55                           push r13
00307EEC  41 56                           push r14
00307EEE  41 57                           push r15
00307EF0  48 81 EC F0 01 00 00            sub rsp, 0x1f0
00307EF7  48 8B 05 42 28 B0 00            mov rax, qword ptr [rip + 0xb02842]
00307EFE  48 33 C4                        xor rax, rsp
00307F01  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00307F09  48 8B B4 24 58 02 00 00         mov rsi, qword ptr [rsp + 0x258]
00307F11  4D 8B F8                        mov r15, r8
00307F14  4C 8B B4 24 50 02 00 00         mov r14, qword ptr [rsp + 0x250]
00307F1C  48 8B DA                        mov rbx, rdx
00307F1F  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00307F24  48 8B E9                        mov rbp, rcx
00307F27  33 D2                           xor edx, edx
00307F29  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00307F2E  41 B8 A0 01 00 00               mov r8d, 0x1a0
00307F34  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00307F39  49 8B F9                        mov rdi, r9
00307F3C  E8 FF EC 3B 00                  call 0x1406c6c40
00307F41  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00307F45  45 33 C9                        xor r9d, r9d
00307F48  44 89 4C 24 24                  mov dword ptr [rsp + 0x24], r9d
00307F4D  41 8B D1                        mov edx, r9d
00307F50  44 88 4D 78                     mov byte ptr [rbp + 0x78], r9b
00307F54  48 85 DB                        test rbx, rbx
00307F57  0F 85 51 02 00 00               jne 0x1403081ae
00307F5D  4C 3B 7D 20                     cmp r15, qword ptr [rbp + 0x20]
00307F61  0F 87 BD 02 00 00               ja 0x140308224
00307F67  48 8B 75 18                     mov rsi, qword ptr [rbp + 0x18]
00307F6B  49 3B F7                        cmp rsi, r15
00307F6E  0F 82 32 02 00 00               jb 0x1403081a6
00307F74  48 85 FF                        test rdi, rdi
00307F77  74 03                           je 0x140307f7c
00307F79  48 8B 17                        mov rdx, qword ptr [rdi]
00307F7C  4D 85 F6                        test r14, r14
00307F7F  74 03                           je 0x140307f84
00307F81  49 8B 0E                        mov rcx, qword ptr [r14]
00307F84  48 8D 46 FF                     lea rax, [rsi - 1]
00307F88  48 85 C6                        test rsi, rax
00307F8B  0F 85 A9 01 00 00               jne 0x14030813a
00307F91  48 85 F6                        test rsi, rsi
00307F94  0F 84 A0 01 00 00               je 0x14030813a
00307F9A  4C 8D 62 FF                     lea r12, [rdx - 1]
00307F9E  48 F7 D0                        not rax
00307FA1  4C 03 E6                        add r12, rsi
00307FA4  4C 23 E0                        and r12, rax
00307FA7  4C 3B E2                        cmp r12, rdx
00307FAA  0F 82 8A 01 00 00               jb 0x14030813a
00307FB0  49 83 CE FF                     or r14, 0xffffffffffffffff
00307FB4  49 3B CE                        cmp rcx, r14
00307FB7  74 13                           je 0x140307fcc
00307FB9  4C 8D 71 01                     lea r14, [rcx + 1]
00307FBD  4C 23 F0                        and r14, rax
00307FC0  49 FF CE                        dec r14
00307FC3  4C 3B F1                        cmp r14, rcx
00307FC6  0F 87 6E 01 00 00               ja 0x14030813a
00307FCC  4D 3B E6                        cmp r12, r14
00307FCF  0F 87 65 01 00 00               ja 0x14030813a
00307FD5  49 8B C6                        mov rax, r14
00307FD8  49 2B C4                        sub rax, r12
00307FDB  48 FF C0                        inc rax
00307FDE  48 3B F0                        cmp rsi, rax
00307FE1  0F 87 47 02 00 00               ja 0x14030822e
00307FE7  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00307FEB  41 8B F9                        mov edi, r9d
00307FEE  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
00307FF2  48 8D 4A FF                     lea rcx, [rdx - 1]
00307FF6  48 03 48 38                     add rcx, qword ptr [rax + 0x38]
00307FFA  49 3B CC                        cmp rcx, r12
00307FFD  0F 82 41 01 00 00               jb 0x140308144
00308003  49 3B D6                        cmp rdx, r14
00308006  0F 87 38 01 00 00               ja 0x140308144
0030800C  4C 8D 6D 70                     lea r13, [rbp + 0x70]
00308010  49 8B CD                        mov rcx, r13
00308013  E8 C8 5C F4 FF                  call 0x14024dce0
00308018  4D 8B CE                        mov r9, r14
0030801B  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0030801F  4D 8B C4                        mov r8, r12
00308022  48 8B D5                        mov rdx, rbp
00308025  48 8B CE                        mov rcx, rsi
00308028  8A D8                           mov bl, al
0030802A  E8 3D F4 15 00                  call 0x14046746c
0030802F  4C 8B F8                        mov r15, rax
00308032  48 85 C0                        test rax, rax
00308035  0F 84 01 02 00 00               je 0x14030823c
0030803B  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00308040  8B D7                           mov edx, edi
00308042  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
00308046  48 3B CE                        cmp rcx, rsi
00308049  0F 85 8B 00 00 00               jne 0x1403080da
0030804F  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
00308053  49 3B C4                        cmp rax, r12
00308056  0F 82 29 01 00 00               jb 0x140308185
0030805C  48 FF C8                        dec rax
0030805F  48 03 C1                        add rax, rcx
00308062  49 3B C6                        cmp rax, r14
00308065  0F 87 1A 01 00 00               ja 0x140308185
0030806B  85 D2                           test edx, edx
0030806D  0F 85 DB 00 00 00               jne 0x14030814e
00308073  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
00308077  49 8B CD                        mov rcx, r13
0030807A  E8 71 8E FE FF                  call 0x1402f0ef0
0030807F  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00308084  49 83 67 28 00                  and qword ptr [r15 + 0x28], 0
00308089  49 89 47 40                     mov qword ptr [r15 + 0x40], rax
0030808D  41 C6 47 48 01                  mov byte ptr [r15 + 0x48], 1
00308092  F0 48 01 45 38                  lock add qword ptr [rbp + 0x38], rax
00308097  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
0030809B  F0 48 01 45 40                  lock add qword ptr [rbp + 0x40], rax
003080A0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
003080A5  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
003080A9  48 89 01                        mov qword ptr [rcx], rax
003080AC  8B C7                           mov eax, edi
003080AE  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
003080B6  48 33 CC                        xor rcx, rsp
003080B9  E8 82 45 3A 00                  call 0x1406ac640
003080BE  48 8B 9C 24 38 02 00 00         mov rbx, qword ptr [rsp + 0x238]
003080C6  48 81 C4 F0 01 00 00            add rsp, 0x1f0
003080CD  41 5F                           pop r15
003080CF  41 5E                           pop r14
003080D1  41 5D                           pop r13
003080D3  41 5C                           pop r12
003080D5  5F                              pop rdi
003080D6  5E                              pop rsi
003080D7  5D                              pop rbp
003080D8  C3                              ret
003080D9  CC                              int3
003080DA  49 8B D7                        mov rdx, r15
003080DD  48 8B CD                        mov rcx, rbp
003080E0  E8 EB 8A 0D 00                  call 0x1403e0bd0
003080E5  8B F8                           mov edi, eax
003080E7  85 C0                           test eax, eax
003080E9  0F 88 96 00 00 00               js 0x140308185
003080EF  4D 8B 47 18                     mov r8, qword ptr [r15 + 0x18]
003080F3  48 8D 4E FF                     lea rcx, [rsi - 1]
003080F7  49 03 CC                        add rcx, r12
003080FA  49 8B 50 38                     mov rdx, qword ptr [r8 + 0x38]
003080FE  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00308102  48 FF CA                        dec rdx
00308105  48 03 D0                        add rdx, rax
00308108  48 3B D1                        cmp rdx, rcx
0030810B  73 63                           jae 0x140308170
0030810D  33 C0                           xor eax, eax
0030810F  4D 8B 7F 20                     mov r15, qword ptr [r15 + 0x20]
00308113  85 C0                           test eax, eax
00308115  0F 84 01 01 00 00               je 0x14030821c
0030811B  49 8B CF                        mov rcx, r15
0030811E  4D 8B F8                        mov r15, r8
00308121  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
00308125  83 FA 34                        cmp edx, 0x34
00308128  73 72                           jae 0x14030819c
0030812A  48 89 4C D4 40                  mov qword ptr [rsp + rdx*8 + 0x40], rcx
0030812F  FF C2                           inc edx
00308131  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00308135  E9 08 FF FF FF                  jmp 0x140308042
0030813A  BF 0D 00 00 C0                  mov edi, 0xc000000d
0030813F  E9 68 FF FF FF                  jmp 0x1403080ac
00308144  BF 30 00 00 C0                  mov edi, 0xc0000030
00308149  E9 5E FF FF FF                  jmp 0x1403080ac
0030814E  48 8D 5C 24 40                  lea rbx, [rsp + 0x40]
00308153  8B F2                           mov esi, edx
00308155  48 8B 0B                        mov rcx, qword ptr [rbx]
00308158  48 8B D5                        mov rdx, rbp
0030815B  E8 08 28 17 00                  call 0x14047a968
00308160  48 8D 5B 08                     lea rbx, [rbx + 8]
00308164  48 83 EE 01                     sub rsi, 1
00308168  0F 84 05 FF FF FF               je 0x140308073
0030816E  EB E5                           jmp 0x140308155
00308170  49 8B CE                        mov rcx, r14
00308173  48 2B CE                        sub rcx, rsi
00308176  48 FF C1                        inc rcx
00308179  48 3B C1                        cmp rax, rcx
0030817C  77 8F                           ja 0x14030810d
0030817E  B8 01 00 00 00                  mov eax, 1
00308183  EB 8A                           jmp 0x14030810f
00308185  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0030818A  48 8B CD                        mov rcx, rbp
0030818D  E8 FE 26 17 00                  call 0x14047a890
00308192  8A D3                           mov dl, bl
00308194  49 8B CD                        mov rcx, r13
00308197  E8 54 8D FE FF                  call 0x1402f0ef0
0030819C  BF 9A 00 00 C0                  mov edi, 0xc000009a
003081A1  E9 06 FF FF FF                  jmp 0x1403080ac
003081A6  48 03 F6                        add rsi, rsi
003081A9  E9 BD FD FF FF                  jmp 0x140307f6b
003081AE  4C 8B 03                        mov r8, qword ptr [rbx]
003081B1  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
003081B5  48 8B 4A 30                     mov rcx, qword ptr [rdx + 0x30]
003081B9  4C 3B C1                        cmp r8, rcx
003081BC  73 27                           jae 0x1403081e5
003081BE  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
003081C2  48 85 C0                        test rax, rax
003081C5  74 0B                           je 0x1403081d2
003081C7  4C 3B 40 30                     cmp r8, qword ptr [rax + 0x30]
003081CB  72 05                           jb 0x1403081d2
003081CD  48 8B D0                        mov rdx, rax
003081D0  EB E3                           jmp 0x1403081b5
003081D2  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
003081D6  48 85 D2                        test rdx, rdx
003081D9  75 DA                           jne 0x1403081b5
003081DB  BF F0 00 00 C0                  mov edi, 0xc00000f0
003081E0  E9 C7 FE FF FF                  jmp 0x1403080ac
003081E5  48 03 4A 38                     add rcx, qword ptr [rdx + 0x38]
003081E9  4C 3B C1                        cmp r8, rcx
003081EC  73 D0                           jae 0x1403081be
003081EE  4C 39 4A 18                     cmp qword ptr [rdx + 0x18], r9
003081F2  75 CA                           jne 0x1403081be
003081F4  4C 39 4A 20                     cmp qword ptr [rdx + 0x20], r9
003081F8  75 C4                           jne 0x1403081be
003081FA  44 38 4A 48                     cmp byte ptr [rdx + 0x48], r9b
003081FE  74 DB                           je 0x1403081db
00308200  48 8D 45 50                     lea rax, [rbp + 0x50]
00308204  48 39 42 28                     cmp qword ptr [rdx + 0x28], rax
00308208  75 D1                           jne 0x1403081db
0030820A  C6 42 49 01                     mov byte ptr [rdx + 0x49], 1
0030820E  41 8B F9                        mov edi, r9d
00308211  48 8B 03                        mov rax, qword ptr [rbx]
00308214  48 89 06                        mov qword ptr [rsi], rax
00308217  E9 90 FE FF FF                  jmp 0x1403080ac
0030821C  49 8B C8                        mov rcx, r8
0030821F  E9 FD FE FF FF                  jmp 0x140308121
00308224  BF F1 00 00 C0                  mov edi, 0xc00000f1
00308229  E9 7E FE FF FF                  jmp 0x1403080ac
0030822E  48 85 C0                        test rax, rax
00308231  0F 85 03 FF FF FF               jne 0x14030813a
00308237  E9 AB FD FF FF                  jmp 0x140307fe7
0030823C  8A D3                           mov dl, bl
0030823E  49 8B CD                        mov rcx, r13
00308241  E8 AA 8C FE FF                  call 0x1402f0ef0
00308246  49 8B CD                        mov rcx, r13
00308249  E8 42 04 F4 FF                  call 0x140248690
0030824E  4D 8B CE                        mov r9, r14
00308251  4D 8B C4                        mov r8, r12
00308254  48 8B D5                        mov rdx, rbp
00308257  48 8B CE                        mov rcx, rsi
0030825A  8A D8                           mov bl, al
0030825C  E8 0B F2 15 00                  call 0x14046746c
00308261  8A D3                           mov dl, bl
00308263  49 8B CD                        mov rcx, r13
00308266  4C 8B F8                        mov r15, rax
00308269  E8 82 8C FB FF                  call 0x1402c0ef0
0030826E  4D 85 FF                        test r15, r15
00308271  0F 84 25 FF FF FF               je 0x14030819c
00308277  49 8B CD                        mov rcx, r13
0030827A  E8 61 5A F4 FF                  call 0x14024dce0
0030827F  8A D8                           mov bl, al
00308281  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00308285  E9 B1 FD FF FF                  jmp 0x14030803b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBuddyAllocatorAllocateLogicalAddress(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m204;
    unsigned __int8 v_stack_m208;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 11544642)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = a3;
    a2 = 0;
    v_stack_m1F0 = a6;
    result = memset(v_stack_m1E8, a2, 416, a4);
    a4 = 0;
    v_stack_m204 = 0;
    *(unsigned __int8 *)(a1 + 120) = 0;
    if (0 != 0) goto loc_003081AE;
    if (a3 > (*(unsigned __int64 *)(a1 + 32))) goto loc_00308224;
loc_00307F6B:
    if ((*(unsigned __int64 *)(a1 + 24)) < a3) goto loc_003081A6;
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(a4);
    }
    if (a5 != 0) {
        a1 = *(unsigned __int64 *)(a5);
    }
    if (((*(unsigned __int64 *)(a1 + 24)) & (*(unsigned __int64 *)(a1 + 24) - 1)) != 0) goto loc_0030813A;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_0030813A;
    result = ~(*(unsigned __int64 *)(a1 + 24) - 1);
    v_r12 = (a2 - 1) + (*(unsigned __int64 *)(a1 + 24));
    v_r12 = (v_r12) & (result);
    if (v_r12 < a2) goto loc_0030813A;
    v_r14 = (a5) | (-1);
    if (a1 == v_r14) goto loc_00307FCC;
    v_r14 = (a1 + 1) & (result);
    v_r14 = (v_r14) - 1;
    if (v_r14 > a1) goto loc_0030813A;
loc_00307FCC:
    if (v_r12 > v_r14) goto loc_0030813A;
    result = (v_r14) - (v_r12);
    result = (result) + 1;
    if ((*(unsigned __int64 *)(a1 + 24)) > result) goto loc_0030822E;
loc_00307FE7:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 48) - 1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 56));
    if (a1 < v_r12) goto loc_00308144;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 48)) > v_r14) goto loc_00308144;
    result = ExAcquireSpinLockShared(a1 + 112, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 48), 416, a4);
    v_stack_m208 = (unsigned __int8)(result);
    result = HalpBuddyAllocatorBltFindAndPop(*(unsigned __int64 *)(a1 + 24), a1, v_r12, v_r14);
    if (result == 0) goto loc_0030823C;
loc_0030803B:
    v_stack_m200 = result;
loc_00308042:
    if ((*(unsigned __int64 *)(result + 56)) != (*(unsigned __int64 *)(a1 + 24))) goto loc_003080DA;
    if ((*(unsigned __int64 *)(result + 48)) < v_r12) goto loc_00308185;
    result = (*(unsigned __int64 *)(result + 48)) - 1;
    result = (result) + (*(unsigned __int64 *)(result + 56));
    if (result > v_r14) goto loc_00308185;
    if (0 != 0) goto loc_0030814E;
loc_00308073:
    result = ExReleaseSpinLockShared(a1 + 112, v_stack_m208, v_r12, v_r14);
    *(unsigned __int64 *)(result + 64) = v_stack_m1F8;
    *(unsigned __int8 *)(result + 72) = 1;
    *(unsigned __int64 *)(v_stack_m1F0) = *(unsigned __int64 *)(result + 48);
loc_003080AC:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m208, v_r12, v_r14);
    v_rsp = (v_rsp) + (496);
    return result;
loc_003080DA:
    result = HalpBuddyAllocatorSplitNode(a1, result, v_r12, v_r14);
    if (sign_flag) goto loc_00308185;
    a1 = (*(unsigned __int64 *)(a1 + 24) - 1) + (v_r12);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 56)) - 1;
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 48));
    if (a2 >= a1) goto loc_00308170;
loc_0030810D:
    result = 0;
loc_0030810F:
    if (0 == 0) goto loc_0030821C;
loc_00308121:
    if (((unsigned int)((unsigned int)(v_stack_p24))) >= 52) goto loc_0030819C;
    *(unsigned __int64 *)(v_rsp + (unsigned int)(v_stack_p24) * 8 + 64) = *(unsigned __int64 *)(result + 32);
    a2 = (unsigned int)(((unsigned int)(v_stack_p24)) + 1);
    v_stack_p24 = (unsigned int)(a2);
    goto loc_00308042;
loc_0030813A:
    goto loc_003080AC;
loc_00308144:
    goto loc_003080AC;
loc_0030814E:
loc_00308155:
    result = HalpBuddyAllocatorBltAdd(*(unsigned __int64 *)(v_stack_p40), a1, *(unsigned __int64 *)(result + 24), v_r14);
    v_rsi = ((unsigned int)((unsigned int)(a2))) - (1);
    if (condition_is_equal) goto loc_00308073;
    goto loc_00308155;
loc_00308170:
    a1 = (v_r14) - (v_rsi);
    a1 = (a1) + 1;
    if (result > a1) goto loc_0030810D;
    goto loc_0030810F;
loc_00308185:
    result = HalpBuddyAllocatorDeleteSubtree(a1, v_stack_p28, *(unsigned __int64 *)(result + 24), v_r14);
    result = ExReleaseSpinLockShared(a1 + 112, (unsigned __int8)(v_stack_p40 + 8), *(unsigned __int64 *)(result + 24), v_r14);
loc_0030819C:
    goto loc_003080AC;
loc_003081A6:
    v_rsi = (v_rsi) + (v_rsi);
    goto loc_00307F6B;
loc_003081AE:
loc_003081B5:
    if ((*(unsigned __int64 *)(v_stack_p40 + 8)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 48))) goto loc_003081E5;
loc_003081BE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) == 0) goto loc_003081D2;
    if ((*(unsigned __int64 *)(v_stack_p40 + 8)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 48))) goto loc_003081D2;
    goto loc_003081B5;
loc_003081D2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) != 0) goto loc_003081B5;
loc_003081DB:
    goto loc_003080AC;
loc_003081E5:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 48)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 56));
    if ((*(unsigned __int64 *)(v_stack_p40 + 8)) >= a1) goto loc_003081BE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 24)) != v_r14) goto loc_003081BE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 32)) != v_r14) goto loc_003081BE;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 72)) == ((unsigned __int8)(v_r14))) goto loc_003081DB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 40)) != (a1 + 80)) goto loc_003081DB;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 32) + 24) + 73) = 1;
    *(unsigned __int64 *)(v_rsi) = *(unsigned __int64 *)(v_stack_p40 + 8);
    goto loc_003080AC;
loc_0030821C:
    goto loc_00308121;
loc_00308224:
    goto loc_003080AC;
loc_0030822E:
    if (*(unsigned __int64 *)(v_stack_p40 + 8) != 0) goto loc_0030813A;
    goto loc_00307FE7;
loc_0030823C:
    result = ExReleaseSpinLockShared(a1 + 112, (unsigned __int8)(v_stack_p40 + 8), *(unsigned __int64 *)(v_stack_p40 + 8), v_r14);
    result = ExAcquireSpinLockExclusive(a1 + 112, (unsigned __int8)(v_stack_p40 + 8), *(unsigned __int64 *)(v_stack_p40 + 8), v_r14);
    result = HalpBuddyAllocatorBltFindAndPop(v_rsi, a1, v_r12, v_r14);
    result = ExReleaseSpinLockExclusive(a1 + 112, (unsigned __int8)((unsigned __int8)(result)), v_r12, v_r14);
    if (result == 0) goto loc_0030819C;
    result = ExAcquireSpinLockShared(a1 + 112, (unsigned __int8)((unsigned __int8)(result)), v_r12, v_r14);
    v_stack_p20 = (unsigned __int8)(result);
    goto loc_0030803B;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBuddyAllocatorAllocateLogicalAddress(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m204;
    uint8_t v_stack_m208;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0xB02842)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1F8 = Arg3;
    Arg2 = 0;
    v_stack_m1F0 = Arg6;
    result = memset(v_stack_m1E8, Arg2, 416, Arg4);
    Arg4 = 0;
    v_stack_m204 = 0;
    *(uint8_t *)(arg1 + 0x78) = 0;
    if (0 != 0) goto loc_003081AE;
    if (Arg3 > (*(uint64_t *)(arg1 + 0x20))) goto loc_00308224;
loc_00307F6B:
    if ((*(uint64_t *)(arg1 + 0x18)) < Arg3) goto loc_003081A6;
    if (0 != 0) {
        Arg2 = *(uint64_t *)(Arg4);
    }
    if (Arg5 != 0) {
        Arg1 = *(uint64_t *)(Arg5);
    }
    if (((*(uint64_t *)(arg1 + 0x18)) & (*(uint64_t *)(arg1 + 0x18) - 1)) != 0) goto loc_0030813A;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_0030813A;
    result = ~(*(uint64_t *)(arg1 + 0x18) - 1);
    local_r12 = (Arg2 - 1) + (*(uint64_t *)(arg1 + 0x18));
    local_r12 = (local_r12) & (result);
    if (local_r12 < Arg2) goto loc_0030813A;
    local_r14 = (Arg5) | (-1);
    if (Arg1 == local_r14) goto loc_00307FCC;
    local_r14 = (Arg1 + 1) & (result);
    local_r14 = (local_r14) - 1;
    if (local_r14 > Arg1) goto loc_0030813A;
loc_00307FCC:
    if (local_r12 > local_r14) goto loc_0030813A;
    result = (local_r14) - (local_r12);
    result = (result) + 1;
    if ((*(uint64_t *)(arg1 + 0x18)) > result) goto loc_0030822E;
loc_00307FE7:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x30) - 1) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x38));
    if (Arg1 < local_r12) goto loc_00308144;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x30)) > local_r14) goto loc_00308144;
    result = ExAcquireSpinLockShared(Arg1 + 112, *(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x30), 416, Arg4);
    v_stack_m208 = (uint8_t)(result);
    result = HalpBuddyAllocatorBltFindAndPop(*(uint64_t *)(arg1 + 0x18), Arg1, local_r12, local_r14);
    if (result == 0) goto loc_0030823C;
loc_0030803B:
    v_stack_m200 = result;
loc_00308042:
    if ((*(uint64_t *)(result + 0x38)) != (*(uint64_t *)(arg1 + 0x18))) goto loc_003080DA;
    if ((*(uint64_t *)(result + 0x30)) < local_r12) goto loc_00308185;
    result = (*(uint64_t *)(result + 0x30)) - 1;
    result = (result) + (*(uint64_t *)(result + 0x38));
    if (result > local_r14) goto loc_00308185;
    if (0 != 0) goto loc_0030814E;
loc_00308073:
    result = ExReleaseSpinLockShared(Arg1 + 112, v_stack_m208, local_r12, local_r14);
    *(uint64_t *)(result + 0x40) = v_stack_m1F8;
    *(uint8_t *)(result + 0x48) = 1;
    *(uint64_t *)(v_stack_m1F0) = *(uint64_t *)(result + 0x30);
loc_003080AC:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m208, local_r12, local_r14);
    local_rsp = (local_rsp) + (496);
    return result;
loc_003080DA:
    result = HalpBuddyAllocatorSplitNode(Arg1, result, local_r12, local_r14);
    if (sign_flag) goto loc_00308185;
    Arg1 = (*(uint64_t *)(arg1 + 0x18) - 1) + (local_r12);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x38)) - 1;
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x30));
    if (Arg2 >= Arg1) goto loc_00308170;
loc_0030810D:
    result = 0;
loc_0030810F:
    if (0 == 0) goto loc_0030821C;
loc_00308121:
    if (((uint32_t)((uint32_t)(v_stack_p24))) >= 52) goto loc_0030819C;
    *(uint64_t *)(local_rsp + (uint32_t)(v_stack_p24) * 8 + 0x40) = *(uint64_t *)(result + 0x20);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p24)) + 1);
    v_stack_p24 = (uint32_t)(Arg2);
    goto loc_00308042;
loc_0030813A:
    goto loc_003080AC;
loc_00308144:
    goto loc_003080AC;
loc_0030814E:
loc_00308155:
    result = HalpBuddyAllocatorBltAdd(*(uint64_t *)(v_stack_p40), Arg1, *(uint64_t *)(result + 0x18), local_r14);
    local_rsi = ((uint32_t)((uint32_t)(Arg2))) - (1);
    if (condition_is_equal) goto loc_00308073;
    goto loc_00308155;
loc_00308170:
    Arg1 = (local_r14) - (local_rsi);
    Arg1 = (Arg1) + 1;
    if (result > Arg1) goto loc_0030810D;
    goto loc_0030810F;
loc_00308185:
    result = HalpBuddyAllocatorDeleteSubtree(Arg1, v_stack_p28, *(uint64_t *)(result + 0x18), local_r14);
    result = ExReleaseSpinLockShared(Arg1 + 112, (uint8_t)(v_stack_p40 + 8), *(uint64_t *)(result + 0x18), local_r14);
loc_0030819C:
    goto loc_003080AC;
loc_003081A6:
    local_rsi = (local_rsi) + (local_rsi);
    goto loc_00307F6B;
loc_003081AE:
loc_003081B5:
    if ((*(uint64_t *)(v_stack_p40 + 0x8)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x30))) goto loc_003081E5;
loc_003081BE:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) == 0) goto loc_003081D2;
    if ((*(uint64_t *)(v_stack_p40 + 0x8)) < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x30))) goto loc_003081D2;
    goto loc_003081B5;
loc_003081D2:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) != 0) goto loc_003081B5;
loc_003081DB:
    goto loc_003080AC;
loc_003081E5:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x30)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x38));
    if ((*(uint64_t *)(v_stack_p40 + 0x8)) >= Arg1) goto loc_003081BE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x18)) != local_r14) goto loc_003081BE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x20)) != local_r14) goto loc_003081BE;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x48)) == ((uint8_t)(local_r14))) goto loc_003081DB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x28)) != (Arg1 + 80)) goto loc_003081DB;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x20) + 0x18) + 0x49) = 1;
    *(uint64_t *)(local_rsi) = *(uint64_t *)(v_stack_p40 + 0x8);
    goto loc_003080AC;
loc_0030821C:
    goto loc_00308121;
loc_00308224:
    goto loc_003080AC;
loc_0030822E:
    if (*(uint64_t *)(v_stack_p40 + 0x8) != 0) goto loc_0030813A;
    goto loc_00307FE7;
loc_0030823C:
    result = ExReleaseSpinLockShared(Arg1 + 112, (uint8_t)(v_stack_p40 + 8), *(uint64_t *)(v_stack_p40 + 0x8), local_r14);
    result = ExAcquireSpinLockExclusive(Arg1 + 112, (uint8_t)(v_stack_p40 + 8), *(uint64_t *)(v_stack_p40 + 0x8), local_r14);
    result = HalpBuddyAllocatorBltFindAndPop(local_rsi, Arg1, local_r12, local_r14);
    result = ExReleaseSpinLockExclusive(Arg1 + 112, (uint8_t)((uint8_t)(result)), local_r12, local_r14);
    if (result == 0) goto loc_0030819C;
    result = ExAcquireSpinLockShared(Arg1 + 112, (uint8_t)((uint8_t)(result)), local_r12, local_r14);
    v_stack_p20 = (uint8_t)(result);
    goto loc_0030803B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `8` | `W` |
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00307EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
