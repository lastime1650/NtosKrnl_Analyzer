# MiInvalidatePageFileBitmapsCache

- RVA: `0x003E3240`–`0x003E34FF` (길이 `703` bytes)
- VA: `0x00000001403E3240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00094C60`
- 디코드: `202`개 명령, `703/703` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E3306` → [MiBitmapsCachedEntryLengthChanged](MiBitmapsCachedEntryLengthChanged_function_003E3508.md) (function, `0x003E3508`)
- `0x003E3311` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x003E3321` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x003E3395` → [MiBitmapsCachedEntryLengthChanged](MiBitmapsCachedEntryLengthChanged_function_003E3508.md) (function, `0x003E3508`)
- `0x003E3407` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x003E344F` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x003733FA`
- [MiFindFreePageFileSpace](MiFindFreePageFileSpace_function_003E2CAC.md) at `0x003E2FDF`
- [sub_006F503A](../6F/Unknown_function_006F503A.md) at `0x006F5154`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003E34EC` → [sub_006EA872](../6E/Unknown_function_006EA872.md) (`tail-transfer`)
  - `0x003E34FA` → [sub_006EA872 + 0xF](../6E/Unknown_function_006EA872.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E3240  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003E3245  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003E324A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
003E324F  41 56                           push r14
003E3251  48 83 EC 20                     sub rsp, 0x20
003E3255  49 8B F9                        mov rdi, r9
003E3258  33 DB                           xor ebx, ebx
003E325A  45 8B D0                        mov r10d, r8d
003E325D  44 8B CA                        mov r9d, edx
003E3260  48 8B F1                        mov rsi, rcx
003E3263  48 85 FF                        test rdi, rdi
003E3266  75 71                           jne 0x1403e32d9
003E3268  48 83 E9 80                     sub rcx, -0x80
003E326C  F6 41 08 01                     test byte ptr [rcx + 8], 1
003E3270  48 8B 11                        mov rdx, qword ptr [rcx]
003E3273  0F 85 E8 01 00 00               jne 0x1403e3461
003E3279  44 0F B6 41 08                  movzx r8d, byte ptr [rcx + 8]
003E327E  41 83 E0 01                     and r8d, 1
003E3282  48 85 D2                        test rdx, rdx
003E3285  74 37                           je 0x1403e32be
003E3287  47 8D 1C 11                     lea r11d, [r9 + r10]
003E328B  8B 4A 18                        mov ecx, dword ptr [rdx + 0x18]
003E328E  44 3B D9                        cmp r11d, ecx
003E3291  0F 86 4A 02 00 00               jbe 0x1403e34e1
003E3297  03 4A 1C                        add ecx, dword ptr [rdx + 0x1c]
003E329A  44 3B C9                        cmp r9d, ecx
003E329D  72 1A                           jb 0x1403e32b9
003E329F  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003E32A3  45 85 C0                        test r8d, r8d
003E32A6  74 09                           je 0x1403e32b1
003E32A8  48 85 C0                        test rax, rax
003E32AB  0F 85 A8 01 00 00               jne 0x1403e3459
003E32B1  48 8B D0                        mov rdx, rax
003E32B4  48 85 D2                        test rdx, rdx
003E32B7  75 D2                           jne 0x1403e328b
003E32B9  48 85 D2                        test rdx, rdx
003E32BC  75 17                           jne 0x1403e32d5
003E32BE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003E32C3  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003E32C8  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
003E32CD  48 83 C4 20                     add rsp, 0x20
003E32D1  41 5E                           pop r14
003E32D3  C3                              ret
003E32D4  CC                              int3
003E32D5  48 8D 7A E8                     lea rdi, [rdx - 0x18]
003E32D9  44 8B 47 30                     mov r8d, dword ptr [rdi + 0x30]
003E32DD  48 8D 57 34                     lea rdx, [rdi + 0x34]
003E32E1  45 3B C1                        cmp r8d, r9d
003E32E4  75 5B                           jne 0x1403e3341
003E32E6  8B 0A                           mov ecx, dword ptr [rdx]
003E32E8  41 2B CA                        sub ecx, r10d
003E32EB  89 0A                           mov dword ptr [rdx], ecx
003E32ED  45 3B C1                        cmp r8d, r9d
003E32F0  75 07                           jne 0x1403e32f9
003E32F2  43 8D 04 10                     lea eax, [r8 + r10]
003E32F6  89 47 30                        mov dword ptr [rdi + 0x30], eax
003E32F9  48 8B D7                        mov rdx, rdi
003E32FC  85 C9                           test ecx, ecx
003E32FE  74 0D                           je 0x1403e330d
003E3300  45 33 C0                        xor r8d, r8d
003E3303  48 8B CE                        mov rcx, rsi
003E3306  E8 FD 01 00 00                  call 0x1403e3508
003E330B  EB B1                           jmp 0x1403e32be
003E330D  48 8D 4E 70                     lea rcx, [rsi + 0x70]
003E3311  E8 FA 18 F0 FF                  call 0x1402e4c10
003E3316  48 8D 57 18                     lea rdx, [rdi + 0x18]
003E331A  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
003E3321  E8 EA 18 F0 FF                  call 0x1402e4c10
003E3326  48 81 C6 90 00 00 00            add rsi, 0x90
003E332D  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003E3331  48 39 30                        cmp qword ptr [rax], rsi
003E3334  0F 84 6A 01 00 00               je 0x1403e34a4
003E333A  B9 03 00 00 00                  mov ecx, 3
003E333F  CD 29                           int 0x29
003E3341  8B 0A                           mov ecx, dword ptr [rdx]
003E3343  47 8D 1C 11                     lea r11d, [r9 + r10]
003E3347  41 03 C8                        add ecx, r8d
003E334A  44 3B D9                        cmp r11d, ecx
003E334D  74 97                           je 0x1403e32e6
003E334F  41 2B C9                        sub ecx, r9d
003E3352  48 8D 86 90 00 00 00            lea rax, [rsi + 0x90]
003E3359  4C 8B 30                        mov r14, qword ptr [rax]
003E335C  41 2B CA                        sub ecx, r10d
003E335F  45 2B C8                        sub r9d, r8d
003E3362  4C 3B F0                        cmp r14, rax
003E3365  0F 84 7E 01 00 00               je 0x1403e34e9
003E336B  49 39 46 08                     cmp qword ptr [r14 + 8], rax
003E336F  75 C9                           jne 0x1403e333a
003E3371  4D 8B 06                        mov r8, qword ptr [r14]
003E3374  4D 39 70 08                     cmp qword ptr [r8 + 8], r14
003E3378  75 C0                           jne 0x1403e333a
003E337A  4C 89 00                        mov qword ptr [rax], r8
003E337D  49 89 40 08                     mov qword ptr [r8 + 8], rax
003E3381  45 33 C0                        xor r8d, r8d
003E3384  41 89 4E 34                     mov dword ptr [r14 + 0x34], ecx
003E3388  48 8B CE                        mov rcx, rsi
003E338B  45 89 5E 30                     mov dword ptr [r14 + 0x30], r11d
003E338F  44 89 0A                        mov dword ptr [rdx], r9d
003E3392  48 8B D7                        mov rdx, rdi
003E3395  E8 6E 01 00 00                  call 0x1403e3508
003E339A  48 8D 4E 70                     lea rcx, [rsi + 0x70]
003E339E  F6 41 08 01                     test byte ptr [rcx + 8], 1
003E33A2  48 8B 11                        mov rdx, qword ptr [rcx]
003E33A5  0F 85 0C 01 00 00               jne 0x1403e34b7
003E33AB  44 0F B6 49 08                  movzx r9d, byte ptr [rcx + 8]
003E33B0  44 8A C3                        mov r8b, bl
003E33B3  41 83 E1 01                     and r9d, 1
003E33B7  48 85 D2                        test rdx, rdx
003E33BA  74 48                           je 0x1403e3404
003E33BC  45 8B 46 34                     mov r8d, dword ptr [r14 + 0x34]
003E33C0  44 3B 42 34                     cmp r8d, dword ptr [rdx + 0x34]
003E33C4  77 2D                           ja 0x1403e33f3
003E33C6  72 09                           jb 0x1403e33d1
003E33C8  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
003E33CB  41 39 46 30                     cmp dword ptr [r14 + 0x30], eax
003E33CF  73 22                           jae 0x1403e33f3
003E33D1  48 8B 02                        mov rax, qword ptr [rdx]
003E33D4  45 85 C9                        test r9d, r9d
003E33D7  74 0C                           je 0x1403e33e5
003E33D9  48 85 C0                        test rax, rax
003E33DC  0F 84 F7 00 00 00               je 0x1403e34d9
003E33E2  48 33 C2                        xor rax, rdx
003E33E5  48 85 C0                        test rax, rax
003E33E8  0F 84 EB 00 00 00               je 0x1403e34d9
003E33EE  48 8B D0                        mov rdx, rax
003E33F1  EB CD                           jmp 0x1403e33c0
003E33F3  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003E33F7  45 85 C9                        test r9d, r9d
003E33FA  74 79                           je 0x1403e3475
003E33FC  48 85 C0                        test rax, rax
003E33FF  75 71                           jne 0x1403e3472
003E3401  41 B0 01                        mov r8b, 1
003E3404  4D 8B CE                        mov r9, r14
003E3407  E8 64 11 F0 FF                  call 0x1402e4570
003E340C  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
003E3413  F6 41 08 01                     test byte ptr [rcx + 8], 1
003E3417  48 8B 11                        mov rdx, qword ptr [rcx]
003E341A  0F 85 A8 00 00 00               jne 0x1403e34c8
003E3420  44 0F B6 41 08                  movzx r8d, byte ptr [rcx + 8]
003E3425  41 83 E0 01                     and r8d, 1
003E3429  48 85 D2                        test rdx, rdx
003E342C  74 1A                           je 0x1403e3448
003E342E  45 8B 4E 30                     mov r9d, dword ptr [r14 + 0x30]
003E3432  44 3B 4A 18                     cmp r9d, dword ptr [rdx + 0x18]
003E3436  72 52                           jb 0x1403e348a
003E3438  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003E343C  45 85 C0                        test r8d, r8d
003E343F  74 42                           je 0x1403e3483
003E3441  48 85 C0                        test rax, rax
003E3444  75 3A                           jne 0x1403e3480
003E3446  B3 01                           mov bl, 1
003E3448  4D 8D 4E 18                     lea r9, [r14 + 0x18]
003E344C  44 8A C3                        mov r8b, bl
003E344F  E8 1C 11 F0 FF                  call 0x1402e4570
003E3454  E9 65 FE FF FF                  jmp 0x1403e32be
003E3459  48 33 D0                        xor rdx, rax
003E345C  E9 53 FE FF FF                  jmp 0x1403e32b4
003E3461  48 85 D2                        test rdx, rdx
003E3464  0F 84 0F FE FF FF               je 0x1403e3279
003E346A  48 33 D1                        xor rdx, rcx
003E346D  E9 07 FE FF FF                  jmp 0x1403e3279
003E3472  48 33 C2                        xor rax, rdx
003E3475  48 85 C0                        test rax, rax
003E3478  0F 85 70 FF FF FF               jne 0x1403e33ee
003E347E  EB 81                           jmp 0x1403e3401
003E3480  48 33 C2                        xor rax, rdx
003E3483  48 85 C0                        test rax, rax
003E3486  74 BE                           je 0x1403e3446
003E3488  EB 15                           jmp 0x1403e349f
003E348A  48 8B 02                        mov rax, qword ptr [rdx]
003E348D  45 85 C0                        test r8d, r8d
003E3490  74 08                           je 0x1403e349a
003E3492  48 85 C0                        test rax, rax
003E3495  74 B1                           je 0x1403e3448
003E3497  48 33 C2                        xor rax, rdx
003E349A  48 85 C0                        test rax, rax
003E349D  74 A9                           je 0x1403e3448
003E349F  48 8B D0                        mov rdx, rax
003E34A2  EB 8E                           jmp 0x1403e3432
003E34A4  48 89 37                        mov qword ptr [rdi], rsi
003E34A7  48 89 47 08                     mov qword ptr [rdi + 8], rax
003E34AB  48 89 38                        mov qword ptr [rax], rdi
003E34AE  48 89 7E 08                     mov qword ptr [rsi + 8], rdi
003E34B2  E9 07 FE FF FF                  jmp 0x1403e32be
003E34B7  48 85 D2                        test rdx, rdx
003E34BA  0F 84 EB FE FF FF               je 0x1403e33ab
003E34C0  48 33 D1                        xor rdx, rcx
003E34C3  E9 E3 FE FF FF                  jmp 0x1403e33ab
003E34C8  48 85 D2                        test rdx, rdx
003E34CB  0F 84 4F FF FF FF               je 0x1403e3420
003E34D1  48 33 D1                        xor rdx, rcx
003E34D4  E9 47 FF FF FF                  jmp 0x1403e3420
003E34D9  44 8A C3                        mov r8b, bl
003E34DC  E9 23 FF FF FF                  jmp 0x1403e3404
003E34E1  48 8B 02                        mov rax, qword ptr [rdx]
003E34E4  E9 BA FD FF FF                  jmp 0x1403e32a3
003E34E9  44 3B C9                        cmp r9d, ecx
003E34EC  0F 86 80 73 30 00               jbe 0x1406ea872
003E34F2  44 89 0A                        mov dword ptr [rdx], r9d
003E34F5  8B 46 6C                        mov eax, dword ptr [rsi + 0x6c]
003E34F8  3B C1                           cmp eax, ecx
003E34FA  E9 82 73 30 00                  jmp 0x1406ea881
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInvalidatePageFileBitmapsCache(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (a4 != 0) goto loc_003E32D9;
    a1 = (a1) - (-128);
    if (((*(unsigned __int8 *)(a1 + 8)) & (1)) != 0) goto loc_003E3461;
loc_003E3279:
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 8)) & (1));
    if (*(unsigned __int64 *)(a1) == 0) goto loc_003E32BE;
