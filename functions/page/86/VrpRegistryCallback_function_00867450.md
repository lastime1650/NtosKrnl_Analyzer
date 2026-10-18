# VrpRegistryCallback

- RVA: `0x00867450`–`0x008676D3` (길이 `643` bytes)
- VA: `0x0000000140867450`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006BC50`
- 디코드: `163`개 명령, `643/643` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00867496` → [VrpShouldOperateOnCall](../93/VrpShouldOperateOnCall_function_00934E90.md) (function, `0x00934E90`)
- `0x008674A8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008674C4` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x008674EA` → [VrpPostQueryKey](../93/VrpPostQueryKey_function_009338F0.md) (function, `0x009338F0`)
- `0x00867519` → [VrpPreOpenOrCreate](../93/VrpPreOpenOrCreate_function_00932B84.md) (function, `0x00932B84`)
- `0x00867527` → [VrpPostOpenOrCreate](../93/VrpPostOpenOrCreate_function_00936510.md) (function, `0x00936510`)
- `0x00867577` → [VrpDecommissionKeyContext](../9F/VrpDecommissionKeyContext_function_009FEF0C.md) (function, `0x009FEF0C`)
- `0x00867599` → [VrpFreeKeyContext](../9F/VrpFreeKeyContext_function_009FEED4.md) (function, `0x009FEED4`)
- `0x008675DD` → [VrpPostEnumerateKey](../93/VrpPostEnumerateKey_function_00933EA8.md) (function, `0x00933EA8`)
- `0x008675FC` → [VrpPreQueryKeyName](../A1/VrpPreQueryKeyName_function_00A16DB8.md) (function, `0x00A16DB8`)
- `0x0086763B` → [VrpPreRenameKey](../83/VrpPreRenameKey_function_0083B9B8.md) (function, `0x0083B9B8`)
- `0x00867699` → [VrpPreLoadKey](../A8/VrpPreLoadKey_function_00A8A43C.md) (function, `0x00A8A43C`)
- `0x008676B8` → [VrpPostUnloadKey](../AD/VrpPostUnloadKey_function_00AD60DC.md) (function, `0x00AD60DC`)

### Direct callers
- [CmpFireCleanupNotifications](CmpFireCleanupNotifications_function_008649B0.md) at `0x00864A21`
- [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) at `0x00866381`
- [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) at `0x00866595`

### Static image references
- `0x0086745F` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008674A8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008674C4` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0086767A` → [sub_00B17664](../B1/Unknown_function_00B17664.md) (`tail-transfer`)
  - `0x008676A6` → [sub_00B17664 + 0xF](../B1/Unknown_function_00B17664.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00867450  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00867455  55                              push rbp
00867456  56                              push rsi
00867457  57                              push rdi
00867458  48 8B EC                        mov rbp, rsp
0086745B  48 83 EC 50                     sub rsp, 0x50
0086745F  48 8B 05 DA 32 5A 00            mov rax, qword ptr [rip + 0x5a32da]
00867466  48 33 C4                        xor rax, rsp
00867469  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0086746D  33 FF                           xor edi, edi
0086746F  0F 57 C0                        xorps xmm0, xmm0
00867472  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
00867476  49 8B F0                        mov rsi, r8
00867479  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
0086747D  48 8B DA                        mov rbx, rdx
00867480  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00867484  83 FA 33                        cmp edx, 0x33
00867487  77 16                           ja 0x14086749f
00867489  4C 8D 4D D0                     lea r9, [rbp - 0x30]
0086748D  48 8B D6                        mov rdx, rsi
00867490  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00867494  8B CB                           mov ecx, ebx
00867496  E8 F5 D9 0C 00                  call 0x140934e90
0086749B  85 C0                           test eax, eax
0086749D  75 1C                           jne 0x1408674bb
0086749F  8B C7                           mov eax, edi
008674A1  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
008674A5  48 33 CC                        xor rcx, rsp
008674A8  E8 93 51 E4 FF                  call 0x1406ac640
008674AD  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
008674B2  48 83 C4 50                     add rsp, 0x50
008674B6  5F                              pop rdi
008674B7  5E                              pop rsi
008674B8  5D                              pop rbp
008674B9  C3                              ret
008674BA  CC                              int3
008674BB  48 8D 55 E0                     lea rdx, [rbp - 0x20]
008674BF  B9 01 00 00 00                  mov ecx, 1
008674C4  E8 57 72 BB FF                  call 0x14041e720
008674C9  83 FB 1B                        cmp ebx, 0x1b
008674CC  7F 25                           jg 0x1408674f3
008674CE  74 50                           je 0x140867520
008674D0  83 FB 0F                        cmp ebx, 0xf
008674D3  7E 59                           jle 0x14086752e
008674D5  83 FB 15                        cmp ebx, 0x15
008674D8  0F 8E C5 00 00 00               jle 0x1408675a3
008674DE  83 EB 16                        sub ebx, 0x16
008674E1  0F 85 5E 01 00 00               jne 0x140867645
008674E7  48 8B CE                        mov rcx, rsi
008674EA  E8 01 C4 0C 00                  call 0x1409338f0
008674EF  8B F8                           mov edi, eax
008674F1  EB AC                           jmp 0x14086749f
008674F3  83 FB 27                        cmp ebx, 0x27
008674F6  0F 8F 85 00 00 00               jg 0x140867581
008674FC  74 A1                           je 0x14086749f
008674FE  83 FB 21                        cmp ebx, 0x21
00867501  0F 8F 9C 01 00 00               jg 0x1408676a3
00867507  74 96                           je 0x14086749f
00867509  83 EB 1C                        sub ebx, 0x1c
0086750C  0F 85 5C 01 00 00               jne 0x14086766e
00867512  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00867516  48 8B CE                        mov rcx, rsi
00867519  E8 66 B6 0C 00                  call 0x140932b84
0086751E  EB CF                           jmp 0x1408674ef
00867520  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00867524  48 8B CE                        mov rcx, rsi
00867527  E8 E4 EF 0C 00                  call 0x140936510
0086752C  EB C1                           jmp 0x1408674ef
0086752E  0F 84 6B FF FF FF               je 0x14086749f
00867534  83 FB 05                        cmp ebx, 5
00867537  0F 8E C9 00 00 00               jle 0x140867606
0086753D  83 EB 06                        sub ebx, 6
00867540  0F 84 59 FF FF FF               je 0x14086749f
00867546  83 EB 01                        sub ebx, 1
00867549  0F 84 50 FF FF FF               je 0x14086749f
0086754F  83 EB 01                        sub ebx, 1
00867552  0F 84 47 FF FF FF               je 0x14086749f
00867558  83 EB 01                        sub ebx, 1
0086755B  0F 84 3E FF FF FF               je 0x14086749f
00867561  83 FB 05                        cmp ebx, 5
00867564  0F 85 35 FF FF FF               jne 0x14086749f
0086756A  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
0086756E  48 85 C9                        test rcx, rcx
00867571  0F 84 28 FF FF FF               je 0x14086749f
00867577  E8 90 79 19 00                  call 0x1409fef0c
0086757C  E9 1E FF FF FF                  jmp 0x14086749f
00867581  83 FB 2D                        cmp ebx, 0x2d
00867584  7F 61                           jg 0x1408675e7
00867586  0F 84 13 FF FF FF               je 0x14086749f
0086758C  83 EB 28                        sub ebx, 0x28
0086758F  0F 85 2D 01 00 00               jne 0x1408676c2
00867595  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00867599  E8 36 79 19 00                  call 0x1409feed4
0086759E  E9 FC FE FF FF                  jmp 0x14086749f
008675A3  0F 84 F6 FE FF FF               je 0x14086749f
008675A9  83 EB 10                        sub ebx, 0x10
008675AC  0F 84 ED FE FF FF               je 0x14086749f
008675B2  83 EB 01                        sub ebx, 1
008675B5  0F 84 E4 FE FF FF               je 0x14086749f
008675BB  83 EB 01                        sub ebx, 1
008675BE  0F 84 DB FE FF FF               je 0x14086749f
008675C4  83 EB 01                        sub ebx, 1
008675C7  0F 84 D2 FE FF FF               je 0x14086749f
008675CD  83 FB 01                        cmp ebx, 1
008675D0  0F 85 C9 FE FF FF               jne 0x14086749f
008675D6  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008675DA  48 8B CE                        mov rcx, rsi
008675DD  E8 C6 C8 0C 00                  call 0x140933ea8
008675E2  E9 08 FF FF FF                  jmp 0x1408674ef
008675E7  83 EB 2E                        sub ebx, 0x2e
008675EA  0F 84 AF FE FF FF               je 0x14086749f
008675F0  83 EB 01                        sub ebx, 1
008675F3  0F 85 D2 00 00 00               jne 0x1408676cb
008675F9  48 8B CE                        mov rcx, rsi
008675FC  E8 B7 F7 1A 00                  call 0x140a16db8
00867601  E9 E9 FE FF FF                  jmp 0x1408674ef
00867606  0F 84 93 FE FF FF               je 0x14086749f
0086760C  85 DB                           test ebx, ebx
0086760E  0F 84 8B FE FF FF               je 0x14086749f
00867614  83 EB 01                        sub ebx, 1
00867617  0F 84 82 FE FF FF               je 0x14086749f
0086761D  83 EB 01                        sub ebx, 1
00867620  0F 84 79 FE FF FF               je 0x14086749f
00867626  83 EB 01                        sub ebx, 1
00867629  0F 84 70 FE FF FF               je 0x14086749f
0086762F  83 FB 01                        cmp ebx, 1
00867632  0F 85 67 FE FF FF               jne 0x14086749f
00867638  48 8B CE                        mov rcx, rsi
0086763B  E8 78 43 FD FF                  call 0x14083b9b8
00867640  E9 AA FE FF FF                  jmp 0x1408674ef
00867645  83 EB 01                        sub ebx, 1
00867648  0F 84 51 FE FF FF               je 0x14086749f
0086764E  83 EB 01                        sub ebx, 1
00867651  0F 84 48 FE FF FF               je 0x14086749f
00867657  83 EB 01                        sub ebx, 1
0086765A  0F 84 3F FE FF FF               je 0x14086749f
00867660  83 FB 01                        cmp ebx, 1
00867663  0F 84 A9 FE FF FF               je 0x140867512
00867669  E9 31 FE FF FF                  jmp 0x14086749f
0086766E  83 EB 01                        sub ebx, 1
00867671  0F 84 A9 FE FF FF               je 0x140867520
00867677  83 EB 01                        sub ebx, 1
0086767A  0F 84 E4 FF 2A 00               je 0x140b17664
00867680  83 EB 01                        sub ebx, 1
00867683  0F 84 16 FE FF FF               je 0x14086749f
00867689  83 FB 01                        cmp ebx, 1
0086768C  0F 85 0D FE FF FF               jne 0x14086749f
00867692  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00867696  48 8B CE                        mov rcx, rsi
00867699  E8 9E 2D 22 00                  call 0x140a8a43c
0086769E  E9 4C FE FF FF                  jmp 0x1408674ef
008676A3  83 EB 22                        sub ebx, 0x22
008676A6  0F 84 C7 FF 2A 00               je 0x140b17673
008676AC  83 EB 01                        sub ebx, 1
008676AF  75 1A                           jne 0x1408676cb
008676B1  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008676B5  48 8B CE                        mov rcx, rsi
008676B8  E8 1F EA 26 00                  call 0x140ad60dc
008676BD  E9 2D FE FF FF                  jmp 0x1408674ef
008676C2  83 EB 01                        sub ebx, 1
008676C5  0F 84 D4 FD FF FF               je 0x14086749f
008676CB  83 EB 01                        sub ebx, 1
008676CE  E9 CC FD FF FF                  jmp 0x14086749f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpRegistryCallback(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 5911258)) ^ (v_rsp);
    v_stack_m28 = result;
    v_rdi = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m38 = v_xmm0;
    if (((unsigned int)(a2)) > 51) goto loc_0086749F;
    result = VrpShouldOperateOnCall((unsigned int)((unsigned int)(a2)), a3, v_stack_m40, v_stack_m48);
    if ((unsigned int)(result) != 0) goto loc_008674BB;
loc_0086749F:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a3, v_stack_m40, v_stack_m48);
    v_rsp = (v_rsp) + (80);
    return result;
loc_008674BB:
    result = EtwActivityIdControl(1, v_stack_m38, v_stack_m40, v_stack_m48);
    if (((unsigned int)(v_stack_p8)) > 27) goto loc_008674F3;
    if (((unsigned int)(v_stack_p8)) == 27) goto loc_00867520;
    if (((unsigned int)(v_stack_p8)) <= 15) goto loc_0086752E;
    if (((unsigned int)(v_stack_p8)) <= 21) goto loc_008675A3;
    v_rbx = (unsigned int)((v_stack_p8) - (22));
    if (condition_is_not_equal) goto loc_00867645;
    result = VrpPostQueryKey(a3, v_stack_m38, v_stack_m40, v_stack_m48);
loc_008674EF:
    goto loc_0086749F;
loc_008674F3:
    if (((unsigned int)(v_rbx)) > 39) goto loc_00867581;
    if (((unsigned int)(v_rbx)) == 39) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) > 33) goto loc_008676A3;
    if (((unsigned int)(v_rbx)) == 33) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (28));
    if (condition_is_not_equal) goto loc_0086766E;
loc_00867512:
    result = VrpPreOpenOrCreate(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867520:
    result = VrpPostOpenOrCreate(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_0086752E:
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) <= 5) goto loc_00867606;
    v_rbx = (unsigned int)((v_rbx) - (6));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) != 5) goto loc_0086749F;
    if (*(unsigned __int64 *)(a3 + 16) == 0) goto loc_0086749F;
    result = VrpDecommissionKeyContext(*(unsigned __int64 *)(a3 + 16), v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_0086749F;
loc_00867581:
    if (((unsigned int)(v_rbx)) > 45) goto loc_008675E7;
    if (((unsigned int)(v_rbx)) == 45) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (40));
    if (condition_is_not_equal) goto loc_008676C2;
    result = VrpFreeKeyContext(*(unsigned __int64 *)(a3 + 8), v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_0086749F;
loc_008675A3:
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (16));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) != 1) goto loc_0086749F;
    result = VrpPostEnumerateKey(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008675E7:
    v_rbx = (unsigned int)((v_rbx) - (46));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008676CB;
    result = VrpPreQueryKeyName(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867606:
    if (condition_is_equal) goto loc_0086749F;
    if ((unsigned int)(v_rbx) == 0) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) != 1) goto loc_0086749F;
    result = VrpPreRenameKey(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867645:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) == 1) goto loc_00867512;
    goto loc_0086749F;
loc_0086766E:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00867520;
    v_rbx = (unsigned int)((v_rbx) - (1));
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((unsigned int)(v_rbx)) != 1) goto loc_0086749F;
    result = VrpPreLoadKey(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008676A3:
    v_rbx = (unsigned int)((v_rbx) - (34));
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008676CB;
    result = VrpPostUnloadKey(a3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008676C2:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
loc_008676CB:
    v_rbx = (unsigned int)((v_rbx) - (1));
    goto loc_0086749F;
}
```

