# MmManagePartitionMoveMemory

- RVA: `0x0080E1F4`–`0x0080E487` (길이 `659` bytes)
- VA: `0x000000014080E1F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D9144`
- 디코드: `192`개 명령, `659/659` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0080E23F` → [KeGetIdealNodeNumberThread](../../text/49/KeGetIdealNodeNumberThread_function_00492A1C.md) (function, `0x00492A1C`)
- `0x0080E312` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (function, `0x004A0650`)
- `0x0080E356` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0080E3B0` → [MiFindSpecialPurposeMemoryTypeByPartition](MiFindSpecialPurposeMemoryTypeByPartition_function_0080F5D8.md) (function, `0x0080F5D8`)
- `0x0080E3DB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0080E3E4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0080E409` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0080E425` → [MiSpecialPurposeMemoryChangePrepare](MiSpecialPurposeMemoryChangePrepare_function_0080FED0.md) (function, `0x0080FED0`)
- `0x0080E44C` → [MiAllocatePartitionPhysicalPages](MiAllocatePartitionPhysicalPages_function_0080C9D4.md) (function, `0x0080C9D4`)
- `0x0080E466` → [MiSpecialPurposeMemoryTypeDereference](../81/MiSpecialPurposeMemoryTypeDereference_function_00810154.md) (function, `0x00810154`)
- `0x0080E47B` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- [NtManagePartition](../90/NtManagePartition_function_00902FC0.md) at `0x009032FB`

### Static image references
- `0x0080E249` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0080E32E` → RVA `0x00E38D00` (`.data`; read)
- `0x0080E34C` → RVA `0x00FD9AD0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x0080E23F` → [KeGetIdealNodeNumberThread](../../text/49/KeGetIdealNodeNumberThread_function_00492A1C.md) (`PAGE` → `.text`)
  - `0x0080E312` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (`PAGE` → `.text`)
  - `0x0080E3DB` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0080E3E4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0080E409` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0080E47B` → [PsDereferencePartition](../../text/34/PsDereferencePartition_function_00342E70.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080E1F4  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0080E1F9  55                              push rbp
0080E1FA  56                              push rsi
0080E1FB  57                              push rdi
0080E1FC  41 54                           push r12
0080E1FE  41 55                           push r13
0080E200  41 56                           push r14
0080E202  41 57                           push r15
0080E204  48 8B EC                        mov rbp, rsp
0080E207  48 83 EC 30                     sub rsp, 0x30
0080E20B  4C 8B 3A                        mov r15, qword ptr [rdx]
0080E20E  33 F6                           xor esi, esi
0080E210  49 8B 10                        mov rdx, qword ptr [r8]
0080E213  4D 8B E0                        mov r12, r8
0080E216  4C 8B 31                        mov r14, qword ptr [rcx]
0080E219  44 8B EE                        mov r13d, esi
0080E21C  48 89 75 48                     mov qword ptr [rbp + 0x48], rsi
0080E220  48 89 75 50                     mov qword ptr [rbp + 0x50], rsi
0080E224  48 85 D2                        test rdx, rdx
0080E227  75 04                           jne 0x14080e22d
0080E229  33 C0                           xor eax, eax
0080E22B  EB 5E                           jmp 0x14080e28b
0080E22D  41 8B 58 08                     mov ebx, dword ptr [r8 + 8]
0080E231  83 FB FF                        cmp ebx, -1
0080E234  75 13                           jne 0x14080e249
0080E236  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0080E23F  E8 D8 47 C8 FF                  call 0x140492a1c
0080E244  0F B7 D8                        movzx ebx, ax
0080E247  EB 0B                           jmp 0x14080e254
0080E249  0F B7 05 B0 6D 7B 00            movzx eax, word ptr [rip + 0x7b6db0]
0080E250  3B D8                           cmp ebx, eax
0080E252  73 32                           jae 0x14080e286
0080E254  41 8B 78 0C                     mov edi, dword ptr [r8 + 0xc]
0080E258  F7 C7 00 F0 FF FF               test edi, 0xfffff000
0080E25E  75 26                           jne 0x14080e286
0080E260  8B CF                           mov ecx, edi
0080E262  81 E1 00 04 00 00               and ecx, 0x400
0080E268  74 3A                           je 0x14080e2a4
0080E26A  4D 3B FE                        cmp r15, r14
0080E26D  75 17                           jne 0x14080e286
0080E26F  48 81 FA 00 00 04 00            cmp rdx, 0x40000
0080E276  75 0E                           jne 0x14080e286
0080E278  8B C7                           mov eax, edi
0080E27A  25 00 0A 00 00                  and eax, 0xa00
0080E27F  3D 00 08 00 00                  cmp eax, 0x800
0080E284  75 24                           jne 0x14080e2aa
0080E286  B8 0D 00 00 C0                  mov eax, 0xc000000d
0080E28B  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0080E293  48 83 C4 30                     add rsp, 0x30
0080E297  41 5F                           pop r15
0080E299  41 5E                           pop r14
0080E29B  41 5D                           pop r13
0080E29D  41 5C                           pop r12
0080E29F  5F                              pop rdi
0080E2A0  5E                              pop rsi
0080E2A1  5D                              pop rbp
0080E2A2  C3                              ret
0080E2A3  CC                              int3
0080E2A4  0F BA E7 0B                     bt edi, 0xb
0080E2A8  72 DC                           jb 0x14080e286
0080E2AA  44 8B C7                        mov r8d, edi
0080E2AD  41 BA 80 01 00 00               mov r10d, 0x180
0080E2B3  41 81 E0 00 02 00 00            and r8d, 0x200
0080E2BA  74 1B                           je 0x14080e2d7
0080E2BC  0F BA E7 08                     bt edi, 8
0080E2C0  73 C4                           jae 0x14080e286
0080E2C2  F7 C7 F6 F0 FF FF               test edi, 0xfffff0f6
0080E2C8  75 BC                           jne 0x14080e286
0080E2CA  B9 08 04 00 00                  mov ecx, 0x408
0080E2CF  8B C7                           mov eax, edi
0080E2D1  23 C1                           and eax, ecx
0080E2D3  3B C1                           cmp eax, ecx
0080E2D5  EB 0F                           jmp 0x14080e2e6
0080E2D7  85 C9                           test ecx, ecx
0080E2D9  74 0D                           je 0x14080e2e8
0080E2DB  F7 C7 7E FA FF FF               test edi, 0xfffffa7e
0080E2E1  75 A3                           jne 0x14080e286
0080E2E3  41 85 FA                        test r10d, edi
0080E2E6  74 9E                           je 0x14080e286
0080E2E8  40 F6 C7 12                     test dil, 0x12
0080E2EC  74 11                           je 0x14080e2ff
0080E2EE  F7 C7 E0 01 00 00               test edi, 0x1e0
0080E2F4  75 90                           jne 0x14080e286
0080E2F6  48 F7 C2 FF 01 00 00            test rdx, 0x1ff
0080E2FD  EB 23                           jmp 0x14080e322
0080E2FF  8B C7                           mov eax, edi
0080E301  41 23 C2                        and eax, r10d
0080E304  40 F6 C7 60                     test dil, 0x60
0080E308  74 04                           je 0x14080e30e
0080E30A  85 C0                           test eax, eax
0080E30C  EB E6                           jmp 0x14080e2f4
0080E30E  85 C0                           test eax, eax
0080E310  74 16                           je 0x14080e328
0080E312  E8 39 23 C9 FF                  call 0x1404a0650
0080E317  85 C0                           test eax, eax
0080E319  74 77                           je 0x14080e392
0080E31B  48 F7 C2 FF FF 03 00            test rdx, 0x3ffff
0080E322  0F 85 5E FF FF FF               jne 0x14080e286
0080E328  40 F6 C7 08                     test dil, 8
0080E32C  74 3B                           je 0x14080e369
0080E32E  48 8D 05 CB A9 62 00            lea rax, [rip + 0x62a9cb]
0080E335  4C 3B F0                        cmp r14, rax
0080E338  0F 85 48 FF FF FF               jne 0x14080e286
0080E33E  4C 3B F8                        cmp r15, rax
0080E341  75 09                           jne 0x14080e34c
0080E343  45 85 C0                        test r8d, r8d
0080E346  0F 84 3A FF FF FF               je 0x14080e286
0080E34C  48 8B 0D 7D B7 7C 00            mov rcx, qword ptr [rip + 0x7cb77d]
0080E353  41 8A D1                        mov dl, r9b
0080E356  E8 C5 3A 06 00                  call 0x140871e20
0080E35B  84 C0                           test al, al
0080E35D  75 0A                           jne 0x14080e369
0080E35F  B8 61 00 00 C0                  mov eax, 0xc0000061
0080E364  E9 22 FF FF FF                  jmp 0x14080e28b
0080E369  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0080E36D  84 C0                           test al, al
0080E36F  79 0D                           jns 0x14080e37e
0080E371  4D 3B F7                        cmp r14, r15
0080E374  75 1C                           jne 0x14080e392
0080E376  F7 C7 00 0C 00 00               test edi, 0xc00
0080E37C  74 14                           je 0x14080e392
0080E37E  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0080E382  84 C0                           test al, al
0080E384  0F 89 B1 00 00 00               jns 0x14080e43b
0080E38A  F7 C7 08 F0 FF FF               test edi, 0xfffff008
0080E390  74 0A                           je 0x14080e39c
0080E392  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0080E397  E9 EF FE FF FF                  jmp 0x14080e28b
0080E39C  4D 3B F7                        cmp r14, r15
0080E39F  75 76                           jne 0x14080e417
0080E3A1  4C 8D 45 40                     lea r8, [rbp + 0x40]
0080E3A5  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
0080E3A9  48 8D 55 50                     lea rdx, [rbp + 0x50]
0080E3AD  49 8B CE                        mov rcx, r14
0080E3B0  E8 23 12 00 00                  call 0x14080f5d8
0080E3B5  48 85 C0                        test rax, rax
0080E3B8  75 0A                           jne 0x14080e3c4
0080E3BA  BE A0 04 00 C0                  mov esi, 0xc00004a0
0080E3BF  E9 A7 00 00 00                  jmp 0x14080e46b
0080E3C4  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0080E3C8  48 83 C8 FF                     or rax, 0xffffffffffffffff
0080E3CC  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0080E3D1  24 06                           and al, 6
0080E3D3  3C 02                           cmp al, 2
0080E3D5  75 09                           jne 0x14080e3e0
0080E3D7  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0080E3DB  E8 F0 79 A5 FF                  call 0x140265dd0
0080E3E0  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0080E3E4  E8 17 32 AD FF                  call 0x1402e1600
0080E3E9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0080E3F2  90                              nop
0080E3F3  66 83 80 E6 01 00 00 01         add word ptr [rax + 0x1e6], 1
0080E3FB  75 11                           jne 0x14080e40e
0080E3FD  48 05 98 00 00 00               add rax, 0x98
0080E403  90                              nop
0080E404  48 39 00                        cmp qword ptr [rax], rax
0080E407  74 05                           je 0x14080e40e
0080E409  E8 72 48 AD FF                  call 0x1402e2c80
0080E40E  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
0080E412  4D 3B F7                        cmp r14, r15
0080E415  74 24                           je 0x14080e43b
0080E417  49 8D 97 E8 44 00 00            lea rdx, [r15 + 0x44e8]
0080E41E  49 8B CE                        mov rcx, r14
0080E421  4C 8D 45 48                     lea r8, [rbp + 0x48]
0080E425  E8 A6 1A 00 00                  call 0x14080fed0
0080E42A  8B F0                           mov esi, eax
0080E42C  85 C0                           test eax, eax
0080E42E  78 2A                           js 0x14080e45a
0080E430  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0080E434  4D 8B EE                        mov r13, r14
0080E437  4C 8B 70 40                     mov r14, qword ptr [rax + 0x40]
0080E43B  4D 8B 04 24                     mov r8, qword ptr [r12]
0080E43F  44 8B CB                        mov r9d, ebx
0080E442  49 8B D6                        mov rdx, r14
0080E445  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0080E449  49 8B CF                        mov rcx, r15
0080E44C  E8 83 E5 FF FF                  call 0x14080c9d4
0080E451  8B F0                           mov esi, eax
0080E453  3D 09 07 00 C0                  cmp eax, 0xc0000709
0080E458  74 E1                           je 0x14080e43b
0080E45A  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0080E45E  48 85 D2                        test rdx, rdx
0080E461  74 08                           je 0x14080e46b
0080E463  49 8B CD                        mov rcx, r13
0080E466  E8 E9 1C 00 00                  call 0x140810154
0080E46B  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0080E46F  48 85 C9                        test rcx, rcx
0080E472  74 0C                           je 0x14080e480
0080E474  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0080E47B  E8 F0 49 B3 FF                  call 0x140342e70
0080E480  8B C6                           mov eax, esi
0080E482  E9 04 FE FF FF                  jmp 0x14080e28b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmManagePartitionMoveMemory(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rsi = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    if (*(unsigned __int64 *)(a3) != 0) goto loc_0080E22D;
    result = 0;
    goto loc_0080E28B;
loc_0080E22D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)))) != -1) goto loc_0080E249;
    result = KeGetIdealNodeNumberThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a3), a3, a4);
    goto loc_0080E254;
