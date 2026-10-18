# KiSetSystemTimeDpc

- RVA: `0x00486130`–`0x0048648B` (길이 `859` bytes)
- VA: `0x0000000140486130`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AF79C`
- 디코드: `237`개 명령, `859/859` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00486208` → [KiUpdateSystemTime](../4B/KiUpdateSystemTime_function_004B1570.md) (function, `0x004B1570`)
- `0x0048621D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0048622D` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x0048623D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0048625E` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004862FF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0048630B` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x0048631B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00486350` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00486378` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00486384` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x00486393` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004863AF` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004863CE` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0048644B` → [KiAdjustTimerDueTimes](../4E/KiAdjustTimerDueTimes_function_004E8CD4.md) (function, `0x004E8CD4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00486180` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x004861A1` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x004861BE` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0048620F` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x004863D8` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x004861FD` → [sub_006F5584 + 0x48](../6F/Unknown_function_006F5584.md) (`tail-transfer`)
  - `0x00486408` → [sub_006F5584](../6F/Unknown_function_006F5584.md) (`tail-transfer`)
  - `0x0048643D` → [sub_006F5584 + 0x6F](../6F/Unknown_function_006F5584.md) (`tail-transfer`)
  - `0x00486486` → [sub_006F5584 + 0xB7](../6F/Unknown_function_006F5584.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00486130  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00486135  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0048613A  55                              push rbp
0048613B  56                              push rsi
0048613C  57                              push rdi
0048613D  41 54                           push r12
0048613F  41 55                           push r13
00486141  41 56                           push r14
00486143  41 57                           push r15
00486145  48 8B EC                        mov rbp, rsp
00486148  48 83 EC 50                     sub rsp, 0x50
0048614C  49 8B D9                        mov rbx, r9
0048614F  4C 8B EA                        mov r13, rdx
00486152  83 C8 FF                        or eax, 0xffffffff
00486155  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
0048615A  FF C8                           dec eax
0048615C  BE 00 00 00 80                  mov esi, 0x80000000
00486161  8B F8                           mov edi, eax
00486163  F7 D7                           not edi
00486165  23 FE                           and edi, esi
00486167  A9 FF FF FF 3F                  test eax, 0x3fffffff
0048616C  0F 84 D5 00 00 00               je 0x140486247
00486172  41 8B 01                        mov eax, dword ptr [r9]
00486175  45 33 F6                        xor r14d, r14d
00486178  45 33 FF                        xor r15d, r15d
0048617B  EB 14                           jmp 0x140486191
0048617D  41 FF C6                        inc r14d
00486180  44 85 35 25 F1 B3 00            test dword ptr [rip + 0xb3f125], r14d
00486187  0F 84 82 00 00 00               je 0x14048620f
0048618D  F3 90                           pause
0048618F  8B 03                           mov eax, dword ptr [rbx]
00486191  23 C6                           and eax, esi
00486193  3B C7                           cmp eax, edi
00486195  75 E6                           jne 0x14048617d
00486197  90                              nop
00486198  65 4C 8B 24 25 20 00 00 00      mov r12, qword ptr gs:[0x20]
004861A1  83 3D 88 EE B3 00 00            cmp dword ptr [rip + 0xb3ee88], 0
004861A8  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
004861AC  0F 84 BB 00 00 00               je 0x14048626d
004861B2  41 80 7C 24 21 00               cmp byte ptr [r12 + 0x21], 0
004861B8  0F 84 AA 00 00 00               je 0x140486268
004861BE  4C 8B 3D 7B 2A B4 00            mov r15, qword ptr [rip + 0xb42a7b]
004861C5  49 81 C7 00 41 00 00            add r15, 0x4100
004861CC  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
004861D6  48 8B 09                        mov rcx, qword ptr [rcx]
004861D9  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
004861DD  48 89 08                        mov qword ptr [rax], rcx
004861E0  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
004861E4  41 8B 55 04                     mov edx, dword ptr [r13 + 4]
004861E8  48 8B 08                        mov rcx, qword ptr [rax]
004861EB  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
004861EF  49 89 4D 18                     mov qword ptr [r13 + 0x18], rcx
004861F3  48 2B 08                        sub rcx, qword ptr [rax]
004861F6  49 89 4D 18                     mov qword ptr [r13 + 0x18], rcx
004861FA  F6 C2 01                        test dl, 1
004861FD  0F 85 C9 F3 26 00               jne 0x1406f55cc
00486203  44 8B C2                        mov r8d, edx
00486206  33 D2                           xor edx, edx
00486208  E8 63 B3 02 00                  call 0x1404b1570
0048620D  EB 72                           jmp 0x140486281
0048620F  8B 05 A3 08 B4 00               mov eax, dword ptr [rip + 0xb408a3]
00486215  A8 40                           test al, 0x40
00486217  0F 84 70 FF FF FF               je 0x14048618d
0048621D  E8 6E 92 E8 FF                  call 0x14030f490
00486222  84 C0                           test al, al
00486224  0F 84 63 FF FF FF               je 0x14048618d
0048622A  41 FF C7                        inc r15d
0048622D  E8 FA 5F 07 00                  call 0x1404fc22c
00486232  84 C0                           test al, al
00486234  0F 85 9E 01 00 00               jne 0x1404863d8
0048623A  41 8B CE                        mov ecx, r14d
0048623D  E8 1E 92 E8 FF                  call 0x14030f460
00486242  E9 48 FF FF FF                  jmp 0x14048618f
00486247  41 0B 79 04                     or edi, dword ptr [r9 + 4]
0048624B  41 87 39                        xchg dword ptr [r9], edi
0048624E  89 7D 48                        mov dword ptr [rbp + 0x48], edi
00486251  0F BA E7 1E                     bt edi, 0x1e
00486255  0F 83 3D FF FF FF               jae 0x140486198
0048625B  48 8B CB                        mov rcx, rbx
0048625E  E8 BD 19 D9 FF                  call 0x140217c20
00486263  E9 30 FF FF FF                  jmp 0x140486198
00486268  45 33 FF                        xor r15d, r15d
0048626B  EB 14                           jmp 0x140486281
0048626D  41 80 7C 24 21 00               cmp byte ptr [r12 + 0x21], 0
00486273  4D 8D BC 24 00 41 00 00         lea r15, [r12 + 0x4100]
0048627B  0F 85 4B FF FF FF               jne 0x1404861cc
00486281  83 C8 FF                        or eax, 0xffffffff
00486284  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
00486288  FF C8                           dec eax
0048628A  8B F8                           mov edi, eax
0048628C  F7 D7                           not edi
0048628E  23 FE                           and edi, esi
00486290  A9 FF FF FF 3F                  test eax, 0x3fffffff
00486295  0F 84 FF 00 00 00               je 0x14048639a
0048629B  45 33 F6                        xor r14d, r14d
0048629E  45 33 E4                        xor r12d, r12d
004862A1  EB 0E                           jmp 0x1404862b1
004862A3  41 FF C6                        inc r14d
004862A6  44 85 35 FF EF B3 00            test dword ptr [rip + 0xb3efff], r14d
004862AD  74 46                           je 0x1404862f5
004862AF  F3 90                           pause
004862B1  8B 03                           mov eax, dword ptr [rbx]
004862B3  23 C6                           and eax, esi
004862B5  3B C7                           cmp eax, edi
004862B7  75 EA                           jne 0x1404862a3
004862B9  4C 8B 65 E8                     mov r12, qword ptr [rbp - 0x18]
004862BD  90                              nop
004862BE  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
004862C3  74 73                           je 0x140486338
004862C5  4D 85 FF                        test r15, r15
004862C8  0F 85 74 01 00 00               jne 0x140486442
004862CE  83 C8 FF                        or eax, 0xffffffff
004862D1  F0 0F C1 03                     lock xadd dword ptr [rbx], eax
004862D5  FF C8                           dec eax
004862D7  8B F8                           mov edi, eax
004862D9  F7 D7                           not edi
004862DB  23 FE                           and edi, esi
004862DD  A9 FF FF FF 3F                  test eax, 0x3fffffff
004862E2  0F 84 D1 00 00 00               je 0x1404863b9
004862E8  33 F6                           xor esi, esi
004862EA  41 BD 00 00 00 80               mov r13d, 0x80000000
004862F0  45 33 FF                        xor r15d, r15d
004862F3  EB 39                           jmp 0x14048632e
004862F5  8B 05 BD 07 B4 00               mov eax, dword ptr [rip + 0xb407bd]
004862FB  A8 40                           test al, 0x40
004862FD  74 B0                           je 0x1404862af
004862FF  E8 8C 91 E8 FF                  call 0x14030f490
00486304  84 C0                           test al, al
00486306  74 A7                           je 0x1404862af
00486308  41 FF C4                        inc r12d
0048630B  E8 1C 5F 07 00                  call 0x1404fc22c
00486310  84 C0                           test al, al
00486312  0F 85 F5 00 00 00               jne 0x14048640d
00486318  41 8B CE                        mov ecx, r14d
0048631B  E8 40 91 E8 FF                  call 0x14030f460
00486320  EB 8F                           jmp 0x1404862b1
00486322  FF C6                           inc esi
00486324  85 35 82 EF B3 00               test dword ptr [rip + 0xb3ef82], esi
0048632A  74 42                           je 0x14048636e
0048632C  F3 90                           pause
0048632E  8B 03                           mov eax, dword ptr [rbx]
00486330  41 23 C5                        and eax, r13d
00486333  3B C7                           cmp eax, edi
00486335  75 EB                           jne 0x140486322
00486337  90                              nop
00486338  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0048633C  45 33 C9                        xor r9d, r9d
0048633F  33 D2                           xor edx, edx
00486341  C6 44 24 20 02                  mov byte ptr [rsp + 0x20], 2
00486346  49 8B CC                        mov rcx, r12
00486349  F0 FF 08                        lock dec dword ptr [rax]
0048634C  45 8D 41 01                     lea r8d, [r9 + 1]
00486350  E8 9B B9 DC FF                  call 0x140251cf0
00486355  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0048635D  48 83 C4 50                     add rsp, 0x50
00486361  41 5F                           pop r15
00486363  41 5E                           pop r14
00486365  41 5D                           pop r13
00486367  41 5C                           pop r12
00486369  5F                              pop rdi
0048636A  5E                              pop rsi
0048636B  5D                              pop rbp
0048636C  C3                              ret
0048636D  CC                              int3
0048636E  8B 05 44 07 B4 00               mov eax, dword ptr [rip + 0xb40744]
00486374  A8 40                           test al, 0x40
00486376  74 B4                           je 0x14048632c
00486378  E8 13 91 E8 FF                  call 0x14030f490
0048637D  84 C0                           test al, al
0048637F  74 AB                           je 0x14048632c
00486381  41 FF C7                        inc r15d
00486384  E8 A3 5E 07 00                  call 0x1404fc22c
00486389  84 C0                           test al, al
0048638B  0F 85 C4 00 00 00               jne 0x140486455
00486391  8B CE                           mov ecx, esi
00486393  E8 C8 90 E8 FF                  call 0x14030f460
00486398  EB 94                           jmp 0x14048632e
0048639A  0B 7B 04                        or edi, dword ptr [rbx + 4]
0048639D  87 3B                           xchg dword ptr [rbx], edi
0048639F  89 7D 58                        mov dword ptr [rbp + 0x58], edi
004863A2  0F BA E7 1E                     bt edi, 0x1e
004863A6  0F 83 12 FF FF FF               jae 0x1404862be
004863AC  48 8B CB                        mov rcx, rbx
004863AF  E8 6C 18 D9 FF                  call 0x140217c20
004863B4  E9 05 FF FF FF                  jmp 0x1404862be
004863B9  0B 7B 04                        or edi, dword ptr [rbx + 4]
004863BC  87 3B                           xchg dword ptr [rbx], edi
004863BE  89 7D E0                        mov dword ptr [rbp - 0x20], edi
004863C1  0F BA E7 1E                     bt edi, 0x1e
004863C5  0F 83 6D FF FF FF               jae 0x140486338
004863CB  48 8B CB                        mov rcx, rbx
004863CE  E8 4D 18 D9 FF                  call 0x140217c20
004863D3  E9 60 FF FF FF                  jmp 0x140486338
004863D8  F7 05 56 07 B4 00 00 00 02 00   test dword ptr [rip + 0xb40756], 0x20000
004863E2  0F 84 52 FE FF FF               je 0x14048623a
004863E8  41 F6 C7 07                     test r15b, 7
004863EC  0F 85 48 FE FF FF               jne 0x14048623a
004863F2  8B 0B                           mov ecx, dword ptr [rbx]
004863F4  8B C1                           mov eax, ecx
004863F6  23 C6                           and eax, esi
004863F8  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
004863FB  3B C7                           cmp eax, edi
004863FD  0F 84 8C FD FF FF               je 0x14048618f
00486403  8B D1                           mov edx, ecx
00486405  44 8B C1                        mov r8d, ecx
00486408  E9 77 F1 26 00                  jmp 0x1406f5584
0048640D  F7 05 21 07 B4 00 00 00 02 00   test dword ptr [rip + 0xb40721], 0x20000
00486417  0F 84 FB FE FF FF               je 0x140486318
0048641D  41 F6 C4 07                     test r12b, 7
00486421  0F 85 F1 FE FF FF               jne 0x140486318
00486427  8B 0B                           mov ecx, dword ptr [rbx]
00486429  8B C1                           mov eax, ecx
0048642B  23 C6                           and eax, esi
0048642D  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
00486430  3B C7                           cmp eax, edi
00486432  0F 84 79 FE FF FF               je 0x1404862b1
00486438  8B D1                           mov edx, ecx
0048643A  44 8B C1                        mov r8d, ecx
0048643D  E9 B1 F1 26 00                  jmp 0x1406f55f3
00486442  4D 8B C5                        mov r8, r13
00486445  49 8B D7                        mov rdx, r15
00486448  49 8B CC                        mov rcx, r12
0048644B  E8 84 28 06 00                  call 0x1404e8cd4
00486450  E9 79 FE FF FF                  jmp 0x1404862ce
00486455  F7 05 D9 06 B4 00 00 00 02 00   test dword ptr [rip + 0xb406d9], 0x20000
0048645F  0F 84 2C FF FF FF               je 0x140486391
00486465  41 F6 C7 07                     test r15b, 7
00486469  0F 85 22 FF FF FF               jne 0x140486391
0048646F  8B 0B                           mov ecx, dword ptr [rbx]
00486471  8B C1                           mov eax, ecx
00486473  41 23 C5                        and eax, r13d
00486476  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
00486479  3B C7                           cmp eax, edi
0048647B  0F 84 AD FE FF FF               je 0x14048632e
00486481  8B D1                           mov edx, ecx
00486483  44 8B C1                        mov r8d, ecx
00486486  E9 B0 F1 26 00                  jmp 0x1406f563b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetSystemTimeDpc(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int8 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_00486247;
    v_r14 = 0;
    v_r15 = 0;
    goto loc_00486191;
loc_0048617D:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 11792677)) & ((unsigned int)(v_r14))) == 0) goto loc_0048620F;
loc_0048618D:
loc_0048618F:
loc_00486191:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_0048617D;
loc_00486198:
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned int *)(v_rip + 11792008)) == 0) goto loc_0048626D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) goto loc_00486268;
    v_r15 = (*(unsigned __int64 *)(v_rip + 11807355)) + (0x4100ULL);
