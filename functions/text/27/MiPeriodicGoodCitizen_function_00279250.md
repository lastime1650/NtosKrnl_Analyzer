# MiPeriodicGoodCitizen

- RVA: `0x00279250`–`0x002796B8` (길이 `1,128` bytes)
- VA: `0x0000000140279250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065FDC`
- 디코드: `263`개 명령, `1,128/1,128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00279563` → [EtwTraceShouldYieldProcessor](EtwTraceShouldYieldProcessor_function_00279088.md) (function, `0x00279088`)
- `0x002796A5` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- [sub_0024A490](../24/Unknown_function_0024A490.md) at `0x0024A4F1`
- [MiWalkPageTablesRecursively](MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B1E3`

### Static image references
- `0x002792AD` → RVA `0x00E38840` (`.data`; read)
- `0x002794C4` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00279550` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x002795BD` → RVA `0x00E2F1AC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00279250  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00279255  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0027925A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0027925F  57                              push rdi
00279260  48 83 EC 20                     sub rsp, 0x20
00279264  4C 8B C9                        mov r9, rcx
00279267  8B 09                           mov ecx, dword ptr [rcx]
00279269  F6 C1 02                        test cl, 2
0027926C  74 7A                           je 0x1402792e8
0027926E  41 0F B6 41 08                  movzx eax, byte ptr [r9 + 8]
00279273  41 84 81 A0 00 00 00            test byte ptr [r9 + 0xa0], al
0027927A  75 6C                           jne 0x1402792e8
0027927C  4D 8B 41 20                     mov r8, qword ptr [r9 + 0x20]
00279280  83 E1 04                        and ecx, 4
00279283  33 DB                           xor ebx, ebx
00279285  BD 01 00 00 00                  mov ebp, 1
0027928A  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00279291  24 0F                           and al, 0xf
00279293  3C 05                           cmp al, 5
00279295  0F 87 88 00 00 00               ja 0x140279323
0027929B  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
002792A2  24 0F                           and al, 0xf
002792A4  40 3A C5                        cmp al, bpl
002792A7  0F 85 FF 03 00 00               jne 0x1402796ac
002792AD  48 8D 05 8C F5 BB 00            lea rax, [rip + 0xbbf58c]
002792B4  4C 8B 18                        mov r11, qword ptr [rax]
002792B7  85 C9                           test ecx, ecx
002792B9  74 49                           je 0x140279304
002792BB  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002792C4  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002792CB  48 85 C9                        test rcx, rcx
002792CE  74 30                           je 0x140279300
002792D0  8B 81 44 01 00 00               mov eax, dword ptr [rcx + 0x144]
002792D6  48 C1 E0 06                     shl rax, 6
002792DA  42 8B 04 18                     mov eax, dword ptr [rax + r11]
002792DE  0F BA E0 1E                     bt eax, 0x1e
002792E2  73 3F                           jae 0x140279323
002792E4  8B C5                           mov eax, ebp
002792E6  EB 02                           jmp 0x1402792ea
002792E8  33 C0                           xor eax, eax
002792EA  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002792EF  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
002792F4  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002792F9  48 83 C4 20                     add rsp, 0x20
002792FD  5F                              pop rdi
002792FE  C3                              ret
002792FF  CC                              int3
00279300  8B C3                           mov eax, ebx
00279302  EB D2                           jmp 0x1402792d6
00279304  44 8B D3                        mov r10d, ebx
00279307  41 83 FA 04                     cmp r10d, 4
0027930B  73 16                           jae 0x140279323
0027930D  41 8B C2                        mov eax, r10d
00279310  48 C1 E0 06                     shl rax, 6
00279314  42 8B 0C 18                     mov ecx, dword ptr [rax + r11]
00279318  0F BA E1 1E                     bt ecx, 0x1e
0027931C  72 C6                           jb 0x1402792e4
0027931E  41 FF C2                        inc r10d
00279321  EB E4                           jmp 0x140279307
00279323  41 8B 01                        mov eax, dword ptr [r9]
00279326  A8 04                           test al, 4
00279328  0F 84 B5 00 00 00               je 0x1402793e3
0027932E  48 C1 EA 09                     shr rdx, 9
00279332  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027933C  48 23 D0                        and rdx, rax
0027933F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00279349  48 03 D0                        add rdx, rax
0027934C  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00279356  48 3B D0                        cmp rdx, rax
00279359  0F 84 16 02 00 00               je 0x140279575
0027935F  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00279366  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00279370  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
0027937A  A8 0F                           test al, 0xf
0027937C  0F 84 E9 00 00 00               je 0x14027946b
00279382  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00279389  A8 0F                           test al, 0xf
0027938B  74 14                           je 0x1402793a1
0027938D  49 8B C2                        mov rax, r10
00279390  48 3B D0                        cmp rdx, rax
00279393  72 0C                           jb 0x1402793a1
00279395  49 8B C3                        mov rax, r11
00279398  48 3B D0                        cmp rdx, rax
0027939B  0F 86 01 02 00 00               jbe 0x1402795a2
002793A1  48 8B 02                        mov rax, qword ptr [rdx]
002793A4  49 8B CA                        mov rcx, r10
002793A7  48 3B D1                        cmp rdx, rcx
002793AA  72 28                           jb 0x1402793d4
002793AC  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
002793B6  48 3B D1                        cmp rdx, rcx
002793B9  77 19                           ja 0x1402793d4
002793BB  40 84 C5                        test bpl, al
002793BE  74 14                           je 0x1402793d4
002793C0  A8 42                           test al, 0x42
002793C2  41 0F 95 C0                     setne r8b
002793C6  A8 20                           test al, 0x20
002793C8  0F 95 C1                        setne cl
002793CB  44 84 C1                        test cl, r8b
002793CE  0F 84 F0 00 00 00               je 0x1402794c4
002793D4  48 C1 E8 3C                     shr rax, 0x3c
002793D8  83 E0 02                        and eax, 2
002793DB  85 C0                           test eax, eax
002793DD  0F 85 01 FF FF FF               jne 0x1402792e4
002793E3  41 80 79 09 02                  cmp byte ptr [r9 + 9], 2
002793E8  0F 83 FA FE FF FF               jae 0x1402792e8
002793EE  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002793F7  44 8B C3                        mov r8d, ebx
002793FA  44 8B CB                        mov r9d, ebx
002793FD  8B 91 BC 38 00 00               mov edx, dword ptr [rcx + 0x38bc]
00279403  8B B9 AC 83 00 00               mov edi, dword ptr [rcx + 0x83ac]
00279409  8B B1 5C 86 00 00               mov esi, dword ptr [rcx + 0x865c]
0027940F  40 84 D5                        test bpl, dl
00279412  0F 85 14 01 00 00               jne 0x14027952c
00279418  38 59 20                        cmp byte ptr [rcx + 0x20], bl
0027941B  0F 85 CD 01 00 00               jne 0x1402795ee
00279421  F6 C2 1E                        test dl, 0x1e
00279424  0F 85 21 01 00 00               jne 0x14027954b
0027942A  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00279431  84 C0                           test al, al
00279433  0F 85 DA 01 00 00               jne 0x140279613
00279439  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0027943D  48 85 C0                        test rax, rax
00279440  0F 85 94 01 00 00               jne 0x1402795da
00279446  83 FF 07                        cmp edi, 7
00279449  0F 86 99 FE FF FF               jbe 0x1402792e8
0027944F  45 85 C0                        test r8d, r8d
00279452  0F 84 C5 01 00 00               je 0x14027961d
00279458  F6 C2 1E                        test dl, 0x1e
0027945B  0F 84 ED 01 00 00               je 0x14027964e
00279461  BB 05 00 00 00                  mov ebx, 5
00279466  E9 E5 00 00 00                  jmp 0x140279550
0027946B  49 8B C2                        mov rax, r10
0027946E  48 3B D0                        cmp rdx, rax
00279471  0F 82 0B FF FF FF               jb 0x140279382
00279477  49 8B C3                        mov rax, r11
0027947A  48 3B D0                        cmp rdx, rax
0027947D  0F 87 FF FE FF FF               ja 0x140279382
00279483  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027948C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00279493  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027949A  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
002794A1  48 85 C9                        test rcx, rcx
002794A4  0F 84 D8 FE FF FF               je 0x140279382
002794AA  C1 EA 03                        shr edx, 3
002794AD  8B C3                           mov eax, ebx
002794AF  81 E2 FF 01 00 00               and edx, 0x1ff
002794B5  8B 0C 91                        mov ecx, dword ptr [rcx + rdx*4]
002794B8  0F BA E1 1E                     bt ecx, 0x1e
002794BC  0F 42 C5                        cmovb eax, ebp
002794BF  E9 17 FF FF FF                  jmp 0x1402793db
002794C4  48 F7 05 B9 D5 D4 00 00 00 60 00  test qword ptr [rip + 0xd4d5b9], 0x600000
002794CF  0F 84 FF FE FF FF               je 0x1402793d4
002794D5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002794DE  4C 8B 81 B8 00 00 00            mov r8, qword ptr [rcx + 0xb8]
002794E5  41 38 A8 60 01 00 00            cmp byte ptr [r8 + 0x160], bpl
002794EC  0F 84 E2 FE FF FF               je 0x1402793d4
002794F2  49 8B 88 08 05 00 00            mov rcx, qword ptr [r8 + 0x508]
002794F9  48 85 C9                        test rcx, rcx
002794FC  0F 84 D2 FE FF FF               je 0x1402793d4
00279502  48 C1 EA 03                     shr rdx, 3
00279506  81 E2 FF 01 00 00               and edx, 0x1ff
0027950C  48 8B 0C D1                     mov rcx, qword ptr [rcx + rdx*8]
00279510  F6 C1 20                        test cl, 0x20
00279513  74 04                           je 0x140279519
00279515  48 83 C8 20                     or rax, 0x20
00279519  48 8B D0                        mov rdx, rax
0027951C  48 83 C8 42                     or rax, 0x42
00279520  F6 C1 42                        test cl, 0x42
00279523  48 0F 44 C2                     cmove rax, rdx
00279527  E9 A8 FE FF FF                  jmp 0x1402793d4
0027952C  44 8B C5                        mov r8d, ebp
0027952F  83 FE 07                        cmp esi, 7
00279532  0F 86 0E FF FF FF               jbe 0x140279446
00279538  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0027953F  84 C0                           test al, al
00279541  0F 84 11 FF FF FF               je 0x140279458
00279547  8B DD                           mov ebx, ebp
00279549  EB 05                           jmp 0x140279550
0027954B  BB 02 00 00 00                  mov ebx, 2
00279550  F7 05 AA D5 D4 00 00 00 00 04   test dword ptr [rip + 0xd4d5aa], 0x4000000
0027955A  74 0C                           je 0x140279568
0027955C  44 8B C6                        mov r8d, esi
0027955F  8B D7                           mov edx, edi
00279561  8B CB                           mov ecx, ebx
00279563  E8 20 FB FF FF                  call 0x140279088
00279568  85 DB                           test ebx, ebx
0027956A  0F 84 78 FD FF FF               je 0x1402792e8
00279570  E9 6F FD FF FF                  jmp 0x1402792e4
00279575  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0027957E  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00279585  24 0F                           and al, 0xf
00279587  0F 85 D5 00 00 00               jne 0x140279662
0027958D  B9 30 00 00 00                  mov ecx, 0x30
00279592  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
0027959A  48 85 C0                        test rax, rax
0027959D  E9 3B FE FF FF                  jmp 0x1402793dd
002795A2  49 8B C2                        mov rax, r10
002795A5  48 2B D0                        sub rdx, rax
002795A8  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
002795AF  48 C1 FA 03                     sar rdx, 3
002795B3  03 D2                           add edx, edx
002795B5  8B C2                           mov eax, edx
002795B7  8B CA                           mov ecx, edx
002795B9  48 C1 E8 05                     shr rax, 5
002795BD  48 8D 15 E8 5B BB 00            lea rdx, [rip + 0xbb5be8]
002795C4  83 E1 1F                        and ecx, 0x1f
002795C7  8B 14 82                        mov edx, dword ptr [rdx + rax*4]
002795CA  D3 EA                           shr edx, cl
002795CC  F6 C2 02                        test dl, 2
002795CF  0F 84 0E FE FF FF               je 0x1402793e3
002795D5  E9 0A FD FF FF                  jmp 0x1402792e4
002795DA  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
002795DE  0F 84 62 FE FF FF               je 0x140279446
002795E4  BB 04 00 00 00                  mov ebx, 4
002795E9  E9 62 FF FF FF                  jmp 0x140279550
002795EE  44 8B CD                        mov r9d, ebp
002795F1  83 FF 07                        cmp edi, 7
002795F4  0F 86 EE FC FF FF               jbe 0x1402792e8
002795FA  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00279601  84 C0                           test al, al
00279603  0F 84 4F FE FF FF               je 0x140279458
00279609  BB 07 00 00 00                  mov ebx, 7
0027960E  E9 3D FF FF FF                  jmp 0x140279550
00279613  BB 03 00 00 00                  mov ebx, 3
00279618  E9 33 FF FF FF                  jmp 0x140279550
0027961D  45 85 C9                        test r9d, r9d
00279620  0F 85 32 FE FF FF               jne 0x140279458
00279626  FA                              cli
00279627  89 99 AC 83 00 00               mov dword ptr [rcx + 0x83ac], ebx
0027962D  89 99 5C 86 00 00               mov dword ptr [rcx + 0x865c], ebx
00279633  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0027963C  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00279643  4D 85 C0                        test r8, r8
00279646  75 43                           jne 0x14027968b
00279648  FB                              sti
00279649  E9 02 FF FF FF                  jmp 0x140279550
0027964E  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00279652  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00279656  74 CE                           je 0x140279626
00279658  BB 06 00 00 00                  mov ebx, 6
0027965D  E9 EE FE FF FF                  jmp 0x140279550
00279662  3C 07                           cmp al, 7
00279664  74 10                           je 0x140279676
00279666  3C 05                           cmp al, 5
00279668  B9 48 00 00 00                  mov ecx, 0x48
0027966D  48 0F 44 CB                     cmove rcx, rbx
00279671  E9 1C FF FF FF                  jmp 0x140279592
00279676  B9 18 00 00 00                  mov ecx, 0x18
0027967B  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
00279683  48 85 C0                        test rax, rax
00279686  E9 52 FD FF FF                  jmp 0x1402793dd
0027968B  41 0F 0D 08                     prefetchw byte ptr [r8]
0027968F  41 8B 00                        mov eax, dword ptr [r8]
00279692  8B D0                           mov edx, eax
00279694  0F BA F2 15                     btr edx, 0x15
00279698  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0027969D  75 F3                           jne 0x140279692
0027969F  0F BA E0 15                     bt eax, 0x15
002796A3  73 A3                           jae 0x140279648
002796A5  E8 26 9B FE FF                  call 0x1402631d0
002796AA  EB 9C                           jmp 0x140279648
002796AC  49 8D 80 C0 00 00 00            lea rax, [r8 + 0xc0]
002796B3  E9 FC FB FF FF                  jmp 0x1402792b4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPeriodicGoodCitizen(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_002792E8;
    if (((*(unsigned __int8 *)(a1 + 160)) & ((unsigned __int8)(*(unsigned __int8 *)(a1 + 8)))) != 0) goto loc_002792E8;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (4));
    v_rbx = 0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_00279323;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_002796AC;
loc_002792B4:
    if ((unsigned int)(a1) == 0) goto loc_00279304;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_00279300;
loc_002792D6:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))) << (6);
    if (condition_is_above_or_equal) goto loc_00279323;