loc_0080E249:
    if (((unsigned int)((unsigned __int16)(result))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 8089008)))) goto loc_0080E286;
loc_0080E254:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (0xFFFFF000ULL)) != 0) goto loc_0080E286;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) & (0x400ULL));
    if (condition_is_equal) goto loc_0080E2A4;
    if ((*(unsigned __int64 *)(a2)) != (*(unsigned __int64 *)(a1))) goto loc_0080E286;
    if ((*(unsigned __int64 *)(a3)) != 0x40000ULL) goto loc_0080E286;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) & (0xA00ULL));
    if (((unsigned int)(result)) != 0x800ULL) goto loc_0080E2AA;
loc_0080E286:
loc_0080E28B:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(0xC000000DULL);
loc_0080E2A4:
    if (condition_is_below) goto loc_0080E286;
loc_0080E2AA:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) & (512));
    if (condition_is_equal) goto loc_0080E2D7;
    if (condition_is_above_or_equal) goto loc_0080E286;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (0xFFFFF0F6ULL)) != 0) goto loc_0080E286;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) & ((unsigned int)((unsigned int)(0x408ULL))));
    goto loc_0080E2E6;
loc_0080E2D7:
    if ((unsigned int)((unsigned int)(0x408ULL)) == 0) goto loc_0080E2E8;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (0xFFFFFA7EULL)) != 0) goto loc_0080E286;