loc_004861CC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16)) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(a2 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16)));
    *(unsigned __int64 *)(a2 + 24) = a1;
    a2 = 0;
    result = KiUpdateSystemTime(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    goto loc_00486281;
loc_0048620F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11798691)))) & (64)) == 0) goto loc_0048618D;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0048618D;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_004863D8;
loc_0048623A:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    goto loc_0048618F;
loc_00486247:
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a4 + 4)));
    v_stack_p10 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_00486198;
    result = KeWakeAddressAll(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    goto loc_00486198;
loc_00486268:
    v_r15 = 0;
    goto loc_00486281;
loc_0048626D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) != 0) goto loc_004861CC;
loc_00486281:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_0048639A;
    v_r14 = 0;
    v_r12 = 0;
    goto loc_004862B1;
loc_004862A3:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 11792383)) & ((unsigned int)(v_r14))) == 0) goto loc_004862F5;
loc_004862AF:
loc_004862B1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_004862A3;
loc_004862BE:
    if ((*(unsigned __int64 *)(a2 + 24)) == 0) goto loc_00486338;
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) + 16640 != 0) goto loc_00486442;
loc_004862CE:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_004863B9;
    v_rsi = 0;
    v_r15 = 0;
    goto loc_0048632E;
loc_004862F5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11798461)))) & (64)) == 0) goto loc_004862AF;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004862AF;
    v_r12 = (unsigned int)((v_stack_m50) + 1);
    result = KeCanUseHaltOnAddress(a4, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0048640D;
loc_00486318:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))), a4);
    goto loc_004862B1;