loc_002792E4:
    goto loc_002792EA;
loc_002792E8:
    result = 0;
loc_002792EA:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00279300:
    goto loc_002792D6;
loc_00279304:
loc_00279307:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) >= 4) goto loc_00279323;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))))) << (6);
    if (condition_is_below) goto loc_002792E4;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) + 1);
    goto loc_00279307;
loc_00279323:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) == 0) goto loc_002793E3;
    a2 = (a2) >> (9);
    a2 = (a2) & ((unsigned int)(*(unsigned int *)(a1)));
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(a1)));
    if (a2 == ((unsigned int)(*(unsigned int *)(a1)))) goto loc_00279575;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) == 0) goto loc_0027946B;
loc_00279382:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) == 0) goto loc_002793A1;
    if (a2 < v_r10) goto loc_002793A1;
    if (a2 <= (*(unsigned __int64 *)(v_rip + 12318092))) goto loc_002795A2;
loc_002793A1:
    if (a2 < v_r10) goto loc_002793D4;
    if (a2 > v_r10) goto loc_002793D4;
    if ((((unsigned __int8)(v_stack_p10)) & ((unsigned __int8)(*(unsigned __int64 *)(a2)))) == 0) goto loc_002793D4;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a3))) == 0) goto loc_002794C4;
loc_002793D4:
    result = (*(unsigned __int64 *)(a2)) >> (60);
    result = (unsigned int)((result) & (2));
