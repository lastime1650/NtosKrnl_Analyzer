# VmpFindNextPinnedPageStateHelper

- RVA: `0x0064C7E4`–`0x0064C9EA` (길이 `518` bytes)
- VA: `0x000000014064C7E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5A38`
- 디코드: `168`개 명령, `518/518` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VmpSplitMemoryRange](../42/VmpSplitMemoryRange_function_00429754.md) at `0x00429AD0`
- [VmpInvalidateSlatBatched](../48/VmpInvalidateSlatBatched_function_00489300.md) at `0x0048939B`
- [VmpInvalidateSlatBatched](../48/VmpInvalidateSlatBatched_function_00489300.md) at `0x004893BC`
- [VmpCheckPinAndReference](VmpCheckPinAndReference_function_0064C44C.md) at `0x0064C4A7`
- [VmpCheckPinAndReference](VmpCheckPinAndReference_function_0064C44C.md) at `0x0064C4BD`
- [VmpCheckPinAndReference](VmpCheckPinAndReference_function_0064C44C.md) at `0x0064C4D5`
- [VmpCheckUnpinAndDereference](VmpCheckUnpinAndDereference_function_0064C540.md) at `0x0064C571`
- [VmpCheckUnpinAndDereference](VmpCheckUnpinAndDereference_function_0064C540.md) at `0x0064C593`
- [VmpCheckUnpinAndDereference](VmpCheckUnpinAndDereference_function_0064C540.md) at `0x0064C5B4`
- [VmpCheckUnpinAndDereference](VmpCheckUnpinAndDereference_function_0064C540.md) at `0x0064C5D5`
- [VmpUnpinMemoryRangeHelper](VmpUnpinMemoryRangeHelper_function_0064D370.md) at `0x0064D4B4`
- [VmpUpdateCommitStateMemoryRange](VmpUpdateCommitStateMemoryRange_function_0064D5D0.md) at `0x0064D703`
- [sub_006E128A](../6E/Unknown_function_006E128A.md) at `0x006E1299`
- [sub_006E128A](../6E/Unknown_function_006E128A.md) at `0x006E12BF`
- [sub_006E128A](../6E/Unknown_function_006E128A.md) at `0x006E1359`
- [sub_006EE148](../6E/Unknown_function_006EE148.md) at `0x006EE1FB`
- [sub_006F5CAE](../6F/Unknown_function_006F5CAE.md) at `0x006F5CF5`
- [sub_006F5CAE](../6F/Unknown_function_006F5CAE.md) at `0x006F5D15`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064C7E4  48 8B C4                        mov rax, rsp
0064C7E7  48 89 58 08                     mov qword ptr [rax + 8], rbx
0064C7EB  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064C7EF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064C7F3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064C7F7  4C 8B D2                        mov r10, rdx
0064C7FA  41 8B F9                        mov edi, r9d
0064C7FD  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
0064C801  49 8B F0                        mov rsi, r8
0064C804  48 8B E9                        mov rbp, rcx
0064C807  48 85 D2                        test rdx, rdx
0064C80A  74 10                           je 0x14064c81c
0064C80C  4C 3B 52 18                     cmp r10, qword ptr [rdx + 0x18]
0064C810  72 0A                           jb 0x14064c81c
0064C812  4C 3B 52 20                     cmp r10, qword ptr [rdx + 0x20]
0064C816  0F 86 A3 00 00 00               jbe 0x14064c8bf
0064C81C  48 83 C1 28                     add rcx, 0x28
0064C820  F6 41 08 01                     test byte ptr [rcx + 8], 1
0064C824  48 8B 11                        mov rdx, qword ptr [rcx]
0064C827  74 08                           je 0x14064c831
0064C829  48 85 D2                        test rdx, rdx
0064C82C  74 03                           je 0x14064c831
0064C82E  48 33 D1                        xor rdx, rcx
0064C831  44 0F B6 41 08                  movzx r8d, byte ptr [rcx + 8]
0064C836  41 83 E0 01                     and r8d, 1
0064C83A  33 C9                           xor ecx, ecx
0064C83C  48 85 D2                        test rdx, rdx
0064C83F  0F 84 AD 00 00 00               je 0x14064c8f2
0064C845  4C 3B 52 18                     cmp r10, qword ptr [rdx + 0x18]
0064C849  73 08                           jae 0x14064c853
0064C84B  48 8B 02                        mov rax, qword ptr [rdx]
0064C84E  48 8B CA                        mov rcx, rdx
0064C851  EB 0A                           jmp 0x14064c85d
0064C853  4C 3B 52 20                     cmp r10, qword ptr [rdx + 0x20]
0064C857  76 18                           jbe 0x14064c871
0064C859  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0064C85D  45 85 C0                        test r8d, r8d
0064C860  74 0A                           je 0x14064c86c
0064C862  48 85 C0                        test rax, rax
0064C865  74 05                           je 0x14064c86c
0064C867  48 33 D0                        xor rdx, rax
0064C86A  EB D0                           jmp 0x14064c83c
0064C86C  48 8B D0                        mov rdx, rax
0064C86F  EB CB                           jmp 0x14064c83c
0064C871  48 8B 02                        mov rax, qword ptr [rdx]
0064C874  45 85 C0                        test r8d, r8d
0064C877  74 08                           je 0x14064c881
0064C879  48 85 C0                        test rax, rax
0064C87C  74 03                           je 0x14064c881
0064C87E  48 33 C2                        xor rax, rdx
0064C881  45 33 C9                        xor r9d, r9d
0064C884  48 85 C0                        test rax, rax
0064C887  74 36                           je 0x14064c8bf
0064C889  4C 3B 50 18                     cmp r10, qword ptr [rax + 0x18]
0064C88D  72 0F                           jb 0x14064c89e
0064C88F  4C 3B 50 20                     cmp r10, qword ptr [rax + 0x20]
0064C893  76 06                           jbe 0x14064c89b
0064C895  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0064C899  EB 06                           jmp 0x14064c8a1
0064C89B  4C 8B C8                        mov r9, rax
0064C89E  48 8B 08                        mov rcx, qword ptr [rax]
0064C8A1  45 85 C0                        test r8d, r8d
0064C8A4  74 0A                           je 0x14064c8b0
0064C8A6  48 85 C9                        test rcx, rcx
0064C8A9  74 05                           je 0x14064c8b0
0064C8AB  48 33 C1                        xor rax, rcx
0064C8AE  EB 03                           jmp 0x14064c8b3
0064C8B0  48 8B C1                        mov rax, rcx
0064C8B3  48 85 C0                        test rax, rax
0064C8B6  75 D1                           jne 0x14064c889
0064C8B8  4D 85 C9                        test r9, r9
0064C8BB  49 0F 45 D1                     cmovne rdx, r9
0064C8BF  4D 8B C2                        mov r8, r10
0064C8C2  48 85 D2                        test rdx, rdx
0064C8C5  0F 84 F9 00 00 00               je 0x14064c9c4
0064C8CB  4C 8B 5A 18                     mov r11, qword ptr [rdx + 0x18]
0064C8CF  4D 3B D8                        cmp r11, r8
0064C8D2  76 11                           jbe 0x14064c8e5
0064C8D4  85 FF                           test edi, edi
0064C8D6  0F 84 EC 00 00 00               je 0x14064c9c8
0064C8DC  4C 3B DE                        cmp r11, rsi
0064C8DF  0F 87 E8 00 00 00               ja 0x14064c9cd
0064C8E5  4D 3B D3                        cmp r10, r11
0064C8E8  76 1F                           jbe 0x14064c909
0064C8EA  41 8B CA                        mov ecx, r10d
0064C8ED  2B 4A 18                        sub ecx, dword ptr [rdx + 0x18]
0064C8F0  EB 19                           jmp 0x14064c90b
0064C8F2  48 8B D1                        mov rdx, rcx
0064C8F5  48 85 C9                        test rcx, rcx
0064C8F8  75 C5                           jne 0x14064c8bf
0064C8FA  48 83 C8 FF                     or rax, 0xffffffffffffffff
0064C8FE  85 FF                           test edi, edi
0064C900  4C 0F 45 D0                     cmovne r10, rax
0064C904  E9 C8 00 00 00                  jmp 0x14064c9d1
0064C909  33 C9                           xor ecx, ecx
0064C90B  48 8B 5A 20                     mov rbx, qword ptr [rdx + 0x20]
0064C90F  44 8B CE                        mov r9d, esi
0064C912  48 3B F3                        cmp rsi, rbx
0064C915  72 03                           jb 0x14064c91a
0064C917  44 8B CB                        mov r9d, ebx
0064C91A  44 2B 4A 18                     sub r9d, dword ptr [rdx + 0x18]
0064C91E  41 3B C9                        cmp ecx, r9d
0064C921  77 43                           ja 0x14064c966
0064C923  44 8A 44 11 28                  mov r8b, byte ptr [rcx + rdx + 0x28]
0064C928  85 FF                           test edi, edi
0064C92A  75 05                           jne 0x14064c931
0064C92C  45 84 C0                        test r8b, r8b
0064C92F  EB 27                           jmp 0x14064c958
0064C931  41 80 F8 01                     cmp r8b, 1
0064C935  72 23                           jb 0x14064c95a
0064C937  83 FF 01                        cmp edi, 1
0064C93A  74 25                           je 0x14064c961
0064C93C  83 FF 02                        cmp edi, 2
0064C93F  75 06                           jne 0x14064c947
0064C941  41 80 F8 01                     cmp r8b, 1
0064C945  EB 11                           jmp 0x14064c958
0064C947  83 FF 03                        cmp edi, 3
0064C94A  75 08                           jne 0x14064c954
0064C94C  41 80 F8 01                     cmp r8b, 1
0064C950  77 0F                           ja 0x14064c961
0064C952  EB 06                           jmp 0x14064c95a
0064C954  41 80 F8 FF                     cmp r8b, 0xff
0064C958  74 07                           je 0x14064c961
0064C95A  FF C1                           inc ecx
0064C95C  41 3B C9                        cmp ecx, r9d
0064C95F  76 C2                           jbe 0x14064c923
0064C961  41 3B C9                        cmp ecx, r9d
0064C964  76 52                           jbe 0x14064c9b8
0064C966  48 3B F3                        cmp rsi, rbx
0064C969  76 62                           jbe 0x14064c9cd
0064C96B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0064C96F  4C 8D 43 01                     lea r8, [rbx + 1]
0064C973  48 8B CA                        mov rcx, rdx
0064C976  48 85 C0                        test rax, rax
0064C979  74 2E                           je 0x14064c9a9
0064C97B  48 8B 08                        mov rcx, qword ptr [rax]
0064C97E  48 8B D0                        mov rdx, rax
0064C981  48 85 C9                        test rcx, rcx
0064C984  0F 84 38 FF FF FF               je 0x14064c8c2
0064C98A  48 8B 01                        mov rax, qword ptr [rcx]
0064C98D  48 8B D1                        mov rdx, rcx
0064C990  48 8B C8                        mov rcx, rax
0064C993  48 85 C0                        test rax, rax
0064C996  75 F2                           jne 0x14064c98a
0064C998  E9 25 FF FF FF                  jmp 0x14064c8c2
0064C99D  48 39 0A                        cmp qword ptr [rdx], rcx
0064C9A0  0F 84 1C FF FF FF               je 0x14064c8c2
0064C9A6  48 8B CA                        mov rcx, rdx
0064C9A9  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
0064C9AD  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
0064C9B1  75 EA                           jne 0x14064c99d
0064C9B3  E9 0A FF FF FF                  jmp 0x14064c8c2
0064C9B8  44 8B D1                        mov r10d, ecx
0064C9BB  4D 03 D3                        add r10, r11
0064C9BE  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
0064C9C2  EB 0D                           jmp 0x14064c9d1
0064C9C4  85 FF                           test edi, edi
0064C9C6  75 05                           jne 0x14064c9cd
0064C9C8  4D 8B D0                        mov r10, r8
0064C9CB  EB 04                           jmp 0x14064c9d1
0064C9CD  49 83 CA FF                     or r10, 0xffffffffffffffff
0064C9D1  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
0064C9D6  49 8B C2                        mov rax, r10
0064C9D9  48 8B 6C 24 10                  mov rbp, qword ptr [rsp + 0x10]
0064C9DE  48 8B 74 24 18                  mov rsi, qword ptr [rsp + 0x18]
0064C9E3  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
0064C9E8  C3                              ret
0064C9E9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpFindNextPinnedPageStateHelper(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_0064C81C;
    if (a2 < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 24))) goto loc_0064C81C;
    if (a2 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 32))) goto loc_0064C8BF;
