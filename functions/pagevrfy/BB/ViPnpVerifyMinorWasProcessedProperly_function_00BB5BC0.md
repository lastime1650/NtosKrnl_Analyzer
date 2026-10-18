# ViPnpVerifyMinorWasProcessedProperly

- RVA: `0x00BB5BC0`–`0x00BB5DEF` (길이 `559` bytes)
- VA: `0x0000000140BB5BC0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008FC44`
- 디코드: `155`개 명령, `559/559` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB5C81` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (function, `0x00614584`)
- `0x00BB5CCC` → [MmIsNonPagedSystemAddressValid](../../text/4B/MmIsNonPagedSystemAddressValid_function_004B79F0.md) (function, `0x004B79F0`)
- `0x00BB5CF0` → [IovUtilIsDeviceObjectMarked](../BA/IovUtilIsDeviceObjectMarked_function_00BA2B34.md) (function, `0x00BA2B34`)
- `0x00BB5CFC` → [IovUtilGetBottomDeviceObjectWithTag](../BA/IovUtilGetBottomDeviceObjectWithTag_function_00BA2A20.md) (function, `0x00BA2A20`)
- `0x00BB5D19` → [ViErrorReport10](../../text/61/ViErrorReport10_function_00614608.md) (function, `0x00614608`)
- `0x00BB5D26` → [IovUtilMarkDeviceObject](../../text/4B/IovUtilMarkDeviceObject_function_004B77B0.md) (function, `0x004B77B0`)
- `0x00BB5D33` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00BB5DCE` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (function, `0x00614584`)

### Direct callers
- [VfPnpVerifyIrpStackDownward](VfPnpVerifyIrpStackDownward_function_00BB5750.md) at `0x00BB58AC`
- [VfPnpVerifyIrpStackUpward](VfPnpVerifyIrpStackUpward_function_00BB58E0.md) at `0x00BB59F3`

