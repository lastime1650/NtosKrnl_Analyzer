# DifExDeleteResourceLiteWrapper

- RVA: `0x0061FA10`–`0x0061FB6F` (길이 `351` bytes)
- VA: `0x000000014061FA10`
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
- `0x0061FA3F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061FA67` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061FA95` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FABC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FAD5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061FADD` → [ExDeleteResourceLite](../38/ExDeleteResourceLite_function_0038BA60.md) (function, `0x0038BA60`)
- `0x0061FB0A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FB31` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FB4A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061FA79` → RVA `0x00F048B8` (`.data`; read)
- `0x0061FA82` → RVA `0x00F04980` (`.data`; read)
- `0x0061FA8E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061FA10  4C 8B DC                        mov r11, rsp
0061FA13  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061FA17  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061FA1B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061FA1F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0061FA23  41 56                           push r14
0061FA25  48 83 EC 40                     sub rsp, 0x40
0061FA29  33 C0                           xor eax, eax
0061FA2B  0F 57 C0                        xorps xmm0, xmm0
0061FA2E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061FA33  48 8B E9                        mov rbp, rcx
0061FA36  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0061FA3A  B9 97 01 00 00                  mov ecx, 0x197
0061FA3F  E8 F0 5F E7 FF                  call 0x140495a34
0061FA44  48 8B F0                        mov rsi, rax
0061FA47  48 85 C0                        test rax, rax
0061FA4A  0F 84 8A 00 00 00               je 0x14061fada
0061FA50  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061FA53  A8 18                           test al, 0x18
0061FA55  74 0C                           je 0x14061fa63
0061FA57  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0061FA5C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061FA61  EB 0E                           jmp 0x14061fa71
0061FA63  A8 04                           test al, 4
0061FA65  74 0A                           je 0x14061fa71
0061FA67  E8 9C 41 EB FF                  call 0x1404d3c08
0061FA6C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061FA71  40 32 FF                        xor dil, dil
0061FA74  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061FA79  40 38 3D 38 4E 8E 00            cmp byte ptr [rip + 0x8e4e38], dil
0061FA80  75 0C                           jne 0x14061fa8e
0061FA82  F7 05 F4 4E 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4ef4], 0x800
0061FA8C  74 13                           je 0x14061faa1
0061FA8E  48 8D 0D EB 43 8E 00            lea rcx, [rip + 0x8e43eb]
0061FA95  E8 86 6B BF FF                  call 0x140216620
0061FA9A  40 8A F8                        mov dil, al
0061FA9D  84 C0                           test al, al
0061FA9F  74 39                           je 0x14061fada
0061FAA1  4C 8D 76 20                     lea r14, [rsi + 0x20]
0061FAA5  49 8B 1E                        mov rbx, qword ptr [r14]
0061FAA8  EB 1A                           jmp 0x14061fac4
0061FAAA  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FAAE  48 85 C0                        test rax, rax
0061FAB1  74 0E                           je 0x14061fac1
0061FAB3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FAB7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FABC  E8 0F B0 09 00                  call 0x1406baad0
0061FAC1  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FAC4  49 3B DE                        cmp rbx, r14
0061FAC7  75 E1                           jne 0x14061faaa
0061FAC9  40 84 FF                        test dil, dil
0061FACC  74 0C                           je 0x14061fada
0061FACE  48 8D 0D AB 43 8E 00            lea rcx, [rip + 0x8e43ab]
0061FAD5  E8 A6 A3 D2 FF                  call 0x140349e80
0061FADA  48 8B CD                        mov rcx, rbp
0061FADD  E8 7E BF D6 FF                  call 0x14038ba60
0061FAE2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0061FAE6  48 85 F6                        test rsi, rsi
0061FAE9  74 64                           je 0x14061fb4f
0061FAEB  40 32 FF                        xor dil, dil
0061FAEE  40 38 3D C3 4D 8E 00            cmp byte ptr [rip + 0x8e4dc3], dil
0061FAF5  75 0C                           jne 0x14061fb03
0061FAF7  F7 05 7F 4E 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4e7f], 0x800
0061FB01  74 13                           je 0x14061fb16
0061FB03  48 8D 0D 76 43 8E 00            lea rcx, [rip + 0x8e4376]
0061FB0A  E8 11 6B BF FF                  call 0x140216620
0061FB0F  40 8A F8                        mov dil, al
0061FB12  84 C0                           test al, al
0061FB14  74 39                           je 0x14061fb4f
0061FB16  48 83 C6 30                     add rsi, 0x30
0061FB1A  48 8B 1E                        mov rbx, qword ptr [rsi]
0061FB1D  EB 1A                           jmp 0x14061fb39
0061FB1F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FB23  48 85 C0                        test rax, rax
0061FB26  74 0E                           je 0x14061fb36
0061FB28  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FB2C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FB31  E8 9A AF 09 00                  call 0x1406baad0
0061FB36  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FB39  48 3B DE                        cmp rbx, rsi
0061FB3C  75 E1                           jne 0x14061fb1f
0061FB3E  40 84 FF                        test dil, dil
0061FB41  74 0C                           je 0x14061fb4f
0061FB43  48 8D 0D 36 43 8E 00            lea rcx, [rip + 0x8e4336]
0061FB4A  E8 31 A3 D2 FF                  call 0x140349e80
0061FB4F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0061FB53  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0061FB58  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0061FB5D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0061FB62  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0061FB67  48 83 C4 40                     add rsp, 0x40
0061FB6B  41 5E                           pop r14
0061FB6D  C3                              ret
0061FB6E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExDeleteResourceLiteWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
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
    result = DifGetAPIThunkContextById(407, a2, a3, a4);
    if (result == 0) goto loc_0061FADA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061FA63;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FA71;
