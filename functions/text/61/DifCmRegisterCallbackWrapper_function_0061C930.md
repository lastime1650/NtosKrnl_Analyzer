# DifCmRegisterCallbackWrapper

- RVA: `0x0061C930`–`0x0061CAA7` (길이 `375` bytes)
- VA: `0x000000014061C930`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061C96E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061C994` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061C9C8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C9EE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061CA07` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061CA15` → [CmRegisterCallback](../../page/7E/CmRegisterCallback_function_007E14E0.md) (function, `0x007E14E0`)
- `0x0061CA41` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061CA67` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061CA80` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061C9A4` → RVA `0x00F048B8` (`.data`; read)
- `0x0061C9B5` → RVA `0x00F04980` (`.data`; read)
- `0x0061C9C1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0061CA15` → [CmRegisterCallback](../../page/7E/CmRegisterCallback_function_007E14E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061C930  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0061C935  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0061C93A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0061C93F  55                              push rbp
0061C940  41 54                           push r12
0061C942  41 55                           push r13
0061C944  41 56                           push r14
0061C946  41 57                           push r15
0061C948  48 8B EC                        mov rbp, rsp
0061C94B  48 83 EC 50                     sub rsp, 0x50
0061C94F  0F 57 C0                        xorps xmm0, xmm0
0061C952  33 C0                           xor eax, eax
0061C954  4C 8B E9                        mov r13, rcx
0061C957  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061C95B  B9 AE 01 00 00                  mov ecx, 0x1ae
0061C960  4D 8B F8                        mov r15, r8
0061C963  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061C967  4C 8B E2                        mov r12, rdx
0061C96A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061C96E  E8 C1 90 E7 FF                  call 0x140495a34
0061C973  48 8B F0                        mov rsi, rax
0061C976  48 85 C0                        test rax, rax
0061C979  0F 84 8D 00 00 00               je 0x14061ca0c
0061C97F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061C982  A8 18                           test al, 0x18
0061C984  74 0A                           je 0x14061c990
0061C986  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061C98A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0061C98E  EB 0D                           jmp 0x14061c99d
0061C990  A8 04                           test al, 4
0061C992  74 09                           je 0x14061c99d
0061C994  E8 6F 72 EB FF                  call 0x1404d3c08
0061C999  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061C99D  45 32 F6                        xor r14b, r14b
0061C9A0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061C9A4  44 38 35 0D 7F 8E 00            cmp byte ptr [rip + 0x8e7f0d], r14b
0061C9AB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0061C9AF  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0061C9B3  75 0C                           jne 0x14061c9c1
0061C9B5  F7 05 C1 7F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7fc1], 0x800
0061C9BF  74 13                           je 0x14061c9d4
0061C9C1  48 8D 0D B8 74 8E 00            lea rcx, [rip + 0x8e74b8]
0061C9C8  E8 53 9C BF FF                  call 0x140216620
0061C9CD  44 8A F0                        mov r14b, al
0061C9D0  84 C0                           test al, al
0061C9D2  74 38                           je 0x14061ca0c
0061C9D4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061C9D8  48 8B 1F                        mov rbx, qword ptr [rdi]
0061C9DB  EB 19                           jmp 0x14061c9f6
0061C9DD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C9E1  48 85 C0                        test rax, rax
0061C9E4  74 0D                           je 0x14061c9f3
0061C9E6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C9EA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061C9EE  E8 DD E0 09 00                  call 0x1406baad0
0061C9F3  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C9F6  48 3B DF                        cmp rbx, rdi
0061C9F9  75 E2                           jne 0x14061c9dd
0061C9FB  45 84 F6                        test r14b, r14b
0061C9FE  74 0C                           je 0x14061ca0c
0061CA00  48 8D 0D 79 74 8E 00            lea rcx, [rip + 0x8e7479]
0061CA07  E8 74 D4 D2 FF                  call 0x140349e80
0061CA0C  4D 8B C7                        mov r8, r15
0061CA0F  49 8B D4                        mov rdx, r12
0061CA12  49 8B CD                        mov rcx, r13
0061CA15  E8 C6 4A 1C 00                  call 0x1407e14e0
0061CA1A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0061CA1D  48 85 F6                        test rsi, rsi
0061CA20  74 63                           je 0x14061ca85
0061CA22  40 32 FF                        xor dil, dil
0061CA25  40 38 3D 8C 7E 8E 00            cmp byte ptr [rip + 0x8e7e8c], dil
0061CA2C  75 0C                           jne 0x14061ca3a
0061CA2E  F7 05 48 7F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7f48], 0x800
0061CA38  74 13                           je 0x14061ca4d
0061CA3A  48 8D 0D 3F 74 8E 00            lea rcx, [rip + 0x8e743f]
0061CA41  E8 DA 9B BF FF                  call 0x140216620
0061CA46  40 8A F8                        mov dil, al
0061CA49  84 C0                           test al, al
0061CA4B  74 38                           je 0x14061ca85
0061CA4D  48 83 C6 30                     add rsi, 0x30
0061CA51  48 8B 1E                        mov rbx, qword ptr [rsi]
0061CA54  EB 19                           jmp 0x14061ca6f
0061CA56  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061CA5A  48 85 C0                        test rax, rax
0061CA5D  74 0D                           je 0x14061ca6c
0061CA5F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061CA63  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061CA67  E8 64 E0 09 00                  call 0x1406baad0
0061CA6C  48 8B 1B                        mov rbx, qword ptr [rbx]
0061CA6F  48 3B DE                        cmp rbx, rsi
0061CA72  75 E2                           jne 0x14061ca56
0061CA74  40 84 FF                        test dil, dil
0061CA77  74 0C                           je 0x14061ca85
0061CA79  48 8D 0D 00 74 8E 00            lea rcx, [rip + 0x8e7400]
0061CA80  E8 FB D3 D2 FF                  call 0x140349e80
0061CA85  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0061CA88  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0061CA8D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0061CA91  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0061CA95  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0061CA99  49 8B E3                        mov rsp, r11
0061CA9C  41 5F                           pop r15
0061CA9E  41 5E                           pop r14
0061CAA0  41 5D                           pop r13
0061CAA2  41 5C                           pop r12
0061CAA4  5D                              pop rbp
0061CAA5  C3                              ret
0061CAA6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCmRegisterCallbackWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(430, a2, a3, a4);
    if (result == 0) goto loc_0061CA0C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061C990;
    v_stack_m58 = v_stack_p0;
    goto loc_0061C99D;