### Static image references
- `0x00BB5C86` → RVA `0x00FF4000` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00BB5C81` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (`PAGEVRFY` → `.text`)
  - `0x00BB5CCC` → [MmIsNonPagedSystemAddressValid](../../text/4B/MmIsNonPagedSystemAddressValid_function_004B79F0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB5D19` → [ViErrorReport10](../../text/61/ViErrorReport10_function_00614608.md) (`PAGEVRFY` → `.text`)
  - `0x00BB5D26` → [IovUtilMarkDeviceObject](../../text/4B/IovUtilMarkDeviceObject_function_004B77B0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB5D33` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB5DCE` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB5BC0  48 8B C4                        mov rax, rsp
00BB5BC3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00BB5BC7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00BB5BCB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00BB5BCF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00BB5BD3  41 57                           push r15
00BB5BD5  48 83 EC 20                     sub rsp, 0x20
00BB5BD9  44 0F B6 52 01                  movzx r10d, byte ptr [rdx + 1]
00BB5BDE  48 8B F2                        mov rsi, rdx
00BB5BE1  48 8B D9                        mov rbx, rcx
00BB5BE4  41 83 FA 0A                     cmp r10d, 0xa
00BB5BE8  0F 87 80 01 00 00               ja 0x140bb5d6e
00BB5BEE  0F 84 C2 01 00 00               je 0x140bb5db6
00BB5BF4  45 85 D2                        test r10d, r10d
00BB5BF7  0F 84 5E 01 00 00               je 0x140bb5d5b
00BB5BFD  41 83 EA 01                     sub r10d, 1
00BB5C01  0F 84 54 01 00 00               je 0x140bb5d5b
00BB5C07  41 83 EA 01                     sub r10d, 1
00BB5C0B  0F 84 32 01 00 00               je 0x140bb5d43
00BB5C11  41 83 EA 01                     sub r10d, 1
00BB5C15  0F 84 40 01 00 00               je 0x140bb5d5b
00BB5C1B  41 83 EA 01                     sub r10d, 1
00BB5C1F  0F 84 36 01 00 00               je 0x140bb5d5b
00BB5C25  41 83 EA 01                     sub r10d, 1
00BB5C29  0F 84 2C 01 00 00               je 0x140bb5d5b
00BB5C2F  41 83 EA 01                     sub r10d, 1
00BB5C33  0F 84 22 01 00 00               je 0x140bb5d5b
00BB5C39  41 83 FA 01                     cmp r10d, 1
00BB5C3D  0F 85 90 01 00 00               jne 0x140bb5dd3
00BB5C43  83 7A 08 04                     cmp dword ptr [rdx + 8], 4
00BB5C47  75 3D                           jne 0x140bb5c86
00BB5C49  45 85 C0                        test r8d, r8d
00BB5C4C  74 0D                           je 0x140bb5c5b
00BB5C4E  41 83 F9 02                     cmp r9d, 2
00BB5C52  75 32                           jne 0x140bb5c86
00BB5C54  B9 18 02 00 00                  mov ecx, 0x218
00BB5C59  EB 1E                           jmp 0x140bb5c79
00BB5C5B  45 85 C9                        test r9d, r9d
00BB5C5E  75 07                           jne 0x140bb5c67
00BB5C60  B9 2A 02 00 00                  mov ecx, 0x22a
00BB5C65  EB 12                           jmp 0x140bb5c79
00BB5C67  83 79 30 00                     cmp dword ptr [rcx + 0x30], 0
00BB5C6B  7C 19                           jl 0x140bb5c86
00BB5C6D  48 83 79 38 00                  cmp qword ptr [rcx + 0x38], 0
00BB5C72  75 12                           jne 0x140bb5c86
00BB5C74  B9 2B 02 00 00                  mov ecx, 0x22b
00BB5C79  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00BB5C7E  4C 8B C3                        mov r8, rbx
00BB5C81  E8 FE E8 A5 FF                  call 0x140614584
00BB5C86  8B 05 74 E3 43 00               mov eax, dword ptr [rip + 0x43e374]
00BB5C8C  85 C0                           test eax, eax
00BB5C8E  0F 85 3F 01 00 00               jne 0x140bb5dd3
00BB5C94  39 43 30                        cmp dword ptr [rbx + 0x30], eax
00BB5C97  0F 8C 36 01 00 00               jl 0x140bb5dd3
00BB5C9D  48 8B 7B 38                     mov rdi, qword ptr [rbx + 0x38]
00BB5CA1  48 85 FF                        test rdi, rdi
00BB5CA4  0F 84 29 01 00 00               je 0x140bb5dd3
00BB5CAA  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
00BB5CAD  85 C9                           test ecx, ecx
00BB5CAF  74 18                           je 0x140bb5cc9
00BB5CB1  83 E9 01                        sub ecx, 1
00BB5CB4  74 13                           je 0x140bb5cc9
00BB5CB6  83 E9 01                        sub ecx, 1
00BB5CB9  74 0E                           je 0x140bb5cc9
00BB5CBB  83 E9 01                        sub ecx, 1
00BB5CBE  74 09                           je 0x140bb5cc9
00BB5CC0  83 F9 01                        cmp ecx, 1
00BB5CC3  0F 85 0A 01 00 00               jne 0x140bb5dd3
00BB5CC9  48 8B CF                        mov rcx, rdi
00BB5CCC  E8 1F 1D 90 FF                  call 0x1404b79f0
00BB5CD1  84 C0                           test al, al
00BB5CD3  0F 84 FA 00 00 00               je 0x140bb5dd3
00BB5CD9  33 F6                           xor esi, esi
00BB5CDB  39 37                           cmp dword ptr [rdi], esi
00BB5CDD  0F 86 F0 00 00 00               jbe 0x140bb5dd3
00BB5CE3  48 8B 6C F7 08                  mov rbp, qword ptr [rdi + rsi*8 + 8]
00BB5CE8  BA 05 00 00 00                  mov edx, 5
00BB5CED  48 8B CD                        mov rcx, rbp
00BB5CF0  E8 3F CE FE FF                  call 0x140ba2b34
00BB5CF5  85 C0                           test eax, eax
00BB5CF7  75 3F                           jne 0x140bb5d38
00BB5CF9  48 8B CD                        mov rcx, rbp
00BB5CFC  E8 1F CD FE FF                  call 0x140ba2a20
00BB5D01  4C 8B F8                        mov r15, rax
00BB5D04  48 3B C5                        cmp rax, rbp
00BB5D07  74 15                           je 0x140bb5d1e
00BB5D09  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00BB5D0E  4C 8B CD                        mov r9, rbp
00BB5D11  4C 8B C3                        mov r8, rbx
00BB5D14  B9 48 02 00 00                  mov ecx, 0x248
00BB5D19  E8 EA E8 A5 FF                  call 0x140614608
00BB5D1E  BA 05 00 00 00                  mov edx, 5
00BB5D23  48 8B CD                        mov rcx, rbp
00BB5D26  E8 85 1A 90 FF                  call 0x1404b77b0
00BB5D2B  BA 56 72 66 49                  mov edx, 0x49667256
00BB5D30  49 8B CF                        mov rcx, r15
00BB5D33  E8 A8 1B 74 FF                  call 0x1402f78e0
00BB5D38  FF C6                           inc esi
00BB5D3A  3B 37                           cmp esi, dword ptr [rdi]
00BB5D3C  72 A5                           jb 0x140bb5ce3
00BB5D3E  E9 90 00 00 00                  jmp 0x140bb5dd3
00BB5D43  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
00BB5D48  0F 85 85 00 00 00               jne 0x140bb5dd3
00BB5D4E  41 83 F9 02                     cmp r9d, 2
00BB5D52  74 7F                           je 0x140bb5dd3
00BB5D54  B9 06 03 00 00                  mov ecx, 0x306
00BB5D59  EB 6B                           jmp 0x140bb5dc6
00BB5D5B  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
00BB5D60  75 71                           jne 0x140bb5dd3
00BB5D62  45 85 C9                        test r9d, r9d
00BB5D65  75 6C                           jne 0x140bb5dd3
00BB5D67  B9 17 02 00 00                  mov ecx, 0x217
00BB5D6C  EB 58                           jmp 0x140bb5dc6
00BB5D6E  41 83 EA 0B                     sub r10d, 0xb
00BB5D72  74 42                           je 0x140bb5db6
00BB5D74  41 83 EA 01                     sub r10d, 1
00BB5D78  74 3C                           je 0x140bb5db6
00BB5D7A  41 83 EA 03                     sub r10d, 3
00BB5D7E  74 36                           je 0x140bb5db6
00BB5D80  41 83 EA 01                     sub r10d, 1
00BB5D84  74 30                           je 0x140bb5db6
00BB5D86  41 83 EA 01                     sub r10d, 1
00BB5D8A  74 2A                           je 0x140bb5db6
00BB5D8C  41 83 EA 01                     sub r10d, 1
00BB5D90  74 24                           je 0x140bb5db6
00BB5D92  41 83 EA 01                     sub r10d, 1
00BB5D96  74 08                           je 0x140bb5da0
00BB5D98  41 83 FA 02                     cmp r10d, 2
00BB5D9C  74 18                           je 0x140bb5db6
00BB5D9E  EB 33                           jmp 0x140bb5dd3
00BB5DA0  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
00BB5DA3  85 C9                           test ecx, ecx
00BB5DA5  74 0F                           je 0x140bb5db6
00BB5DA7  83 E9 01                        sub ecx, 1
00BB5DAA  74 0A                           je 0x140bb5db6
00BB5DAC  83 E9 01                        sub ecx, 1
00BB5DAF  74 05                           je 0x140bb5db6
00BB5DB1  83 F9 01                        cmp ecx, 1
00BB5DB4  75 1D                           jne 0x140bb5dd3
00BB5DB6  45 85 C0                        test r8d, r8d
00BB5DB9  74 18                           je 0x140bb5dd3
00BB5DBB  41 83 F9 02                     cmp r9d, 2
00BB5DBF  75 12                           jne 0x140bb5dd3
00BB5DC1  B9 18 02 00 00                  mov ecx, 0x218
00BB5DC6  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00BB5DCB  4C 8B C3                        mov r8, rbx
00BB5DCE  E8 B1 E7 A5 FF                  call 0x140614584
00BB5DD3  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BB5DD8  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00BB5DDD  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB5DE2  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BB5DE7  48 83 C4 20                     add rsp, 0x20
00BB5DEB  41 5F                           pop r15
00BB5DED  C3                              ret
00BB5DEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViPnpVerifyMinorWasProcessedProperly(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 1))) > 10) goto loc_00BB5D6E;
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 1))) == 10) goto loc_00BB5DB6;
    if ((unsigned int)(*(unsigned __int8 *)(a2 + 1)) == 0) goto loc_00BB5D5B;
    v_r10 = (unsigned int)((*(unsigned __int8 *)(a2 + 1)) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D43;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    if (((unsigned int)(v_r10)) != 1) goto loc_00BB5DD3;
    if ((*(unsigned int *)(a2 + 8)) != 4) goto loc_00BB5C86;
    if (a3 == 0) goto loc_00BB5C5B;
    if (a4 != 2) goto loc_00BB5C86;
    goto loc_00BB5C79;
loc_00BB5C5B:
    if (a4 != 0) goto loc_00BB5C67;
    goto loc_00BB5C79;
loc_00BB5C67:
    if ((*(unsigned int *)(554 + 48)) < 0) goto loc_00BB5C86;
    if ((*(unsigned __int64 *)(554 + 56)) != 0) goto loc_00BB5C86;
loc_00BB5C79:
    result = ViErrorReport1(555, a5, a1, a4);
loc_00BB5C86:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4449140))) != 0) goto loc_00BB5DD3;
    if ((*(unsigned int *)(a1 + 48)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4449140))))) goto loc_00BB5DD3;
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_00BB5DD3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))) == 0) goto loc_00BB5CC9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    if (((unsigned int)(a1)) != 1) goto loc_00BB5DD3;
loc_00BB5CC9:
    result = MmIsNonPagedSystemAddressValid(*(unsigned __int64 *)(a1 + 56), a5, a1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00BB5DD3;
    v_rsi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 56))) <= 0) goto loc_00BB5DD3;