loc_0064C81C:
    a1 = (a1) + (40);
    if (((*(unsigned __int8 *)(a1 + 8)) & (1)) == 0) goto loc_0064C831;
    if (*(unsigned __int64 *)(a1) != 0) {
        a2 = (*(unsigned __int64 *)(a1)) ^ (a1);
    }
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 8)) & (1));
    a1 = 0;
loc_0064C83C:
    if (a2 == 0) goto loc_0064C8F2;
    if (a2 >= (*(unsigned __int64 *)(a2 + 24))) goto loc_0064C853;
    goto loc_0064C85D;
loc_0064C853:
    if (a2 <= (*(unsigned __int64 *)(a2 + 32))) goto loc_0064C871;
loc_0064C85D:
    if ((unsigned int)(a3) == 0) goto loc_0064C86C;
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0064C86C;
    a2 = (a2) ^ (*(unsigned __int64 *)(a2 + 8));
    goto loc_0064C83C;
loc_0064C86C:
    goto loc_0064C83C;
loc_0064C871:
    if ((unsigned int)(a3) == 0) goto loc_0064C881;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) ^ (*(unsigned __int64 *)(a2 + 8));
    }
    a4 = 0;
    if (result == 0) goto loc_0064C8BF;
loc_0064C889:
    if (a2 < (*(unsigned __int64 *)(result + 24))) goto loc_0064C89E;
    if (a2 <= (*(unsigned __int64 *)(result + 32))) goto loc_0064C89B;
    goto loc_0064C8A1;