loc_00486322:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 11792258)) & ((unsigned int)(v_rsi))) == 0) goto loc_0048636E;
loc_0048632C:
loc_0048632E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_00486322;
loc_00486338:
    a4 = 0;
    a2 = 0;
    v_stack_m68 = 2;
    result = KiExitDispatcher(v_r12, a2, a4 + 1, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_0048636E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11798340)))) & (64)) == 0) goto loc_0048632C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r12, a2, a4 + 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0048632C;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(v_r12, a2, a4 + 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00486455;
loc_00486391:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, a4 + 1, a4);
    goto loc_0048632E;
loc_0048639A:
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(v_stack_p8 + 4)));
    v_stack_p20 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_004862BE;
    result = KeWakeAddressAll(v_stack_p8, a2, a4 + 1, a4);
    goto loc_004862BE;
loc_004863B9:
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(v_stack_p8 + 4)));
    v_stack_m58 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_00486338;
    result = KeWakeAddressAll(v_stack_p8, a2, a4 + 1, a4);
    goto loc_00486338;
loc_004863D8:
    if (((*(unsigned int *)(v_rip + 11798358)) & (0x20000ULL)) == 0) goto loc_0048623A;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_0048623A;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8))))) & ((unsigned int)(v_rsi)));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_0048618F;
