# PnpValidatePropertyData

- RVA: `0x008F7658`–`0x008F78F7` (길이 `671` bytes)
- VA: `0x00000001408F7658`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087A98`
- 디코드: `183`개 명령, `671/671` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008F7692` → [GetBaseTypeSize](../../text/46/GetBaseTypeSize_function_00466DBC.md) (function, `0x00466DBC`)
- `0x008F76CE` → [IsFixedSizeType](../../text/47/IsFixedSizeType_function_0047E1E8.md) (function, `0x0047E1E8`)
- `0x008F7873` → [IsFixedSizeType](../../text/47/IsFixedSizeType_function_0047E1E8.md) (function, `0x0047E1E8`)
- `0x008F78B7` → [RtlValidRelativeSecurityDescriptor](../8B/RtlValidRelativeSecurityDescriptor_function_008BDC70.md) (function, `0x008BDC70`)
- `0x008F78C7` → [RtlLengthSecurityDescriptor](../8B/RtlLengthSecurityDescriptor_function_008BC870.md) (function, `0x008BC870`)

### Direct callers
- [ValidFilterExpression](../../text/49/ValidFilterExpression_function_00491EE4.md) at `0x00491F28`
- [PiDqQueryValidateQueryData](../8D/PiDqQueryValidateQueryData_function_008DC67C.md) at `0x008DC803`
- [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E1110.md) at `0x008E14F0`
- [PnpGetObjectPropertyWorker](../8E/PnpGetObjectPropertyWorker_function_008E1810.md) at `0x008E1B72`
- [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) at `0x008E2622`
- [PnpSetObjectPropertyWorker](PnpSetObjectPropertyWorker_function_008F7438.md) at `0x008F74AA`
- [PiSwValidatePropertyArray](PiSwValidatePropertyArray_function_008F75F4.md) at `0x008F762C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008F7692` → [GetBaseTypeSize](../../text/46/GetBaseTypeSize_function_00466DBC.md) (`PAGE` → `.text`)
  - `0x008F76CE` → [IsFixedSizeType](../../text/47/IsFixedSizeType_function_0047E1E8.md) (`PAGE` → `.text`)
  - `0x008F7873` → [IsFixedSizeType](../../text/47/IsFixedSizeType_function_0047E1E8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F7658  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008F765D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008F7662  57                              push rdi
008F7663  48 83 EC 20                     sub rsp, 0x20
008F7667  33 DB                           xor ebx, ebx
008F7669  8B F2                           mov esi, edx
008F766B  45 8B C8                        mov r9d, r8d
008F766E  48 8B F9                        mov rdi, rcx
008F7671  41 F7 C0 00 00 FF FF            test r8d, 0xffff0000
008F7678  0F 85 EA 00 00 00               jne 0x1408f7768
008F767E  41 81 E0 FF 0F 00 00            and r8d, 0xfff
008F7685  41 83 F8 19                     cmp r8d, 0x19
008F7689  0F 87 D9 00 00 00               ja 0x1408f7768
008F768F  41 8B C8                        mov ecx, r8d
008F7692  E8 25 F7 B6 FF                  call 0x140466dbc
008F7697  45 8B D1                        mov r10d, r9d
008F769A  44 8B D8                        mov r11d, eax
008F769D  41 81 E2 00 F0 00 00            and r10d, 0xf000
008F76A4  85 C0                           test eax, eax
008F76A6  74 38                           je 0x1408f76e0
008F76A8  41 81 FA 00 10 00 00            cmp r10d, 0x1000
008F76AF  0F 84 A6 01 00 00               je 0x1408f785b
008F76B5  41 81 FA 00 20 00 00            cmp r10d, 0x2000
008F76BC  0F 84 88 00 00 00               je 0x1408f774a
008F76C2  45 85 D2                        test r10d, r10d
008F76C5  0F 85 9D 00 00 00               jne 0x1408f7768
008F76CB  41 8B C9                        mov ecx, r9d
008F76CE  E8 15 6B B8 FF                  call 0x14047e1e8
008F76D3  84 C0                           test al, al
008F76D5  74 09                           je 0x1408f76e0
008F76D7  41 3B F3                        cmp esi, r11d
008F76DA  0F 85 88 00 00 00               jne 0x1408f7768
008F76E0  45 85 C0                        test r8d, r8d
008F76E3  0F 84 FF 01 00 00               je 0x1408f78e8
008F76E9  41 83 E8 01                     sub r8d, 1
008F76ED  0F 84 F5 01 00 00               je 0x1408f78e8
008F76F3  41 83 E8 0F                     sub r8d, 0xf
008F76F7  0F 84 38 01 00 00               je 0x1408f7835
008F76FD  41 83 E8 01                     sub r8d, 1
008F7701  74 7D                           je 0x1408f7780
008F7703  41 83 E8 01                     sub r8d, 1
008F7707  74 14                           je 0x1408f771d
008F7709  41 83 E8 01                     sub r8d, 1
008F770D  0F 84 93 01 00 00               je 0x1408f78a6
008F7713  41 83 E8 01                     sub r8d, 1
008F7717  0F 85 7A 01 00 00               jne 0x1408f7897
008F771D  48 85 FF                        test rdi, rdi
008F7720  74 46                           je 0x1408f7768
008F7722  83 FE 02                        cmp esi, 2
008F7725  72 41                           jb 0x1408f7768
008F7727  48 8B CE                        mov rcx, rsi
008F772A  41 0F BA E2 0D                  bt r10d, 0xd
008F772F  73 5C                           jae 0x1408f778d
008F7731  4C 8B C3                        mov r8, rbx
008F7734  49 8D 40 02                     lea rax, [r8 + 2]
008F7738  48 3B C1                        cmp rax, rcx
008F773B  77 2B                           ja 0x1408f7768
008F773D  66 39 1F                        cmp word ptr [rdi], bx
008F7740  75 7F                           jne 0x1408f77c1
008F7742  48 3B C1                        cmp rax, rcx
008F7745  E9 84 01 00 00                  jmp 0x1408f78ce
008F774A  41 83 F8 14                     cmp r8d, 0x14
008F774E  74 CD                           je 0x1408f771d
008F7750  41 83 F8 12                     cmp r8d, 0x12
008F7754  74 C7                           je 0x1408f771d
008F7756  EB 10                           jmp 0x1408f7768
008F7758  8B C2                           mov eax, edx
008F775A  8A 0C 38                        mov cl, byte ptr [rax + rdi]
008F775D  FE C1                           inc cl
008F775F  80 F9 01                        cmp cl, 1
008F7762  0F 86 79 01 00 00               jbe 0x1408f78e1
008F7768  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F776D  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008F7772  8B C3                           mov eax, ebx
008F7774  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008F7779  48 83 C4 20                     add rsp, 0x20
008F777D  5F                              pop rdi
008F777E  C3                              ret
008F777F  CC                              int3
008F7780  48 85 FF                        test rdi, rdi
008F7783  74 E3                           je 0x1408f7768
008F7785  8B D3                           mov edx, ebx
008F7787  3B D6                           cmp edx, esi
008F7789  73 E2                           jae 0x1408f776d
008F778B  EB CB                           jmp 0x1408f7758
008F778D  48 8B C1                        mov rax, rcx
008F7790  48 D1 E8                        shr rax, 1
008F7793  48 8B D0                        mov rdx, rax
008F7796  74 0F                           je 0x1408f77a7
008F7798  66 39 1F                        cmp word ptr [rdi], bx
008F779B  74 0F                           je 0x1408f77ac
008F779D  48 83 C7 02                     add rdi, 2
008F77A1  48 83 E8 01                     sub rax, 1
008F77A5  75 F1                           jne 0x1408f7798
008F77A7  48 85 C0                        test rax, rax
008F77AA  74 BC                           je 0x1408f7768
008F77AC  48 2B D0                        sub rdx, rax
008F77AF  48 8D 04 55 02 00 00 00         lea rax, [rdx*2 + 2]
008F77B7  48 3D FE FF 00 00               cmp rax, 0xfffe
008F77BD  77 A9                           ja 0x1408f7768
008F77BF  EB 81                           jmp 0x1408f7742
008F77C1  48 8B C1                        mov rax, rcx
008F77C4  49 2B C0                        sub rax, r8
008F77C7  48 D1 E8                        shr rax, 1
008F77CA  48 3D FF FF FF 7F               cmp rax, 0x7fffffff
008F77D0  77 96                           ja 0x1408f7768
008F77D2  48 8B D0                        mov rdx, rax
008F77D5  4C 8B CF                        mov r9, rdi
008F77D8  48 85 C0                        test rax, rax
008F77DB  74 10                           je 0x1408f77ed
008F77DD  66 41 39 19                     cmp word ptr [r9], bx
008F77E1  74 0A                           je 0x1408f77ed
008F77E3  49 83 C1 02                     add r9, 2
008F77E7  48 83 EA 01                     sub rdx, 1
008F77EB  75 F0                           jne 0x1408f77dd
008F77ED  48 85 D2                        test rdx, rdx
008F77F0  0F 84 E3 00 00 00               je 0x1408f78d9
008F77F6  48 2B C2                        sub rax, rdx
008F77F9  48 85 D2                        test rdx, rdx
008F77FC  0F 84 66 FF FF FF               je 0x1408f7768
008F7802  48 03 C0                        add rax, rax
008F7805  A8 01                           test al, 1
008F7807  0F 85 5B FF FF FF               jne 0x1408f7768
008F780D  48 83 C0 02                     add rax, 2
008F7811  48 3D FE FF 00 00               cmp rax, 0xfffe
008F7817  0F 87 4B FF FF FF               ja 0x1408f7768
008F781D  4C 03 C0                        add r8, rax
008F7820  4C 3B C1                        cmp r8, rcx
008F7823  0F 87 3F FF FF FF               ja 0x1408f7768
008F7829  48 D1 E8                        shr rax, 1
008F782C  48 8D 3C 47                     lea rdi, [rdi + rax*2]
008F7830  E9 FF FE FF FF                  jmp 0x1408f7734
008F7835  48 85 FF                        test rdi, rdi
008F7838  0F 84 2A FF FF FF               je 0x1408f7768
008F783E  8B CB                           mov ecx, ebx
008F7840  C1 EE 03                        shr esi, 3
008F7843  3B CE                           cmp ecx, esi
008F7845  0F 83 22 FF FF FF               jae 0x1408f776d
008F784B  8B C1                           mov eax, ecx
008F784D  48 39 1C C7                     cmp qword ptr [rdi + rax*8], rbx
008F7851  0F 8C 11 FF FF FF               jl 0x1408f7768
008F7857  FF C1                           inc ecx
008F7859  EB E8                           jmp 0x1408f7843
008F785B  41 8B C0                        mov eax, r8d
008F785E  45 85 C0                        test r8d, r8d
008F7861  0F 84 01 FF FF FF               je 0x1408f7768
008F7867  83 F8 01                        cmp eax, 1
008F786A  0F 84 F8 FE FF FF               je 0x1408f7768
008F7870  41 8B C9                        mov ecx, r9d
008F7873  E8 70 69 B8 FF                  call 0x14047e1e8
008F7878  84 C0                           test al, al
008F787A  0F 84 E8 FE FF FF               je 0x1408f7768
008F7880  41 3B F3                        cmp esi, r11d
008F7883  0F 82 DF FE FF FF               jb 0x1408f7768
008F7889  33 D2                           xor edx, edx
008F788B  8B C6                           mov eax, esi
008F788D  41 F7 F3                        div r11d
008F7890  85 D2                           test edx, edx
008F7892  E9 43 FE FF FF                  jmp 0x1408f76da
008F7897  41 83 F8 05                     cmp r8d, 5
008F789B  0F 84 7C FE FF FF               je 0x1408f771d
008F78A1  E9 C7 FE FF FF                  jmp 0x1408f776d
008F78A6  48 85 FF                        test rdi, rdi
008F78A9  0F 84 B9 FE FF FF               je 0x1408f7768
008F78AF  45 33 C0                        xor r8d, r8d
008F78B2  8B D6                           mov edx, esi
008F78B4  48 8B CF                        mov rcx, rdi
008F78B7  E8 B4 63 FC FF                  call 0x1408bdc70
008F78BC  84 C0                           test al, al
008F78BE  0F 84 A4 FE FF FF               je 0x1408f7768
008F78C4  48 8B CF                        mov rcx, rdi
008F78C7  E8 A4 4F FC FF                  call 0x1408bc870
008F78CC  3B C6                           cmp eax, esi
008F78CE  0F 84 99 FE FF FF               je 0x1408f776d
008F78D4  E9 8F FE FF FF                  jmp 0x1408f7768
008F78D9  48 8B C3                        mov rax, rbx
008F78DC  E9 18 FF FF FF                  jmp 0x1408f77f9
008F78E1  FF C2                           inc edx
008F78E3  E9 9F FE FF FF                  jmp 0x1408f7787
008F78E8  85 F6                           test esi, esi
008F78EA  B8 0D 00 00 C0                  mov eax, 0xc000000d
008F78EF  0F 45 D8                        cmovne ebx, eax
008F78F2  E9 76 FE FF FF                  jmp 0x1408f776d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpValidatePropertyData(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (((a3) & (0xFFFF0000ULL)) != 0) goto loc_008F7768;
    a3 = (unsigned int)((a3) & (0xFFFULL));
    if (a3 > 25) goto loc_008F7768;
    result = GetBaseTypeSize((unsigned int)(a3), a2, a3, (unsigned int)(a3));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0xF000ULL));
    if ((unsigned int)(result) == 0) goto loc_008F76E0;
    if (((unsigned int)(v_r10)) == 0x1000ULL) goto loc_008F785B;
    if (((unsigned int)(v_r10)) == 0x2000ULL) goto loc_008F774A;
    if ((unsigned int)(v_r10) != 0) goto loc_008F7768;
    result = IsFixedSizeType((unsigned int)((unsigned int)((unsigned int)(a3))), a2, a3, (unsigned int)(a3));
    if ((unsigned __int8)(result) == 0) goto loc_008F76E0;