loc_0061FA63:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9326136)) != 0) goto loc_0061FA8E;
    if (((*(unsigned int *)(v_rip + 9326324)) & (0x800ULL)) == 0) goto loc_0061FAA1;
loc_0061FA8E:
    result = ExAcquireRundownProtection(v_rip + 9323499, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FADA;
loc_0061FAA1:
    goto loc_0061FAC4;
loc_0061FAAA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FAC4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061FAAA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9323435;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExDeleteResourceLite(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0061FB4F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9326019)) != 0) goto loc_0061FB03;
    if (((*(unsigned int *)(v_rip + 9326207)) & (0x800ULL)) == 0) goto loc_0061FB16;
loc_0061FB03:
    result = ExAcquireRundownProtection(v_rip + 9323382, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FB4F;
loc_0061FB16:
    v_rsi = (result) + (48);
    goto loc_0061FB39;
loc_0061FB1F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FB39:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061FB1F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9323318;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifExDeleteResourceLiteWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(407, a2, a3, a4);
    if (result == 0) goto loc_0061FADA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061FA63;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FA71;
loc_0061FA63:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4E38)) != 0) goto loc_0061FA8E;
    if (((*(uint32_t *)(v_rip + 0x8E4EF4)) & (0x800ULL)) == 0) goto loc_0061FAA1;
loc_0061FA8E:
    result = ExAcquireRundownProtection(v_rip + 9323499, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FADA;
loc_0061FAA1:
    goto loc_0061FAC4;
loc_0061FAAA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FAC4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061FAAA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9323435;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExDeleteResourceLite(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0061FB4F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4DC3)) != 0) goto loc_0061FB03;
    if (((*(uint32_t *)(v_rip + 0x8E4E7F)) & (0x800ULL)) == 0) goto loc_0061FB16;