loc_003E328B:
    if (((unsigned int)((unsigned int)(a2) + (unsigned int)(a3) * 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24))))) goto loc_003E34E1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 24))) + (*(unsigned int *)(*(unsigned __int64 *)(a1) + 28)));
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)(a1))) goto loc_003E32B9;
loc_003E32A3:
    if (a3 == 0) goto loc_003E32B1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) != 0) goto loc_003E3459;
loc_003E32B1:
loc_003E32B4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) != 0) goto loc_003E328B;
loc_003E32B9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) != 0) goto loc_003E32D5;
loc_003E32BE:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8);
loc_003E32D5:
loc_003E32D9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 48)))) != ((unsigned int)((unsigned int)(a2)))) goto loc_003E3341;
loc_003E32E6:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 52))) - ((unsigned int)((unsigned int)(a3))));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 52) = (unsigned int)(a1);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 48)))) == ((unsigned int)((unsigned int)(a2)))) {
        result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 48)) + (unsigned int)(a3) * 1;
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 48) = (unsigned int)(result);
    }
    if ((unsigned int)(a1) == 0) goto loc_003E330D;
    a3 = 0;
    result = MiBitmapsCachedEntryLengthChanged(v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24, a3, (unsigned int)(a2));
    goto loc_003E32BE;