loc_008F76DA:
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_008F7768;
loc_008F76E0:
    if (a3 == 0) goto loc_008F78E8;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_008F78E8;
    a3 = (unsigned int)((a3) - (15));
    if (condition_is_equal) goto loc_008F7835;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_008F7780;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_008F771D;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_008F78A6;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_not_equal) goto loc_008F7897;
loc_008F771D:
    if (a1 == 0) goto loc_008F7768;
    if (((unsigned int)((unsigned int)(a2))) < 2) goto loc_008F7768;
    if (((unsigned int)((unsigned int)(a2))) >= 2) goto loc_008F778D;
loc_008F7734:
    if ((0 + 2) > ((unsigned int)(a2))) goto loc_008F7768;
    if ((*(unsigned __int16 *)(a1)) != 0) goto loc_008F77C1;
loc_008F7742:
    goto loc_008F78CE;
loc_008F774A:
    if (0 == 20) goto loc_008F771D;
    if (0 == 18) goto loc_008F771D;
    goto loc_008F7768;
loc_008F7758:
    a1 = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(a2) + a1 * 1)) + 1);
    if (((unsigned __int8)(a1)) <= 1) goto loc_008F78E1;
loc_008F7768:
loc_008F776D:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_008F7780:
    if (a1 == 0) goto loc_008F7768;
