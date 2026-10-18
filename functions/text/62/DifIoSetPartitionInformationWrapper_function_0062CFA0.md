# DifIoSetPartitionInformationWrapper

- RVA: `0x0062CFA0`–`0x0062D129` (길이 `393` bytes)
- VA: `0x000000014062CFA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `113`개 명령, `393/393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062CFE2` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062D00A` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062D046` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D06C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D085` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062D097` → [IoSetPartitionInformation](../../page/71/IoSetPartitionInformation_function_00717680.md) (function, `0x00717680`)
- `0x0062D0C3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D0E9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D102` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062D01A` → RVA `0x00F048B8` (`.data`; read)
- `0x0062D033` → RVA `0x00F04980` (`.data`; read)
- `0x0062D03F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062D097` → [IoSetPartitionInformation](../../page/71/IoSetPartitionInformation_function_00717680.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062CFA0  48 8B C4                        mov rax, rsp
0062CFA3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062CFA7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062CFAB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062CFAF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0062CFB3  55                              push rbp
0062CFB4  41 54                           push r12
0062CFB6  41 55                           push r13
0062CFB8  41 56                           push r14
0062CFBA  41 57                           push r15
0062CFBC  48 8B EC                        mov rbp, rsp
0062CFBF  48 83 EC 50                     sub rsp, 0x50
0062CFC3  0F 57 C0                        xorps xmm0, xmm0
0062CFC6  33 C0                           xor eax, eax
0062CFC8  B9 37 01 00 00                  mov ecx, 0x137
0062CFCD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062CFD1  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062CFD5  45 8B F9                        mov r15d, r9d
0062CFD8  45 8B E0                        mov r12d, r8d
0062CFDB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062CFDF  44 8B EA                        mov r13d, edx
0062CFE2  E8 4D 8A E6 FF                  call 0x140495a34
0062CFE7  4C 8B F0                        mov r14, rax
0062CFEA  48 85 C0                        test rax, rax
0062CFED  0F 84 97 00 00 00               je 0x14062d08a
0062CFF3  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0062CFF6  F6 C1 18                        test cl, 0x18
0062CFF9  74 0A                           je 0x14062d005
0062CFFB  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062CFFF  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062D003  EB 0E                           jmp 0x14062d013
0062D005  F6 C1 04                        test cl, 4
0062D008  74 09                           je 0x14062d013
0062D00A  E8 F9 6B EA FF                  call 0x1404d3c08
0062D00F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062D013  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0062D017  40 32 F6                        xor sil, sil
0062D01A  40 38 35 97 78 8D 00            cmp byte ptr [rip + 0x8d7897], sil
0062D021  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0062D025  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
0062D029  44 89 65 DC                     mov dword ptr [rbp - 0x24], r12d
0062D02D  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0062D031  75 0C                           jne 0x14062d03f
0062D033  F7 05 43 79 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7943], 0x800
0062D03D  74 13                           je 0x14062d052
0062D03F  48 8D 0D 3A 6E 8D 00            lea rcx, [rip + 0x8d6e3a]
0062D046  E8 D5 95 BE FF                  call 0x140216620
0062D04B  40 8A F0                        mov sil, al
0062D04E  84 C0                           test al, al
0062D050  74 38                           je 0x14062d08a
0062D052  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0062D056  48 8B 1F                        mov rbx, qword ptr [rdi]
0062D059  EB 19                           jmp 0x14062d074
0062D05B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D05F  48 85 C0                        test rax, rax
0062D062  74 0D                           je 0x14062d071
0062D064  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D068  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062D06C  E8 5F DA 08 00                  call 0x1406baad0
0062D071  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D074  48 3B DF                        cmp rbx, rdi
0062D077  75 E2                           jne 0x14062d05b
0062D079  40 84 F6                        test sil, sil
0062D07C  74 0C                           je 0x14062d08a
0062D07E  48 8D 0D FB 6D 8D 00            lea rcx, [rip + 0x8d6dfb]
0062D085  E8 F6 CD D1 FF                  call 0x140349e80
0062D08A  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062D08E  45 8B CF                        mov r9d, r15d
0062D091  45 8B C4                        mov r8d, r12d
0062D094  41 8B D5                        mov edx, r13d
0062D097  E8 E4 A5 0E 00                  call 0x140717680
0062D09C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0062D09F  4D 85 F6                        test r14, r14
0062D0A2  74 63                           je 0x14062d107
0062D0A4  40 32 FF                        xor dil, dil
0062D0A7  40 38 3D 0A 78 8D 00            cmp byte ptr [rip + 0x8d780a], dil
0062D0AE  75 0C                           jne 0x14062d0bc
0062D0B0  F7 05 C6 78 8D 00 00 08 00 00   test dword ptr [rip + 0x8d78c6], 0x800
0062D0BA  74 13                           je 0x14062d0cf
0062D0BC  48 8D 0D BD 6D 8D 00            lea rcx, [rip + 0x8d6dbd]
0062D0C3  E8 58 95 BE FF                  call 0x140216620
0062D0C8  40 8A F8                        mov dil, al
0062D0CB  84 C0                           test al, al
0062D0CD  74 38                           je 0x14062d107
0062D0CF  49 8D 76 30                     lea rsi, [r14 + 0x30]
0062D0D3  48 8B 1E                        mov rbx, qword ptr [rsi]
0062D0D6  EB 19                           jmp 0x14062d0f1
0062D0D8  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D0DC  48 85 C0                        test rax, rax
0062D0DF  74 0D                           je 0x14062d0ee
0062D0E1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D0E5  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062D0E9  E8 E2 D9 08 00                  call 0x1406baad0
0062D0EE  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D0F1  48 3B DE                        cmp rbx, rsi
0062D0F4  75 E2                           jne 0x14062d0d8
0062D0F6  40 84 FF                        test dil, dil
0062D0F9  74 0C                           je 0x14062d107
0062D0FB  48 8D 0D 7E 6D 8D 00            lea rcx, [rip + 0x8d6d7e]
0062D102  E8 79 CD D1 FF                  call 0x140349e80
0062D107  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0062D10A  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062D10F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062D113  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062D117  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0062D11B  49 8B E3                        mov rsp, r11
0062D11E  41 5F                           pop r15
0062D120  41 5E                           pop r14
0062D122  41 5D                           pop r13
0062D124  41 5C                           pop r12
0062D126  5D                              pop rbp
0062D127  C3                              ret
0062D128  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoSetPartitionInformationWrapper(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(311, a2, a3, a4);
    if (result == 0) goto loc_0062D08A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062D005;
    v_stack_m58 = v_stack_p0;
    goto loc_0062D013;
loc_0062D005:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m4C = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9271447)) != 0) goto loc_0062D03F;
    if (((*(unsigned int *)(v_rip + 9271619)) & (0x800ULL)) == 0) goto loc_0062D052;