loc_00BB5CE3:
    result = IovUtilIsDeviceObjectMarked(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + v_rsi * 8 + 8), 5, a1, a4);
    if ((unsigned int)(result) != 0) goto loc_00BB5D38;
    result = IovUtilGetBottomDeviceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + v_rsi * 8 + 8), 5, a1, a4);
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + v_rsi * 8 + 8))) {
        a2 = a5;
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + v_rsi * 8 + 8);
        a3 = a1;
        a1 = 584;
        result = ViErrorReport10(a1, a2, a3, a4);
    }
    result = IovUtilMarkDeviceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + v_rsi * 8 + 8), 5, a3, a4);
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x49667256ULL), a3, a4);
loc_00BB5D38:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 56)))) goto loc_00BB5CE3;
    goto loc_00BB5DD3;
loc_00BB5D43:
    if (a6 != 0) goto loc_00BB5DD3;
    if (a4 == 2) goto loc_00BB5DD3;
    goto loc_00BB5DC6;
loc_00BB5D5B:
    if (a6 != 0) goto loc_00BB5DD3;
    if (a4 != 0) goto loc_00BB5DD3;
    goto loc_00BB5DC6;
loc_00BB5D6E:
    v_r10 = (unsigned int)((v_r10) - (11));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (3));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DA0;
    if (((unsigned int)(v_r10)) == 2) goto loc_00BB5DB6;
    goto loc_00BB5DD3;
