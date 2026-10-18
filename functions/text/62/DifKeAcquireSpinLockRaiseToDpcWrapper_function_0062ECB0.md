# DifKeAcquireSpinLockRaiseToDpcWrapper

- RVA: `0x0062ECB0`–`0x0062EE0F` (길이 `351` bytes)
- VA: `0x000000014062ECB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062ECDF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062ED07` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062ED35` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062ED5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062ED75` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062ED7D` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0062EDAA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062EDD1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062EDEA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062ED19` → RVA `0x00F048B8` (`.data`; read)
- `0x0062ED22` → RVA `0x00F04980` (`.data`; read)
- `0x0062ED2E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062ECB0  4C 8B DC                        mov r11, rsp
0062ECB3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062ECB7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062ECBB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062ECBF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062ECC3  41 56                           push r14
0062ECC5  48 83 EC 40                     sub rsp, 0x40
0062ECC9  33 C0                           xor eax, eax
0062ECCB  0F 57 C0                        xorps xmm0, xmm0
0062ECCE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062ECD3  48 8B E9                        mov rbp, rcx
0062ECD6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062ECDA  B9 23 01 00 00                  mov ecx, 0x123
0062ECDF  E8 50 6D E6 FF                  call 0x140495a34
0062ECE4  48 8B F0                        mov rsi, rax
0062ECE7  48 85 C0                        test rax, rax
0062ECEA  0F 84 8A 00 00 00               je 0x14062ed7a
0062ECF0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062ECF3  A8 18                           test al, 0x18
0062ECF5  74 0C                           je 0x14062ed03
0062ECF7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062ECFC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062ED01  EB 0E                           jmp 0x14062ed11
0062ED03  A8 04                           test al, 4
0062ED05  74 0A                           je 0x14062ed11
0062ED07  E8 FC 4E EA FF                  call 0x1404d3c08
0062ED0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062ED11  40 32 FF                        xor dil, dil
0062ED14  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062ED19  40 38 3D 98 5B 8D 00            cmp byte ptr [rip + 0x8d5b98], dil
0062ED20  75 0C                           jne 0x14062ed2e
0062ED22  F7 05 54 5C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5c54], 0x800
0062ED2C  74 13                           je 0x14062ed41
0062ED2E  48 8D 0D 4B 51 8D 00            lea rcx, [rip + 0x8d514b]
0062ED35  E8 E6 78 BE FF                  call 0x140216620
0062ED3A  40 8A F8                        mov dil, al
0062ED3D  84 C0                           test al, al
0062ED3F  74 39                           je 0x14062ed7a
0062ED41  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062ED45  49 8B 1E                        mov rbx, qword ptr [r14]
0062ED48  EB 1A                           jmp 0x14062ed64
0062ED4A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062ED4E  48 85 C0                        test rax, rax
0062ED51  74 0E                           je 0x14062ed61
0062ED53  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062ED57  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062ED5C  E8 6F BD 08 00                  call 0x1406baad0
0062ED61  48 8B 1B                        mov rbx, qword ptr [rbx]
0062ED64  49 3B DE                        cmp rbx, r14
0062ED67  75 E1                           jne 0x14062ed4a
0062ED69  40 84 FF                        test dil, dil
0062ED6C  74 0C                           je 0x14062ed7a
0062ED6E  48 8D 0D 0B 51 8D 00            lea rcx, [rip + 0x8d510b]
0062ED75  E8 06 B1 D1 FF                  call 0x140349e80
0062ED7A  48 8B CD                        mov rcx, rbp
0062ED7D  E8 EE 96 BD FF                  call 0x140208470
0062ED82  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0062ED86  48 85 F6                        test rsi, rsi
0062ED89  74 64                           je 0x14062edef
0062ED8B  40 32 FF                        xor dil, dil
0062ED8E  40 38 3D 23 5B 8D 00            cmp byte ptr [rip + 0x8d5b23], dil
0062ED95  75 0C                           jne 0x14062eda3
0062ED97  F7 05 DF 5B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d5bdf], 0x800
0062EDA1  74 13                           je 0x14062edb6
0062EDA3  48 8D 0D D6 50 8D 00            lea rcx, [rip + 0x8d50d6]
0062EDAA  E8 71 78 BE FF                  call 0x140216620
0062EDAF  40 8A F8                        mov dil, al
0062EDB2  84 C0                           test al, al
0062EDB4  74 39                           je 0x14062edef
0062EDB6  48 83 C6 30                     add rsi, 0x30
0062EDBA  48 8B 1E                        mov rbx, qword ptr [rsi]
0062EDBD  EB 1A                           jmp 0x14062edd9
0062EDBF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062EDC3  48 85 C0                        test rax, rax
0062EDC6  74 0E                           je 0x14062edd6
0062EDC8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062EDCC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062EDD1  E8 FA BC 08 00                  call 0x1406baad0
0062EDD6  48 8B 1B                        mov rbx, qword ptr [rbx]
0062EDD9  48 3B DE                        cmp rbx, rsi
0062EDDC  75 E1                           jne 0x14062edbf
0062EDDE  40 84 FF                        test dil, dil
0062EDE1  74 0C                           je 0x14062edef
0062EDE3  48 8D 0D 96 50 8D 00            lea rcx, [rip + 0x8d5096]
0062EDEA  E8 91 B0 D1 FF                  call 0x140349e80
0062EDEF  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
0062EDF3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062EDF8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062EDFD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062EE02  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062EE07  48 83 C4 40                     add rsp, 0x40
0062EE0B  41 5E                           pop r14
0062EE0D  C3                              ret
0062EE0E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeAcquireSpinLockRaiseToDpcWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(291, a2, a3, a4);
    if (result == 0) goto loc_0062ED7A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062ED03;
    v_stack_m28 = v_stack_p0;
    goto loc_0062ED11;
loc_0062ED03:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9264024)) != 0) goto loc_0062ED2E;
    if (((*(unsigned int *)(v_rip + 9264212)) & (0x800ULL)) == 0) goto loc_0062ED41;
loc_0062ED2E:
    result = ExAcquireRundownProtection(v_rip + 9261387, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062ED7A;
loc_0062ED41:
    goto loc_0062ED64;
loc_0062ED4A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062ED64:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062ED4A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9261323;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeAcquireSpinLockRaiseToDpc(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062EDEF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9263907)) != 0) goto loc_0062EDA3;
    if (((*(unsigned int *)(v_rip + 9264095)) & (0x800ULL)) == 0) goto loc_0062EDB6;
loc_0062EDA3:
    result = ExAcquireRundownProtection(v_rip + 9261270, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062EDEF;
loc_0062EDB6:
    v_rsi = (result) + (48);
    goto loc_0062EDD9;
loc_0062EDBF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062EDD9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062EDBF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9261206;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeAcquireSpinLockRaiseToDpcWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(291, a2, a3, a4);
    if (result == 0) goto loc_0062ED7A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062ED03;
    v_stack_m28 = v_stack_p0;
    goto loc_0062ED11;
loc_0062ED03:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D5B98)) != 0) goto loc_0062ED2E;
    if (((*(uint32_t *)(v_rip + 0x8D5C54)) & (0x800ULL)) == 0) goto loc_0062ED41;
loc_0062ED2E:
    result = ExAcquireRundownProtection(v_rip + 9261387, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062ED7A;
loc_0062ED41:
    goto loc_0062ED64;
loc_0062ED4A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062ED64:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062ED4A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9261323;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeAcquireSpinLockRaiseToDpc(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062EDEF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D5B23)) != 0) goto loc_0062EDA3;
    if (((*(uint32_t *)(v_rip + 0x8D5BDF)) & (0x800ULL)) == 0) goto loc_0062EDB6;
loc_0062EDA3:
    result = ExAcquireRundownProtection(v_rip + 9261270, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062EDEF;
loc_0062EDB6:
    local_rsi = (result) + (48);
    goto loc_0062EDD9;
loc_0062EDBF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062EDD9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062EDBF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9261206;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062ECB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062ECB0[BB_0062ECB0]
  bb_0062ECF0[BB_0062ECF0]
  bb_0062ECF7[BB_0062ECF7]
  bb_0062ED03[BB_0062ED03]
  bb_0062ED07[BB_0062ED07]
  bb_0062ED11[BB_0062ED11]
  bb_0062ED22[BB_0062ED22]
  bb_0062ED2E[BB_0062ED2E]
  bb_0062ED41[BB_0062ED41]
  bb_0062ED4A[BB_0062ED4A]
  bb_0062ED53[BB_0062ED53]
  bb_0062ED61[BB_0062ED61]
  bb_0062ED64[BB_0062ED64]
  bb_0062ED69[BB_0062ED69]
  bb_0062ED6E[BB_0062ED6E]
  bb_0062ED7A[BB_0062ED7A]
  bb_0062ED8B[BB_0062ED8B]
  bb_0062ED97[BB_0062ED97]
  bb_0062EDA3[BB_0062EDA3]
  bb_0062EDB6[BB_0062EDB6]
  bb_0062EDBF[BB_0062EDBF]
  bb_0062EDC8[BB_0062EDC8]
  bb_0062EDD6[BB_0062EDD6]
  bb_0062EDD9[BB_0062EDD9]
  bb_0062EDDE[BB_0062EDDE]
  bb_0062EDE3[BB_0062EDE3]
  bb_0062EDEF[BB_0062EDEF]
  bb_0062EE0E[BB_0062EE0E]
  bb_0062ECB0 -->|branch| bb_0062ED7A
  bb_0062ECB0 -->|fallthrough| bb_0062ECF0
  bb_0062ECF0 -->|branch| bb_0062ED03
  bb_0062ECF0 -->|fallthrough| bb_0062ECF7
  bb_0062ECF7 -->|branch| bb_0062ED11
  bb_0062ED03 -->|branch| bb_0062ED11
  bb_0062ED03 -->|fallthrough| bb_0062ED07
  bb_0062ED07 -->|flow| bb_0062ED11
  bb_0062ED11 -->|branch| bb_0062ED2E
  bb_0062ED11 -->|fallthrough| bb_0062ED22
  bb_0062ED22 -->|branch| bb_0062ED41
  bb_0062ED22 -->|fallthrough| bb_0062ED2E
  bb_0062ED2E -->|branch| bb_0062ED7A
  bb_0062ED2E -->|fallthrough| bb_0062ED41
  bb_0062ED41 -->|branch| bb_0062ED64
  bb_0062ED4A -->|branch| bb_0062ED61
  bb_0062ED4A -->|fallthrough| bb_0062ED53
  bb_0062ED53 -->|flow| bb_0062ED61
  bb_0062ED61 -->|flow| bb_0062ED64
  bb_0062ED64 -->|branch| bb_0062ED4A
  bb_0062ED64 -->|fallthrough| bb_0062ED69
  bb_0062ED69 -->|branch| bb_0062ED7A
  bb_0062ED69 -->|fallthrough| bb_0062ED6E
  bb_0062ED6E -->|flow| bb_0062ED7A
  bb_0062ED7A -->|branch| bb_0062EDEF
  bb_0062ED7A -->|fallthrough| bb_0062ED8B
  bb_0062ED8B -->|branch| bb_0062EDA3
  bb_0062ED8B -->|fallthrough| bb_0062ED97
  bb_0062ED97 -->|branch| bb_0062EDB6
  bb_0062ED97 -->|fallthrough| bb_0062EDA3
  bb_0062EDA3 -->|branch| bb_0062EDEF
  bb_0062EDA3 -->|fallthrough| bb_0062EDB6
  bb_0062EDB6 -->|branch| bb_0062EDD9
  bb_0062EDBF -->|branch| bb_0062EDD6
  bb_0062EDBF -->|fallthrough| bb_0062EDC8
  bb_0062EDC8 -->|flow| bb_0062EDD6
  bb_0062EDD6 -->|flow| bb_0062EDD9
  bb_0062EDD9 -->|branch| bb_0062EDBF
  bb_0062EDD9 -->|fallthrough| bb_0062EDDE
  bb_0062EDDE -->|branch| bb_0062EDEF
  bb_0062EDDE -->|fallthrough| bb_0062EDE3
  bb_0062EDE3 -->|flow| bb_0062EDEF
```