loc_008F7787:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) >= ((unsigned int)(v_stack_p10))) goto loc_008F776D;
    goto loc_008F7758;
loc_008F778D:
    result = (a1) >> (1);
    if (condition_is_equal) goto loc_008F77A7;
loc_008F7798:
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(v_stack_p8))) goto loc_008F77AC;
    v_rdi = (a1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_008F7798;
loc_008F77A7:
    if (result == 0) goto loc_008F7768;
loc_008F77AC:
    a2 = (result) - (result);
    if ((a2 * 2 + 2) > 0xFFFEULL) goto loc_008F7768;
    goto loc_008F7742;
loc_008F77C1:
    result = (a1) - (0);
    result = (result) >> (1);
    if (result > 0x7FFFFFFFULL) goto loc_008F7768;
    if (result == 0) goto loc_008F77ED;
loc_008F77DD:
    if ((*(unsigned __int16 *)(v_rdi)) == ((unsigned __int16)(v_stack_p8))) goto loc_008F77ED;
    a4 = (v_rdi) + (2);
    a2 = (result) - (1);
    if (condition_is_not_equal) goto loc_008F77DD;
loc_008F77ED:
    if (a2 == 0) goto loc_008F78D9;
    result = (result) - (a2);
loc_008F77F9:
    if (a2 == 0) goto loc_008F7768;
    result = (result) + (result);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_008F7768;
    result = (result) + (2);
    if (result > 0xFFFEULL) goto loc_008F7768;
    a3 = (0) + (result);
    if (a3 > a1) goto loc_008F7768;
    result = (result) >> (1);
    goto loc_008F7734;
loc_008F7835:
    if (v_rdi + result * 2 == 0) goto loc_008F7768;
    v_rsi = (unsigned int)((v_stack_p10) >> (3));
loc_008F7843:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) >= ((unsigned int)(v_rsi))) goto loc_008F776D;
    if ((*(unsigned __int64 *)(v_rdi + result * 2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) * 8)) < v_stack_p8) goto loc_008F7768;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) + 1);
    goto loc_008F7843;