loc_003E330D:
    result = RtlRbRemoveNode(v_stack_p10 + 112, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24, a3, (unsigned int)(a2));
    result = RtlRbRemoveNode(v_stack_p10 + 128, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 24, a3, (unsigned int)(a2));
    v_rsi = (v_stack_p10) + (144);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) == v_rsi) goto loc_003E34A4;
loc_003E333A:
loc_003E3341:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 24))) + (0));
    if (((unsigned int)((unsigned int)(a2) + (unsigned int)(a3) * 1)) == ((unsigned int)(a1))) goto loc_003E32E6;
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(a2))));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(a3))));
    a4 = (unsigned int)(((unsigned int)(a2)) - (0));
    if ((*(unsigned __int64 *)(v_rsi + 144)) == (v_rsi + 144)) goto loc_003E34E9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 144) + 8)) != (v_rsi + 144)) goto loc_003E333A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 144)) + 8)) != (*(unsigned __int64 *)(v_rsi + 144))) goto loc_003E333A;
    *(unsigned __int64 *)(v_rsi + 144) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 144));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 144)) + 8) = v_rsi + 144;
    a3 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 52) = (unsigned int)(a1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 48) = (unsigned int)((unsigned int)(a2) + (unsigned int)(a3) * 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 24) = (unsigned int)(a4);
    result = MiBitmapsCachedEntryLengthChanged(v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24, a3, a4);
    if (((*(unsigned __int8 *)(v_rsi + 112 + 8)) & (1)) != 0) goto loc_003E34B7;