loc_0064C89B:
loc_0064C89E:
loc_0064C8A1:
    if ((unsigned int)(a3) == 0) goto loc_0064C8B0;
    if (*(unsigned __int64 *)(result) == 0) goto loc_0064C8B0;
    result = (result) ^ (*(unsigned __int64 *)(result));
    goto loc_0064C8B3;
loc_0064C8B0:
loc_0064C8B3:
    if (*(unsigned __int64 *)(result) != 0) goto loc_0064C889;
    a2 = *(unsigned __int64 *)(a2 + 8);
    if (result != 0) { a2 = result; }
loc_0064C8BF:
loc_0064C8C2:
    if (a2 == 0) goto loc_0064C9C4;
    if ((*(unsigned __int64 *)(a2 + 24)) <= a2) goto loc_0064C8E5;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_0064C9C8;
    if ((*(unsigned __int64 *)(a2 + 24)) > a3) goto loc_0064C9CD;
loc_0064C8E5:
    if (a2 <= (*(unsigned __int64 *)(a2 + 24))) goto loc_0064C909;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - (*(unsigned int *)(a2 + 24)));
    goto loc_0064C90B;
loc_0064C8F2:
    if (a1 != 0) goto loc_0064C8BF;
    result = (*(unsigned __int64 *)(result)) | (-1);
    if ((unsigned int)((unsigned int)(a4)) != 0) { a2 = result; }
    goto loc_0064C9D1;
