# DifZwPrepareEnlistmentWrapper

- RVA: `0x00645970`–`0x00645AD4` (길이 `356` bytes)
- VA: `0x0000000140645970`
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
- `0x0064599E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006459C6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006459F9` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645A20` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645A39` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00645A44` → [ZwPrepareEnlistment](../6A/ZwPrepareEnlistment_function_006AF910.md) (function, `0x006AF910`)
- `0x00645A71` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645A98` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645AB1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006459D8` → RVA `0x00F048B8` (`.data`; read)
- `0x006459E6` → RVA `0x00F04980` (`.data`; read)
- `0x006459F2` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645970  48 8B C4                        mov rax, rsp
00645973  48 89 58 08                     mov qword ptr [rax + 8], rbx
00645977  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064597B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064597F  57                              push rdi
00645980  41 56                           push r14
00645982  41 57                           push r15
00645984  48 83 EC 40                     sub rsp, 0x40
00645988  0F 57 C0                        xorps xmm0, xmm0
0064598B  4C 8B F9                        mov r15, rcx
0064598E  B9 40 00 00 00                  mov ecx, 0x40
00645993  4C 8B F2                        mov r14, rdx
00645996  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0064599A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0064599E  E8 91 00 E5 FF                  call 0x140495a34
006459A3  48 8B F0                        mov rsi, rax
006459A6  48 85 C0                        test rax, rax
006459A9  0F 84 8F 00 00 00               je 0x140645a3e
006459AF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006459B2  A8 18                           test al, 0x18
006459B4  74 0C                           je 0x1406459c2
006459B6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006459BB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006459C0  EB 0E                           jmp 0x1406459d0
006459C2  A8 04                           test al, 4
006459C4  74 0A                           je 0x1406459d0
006459C6  E8 3D E2 E8 FF                  call 0x1404d3c08
006459CB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006459D0  40 32 ED                        xor bpl, bpl
006459D3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006459D8  40 38 2D D9 EE 8B 00            cmp byte ptr [rip + 0x8beed9], bpl
006459DF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006459E4  75 0C                           jne 0x1406459f2
006459E6  F7 05 90 EF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bef90], 0x800
006459F0  74 13                           je 0x140645a05
006459F2  48 8D 0D 87 E4 8B 00            lea rcx, [rip + 0x8be487]
006459F9  E8 22 0C BD FF                  call 0x140216620
006459FE  40 8A E8                        mov bpl, al
00645A01  84 C0                           test al, al
00645A03  74 39                           je 0x140645a3e
00645A05  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00645A09  48 8B 1F                        mov rbx, qword ptr [rdi]
00645A0C  EB 1A                           jmp 0x140645a28
00645A0E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645A12  48 85 C0                        test rax, rax
00645A15  74 0E                           je 0x140645a25
00645A17  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645A1B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645A20  E8 AB 50 07 00                  call 0x1406baad0
00645A25  48 8B 1B                        mov rbx, qword ptr [rbx]
00645A28  48 3B DF                        cmp rbx, rdi
00645A2B  75 E1                           jne 0x140645a0e
00645A2D  40 84 ED                        test bpl, bpl
00645A30  74 0C                           je 0x140645a3e
00645A32  48 8D 0D 47 E4 8B 00            lea rcx, [rip + 0x8be447]
00645A39  E8 42 44 D0 FF                  call 0x140349e80
00645A3E  49 8B D6                        mov rdx, r14
00645A41  49 8B CF                        mov rcx, r15
00645A44  E8 C7 9E 06 00                  call 0x1406af910
00645A49  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00645A4D  48 85 F6                        test rsi, rsi
00645A50  74 64                           je 0x140645ab6
00645A52  40 32 FF                        xor dil, dil
00645A55  40 38 3D 5C EE 8B 00            cmp byte ptr [rip + 0x8bee5c], dil
00645A5C  75 0C                           jne 0x140645a6a
00645A5E  F7 05 18 EF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bef18], 0x800
00645A68  74 13                           je 0x140645a7d
00645A6A  48 8D 0D 0F E4 8B 00            lea rcx, [rip + 0x8be40f]
00645A71  E8 AA 0B BD FF                  call 0x140216620
00645A76  40 8A F8                        mov dil, al
00645A79  84 C0                           test al, al
00645A7B  74 39                           je 0x140645ab6
00645A7D  48 83 C6 30                     add rsi, 0x30
00645A81  48 8B 1E                        mov rbx, qword ptr [rsi]
00645A84  EB 1A                           jmp 0x140645aa0
00645A86  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645A8A  48 85 C0                        test rax, rax
00645A8D  74 0E                           je 0x140645a9d
00645A8F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645A93  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645A98  E8 33 50 07 00                  call 0x1406baad0
00645A9D  48 8B 1B                        mov rbx, qword ptr [rbx]
00645AA0  48 3B DE                        cmp rbx, rsi
00645AA3  75 E1                           jne 0x140645a86
00645AA5  40 84 FF                        test dil, dil
00645AA8  74 0C                           je 0x140645ab6
00645AAA  48 8D 0D CF E3 8B 00            lea rcx, [rip + 0x8be3cf]
00645AB1  E8 CA 43 D0 FF                  call 0x140349e80
00645AB6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00645ABA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00645ABF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00645AC4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00645AC9  48 83 C4 40                     add rsp, 0x40
00645ACD  41 5F                           pop r15
00645ACF  41 5E                           pop r14
00645AD1  5F                              pop rdi
00645AD2  C3                              ret
00645AD3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwPrepareEnlistmentWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(64, a2, a3, a4);
    if (result == 0) goto loc_00645A3E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006459C2;
    v_stack_m38 = v_stack_p0;
    goto loc_006459D0;
loc_006459C2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9170649)) != 0) goto loc_006459F2;
    if (((*(unsigned int *)(v_rip + 9170832)) & (0x800ULL)) == 0) goto loc_00645A05;
loc_006459F2:
    result = ExAcquireRundownProtection(v_rip + 9168007, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645A3E;
loc_00645A05:
    goto loc_00645A28;
loc_00645A0E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645A28:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00645A0E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167943;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwPrepareEnlistment(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00645AB6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9170524)) != 0) goto loc_00645A6A;
    if (((*(unsigned int *)(v_rip + 9170712)) & (0x800ULL)) == 0) goto loc_00645A7D;
loc_00645A6A:
    result = ExAcquireRundownProtection(v_rip + 9167887, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645AB6;
loc_00645A7D:
    v_rsi = (result) + (48);
    goto loc_00645AA0;
loc_00645A86:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645AA0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00645A86;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167823;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwPrepareEnlistmentWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(64, Arg2, a3, a4);
    if (result == 0) goto loc_00645A3E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006459C2;
    v_stack_m38 = v_stack_p0;
    goto loc_006459D0;
loc_006459C2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BEED9)) != 0) goto loc_006459F2;
    if (((*(uint32_t *)(v_rip + 0x8BEF90)) & (0x800ULL)) == 0) goto loc_00645A05;
loc_006459F2:
    result = ExAcquireRundownProtection(v_rip + 9168007, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645A3E;
loc_00645A05:
    goto loc_00645A28;
loc_00645A0E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645A28:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00645A0E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167943;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwPrepareEnlistment(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00645AB6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BEE5C)) != 0) goto loc_00645A6A;
    if (((*(uint32_t *)(v_rip + 0x8BEF18)) & (0x800ULL)) == 0) goto loc_00645A7D;
loc_00645A6A:
    result = ExAcquireRundownProtection(v_rip + 9167887, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645AB6;
loc_00645A7D:
    local_rsi = (result) + (48);
    goto loc_00645AA0;
loc_00645A86:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645AA0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00645A86;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167823;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645970[BB_00645970]
  bb_006459AF[BB_006459AF]
  bb_006459B6[BB_006459B6]
  bb_006459C2[BB_006459C2]
  bb_006459C6[BB_006459C6]
  bb_006459D0[BB_006459D0]
  bb_006459E6[BB_006459E6]
  bb_006459F2[BB_006459F2]
  bb_00645A05[BB_00645A05]
  bb_00645A0E[BB_00645A0E]
  bb_00645A17[BB_00645A17]
  bb_00645A25[BB_00645A25]
  bb_00645A28[BB_00645A28]
  bb_00645A2D[BB_00645A2D]
  bb_00645A32[BB_00645A32]
  bb_00645A3E[BB_00645A3E]
  bb_00645A52[BB_00645A52]
  bb_00645A5E[BB_00645A5E]
  bb_00645A6A[BB_00645A6A]
  bb_00645A7D[BB_00645A7D]
  bb_00645A86[BB_00645A86]
  bb_00645A8F[BB_00645A8F]
  bb_00645A9D[BB_00645A9D]
  bb_00645AA0[BB_00645AA0]
  bb_00645AA5[BB_00645AA5]
  bb_00645AAA[BB_00645AAA]
  bb_00645AB6[BB_00645AB6]
  bb_00645AD3[BB_00645AD3]
  bb_00645970 -->|branch| bb_00645A3E
  bb_00645970 -->|fallthrough| bb_006459AF
  bb_006459AF -->|branch| bb_006459C2
  bb_006459AF -->|fallthrough| bb_006459B6
  bb_006459B6 -->|branch| bb_006459D0
  bb_006459C2 -->|branch| bb_006459D0
  bb_006459C2 -->|fallthrough| bb_006459C6
  bb_006459C6 -->|flow| bb_006459D0
  bb_006459D0 -->|branch| bb_006459F2
  bb_006459D0 -->|fallthrough| bb_006459E6
  bb_006459E6 -->|branch| bb_00645A05
  bb_006459E6 -->|fallthrough| bb_006459F2
  bb_006459F2 -->|branch| bb_00645A3E
  bb_006459F2 -->|fallthrough| bb_00645A05
  bb_00645A05 -->|branch| bb_00645A28
  bb_00645A0E -->|branch| bb_00645A25
  bb_00645A0E -->|fallthrough| bb_00645A17
  bb_00645A17 -->|flow| bb_00645A25
  bb_00645A25 -->|flow| bb_00645A28
  bb_00645A28 -->|branch| bb_00645A0E
  bb_00645A28 -->|fallthrough| bb_00645A2D
  bb_00645A2D -->|branch| bb_00645A3E
  bb_00645A2D -->|fallthrough| bb_00645A32
  bb_00645A32 -->|flow| bb_00645A3E
  bb_00645A3E -->|branch| bb_00645AB6
  bb_00645A3E -->|fallthrough| bb_00645A52
  bb_00645A52 -->|branch| bb_00645A6A
  bb_00645A52 -->|fallthrough| bb_00645A5E
  bb_00645A5E -->|branch| bb_00645A7D
  bb_00645A5E -->|fallthrough| bb_00645A6A
  bb_00645A6A -->|branch| bb_00645AB6
  bb_00645A6A -->|fallthrough| bb_00645A7D
  bb_00645A7D -->|branch| bb_00645AA0
  bb_00645A86 -->|branch| bb_00645A9D
  bb_00645A86 -->|fallthrough| bb_00645A8F
  bb_00645A8F -->|flow| bb_00645A9D
  bb_00645A9D -->|flow| bb_00645AA0
  bb_00645AA0 -->|branch| bb_00645A86
  bb_00645AA0 -->|fallthrough| bb_00645AA5
  bb_00645AA5 -->|branch| bb_00645AB6
  bb_00645AA5 -->|fallthrough| bb_00645AAA
  bb_00645AAA -->|flow| bb_00645AB6
```