loc_003E33AB:
    a4 = (unsigned int)((*(unsigned __int8 *)(v_rsi + 112 + 8)) & (1));
    if (*(unsigned __int64 *)(v_rsi + 112) == 0) goto loc_003E3404;
loc_003E33C0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 52)))) > (*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 112) + 52))) goto loc_003E33F3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 52)))) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 112) + 52))) goto loc_003E33D1;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 48)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 112) + 48))))) goto loc_003E33F3;
loc_003E33D1:
    if ((unsigned int)(a4) == 0) goto loc_003E33E5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 112)) == 0) goto loc_003E34D9;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 112))) ^ (*(unsigned __int64 *)(v_rsi + 112));
loc_003E33E5:
    if (result == 0) goto loc_003E34D9;
loc_003E33EE:
    goto loc_003E33C0;
loc_003E33F3:
    if ((unsigned int)(a4) == 0) goto loc_003E3475;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_003E3472;
loc_003E3401:
loc_003E3404:
    result = RtlRbInsertNodeEx(v_rsi + 112, result, 1, *(unsigned __int64 *)(v_rsi + 144));
    if (((*(unsigned __int8 *)(v_rsi + 128 + 8)) & (1)) != 0) goto loc_003E34C8;
loc_003E3420:
    a3 = (unsigned int)((*(unsigned __int8 *)(v_rsi + 128 + 8)) & (1));
    if (*(unsigned __int64 *)(v_rsi + 128) == 0) goto loc_003E3448;