loc_0064C909:
    a1 = 0;
loc_0064C90B:
    if (a3 >= (*(unsigned __int64 *)(a1 + 32))) {
        a4 = (unsigned int)(*(unsigned __int64 *)(a1 + 32));
    }
    a4 = (unsigned int)((a4) - (*(unsigned int *)(a1 + 24)));
    if (0 > a4) goto loc_0064C966;
loc_0064C923:
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_0064C931;
    goto loc_0064C958;
loc_0064C931:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + a1 * 1 + 40))) < 1) goto loc_0064C95A;
    if (((unsigned int)((unsigned int)(a4))) == 1) goto loc_0064C961;
    if (((unsigned int)((unsigned int)(a4))) != 2) goto loc_0064C947;
    goto loc_0064C958;
loc_0064C947:
    if (((unsigned int)((unsigned int)(a4))) != 3) goto loc_0064C954;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + a1 * 1 + 40))) > 1) goto loc_0064C961;
    goto loc_0064C95A;
loc_0064C954:
loc_0064C958:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + a1 * 1 + 40))) == 255) goto loc_0064C961;
loc_0064C95A:
    a1 = (unsigned int)((a1) + 1);
    if (((unsigned int)(a1)) <= a4) goto loc_0064C923;
loc_0064C961:
    if (((unsigned int)(a1)) <= a4) goto loc_0064C9B8;