loc_0061FB03:
    result = ExAcquireRundownProtection(v_rip + 9323382, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FB4F;
loc_0061FB16:
    local_rsi = (result) + (48);
    goto loc_0061FB39;
loc_0061FB1F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FB39:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061FB1F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9323318;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061FA10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061FA10[BB_0061FA10]
  bb_0061FA50[BB_0061FA50]
  bb_0061FA57[BB_0061FA57]
  bb_0061FA63[BB_0061FA63]
  bb_0061FA67[BB_0061FA67]
  bb_0061FA71[BB_0061FA71]
  bb_0061FA82[BB_0061FA82]
  bb_0061FA8E[BB_0061FA8E]
  bb_0061FAA1[BB_0061FAA1]
  bb_0061FAAA[BB_0061FAAA]
  bb_0061FAB3[BB_0061FAB3]
  bb_0061FAC1[BB_0061FAC1]
  bb_0061FAC4[BB_0061FAC4]
  bb_0061FAC9[BB_0061FAC9]
  bb_0061FACE[BB_0061FACE]
  bb_0061FADA[BB_0061FADA]
  bb_0061FAEB[BB_0061FAEB]
  bb_0061FAF7[BB_0061FAF7]
  bb_0061FB03[BB_0061FB03]
  bb_0061FB16[BB_0061FB16]
  bb_0061FB1F[BB_0061FB1F]
  bb_0061FB28[BB_0061FB28]
  bb_0061FB36[BB_0061FB36]
  bb_0061FB39[BB_0061FB39]
  bb_0061FB3E[BB_0061FB3E]
  bb_0061FB43[BB_0061FB43]
  bb_0061FB4F[BB_0061FB4F]
  bb_0061FB6E[BB_0061FB6E]
  bb_0061FA10 -->|branch| bb_0061FADA
  bb_0061FA10 -->|fallthrough| bb_0061FA50
  bb_0061FA50 -->|branch| bb_0061FA63
  bb_0061FA50 -->|fallthrough| bb_0061FA57
  bb_0061FA57 -->|branch| bb_0061FA71
  bb_0061FA63 -->|branch| bb_0061FA71
  bb_0061FA63 -->|fallthrough| bb_0061FA67
  bb_0061FA67 -->|flow| bb_0061FA71
  bb_0061FA71 -->|branch| bb_0061FA8E
  bb_0061FA71 -->|fallthrough| bb_0061FA82
  bb_0061FA82 -->|branch| bb_0061FAA1
  bb_0061FA82 -->|fallthrough| bb_0061FA8E
  bb_0061FA8E -->|branch| bb_0061FADA
  bb_0061FA8E -->|fallthrough| bb_0061FAA1
  bb_0061FAA1 -->|branch| bb_0061FAC4
  bb_0061FAAA -->|branch| bb_0061FAC1
  bb_0061FAAA -->|fallthrough| bb_0061FAB3
  bb_0061FAB3 -->|flow| bb_0061FAC1
  bb_0061FAC1 -->|flow| bb_0061FAC4
  bb_0061FAC4 -->|branch| bb_0061FAAA
  bb_0061FAC4 -->|fallthrough| bb_0061FAC9
  bb_0061FAC9 -->|branch| bb_0061FADA
  bb_0061FAC9 -->|fallthrough| bb_0061FACE
  bb_0061FACE -->|flow| bb_0061FADA
  bb_0061FADA -->|branch| bb_0061FB4F
  bb_0061FADA -->|fallthrough| bb_0061FAEB
  bb_0061FAEB -->|branch| bb_0061FB03
  bb_0061FAEB -->|fallthrough| bb_0061FAF7
  bb_0061FAF7 -->|branch| bb_0061FB16
  bb_0061FAF7 -->|fallthrough| bb_0061FB03
  bb_0061FB03 -->|branch| bb_0061FB4F
  bb_0061FB03 -->|fallthrough| bb_0061FB16
  bb_0061FB16 -->|branch| bb_0061FB39
  bb_0061FB1F -->|branch| bb_0061FB36
  bb_0061FB1F -->|fallthrough| bb_0061FB28
  bb_0061FB28 -->|flow| bb_0061FB36
  bb_0061FB36 -->|flow| bb_0061FB39
  bb_0061FB39 -->|branch| bb_0061FB1F
  bb_0061FB39 -->|fallthrough| bb_0061FB3E
  bb_0061FB3E -->|branch| bb_0061FB4F
  bb_0061FB3E -->|fallthrough| bb_0061FB43
  bb_0061FB43 -->|flow| bb_0061FB4F
```
