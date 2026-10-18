# MiDecommitHandleTransitionPte

- RVA: `0x0024037C`–`0x0024077A` (길이 `1,022` bytes)
- VA: `0x000000014024037C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006173C`
- 디코드: `243`개 명령, `1,022/1,022` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x002403C8` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002403DE` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x00240466` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00240539` → [MiDeleteTransitionPte](../37/MiDeleteTransitionPte_function_00371B70.md) (function, `0x00371B70`)
- `0x0024062C` → [MI_IS_PTE_IN_WS_SWAP_SET](../38/MI_IS_PTE_IN_WS_SWAP_SET_function_00385DD8.md) (function, `0x00385DD8`)
- `0x00240641` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x00240681` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00240695` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002406A4` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002406D6` → [MiReturnPagedPoolLockCharge](MiReturnPagedPoolLockCharge_function_00240780.md) (function, `0x00240780`)
- `0x002406F3` → [MiIsPfnSystemCharged](../43/MiIsPfnSystemCharged_function_0043E910.md) (function, `0x0043E910`)
- `0x00240735` → [MiReleasePageFileSpace](../28/MiReleasePageFileSpace_function_00285980.md) (function, `0x00285980`)

### Direct callers
- [sub_00241E90](Unknown_function_00241E90.md) at `0x0024219C`
- [MiDeleteVa](../27/MiDeleteVa_function_002789E0.md) at `0x00278ED1`