loc_002793DB:
loc_002793DD:
    if ((unsigned int)(result) != 0) goto loc_002792E4;
loc_002793E3:
    if ((*(unsigned __int8 *)(a1 + 9)) >= 2) goto loc_002792E8;
    if ((((unsigned __int8)(v_stack_p10)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524))))) != 0) goto loc_0027952C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != ((unsigned __int8)(v_stack_p8))) goto loc_002795EE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) != 0) goto loc_0027954B;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) != 0) goto loc_00279613;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) != 0) goto loc_002795DA;
loc_00279446:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_002792E8;
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) == 0) goto loc_0027961D;
loc_00279458:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) == 0) goto loc_0027964E;
    goto loc_00279550;
loc_0027946B:
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524))) < v_r10) goto loc_00279382;
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524))) > (*(unsigned __int64 *)(v_rip + 12318092))) goto loc_00279382;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_00279382;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524))) >> (3));
    a2 = (unsigned int)((a2) & (511));
    result = 5;
    if (condition_is_below) { result = (unsigned int)(v_stack_p10); }
    goto loc_002793DB;
loc_002794C4:
    if (((*(unsigned __int64 *)(v_rip + 13948345)) & (0x600000ULL)) == 0) goto loc_002793D4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == ((unsigned __int8)(v_stack_p10))) goto loc_002793D4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002793D4;
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8))) & (66)) == 0) { result = result; }
    goto loc_002793D4;