loc_0064C966:
    if (a3 <= (*(unsigned __int64 *)(a1 + 32))) goto loc_0064C9CD;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0064C9A9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) == 0) goto loc_0064C8C2;
loc_0064C98A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != 0) goto loc_0064C98A;
    goto loc_0064C8C2;
loc_0064C99D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_0064C8C2;
loc_0064C9A9:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0064C99D;
    goto loc_0064C8C2;
loc_0064C9B8:
    v_r10 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))))) + (*(unsigned __int64 *)(a2 + 24));
    *(unsigned __int64 *)(a1 + 56) = a2;
    goto loc_0064C9D1;
loc_0064C9C4:
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_0064C9CD;
loc_0064C9C8:
    goto loc_0064C9D1;
loc_0064C9CD:
    v_r10 = (*(unsigned __int64 *)(a1 + 32) + 1) | (-1);
loc_0064C9D1:
    return v_r10;
}
```

## 5. (Beta) C Style

```c
int64_t VmpFindNextPinnedPageStateHelper(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_0064C81C;
    if (Arg2 < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x18))) goto loc_0064C81C;
    if (Arg2 <= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x20))) goto loc_0064C8BF;
loc_0064C81C:
    Arg1 = (Arg1) + (40);
    if (((*(uint8_t *)(arg1 + 0x8)) & (1)) == 0) goto loc_0064C831;
    if (*(uint64_t *)(arg1) != 0) {
        Arg2 = (*(uint64_t *)(arg1)) ^ (Arg1);
    }
    Arg3 = (uint32_t)((*(uint8_t *)(arg1 + 0x8)) & (1));
    Arg1 = 0;
loc_0064C83C:
    if (Arg2 == 0) goto loc_0064C8F2;
    if (Arg2 >= (*(uint64_t *)(Arg2 + 0x18))) goto loc_0064C853;
    goto loc_0064C85D;
loc_0064C853:
    if (Arg2 <= (*(uint64_t *)(Arg2 + 0x20))) goto loc_0064C871;
loc_0064C85D:
    if ((uint32_t)(Arg3) == 0) goto loc_0064C86C;
    if (*(uint64_t *)(Arg2 + 0x8) == 0) goto loc_0064C86C;
    Arg2 = (Arg2) ^ (*(uint64_t *)(Arg2 + 0x8));
    goto loc_0064C83C;
loc_0064C86C:
    goto loc_0064C83C;
loc_0064C871:
    if ((uint32_t)(Arg3) == 0) goto loc_0064C881;
    result = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8));
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8)) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8))) ^ (*(uint64_t *)(Arg2 + 0x8));
    }
    Arg4 = 0;
    if (result == 0) goto loc_0064C8BF;
loc_0064C889:
    if (Arg2 < (*(uint64_t *)(result + 0x18))) goto loc_0064C89E;
    if (Arg2 <= (*(uint64_t *)(result + 0x20))) goto loc_0064C89B;
    goto loc_0064C8A1;
