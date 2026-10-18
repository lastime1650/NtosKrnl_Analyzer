# MiUpdatePfnForPrefetchByPte

- RVA: `0x00321210`–`0x0032160E` (길이 `1,022` bytes)
- VA: `0x0000000140321210`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000756CC`
- 디코드: `252`개 명령, `1,022/1,022` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0032124C` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032127B` → [MiSafeLockPage](MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x003212E7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032132F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00321345` → [MiGetPfnPriority](MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x00321389` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003213D2` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x003213EC` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x003214CA` → [MiRelinkStandbyPage](../2B/MiRelinkStandbyPage_function_002B9D30.md) (function, `0x002B9D30`)
- `0x003214E4` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0032151F` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0032158D` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x003215D9` → [MiSetActivePfnHeat](../40/MiSetActivePfnHeat_function_00409E00.md) (function, `0x00409E00`)
- `0x00321604` → [MiAddPageToHeatList](../44/MiAddPageToHeatList_function_0044603C.md) (function, `0x0044603C`)

### Direct callers
- [MiSystemFault](../34/MiSystemFault_function_0034AA64.md) at `0x0034B093`
- [MiPfPrepareReadList](../../page/93/MiPfPrepareReadList_function_0093CD5C.md) at `0x0093CFF6`
- [MiPfPrepareSequentialReadList](../../page/93/MiPfPrepareSequentialReadList_function_0093D8E8.md) at `0x0093DE37`

### Static image references
- `0x0032131E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003213F5` → RVA `0x00E2DC80` (`.data`; read)
- `0x0032146B` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00321210  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00321215  53                              push rbx
00321216  55                              push rbp
00321217  57                              push rdi
00321218  41 54                           push r12
0032121A  41 55                           push r13
0032121C  41 57                           push r15
0032121E  48 83 EC 28                     sub rsp, 0x28
00321222  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00321227  44 8B E2                        mov r12d, edx
0032122A  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0032122F  48 8B E9                        mov rbp, rcx
00321232  45 33 ED                        xor r13d, r13d
00321235  49 BF FF FF FF FF FF 00 00 00   movabs r15, 0xffffffffff
0032123F  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
00321249  48 8B CD                        mov rcx, rbp
0032124C  E8 4F 16 F6 FF                  call 0x1402828a0
00321251  48 8B D8                        mov rbx, rax
00321254  A8 01                           test al, 1
00321256  0F 84 80 01 00 00               je 0x1403213dc
0032125C  41 BE 06 00 00 00               mov r14d, 6
00321262  48 8B C8                        mov rcx, rax
00321265  48 C1 E9 0C                     shr rcx, 0xc
00321269  49 23 CF                        and rcx, r15
0032126C  4C 8D 3C 49                     lea r15, [rcx + rcx*2]
00321270  49 C1 E7 04                     shl r15, 4
00321274  48 8B C7                        mov rax, rdi
00321277  49 8D 3C 07                     lea rdi, [r15 + rax]
0032127B  E8 A0 03 00 00                  call 0x140321620
00321280  0F B6 F0                        movzx esi, al
00321283  40 80 FE 11                     cmp sil, 0x11
00321287  0F 84 0E 01 00 00               je 0x14032139b
0032128D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00321291  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0032129B  48 0B C8                        or rcx, rax
0032129E  48 3B CD                        cmp rcx, rbp
003212A1  0F 85 2D 02 00 00               jne 0x1403214d4
003212A7  0F B6 47 22                     movzx eax, byte ptr [rdi + 0x22]
003212AB  24 07                           and al, 7
003212AD  41 83 FE 06                     cmp r14d, 6
003212B1  0F 85 FD 00 00 00               jne 0x1403213b4
003212B7  41 3A C6                        cmp al, r14b
003212BA  0F 85 58 02 00 00               jne 0x140321518
003212C0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003212CA  48 8B C0                        mov rax, rax
003212CD  48 3B E8                        cmp rbp, rax
003212D0  72 6B                           jb 0x14032133d
003212D2  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
003212DC  48 8B C0                        mov rax, rax
003212DF  48 3B E8                        cmp rbp, rax
003212E2  77 59                           ja 0x14032133d
003212E4  48 8B CD                        mov rcx, rbp
003212E7  E8 B4 15 F6 FF                  call 0x1402828a0
003212EC  48 3B D8                        cmp rbx, rax
003212EF  74 4C                           je 0x14032133d
003212F1  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003212FB  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00321300  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
0032130A  49 BF FF FF FF FF FF 00 00 00   movabs r15, 0xffffffffff
00321314  40 80 FE 02                     cmp sil, 2
00321318  0F 83 2B FF FF FF               jae 0x140321249
0032131E  44 39 2D FB 59 CA 00            cmp dword ptr [rip + 0xca59fb], r13d
00321325  74 0D                           je 0x140321334
00321327  44 0F 20 C1                     mov rcx, cr8
0032132B  40 0F B6 D6                     movzx edx, sil
0032132F  E8 64 43 1D 00                  call 0x1404f5698
00321334  44 0F 22 C6                     mov cr8, rsi
00321338  E9 02 FF FF FF                  jmp 0x14032123f
0032133D  48 85 FF                        test rdi, rdi
00321340  74 59                           je 0x14032139b
00321342  48 8B CF                        mov rcx, rdi
00321345  E8 A6 13 00 00                  call 0x1403226f0
0032134A  44 3B E0                        cmp r12d, eax
0032134D  74 06                           je 0x140321355
0032134F  0F 83 CB 00 00 00               jae 0x140321420
00321355  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0032135A  48 85 DB                        test rbx, rbx
0032135D  0F 85 3D 02 00 00               jne 0x1403215a0
00321363  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032136D  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00321372  40 80 FE 02                     cmp sil, 2
00321376  73 1A                           jae 0x140321392
00321378  83 3D A1 59 CA 00 00            cmp dword ptr [rip + 0xca59a1], 0
0032137F  74 0D                           je 0x14032138e
00321381  44 0F 20 C1                     mov rcx, cr8
00321385  40 0F B6 D6                     movzx edx, sil
00321389  E8 0A 43 1D 00                  call 0x1404f5698
0032138E  44 0F 22 C6                     mov cr8, rsi
00321392  45 85 ED                        test r13d, r13d
00321395  0F 85 4E 02 00 00               jne 0x1403215e9
0032139B  4C 8B 74 24 20                  mov r14, qword ptr [rsp + 0x20]
003213A0  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
003213A5  48 83 C4 28                     add rsp, 0x28
003213A9  41 5F                           pop r15
003213AB  41 5D                           pop r13
003213AD  41 5C                           pop r12
003213AF  5F                              pop rdi
003213B0  5D                              pop rbp
003213B1  5B                              pop rbx
003213B2  C3                              ret
003213B3  CC                              int3
003213B4  3C 02                           cmp al, 2
003213B6  72 13                           jb 0x1403213cb
003213B8  3C 04                           cmp al, 4
003213BA  77 0F                           ja 0x1403213cb
003213BC  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003213C0  48 0F BA E0 3E                  bt rax, 0x3e
003213C5  0F 83 F5 FE FF FF               jae 0x1403212c0
003213CB  40 0F B6 D6                     movzx edx, sil
003213CF  48 8B CF                        mov rcx, rdi
003213D2  E8 09 90 FF FF                  call 0x14031a3e0
003213D7  E9 59 FE FF FF                  jmp 0x140321235
003213DC  25 00 0C 00 00                  and eax, 0xc00
003213E1  48 3D 00 08 00 00               cmp rax, 0x800
003213E7  75 B2                           jne 0x14032139b
003213E9  48 8B CB                        mov rcx, rbx
003213EC  E8 1F 16 05 00                  call 0x140372a10
003213F1  85 C0                           test eax, eax
003213F3  74 A6                           je 0x14032139b
003213F5  48 8B 05 84 C8 B0 00            mov rax, qword ptr [rip + 0xb0c884]
003213FC  48 85 C0                        test rax, rax
003213FF  74 0E                           je 0x14032140f
00321401  F6 C3 10                        test bl, 0x10
00321404  75 14                           jne 0x14032141a
00321406  48 8B C8                        mov rcx, rax
00321409  48 F7 D1                        not rcx
0032140C  48 23 CB                        and rcx, rbx
0032140F  41 BE 02 00 00 00               mov r14d, 2
00321415  E9 4B FE FF FF                  jmp 0x140321265
0032141A  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0032141E  EB EF                           jmp 0x14032140f
00321420  0F B6 4F 22                     movzx ecx, byte ptr [rdi + 0x22]
00321424  80 E1 07                        and cl, 7
00321427  80 F9 02                        cmp cl, 2
0032142A  74 2D                           je 0x140321459
0032142C  80 F9 06                        cmp cl, 6
0032142F  75 04                           jne 0x140321435
00321431  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00321435  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00321438  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0032143C  C1 E9 18                        shr ecx, 0x18
0032143F  0F B6 C1                        movzx eax, cl
00321442  41 32 C4                        xor al, r12b
00321445  24 07                           and al, 7
00321447  32 C1                           xor al, cl
00321449  88 44 24 7B                     mov byte ptr [rsp + 0x7b], al
0032144D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00321451  89 47 20                        mov dword ptr [rdi + 0x20], eax
00321454  E9 FC FE FF FF                  jmp 0x140321355
00321459  85 C0                           test eax, eax
0032145B  75 67                           jne 0x1403214c4
0032145D  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00321460  48 0F BA E0 0A                  bt rax, 0xa
00321465  72 5D                           jb 0x1403214c4
00321467  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0032146B  48 8B 0D 16 EC B0 00            mov rcx, qword ptr [rip + 0xb0ec16]
00321472  48 C1 E8 2B                     shr rax, 0x2b
00321476  25 FF 03 00 00                  and eax, 0x3ff
0032147B  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0032147F  8B 40 04                        mov eax, dword ptr [rax + 4]
00321482  84 C0                           test al, al
00321484  78 3E                           js 0x1403214c4
00321486  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0032148A  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0032148E  0F B6 D0                        movzx edx, al
00321491  C0 EA 02                        shr dl, 2
00321494  F6 C2 01                        test dl, 1
00321497  74 2B                           je 0x1403214c4
00321499  48 8B 15 E8 EB B0 00            mov rdx, qword ptr [rip + 0xb0ebe8]
003214A0  48 C1 E9 2B                     shr rcx, 0x2b
003214A4  81 E1 FF 03 00 00               and ecx, 0x3ff
003214AA  48 C1 E8 0C                     shr rax, 0xc
003214AE  83 E0 0F                        and eax, 0xf
003214B1  4C 8B 04 CA                     mov r8, qword ptr [rdx + rcx*8]
003214B5  41 8B 88 B4 04 00 00            mov ecx, dword ptr [r8 + 0x4b4]
003214BC  3B C1                           cmp eax, ecx
003214BE  0F 84 91 FE FF FF               je 0x140321355
003214C4  41 8B D4                        mov edx, r12d
003214C7  48 8B CF                        mov rcx, rdi
003214CA  E8 61 88 F9 FF                  call 0x1402b9d30
003214CF  E9 81 FE FF FF                  jmp 0x140321355
003214D4  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
003214D8  48 85 C9                        test rcx, rcx
003214DB  78 11                           js 0x1403214ee
003214DD  40 0F B6 D6                     movzx edx, sil
003214E1  48 8B CF                        mov rcx, rdi
003214E4  E8 F7 8E FF FF                  call 0x14031a3e0
003214E9  E9 AD FE FF FF                  jmp 0x14032139b
003214EE  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003214F8  48 8B C0                        mov rax, rax
003214FB  48 3B E8                        cmp rbp, rax
003214FE  72 DD                           jb 0x1403214dd
00321500  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0032150A  48 8B C0                        mov rax, rax
0032150D  48 3B E8                        cmp rbp, rax
00321510  0F 86 91 FD FF FF               jbe 0x1403212a7
00321516  EB C5                           jmp 0x1403214dd
00321518  40 0F B6 D6                     movzx edx, sil
0032151C  48 8B CF                        mov rcx, rdi
0032151F  E8 BC 8E FF FF                  call 0x14031a3e0
00321524  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
0032152E  49 8B C6                        mov rax, r14
00321531  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
0032153B  49 BF FF FF FF FF FF 00 00 00   movabs r15, 0xffffffffff
00321545  48 3B E8                        cmp rbp, rax
00321548  0F 82 FB FC FF FF               jb 0x140321249
0032154E  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
00321558  48 8B C2                        mov rax, rdx
0032155B  48 3B E8                        cmp rbp, rax
0032155E  0F 87 E5 FC FF FF               ja 0x140321249
00321564  48 8B CD                        mov rcx, rbp
00321567  48 C1 E1 19                     shl rcx, 0x19
0032156B  49 8B C6                        mov rax, r14
0032156E  48 C1 E0 19                     shl rax, 0x19
00321572  48 2B C8                        sub rcx, rax
00321575  48 C1 F9 10                     sar rcx, 0x10
00321579  49 8B C6                        mov rax, r14
0032157C  48 3B C8                        cmp rcx, rax
0032157F  72 0C                           jb 0x14032158d
00321581  48 8B C2                        mov rax, rdx
00321584  48 3B C8                        cmp rcx, rax
00321587  0F 86 BC FC FF FF               jbe 0x140321249
0032158D  E8 EE D6 F6 FF                  call 0x14028ec80
00321592  83 F8 08                        cmp eax, 8
00321595  0F 84 00 FE FF FF               je 0x14032139b
0032159B  E9 95 FC FF FF                  jmp 0x140321235
003215A0  0F B6 47 22                     movzx eax, byte ptr [rdi + 0x22]
003215A4  24 07                           and al, 7
003215A6  3C 02                           cmp al, 2
003215A8  0F 85 B5 FD FF FF               jne 0x140321363
003215AE  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003215B2  48 8B D0                        mov rdx, rax
003215B5  48 8B C8                        mov rcx, rax
003215B8  48 C1 E9 0B                     shr rcx, 0xb
003215BC  81 E2 00 04 00 00               and edx, 0x400
003215C2  48 C1 E8 03                     shr rax, 3
003215C6  48 85 D2                        test rdx, rdx
003215C9  0F 45 C1                        cmovne eax, ecx
003215CC  A8 01                           test al, 1
003215CE  0F 84 8F FD FF FF               je 0x140321363
003215D4  33 D2                           xor edx, edx
003215D6  48 8B CF                        mov rcx, rdi
003215D9  E8 22 88 0E 00                  call 0x140409e00
003215DE  41 BD 01 00 00 00               mov r13d, 1
003215E4  E9 7A FD FF FF                  jmp 0x140321363
003215E9  49 C1 FF 04                     sar r15, 4
003215ED  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
003215F7  49 0F AF D7                     imul rdx, r15
003215FB  41 B8 03 00 00 00               mov r8d, 3
00321601  48 8B CB                        mov rcx, rbx
00321604  E8 33 4A 12 00                  call 0x14044603c
00321609  E9 8D FD FF FF                  jmp 0x14032139b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdatePfnForPrefetchByPte(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p78;
    unsigned __int8 v_stack_p7B;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (40);
    v_stack_p8 = v_rsi;
    v_stack_m38 = v_r14;
    v_r13 = 0;
loc_00321235:
loc_0032123F:
loc_00321249:
    result = MI_READ_PTE_LOCK_FREE(a1, a2, a3, a4);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_003213DC;
loc_00321265:
    a1 = (result) >> (12);
    a1 = (a1) & (v_r15);
    v_r15 = (a1 + a1 * 2) << (4);
    result = MiSafeLockPage(a1, a2, a3, a4);
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_0032139B;
    a1 = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 8)) | (result);
    if (a1 != a1) goto loc_003214D4;
loc_003212A7:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + v_rdi * 1 + 34)) & (7));
    if (6 != 6) goto loc_003213B4;
    if (((unsigned __int8)(result)) != 6) goto loc_00321518;
loc_003212C0:
    if (a1 < result) goto loc_0032133D;
    if (a1 > result) goto loc_0032133D;
    result = MI_READ_PTE_LOCK_FREE(a1, a2, a3, a4);
    if (result == result) goto loc_0032133D;
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_00321249;
    if ((*(unsigned int *)(v_rip + 13261307)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_0032123F;
loc_0032133D:
    if (v_r15 + v_rdi * 1 == 0) goto loc_0032139B;
    result = MiGetPfnPriority(v_r15 + v_rdi * 1, a2, a3, a4);
    if (((unsigned int)((unsigned int)(a2))) == ((unsigned int)(result))) goto loc_00321355;
    if (((unsigned int)((unsigned int)(a2))) >= ((unsigned int)(result))) goto loc_00321420;
loc_00321355:
    if (v_stack_p18 != 0) goto loc_003215A0;
loc_00321363:
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_00321392;
    if ((*(unsigned int *)(v_rip + 13261217)) != 0) {
        a1 = (unsigned __int8)(result);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00321392:
    if (0 != 0) goto loc_003215E9;
loc_0032139B:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003213B4:
    if (((unsigned __int8)(result)) < 2) goto loc_003213CB;
    if (((unsigned __int8)(result)) > 4) goto loc_003213CB;
    if (((unsigned __int8)(result)) >= 4) goto loc_003212C0;
loc_003213CB:
    result = MiUnlockPage(v_r15 + v_rdi * 1, (unsigned __int8)(v_stack_p8), a3, a4);
    goto loc_00321235;
loc_003213DC:
    result = (unsigned int)((result) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_0032139B;
    result = MiInvalidPteConforms(v_stack_p18, (unsigned __int8)(v_stack_p8), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032139B;
    if (*(unsigned __int64 *)(v_rip + 11585668) == 0) goto loc_0032140F;
    if ((((unsigned __int8)(v_stack_p18)) & (16)) != 0) goto loc_0032141A;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11585668));
    a1 = (a1) & (v_stack_p18);
loc_0032140F:
    goto loc_00321265;
loc_0032141A:
    a1 = (a1) & (-17);
    goto loc_0032140F;
loc_00321420:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + v_rdi * 1 + 34)) & (7));
    if (((unsigned __int8)(a1)) == 2) goto loc_00321459;
    result = *(unsigned __int64 *)(v_rip + 11585668);
    if (((unsigned __int8)(a1)) == 6) {
        result = *(unsigned __int64 *)(v_r15 + v_rdi * 1 + 24);
    }
    v_stack_p78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + v_rdi * 1 + 32)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + v_rdi * 1 + 32))) >> (24));
    result = (unsigned __int8)(((unsigned __int8)(a1)) ^ ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    v_stack_p7B = (unsigned __int8)(result);
    *(unsigned int *)(v_r15 + v_rdi * 1 + 32) = (unsigned int)((unsigned int)(v_stack_p78));
    goto loc_00321355;
loc_00321459:
    if ((unsigned int)((unsigned int)(v_stack_p78)) != 0) goto loc_003214C4;
    if (condition_is_below) goto loc_003214C4;
    result = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003214C4;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 16))) >> (2));
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_003214C4;
    a1 = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 16)) >> (12);
    result = (unsigned int)((result) & (15));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8) + 1204))))) goto loc_00321355;
loc_003214C4:
    result = MiRelinkStandbyPage(v_r15 + v_rdi * 1, (unsigned int)((unsigned int)((unsigned int)(a2))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8), a4);
    goto loc_00321355;
loc_003214D4:
    if (sign_flag) goto loc_003214EE;
loc_003214DD:
    result = MiUnlockPage(v_r15 + v_rdi * 1, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8), a4);
    goto loc_0032139B;
loc_003214EE:
    if (a1 < result) goto loc_003214DD;
    if (a1 <= result) goto loc_003212A7;
    goto loc_003214DD;
loc_00321518:
    result = MiUnlockPage(v_r15 + v_rdi * 1, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8), a4);
    if (a1 < 2) goto loc_00321249;
    if (a1 > ((unsigned __int8)(v_stack_p8))) goto loc_00321249;
    a1 = (a1) << (25);
    result = (2) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    if (a1 < 2) goto loc_0032158D;
    if (a1 <= ((unsigned __int8)(v_stack_p8))) goto loc_00321249;
loc_0032158D:
    result = MiGetSystemRegionType(a1, (unsigned __int8)(v_stack_p8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8), a4);
    if (((unsigned int)(result)) == 8) goto loc_0032139B;
    goto loc_00321235;
loc_003215A0:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + v_rdi * 1 + 34)) & (7));
    if (((unsigned __int8)(result)) != 2) goto loc_00321363;
    a1 = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 16)) >> (11);
    a2 = (unsigned int)((*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 16)) & (0x400ULL));
    result = (*(unsigned __int64 *)(v_r15 + v_rdi * 1 + 16)) >> (3);
    if (a2 != 0) { result = (unsigned int)(a1); }
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00321363;
    a2 = 0;
    result = MiSetActivePfnHeat(v_r15 + v_rdi * 1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11594728) + a1 * 8), a4);
    goto loc_00321363;
loc_003215E9:
    v_r15 = (v_r15) >> (4);
    a2 = (a2) * (v_r15);
    result = MiAddPageToHeatList(v_stack_p18, a2, 3, a4);
    goto loc_0032139B;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdatePfnForPrefetchByPte(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_p18;
    uint32_t v_stack_p78;
    uint8_t v_stack_p7B;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (40);
    v_stack_p8 = local_rsi;
    v_stack_m38 = local_r14;
    local_r13 = 0;
loc_00321235:
loc_0032123F:
loc_00321249:
    result = MI_READ_PTE_LOCK_FREE(Arg1, Arg2, Arg3, a4);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_003213DC;
loc_00321265:
    Arg1 = (result) >> (12);
    Arg1 = (Arg1) & (local_r15);
    local_r15 = (Arg1 + Arg1 * 2) << (4);
    result = MiSafeLockPage(Arg1, Arg2, Arg3, a4);
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_0032139B;
    Arg1 = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x8)) | (result);
    if (Arg1 != Arg1) goto loc_003214D4;
loc_003212A7:
    result = (uint8_t)((*(uint8_t *)(local_r15 + local_rdi * 1 + 0x22)) & (7));
    if (6 != 6) goto loc_003213B4;
    if (((uint8_t)(result)) != 6) goto loc_00321518;
loc_003212C0:
    if (Arg1 < result) goto loc_0032133D;
    if (Arg1 > result) goto loc_0032133D;
    result = MI_READ_PTE_LOCK_FREE(Arg1, Arg2, Arg3, a4);
    if (result == result) goto loc_0032133D;
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_00321249;
    if ((*(uint32_t *)(v_rip + 0xCA59FB)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    goto loc_0032123F;
loc_0032133D:
    if (local_r15 + local_rdi * 1 == 0) goto loc_0032139B;
    result = MiGetPfnPriority(local_r15 + local_rdi * 1, Arg2, Arg3, a4);
    if (((uint32_t)((uint32_t)(Arg2))) == ((uint32_t)(result))) goto loc_00321355;
    if (((uint32_t)((uint32_t)(Arg2))) >= ((uint32_t)(result))) goto loc_00321420;
loc_00321355:
    if (v_stack_p18 != 0) goto loc_003215A0;
loc_00321363:
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_00321392;
    if ((*(uint32_t *)(v_rip + 0xCA59A1)) != 0) {
        Arg1 = (uint8_t)(result);
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
loc_00321392:
    if (0 != 0) goto loc_003215E9;
loc_0032139B:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003213B4:
    if (((uint8_t)(result)) < 2) goto loc_003213CB;
    if (((uint8_t)(result)) > 4) goto loc_003213CB;
    if (((uint8_t)(result)) >= 4) goto loc_003212C0;
loc_003213CB:
    result = MiUnlockPage(local_r15 + local_rdi * 1, (uint8_t)(v_stack_p8), Arg3, a4);
    goto loc_00321235;
loc_003213DC:
    result = (uint32_t)((result) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_0032139B;
    result = MiInvalidPteConforms(v_stack_p18, (uint8_t)(v_stack_p8), Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_0032139B;
    if (*(uint64_t *)(v_rip + 0xB0C884) == 0) goto loc_0032140F;
    if ((((uint8_t)(v_stack_p18)) & (16)) != 0) goto loc_0032141A;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xB0C884));
    Arg1 = (Arg1) & (v_stack_p18);
loc_0032140F:
    goto loc_00321265;
loc_0032141A:
    Arg1 = (Arg1) & (-17);
    goto loc_0032140F;
loc_00321420:
    Arg1 = (uint8_t)((*(uint8_t *)(local_r15 + local_rdi * 1 + 0x22)) & (7));
    if (((uint8_t)(Arg1)) == 2) goto loc_00321459;
    result = *(uint64_t *)(v_rip + 0xB0C884);
    if (((uint8_t)(Arg1)) == 6) {
        result = *(uint64_t *)(local_r15 + local_rdi * 1 + 0x18);
    }
    v_stack_p78 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + local_rdi * 1 + 0x20)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + local_rdi * 1 + 0x20))) >> (24));
    result = (uint8_t)(((uint8_t)(Arg1)) ^ ((uint8_t)((uint32_t)(Arg2))));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    v_stack_p7B = (uint8_t)(result);
    *(uint32_t *)(local_r15 + local_rdi * 1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p78));
    goto loc_00321355;
loc_00321459:
    if ((uint32_t)((uint32_t)(v_stack_p78)) != 0) goto loc_003214C4;
    if (condition_is_below) goto loc_003214C4;
    result = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003214C4;
    Arg2 = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r15 + local_rdi * 1 + 0x10))) >> (2));
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_003214C4;
    Arg1 = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x10)) >> (12);
    result = (uint32_t)((result) & (15));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8) + 0x4B4))))) goto loc_00321355;
loc_003214C4:
    result = MiRelinkStandbyPage(local_r15 + local_rdi * 1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8), a4);
    goto loc_00321355;
loc_003214D4:
    if (sign_flag) goto loc_003214EE;
loc_003214DD:
    result = MiUnlockPage(local_r15 + local_rdi * 1, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8), a4);
    goto loc_0032139B;
loc_003214EE:
    if (Arg1 < result) goto loc_003214DD;
    if (Arg1 <= result) goto loc_003212A7;
    goto loc_003214DD;
loc_00321518:
    result = MiUnlockPage(local_r15 + local_rdi * 1, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8), a4);
    if (Arg1 < 2) goto loc_00321249;
    if (Arg1 > ((uint8_t)(v_stack_p8))) goto loc_00321249;
    Arg1 = (Arg1) << (25);
    result = (2) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    if (Arg1 < 2) goto loc_0032158D;
    if (Arg1 <= ((uint8_t)(v_stack_p8))) goto loc_00321249;
loc_0032158D:
    result = MiGetSystemRegionType(Arg1, (uint8_t)(v_stack_p8), *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8), a4);
    if (((uint32_t)(result)) == 8) goto loc_0032139B;
    goto loc_00321235;
loc_003215A0:
    result = (uint8_t)((*(uint8_t *)(local_r15 + local_rdi * 1 + 0x22)) & (7));
    if (((uint8_t)(result)) != 2) goto loc_00321363;
    Arg1 = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x10)) >> (11);
    Arg2 = (uint32_t)((*(uint64_t *)(local_r15 + local_rdi * 1 + 0x10)) & (0x400ULL));
    result = (*(uint64_t *)(local_r15 + local_rdi * 1 + 0x10)) >> (3);
    if (Arg2 != 0) { result = (uint32_t)(Arg1); }
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00321363;
    Arg2 = 0;
    result = MiSetActivePfnHeat(local_r15 + local_rdi * 1, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB0EBE8) + Arg1 * 8), a4);
    goto loc_00321363;
loc_003215E9:
    local_r15 = (local_r15) >> (4);
    Arg2 = (Arg2) * (local_r15);
    result = MiAddPageToHeatList(v_stack_p18, Arg2, 3, a4);
    goto loc_0032139B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00321210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