loc_00BB5DA0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x49667256ULL) + 8))) == 0) goto loc_00BB5DB6;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0x49667256ULL) + 8))) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    if (((unsigned int)(a1)) != 1) goto loc_00BB5DD3;
loc_00BB5DB6:
    if (a3 == 0) goto loc_00BB5DD3;
    if (a4 != 2) goto loc_00BB5DD3;
loc_00BB5DC6:
    result = ViErrorReport1(536, a5, a1, a4);
loc_00BB5DD3:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViPnpVerifyMinorWasProcessedProperly(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    if (((uint32_t)(*(uint8_t *)(arg2 + 0x1))) > 10) goto loc_00BB5D6E;
    if (((uint32_t)(*(uint8_t *)(arg2 + 0x1))) == 10) goto loc_00BB5DB6;
    if ((uint32_t)(*(uint8_t *)(arg2 + 0x1)) == 0) goto loc_00BB5D5B;
    local_r10 = (uint32_t)((*(uint8_t *)(arg2 + 0x1)) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D43;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5D5B;
    if (((uint32_t)(local_r10)) != 1) goto loc_00BB5DD3;
    if ((*(uint32_t *)(arg2 + 0x8)) != 4) goto loc_00BB5C86;
    if (Arg3 == 0) goto loc_00BB5C5B;
    if (Arg4 != 2) goto loc_00BB5C86;
    goto loc_00BB5C79;
loc_00BB5C5B:
    if (Arg4 != 0) goto loc_00BB5C67;
    goto loc_00BB5C79;
loc_00BB5C67:
    if ((*(uint32_t *)(554 + 0x30)) < 0) goto loc_00BB5C86;
    if ((*(uint64_t *)(554 + 0x38)) != 0) goto loc_00BB5C86;
loc_00BB5C79:
    result = ViErrorReport1(555, Arg5, Arg1, Arg4);
loc_00BB5C86:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x43E374))) != 0) goto loc_00BB5DD3;
    if ((*(uint32_t *)(arg1 + 0x30)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x43E374))))) goto loc_00BB5DD3;
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_00BB5DD3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))) == 0) goto loc_00BB5CC9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x8))) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BB5CC9;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BB5DD3;
loc_00BB5CC9:
    result = MmIsNonPagedSystemAddressValid(*(uint64_t *)(arg1 + 0x38), Arg5, Arg1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00BB5DD3;
    local_rsi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x38))) <= 0) goto loc_00BB5DD3;