loc_008F785B:
    if (a3 == 0) goto loc_008F7768;
    if (((unsigned int)((unsigned int)(a3))) == 1) goto loc_008F7768;
    result = IsFixedSizeType((unsigned int)((unsigned int)(a4)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008F7768;
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_008F7768;
    a2 = 0;
    goto loc_008F76DA;
loc_008F7897:
    if (a3 == 5) goto loc_008F771D;
    goto loc_008F776D;
loc_008F78A6:
    if (v_rdi + result * 2 == 0) goto loc_008F7768;
    a3 = 0;
    result = RtlValidRelativeSecurityDescriptor(v_rdi + result * 2, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008F7768;
    result = RtlLengthSecurityDescriptor(v_rdi + result * 2, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
loc_008F78CE:
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi))) goto loc_008F776D;
    goto loc_008F7768;
loc_008F78D9:
    goto loc_008F77F9;
loc_008F78E1:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + 1);
    goto loc_008F7787;
loc_008F78E8:
    v_rbx = v_stack_p8;
    if ((unsigned int)(v_rsi) != 0) { v_rbx = (unsigned int)((unsigned int)(0xC000000DULL)); }
    goto loc_008F776D;
}
```

## 5. (Beta) C Style

```c
int64_t PnpValidatePropertyData(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (((Arg3) & (0xFFFF0000ULL)) != 0) goto loc_008F7768;
    Arg3 = (uint32_t)((Arg3) & (0xFFFULL));
    if (Arg3 > 25) goto loc_008F7768;
    result = GetBaseTypeSize((uint32_t)(Arg3), Arg2, Arg3, (uint32_t)(Arg3));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0xF000ULL));
    if ((uint32_t)(result) == 0) goto loc_008F76E0;
    if (((uint32_t)(local_r10)) == 0x1000ULL) goto loc_008F785B;
    if (((uint32_t)(local_r10)) == 0x2000ULL) goto loc_008F774A;
    if ((uint32_t)(local_r10) != 0) goto loc_008F7768;
    result = IsFixedSizeType((uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2, Arg3, (uint32_t)(Arg3));
    if ((uint8_t)(result) == 0) goto loc_008F76E0;
loc_008F76DA:
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_008F7768;
loc_008F76E0:
    if (Arg3 == 0) goto loc_008F78E8;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_008F78E8;
    Arg3 = (uint32_t)((Arg3) - (15));
    if (condition_is_equal) goto loc_008F7835;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_008F7780;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_008F771D;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_008F78A6;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_not_equal) goto loc_008F7897;