loc_003E3432:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 144) + 48)))) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 128) + 24))) goto loc_003E348A;
    if (a3 == 0) goto loc_003E3483;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 128) + 8) != 0) goto loc_003E3480;
loc_003E3446:
loc_003E3448:
    result = RtlRbInsertNodeEx(v_rsi + 128, *(unsigned __int64 *)(v_rsi + 128), 1, *(unsigned __int64 *)(v_rsi + 144) + 24);
    goto loc_003E32BE;
loc_003E3459:
    a2 = (*(unsigned __int64 *)(v_rsi + 128)) ^ (result);
    goto loc_003E32B4;
loc_003E3461:
    if (a2 == 0) goto loc_003E3279;
    a2 = (a2) ^ (v_rsi + 128);
    goto loc_003E3279;
loc_003E3472:
    result = (result) ^ (a2);
loc_003E3475:
    if (result != 0) goto loc_003E33EE;
    goto loc_003E3401;
loc_003E3480:
    result = (result) ^ (a2);
loc_003E3483:
    if (result == 0) goto loc_003E3446;
    goto loc_003E349F;
loc_003E348A:
    if (1 == 0) goto loc_003E349A;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003E3448;
    result = (*(unsigned __int64 *)(a2)) ^ (a2);
loc_003E349A:
    if (result == 0) goto loc_003E3448;
loc_003E349F:
    goto loc_003E3432;
loc_003E34A4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24) = v_rsi;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24 + 8) = result;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24;
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) - 24;
    goto loc_003E32BE;
loc_003E34B7:
    if (result == 0) goto loc_003E33AB;
    a2 = (result) ^ (v_rsi + 128);
    goto loc_003E33AB;
