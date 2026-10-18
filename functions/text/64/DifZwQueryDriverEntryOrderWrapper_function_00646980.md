# DifZwQueryDriverEntryOrderWrapper

- RVA: `0x00646980`–`0x00646AE4` (길이 `356` bytes)
- VA: `0x0000000140646980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006469AE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006469D6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00646A09` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00646A30` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646A49` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00646A54` → [ZwQueryDriverEntryOrder](../6A/ZwQueryDriverEntryOrder_function_006AFAD0.md) (function, `0x006AFAD0`)
- `0x00646A81` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00646AA8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646AC1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006469E8` → RVA `0x00F048B8` (`.data`; read)
- `0x006469F6` → RVA `0x00F04980` (`.data`; read)
- `0x00646A02` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00646980  48 8B C4                        mov rax, rsp
00646983  48 89 58 08                     mov qword ptr [rax + 8], rbx
00646987  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064698B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064698F  57                              push rdi
00646990  41 56                           push r14
00646992  41 57                           push r15
00646994  48 83 EC 40                     sub rsp, 0x40
00646998  0F 57 C0                        xorps xmm0, xmm0
0064699B  4C 8B F9                        mov r15, rcx
0064699E  B9 36 00 00 00                  mov ecx, 0x36
006469A3  4C 8B F2                        mov r14, rdx
006469A6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006469AA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006469AE  E8 81 F0 E4 FF                  call 0x140495a34
006469B3  48 8B F0                        mov rsi, rax
006469B6  48 85 C0                        test rax, rax
006469B9  0F 84 8F 00 00 00               je 0x140646a4e
006469BF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006469C2  A8 18                           test al, 0x18
006469C4  74 0C                           je 0x1406469d2
006469C6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006469CB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006469D0  EB 0E                           jmp 0x1406469e0
006469D2  A8 04                           test al, 4
006469D4  74 0A                           je 0x1406469e0
006469D6  E8 2D D2 E8 FF                  call 0x1404d3c08
006469DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006469E0  40 32 ED                        xor bpl, bpl
006469E3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006469E8  40 38 2D C9 DE 8B 00            cmp byte ptr [rip + 0x8bdec9], bpl
006469EF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006469F4  75 0C                           jne 0x140646a02
006469F6  F7 05 80 DF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bdf80], 0x800
00646A00  74 13                           je 0x140646a15
00646A02  48 8D 0D 77 D4 8B 00            lea rcx, [rip + 0x8bd477]
00646A09  E8 12 FC BC FF                  call 0x140216620
00646A0E  40 8A E8                        mov bpl, al
00646A11  84 C0                           test al, al
00646A13  74 39                           je 0x140646a4e
00646A15  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00646A19  48 8B 1F                        mov rbx, qword ptr [rdi]
00646A1C  EB 1A                           jmp 0x140646a38
00646A1E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00646A22  48 85 C0                        test rax, rax
00646A25  74 0E                           je 0x140646a35
00646A27  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00646A2B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00646A30  E8 9B 40 07 00                  call 0x1406baad0
00646A35  48 8B 1B                        mov rbx, qword ptr [rbx]
00646A38  48 3B DF                        cmp rbx, rdi
00646A3B  75 E1                           jne 0x140646a1e
00646A3D  40 84 ED                        test bpl, bpl
00646A40  74 0C                           je 0x140646a4e
00646A42  48 8D 0D 37 D4 8B 00            lea rcx, [rip + 0x8bd437]
00646A49  E8 32 34 D0 FF                  call 0x140349e80
00646A4E  49 8B D6                        mov rdx, r14
00646A51  49 8B CF                        mov rcx, r15
00646A54  E8 77 90 06 00                  call 0x1406afad0
00646A59  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00646A5D  48 85 F6                        test rsi, rsi
00646A60  74 64                           je 0x140646ac6
00646A62  40 32 FF                        xor dil, dil
00646A65  40 38 3D 4C DE 8B 00            cmp byte ptr [rip + 0x8bde4c], dil
00646A6C  75 0C                           jne 0x140646a7a
00646A6E  F7 05 08 DF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bdf08], 0x800
00646A78  74 13                           je 0x140646a8d
00646A7A  48 8D 0D FF D3 8B 00            lea rcx, [rip + 0x8bd3ff]
00646A81  E8 9A FB BC FF                  call 0x140216620
00646A86  40 8A F8                        mov dil, al
00646A89  84 C0                           test al, al
00646A8B  74 39                           je 0x140646ac6
00646A8D  48 83 C6 30                     add rsi, 0x30
00646A91  48 8B 1E                        mov rbx, qword ptr [rsi]
00646A94  EB 1A                           jmp 0x140646ab0
00646A96  48 8D 43 F0                     lea rax, [rbx - 0x10]
00646A9A  48 85 C0                        test rax, rax
00646A9D  74 0E                           je 0x140646aad
00646A9F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00646AA3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00646AA8  E8 23 40 07 00                  call 0x1406baad0
00646AAD  48 8B 1B                        mov rbx, qword ptr [rbx]
00646AB0  48 3B DE                        cmp rbx, rsi
00646AB3  75 E1                           jne 0x140646a96
00646AB5  40 84 FF                        test dil, dil
00646AB8  74 0C                           je 0x140646ac6
00646ABA  48 8D 0D BF D3 8B 00            lea rcx, [rip + 0x8bd3bf]
00646AC1  E8 BA 33 D0 FF                  call 0x140349e80
00646AC6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00646ACA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00646ACF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00646AD4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00646AD9  48 83 C4 40                     add rsp, 0x40
00646ADD  41 5F                           pop r15
00646ADF  41 5E                           pop r14
00646AE1  5F                              pop rdi
00646AE2  C3                              ret
00646AE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryDriverEntryOrderWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(54, a2, a3, a4);
    if (result == 0) goto loc_00646A4E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006469D2;
    v_stack_m38 = v_stack_p0;
    goto loc_006469E0;