loc_008F771D:
    if (Arg1 == 0) goto loc_008F7768;
    if (((uint32_t)((uint32_t)(Arg2))) < 2) goto loc_008F7768;
    if (((uint32_t)((uint32_t)(Arg2))) >= 2) goto loc_008F778D;
loc_008F7734:
    if ((0 + 2) > ((uint32_t)(Arg2))) goto loc_008F7768;
    if ((*(uint16_t *)(Arg1)) != 0) goto loc_008F77C1;
loc_008F7742:
    goto loc_008F78CE;
loc_008F774A:
    if (0 == 20) goto loc_008F771D;
    if (0 == 18) goto loc_008F771D;
    goto loc_008F7768;
loc_008F7758:
    Arg1 = (uint8_t)((*(uint8_t *)((uint32_t)(Arg2) + Arg1 * 1)) + 1);
    if (((uint8_t)(Arg1)) <= 1) goto loc_008F78E1;
loc_008F7768:
loc_008F776D:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_008F7780:
    if (Arg1 == 0) goto loc_008F7768;
loc_008F7787:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) >= ((uint32_t)(v_stack_p10))) goto loc_008F776D;
    goto loc_008F7758;
loc_008F778D:
    result = (Arg1) >> (1);
    if (condition_is_equal) goto loc_008F77A7;
