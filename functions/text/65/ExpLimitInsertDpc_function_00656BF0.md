# ExpLimitInsertDpc

- RVA: `0x00656BF0`–`0x00656F0B` (길이 `795` bytes)
- VA: `0x0000000140656BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4D08`
- 디코드: `257`개 명령, `795/795` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00656C46` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00656C5E` → [ExpLimitDpcInsertEntry](ExpLimitDpcInsertEntry_function_00656940.md) (function, `0x00656940`)
- `0x00656C92` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00656CC2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00656CCE` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x00656D1C` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x00656D3D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00656D85` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00656D91` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x00656DDF` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x00656E00` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00656E60` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00656E6C` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x00656EBA` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x00656EDB` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00656CA8` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00656CB4` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00656CD7` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00656BF0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00656BF5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00656BFA  55                              push rbp
00656BFB  56                              push rsi
00656BFC  57                              push rdi
00656BFD  41 56                           push r14
00656BFF  41 57                           push r15
00656C01  48 83 EC 30                     sub rsp, 0x30
00656C05  49 8B D9                        mov rbx, r9
00656C08  48 8B F2                        mov rsi, rdx
00656C0B  83 C8 FF                        or eax, 0xffffffff
00656C0E  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
00656C13  FF C8                           dec eax
00656C15  41 BE FF FF FF 3F               mov r14d, 0x3fffffff
00656C1B  8B F8                           mov edi, eax
00656C1D  BD 00 00 00 80                  mov ebp, 0x80000000
00656C22  F7 D7                           not edi
00656C24  23 FD                           and edi, ebp
00656C26  45 8D 7E 01                     lea r15d, [r14 + 1]
00656C2A  41 85 C6                        test r14d, eax
00656C2D  0F 85 24 01 00 00               jne 0x140656d57
00656C33  41 0B 79 04                     or edi, dword ptr [r9 + 4]
00656C37  41 87 39                        xchg dword ptr [r9], edi
00656C3A  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00656C3E  41 85 FF                        test r15d, edi
00656C41  74 08                           je 0x140656c4b
00656C43  48 8B CB                        mov rcx, rbx
00656C46  E8 D5 0F BC FF                  call 0x140217c20
00656C4B  33 FF                           xor edi, edi
00656C4D  39 3E                           cmp dword ptr [rsi], edi
00656C4F  76 18                           jbe 0x140656c69
00656C51  8B C7                           mov eax, edi
00656C53  48 6B C8 38                     imul rcx, rax, 0x38
00656C57  48 83 C1 08                     add rcx, 8
00656C5B  48 03 CE                        add rcx, rsi
00656C5E  E8 DD FC FF FF                  call 0x140656940
00656C63  FF C7                           inc edi
00656C65  3B 3E                           cmp edi, dword ptr [rsi]
00656C67  72 E8                           jb 0x140656c51
00656C69  83 C8 FF                        or eax, 0xffffffff
00656C6C  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
00656C70  FF C8                           dec eax
00656C72  8B F8                           mov edi, eax
00656C74  F7 D7                           not edi
00656C76  23 FD                           and edi, ebp
00656C78  41 85 C6                        test r14d, eax
00656C7B  75 1F                           jne 0x140656c9c
00656C7D  0B 7B 04                        or edi, dword ptr [rbx + 4]
00656C80  87 3B                           xchg dword ptr [rbx], edi
00656C82  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
00656C86  41 85 FF                        test r15d, edi
00656C89  0F 84 62 02 00 00               je 0x140656ef1
00656C8F  48 8B CB                        mov rcx, rbx
00656C92  E8 89 0F BC FF                  call 0x140217c20
00656C97  E9 55 02 00 00                  jmp 0x140656ef1
00656C9C  33 F6                           xor esi, esi
00656C9E  45 33 F6                        xor r14d, r14d
00656CA1  E9 A0 00 00 00                  jmp 0x140656d46
00656CA6  FF C6                           inc esi
00656CA8  85 35 FE E5 96 00               test dword ptr [rip + 0x96e5fe], esi
00656CAE  0F 85 90 00 00 00               jne 0x140656d44
00656CB4  8B 05 FE FD 96 00               mov eax, dword ptr [rip + 0x96fdfe]
00656CBA  A8 40                           test al, 0x40
00656CBC  0F 84 82 00 00 00               je 0x140656d44
00656CC2  E8 C9 87 CB FF                  call 0x14030f490
00656CC7  84 C0                           test al, al
00656CC9  74 79                           je 0x140656d44
00656CCB  41 FF C6                        inc r14d
00656CCE  E8 59 55 EA FF                  call 0x1404fc22c
00656CD3  84 C0                           test al, al
00656CD5  74 64                           je 0x140656d3b
00656CD7  F7 05 57 FE 96 00 00 00 02 00   test dword ptr [rip + 0x96fe57], 0x20000
00656CE1  74 58                           je 0x140656d3b
00656CE3  41 F6 C6 07                     test r14b, 7
00656CE7  75 52                           jne 0x140656d3b
00656CE9  8B 0B                           mov ecx, dword ptr [rbx]
00656CEB  8B C1                           mov eax, ecx
00656CED  23 C5                           and eax, ebp
00656CEF  3B C7                           cmp eax, edi
00656CF1  74 53                           je 0x140656d46
00656CF3  8B D1                           mov edx, ecx
00656CF5  44 8B C1                        mov r8d, ecx
00656CF8  41 0B CF                        or ecx, r15d
00656CFB  8B C2                           mov eax, edx
00656CFD  8B E9                           mov ebp, ecx
00656CFF  F0 0F B1 2B                     lock cmpxchg dword ptr [rbx], ebp
00656D03  8B C8                           mov ecx, eax
00656D05  41 3B C0                        cmp eax, r8d
00656D08  75 1D                           jne 0x140656d27
00656D0A  89 6C 24 78                     mov dword ptr [rsp + 0x78], ebp
00656D0E  41 B8 04 00 00 00               mov r8d, 4
00656D14  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00656D19  48 8B CB                        mov rcx, rbx
00656D1C  E8 1B 4D EA FF                  call 0x1404fba3c
00656D21  8B 0B                           mov ecx, dword ptr [rbx]
00656D23  3B CD                           cmp ecx, ebp
00656D25  74 E7                           je 0x140656d0e
00656D27  8B C1                           mov eax, ecx
00656D29  BD 00 00 00 80                  mov ebp, 0x80000000
00656D2E  23 C5                           and eax, ebp
00656D30  8B D1                           mov edx, ecx
00656D32  44 8B C1                        mov r8d, ecx
00656D35  3B C7                           cmp eax, edi
00656D37  75 BF                           jne 0x140656cf8
00656D39  EB 0B                           jmp 0x140656d46
00656D3B  8B CE                           mov ecx, esi
00656D3D  E8 1E 87 CB FF                  call 0x14030f460
00656D42  EB 02                           jmp 0x140656d46
00656D44  F3 90                           pause
00656D46  8B 03                           mov eax, dword ptr [rbx]
00656D48  23 C5                           and eax, ebp
00656D4A  3B C7                           cmp eax, edi
00656D4C  0F 85 54 FF FF FF               jne 0x140656ca6
00656D52  E9 99 01 00 00                  jmp 0x140656ef0
00656D57  41 8B 01                        mov eax, dword ptr [r9]
00656D5A  33 ED                           xor ebp, ebp
00656D5C  45 33 F6                        xor r14d, r14d
00656D5F  BE 00 00 00 80                  mov esi, 0x80000000
00656D64  E9 A2 00 00 00                  jmp 0x140656e0b
00656D69  FF C5                           inc ebp
00656D6B  85 2D 3B E5 96 00               test dword ptr [rip + 0x96e53b], ebp
00656D71  0F 85 90 00 00 00               jne 0x140656e07
00656D77  8B 05 3B FD 96 00               mov eax, dword ptr [rip + 0x96fd3b]
00656D7D  A8 40                           test al, 0x40
00656D7F  0F 84 82 00 00 00               je 0x140656e07
00656D85  E8 06 87 CB FF                  call 0x14030f490
00656D8A  84 C0                           test al, al
00656D8C  74 79                           je 0x140656e07
00656D8E  41 FF C6                        inc r14d
00656D91  E8 96 54 EA FF                  call 0x1404fc22c
00656D96  84 C0                           test al, al
00656D98  74 64                           je 0x140656dfe
00656D9A  F7 05 94 FD 96 00 00 00 02 00   test dword ptr [rip + 0x96fd94], 0x20000
00656DA4  74 58                           je 0x140656dfe
00656DA6  41 F6 C6 07                     test r14b, 7
00656DAA  75 52                           jne 0x140656dfe
00656DAC  8B 0B                           mov ecx, dword ptr [rbx]
00656DAE  8B C1                           mov eax, ecx
00656DB0  23 C6                           and eax, esi
00656DB2  3B C7                           cmp eax, edi
00656DB4  74 53                           je 0x140656e09
00656DB6  8B D1                           mov edx, ecx
00656DB8  44 8B C1                        mov r8d, ecx
00656DBB  41 0B CF                        or ecx, r15d
00656DBE  8B C2                           mov eax, edx
00656DC0  8B F1                           mov esi, ecx
00656DC2  F0 0F B1 33                     lock cmpxchg dword ptr [rbx], esi
00656DC6  8B C8                           mov ecx, eax
00656DC8  41 3B C0                        cmp eax, r8d
00656DCB  75 1D                           jne 0x140656dea
00656DCD  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00656DD1  41 B8 04 00 00 00               mov r8d, 4
00656DD7  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00656DDC  48 8B CB                        mov rcx, rbx
00656DDF  E8 58 4C EA FF                  call 0x1404fba3c
00656DE4  8B 0B                           mov ecx, dword ptr [rbx]
00656DE6  3B CE                           cmp ecx, esi
00656DE8  74 E7                           je 0x140656dd1
00656DEA  8B C1                           mov eax, ecx
00656DEC  BE 00 00 00 80                  mov esi, 0x80000000
00656DF1  23 C6                           and eax, esi
00656DF3  8B D1                           mov edx, ecx
00656DF5  44 8B C1                        mov r8d, ecx
00656DF8  3B C7                           cmp eax, edi
00656DFA  75 BF                           jne 0x140656dbb
00656DFC  EB 0B                           jmp 0x140656e09
00656DFE  8B CD                           mov ecx, ebp
00656E00  E8 5B 86 CB FF                  call 0x14030f460
00656E05  EB 02                           jmp 0x140656e09
00656E07  F3 90                           pause
00656E09  8B 03                           mov eax, dword ptr [rbx]
00656E0B  23 C6                           and eax, esi
00656E0D  3B C7                           cmp eax, edi
00656E0F  0F 85 54 FF FF FF               jne 0x140656d69
00656E15  90                              nop
00656E16  83 C8 FF                        or eax, 0xffffffff
00656E19  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
00656E1D  FF C8                           dec eax
00656E1F  8B F8                           mov edi, eax
00656E21  F7 D7                           not edi
00656E23  23 FE                           and edi, esi
00656E25  A9 FF FF FF 3F                  test eax, 0x3fffffff
00656E2A  75 0E                           jne 0x140656e3a
00656E2C  0B 7B 04                        or edi, dword ptr [rbx + 4]
00656E2F  87 3B                           xchg dword ptr [rbx], edi
00656E31  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
00656E35  E9 4C FE FF FF                  jmp 0x140656c86
00656E3A  33 ED                           xor ebp, ebp
00656E3C  45 33 F6                        xor r14d, r14d
00656E3F  E9 A0 00 00 00                  jmp 0x140656ee4
00656E44  FF C5                           inc ebp
00656E46  85 2D 60 E4 96 00               test dword ptr [rip + 0x96e460], ebp
00656E4C  0F 85 90 00 00 00               jne 0x140656ee2
00656E52  8B 05 60 FC 96 00               mov eax, dword ptr [rip + 0x96fc60]
00656E58  A8 40                           test al, 0x40
00656E5A  0F 84 82 00 00 00               je 0x140656ee2
00656E60  E8 2B 86 CB FF                  call 0x14030f490
00656E65  84 C0                           test al, al
00656E67  74 79                           je 0x140656ee2
00656E69  41 FF C6                        inc r14d
00656E6C  E8 BB 53 EA FF                  call 0x1404fc22c
00656E71  84 C0                           test al, al
00656E73  74 64                           je 0x140656ed9
00656E75  F7 05 B9 FC 96 00 00 00 02 00   test dword ptr [rip + 0x96fcb9], 0x20000
00656E7F  74 58                           je 0x140656ed9
00656E81  41 F6 C6 07                     test r14b, 7
00656E85  75 52                           jne 0x140656ed9
00656E87  8B 0B                           mov ecx, dword ptr [rbx]
00656E89  8B C1                           mov eax, ecx
00656E8B  23 C6                           and eax, esi
00656E8D  3B C7                           cmp eax, edi
00656E8F  74 53                           je 0x140656ee4
00656E91  8B D1                           mov edx, ecx
00656E93  44 8B C1                        mov r8d, ecx
00656E96  41 0B CF                        or ecx, r15d
00656E99  8B C2                           mov eax, edx
00656E9B  8B F1                           mov esi, ecx
00656E9D  F0 0F B1 33                     lock cmpxchg dword ptr [rbx], esi
00656EA1  8B C8                           mov ecx, eax
00656EA3  41 3B C0                        cmp eax, r8d
00656EA6  75 1D                           jne 0x140656ec5
00656EA8  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
00656EAC  41 B8 04 00 00 00               mov r8d, 4
00656EB2  48 8D 54 24 24                  lea rdx, [rsp + 0x24]
00656EB7  48 8B CB                        mov rcx, rbx
00656EBA  E8 7D 4B EA FF                  call 0x1404fba3c
00656EBF  8B 0B                           mov ecx, dword ptr [rbx]
00656EC1  3B CE                           cmp ecx, esi
00656EC3  74 E7                           je 0x140656eac
00656EC5  8B C1                           mov eax, ecx
00656EC7  BE 00 00 00 80                  mov esi, 0x80000000
00656ECC  23 C6                           and eax, esi
00656ECE  8B D1                           mov edx, ecx
00656ED0  44 8B C1                        mov r8d, ecx
00656ED3  3B C7                           cmp eax, edi
00656ED5  75 BF                           jne 0x140656e96
00656ED7  EB 0B                           jmp 0x140656ee4
00656ED9  8B CD                           mov ecx, ebp
00656EDB  E8 80 85 CB FF                  call 0x14030f460
00656EE0  EB 02                           jmp 0x140656ee4
00656EE2  F3 90                           pause
00656EE4  8B 03                           mov eax, dword ptr [rbx]
00656EE6  23 C6                           and eax, esi
00656EE8  3B C7                           cmp eax, edi
00656EEA  0F 85 54 FF FF FF               jne 0x140656e44
00656EF0  90                              nop
00656EF1  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00656EF6  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00656EFB  F0 FF 08                        lock dec dword ptr [rax]
00656EFE  48 83 C4 30                     add rsp, 0x30
00656F02  41 5F                           pop r15
00656F04  41 5E                           pop r14
00656F06  5F                              pop rdi
00656F07  5E                              pop rsi
00656F08  5D                              pop rbp
00656F09  C3                              ret
00656F0A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpLimitInsertDpc(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x3FFFFFFFULL))) & ((unsigned int)(result))) != 0) goto loc_00656D57;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a4 + 4)));
    v_stack_m38 = (unsigned int)(v_rdi);
    if ((((unsigned int)((unsigned int)(0x3FFFFFFFULL) + 1)) & ((unsigned int)(v_rdi))) != 0) {
        a1 = a4;
        result = KeWakeAddressAll(a1, a2, a3, a4);
    }
    v_rdi = 0;
    if ((*(unsigned int *)(a2)) <= 0) goto loc_00656C69;
loc_00656C51:
    a1 = (a1) * (0);
    a1 = (a1) + (8);
    a1 = (a1) + (a2);
    result = ExpLimitDpcInsertEntry(a1, a2, a3, a4);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(a2))) goto loc_00656C51;
loc_00656C69:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x3FFFFFFFULL))) & ((unsigned int)(result))) != 0) goto loc_00656C9C;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a4 + 4)));
    v_stack_p20 = (unsigned int)(v_rdi);
loc_00656C86:
    if ((((unsigned int)((unsigned int)(0x3FFFFFFFULL) + 1)) & ((unsigned int)(v_rdi))) == 0) goto loc_00656EF1;
    result = KeWakeAddressAll(a4, a2, a3, a4);
    goto loc_00656EF1;
loc_00656C9C:
    v_rsi = 0;
    v_r14 = 0;
    goto loc_00656D46;
loc_00656CA6:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 9889278)) & ((unsigned int)(v_rsi))) != 0) goto loc_00656D44;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9895422)))) & (64)) == 0) goto loc_00656D44;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656D44;
    v_r14 = (unsigned int)((v_r14) + 1);
    result = KeCanUseHaltOnAddress(a4, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656D3B;
    if (((*(unsigned int *)(v_rip + 9895511)) & (0x20000ULL)) == 0) goto loc_00656D3B;
    if ((((unsigned __int8)(v_r14)) & (7)) != 0) goto loc_00656D3B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_00656D46;
loc_00656CF8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)((unsigned int)(0x3FFFFFFFULL) + 1)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00656D27;
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_00656D0E:
    result = KiHaltOnAddress(a4, v_stack_p20, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00656D0E;
loc_00656D27:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656CF8;
    goto loc_00656D46;
loc_00656D3B:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    goto loc_00656D46;
loc_00656D44:
loc_00656D46:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656CA6;
    goto loc_00656EF0;
loc_00656D57:
    v_rbp = 0;
    v_r14 = 0;
    goto loc_00656E0B;
loc_00656D69:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 9889083)) & ((unsigned int)(v_rbp))) != 0) goto loc_00656E07;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9895227)))) & (64)) == 0) goto loc_00656E07;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656E07;
    v_r14 = (unsigned int)((v_r14) + 1);
    result = KeCanUseHaltOnAddress((unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656DFE;
    if (((*(unsigned int *)(v_rip + 9895316)) & (0x20000ULL)) == 0) goto loc_00656DFE;
    if ((((unsigned __int8)(v_r14)) & (7)) != 0) goto loc_00656DFE;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_00656E09;
loc_00656DBB:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)((unsigned int)(0x3FFFFFFFULL) + 1)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00656DEA;
    v_stack_m38 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_00656DD1:
    result = KiHaltOnAddress(a4, v_stack_m38, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00656DD1;
loc_00656DEA:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656DBB;
    goto loc_00656E09;
loc_00656DFE:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    goto loc_00656E09;
loc_00656E07:
loc_00656E09:
loc_00656E0B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656D69;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_00656E3A;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a4 + 4)));
    v_stack_m34 = (unsigned int)(v_rdi);
    goto loc_00656C86;
loc_00656E3A:
    v_rbp = 0;
    v_r14 = 0;
    goto loc_00656EE4;
loc_00656E44:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 9888864)) & ((unsigned int)(v_rbp))) != 0) goto loc_00656EE2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9895008)))) & (64)) == 0) goto loc_00656EE2;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656EE2;
    v_r14 = (unsigned int)((v_r14) + 1);
    result = KeCanUseHaltOnAddress((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00656ED9;
    if (((*(unsigned int *)(v_rip + 9895097)) & (0x20000ULL)) == 0) goto loc_00656ED9;
    if ((((unsigned __int8)(v_r14)) & (7)) != 0) goto loc_00656ED9;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_00656EE4;
loc_00656E96:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)((unsigned int)(0x3FFFFFFFULL) + 1)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))))) goto loc_00656EC5;
    v_stack_m34 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_00656EAC:
    result = KiHaltOnAddress(a4, v_stack_m34, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00656EAC;
loc_00656EC5:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656E96;
    goto loc_00656EE4;
loc_00656ED9:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4)))), a4);
    goto loc_00656EE4;
loc_00656EE2:
loc_00656EE4:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00656E44;
loc_00656EF0:
loc_00656EF1:
    v_rsp = (v_rsp) + (48);
    return v_stack_p18;
}
```