loc_0061C990:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9338637)) != 0) goto loc_0061C9C1;
    if (((*(unsigned int *)(v_rip + 9338817)) & (0x800ULL)) == 0) goto loc_0061C9D4;
loc_0061C9C1:
    result = ExAcquireRundownProtection(v_rip + 9335992, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061CA0C;
loc_0061C9D4:
    goto loc_0061C9F6;
loc_0061C9DD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061C9F6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061C9DD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9335929;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = CmRegisterCallback(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0061CA85;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9338508)) != 0) goto loc_0061CA3A;
    if (((*(unsigned int *)(v_rip + 9338696)) & (0x800ULL)) == 0) goto loc_0061CA4D;
loc_0061CA3A:
    result = ExAcquireRundownProtection(v_rip + 9335871, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061CA85;
loc_0061CA4D:
    v_rsi = (result) + (48);
    goto loc_0061CA6F;
loc_0061CA56:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061CA6F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061CA56;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9335808;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifCmRegisterCallbackWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(430, Arg2, Arg3, a4);
    if (result == 0) goto loc_0061CA0C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061C990;
    v_stack_m58 = v_stack_p0;
    goto loc_0061C99D;
loc_0061C990:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8E7F0D)) != 0) goto loc_0061C9C1;
    if (((*(uint32_t *)(v_rip + 0x8E7FC1)) & (0x800ULL)) == 0) goto loc_0061C9D4;
loc_0061C9C1:
    result = ExAcquireRundownProtection(v_rip + 9335992, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061CA0C;
loc_0061C9D4:
    goto loc_0061C9F6;
loc_0061C9DD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061C9F6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061C9DD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9335929;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = CmRegisterCallback(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0061CA85;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E7E8C)) != 0) goto loc_0061CA3A;
    if (((*(uint32_t *)(v_rip + 0x8E7F48)) & (0x800ULL)) == 0) goto loc_0061CA4D;