loc_0062D03F:
    result = ExAcquireRundownProtection(v_rip + 9268794, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D08A;
loc_0062D052:
    goto loc_0062D074;
loc_0062D05B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062D074:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062D05B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9268731;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoSetPartitionInformation(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0062D107;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9271306)) != 0) goto loc_0062D0BC;
    if (((*(unsigned int *)(v_rip + 9271494)) & (0x800ULL)) == 0) goto loc_0062D0CF;
loc_0062D0BC:
    result = ExAcquireRundownProtection(v_rip + 9268669, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0062D107;
loc_0062D0CF:
    goto loc_0062D0F1;
loc_0062D0D8:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0062D0F1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0062D0D8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9268606;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoSetPartitionInformationWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(311, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062D08A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062D005;
    v_stack_m58 = v_stack_p0;
    goto loc_0062D013;
loc_0062D005:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m4C = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8D7897)) != 0) goto loc_0062D03F;
    if (((*(uint32_t *)(v_rip + 0x8D7943)) & (0x800ULL)) == 0) goto loc_0062D052;
loc_0062D03F:
    result = ExAcquireRundownProtection(v_rip + 9268794, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062D08A;
loc_0062D052:
    goto loc_0062D074;
loc_0062D05B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062D074:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062D05B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9268731;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = IoSetPartitionInformation(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0062D107;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D780A)) != 0) goto loc_0062D0BC;
    if (((*(uint32_t *)(v_rip + 0x8D78C6)) & (0x800ULL)) == 0) goto loc_0062D0CF;