loc_0027952C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)))) <= 7) goto loc_00279446;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8) + 14521)) == 0) goto loc_00279458;
    goto loc_00279550;
loc_0027954B:
loc_00279550:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8) + 14521);
    if (((*(unsigned int *)(v_rip + 13948330)) & (0x4000000ULL)) != 0) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)));
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)));
        a1 = 2;
        result = EtwTraceShouldYieldProcessor(a1, a2, a3, (unsigned int)((unsigned int)(v_stack_p8)));
    }
    if (2 == 0) goto loc_002792E8;
    goto loc_002792E4;
loc_00279575:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a3 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00279662;
loc_00279592:
    goto loc_002793DD;
loc_002795A2:
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32))) - (v_r10);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    result = ((unsigned int)((unsigned int)(a2))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12278760 + result * 4))) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(a2)) & (2)) == 0) goto loc_002793E3;
    goto loc_002792E4;
loc_002795DA:
    if (result == (*(unsigned __int64 *)(a1 + 8))) goto loc_00279446;
    goto loc_00279550;
loc_002795EE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_002792E8;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14521)) == 0) goto loc_00279458;
    goto loc_00279550;
loc_00279613:
    goto loc_00279550;
loc_0027961D:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10))) != 0) goto loc_00279458;
loc_00279626:
    *(unsigned int *)(a1 + 33708) = 3;
    *(unsigned int *)(a1 + 34396) = 3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0027968B;