loc_0048640D:
    if (((*(unsigned int *)(v_rip + 11798305)) & (0x20000ULL)) == 0) goto loc_00486318;
    if ((((unsigned __int8)(v_r12)) & (7)) != 0) goto loc_00486318;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8))))) & ((unsigned int)(v_rsi)));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_004862B1;
loc_00486442:
    result = KiAdjustTimerDueTimes(v_r12, v_r15, (unsigned int)(0x80000000ULL), a4);
    goto loc_004862CE;
loc_00486455:
    if (((*(unsigned int *)(v_rip + 11798233)) & (0x20000ULL)) == 0) goto loc_00486391;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_00486391;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_0048632E;
}
```

## 5. (Beta) C Style

```c
int64_t KiSetSystemTimeDpc(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint8_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_00486247;
    local_r14 = 0;
    local_r15 = 0;
    goto loc_00486191;
loc_0048617D:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xB3F125)) & ((uint32_t)(local_r14))) == 0) goto loc_0048620F;
loc_0048618D:
loc_0048618F:
loc_00486191:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_0048617D;
loc_00486198:
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint32_t *)(v_rip + 0xB3EE88)) == 0) goto loc_0048626D;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) goto loc_00486268;
    local_r15 = (*(uint64_t *)(v_rip + 0xB42A7B)) + (0x4100ULL);