loc_006469D2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9166537)) != 0) goto loc_00646A02;
    if (((*(unsigned int *)(v_rip + 9166720)) & (0x800ULL)) == 0) goto loc_00646A15;
loc_00646A02:
    result = ExAcquireRundownProtection(v_rip + 9163895, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00646A4E;
loc_00646A15:
    goto loc_00646A38;
loc_00646A1E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00646A38:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00646A1E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9163831;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwQueryDriverEntryOrder(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00646AC6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9166412)) != 0) goto loc_00646A7A;
    if (((*(unsigned int *)(v_rip + 9166600)) & (0x800ULL)) == 0) goto loc_00646A8D;
loc_00646A7A:
    result = ExAcquireRundownProtection(v_rip + 9163775, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00646AC6;
loc_00646A8D:
    v_rsi = (result) + (48);
    goto loc_00646AB0;
loc_00646A96:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00646AB0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00646A96;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9163711;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryDriverEntryOrderWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(54, Arg2, a3, a4);
    if (result == 0) goto loc_00646A4E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006469D2;
    v_stack_m38 = v_stack_p0;
    goto loc_006469E0;
loc_006469D2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BDEC9)) != 0) goto loc_00646A02;
    if (((*(uint32_t *)(v_rip + 0x8BDF80)) & (0x800ULL)) == 0) goto loc_00646A15;
loc_00646A02:
    result = ExAcquireRundownProtection(v_rip + 9163895, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00646A4E;
loc_00646A15:
    goto loc_00646A38;
loc_00646A1E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00646A38:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00646A1E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9163831;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwQueryDriverEntryOrder(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00646AC6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BDE4C)) != 0) goto loc_00646A7A;
    if (((*(uint32_t *)(v_rip + 0x8BDF08)) & (0x800ULL)) == 0) goto loc_00646A8D;