loc_003E34C8:
    if (a2 == 0) goto loc_003E3420;
    a2 = (a2) ^ (v_rsi + 128);
    goto loc_003E3420;
loc_003E34D9:
    goto loc_003E3404;
loc_003E34E1:
    goto loc_003E32A3;
loc_003E34E9:
    *(unsigned int *)(a2) = (unsigned int)(*(unsigned __int64 *)(v_rsi + 144) + 24);
}
```

## 5. (Beta) C Style

```c
int64_t MiInvalidatePageFileBitmapsCache(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (Arg4 != 0) goto loc_003E32D9;
    Arg1 = (Arg1) - (-128);
    if (((*(uint8_t *)(arg1 + 0x8)) & (1)) != 0) goto loc_003E3461;
loc_003E3279:
    Arg3 = (uint32_t)((*(uint8_t *)(arg1 + 0x8)) & (1));
    if (*(uint64_t *)(arg1) == 0) goto loc_003E32BE;
loc_003E328B:
    if (((uint32_t)((uint32_t)(Arg2) + (uint32_t)(Arg3) * 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18))))) goto loc_003E34E1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x18))) + (*(uint32_t *)(*(uint64_t *)(arg1) + 0x1C)));
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)(Arg1))) goto loc_003E32B9;
loc_003E32A3:
    if (Arg3 == 0) goto loc_003E32B1;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) != 0) goto loc_003E3459;
loc_003E32B1:
loc_003E32B4:
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) != 0) goto loc_003E328B;
loc_003E32B9:
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) != 0) goto loc_003E32D5;
loc_003E32BE:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(*(uint64_t *)(arg1) + 0x8);
loc_003E32D5:
loc_003E32D9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x30)))) != ((uint32_t)((uint32_t)(Arg2)))) goto loc_003E3341;
loc_003E32E6:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x34))) - ((uint32_t)((uint32_t)(Arg3))));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x34) = (uint32_t)(Arg1);
    result = *(uint64_t *)(*(uint64_t *)(arg1) + 0x8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x30)))) == ((uint32_t)((uint32_t)(Arg2)))) {
        result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x30)) + (uint32_t)(Arg3) * 1;
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x30) = (uint32_t)(result);
    }
    if ((uint32_t)(Arg1) == 0) goto loc_003E330D;
    Arg3 = 0;
    result = MiBitmapsCachedEntryLengthChanged(v_stack_p10, *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24, Arg3, (uint32_t)(Arg2));
    goto loc_003E32BE;
loc_003E330D:
    result = RtlRbRemoveNode(v_stack_p10 + 112, *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24, Arg3, (uint32_t)(Arg2));
    result = RtlRbRemoveNode(v_stack_p10 + 128, *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24 + 24, Arg3, (uint32_t)(Arg2));
    local_rsi = (v_stack_p10) + (144);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) == local_rsi) goto loc_003E34A4;
loc_003E333A:
loc_003E3341:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x18))) + (0));
    if (((uint32_t)((uint32_t)(Arg2) + (uint32_t)(Arg3) * 1)) == ((uint32_t)(Arg1))) goto loc_003E32E6;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(Arg2))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(Arg3))));
    Arg4 = (uint32_t)(((uint32_t)(Arg2)) - (0));
    if ((*(uint64_t *)(local_rsi + 0x90)) == (local_rsi + 144)) goto loc_003E34E9;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x8)) != (local_rsi + 144)) goto loc_003E333A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x90)) + 0x8)) != (*(uint64_t *)(local_rsi + 0x90))) goto loc_003E333A;
    *(uint64_t *)(local_rsi + 0x90) = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x90));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x90)) + 0x8) = local_rsi + 144;
    Arg3 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x34) = (uint32_t)(Arg1);
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x30) = (uint32_t)((uint32_t)(Arg2) + (uint32_t)(Arg3) * 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x18) = (uint32_t)(Arg4);
    result = MiBitmapsCachedEntryLengthChanged(local_rsi, *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24, Arg3, Arg4);
    if (((*(uint8_t *)(local_rsi + 0x70 + 0x8)) & (1)) != 0) goto loc_003E34B7;