loc_00BB5CE3:
    result = IovUtilIsDeviceObjectMarked(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + local_rsi * 8 + 0x8), 5, Arg1, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00BB5D38;
    result = IovUtilGetBottomDeviceObjectWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + local_rsi * 8 + 0x8), 5, Arg1, Arg4);
    if (result != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + local_rsi * 8 + 0x8))) {
        Arg2 = Arg5;
        Arg4 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + local_rsi * 8 + 0x8);
        Arg3 = Arg1;
        Arg1 = 584;
        result = ViErrorReport10(Arg1, Arg2, Arg3, Arg4);
    }
    result = IovUtilMarkDeviceObject(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + local_rsi * 8 + 0x8), 5, Arg3, Arg4);
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x49667256ULL), Arg3, Arg4);
loc_00BB5D38:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x38)))) goto loc_00BB5CE3;
    goto loc_00BB5DD3;
loc_00BB5D43:
    if (Arg6 != 0) goto loc_00BB5DD3;
    if (Arg4 == 2) goto loc_00BB5DD3;
    goto loc_00BB5DC6;
loc_00BB5D5B:
    if (Arg6 != 0) goto loc_00BB5DD3;
    if (Arg4 != 0) goto loc_00BB5DD3;
    goto loc_00BB5DC6;
loc_00BB5D6E:
    local_r10 = (uint32_t)((local_r10) - (11));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (3));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_00BB5DA0;
    if (((uint32_t)(local_r10)) == 2) goto loc_00BB5DB6;
    goto loc_00BB5DD3;
loc_00BB5DA0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x49667256ULL) + 0x8))) == 0) goto loc_00BB5DB6;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0x49667256ULL) + 0x8))) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BB5DB6;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BB5DD3;
loc_00BB5DB6:
    if (Arg3 == 0) goto loc_00BB5DD3;
    if (Arg4 != 2) goto loc_00BB5DD3;
loc_00BB5DC6:
    result = ViErrorReport1(536, Arg5, Arg1, Arg4);
loc_00BB5DD3:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x1` | `8` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB5BC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