loc_0061CA3A:
    result = ExAcquireRundownProtection(v_rip + 9335871, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061CA85;
loc_0061CA4D:
    local_rsi = (result) + (48);
    goto loc_0061CA6F;
loc_0061CA56:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061CA6F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061CA56;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9335808;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061C930&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061C930[BB_0061C930]
  bb_0061C97F[BB_0061C97F]
  bb_0061C986[BB_0061C986]
  bb_0061C990[BB_0061C990]
  bb_0061C994[BB_0061C994]
  bb_0061C99D[BB_0061C99D]
  bb_0061C9B5[BB_0061C9B5]
  bb_0061C9C1[BB_0061C9C1]
  bb_0061C9D4[BB_0061C9D4]
  bb_0061C9DD[BB_0061C9DD]
  bb_0061C9E6[BB_0061C9E6]
  bb_0061C9F3[BB_0061C9F3]
  bb_0061C9F6[BB_0061C9F6]
  bb_0061C9FB[BB_0061C9FB]
  bb_0061CA00[BB_0061CA00]
  bb_0061CA0C[BB_0061CA0C]
  bb_0061CA22[BB_0061CA22]
  bb_0061CA2E[BB_0061CA2E]
  bb_0061CA3A[BB_0061CA3A]
  bb_0061CA4D[BB_0061CA4D]
  bb_0061CA56[BB_0061CA56]
  bb_0061CA5F[BB_0061CA5F]
  bb_0061CA6C[BB_0061CA6C]
  bb_0061CA6F[BB_0061CA6F]
  bb_0061CA74[BB_0061CA74]
  bb_0061CA79[BB_0061CA79]
  bb_0061CA85[BB_0061CA85]
  bb_0061CAA6[BB_0061CAA6]
  bb_0061C930 -->|branch| bb_0061CA0C
  bb_0061C930 -->|fallthrough| bb_0061C97F
  bb_0061C97F -->|branch| bb_0061C990
  bb_0061C97F -->|fallthrough| bb_0061C986
  bb_0061C986 -->|branch| bb_0061C99D
  bb_0061C990 -->|branch| bb_0061C99D
  bb_0061C990 -->|fallthrough| bb_0061C994
  bb_0061C994 -->|flow| bb_0061C99D
  bb_0061C99D -->|branch| bb_0061C9C1
  bb_0061C99D -->|fallthrough| bb_0061C9B5
  bb_0061C9B5 -->|branch| bb_0061C9D4
  bb_0061C9B5 -->|fallthrough| bb_0061C9C1
  bb_0061C9C1 -->|branch| bb_0061CA0C
  bb_0061C9C1 -->|fallthrough| bb_0061C9D4
  bb_0061C9D4 -->|branch| bb_0061C9F6
  bb_0061C9DD -->|branch| bb_0061C9F3
  bb_0061C9DD -->|fallthrough| bb_0061C9E6
  bb_0061C9E6 -->|flow| bb_0061C9F3
  bb_0061C9F3 -->|flow| bb_0061C9F6
  bb_0061C9F6 -->|branch| bb_0061C9DD
  bb_0061C9F6 -->|fallthrough| bb_0061C9FB
  bb_0061C9FB -->|branch| bb_0061CA0C
  bb_0061C9FB -->|fallthrough| bb_0061CA00
  bb_0061CA00 -->|flow| bb_0061CA0C
  bb_0061CA0C -->|branch| bb_0061CA85
  bb_0061CA0C -->|fallthrough| bb_0061CA22
  bb_0061CA22 -->|branch| bb_0061CA3A
  bb_0061CA22 -->|fallthrough| bb_0061CA2E
  bb_0061CA2E -->|branch| bb_0061CA4D
  bb_0061CA2E -->|fallthrough| bb_0061CA3A
  bb_0061CA3A -->|branch| bb_0061CA85
  bb_0061CA3A -->|fallthrough| bb_0061CA4D
  bb_0061CA4D -->|branch| bb_0061CA6F
  bb_0061CA56 -->|branch| bb_0061CA6C
  bb_0061CA56 -->|fallthrough| bb_0061CA5F
  bb_0061CA5F -->|flow| bb_0061CA6C
  bb_0061CA6C -->|flow| bb_0061CA6F
  bb_0061CA6F -->|branch| bb_0061CA56
  bb_0061CA6F -->|fallthrough| bb_0061CA74
  bb_0061CA74 -->|branch| bb_0061CA85
  bb_0061CA74 -->|fallthrough| bb_0061CA79
  bb_0061CA79 -->|flow| bb_0061CA85
```