loc_003E33AB:
    Arg4 = (uint32_t)((*(uint8_t *)(local_rsi + 0x70 + 0x8)) & (1));
    if (*(uint64_t *)(local_rsi + 0x70) == 0) goto loc_003E3404;
loc_003E33C0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x34)))) > (*(uint32_t *)(*(uint64_t *)(local_rsi + 0x70) + 0x34))) goto loc_003E33F3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x34)))) < (*(uint32_t *)(*(uint64_t *)(local_rsi + 0x70) + 0x34))) goto loc_003E33D1;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x30)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x70) + 0x30))))) goto loc_003E33F3;
loc_003E33D1:
    if ((uint32_t)(Arg4) == 0) goto loc_003E33E5;
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x70)) == 0) goto loc_003E34D9;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x70))) ^ (*(uint64_t *)(local_rsi + 0x70));
loc_003E33E5:
    if (result == 0) goto loc_003E34D9;
loc_003E33EE:
    goto loc_003E33C0;
loc_003E33F3:
    if ((uint32_t)(Arg4) == 0) goto loc_003E3475;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_003E3472;
loc_003E3401:
loc_003E3404:
    result = RtlRbInsertNodeEx(local_rsi + 112, result, 1, *(uint64_t *)(local_rsi + 0x90));
    if (((*(uint8_t *)(local_rsi + 0x80 + 0x8)) & (1)) != 0) goto loc_003E34C8;
loc_003E3420:
    Arg3 = (uint32_t)((*(uint8_t *)(local_rsi + 0x80 + 0x8)) & (1));
    if (*(uint64_t *)(local_rsi + 0x80) == 0) goto loc_003E3448;
loc_003E3432:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x90) + 0x30)))) < (*(uint32_t *)(*(uint64_t *)(local_rsi + 0x80) + 0x18))) goto loc_003E348A;
    if (Arg3 == 0) goto loc_003E3483;
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x80) + 0x8) != 0) goto loc_003E3480;
loc_003E3446:
loc_003E3448:
    result = RtlRbInsertNodeEx(local_rsi + 128, *(uint64_t *)(local_rsi + 0x80), 1, *(uint64_t *)(local_rsi + 0x90) + 24);
    goto loc_003E32BE;
loc_003E3459:
    Arg2 = (*(uint64_t *)(local_rsi + 0x80)) ^ (result);
    goto loc_003E32B4;
loc_003E3461:
    if (Arg2 == NULL) goto loc_003E3279;
    Arg2 = (Arg2) ^ (local_rsi + 128);
    goto loc_003E3279;
loc_003E3472:
    result = (result) ^ (Arg2);
loc_003E3475:
    if (result != 0) goto loc_003E33EE;
    goto loc_003E3401;
loc_003E3480:
    result = (result) ^ (Arg2);
loc_003E3483:
    if (result == 0) goto loc_003E3446;
    goto loc_003E349F;
loc_003E348A:
    if (1 == 0) goto loc_003E349A;
    if (*(uint64_t *)(arg2) == 0) goto loc_003E3448;
    result = (*(uint64_t *)(arg2)) ^ (Arg2);
loc_003E349A:
    if (result == 0) goto loc_003E3448;
loc_003E349F:
    goto loc_003E3432;
loc_003E34A4:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18) = local_rsi;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 0x18 + 0x8) = result;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24;
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) - 24;
    goto loc_003E32BE;
loc_003E34B7:
    if (result == 0) goto loc_003E33AB;
    Arg2 = (result) ^ (local_rsi + 128);
    goto loc_003E33AB;
loc_003E34C8:
    if (Arg2 == NULL) goto loc_003E3420;
    Arg2 = (Arg2) ^ (local_rsi + 128);
    goto loc_003E3420;
loc_003E34D9:
    goto loc_003E3404;
loc_003E34E1:
    goto loc_003E32A3;
loc_003E34E9:
    *(uint32_t *)(arg2) = (uint32_t)(*(uint64_t *)(local_rsi + 0x90) + 24);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x6C` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg2` | `+ 0x0 + r10*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E3240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
