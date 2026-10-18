# HalpLbrInitializeIntel

- RVA: `0x00B610EC`–`0x00B612E9` (길이 `509` bytes)
- VA: `0x0000000140B610EC`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C477C`
- 디코드: `161`개 명령, `509/509` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00B612D8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpLbrInitialize](HalpLbrInitialize_function_00B60F78.md) at `0x00B61000`

### Static image references
- `0x00B610F9` → RVA `0x00E0A740` (`.data`; read)
- `0x00B61127` → RVA `0x00F8F9A0` (`.data`; write)
- `0x00B6113D` → RVA `0x00F8F9A4` (`.data`; write)
- `0x00B6114A` → RVA `0x00F8F998` (`.data`; write)
- `0x00B6124F` → RVA `0x00F8F998` (`.data`; read)
- `0x00B6126F` → RVA `0x00E0A842` (`.data`; read)
- `0x00B612AA` → RVA `0x00E11810` (`.data`; write)
- `0x00B612B3` → RVA `0x00E0A843` (`.data`; write)
- `0x00B612BA` → RVA `0x00E0A841` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B612D8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B610EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B610F1  55                              push rbp
00B610F2  48 8B EC                        mov rbp, rsp
00B610F5  48 83 EC 20                     sub rsp, 0x20
00B610F9  48 8B 05 40 96 2A 00            mov rax, qword ptr [rip + 0x2a9640]
00B61100  48 33 C4                        xor rax, rsp
00B61103  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B61107  41 BB 07 00 00 00               mov r11d, 7
00B6110D  44 0F B6 CA                     movzx r9d, dl
00B61111  44 8A C1                        mov r8b, cl
00B61114  41 8B C3                        mov eax, r11d
00B61117  33 C9                           xor ecx, ecx
00B61119  0F A2                           cpuid
00B6111B  45 8D 53 FA                     lea r10d, [r11 - 6]
00B6111F  0F BA E2 13                     bt edx, 0x13
00B61123  73 30                           jae 0x140b61155
00B61125  33 C9                           xor ecx, ecx
00B61127  C7 05 6F E8 42 00 02 00 00 00   mov dword ptr [rip + 0x42e86f], 2
00B61131  41 8D 43 15                     lea eax, [r11 + 0x15]
00B61135  0F A2                           cpuid
00B61137  0F B6 C0                        movzx eax, al
00B6113A  0F BD C0                        bsr eax, eax
00B6113D  89 1D 61 E8 42 00               mov dword ptr [rip + 0x42e861], ebx
00B61143  8D 04 C5 08 00 00 00            lea eax, [rax*8 + 8]
00B6114A  89 05 48 E8 42 00               mov dword ptr [rip + 0x42e848], eax
00B61150  E9 FA 00 00 00                  jmp 0x140b6124f
00B61155  41 80 F8 06                     cmp r8b, 6
00B61159  0F 85 F0 00 00 00               jne 0x140b6124f
00B6115F  44 89 15 3A E8 42 00            mov dword ptr [rip + 0x42e83a], r10d
00B61166  41 8B C9                        mov ecx, r9d
00B61169  41 83 F9 55                     cmp r9d, 0x55
00B6116D  77 73                           ja 0x140b611e2
00B6116F  0F 84 D0 00 00 00               je 0x140b61245
00B61175  83 F9 3A                        cmp ecx, 0x3a
00B61178  77 39                           ja 0x140b611b3
00B6117A  74 28                           je 0x140b611a4
00B6117C  83 E9 1A                        sub ecx, 0x1a
00B6117F  74 23                           je 0x140b611a4
00B61181  83 E9 04                        sub ecx, 4
00B61184  74 1E                           je 0x140b611a4
00B61186  41 2B CA                        sub ecx, r10d
00B61189  74 19                           je 0x140b611a4
00B6118B  83 E9 06                        sub ecx, 6
00B6118E  74 14                           je 0x140b611a4
00B61190  83 E9 05                        sub ecx, 5
00B61193  74 0F                           je 0x140b611a4
00B61195  83 E9 02                        sub ecx, 2
00B61198  74 0A                           je 0x140b611a4
00B6119A  41 2B CA                        sub ecx, r10d
00B6119D  74 05                           je 0x140b611a4
00B6119F  41 2B CA                        sub ecx, r10d
00B611A2  75 37                           jne 0x140b611db
00B611A4  C7 05 EA E7 42 00 10 00 00 00   mov dword ptr [rip + 0x42e7ea], 0x10
00B611AE  E9 A5 00 00 00                  jmp 0x140b61258
00B611B3  83 E9 3C                        sub ecx, 0x3c
00B611B6  74 EC                           je 0x140b611a4
00B611B8  41 2B CA                        sub ecx, r10d
00B611BB  74 E7                           je 0x140b611a4
00B611BD  41 2B CA                        sub ecx, r10d
00B611C0  74 E2                           je 0x140b611a4
00B611C2  41 2B CA                        sub ecx, r10d
00B611C5  74 DD                           je 0x140b611a4
00B611C7  83 E9 06                        sub ecx, 6
00B611CA  74 D8                           je 0x140b611a4
00B611CC  41 2B CA                        sub ecx, r10d
00B611CF  74 D3                           je 0x140b611a4
00B611D1  41 2B CA                        sub ecx, r10d
00B611D4  74 CE                           je 0x140b611a4
00B611D6  41 2B CB                        sub ecx, r11d
00B611D9  74 6A                           je 0x140b61245
00B611DB  41 3B CA                        cmp ecx, r10d
00B611DE  74 C4                           je 0x140b611a4
00B611E0  EB 6D                           jmp 0x140b6124f
00B611E2  83 F9 7D                        cmp ecx, 0x7d
00B611E5  77 31                           ja 0x140b61218
00B611E7  74 5C                           je 0x140b61245
00B611E9  83 E9 56                        sub ecx, 0x56
00B611EC  74 B6                           je 0x140b611a4
00B611EE  83 E9 06                        sub ecx, 6
00B611F1  74 52                           je 0x140b61245
00B611F3  83 E9 02                        sub ecx, 2
00B611F6  74 4D                           je 0x140b61245
00B611F8  41 2B CA                        sub ecx, r10d
00B611FB  74 48                           je 0x140b61245
00B611FD  41 2B CB                        sub ecx, r11d
00B61200  74 43                           je 0x140b61245
00B61202  41 2B CA                        sub ecx, r10d
00B61205  74 3E                           je 0x140b61245
00B61207  83 E9 03                        sub ecx, 3
00B6120A  74 39                           je 0x140b61245
00B6120C  83 E9 02                        sub ecx, 2
00B6120F  74 34                           je 0x140b61245
00B61211  83 F9 0E                        cmp ecx, 0xe
00B61214  74 2F                           je 0x140b61245
00B61216  EB 37                           jmp 0x140b6124f
00B61218  83 E9 7E                        sub ecx, 0x7e
00B6121B  74 28                           je 0x140b61245
00B6121D  83 E9 0E                        sub ecx, 0xe
00B61220  74 23                           je 0x140b61245
00B61222  41 2B CA                        sub ecx, r10d
00B61225  74 1E                           je 0x140b61245
00B61227  41 2B CA                        sub ecx, r10d
00B6122A  74 19                           je 0x140b61245
00B6122C  83 E9 10                        sub ecx, 0x10
00B6122F  74 14                           je 0x140b61245
00B61231  41 2B CB                        sub ecx, r11d
00B61234  74 0F                           je 0x140b61245
00B61236  41 2B CA                        sub ecx, r10d
00B61239  74 0A                           je 0x140b61245
00B6123B  41 2B CA                        sub ecx, r10d
00B6123E  74 05                           je 0x140b61245
00B61240  41 3B CA                        cmp ecx, r10d
00B61243  75 0A                           jne 0x140b6124f
00B61245  C7 05 49 E7 42 00 20 00 00 00   mov dword ptr [rip + 0x42e749], 0x20
00B6124F  83 3D 42 E7 42 00 00            cmp dword ptr [rip + 0x42e742], 0
00B61256  74 77                           je 0x140b612cf
00B61258  33 C9                           xor ecx, ecx
00B6125A  B8 0A 00 00 00                  mov eax, 0xa
00B6125F  0F A2                           cpuid
00B61261  0F B6 C8                        movzx ecx, al
00B61264  41 3B CA                        cmp ecx, r10d
00B61267  72 66                           jb 0x140b612cf
00B61269  83 F9 03                        cmp ecx, 3
00B6126C  41 8B C2                        mov eax, r10d
00B6126F  0F 96 05 CC 95 2A 00            setbe byte ptr [rip + 0x2a95cc]
00B61276  33 C9                           xor ecx, ecx
00B61278  0F A2                           cpuid
00B6127A  0F BA E1 0F                     bt ecx, 0xf
00B6127E  73 41                           jae 0x140b612c1
00B61280  B9 45 03 00 00                  mov ecx, 0x345
00B61285  0F 32                           rdmsr
00B61287  48 C1 E2 20                     shl rdx, 0x20
00B6128B  48 0B C2                        or rax, rdx
00B6128E  83 E0 3F                        and eax, 0x3f
00B61291  83 E8 03                        sub eax, 3
00B61294  74 24                           je 0x140b612ba
00B61296  41 2B C2                        sub eax, r10d
00B61299  74 2B                           je 0x140b612c6
00B6129B  41 2B C2                        sub eax, r10d
00B6129E  74 0A                           je 0x140b612aa
00B612A0  41 2B C2                        sub eax, r10d
00B612A3  74 0E                           je 0x140b612b3
00B612A5  41 3B C2                        cmp eax, r10d
00B612A8  75 17                           jne 0x140b612c1
00B612AA  44 88 15 5F 05 2B 00            mov byte ptr [rip + 0x2b055f], r10b
00B612B1  EB 0E                           jmp 0x140b612c1
00B612B3  C6 05 89 95 2A 00 2F            mov byte ptr [rip + 0x2a9589], 0x2f
00B612BA  C6 05 80 95 2A 00 3E            mov byte ptr [rip + 0x2a9580], 0x3e
00B612C1  41 8A C2                        mov al, r10b
00B612C4  EB 0B                           jmp 0x140b612d1
00B612C6  C6 05 74 95 2A 00 3C            mov byte ptr [rip + 0x2a9574], 0x3c
00B612CD  EB F2                           jmp 0x140b612c1
00B612CF  32 C0                           xor al, al
00B612D1  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00B612D5  48 33 CC                        xor rcx, rsp
00B612D8  E8 63 B3 B4 FF                  call 0x1406ac640
00B612DD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B612E2  48 83 C4 20                     add rsp, 0x20
00B612E6  5D                              pop rbp
00B612E7  C3                              ret
00B612E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpLbrInitializeIntel(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = (*(unsigned __int64 *)(v_rip + 2790976)) ^ (v_rsp);
    v_stack_m10 = result;
    a1 = 0;
    if (condition_is_above_or_equal) goto loc_00B61155;
    a1 = 0;
    *(unsigned int *)(v_rip + 4384879) = 2;
    *(unsigned int *)(v_rip + 4384865) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4384840) = (unsigned int)((unsigned __int8)(7 + 21) * 8 + 8);
    goto loc_00B6124F;
loc_00B61155:
    if (((unsigned __int8)((unsigned __int8)(a1))) != 6) goto loc_00B6124F;
    *(unsigned int *)(v_rip + 4384826) = (unsigned int)(7 - 6);
    if (((unsigned int)((unsigned __int8)(a2))) > 85) goto loc_00B611E2;
    if (((unsigned int)((unsigned __int8)(a2))) == 85) goto loc_00B61245;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(a2))))) > 58) goto loc_00B611B3;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(a2))))) == 58) goto loc_00B611A4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(a2)))) - (26));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_not_equal) goto loc_00B611DB;
loc_00B611A4:
    *(unsigned int *)(v_rip + 4384746) = 16;
    goto loc_00B61258;
loc_00B611B3:
    a1 = (unsigned int)((a1) - (60));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00B61245;
loc_00B611DB:
    if (a1 == ((unsigned int)(7 - 6))) goto loc_00B611A4;
    goto loc_00B6124F;
loc_00B611E2:
    if (a1 > 125) goto loc_00B61218;
    if (a1 == 125) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (86));
    if (condition_is_equal) goto loc_00B611A4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B61245;
    if (a1 == 14) goto loc_00B61245;
    goto loc_00B6124F;
loc_00B61218:
    a1 = (unsigned int)((a1) - (126));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (14));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    a1 = (unsigned int)((a1) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    if (a1 == ((unsigned int)(7 - 6))) {
        *(unsigned int *)(v_rip + 4384585) = 32;
    }
    if ((*(unsigned int *)(v_rip + 4384578)) == 0) goto loc_00B612CF;
loc_00B61258:
    a1 = 0;
    if (10 < ((unsigned int)(7 - 6))) goto loc_00B612CF;
    a1 = 0;
    if (condition_is_above_or_equal) goto loc_00B612C1;
    a2 = (a2) << (32);
    result = ((unsigned int)((unsigned int)(7 - 6))) | (a2);
    result = (unsigned int)((result) & (63));
    result = (unsigned int)((result) - (3));
    if (condition_is_equal) goto loc_00B612BA;
    result = (unsigned int)((result) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B612C6;
    result = (unsigned int)((result) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B612AA;
    result = (unsigned int)((result) - ((unsigned int)(7 - 6)));
    if (condition_is_equal) goto loc_00B612B3;
    if (((unsigned int)(result)) != ((unsigned int)(7 - 6))) goto loc_00B612C1;
loc_00B612AA:
    *(unsigned __int8 *)(v_rip + 2819423) = (unsigned __int8)(7 - 6);
    goto loc_00B612C1;
loc_00B612B3:
    *(unsigned __int8 *)(v_rip + 2790793) = 47;
loc_00B612BA:
    *(unsigned __int8 *)(v_rip + 2790784) = 62;
loc_00B612C1:
    goto loc_00B612D1;
loc_00B612C6:
    *(unsigned __int8 *)(v_rip + 2790772) = 60;
    goto loc_00B612C1;
loc_00B612CF:
    result = 0;
loc_00B612D1:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned __int8)(a1), (unsigned __int8)(a2));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpLbrInitializeIntel(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = (*(uint64_t *)(v_rip + 0x2A9640)) ^ (local_rsp);
    v_stack_m10 = result;
    Arg1 = 0;
    if (condition_is_above_or_equal) goto loc_00B61155;
    Arg1 = 0;
    *(uint32_t *)(v_rip + 0x42E86F) = 2;
    *(uint32_t *)(v_rip + 0x42E861) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42E848) = (uint32_t)((uint8_t)(7 + 21) * 8 + 8);
    goto loc_00B6124F;
loc_00B61155:
    if (((uint8_t)((uint8_t)(Arg1))) != 6) goto loc_00B6124F;
    *(uint32_t *)(v_rip + 0x42E83A) = (uint32_t)(7 - 6);
    if (((uint32_t)((uint8_t)(Arg2))) > 85) goto loc_00B611E2;
    if (((uint32_t)((uint8_t)(Arg2))) == 85) goto loc_00B61245;
    if (((uint32_t)((uint32_t)((uint32_t)((uint8_t)(Arg2))))) > 58) goto loc_00B611B3;
    if (((uint32_t)((uint32_t)((uint32_t)((uint8_t)(Arg2))))) == 58) goto loc_00B611A4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(Arg2)))) - (26));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_not_equal) goto loc_00B611DB;
loc_00B611A4:
    *(uint32_t *)(v_rip + 0x42E7EA) = 16;
    goto loc_00B61258;
loc_00B611B3:
    Arg1 = (uint32_t)((Arg1) - (60));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00B61245;
loc_00B611DB:
    if (Arg1 == ((uint32_t)(7 - 6))) goto loc_00B611A4;
    goto loc_00B6124F;
loc_00B611E2:
    if (Arg1 > 125) goto loc_00B61218;
    if (Arg1 == 125) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (86));
    if (condition_is_equal) goto loc_00B611A4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B61245;
    if (Arg1 == 14) goto loc_00B61245;
    goto loc_00B6124F;
loc_00B61218:
    Arg1 = (uint32_t)((Arg1) - (126));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (14));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B61245;
    if (Arg1 == ((uint32_t)(7 - 6))) {
        *(uint32_t *)(v_rip + 0x42E749) = 32;
    }
    if ((*(uint32_t *)(v_rip + 0x42E742)) == 0) goto loc_00B612CF;
loc_00B61258:
    Arg1 = 0;
    if (10 < ((uint32_t)(7 - 6))) goto loc_00B612CF;
    Arg1 = 0;
    if (condition_is_above_or_equal) goto loc_00B612C1;
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)((uint32_t)(7 - 6))) | (Arg2);
    result = (uint32_t)((result) & (63));
    result = (uint32_t)((result) - (3));
    if (condition_is_equal) goto loc_00B612BA;
    result = (uint32_t)((result) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B612C6;
    result = (uint32_t)((result) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B612AA;
    result = (uint32_t)((result) - ((uint32_t)(7 - 6)));
    if (condition_is_equal) goto loc_00B612B3;
    if (((uint32_t)(result)) != ((uint32_t)(7 - 6))) goto loc_00B612C1;
loc_00B612AA:
    *(uint8_t *)(v_rip + 0x2B055F) = (uint8_t)(7 - 6);
    goto loc_00B612C1;
loc_00B612B3:
    *(uint8_t *)(v_rip + 0x2A9589) = 47;
loc_00B612BA:
    *(uint8_t *)(v_rip + 0x2A9580) = 62;
loc_00B612C1:
    goto loc_00B612D1;
loc_00B612C6:
    *(uint8_t *)(v_rip + 0x2A9574) = 60;
    goto loc_00B612C1;
loc_00B612CF:
    result = 0;
loc_00B612D1:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint8_t)(Arg1), (uint8_t)(Arg2));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B610EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