loc_0080E2E6:
    if (((384) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) == 0) goto loc_0080E286;
loc_0080E2E8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (18)) == 0) goto loc_0080E2FF;
loc_0080E2F4:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (480)) != 0) goto loc_0080E286;
    goto loc_0080E322;
loc_0080E2FF:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) & (384));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (96)) == 0) goto loc_0080E30E;
    goto loc_0080E2F4;
loc_0080E30E:
    if ((unsigned int)(result) == 0) goto loc_0080E328;
    result = MiHugePagesSupported((unsigned int)(0x408ULL), *(unsigned __int64 *)(a3), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0080E392;
loc_0080E322:
    if (((*(unsigned __int64 *)(a3)) & (0x3FFFFULL)) != 0) goto loc_0080E286;
loc_0080E328:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (8)) == 0) goto loc_0080E369;
    if ((*(unsigned __int64 *)(a1)) != (v_rip + 6465995)) goto loc_0080E286;
    if ((*(unsigned __int64 *)(a2)) != (v_rip + 6465995)) goto loc_0080E34C;
    if ((unsigned int)(a3) == 0) goto loc_0080E286;
loc_0080E34C:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8173437), a4, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0080E369;
    goto loc_0080E28B;
loc_0080E369:
    if (!sign_flag) goto loc_0080E37E;
    if ((*(unsigned __int64 *)(a1)) != (*(unsigned __int64 *)(a2))) goto loc_0080E392;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (0xC00ULL)) == 0) goto loc_0080E392;