loc_00279648:
    goto loc_00279550;
loc_0027964E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_00279626;
    goto loc_00279550;
loc_00279662:
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) == 7) goto loc_00279676;
    a1 = 72;
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) == 5) { a1 = 6; }
    goto loc_00279592;
loc_00279676:
    goto loc_002793DD;
loc_0027968B:
loc_00279692:
    if (*(unsigned __int64 *)(24 + a2 * 1 + 40000) != 0) goto loc_00279692;
    if (condition_is_above_or_equal) goto loc_00279648;
    result = KiRemoveSystemWorkPriorityKick(24, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)((unsigned int)(v_stack_p10)));
    goto loc_00279648;
loc_002796AC:
    goto loc_002792B4;
}
```

## 5. (Beta) C Style

```c
int64_t MiPeriodicGoodCitizen(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_002792E8;
    if (((*(uint8_t *)(arg1 + 0xA0)) & ((uint8_t)(*(uint8_t *)(arg1 + 0x8)))) != 0) goto loc_002792E8;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (4));
    local_rbx = 0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_00279323;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_002796AC;
loc_002792B4:
    if ((uint32_t)(Arg1) == 0) goto loc_00279304;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_00279300;
loc_002792D6:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))) << (6);
    if (condition_is_above_or_equal) goto loc_00279323;
loc_002792E4:
    goto loc_002792EA;
loc_002792E8:
    result = 0;
loc_002792EA:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00279300:
    goto loc_002792D6;
loc_00279304:
loc_00279307:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) >= 4) goto loc_00279323;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))))) << (6);
    if (condition_is_below) goto loc_002792E4;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) + 1);
    goto loc_00279307;
loc_00279323:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) == 0) goto loc_002793E3;
    Arg2 = (Arg2) >> (9);
    Arg2 = (Arg2) & ((uint32_t)(*(uint32_t *)(arg1)));
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(arg1)));
    if (Arg2 == ((uint32_t)(*(uint32_t *)(arg1)))) goto loc_00279575;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) == 0) goto loc_0027946B;