loc_00646A7A:
    result = ExAcquireRundownProtection(v_rip + 9163775, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00646AC6;
loc_00646A8D:
    local_rsi = (result) + (48);
    goto loc_00646AB0;
loc_00646A96:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00646AB0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00646A96;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9163711;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00646980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00646980[BB_00646980]
  bb_006469BF[BB_006469BF]
  bb_006469C6[BB_006469C6]
  bb_006469D2[BB_006469D2]
  bb_006469D6[BB_006469D6]
  bb_006469E0[BB_006469E0]
  bb_006469F6[BB_006469F6]
  bb_00646A02[BB_00646A02]
  bb_00646A15[BB_00646A15]
  bb_00646A1E[BB_00646A1E]
  bb_00646A27[BB_00646A27]
  bb_00646A35[BB_00646A35]
  bb_00646A38[BB_00646A38]
  bb_00646A3D[BB_00646A3D]
  bb_00646A42[BB_00646A42]
  bb_00646A4E[BB_00646A4E]
  bb_00646A62[BB_00646A62]
  bb_00646A6E[BB_00646A6E]
  bb_00646A7A[BB_00646A7A]
  bb_00646A8D[BB_00646A8D]
  bb_00646A96[BB_00646A96]
  bb_00646A9F[BB_00646A9F]
  bb_00646AAD[BB_00646AAD]
  bb_00646AB0[BB_00646AB0]
  bb_00646AB5[BB_00646AB5]
  bb_00646ABA[BB_00646ABA]
  bb_00646AC6[BB_00646AC6]
  bb_00646AE3[BB_00646AE3]
  bb_00646980 -->|branch| bb_00646A4E
  bb_00646980 -->|fallthrough| bb_006469BF
  bb_006469BF -->|branch| bb_006469D2
  bb_006469BF -->|fallthrough| bb_006469C6
  bb_006469C6 -->|branch| bb_006469E0
  bb_006469D2 -->|branch| bb_006469E0
  bb_006469D2 -->|fallthrough| bb_006469D6
  bb_006469D6 -->|flow| bb_006469E0
  bb_006469E0 -->|branch| bb_00646A02
  bb_006469E0 -->|fallthrough| bb_006469F6
  bb_006469F6 -->|branch| bb_00646A15
  bb_006469F6 -->|fallthrough| bb_00646A02
  bb_00646A02 -->|branch| bb_00646A4E
  bb_00646A02 -->|fallthrough| bb_00646A15
  bb_00646A15 -->|branch| bb_00646A38
  bb_00646A1E -->|branch| bb_00646A35
  bb_00646A1E -->|fallthrough| bb_00646A27
  bb_00646A27 -->|flow| bb_00646A35
  bb_00646A35 -->|flow| bb_00646A38
  bb_00646A38 -->|branch| bb_00646A1E
  bb_00646A38 -->|fallthrough| bb_00646A3D
  bb_00646A3D -->|branch| bb_00646A4E
  bb_00646A3D -->|fallthrough| bb_00646A42
  bb_00646A42 -->|flow| bb_00646A4E
  bb_00646A4E -->|branch| bb_00646AC6
  bb_00646A4E -->|fallthrough| bb_00646A62
  bb_00646A62 -->|branch| bb_00646A7A
  bb_00646A62 -->|fallthrough| bb_00646A6E
  bb_00646A6E -->|branch| bb_00646A8D
  bb_00646A6E -->|fallthrough| bb_00646A7A
  bb_00646A7A -->|branch| bb_00646AC6
  bb_00646A7A -->|fallthrough| bb_00646A8D
  bb_00646A8D -->|branch| bb_00646AB0
  bb_00646A96 -->|branch| bb_00646AAD
  bb_00646A96 -->|fallthrough| bb_00646A9F
  bb_00646A9F -->|flow| bb_00646AAD
  bb_00646AAD -->|flow| bb_00646AB0
  bb_00646AB0 -->|branch| bb_00646A96
  bb_00646AB0 -->|fallthrough| bb_00646AB5
  bb_00646AB5 -->|branch| bb_00646AC6
  bb_00646AB5 -->|fallthrough| bb_00646ABA
  bb_00646ABA -->|flow| bb_00646AC6
```