## 5. (Beta) C Style

```c
int64_t VrpRegistryCallback(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x5A32DA)) ^ (local_rsp);
    v_stack_m28 = result;
    local_rdi = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m38 = v_xmm0;
    if (((uint32_t)(Arg2)) > 51) goto loc_0086749F;
    result = VrpShouldOperateOnCall((uint32_t)((uint32_t)(Arg2)), Arg3, v_stack_m40, v_stack_m48);
    if ((uint32_t)(result) != 0) goto loc_008674BB;
loc_0086749F:
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg3, v_stack_m40, v_stack_m48);
    local_rsp = (local_rsp) + (80);
    return result;
loc_008674BB:
    result = EtwActivityIdControl(1, v_stack_m38, v_stack_m40, v_stack_m48);
    if (((uint32_t)(v_stack_p8)) > 27) goto loc_008674F3;
    if (((uint32_t)(v_stack_p8)) == 27) goto loc_00867520;
    if (((uint32_t)(v_stack_p8)) <= 15) goto loc_0086752E;
    if (((uint32_t)(v_stack_p8)) <= 21) goto loc_008675A3;
    local_rbx = (uint32_t)((v_stack_p8) - (22));
    if (condition_is_not_equal) goto loc_00867645;
    result = VrpPostQueryKey(Arg3, v_stack_m38, v_stack_m40, v_stack_m48);
loc_008674EF:
    goto loc_0086749F;
loc_008674F3:
    if (((uint32_t)(local_rbx)) > 39) goto loc_00867581;
    if (((uint32_t)(local_rbx)) == 39) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) > 33) goto loc_008676A3;
    if (((uint32_t)(local_rbx)) == 33) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (28));
    if (condition_is_not_equal) goto loc_0086766E;
loc_00867512:
    result = VrpPreOpenOrCreate(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867520:
    result = VrpPostOpenOrCreate(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_0086752E:
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) <= 5) goto loc_00867606;
    local_rbx = (uint32_t)((local_rbx) - (6));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) != 5) goto loc_0086749F;
    if (*(uint64_t *)(arg3 + 0x10) == 0) goto loc_0086749F;
    result = VrpDecommissionKeyContext(*(uint64_t *)(arg3 + 0x10), v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_0086749F;
loc_00867581:
    if (((uint32_t)(local_rbx)) > 45) goto loc_008675E7;
    if (((uint32_t)(local_rbx)) == 45) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (40));
    if (condition_is_not_equal) goto loc_008676C2;
    result = VrpFreeKeyContext(*(uint64_t *)(arg3 + 0x8), v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_0086749F;
loc_008675A3:
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (16));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) != 1) goto loc_0086749F;
    result = VrpPostEnumerateKey(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008675E7:
    local_rbx = (uint32_t)((local_rbx) - (46));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008676CB;
    result = VrpPreQueryKeyName(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867606:
    if (condition_is_equal) goto loc_0086749F;
    if ((uint32_t)(local_rbx) == 0) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) != 1) goto loc_0086749F;
    result = VrpPreRenameKey(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_00867645:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) == 1) goto loc_00867512;
    goto loc_0086749F;
loc_0086766E:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00867520;
    local_rbx = (uint32_t)((local_rbx) - (1));
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
    if (((uint32_t)(local_rbx)) != 1) goto loc_0086749F;
    result = VrpPreLoadKey(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008676A3:
    local_rbx = (uint32_t)((local_rbx) - (34));
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008676CB;
    result = VrpPostUnloadKey(Arg3, v_stack_m48, v_stack_m40, v_stack_m48);
    goto loc_008674EF;
loc_008676C2:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_0086749F;
loc_008676CB:
    local_rbx = (uint32_t)((local_rbx) - (1));
    goto loc_0086749F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00867450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