loc_004861CC:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x10)) = *(uint64_t *)(Arg1);
    *(uint64_t *)(arg2 + 0x18) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) - (*(uint64_t *)(*(uint64_t *)(arg2 + 0x10)));
    *(uint64_t *)(arg2 + 0x18) = Arg1;
    Arg2 = 0;
    result = KiUpdateSystemTime(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    goto loc_00486281;
loc_0048620F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB408A3)))) & (64)) == 0) goto loc_0048618D;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0048618D;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_004863D8;
loc_0048623A:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    goto loc_0048618F;
loc_00486247:
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(arg4 + 0x4)));
    v_stack_p10 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_00486198;
    result = KeWakeAddressAll(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    goto loc_00486198;
loc_00486268:
    local_r15 = 0;
    goto loc_00486281;
loc_0048626D:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) != 0) goto loc_004861CC;
loc_00486281:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_0048639A;
    local_r14 = 0;
    local_r12 = 0;
    goto loc_004862B1;
loc_004862A3:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xB3EFFF)) & ((uint32_t)(local_r14))) == 0) goto loc_004862F5;
loc_004862AF:
loc_004862B1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_004862A3;
loc_004862BE:
    if ((*(uint64_t *)(arg2 + 0x18)) == 0) goto loc_00486338;
    if (*(uint64_t *)(gs_base + (0 + 0x20)) + 16640 != 0) goto loc_00486442;