loc_0080E37E:
    if (!sign_flag) goto loc_0080E43B;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (0xFFFFF008ULL)) == 0) goto loc_0080E39C;
loc_0080E392:
    goto loc_0080E28B;
loc_0080E39C:
    if ((*(unsigned __int64 *)(a1)) != (*(unsigned __int64 *)(a2))) goto loc_0080E417;
    v_stack_p8 = 0;
    result = MiFindSpecialPurposeMemoryTypeByPartition(*(unsigned __int64 *)(a1), v_stack_p18, v_stack_p8, a4);
    if (result != 0) goto loc_0080E3C4;
    goto loc_0080E46B;
loc_0080E3C4:
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_stack_p8;
        result = ExfTryToWakePushLock(a1, v_stack_p18, v_stack_p8, a4);
    }
    result = KeAbPostRelease(v_stack_p8, v_stack_p18, v_stack_p8, a4);
    if (((unsigned __int8)(result)) != 2) goto loc_0080E40E;
    result = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (152);
    if ((*(unsigned __int64 *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(v_stack_p8, v_stack_p18, v_stack_p8, a4);
    }
    if (v_stack_p18 == (*(unsigned __int64 *)(a2))) goto loc_0080E43B;
loc_0080E417:
    result = MiSpecialPurposeMemoryChangePrepare(v_stack_p18, *(unsigned __int64 *)(a2) + 17640, v_stack_p10, a4);
    if (sign_flag) goto loc_0080E45A;
loc_0080E43B:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)));
    result = MiAllocatePartitionPhysicalPages(*(unsigned __int64 *)(a2), *(unsigned __int64 *)(v_stack_p10 + 64), *(unsigned __int64 *)(a3), (unsigned int)((unsigned int)(v_stack_p20)));
    if (((unsigned int)(result)) == 0xC0000709ULL) goto loc_0080E43B;
