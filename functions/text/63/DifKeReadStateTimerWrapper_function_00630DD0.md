# DifKeReadStateTimerWrapper

- RVA: `0x00630DD0`–`0x00630F2A` (길이 `346` bytes)
- VA: `0x0000000140630DD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `93`개 명령, `346/346` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00630DFF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00630E27` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00630E55` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630E7C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630E95` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00630EC5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630EEC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630F05` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00630E39` → RVA `0x00F048B8` (`.data`; read)
- `0x00630E42` → RVA `0x00F04980` (`.data`; read)
- `0x00630E4E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00630DD0  4C 8B DC                        mov r11, rsp
00630DD3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00630DD7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00630DDB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00630DDF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00630DE3  41 56                           push r14
00630DE5  48 83 EC 40                     sub rsp, 0x40
00630DE9  33 C0                           xor eax, eax
00630DEB  0F 57 C0                        xorps xmm0, xmm0
00630DEE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00630DF3  48 8B E9                        mov rbp, rcx
00630DF6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00630DFA  B9 0C 01 00 00                  mov ecx, 0x10c
00630DFF  E8 30 4C E6 FF                  call 0x140495a34
00630E04  48 8B F0                        mov rsi, rax
00630E07  48 85 C0                        test rax, rax
00630E0A  0F 84 8A 00 00 00               je 0x140630e9a
00630E10  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00630E13  A8 18                           test al, 0x18
00630E15  74 0C                           je 0x140630e23
00630E17  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00630E1C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00630E21  EB 0E                           jmp 0x140630e31
00630E23  A8 04                           test al, 4
00630E25  74 0A                           je 0x140630e31
00630E27  E8 DC 2D EA FF                  call 0x1404d3c08
00630E2C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00630E31  40 32 FF                        xor dil, dil
00630E34  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00630E39  40 38 3D 78 3A 8D 00            cmp byte ptr [rip + 0x8d3a78], dil
00630E40  75 0C                           jne 0x140630e4e
00630E42  F7 05 34 3B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d3b34], 0x800
00630E4C  74 13                           je 0x140630e61
00630E4E  48 8D 0D 2B 30 8D 00            lea rcx, [rip + 0x8d302b]
00630E55  E8 C6 57 BE FF                  call 0x140216620
00630E5A  40 8A F8                        mov dil, al
00630E5D  84 C0                           test al, al
00630E5F  74 39                           je 0x140630e9a
00630E61  4C 8D 76 20                     lea r14, [rsi + 0x20]
00630E65  49 8B 1E                        mov rbx, qword ptr [r14]
00630E68  EB 1A                           jmp 0x140630e84
00630E6A  48 8D 43 F0                     lea rax, [rbx - 0x10]
00630E6E  48 85 C0                        test rax, rax
00630E71  74 0E                           je 0x140630e81
00630E73  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630E77  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00630E7C  E8 4F 9C 08 00                  call 0x1406baad0
00630E81  48 8B 1B                        mov rbx, qword ptr [rbx]
00630E84  49 3B DE                        cmp rbx, r14
00630E87  75 E1                           jne 0x140630e6a
00630E89  40 84 FF                        test dil, dil
00630E8C  74 0C                           je 0x140630e9a
00630E8E  48 8D 0D EB 2F 8D 00            lea rcx, [rip + 0x8d2feb]
00630E95  E8 E6 8F D1 FF                  call 0x140349e80
00630E9A  8A 45 04                        mov al, byte ptr [rbp + 4]
00630E9D  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00630EA1  48 85 F6                        test rsi, rsi
00630EA4  74 64                           je 0x140630f0a
00630EA6  40 32 FF                        xor dil, dil
00630EA9  40 38 3D 08 3A 8D 00            cmp byte ptr [rip + 0x8d3a08], dil
00630EB0  75 0C                           jne 0x140630ebe
00630EB2  F7 05 C4 3A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d3ac4], 0x800
00630EBC  74 13                           je 0x140630ed1
00630EBE  48 8D 0D BB 2F 8D 00            lea rcx, [rip + 0x8d2fbb]
00630EC5  E8 56 57 BE FF                  call 0x140216620
00630ECA  40 8A F8                        mov dil, al
00630ECD  84 C0                           test al, al
00630ECF  74 39                           je 0x140630f0a
00630ED1  48 83 C6 30                     add rsi, 0x30
00630ED5  48 8B 1E                        mov rbx, qword ptr [rsi]
00630ED8  EB 1A                           jmp 0x140630ef4
00630EDA  48 8D 43 F0                     lea rax, [rbx - 0x10]
00630EDE  48 85 C0                        test rax, rax
00630EE1  74 0E                           je 0x140630ef1
00630EE3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630EE7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00630EEC  E8 DF 9B 08 00                  call 0x1406baad0
00630EF1  48 8B 1B                        mov rbx, qword ptr [rbx]
00630EF4  48 3B DE                        cmp rbx, rsi
00630EF7  75 E1                           jne 0x140630eda
00630EF9  40 84 FF                        test dil, dil
00630EFC  74 0C                           je 0x140630f0a
00630EFE  48 8D 0D 7B 2F 8D 00            lea rcx, [rip + 0x8d2f7b]
00630F05  E8 76 8F D1 FF                  call 0x140349e80
00630F0A  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00630F0E  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00630F13  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00630F18  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00630F1D  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00630F22  48 83 C4 40                     add rsp, 0x40
00630F26  41 5E                           pop r14
00630F28  C3                              ret
00630F29  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReadStateTimerWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(268, a2, a3, a4);
    if (result == 0) goto loc_00630E9A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00630E23;
    v_stack_m28 = v_stack_p0;
    goto loc_00630E31;
loc_00630E23:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9255544)) != 0) goto loc_00630E4E;
    if (((*(unsigned int *)(v_rip + 9255732)) & (0x800ULL)) == 0) goto loc_00630E61;
loc_00630E4E:
    result = ExAcquireRundownProtection(v_rip + 9252907, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630E9A;
loc_00630E61:
    goto loc_00630E84;
loc_00630E6A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00630E84:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00630E6A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9252843;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m18 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 4));
    if (result == 0) goto loc_00630F0A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9255432)) != 0) goto loc_00630EBE;
    if (((*(unsigned int *)(v_rip + 9255620)) & (0x800ULL)) == 0) goto loc_00630ED1;
loc_00630EBE:
    result = ExAcquireRundownProtection(v_rip + 9252795, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630F0A;
loc_00630ED1:
    v_rsi = (result) + (48);
    goto loc_00630EF4;
loc_00630EDA:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00630EF4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00630EDA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9252731;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReadStateTimerWrapper(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    result = DifGetAPIThunkContextById(268, a2, a3, a4);
    if (result == 0) goto loc_00630E9A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00630E23;
    v_stack_m28 = v_stack_p0;
    goto loc_00630E31;
loc_00630E23:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D3A78)) != 0) goto loc_00630E4E;
    if (((*(uint32_t *)(v_rip + 0x8D3B34)) & (0x800ULL)) == 0) goto loc_00630E61;
loc_00630E4E:
    result = ExAcquireRundownProtection(v_rip + 9252907, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630E9A;
loc_00630E61:
    goto loc_00630E84;
loc_00630E6A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00630E84:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00630E6A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9252843;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    v_stack_m18 = (uint8_t)(*(uint8_t *)(arg1 + 0x4));
    if (result == 0) goto loc_00630F0A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D3A08)) != 0) goto loc_00630EBE;
    if (((*(uint32_t *)(v_rip + 0x8D3AC4)) & (0x800ULL)) == 0) goto loc_00630ED1;
loc_00630EBE:
    result = ExAcquireRundownProtection(v_rip + 9252795, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630F0A;
loc_00630ED1:
    local_rsi = (result) + (48);
    goto loc_00630EF4;
loc_00630EDA:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00630EF4:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00630EDA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9252731;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00630DD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00630DD0[BB_00630DD0]
  bb_00630E10[BB_00630E10]
  bb_00630E17[BB_00630E17]
  bb_00630E23[BB_00630E23]
  bb_00630E27[BB_00630E27]
  bb_00630E31[BB_00630E31]
  bb_00630E42[BB_00630E42]
  bb_00630E4E[BB_00630E4E]
  bb_00630E61[BB_00630E61]
  bb_00630E6A[BB_00630E6A]
  bb_00630E73[BB_00630E73]
  bb_00630E81[BB_00630E81]
  bb_00630E84[BB_00630E84]
  bb_00630E89[BB_00630E89]
  bb_00630E8E[BB_00630E8E]
  bb_00630E9A[BB_00630E9A]
  bb_00630EA6[BB_00630EA6]
  bb_00630EB2[BB_00630EB2]
  bb_00630EBE[BB_00630EBE]
  bb_00630ED1[BB_00630ED1]
  bb_00630EDA[BB_00630EDA]
  bb_00630EE3[BB_00630EE3]
  bb_00630EF1[BB_00630EF1]
  bb_00630EF4[BB_00630EF4]
  bb_00630EF9[BB_00630EF9]
  bb_00630EFE[BB_00630EFE]
  bb_00630F0A[BB_00630F0A]
  bb_00630F29[BB_00630F29]
  bb_00630DD0 -->|branch| bb_00630E9A
  bb_00630DD0 -->|fallthrough| bb_00630E10
  bb_00630E10 -->|branch| bb_00630E23
  bb_00630E10 -->|fallthrough| bb_00630E17
  bb_00630E17 -->|branch| bb_00630E31
  bb_00630E23 -->|branch| bb_00630E31
  bb_00630E23 -->|fallthrough| bb_00630E27
  bb_00630E27 -->|flow| bb_00630E31
  bb_00630E31 -->|branch| bb_00630E4E
  bb_00630E31 -->|fallthrough| bb_00630E42
  bb_00630E42 -->|branch| bb_00630E61
  bb_00630E42 -->|fallthrough| bb_00630E4E
  bb_00630E4E -->|branch| bb_00630E9A
  bb_00630E4E -->|fallthrough| bb_00630E61
  bb_00630E61 -->|branch| bb_00630E84
  bb_00630E6A -->|branch| bb_00630E81
  bb_00630E6A -->|fallthrough| bb_00630E73
  bb_00630E73 -->|flow| bb_00630E81
  bb_00630E81 -->|flow| bb_00630E84
  bb_00630E84 -->|branch| bb_00630E6A
  bb_00630E84 -->|fallthrough| bb_00630E89
  bb_00630E89 -->|branch| bb_00630E9A
  bb_00630E89 -->|fallthrough| bb_00630E8E
  bb_00630E8E -->|flow| bb_00630E9A
  bb_00630E9A -->|branch| bb_00630F0A
  bb_00630E9A -->|fallthrough| bb_00630EA6
  bb_00630EA6 -->|branch| bb_00630EBE
  bb_00630EA6 -->|fallthrough| bb_00630EB2
  bb_00630EB2 -->|branch| bb_00630ED1
  bb_00630EB2 -->|fallthrough| bb_00630EBE
  bb_00630EBE -->|branch| bb_00630F0A
  bb_00630EBE -->|fallthrough| bb_00630ED1
  bb_00630ED1 -->|branch| bb_00630EF4
  bb_00630EDA -->|branch| bb_00630EF1
  bb_00630EDA -->|fallthrough| bb_00630EE3
  bb_00630EE3 -->|flow| bb_00630EF1
  bb_00630EF1 -->|flow| bb_00630EF4
  bb_00630EF4 -->|branch| bb_00630EDA
  bb_00630EF4 -->|fallthrough| bb_00630EF9
  bb_00630EF9 -->|branch| bb_00630F0A
  bb_00630EF9 -->|fallthrough| bb_00630EFE
  bb_00630EFE -->|flow| bb_00630F0A
```