loc_004862CE:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_004863B9;
    local_rsi = 0;
    local_r15 = 0;
    goto loc_0048632E;
loc_004862F5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB407BD)))) & (64)) == 0) goto loc_004862AF;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_004862AF;
    local_r12 = (uint32_t)((v_stack_m50) + 1);
    result = KeCanUseHaltOnAddress(Arg4, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0048640D;
loc_00486318:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))), Arg4);
    goto loc_004862B1;
loc_00486322:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xB3EF82)) & ((uint32_t)(local_rsi))) == 0) goto loc_0048636E;
loc_0048632C:
loc_0048632E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_00486322;
loc_00486338:
    Arg4 = 0;
    Arg2 = 0;
    v_stack_m68 = 2;
    result = KiExitDispatcher(local_r12, Arg2, Arg4 + 1, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_0048636E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB40744)))) & (64)) == 0) goto loc_0048632C;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r12, Arg2, Arg4 + 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0048632C;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(local_r12, Arg2, Arg4 + 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00486455;
loc_00486391:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), Arg2, Arg4 + 1, Arg4);
    goto loc_0048632E;
loc_0048639A:
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(v_stack_p8 + 0x4)));
    v_stack_p20 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_004862BE;
    result = KeWakeAddressAll(v_stack_p8, Arg2, Arg4 + 1, Arg4);
    goto loc_004862BE;
loc_004863B9:
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(v_stack_p8 + 0x4)));
    v_stack_m58 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_00486338;
    result = KeWakeAddressAll(v_stack_p8, Arg2, Arg4 + 1, Arg4);
    goto loc_00486338;
loc_004863D8:
    if (((*(uint32_t *)(v_rip + 0xB40756)) & (0x20000ULL)) == 0) goto loc_0048623A;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_0048623A;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8))))) & ((uint32_t)(local_rsi)));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_0048618F;
loc_0048640D:
    if (((*(uint32_t *)(v_rip + 0xB40721)) & (0x20000ULL)) == 0) goto loc_00486318;
    if ((((uint8_t)(local_r12)) & (7)) != 0) goto loc_00486318;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8))))) & ((uint32_t)(local_rsi)));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_004862B1;
loc_00486442:
    result = KiAdjustTimerDueTimes(local_r12, local_r15, (uint32_t)(0x80000000ULL), Arg4);
    goto loc_004862CE;
loc_00486455:
    if (((*(uint32_t *)(v_rip + 0xB406D9)) & (0x20000ULL)) == 0) goto loc_00486391;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_00486391;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_0048632E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00486130&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
