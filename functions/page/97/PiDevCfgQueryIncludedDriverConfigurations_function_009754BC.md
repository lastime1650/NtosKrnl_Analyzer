# PiDevCfgQueryIncludedDriverConfigurations

- RVA: `0x009754BC`–`0x00975844` (길이 `904` bytes)
- VA: `0x00000001409754BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009665C`
- 디코드: `252`개 명령, `904/904` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0097550E` → [PiDevCfgPushDriverNodeEntry](../../text/5A/PiDevCfgPushDriverNodeEntry_function_005A7FA8.md) (function, `0x005A7FA8`)
- `0x0097552B` → [PiDevCfgPopDriverNodeEntry](../../text/4D/PiDevCfgPopDriverNodeEntry_function_004D4E5C.md) (function, `0x004D4E5C`)
- `0x00975562` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x009755AD` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (function, `0x00501E50`)
- `0x009755FE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x0097562A` → [PiDevCfgGetDriverConfigurationKeyScope](../../text/5A/PiDevCfgGetDriverConfigurationKeyScope_function_005A7D68.md) (function, `0x005A7D68`)
- `0x00975651` → [PiDevCfgQueryIncludedDriverNode](../73/PiDevCfgQueryIncludedDriverNode_function_00734D88.md) (function, `0x00734D88`)
- `0x00975682` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00975697` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x009756B8` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x009756FF` → [PiDevCfgQueryDriverConfiguration](PiDevCfgQueryDriverConfiguration_function_0097584C.md) (function, `0x0097584C`)
- `0x00975731` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x0097575A` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x00975785` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009757AC` → [PiDevCfgAppendMultiSz](../73/PiDevCfgAppendMultiSz_function_00731B28.md) (function, `0x00731B28`)
- `0x009757BE` → [PiDevCfgPushDriverNodeEntry](../../text/5A/PiDevCfgPushDriverNodeEntry_function_005A7FA8.md) (function, `0x005A7FA8`)
- `0x0097581B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiDevCfgQueryDriverConfiguration](PiDevCfgQueryDriverConfiguration_function_0097584C.md) at `0x00975E44`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0097550E` → [PiDevCfgPushDriverNodeEntry](../../text/5A/PiDevCfgPushDriverNodeEntry_function_005A7FA8.md) (`PAGE` → `.text`)
  - `0x0097552B` → [PiDevCfgPopDriverNodeEntry](../../text/4D/PiDevCfgPopDriverNodeEntry_function_004D4E5C.md) (`PAGE` → `.text`)
  - `0x00975562` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x009755AD` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (`PAGE` → `.text`)
  - `0x009755FE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x0097562A` → [PiDevCfgGetDriverConfigurationKeyScope](../../text/5A/PiDevCfgGetDriverConfigurationKeyScope_function_005A7D68.md) (`PAGE` → `.text`)
  - `0x00975731` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x009757BE` → [PiDevCfgPushDriverNodeEntry](../../text/5A/PiDevCfgPushDriverNodeEntry_function_005A7FA8.md) (`PAGE` → `.text`)
  - `0x0097581B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009754BC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009754C1  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
009754C6  55                              push rbp
009754C7  56                              push rsi
009754C8  57                              push rdi
009754C9  41 54                           push r12
009754CB  41 55                           push r13
009754CD  41 56                           push r14
009754CF  41 57                           push r15
009754D1  48 8B EC                        mov rbp, rsp
009754D4  48 83 EC 40                     sub rsp, 0x40
009754D8  45 33 F6                        xor r14d, r14d
009754DB  48 8D 45 F0                     lea rax, [rbp - 0x10]
009754DF  4C 8B F9                        mov r15, rcx
009754E2  48 89 45 F8                     mov qword ptr [rbp - 8], rax
009754E6  48 8D 45 F0                     lea rax, [rbp - 0x10]
009754EA  4C 89 75 48                     mov qword ptr [rbp + 0x48], r14
009754EE  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
009754F2  4C 89 75 50                     mov qword ptr [rbp + 0x50], r14
009754F6  4C 39 B1 78 01 00 00            cmp qword ptr [rcx + 0x178], r14
009754FD  75 08                           jne 0x140975507
009754FF  41 8B DE                        mov ebx, r14d
00975502  E9 E7 02 00 00                  jmp 0x1409757ee
00975507  48 8B D1                        mov rdx, rcx
0097550A  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0097550E  E8 95 2A C3 FF                  call 0x1405a7fa8
00975513  8B D8                           mov ebx, eax
00975515  85 C0                           test eax, eax
00975517  0F 88 D1 02 00 00               js 0x1409757ee
0097551D  41 BD 2A 00 00 00               mov r13d, 0x2a
00975523  48 8D 55 48                     lea rdx, [rbp + 0x48]
00975527  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0097552B  E8 2C F9 B5 FF                  call 0x1404d4e5c
00975530  84 C0                           test al, al
00975532  0F 84 B6 02 00 00               je 0x1409757ee
00975538  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
0097553C  48 8B B6 78 01 00 00            mov rsi, qword ptr [rsi + 0x178]
00975543  48 85 F6                        test rsi, rsi
00975546  74 DB                           je 0x140975523
00975548  8B C3                           mov eax, ebx
0097554A  4C 8B E6                        mov r12, rsi
0097554D  66 44 39 36                     cmp word ptr [rsi], r14w
00975551  0F 84 80 02 00 00               je 0x1409757d7
00975557  BA 3A 00 00 00                  mov edx, 0x3a
0097555C  48 8B CE                        mov rcx, rsi
0097555F  4C 8B F6                        mov r14, rsi
00975562  E8 F9 C4 B8 FF                  call 0x140501a60
00975567  48 8B F8                        mov rdi, rax
0097556A  33 C0                           xor eax, eax
0097556C  48 85 FF                        test rdi, rdi
0097556F  0F 84 5A 02 00 00               je 0x1409757cf
00975575  66 89 07                        mov word ptr [rdi], ax
00975578  48 83 C7 02                     add rdi, 2
0097557C  48 8B F7                        mov rsi, rdi
0097557F  66 45 39 2E                     cmp word ptr [r14], r13w
00975583  75 10                           jne 0x140975595
00975585  41 0F B7 4E 02                  movzx ecx, word ptr [r14 + 2]
0097558A  45 33 F6                        xor r14d, r14d
0097558D  66 41 3B CE                     cmp cx, r14w
00975591  74 0A                           je 0x14097559d
00975593  EB 03                           jmp 0x140975598
00975595  45 33 F6                        xor r14d, r14d
00975598  1B C0                           sbb eax, eax
0097559A  83 C8 01                        or eax, 1
0097559D  F7 D8                           neg eax
0097559F  BA 2E 00 00 00                  mov edx, 0x2e
009755A4  48 8B CF                        mov rcx, rdi
009755A7  4D 1B ED                        sbb r13, r13
009755AA  4D 23 EC                        and r13, r12
009755AD  E8 9E C8 B8 FF                  call 0x140501e50
009755B2  48 8B D0                        mov rdx, rax
009755B5  48 85 C0                        test rax, rax
009755B8  0F 84 02 01 00 00               je 0x1409756c0
009755BE  66 44 89 30                     mov word ptr [rax], r14w
009755C2  48 8D 70 02                     lea rsi, [rax + 2]
009755C6  44 0F B7 40 02                  movzx r8d, word ptr [rax + 2]
009755CB  41 83 E8 2A                     sub r8d, 0x2a
009755CF  75 0C                           jne 0x1409755dd
009755D1  44 0F B7 40 04                  movzx r8d, word ptr [rax + 4]
009755D6  41 0F B7 C6                     movzx eax, r14w
009755DA  44 2B C0                        sub r8d, eax
009755DD  45 85 C0                        test r8d, r8d
009755E0  75 06                           jne 0x1409755e8
009755E2  41 83 CE FF                     or r14d, 0xffffffff
009755E6  EB 53                           jmp 0x14097563b
009755E8  45 33 E4                        xor r12d, r12d
009755EB  48 8D 72 02                     lea rsi, [rdx + 2]
009755EF  66 44 39 62 02                  cmp word ptr [rdx + 2], r12w
009755F4  74 45                           je 0x14097563b
009755F6  BA 2C 00 00 00                  mov edx, 0x2c
009755FB  48 8B CE                        mov rcx, rsi
009755FE  E8 5D C4 B8 FF                  call 0x140501a60
00975603  48 8B D8                        mov rbx, rax
00975606  48 85 C0                        test rax, rax
00975609  74 0A                           je 0x140975615
0097560B  66 44 89 20                     mov word ptr [rax], r12w
0097560F  48 83 C3 02                     add rbx, 2
00975613  EB 12                           jmp 0x140975627
00975615  48 83 C8 FF                     or rax, 0xffffffffffffffff
00975619  48 FF C0                        inc rax
0097561C  66 44 39 24 46                  cmp word ptr [rsi + rax*2], r12w
00975621  75 F6                           jne 0x140975619
00975623  48 8D 1C 46                     lea rbx, [rsi + rax*2]
00975627  48 8B CE                        mov rcx, rsi
0097562A  E8 39 27 C3 FF                  call 0x1405a7d68
0097562F  44 0B F0                        or r14d, eax
00975632  48 8B F3                        mov rsi, rbx
00975635  66 44 39 23                     cmp word ptr [rbx], r12w
00975639  75 BB                           jne 0x1409755f6
0097563B  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0097563F  48 8D 45 50                     lea rax, [rbp + 0x50]
00975643  45 8B CE                        mov r9d, r14d
00975646  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097564B  4C 8B C7                        mov r8, rdi
0097564E  49 8B D5                        mov rdx, r13
00975651  E8 32 F7 DB FF                  call 0x140734d88
00975656  8B D8                           mov ebx, eax
00975658  85 C0                           test eax, eax
0097565A  0F 88 87 01 00 00               js 0x1409757e7
00975660  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00975664  4D 8D B7 80 01 00 00            lea r14, [r15 + 0x180]
0097566B  4D 8B 26                        mov r12, qword ptr [r14]
0097566E  4D 3B E6                        cmp r12, r14
00975671  74 6E                           je 0x1409756e1
00975673  49 8D 4C 24 58                  lea rcx, [r12 + 0x58]
00975678  41 B0 01                        mov r8b, 1
0097567B  48 8D 57 58                     lea rdx, [rdi + 0x58]
0097567F  4D 8B EC                        mov r13, r12
00975682  E8 99 D3 FB FF                  call 0x140932a20
00975687  84 C0                           test al, al
00975689  74 15                           je 0x1409756a0
0097568B  48 8D 57 28                     lea rdx, [rdi + 0x28]
0097568F  41 B0 01                        mov r8b, 1
00975692  49 8D 4C 24 28                  lea rcx, [r12 + 0x28]
00975697  E8 84 D3 FB FF                  call 0x140932a20
0097569C  84 C0                           test al, al
0097569E  75 0C                           jne 0x1409756ac
009756A0  4D 8B 24 24                     mov r12, qword ptr [r12]
009756A4  45 33 ED                        xor r13d, r13d
009756A7  4D 3B E6                        cmp r12, r14
009756AA  75 C7                           jne 0x140975673
009756AC  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
009756B0  4D 85 ED                        test r13, r13
009756B3  74 2C                           je 0x1409756e1
009756B5  48 8B CF                        mov rcx, rdi
009756B8  E8 97 DC DB FF                  call 0x140733354
009756BD  45 33 F6                        xor r14d, r14d
009756C0  41 BD 2A 00 00 00               mov r13d, 0x2a
009756C6  48 83 C8 FF                     or rax, 0xffffffffffffffff
009756CA  48 FF C0                        inc rax
009756CD  66 44 39 34 46                  cmp word ptr [rsi + rax*2], r14w
009756D2  75 F6                           jne 0x1409756ca
009756D4  48 8D 34 46                     lea rsi, [rsi + rax*2]
009756D8  48 83 C6 02                     add rsi, 2
009756DC  E9 67 FE FF FF                  jmp 0x140975548
009756E1  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
009756E5  4C 39 30                        cmp qword ptr [rax], r14
009756E8  0F 85 34 01 00 00               jne 0x140975822
009756EE  4C 89 37                        mov qword ptr [rdi], r14
009756F1  48 8B CF                        mov rcx, rdi
009756F4  48 89 47 08                     mov qword ptr [rdi + 8], rax
009756F8  48 89 38                        mov qword ptr [rax], rdi
009756FB  49 89 7E 08                     mov qword ptr [r14 + 8], rdi
009756FF  E8 48 01 00 00                  call 0x14097584c
00975704  45 33 F6                        xor r14d, r14d
00975707  8B D8                           mov ebx, eax
00975709  85 C0                           test eax, eax
0097570B  0F 88 DD 00 00 00               js 0x1409757ee
00975711  4C 39 B7 28 01 00 00            cmp qword ptr [rdi + 0x128], r14
00975718  74 24                           je 0x14097573e
0097571A  4D 39 B7 28 01 00 00            cmp qword ptr [r15 + 0x128], r14
00975721  75 1B                           jne 0x14097573e
00975723  48 8D 97 20 01 00 00            lea rdx, [rdi + 0x120]
0097572A  49 8D 8F 20 01 00 00            lea rcx, [r15 + 0x120]
00975731  E8 0E 69 B5 FF                  call 0x1404cc044
00975736  84 C0                           test al, al
00975738  0F 84 A2 00 00 00               je 0x1409757e0
0097573E  4C 39 B7 38 01 00 00            cmp qword ptr [rdi + 0x138], r14
00975745  74 22                           je 0x140975769
00975747  4C 8D 87 30 01 00 00            lea r8, [rdi + 0x130]
0097574E  45 33 C9                        xor r9d, r9d
00975751  49 8D 8F 30 01 00 00            lea rcx, [r15 + 0x130]
00975758  33 D2                           xor edx, edx
0097575A  E8 C9 C3 DB FF                  call 0x140731b28
0097575F  8B D8                           mov ebx, eax
00975761  85 C0                           test eax, eax
00975763  0F 88 85 00 00 00               js 0x1409757ee
00975769  4C 39 B7 48 01 00 00            cmp qword ptr [rdi + 0x148], r14
00975770  74 1E                           je 0x140975790
00975772  4C 8D 87 40 01 00 00            lea r8, [rdi + 0x140]
00975779  45 33 C9                        xor r9d, r9d
0097577C  49 8D 8F 40 01 00 00            lea rcx, [r15 + 0x140]
00975783  33 D2                           xor edx, edx
00975785  E8 9E C3 DB FF                  call 0x140731b28
0097578A  8B D8                           mov ebx, eax
0097578C  85 C0                           test eax, eax
0097578E  78 5E                           js 0x1409757ee
00975790  4C 39 B7 58 01 00 00            cmp qword ptr [rdi + 0x158], r14
00975797  74 1E                           je 0x1409757b7
00975799  4C 8D 87 50 01 00 00            lea r8, [rdi + 0x150]
009757A0  45 33 C9                        xor r9d, r9d
009757A3  49 8D 8F 50 01 00 00            lea rcx, [r15 + 0x150]
009757AA  33 D2                           xor edx, edx
009757AC  E8 77 C3 DB FF                  call 0x140731b28
009757B1  8B D8                           mov ebx, eax
009757B3  85 C0                           test eax, eax
009757B5  78 37                           js 0x1409757ee
009757B7  48 8B D7                        mov rdx, rdi
009757BA  48 8D 4D F0                     lea rcx, [rbp - 0x10]
009757BE  E8 E5 27 C3 FF                  call 0x1405a7fa8
009757C3  8B D8                           mov ebx, eax
009757C5  85 C0                           test eax, eax
009757C7  0F 89 F3 FE FF FF               jns 0x1409756c0
009757CD  EB 1F                           jmp 0x1409757ee
009757CF  45 33 F6                        xor r14d, r14d
009757D2  E9 EF FE FF FF                  jmp 0x1409756c6
009757D7  85 C0                           test eax, eax
009757D9  78 13                           js 0x1409757ee
009757DB  E9 43 FD FF FF                  jmp 0x140975523
009757E0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009757E5  EB 07                           jmp 0x1409757ee
009757E7  41 89 87 BC 01 00 00            mov dword ptr [r15 + 0x1bc], eax
009757EE  48 8D 45 F0                     lea rax, [rbp - 0x10]
009757F2  48 39 45 F0                     cmp qword ptr [rbp - 0x10], rax
009757F6  74 31                           je 0x140975829
009757F8  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
009757FC  48 8D 45 F0                     lea rax, [rbp - 0x10]
00975800  48 39 01                        cmp qword ptr [rcx], rax
00975803  75 1D                           jne 0x140975822
00975805  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00975809  48 39 08                        cmp qword ptr [rax], rcx
0097580C  75 14                           jne 0x140975822
0097580E  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00975812  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00975816  48 89 10                        mov qword ptr [rax], rdx
00975819  33 D2                           xor edx, edx
0097581B  E8 50 D0 20 00                  call 0x140b82870
00975820  EB CC                           jmp 0x1409757ee
00975822  B9 03 00 00 00                  mov ecx, 3
00975827  CD 29                           int 0x29
00975829  8B C3                           mov eax, ebx
0097582B  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00975833  48 83 C4 40                     add rsp, 0x40
00975837  41 5F                           pop r15
00975839  41 5E                           pop r14
0097583B  41 5D                           pop r13
0097583D  41 5C                           pop r12
0097583F  5F                              pop rdi
00975840  5E                              pop rsi
00975841  5D                              pop rbp
00975842  C3                              ret
00975843  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgQueryIncludedDriverConfigurations(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_r14 = 0;
    v_stack_m40 = v_stack_m48;
    v_stack_p10 = 0;
    v_stack_m48 = v_stack_m48;
    v_stack_p18 = 0;
    if ((*(unsigned __int64 *)(a1 + 376)) != 0) goto loc_00975507;
    goto loc_009757EE;
loc_00975507:
    result = PiDevCfgPushDriverNodeEntry(v_stack_m48, a1, a3, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975523:
    result = PiDevCfgPopDriverNodeEntry(v_stack_m48, v_stack_p10, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009757EE;
    if (*(unsigned __int64 *)(v_stack_p10 + 376) == 0) goto loc_00975523;
loc_00975548:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 376))) == 0) goto loc_009757D7;
    result = wcschr(*(unsigned __int64 *)(v_stack_p10 + 376), 58, a3, a4);
    result = 0;
    if (0 == 0) goto loc_009757CF;
    *(unsigned __int16 *)(result) = 0;
    v_rdi = (result) + (2);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 376))) != 42) goto loc_00975595;
    v_r14 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 376) + 2))) == 0) goto loc_0097559D;
    goto loc_00975598;
loc_00975595:
    v_r14 = 0;
loc_00975598:
    result = (unsigned int)((result) | (1));
loc_0097559D:
    result = (unsigned int)(-(result));
    v_r13 = (42) & (*(unsigned __int64 *)(v_stack_p10 + 376));
    result = wcsrchr(v_rdi, 46, a3, a4);
    if (result == 0) goto loc_009756C0;
    *(unsigned __int16 *)(result) = 0;
    a3 = (unsigned int)((*(unsigned __int16 *)(result + 2)) - (42));
    if (!(condition_is_not_equal)) {
        a3 = *(unsigned __int16 *)(result + 4);
        result = 0;
        a3 = (unsigned int)((a3) - ((unsigned int)(result)));
    }
    if ((unsigned int)(a3) != 0) goto loc_009755E8;
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    goto loc_0097563B;
loc_009755E8:
    v_r12 = 0;
    if ((*(unsigned __int16 *)(result + 2)) == 0) goto loc_0097563B;
loc_009755F6:
    result = wcschr(result + 2, 44, a3, a4);
    if (result == 0) goto loc_00975615;
    *(unsigned __int16 *)(result) = 0;
    v_rbx = (result) + (2);
    goto loc_00975627;
loc_00975615:
    result = (result) | (-1);
loc_00975619:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(result + 2 + result * 2)) != 0) goto loc_00975619;
loc_00975627:
    result = PiDevCfgGetDriverConfigurationKeyScope(result + 2, 44, a3, a4);
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(result)));
    if ((*(unsigned __int16 *)(result + 2 + result * 2)) != 0) goto loc_009755F6;
loc_0097563B:
    v_stack_m58 = v_stack_p18;
    result = PiDevCfgQueryIncludedDriverNode(v_stack_p10, v_r13, v_rdi, (unsigned int)((unsigned int)(v_r14)));
    if (sign_flag) goto loc_009757E7;
    if ((*(unsigned __int64 *)(a1 + 384)) == (a1 + 384)) goto loc_009756E1;
loc_00975673:
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(a1 + 384) + 88, v_stack_p18 + 88, 1, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) == 0) goto loc_009756A0;
    result = RtlEqualUnicodeString(*(unsigned __int64 *)(a1 + 384) + 40, v_stack_p18 + 40, 1, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) != 0) goto loc_009756AC;
loc_009756A0:
    v_r13 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 384))) != (a1 + 384)) goto loc_00975673;
loc_009756AC:
    if (0 == 0) goto loc_009756E1;
    result = PiDevCfgFreeDriverNode(v_stack_p18, v_stack_p18 + 40, 1, (unsigned int)((unsigned int)(v_r14)));
    v_r14 = 0;
loc_009756C0:
loc_009756C6:
    result = (result) | (-1);
loc_009756CA:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(result + 2 + result * 2 + result * 2)) != 0) goto loc_009756CA;
    v_rsi = (result + 2 + result * 2 + result * 2) + (2);
    goto loc_00975548;
loc_009756E1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8))) != 0) goto loc_00975822;
    *(unsigned __int64 *)(v_stack_p18) = 0;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)(v_r14 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8)) = v_stack_p18;
    *(unsigned __int64 *)(v_r14 + 8) = v_stack_p18;
    result = PiDevCfgQueryDriverConfiguration(v_stack_p18, v_stack_p18 + 40, 1, (unsigned int)((unsigned int)(v_r14)));
    v_r14 = 0;
    if (sign_flag) goto loc_009757EE;
    if ((*(unsigned __int64 *)(v_stack_p18 + 296)) == 0) goto loc_0097573E;
    if ((*(unsigned __int64 *)(v_stack_p8 + 296)) != 0) goto loc_0097573E;
    result = PnpDuplicateUnicodeString(v_stack_p8 + 288, v_stack_p18 + 288, 1, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned __int8)(result) == 0) goto loc_009757E0;
loc_0097573E:
    if ((*(unsigned __int64 *)(v_stack_p18 + 312)) == 0) goto loc_00975769;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 304, a2, v_stack_p18 + 304, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975769:
    if ((*(unsigned __int64 *)(v_stack_p18 + 328)) == 0) goto loc_00975790;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 320, a2, v_stack_p18 + 320, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975790:
    if ((*(unsigned __int64 *)(v_stack_p18 + 344)) == 0) goto loc_009757B7;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 336, a2, v_stack_p18 + 336, a4);
    if (sign_flag) goto loc_009757EE;
loc_009757B7:
    result = PiDevCfgPushDriverNodeEntry(v_stack_m48, v_stack_p18, v_stack_p18 + 336, a4);
    if (!sign_flag) goto loc_009756C0;
    goto loc_009757EE;
loc_009757CF:
    v_r14 = 0;
    goto loc_009756C6;
loc_009757D7:
    if (sign_flag) goto loc_009757EE;
    goto loc_00975523;
loc_009757E0:
    goto loc_009757EE;
loc_009757E7:
    *(unsigned int *)(v_stack_p8 + 444) = (unsigned int)(result);
loc_009757EE:
    if (v_stack_m48 == v_stack_m48) goto loc_00975829;
    if ((*(unsigned __int64 *)(v_stack_m40)) != v_stack_m48) goto loc_00975822;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m40 + 8))) != v_stack_m40) goto loc_00975822;
    v_stack_m40 = *(unsigned __int64 *)(v_stack_m40 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m40 + 8)) = v_stack_m48;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m40, a2, v_stack_p18 + 336, a4);
    goto loc_009757EE;
loc_00975822:
loc_00975829:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgQueryIncludedDriverConfigurations(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    local_r14 = 0;
    v_stack_m40 = v_stack_m48;
    v_stack_p10 = 0;
    v_stack_m48 = v_stack_m48;
    v_stack_p18 = 0;
    if ((*(uint64_t *)(arg1 + 0x178)) != 0) goto loc_00975507;
    goto loc_009757EE;
loc_00975507:
    result = PiDevCfgPushDriverNodeEntry(v_stack_m48, Arg1, a3, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975523:
    result = PiDevCfgPopDriverNodeEntry(v_stack_m48, v_stack_p10, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_009757EE;
    if (*(uint64_t *)(v_stack_p10 + 0x178) == 0) goto loc_00975523;
loc_00975548:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x178))) == 0) goto loc_009757D7;
    result = wcschr(*(uint64_t *)(v_stack_p10 + 0x178), 58, a3, a4);
    result = 0;
    if (0 == 0) goto loc_009757CF;
    *(uint16_t *)(result) = 0;
    local_rdi = (result) + (2);
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x178))) != 42) goto loc_00975595;
    local_r14 = 0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x178) + 0x2))) == 0) goto loc_0097559D;
    goto loc_00975598;
loc_00975595:
    local_r14 = 0;
loc_00975598:
    result = (uint32_t)((result) | (1));
loc_0097559D:
    result = (uint32_t)(-(result));
    local_r13 = (42) & (*(uint64_t *)(v_stack_p10 + 0x178));
    result = wcsrchr(local_rdi, 46, a3, a4);
    if (result == 0) goto loc_009756C0;
    *(uint16_t *)(result) = 0;
    a3 = (uint32_t)((*(uint16_t *)(result + 0x2)) - (42));
    if (!(condition_is_not_equal)) {
        a3 = *(uint16_t *)(result + 0x4);
        result = 0;
        a3 = (uint32_t)((a3) - ((uint32_t)(result)));
    }
    if ((uint32_t)(a3) != 0) goto loc_009755E8;
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    goto loc_0097563B;
loc_009755E8:
    local_r12 = 0;
    if ((*(uint16_t *)(result + 0x2)) == 0) goto loc_0097563B;
loc_009755F6:
    result = wcschr(result + 2, 44, a3, a4);
    if (result == 0) goto loc_00975615;
    *(uint16_t *)(result) = 0;
    local_rbx = (result) + (2);
    goto loc_00975627;
loc_00975615:
    result = (result) | (-1);
loc_00975619:
    result = (result) + 1;
    if ((*(uint16_t *)(result + 0x2 + result * 2)) != 0) goto loc_00975619;
loc_00975627:
    result = PiDevCfgGetDriverConfigurationKeyScope(result + 2, 44, a3, a4);
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(result)));
    if ((*(uint16_t *)(result + 0x2 + result * 2)) != 0) goto loc_009755F6;
loc_0097563B:
    v_stack_m58 = v_stack_p18;
    result = PiDevCfgQueryIncludedDriverNode(v_stack_p10, local_r13, local_rdi, (uint32_t)((uint32_t)(local_r14)));
    if (sign_flag) goto loc_009757E7;
    if ((*(uint64_t *)(arg1 + 0x180)) == (Arg1 + 384)) goto loc_009756E1;
loc_00975673:
    result = RtlEqualUnicodeString(*(uint64_t *)(arg1 + 0x180) + 88, v_stack_p18 + 88, 1, (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) == 0) goto loc_009756A0;
    result = RtlEqualUnicodeString(*(uint64_t *)(arg1 + 0x180) + 40, v_stack_p18 + 40, 1, (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) != 0) goto loc_009756AC;
loc_009756A0:
    local_r13 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x180))) != (Arg1 + 384)) goto loc_00975673;
loc_009756AC:
    if (0 == 0) goto loc_009756E1;
    result = PiDevCfgFreeDriverNode(v_stack_p18, v_stack_p18 + 40, 1, (uint32_t)((uint32_t)(local_r14)));
    local_r14 = 0;
loc_009756C0:
loc_009756C6:
    result = (result) | (-1);
loc_009756CA:
    result = (result) + 1;
    if ((*(uint16_t *)(result + 0x2 + result * 2 + result * 2)) != 0) goto loc_009756CA;
    local_rsi = (result + 2 + result * 2 + result * 2) + (2);
    goto loc_00975548;
loc_009756E1:
    if ((*(uint64_t *)(*(uint64_t *)(local_r14 + 0x8))) != 0) goto loc_00975822;
    *(uint64_t *)(v_stack_p18) = 0;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)(local_r14 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x8)) = v_stack_p18;
    *(uint64_t *)(local_r14 + 0x8) = v_stack_p18;
    result = PiDevCfgQueryDriverConfiguration(v_stack_p18, v_stack_p18 + 40, 1, (uint32_t)((uint32_t)(local_r14)));
    local_r14 = 0;
    if (sign_flag) goto loc_009757EE;
    if ((*(uint64_t *)(v_stack_p18 + 0x128)) == 0) goto loc_0097573E;
    if ((*(uint64_t *)(v_stack_p8 + 0x128)) != 0) goto loc_0097573E;
    result = PnpDuplicateUnicodeString(v_stack_p8 + 288, v_stack_p18 + 288, 1, (uint32_t)((uint32_t)(local_r14)));
    if ((uint8_t)(result) == 0) goto loc_009757E0;
loc_0097573E:
    if ((*(uint64_t *)(v_stack_p18 + 0x138)) == 0) goto loc_00975769;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 304, a2, v_stack_p18 + 304, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975769:
    if ((*(uint64_t *)(v_stack_p18 + 0x148)) == 0) goto loc_00975790;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 320, a2, v_stack_p18 + 320, a4);
    if (sign_flag) goto loc_009757EE;
loc_00975790:
    if ((*(uint64_t *)(v_stack_p18 + 0x158)) == 0) goto loc_009757B7;
    a4 = 0;
    a2 = 0;
    result = PiDevCfgAppendMultiSz(v_stack_p8 + 336, a2, v_stack_p18 + 336, a4);
    if (sign_flag) goto loc_009757EE;
loc_009757B7:
    result = PiDevCfgPushDriverNodeEntry(v_stack_m48, v_stack_p18, v_stack_p18 + 336, a4);
    if (!sign_flag) goto loc_009756C0;
    goto loc_009757EE;
loc_009757CF:
    local_r14 = 0;
    goto loc_009756C6;
loc_009757D7:
    if (sign_flag) goto loc_009757EE;
    goto loc_00975523;
loc_009757E0:
    goto loc_009757EE;
loc_009757E7:
    *(uint32_t *)(v_stack_p8 + 0x1BC) = (uint32_t)(result);
loc_009757EE:
    if (v_stack_m48 == v_stack_m48) goto loc_00975829;
    if ((*(uint64_t *)(v_stack_m40)) != v_stack_m48) goto loc_00975822;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m40 + 0x8))) != v_stack_m40) goto loc_00975822;
    v_stack_m40 = *(uint64_t *)(v_stack_m40 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m40 + 0x8)) = v_stack_m48;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m40, a2, v_stack_p18 + 336, a4);
    goto loc_009757EE;
loc_00975822:
loc_00975829:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x178` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009754BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