### Static image references
- `0x002403EA` → RVA `0x00E2DC80` (`.data`; read)
- `0x0024042A` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00240478` → RVA `0x00E30088` (`.data`; read)
- `0x0024059A` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00240687` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x002406B2` → [sub_006D7C08](../6D/Unknown_function_006D7C08.md) (`tail-transfer`)
  - `0x002406C7` → [sub_006D7C08](../6D/Unknown_function_006D7C08.md) (`tail-transfer`)
  - `0x0024075E` → [sub_006D7C08 + 0x10](../6D/Unknown_function_006D7C08.md) (`tail-transfer`)
  - `0x00240766` → [sub_006D7C08 + 0x10](../6D/Unknown_function_006D7C08.md) (`tail-transfer`)
  - `0x00240775` → [sub_006D7C08 + 0x10](../6D/Unknown_function_006D7C08.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024037C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00240381  55                              push rbp
00240382  56                              push rsi
00240383  57                              push rdi
00240384  41 54                           push r12
00240386  41 55                           push r13
00240388  41 56                           push r14
0024038A  41 57                           push r15
0024038C  48 83 EC 30                     sub rsp, 0x30
00240390  81 E2 E0 03 00 00               and edx, 0x3e0
00240396  45 33 ED                        xor r13d, r13d
00240399  48 8B F1                        mov rsi, rcx
0024039C  48 81 FA 00 03 00 00            cmp rdx, 0x300
002403A3  0F 84 05 03 00 00               je 0x1402406ae
002403A9  48 83 B9 C0 00 00 00 01         cmp qword ptr [rcx + 0xc0], 1
002403B1  0F 85 06 03 00 00               jne 0x1402406bd
002403B7  4C 8B 71 58                     mov r14, qword ptr [rcx + 0x58]
002403BB  49 BF FF FF FF FF FF FF FF 7F   movabs r15, 0x7fffffffffffffff
002403C5  49 8B CE                        mov rcx, r14
002403C8  E8 D3 24 04 00                  call 0x1402828a0
002403CD  48 8B D8                        mov rbx, rax
002403D0  48 0F BA E0 0B                  bt rax, 0xb
002403D5  0F 83 77 02 00 00               jae 0x140240652
002403DB  48 8B C8                        mov rcx, rax
002403DE  E8 2D 26 13 00                  call 0x140372a10
002403E3  85 C0                           test eax, eax
002403E5  74 DE                           je 0x1402403c5
002403E7  48 8B C1                        mov rax, rcx
002403EA  48 8B 0D 8F D8 BE 00            mov rcx, qword ptr [rip + 0xbed88f]
002403F1  48 85 C9                        test rcx, rcx
002403F4  74 12                           je 0x140240408
002403F6  F6 C3 10                        test bl, 0x10
002403F9  0F 85 90 01 00 00               jne 0x14024058f
002403FF  48 8B C1                        mov rax, rcx
00240402  48 F7 D0                        not rax
00240405  48 23 C3                        and rax, rbx
00240408  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00240412  48 C1 E8 0C                     shr rax, 0xc
00240416  48 23 C1                        and rax, rcx
00240419  48 8D 0C 40                     lea rcx, [rax + rax*2]
0024041D  48 03 C9                        add rcx, rcx
00240420  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0024042A  48 3B 05 AF D8 BE 00            cmp rax, qword ptr [rip + 0xbed8af]
00240431  48 8D 3C CA                     lea rdi, [rdx + rcx*8]
00240435  77 8E                           ja 0x1402403c5
00240437  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00240441  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00240445  48 C1 E8 36                     shr rax, 0x36
00240449  0F BA E0 00                     bt eax, 0
0024044D  0F 83 72 FF FF FF               jae 0x1402403c5
00240453  41 8B ED                        mov ebp, r13d
00240456  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0024045D  0F 82 35 01 00 00               jb 0x140240598
00240463  49 8B CE                        mov rcx, r14
00240466  E8 35 24 04 00                  call 0x1402828a0
0024046B  48 3B C3                        cmp rax, rbx
0024046E  0F 85 6D 01 00 00               jne 0x1402405e1
00240474  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00240478  48 8B 15 09 FC BE 00            mov rdx, qword ptr [rip + 0xbefc09]
0024047F  48 C1 E8 2B                     shr rax, 0x2b
00240483  25 FF 03 00 00                  and eax, 0x3ff
00240488  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0024048C  8B 40 04                        mov eax, dword ptr [rax + 4]
0024048F  84 C0                           test al, al
00240491  0F 88 A5 01 00 00               js 0x14024063c
00240497  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0024049B  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002404A5  48 0B C1                        or rax, rcx
002404A8  49 3B C6                        cmp rax, r14
002404AB  0F 85 A8 01 00 00               jne 0x140240659
002404B1  48 85 FF                        test rdi, rdi
002404B4  0F 84 98 01 00 00               je 0x140240652
002404BA  8B 8E 9C 00 00 00               mov ecx, dword ptr [rsi + 0x9c]
002404C0  F6 C1 08                        test cl, 8
002404C3  0F 85 03 02 00 00               jne 0x1402406cc
002404C9  4C 8B 7E 08                     mov r15, qword ptr [rsi + 8]
002404CD  49 8B DD                        mov rbx, r13
002404D0  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
002404D8  45 8B D5                        mov r10d, r13d
002404DB  45 8B E5                        mov r12d, r13d
002404DE  BD 01 00 00 00                  mov ebp, 1
002404E3  F6 C1 20                        test cl, 0x20
002404E6  0F 85 E5 00 00 00               jne 0x1402405d1
002404EC  44 39 6E 28                     cmp dword ptr [rsi + 0x28], r13d
002404F0  0F 85 EF 01 00 00               jne 0x1402406e5
002404F6  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
002404F9  66 85 C0                        test ax, ax
002404FC  0F 84 E9 00 00 00               je 0x1402405eb
00240502  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0024050B  4C 8D 76 18                     lea r14, [rsi + 0x18]
0024050F  41 BA 02 00 00 00               mov r10d, 2
00240515  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0024051C  F0 48 FF 89 88 02 00 00         lock dec qword ptr [rcx + 0x288]
00240524  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0024052C  48 8B 4E 58                     mov rcx, qword ptr [rsi + 0x58]
00240530  45 8B CA                        mov r9d, r10d
00240533  41 B0 11                        mov r8b, 0x11
00240536  48 8B D7                        mov rdx, rdi
00240539  E8 32 16 13 00                  call 0x140371b70
0024053E  83 F8 03                        cmp eax, 3
00240541  0F 84 C5 01 00 00               je 0x14024070c
00240547  45 85 E4                        test r12d, r12d
0024054A  0F 85 BC 01 00 00               jne 0x14024070c
00240550  8B 86 9C 00 00 00               mov eax, dword ptr [rsi + 0x9c]
00240556  48 8B BE B0 00 00 00            mov rdi, qword ptr [rsi + 0xb0]
0024055D  A8 20                           test al, 0x20
0024055F  74 56                           je 0x1402405b7
00240561  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
00240564  85 C0                           test eax, eax
00240566  0F 85 AC 01 00 00               jne 0x140240718
0024056C  48 85 FF                        test rdi, rdi
0024056F  75 03                           jne 0x140240574
00240571  FF 46 70                        inc dword ptr [rsi + 0x70]
00240574  B8 01 00 00 00                  mov eax, 1
00240579  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0024057E  48 83 C4 30                     add rsp, 0x30
00240582  41 5F                           pop r15
00240584  41 5E                           pop r14
00240586  41 5D                           pop r13
00240588  41 5C                           pop r12
0024058A  5F                              pop rdi
0024058B  5E                              pop rsi
0024058C  5D                              pop rbp
0024058D  C3                              ret
0024058E  CC                              int3
0024058F  48 83 E0 EF                     and rax, 0xffffffffffffffef
00240593  E9 70 FE FF FF                  jmp 0x140240408
00240598  FF C5                           inc ebp
0024059A  85 2D 0C 4D D8 00               test dword ptr [rip + 0xd84d0c], ebp
002405A0  0F 84 E1 00 00 00               je 0x140240687
002405A6  F3 90                           pause
002405A8  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002405AC  48 85 C0                        test rax, rax
002405AF  0F 89 A1 FE FF FF               jns 0x140240456
002405B5  EB E1                           jmp 0x140240598
002405B7  48 85 DB                        test rbx, rbx
002405BA  0F 85 6C 01 00 00               jne 0x14024072c
002405C0  85 ED                           test ebp, ebp
002405C2  0F 84 77 01 00 00               je 0x14024073f
002405C8  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
002405CC  48 89 38                        mov qword ptr [rax], rdi
002405CF  EB 9B                           jmp 0x14024056c
002405D1  4C 8D 76 18                     lea r14, [rsi + 0x18]
002405D5  49 8B 06                        mov rax, qword ptr [r14]
002405D8  48 FF 40 18                     inc qword ptr [rax + 0x18]
002405DC  E9 4B FF FF FF                  jmp 0x14024052c
002405E1  F0 4C 21 7F 18                  lock and qword ptr [rdi + 0x18], r15
002405E6  E9 DA FD FF FF                  jmp 0x1402403c5
002405EB  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002405EF  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002405F7  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
002405FB  48 8B 0D 86 FA BE 00            mov rcx, qword ptr [rip + 0xbefa86]
00240602  48 C1 E8 2B                     shr rax, 0x2b
00240606  25 FF 03 00 00                  and eax, 0x3ff
0024060B  4C 8B 3C C1                     mov r15, qword ptr [rcx + rax*8]
0024060F  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00240616  D0 E8                           shr al, 1
00240618  40 84 C5                        test bpl, al
0024061B  0F 84 E1 FE FF FF               je 0x140240502
00240621  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00240629  49 8B CF                        mov rcx, r15
0024062C  E8 A7 57 14 00                  call 0x140385dd8
00240631  F7 D8                           neg eax
00240633  1B C9                           sbb ecx, ecx
00240635  23 E9                           and ebp, ecx
00240637  E9 C6 FE FF FF                  jmp 0x140240502
0024063C  33 D2                           xor edx, edx
0024063E  48 8B CF                        mov rcx, rdi
00240641  E8 AA 43 1C 00                  call 0x1404049f0
00240646  48 8B F8                        mov rdi, rax
00240649  48 85 C0                        test rax, rax
0024064C  0F 85 45 FE FF FF               jne 0x140240497
00240652  33 C0                           xor eax, eax
00240654  E9 20 FF FF FF                  jmp 0x140240579
00240659  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0024065D  48 0F BA E0 28                  bt rax, 0x28
00240662  0F 82 49 FE FF FF               jb 0x1402404b1
00240668  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0024066C  4C 8B CB                        mov r9, rbx
0024066F  4D 8B C6                        mov r8, r14
00240672  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00240677  BA 11 04 00 00                  mov edx, 0x411
0024067C  B9 1A 00 00 00                  mov ecx, 0x1a
00240681  E8 DA CF 2B 00                  call 0x1404fd660
00240686  CC                              int3
00240687  8B 05 2B 64 D8 00               mov eax, dword ptr [rip + 0xd8642b]
0024068D  A8 40                           test al, 0x40
0024068F  0F 84 11 FF FF FF               je 0x1402405a6
00240695  E8 F6 ED 0C 00                  call 0x14030f490
0024069A  84 C0                           test al, al
0024069C  0F 84 04 FF FF FF               je 0x1402405a6
002406A2  8B CD                           mov ecx, ebp
002406A4  E8 B7 ED 0C 00                  call 0x14030f460
002406A9  E9 FA FE FF FF                  jmp 0x1402405a8
002406AE  44 39 69 60                     cmp dword ptr [rcx + 0x60], r13d
002406B2  0F 85 50 75 49 00               jne 0x1406d7c08
002406B8  E9 EC FC FF FF                  jmp 0x1402403a9
002406BD  44 39 69 60                     cmp dword ptr [rcx + 0x60], r13d
002406C1  0F 85 F0 FC FF FF               jne 0x1402403b7
002406C7  E9 3C 75 49 00                  jmp 0x1406d7c08
002406CC  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
002406D0  48 8B CE                        mov rcx, rsi
002406D3  48 8B 12                        mov rdx, qword ptr [rdx]
002406D6  E8 A5 00 00 00                  call 0x140240780
002406DB  F0 4C 21 7F 18                  lock and qword ptr [rdi + 0x18], r15
002406E0  E9 8F FE FF FF                  jmp 0x140240574
002406E5  4C 8D 76 18                     lea r14, [rsi + 0x18]
002406E9  48 8B CF                        mov rcx, rdi
002406EC  49 8B 06                        mov rax, qword ptr [r14]
002406EF  48 FF 40 18                     inc qword ptr [rax + 0x18]
002406F3  E8 18 E2 1F 00                  call 0x14043e910
002406F8  85 C0                           test eax, eax
002406FA  0F 84 2C FE FF FF               je 0x14024052c
00240700  80 67 23 DF                     and byte ptr [rdi + 0x23], 0xdf
00240704  44 8B E5                        mov r12d, ebp
00240707  E9 20 FE FF FF                  jmp 0x14024052c
0024070C  49 8B 06                        mov rax, qword ptr [r14]
0024070F  48 FF 40 08                     inc qword ptr [rax + 8]
00240713  E9 38 FE FF FF                  jmp 0x140240550
00240718  83 F8 03                        cmp eax, 3
0024071B  0F 84 4B FE FF FF               je 0x14024056c
00240721  49 8B 06                        mov rax, qword ptr [r14]
00240724  48 FF 00                        inc qword ptr [rax]
00240727  E9 40 FE FF FF                  jmp 0x14024056c
0024072C  44 8B C5                        mov r8d, ebp
0024072F  48 8B D3                        mov rdx, rbx
00240732  49 8B CF                        mov rcx, r15
00240735  E8 46 52 04 00                  call 0x140285980
0024073A  E9 81 FE FF FF                  jmp 0x1402405c0
0024073F  48 8B 0D 3A D5 BE 00            mov rcx, qword ptr [rip + 0xbed53a]
00240746  48 8B C3                        mov rax, rbx
00240749  48 C1 E8 0C                     shr rax, 0xc
0024074D  83 E0 0F                        and eax, 0xf
00240750  49 8B 94 C7 60 48 00 00         mov rdx, qword ptr [r15 + rax*8 + 0x4860]
00240758  48 8B C3                        mov rax, rbx
0024075B  48 85 C9                        test rcx, rcx
0024075E  0F 84 B4 74 49 00               je 0x1406d7c18
00240764  A8 10                           test al, 0x10
00240766  0F 85 AC 74 49 00               jne 0x1406d7c18
0024076C  48 8B D9                        mov rbx, rcx
0024076F  48 F7 D3                        not rbx
00240772  48 23 D8                        and rbx, rax
00240775  E9 9E 74 49 00                  jmp 0x1406d7c18
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitHandleTransitionPte(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    a2 = (unsigned int)((a2) & (992));
    v_r13 = 0;
    if (a2 == 768) goto loc_002406AE;
loc_002403A9:
    if ((*(unsigned __int64 *)(a1 + 192)) != 1) goto loc_002406BD;
loc_002403B7:
loc_002403C5:
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a1 + 88), a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 192)) >= 1) goto loc_00240652;
    result = MiInvalidPteConforms(result, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002403C5;
    if (*(unsigned __int64 *)(v_rip + 12507279) == 0) goto loc_00240408;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0024058F;
    result = ~(*(unsigned __int64 *)(v_rip + 12507279));
    result = (result) & (result);
loc_00240408:
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 12507279));
    a1 = (result + result * 2) + (result + result * 2);
    if (result > (*(unsigned __int64 *)(v_rip + 12507311))) goto loc_002403C5;
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002403C5;
loc_00240456:
    if (condition_is_below) goto loc_00240598;
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a1 + 88), a2, a3, a4);
    if (result != result) goto loc_002405E1;
    result = (*(unsigned __int64 *)(a2 + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0024063C;
loc_00240497:
    result = (*(unsigned __int64 *)(a2 + a1 * 8 + 8)) | (*(unsigned __int64 *)(a1 + 88));
    if (result != (*(unsigned __int64 *)(a1 + 88))) goto loc_00240659;
loc_002404B1:
    if (a2 + a1 * 8 == 0) goto loc_00240652;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (8)) != 0) goto loc_002406CC;
    v_stack_p18 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) != 0) goto loc_002405D1;
    if ((*(unsigned int *)(a1 + 40)) != 0) goto loc_002406E5;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + a1 * 8 + 32))) == 0) goto loc_002405EB;
loc_00240502:
loc_0024052C:
    result = MiDeleteTransitionPte(*(unsigned __int64 *)(a1 + 88), a2 + a1 * 8, 17, 2);
    if (((unsigned int)(result)) == 3) goto loc_0024070C;
    if (0 != 0) goto loc_0024070C;
loc_00240550:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) == 0) goto loc_002405B7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) != 0) goto loc_00240718;
loc_0024056C:
    if (*(unsigned __int64 *)(a1 + 176) == 0) {
    }
loc_00240579:
    v_rsp = (v_rsp) + (48);
    return 1;
loc_0024058F:
    result = (1) & (-17);
    goto loc_00240408;
loc_00240598:
    v_rbp = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 14175500)) & ((unsigned int)(v_rbp))) == 0) goto loc_00240687;
loc_002405A6:
loc_002405A8:
    if (!sign_flag) goto loc_00240456;
    goto loc_00240598;
loc_002405B7:
    if (v_stack_p8 != 0) goto loc_0024072C;
loc_002405C0:
    if ((unsigned int)(v_rbp) == 0) goto loc_0024073F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88)) = *(unsigned __int64 *)(a1 + 176);
    goto loc_0024056C;
loc_002405D1:
    goto loc_0024052C;
loc_002405E1:
    goto loc_002403C5;
loc_002405EB:
    v_stack_p80 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176) + 16);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = (unsigned __int8)((v_stack_p80) >> (1));
    if ((((unsigned __int8)(v_rbp)) & ((unsigned __int8)(result))) == 0) goto loc_00240502;
    result = MI_IS_PTE_IN_WS_SWAP_SET(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12515974) + result * 8), v_stack_p80, 17, 2);
    result = (unsigned int)(-(result));
    v_rbp = (unsigned int)((v_rbp) & ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12515974) + result * 8))));
    goto loc_00240502;
loc_0024063C:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(unsigned __int64 *)(a1 + 176), a2, 17, 2);
    if (result != 0) goto loc_00240497;
loc_00240652:
    result = 0;
    goto loc_00240579;
loc_00240659:
    if (condition_is_below) goto loc_002404B1;
    v_stack_p20 = *(unsigned __int64 *)(result + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), a1 + 24, v_stack_p8);
loc_00240687:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14181419)))) & (64)) == 0) goto loc_002405A6;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), a1 + 24, v_stack_p8);
    if ((unsigned __int8)(result) == 0) goto loc_002405A6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0x411ULL), a1 + 24, v_stack_p8);
    goto loc_002405A8;
loc_002406AE:
    goto loc_002403A9;
loc_002406BD:
    if ((*(unsigned int *)((unsigned int)((unsigned int)(v_rbp)) + 96)) != 0) goto loc_002403B7;
loc_002406CC:
    result = MiReturnPagedPoolLockCharge(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88)), a1 + 24, v_stack_p8);
    goto loc_00240574;
loc_002406E5:
    result = MiIsPfnSystemCharged(result, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88)), a1 + 24, v_stack_p8);
    if ((unsigned int)(result) == 0) goto loc_0024052C;
    goto loc_0024052C;
loc_0024070C:
    goto loc_00240550;
loc_00240718:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 24))) == 3) goto loc_0024056C;
    goto loc_0024056C;
loc_0024072C:
    result = MiReleasePageFileSpace(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12515974) + result * 8), v_stack_p8, (unsigned int)((unsigned int)(v_rbp)), v_stack_p8);
    goto loc_002405C0;
loc_0024073F:
    result = (v_stack_p8) >> (12);
    result = (unsigned int)((result) & (15));
    v_rbx = ~(*(unsigned __int64 *)(v_rip + 12506426));
    v_rbx = (v_rbx) & (v_stack_p8);
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitHandleTransitionPte(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    Arg2 = (uint32_t)((Arg2) & (992));
    local_r13 = 0;
    if (Arg2 == 768) goto loc_002406AE;
loc_002403A9:
    if ((*(uint64_t *)(arg1 + 0xC0)) != 1) goto loc_002406BD;
loc_002403B7:
loc_002403C5:
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(arg1 + 0x58), Arg2, a3, a4);
    if ((*(uint64_t *)(arg1 + 0xC0)) >= 1) goto loc_00240652;
    result = MiInvalidPteConforms(result, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_002403C5;
    if (*(uint64_t *)(v_rip + 0xBED88F) == 0) goto loc_00240408;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0024058F;
    result = ~(*(uint64_t *)(v_rip + 0xBED88F));
    result = (result) & (result);
loc_00240408:
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xBED88F));
    Arg1 = (result + result * 2) + (result + result * 2);
    if (result > (*(uint64_t *)(v_rip + 0xBED8AF))) goto loc_002403C5;
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002403C5;
loc_00240456:
    if (condition_is_below) goto loc_00240598;
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(arg1 + 0x58), Arg2, a3, a4);
    if (result != result) goto loc_002405E1;
    result = (*(uint64_t *)(Arg2 + arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0024063C;
loc_00240497:
    result = (*(uint64_t *)(Arg2 + arg1 * 8 + 0x8)) | (*(uint64_t *)(arg1 + 0x58));
    if (result != (*(uint64_t *)(arg1 + 0x58))) goto loc_00240659;
loc_002404B1:
    if (Arg2 + Arg1 * 8 == 0) goto loc_00240652;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (8)) != 0) goto loc_002406CC;
    v_stack_p18 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) != 0) goto loc_002405D1;
    if ((*(uint32_t *)(arg1 + 0x28)) != 0) goto loc_002406E5;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg2 + arg1 * 8 + 0x20))) == 0) goto loc_002405EB;
loc_00240502:
loc_0024052C:
    result = MiDeleteTransitionPte(*(uint64_t *)(arg1 + 0x58), Arg2 + Arg1 * 8, 17, 2);
    if (((uint32_t)(result)) == 3) goto loc_0024070C;
    if (0 != 0) goto loc_0024070C;
loc_00240550:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) == 0) goto loc_002405B7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) != 0) goto loc_00240718;
loc_0024056C:
    if (*(uint64_t *)(arg1 + 0xB0) == 0) {
    }
loc_00240579:
    local_rsp = (local_rsp) + (48);
    return 1;
loc_0024058F:
    result = (1) & (-17);
    goto loc_00240408;
loc_00240598:
    local_rbp = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xD84D0C)) & ((uint32_t)(local_rbp))) == 0) goto loc_00240687;
loc_002405A6:
loc_002405A8:
    if (!sign_flag) goto loc_00240456;
    goto loc_00240598;
loc_002405B7:
    if (v_stack_p8 != 0) goto loc_0024072C;
loc_002405C0:
    if ((uint32_t)(local_rbp) == 0) goto loc_0024073F;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x58)) = *(uint64_t *)(arg1 + 0xB0);
    goto loc_0024056C;
loc_002405D1:
    goto loc_0024052C;
loc_002405E1:
    goto loc_002403C5;
loc_002405EB:
    v_stack_p80 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xB0) + 0x10);
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB0) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = (uint8_t)((v_stack_p80) >> (1));
    if ((((uint8_t)(local_rbp)) & ((uint8_t)(result))) == 0) goto loc_00240502;
    result = MI_IS_PTE_IN_WS_SWAP_SET(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBEFA86) + result * 8), v_stack_p80, 17, 2);
    result = (uint32_t)(-(result));
    local_rbp = (uint32_t)((local_rbp) & ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBEFA86) + result * 8))));
    goto loc_00240502;
loc_0024063C:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(uint64_t *)(arg1 + 0xB0), Arg2, 17, 2);
    if (result != 0) goto loc_00240497;
loc_00240652:
    result = 0;
    goto loc_00240579;
loc_00240659:
    if (condition_is_below) goto loc_002404B1;
    v_stack_p20 = *(uint64_t *)(result + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), Arg1 + 24, v_stack_p8);
loc_00240687:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD8642B)))) & (64)) == 0) goto loc_002405A6;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), Arg1 + 24, v_stack_p8);
    if ((uint8_t)(result) == 0) goto loc_002405A6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0x411ULL), Arg1 + 24, v_stack_p8);
    goto loc_002405A8;
loc_002406AE:
    goto loc_002403A9;
loc_002406BD:
    if ((*(uint32_t *)((uint32_t)((uint32_t)(local_rbp)) + 0x60)) != 0) goto loc_002403B7;
loc_002406CC:
    result = MiReturnPagedPoolLockCharge(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x58)), Arg1 + 24, v_stack_p8);
    goto loc_00240574;
loc_002406E5:
    result = MiIsPfnSystemCharged(result, *(uint64_t *)(*(uint64_t *)(arg1 + 0x58)), Arg1 + 24, v_stack_p8);
    if ((uint32_t)(result) == 0) goto loc_0024052C;
    goto loc_0024052C;
loc_0024070C:
    goto loc_00240550;
loc_00240718:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x18))) == 3) goto loc_0024056C;
    goto loc_0024056C;
loc_0024072C:
    result = MiReleasePageFileSpace(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBEFA86) + result * 8), v_stack_p8, (uint32_t)((uint32_t)(local_rbp)), v_stack_p8);
    goto loc_002405C0;
loc_0024073F:
    result = (v_stack_p8) >> (12);
    result = (uint32_t)((result) & (15));
    local_rbx = ~(*(uint64_t *)(v_rip + 0xBED53A));
    local_rbx = (local_rbx) & (v_stack_p8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R/W` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024037C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