loc_0080E45A:
    if (v_stack_p10 != 0) {
        a1 = v_stack_p18;
        result = MiSpecialPurposeMemoryTypeDereference(a1, v_stack_p10, *(unsigned __int64 *)(a3), (unsigned int)((unsigned int)(v_stack_p20)));
    }
    if (v_stack_p18 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p18 + 184);
        result = PsDereferencePartition(a1, v_stack_p10, *(unsigned __int64 *)(a3), (unsigned int)((unsigned int)(v_stack_p20)));
    }
    goto loc_0080E28B;
}
```

## 5. (Beta) C Style

```c
int64_t MmManagePartitionMoveMemory(void *Arg1, void *Arg2, void *Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rsi = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    if (*(uint64_t *)(arg3) != 0) goto loc_0080E22D;
    result = 0;
    goto loc_0080E28B;
loc_0080E22D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) != -1) goto loc_0080E249;
    result = KeGetIdealNodeNumberThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg3), Arg3, Arg4);
    goto loc_0080E254;
loc_0080E249:
    if (((uint32_t)((uint16_t)(result))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0x7B6DB0)))) goto loc_0080E286;
loc_0080E254:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (0xFFFFF000ULL)) != 0) goto loc_0080E286;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) & (0x400ULL));
    if (condition_is_equal) goto loc_0080E2A4;
    if ((*(uint64_t *)(arg2)) != (*(uint64_t *)(arg1))) goto loc_0080E286;
    if ((*(uint64_t *)(arg3)) != 0x40000ULL) goto loc_0080E286;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) & (0xA00ULL));
    if (((uint32_t)(result)) != 0x800ULL) goto loc_0080E2AA;
loc_0080E286:
loc_0080E28B:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(0xC000000DULL);
loc_0080E2A4:
    if (condition_is_below) goto loc_0080E286;
loc_0080E2AA:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) & (512));
    if (condition_is_equal) goto loc_0080E2D7;
    if (condition_is_above_or_equal) goto loc_0080E286;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (0xFFFFF0F6ULL)) != 0) goto loc_0080E286;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) & ((uint32_t)((uint32_t)(0x408ULL))));
    goto loc_0080E2E6;
loc_0080E2D7:
    if ((uint32_t)((uint32_t)(0x408ULL)) == 0) goto loc_0080E2E8;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (0xFFFFFA7EULL)) != 0) goto loc_0080E286;