loc_00279382:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) == 0) goto loc_002793A1;
    if (Arg2 < local_r10) goto loc_002793A1;
    if (Arg2 <= (*(uint64_t *)(v_rip + 0xBBF58C))) goto loc_002795A2;
loc_002793A1:
    if (Arg2 < local_r10) goto loc_002793D4;
    if (Arg2 > local_r10) goto loc_002793D4;
    if ((((uint8_t)(v_stack_p10)) & ((uint8_t)(*(uint64_t *)(Arg2)))) == 0) goto loc_002793D4;
    a3 = ((((uint8_t)(*(uint64_t *)(Arg2))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg2))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a3))) == 0) goto loc_002794C4;
loc_002793D4:
    result = (*(uint64_t *)(Arg2)) >> (60);
    result = (uint32_t)((result) & (2));
loc_002793DB:
loc_002793DD:
    if ((uint32_t)(result) != 0) goto loc_002792E4;
loc_002793E3:
    if ((*(uint8_t *)(arg1 + 0x9)) >= 2) goto loc_002792E8;
    if ((((uint8_t)(v_stack_p10)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC))))) != 0) goto loc_0027952C;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != ((uint8_t)(v_stack_p8))) goto loc_002795EE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) != 0) goto loc_0027954B;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) != 0) goto loc_00279613;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) != 0) goto loc_002795DA;
loc_00279446:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_002792E8;
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) == 0) goto loc_0027961D;
loc_00279458:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) == 0) goto loc_0027964E;
    goto loc_00279550;
loc_0027946B:
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC))) < local_r10) goto loc_00279382;
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC))) > (*(uint64_t *)(v_rip + 0xBBF58C))) goto loc_00279382;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_00279382;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (511));
    result = 5;
    if (condition_is_below) { result = (uint32_t)(v_stack_p10); }
    goto loc_002793DB;
loc_002794C4:
    if (((*(uint64_t *)(v_rip + 0xD4D5B9)) & (0x600000ULL)) == 0) goto loc_002793D4;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == ((uint8_t)(v_stack_p10))) goto loc_002793D4;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002793D4;
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg2 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg2 * 8))) & (66)) == 0) { result = result; }
    goto loc_002793D4;
loc_0027952C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)))) <= 7) goto loc_00279446;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg2 * 8) + 0x38B9)) == 0) goto loc_00279458;
    goto loc_00279550;
loc_0027954B:
loc_00279550:
    result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg2 * 8) + 0x38B9);
    if (((*(uint32_t *)(v_rip + 0xD4D5AA)) & (0x4000000ULL)) != 0) {
        a3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)));
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)));
        Arg1 = 2;
        result = EtwTraceShouldYieldProcessor(Arg1, Arg2, a3, (uint32_t)((uint32_t)(v_stack_p8)));
    }
    if (2 == 0) goto loc_002792E8;
    goto loc_002792E4;
loc_00279575:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(a3 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00279662;
loc_00279592:
    goto loc_002793DD;
loc_002795A2:
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20))) - (local_r10);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    result = ((uint32_t)((uint32_t)(Arg2))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBB5BE8 + result * 4))) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(Arg2)) & (2)) == 0) goto loc_002793E3;
    goto loc_002792E4;
loc_002795DA:
    if (result == (*(uint64_t *)(arg1 + 0x8))) goto loc_00279446;
    goto loc_00279550;
loc_002795EE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_002792E8;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x38B9)) == 0) goto loc_00279458;
    goto loc_00279550;
loc_00279613:
    goto loc_00279550;
loc_0027961D:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10))) != 0) goto loc_00279458;
loc_00279626:
    *(uint32_t *)(arg1 + 0x83AC) = 3;
    *(uint32_t *)(arg1 + 0x865C) = 3;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0027968B;
loc_00279648:
    goto loc_00279550;
loc_0027964E:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_00279626;
    goto loc_00279550;
loc_00279662:
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) == 7) goto loc_00279676;
    Arg1 = 72;
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) == 5) { Arg1 = 6; }
    goto loc_00279592;
loc_00279676:
    goto loc_002793DD;
loc_0027968B:
loc_00279692:
    if (*(uint64_t *)(24 + Arg2 * 1 + 0x9C40) != 0) goto loc_00279692;
    if (condition_is_above_or_equal) goto loc_00279648;
    result = KiRemoveSystemWorkPriorityKick(24, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)((uint32_t)(v_stack_p10)));
    goto loc_00279648;
loc_002796AC:
    goto loc_002792B4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00279250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