loc_0064C89B:
loc_0064C89E:
loc_0064C8A1:
    if ((uint32_t)(Arg3) == 0) goto loc_0064C8B0;
    if (*(uint64_t *)(result) == 0) goto loc_0064C8B0;
    result = (result) ^ (*(uint64_t *)(result));
    goto loc_0064C8B3;
loc_0064C8B0:
loc_0064C8B3:
    if (*(uint64_t *)(result) != 0) goto loc_0064C889;
    Arg2 = *(uint64_t *)(Arg2 + 0x8);
    if (result != 0) { Arg2 = result; }
loc_0064C8BF:
loc_0064C8C2:
    if (Arg2 == 0) goto loc_0064C9C4;
    if ((*(uint64_t *)(Arg2 + 0x18)) <= Arg2) goto loc_0064C8E5;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_0064C9C8;
    if ((*(uint64_t *)(Arg2 + 0x18)) > Arg3) goto loc_0064C9CD;
loc_0064C8E5:
    if (Arg2 <= (*(uint64_t *)(Arg2 + 0x18))) goto loc_0064C909;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - (*(uint32_t *)(Arg2 + 0x18)));
    goto loc_0064C90B;
loc_0064C8F2:
    if (Arg1 != NULL) goto loc_0064C8BF;
    result = (*(uint64_t *)(result)) | (-1);
    if ((uint32_t)((uint32_t)(Arg4)) != 0) { Arg2 = result; }
    goto loc_0064C9D1;
loc_0064C909:
    Arg1 = 0;
loc_0064C90B:
    if (Arg3 >= (*(uint64_t *)(arg1 + 0x20))) {
        Arg4 = (uint32_t)(*(uint64_t *)(arg1 + 0x20));
    }
    Arg4 = (uint32_t)((Arg4) - (*(uint32_t *)(arg1 + 0x18)));
    if (0 > Arg4) goto loc_0064C966;
loc_0064C923:
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_0064C931;
    goto loc_0064C958;
loc_0064C931:
    if (((uint8_t)(*(uint8_t *)(arg1 + arg1 * 1 + 0x28))) < 1) goto loc_0064C95A;
    if (((uint32_t)((uint32_t)(Arg4))) == 1) goto loc_0064C961;
    if (((uint32_t)((uint32_t)(Arg4))) != 2) goto loc_0064C947;
    goto loc_0064C958;
loc_0064C947:
    if (((uint32_t)((uint32_t)(Arg4))) != 3) goto loc_0064C954;
    if (((uint8_t)(*(uint8_t *)(arg1 + arg1 * 1 + 0x28))) > 1) goto loc_0064C961;
    goto loc_0064C95A;
loc_0064C954:
loc_0064C958:
    if (((uint8_t)(*(uint8_t *)(arg1 + arg1 * 1 + 0x28))) == 255) goto loc_0064C961;
loc_0064C95A:
    Arg1 = (uint32_t)((Arg1) + 1);
    if (((uint32_t)(Arg1)) <= Arg4) goto loc_0064C923;
loc_0064C961:
    if (((uint32_t)(Arg1)) <= Arg4) goto loc_0064C9B8;
loc_0064C966:
    if (Arg3 <= (*(uint64_t *)(arg1 + 0x20))) goto loc_0064C9CD;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_0064C9A9;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) == 0) goto loc_0064C8C2;
loc_0064C98A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != 0) goto loc_0064C98A;
    goto loc_0064C8C2;
loc_0064C99D:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_0064C8C2;
loc_0064C9A9:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0064C99D;
    goto loc_0064C8C2;
loc_0064C9B8:
    local_r10 = ((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))))) + (*(uint64_t *)(Arg2 + 0x18));
    *(uint64_t *)(arg1 + 0x38) = Arg2;
    goto loc_0064C9D1;
loc_0064C9C4:
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_0064C9CD;
loc_0064C9C8:
    goto loc_0064C9D1;
loc_0064C9CD:
    local_r10 = (*(uint64_t *)(arg1 + 0x20) + 1) | (-1);
loc_0064C9D1:
    return local_r10;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064C7E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