loc_0080E2E6:
    if (((384) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) == 0) goto loc_0080E286;
loc_0080E2E8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (18)) == 0) goto loc_0080E2FF;
loc_0080E2F4:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (480)) != 0) goto loc_0080E286;
    goto loc_0080E322;
loc_0080E2FF:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))))) & (384));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (96)) == 0) goto loc_0080E30E;
    goto loc_0080E2F4;
loc_0080E30E:
    if ((uint32_t)(result) == 0) goto loc_0080E328;
    result = MiHugePagesSupported((uint32_t)(0x408ULL), *(uint64_t *)(arg3), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0080E392;
loc_0080E322:
    if (((*(uint64_t *)(arg3)) & (0x3FFFFULL)) != 0) goto loc_0080E286;
loc_0080E328:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (8)) == 0) goto loc_0080E369;
    if ((*(uint64_t *)(arg1)) != (v_rip + 6465995)) goto loc_0080E286;
    if ((*(uint64_t *)(arg2)) != (v_rip + 6465995)) goto loc_0080E34C;
    if ((uint32_t)(Arg3) == 0) goto loc_0080E286;
loc_0080E34C:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x7CB77D), Arg4, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0080E369;
    goto loc_0080E28B;
loc_0080E369:
    if (!sign_flag) goto loc_0080E37E;
    if ((*(uint64_t *)(arg1)) != (*(uint64_t *)(arg2))) goto loc_0080E392;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (0xC00ULL)) == 0) goto loc_0080E392;
loc_0080E37E:
    if (!sign_flag) goto loc_0080E43B;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) & (0xFFFFF008ULL)) == 0) goto loc_0080E39C;
loc_0080E392:
    goto loc_0080E28B;
loc_0080E39C:
    if ((*(uint64_t *)(arg1)) != (*(uint64_t *)(arg2))) goto loc_0080E417;
    v_stack_p8 = 0;
    result = MiFindSpecialPurposeMemoryTypeByPartition(*(uint64_t *)(arg1), v_stack_p18, v_stack_p8, Arg4);
    if (result != 0) goto loc_0080E3C4;
    goto loc_0080E46B;
loc_0080E3C4:
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_stack_p8;
        result = ExfTryToWakePushLock(Arg1, v_stack_p18, v_stack_p8, Arg4);
    }
    result = KeAbPostRelease(v_stack_p8, v_stack_p18, v_stack_p8, Arg4);
    if (((uint8_t)(result)) != 2) goto loc_0080E40E;
    result = (*(uint64_t *)(gs_base + (0 + 0x188))) + (152);
    if ((*(uint64_t *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(v_stack_p8, v_stack_p18, v_stack_p8, Arg4);
    }
    if (v_stack_p18 == (*(uint64_t *)(arg2))) goto loc_0080E43B;
loc_0080E417:
    result = MiSpecialPurposeMemoryChangePrepare(v_stack_p18, *(uint64_t *)(arg2) + 17640, v_stack_p10, Arg4);
    if (sign_flag) goto loc_0080E45A;
loc_0080E43B:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)));
    result = MiAllocatePartitionPhysicalPages(*(uint64_t *)(arg2), *(uint64_t *)(v_stack_p10 + 0x40), *(uint64_t *)(arg3), (uint32_t)((uint32_t)(v_stack_p20)));
    if (((uint32_t)(result)) == 0xC0000709ULL) goto loc_0080E43B;
loc_0080E45A:
    if (v_stack_p10 != 0) {
        Arg1 = v_stack_p18;
        result = MiSpecialPurposeMemoryTypeDereference(Arg1, v_stack_p10, *(uint64_t *)(arg3), (uint32_t)((uint32_t)(v_stack_p20)));
    }
    if (v_stack_p18 != 0) {
        Arg1 = *(uint64_t *)(v_stack_p18 + 0xB8);
        result = PsDereferencePartition(Arg1, v_stack_p10, *(uint64_t *)(arg3), (uint32_t)((uint32_t)(v_stack_p20)));
    }
    goto loc_0080E28B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080E1F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