loc_008F7798:
    if ((*(uint16_t *)(Arg1)) == ((uint16_t)(v_stack_p8))) goto loc_008F77AC;
    local_rdi = (Arg1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_008F7798;
loc_008F77A7:
    if (result == 0) goto loc_008F7768;
loc_008F77AC:
    Arg2 = (result) - (result);
    if ((Arg2 * 2 + 2) > 0xFFFEULL) goto loc_008F7768;
    goto loc_008F7742;
loc_008F77C1:
    result = (Arg1) - (0);
    result = (result) >> (1);
    if (result > 0x7FFFFFFFULL) goto loc_008F7768;
    if (result == 0) goto loc_008F77ED;
loc_008F77DD:
    if ((*(uint16_t *)(local_rdi)) == ((uint16_t)(v_stack_p8))) goto loc_008F77ED;
    a4 = (local_rdi) + (2);
    Arg2 = (result) - (1);
    if (condition_is_not_equal) goto loc_008F77DD;
loc_008F77ED:
    if (Arg2 == 0) goto loc_008F78D9;
    result = (result) - (Arg2);
loc_008F77F9:
    if (Arg2 == 0) goto loc_008F7768;
    result = (result) + (result);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_008F7768;
    result = (result) + (2);
    if (result > 0xFFFEULL) goto loc_008F7768;
    Arg3 = (0) + (result);
    if (Arg3 > Arg1) goto loc_008F7768;
    result = (result) >> (1);
    goto loc_008F7734;
loc_008F7835:
    if (local_rdi + result * 2 == 0) goto loc_008F7768;
    local_rsi = (uint32_t)((v_stack_p10) >> (3));
loc_008F7843:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) >= ((uint32_t)(local_rsi))) goto loc_008F776D;
    if ((*(uint64_t *)(local_rdi + result * 2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) * 8)) < v_stack_p8) goto loc_008F7768;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) + 1);
    goto loc_008F7843;
loc_008F785B:
    if (Arg3 == 0) goto loc_008F7768;
    if (((uint32_t)((uint32_t)(Arg3))) == 1) goto loc_008F7768;
    result = IsFixedSizeType((uint32_t)((uint32_t)(a4)), Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_008F7768;
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_008F7768;
    Arg2 = 0;
    goto loc_008F76DA;
loc_008F7897:
    if (Arg3 == 5) goto loc_008F771D;
    goto loc_008F776D;
loc_008F78A6:
    if (local_rdi + result * 2 == 0) goto loc_008F7768;
    Arg3 = 0;
    result = RtlValidRelativeSecurityDescriptor(local_rdi + result * 2, (uint32_t)((uint32_t)(local_rsi)), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_008F7768;
    result = RtlLengthSecurityDescriptor(local_rdi + result * 2, (uint32_t)((uint32_t)(local_rsi)), Arg3, a4);
loc_008F78CE:
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi))) goto loc_008F776D;
    goto loc_008F7768;
loc_008F78D9:
    goto loc_008F77F9;
loc_008F78E1:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + 1);
    goto loc_008F7787;
loc_008F78E8:
    local_rbx = v_stack_p8;
    if ((uint32_t)(local_rsi) != 0) { local_rbx = (uint32_t)((uint32_t)(0xC000000DULL)); }
    goto loc_008F776D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F7658&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