## 5. (Beta) C Style

```c
int64_t ExpLimitInsertDpc(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x3FFFFFFFULL))) & ((uint32_t)(result))) != 0) goto loc_00656D57;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_m38 = (uint32_t)(local_rdi);
    if ((((uint32_t)((uint32_t)(0x3FFFFFFFULL) + 1)) & ((uint32_t)(local_rdi))) != 0) {
        Arg1 = Arg4;
        result = KeWakeAddressAll(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = 0;
    if ((*(uint32_t *)(arg2)) <= 0) goto loc_00656C69;
loc_00656C51:
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) + (8);
    Arg1 = (Arg1) + (Arg2);
    result = ExpLimitDpcInsertEntry(Arg1, Arg2, Arg3, Arg4);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(arg2))) goto loc_00656C51;
loc_00656C69:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x3FFFFFFFULL))) & ((uint32_t)(result))) != 0) goto loc_00656C9C;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_p20 = (uint32_t)(local_rdi);
loc_00656C86:
    if ((((uint32_t)((uint32_t)(0x3FFFFFFFULL) + 1)) & ((uint32_t)(local_rdi))) == 0) goto loc_00656EF1;
    result = KeWakeAddressAll(Arg4, Arg2, Arg3, Arg4);
    goto loc_00656EF1;
loc_00656C9C:
    local_rsi = 0;
    local_r14 = 0;
    goto loc_00656D46;
loc_00656CA6:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0x96E5FE)) & ((uint32_t)(local_rsi))) != 0) goto loc_00656D44;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96FDFE)))) & (64)) == 0) goto loc_00656D44;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656D44;
    local_r14 = (uint32_t)((local_r14) + 1);
    result = KeCanUseHaltOnAddress(Arg4, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656D3B;
    if (((*(uint32_t *)(v_rip + 0x96FE57)) & (0x20000ULL)) == 0) goto loc_00656D3B;
    if ((((uint8_t)(local_r14)) & (7)) != 0) goto loc_00656D3B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_00656D46;
loc_00656CF8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) | ((uint32_t)((uint32_t)(0x3FFFFFFFULL) + 1)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00656D27;
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_00656D0E:
    result = KiHaltOnAddress(Arg4, v_stack_p20, 4, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00656D0E;
loc_00656D27:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656CF8;
    goto loc_00656D46;
loc_00656D3B:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    goto loc_00656D46;
loc_00656D44:
loc_00656D46:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656CA6;
    goto loc_00656EF0;
loc_00656D57:
    local_rbp = 0;
    local_r14 = 0;
    goto loc_00656E0B;
loc_00656D69:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0x96E53B)) & ((uint32_t)(local_rbp))) != 0) goto loc_00656E07;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96FD3B)))) & (64)) == 0) goto loc_00656E07;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656E07;
    local_r14 = (uint32_t)((local_r14) + 1);
    result = KeCanUseHaltOnAddress((uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656DFE;
    if (((*(uint32_t *)(v_rip + 0x96FD94)) & (0x20000ULL)) == 0) goto loc_00656DFE;
    if ((((uint8_t)(local_r14)) & (7)) != 0) goto loc_00656DFE;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_00656E09;
loc_00656DBB:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) | ((uint32_t)((uint32_t)(0x3FFFFFFFULL) + 1)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00656DEA;
    v_stack_m38 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_00656DD1:
    result = KiHaltOnAddress(Arg4, v_stack_m38, 4, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00656DD1;
loc_00656DEA:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656DBB;
    goto loc_00656E09;
loc_00656DFE:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    goto loc_00656E09;
loc_00656E07:
loc_00656E09:
loc_00656E0B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656D69;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_00656E3A;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_m34 = (uint32_t)(local_rdi);
    goto loc_00656C86;
loc_00656E3A:
    local_rbp = 0;
    local_r14 = 0;
    goto loc_00656EE4;
loc_00656E44:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0x96E460)) & ((uint32_t)(local_rbp))) != 0) goto loc_00656EE2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96FC60)))) & (64)) == 0) goto loc_00656EE2;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656EE2;
    local_r14 = (uint32_t)((local_r14) + 1);
    result = KeCanUseHaltOnAddress((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00656ED9;
    if (((*(uint32_t *)(v_rip + 0x96FCB9)) & (0x20000ULL)) == 0) goto loc_00656ED9;
    if ((((uint8_t)(local_r14)) & (7)) != 0) goto loc_00656ED9;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_00656EE4;
loc_00656E96:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) | ((uint32_t)((uint32_t)(0x3FFFFFFFULL) + 1)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))))) goto loc_00656EC5;
    v_stack_m34 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_00656EAC:
    result = KiHaltOnAddress(Arg4, v_stack_m34, 4, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00656EAC;
loc_00656EC5:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656E96;
    goto loc_00656EE4;
loc_00656ED9:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))), Arg4);
    goto loc_00656EE4;
loc_00656EE2:
loc_00656EE4:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00656E44;
loc_00656EF0:
loc_00656EF1:
    local_rsp = (local_rsp) + (48);
    return v_stack_p18;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00656BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