loc_0062D0BC:
    result = ExAcquireRundownProtection(v_rip + 9268669, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0062D107;
loc_0062D0CF:
    goto loc_0062D0F1;
loc_0062D0D8:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0062D0F1:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0062D0D8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9268606;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062CFA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062CFA0[BB_0062CFA0]
  bb_0062CFF3[BB_0062CFF3]
  bb_0062CFFB[BB_0062CFFB]
  bb_0062D005[BB_0062D005]
  bb_0062D00A[BB_0062D00A]
  bb_0062D013[BB_0062D013]
  bb_0062D033[BB_0062D033]
  bb_0062D03F[BB_0062D03F]
  bb_0062D052[BB_0062D052]
  bb_0062D05B[BB_0062D05B]
  bb_0062D064[BB_0062D064]
  bb_0062D071[BB_0062D071]
  bb_0062D074[BB_0062D074]
  bb_0062D079[BB_0062D079]
  bb_0062D07E[BB_0062D07E]
  bb_0062D08A[BB_0062D08A]
  bb_0062D0A4[BB_0062D0A4]
  bb_0062D0B0[BB_0062D0B0]
  bb_0062D0BC[BB_0062D0BC]
  bb_0062D0CF[BB_0062D0CF]
  bb_0062D0D8[BB_0062D0D8]
  bb_0062D0E1[BB_0062D0E1]
  bb_0062D0EE[BB_0062D0EE]
  bb_0062D0F1[BB_0062D0F1]
  bb_0062D0F6[BB_0062D0F6]
  bb_0062D0FB[BB_0062D0FB]
  bb_0062D107[BB_0062D107]
  bb_0062D128[BB_0062D128]
  bb_0062CFA0 -->|branch| bb_0062D08A
  bb_0062CFA0 -->|fallthrough| bb_0062CFF3
  bb_0062CFF3 -->|branch| bb_0062D005
  bb_0062CFF3 -->|fallthrough| bb_0062CFFB
  bb_0062CFFB -->|branch| bb_0062D013
  bb_0062D005 -->|branch| bb_0062D013
  bb_0062D005 -->|fallthrough| bb_0062D00A
  bb_0062D00A -->|flow| bb_0062D013
  bb_0062D013 -->|branch| bb_0062D03F
  bb_0062D013 -->|fallthrough| bb_0062D033
  bb_0062D033 -->|branch| bb_0062D052
  bb_0062D033 -->|fallthrough| bb_0062D03F
  bb_0062D03F -->|branch| bb_0062D08A
  bb_0062D03F -->|fallthrough| bb_0062D052
  bb_0062D052 -->|branch| bb_0062D074
  bb_0062D05B -->|branch| bb_0062D071
  bb_0062D05B -->|fallthrough| bb_0062D064
  bb_0062D064 -->|flow| bb_0062D071
  bb_0062D071 -->|flow| bb_0062D074
  bb_0062D074 -->|branch| bb_0062D05B
  bb_0062D074 -->|fallthrough| bb_0062D079
  bb_0062D079 -->|branch| bb_0062D08A
  bb_0062D079 -->|fallthrough| bb_0062D07E
  bb_0062D07E -->|flow| bb_0062D08A
  bb_0062D08A -->|branch| bb_0062D107
  bb_0062D08A -->|fallthrough| bb_0062D0A4
  bb_0062D0A4 -->|branch| bb_0062D0BC
  bb_0062D0A4 -->|fallthrough| bb_0062D0B0
  bb_0062D0B0 -->|branch| bb_0062D0CF
  bb_0062D0B0 -->|fallthrough| bb_0062D0BC
  bb_0062D0BC -->|branch| bb_0062D107
  bb_0062D0BC -->|fallthrough| bb_0062D0CF
  bb_0062D0CF -->|branch| bb_0062D0F1
  bb_0062D0D8 -->|branch| bb_0062D0EE
  bb_0062D0D8 -->|fallthrough| bb_0062D0E1
  bb_0062D0E1 -->|flow| bb_0062D0EE
  bb_0062D0EE -->|flow| bb_0062D0F1
  bb_0062D0F1 -->|branch| bb_0062D0D8
  bb_0062D0F1 -->|fallthrough| bb_0062D0F6
  bb_0062D0F6 -->|branch| bb_0062D107
  bb_0062D0F6 -->|fallthrough| bb_0062D0FB
  bb_0062D0FB -->|flow| bb_0062D107
```
