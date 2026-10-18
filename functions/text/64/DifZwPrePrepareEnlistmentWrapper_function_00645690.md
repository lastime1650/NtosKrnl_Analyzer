# DifZwPrePrepareEnlistmentWrapper

- RVA: `0x00645690`–`0x006457F4` (길이 `356` bytes)
- VA: `0x0000000140645690`
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
- `0x006456BE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006456E6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645719` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645740` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645759` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00645764` → [ZwPrePrepareEnlistment](../6A/ZwPrePrepareEnlistment_function_006AF8D0.md) (function, `0x006AF8D0`)
- `0x00645791` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006457B8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006457D1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006456F8` → RVA `0x00F048B8` (`.data`; read)
- `0x00645706` → RVA `0x00F04980` (`.data`; read)
- `0x00645712` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645690  48 8B C4                        mov rax, rsp
00645693  48 89 58 08                     mov qword ptr [rax + 8], rbx
00645697  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064569B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064569F  57                              push rdi
006456A0  41 56                           push r14
006456A2  41 57                           push r15
006456A4  48 83 EC 40                     sub rsp, 0x40
006456A8  0F 57 C0                        xorps xmm0, xmm0
006456AB  4C 8B F9                        mov r15, rcx
006456AE  B9 42 00 00 00                  mov ecx, 0x42
006456B3  4C 8B F2                        mov r14, rdx
006456B6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006456BA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006456BE  E8 71 03 E5 FF                  call 0x140495a34
006456C3  48 8B F0                        mov rsi, rax
006456C6  48 85 C0                        test rax, rax
006456C9  0F 84 8F 00 00 00               je 0x14064575e
006456CF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006456D2  A8 18                           test al, 0x18
006456D4  74 0C                           je 0x1406456e2
006456D6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006456DB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006456E0  EB 0E                           jmp 0x1406456f0
006456E2  A8 04                           test al, 4
006456E4  74 0A                           je 0x1406456f0
006456E6  E8 1D E5 E8 FF                  call 0x1404d3c08
006456EB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006456F0  40 32 ED                        xor bpl, bpl
006456F3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006456F8  40 38 2D B9 F1 8B 00            cmp byte ptr [rip + 0x8bf1b9], bpl
006456FF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00645704  75 0C                           jne 0x140645712
00645706  F7 05 70 F2 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf270], 0x800
00645710  74 13                           je 0x140645725
00645712  48 8D 0D 67 E7 8B 00            lea rcx, [rip + 0x8be767]
00645719  E8 02 0F BD FF                  call 0x140216620
0064571E  40 8A E8                        mov bpl, al
00645721  84 C0                           test al, al
00645723  74 39                           je 0x14064575e
00645725  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00645729  48 8B 1F                        mov rbx, qword ptr [rdi]
0064572C  EB 1A                           jmp 0x140645748
0064572E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645732  48 85 C0                        test rax, rax
00645735  74 0E                           je 0x140645745
00645737  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064573B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645740  E8 8B 53 07 00                  call 0x1406baad0
00645745  48 8B 1B                        mov rbx, qword ptr [rbx]
00645748  48 3B DF                        cmp rbx, rdi
0064574B  75 E1                           jne 0x14064572e
0064574D  40 84 ED                        test bpl, bpl
00645750  74 0C                           je 0x14064575e
00645752  48 8D 0D 27 E7 8B 00            lea rcx, [rip + 0x8be727]
00645759  E8 22 47 D0 FF                  call 0x140349e80
0064575E  49 8B D6                        mov rdx, r14
00645761  49 8B CF                        mov rcx, r15
00645764  E8 67 A1 06 00                  call 0x1406af8d0
00645769  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0064576D  48 85 F6                        test rsi, rsi
00645770  74 64                           je 0x1406457d6
00645772  40 32 FF                        xor dil, dil
00645775  40 38 3D 3C F1 8B 00            cmp byte ptr [rip + 0x8bf13c], dil
0064577C  75 0C                           jne 0x14064578a
0064577E  F7 05 F8 F1 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf1f8], 0x800
00645788  74 13                           je 0x14064579d
0064578A  48 8D 0D EF E6 8B 00            lea rcx, [rip + 0x8be6ef]
00645791  E8 8A 0E BD FF                  call 0x140216620
00645796  40 8A F8                        mov dil, al
00645799  84 C0                           test al, al
0064579B  74 39                           je 0x1406457d6
0064579D  48 83 C6 30                     add rsi, 0x30
006457A1  48 8B 1E                        mov rbx, qword ptr [rsi]
006457A4  EB 1A                           jmp 0x1406457c0
006457A6  48 8D 43 F0                     lea rax, [rbx - 0x10]
006457AA  48 85 C0                        test rax, rax
006457AD  74 0E                           je 0x1406457bd
006457AF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006457B3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006457B8  E8 13 53 07 00                  call 0x1406baad0
006457BD  48 8B 1B                        mov rbx, qword ptr [rbx]
006457C0  48 3B DE                        cmp rbx, rsi
006457C3  75 E1                           jne 0x1406457a6
006457C5  40 84 FF                        test dil, dil
006457C8  74 0C                           je 0x1406457d6
006457CA  48 8D 0D AF E6 8B 00            lea rcx, [rip + 0x8be6af]
006457D1  E8 AA 46 D0 FF                  call 0x140349e80
006457D6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
006457DA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006457DF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006457E4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006457E9  48 83 C4 40                     add rsp, 0x40
006457ED  41 5F                           pop r15
006457EF  41 5E                           pop r14
006457F1  5F                              pop rdi
006457F2  C3                              ret
006457F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwPrePrepareEnlistmentWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(66, a2, a3, a4);
    if (result == 0) goto loc_0064575E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006456E2;
    v_stack_m38 = v_stack_p0;
    goto loc_006456F0;
loc_006456E2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9171385)) != 0) goto loc_00645712;
    if (((*(unsigned int *)(v_rip + 9171568)) & (0x800ULL)) == 0) goto loc_00645725;
loc_00645712:
    result = ExAcquireRundownProtection(v_rip + 9168743, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064575E;
loc_00645725:
    goto loc_00645748;
loc_0064572E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645748:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064572E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9168679;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwPrePrepareEnlistment(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_006457D6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9171260)) != 0) goto loc_0064578A;
    if (((*(unsigned int *)(v_rip + 9171448)) & (0x800ULL)) == 0) goto loc_0064579D;
loc_0064578A:
    result = ExAcquireRundownProtection(v_rip + 9168623, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006457D6;
loc_0064579D:
    v_rsi = (result) + (48);
    goto loc_006457C0;
loc_006457A6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006457C0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006457A6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9168559;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwPrePrepareEnlistmentWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(66, Arg2, a3, a4);
    if (result == 0) goto loc_0064575E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006456E2;
    v_stack_m38 = v_stack_p0;
    goto loc_006456F0;
loc_006456E2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BF1B9)) != 0) goto loc_00645712;
    if (((*(uint32_t *)(v_rip + 0x8BF270)) & (0x800ULL)) == 0) goto loc_00645725;
loc_00645712:
    result = ExAcquireRundownProtection(v_rip + 9168743, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064575E;
loc_00645725:
    goto loc_00645748;
loc_0064572E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645748:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064572E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9168679;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwPrePrepareEnlistment(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_006457D6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BF13C)) != 0) goto loc_0064578A;
    if (((*(uint32_t *)(v_rip + 0x8BF1F8)) & (0x800ULL)) == 0) goto loc_0064579D;
loc_0064578A:
    result = ExAcquireRundownProtection(v_rip + 9168623, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006457D6;
loc_0064579D:
    local_rsi = (result) + (48);
    goto loc_006457C0;
loc_006457A6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006457C0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006457A6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9168559;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645690[BB_00645690]
  bb_006456CF[BB_006456CF]
  bb_006456D6[BB_006456D6]
  bb_006456E2[BB_006456E2]
  bb_006456E6[BB_006456E6]
  bb_006456F0[BB_006456F0]
  bb_00645706[BB_00645706]
  bb_00645712[BB_00645712]
  bb_00645725[BB_00645725]
  bb_0064572E[BB_0064572E]
  bb_00645737[BB_00645737]
  bb_00645745[BB_00645745]
  bb_00645748[BB_00645748]
  bb_0064574D[BB_0064574D]
  bb_00645752[BB_00645752]
  bb_0064575E[BB_0064575E]
  bb_00645772[BB_00645772]
  bb_0064577E[BB_0064577E]
  bb_0064578A[BB_0064578A]
  bb_0064579D[BB_0064579D]
  bb_006457A6[BB_006457A6]
  bb_006457AF[BB_006457AF]
  bb_006457BD[BB_006457BD]
  bb_006457C0[BB_006457C0]
  bb_006457C5[BB_006457C5]
  bb_006457CA[BB_006457CA]
  bb_006457D6[BB_006457D6]
  bb_006457F3[BB_006457F3]
  bb_00645690 -->|branch| bb_0064575E
  bb_00645690 -->|fallthrough| bb_006456CF
  bb_006456CF -->|branch| bb_006456E2
  bb_006456CF -->|fallthrough| bb_006456D6
  bb_006456D6 -->|branch| bb_006456F0
  bb_006456E2 -->|branch| bb_006456F0
  bb_006456E2 -->|fallthrough| bb_006456E6
  bb_006456E6 -->|flow| bb_006456F0
  bb_006456F0 -->|branch| bb_00645712
  bb_006456F0 -->|fallthrough| bb_00645706
  bb_00645706 -->|branch| bb_00645725
  bb_00645706 -->|fallthrough| bb_00645712
  bb_00645712 -->|branch| bb_0064575E
  bb_00645712 -->|fallthrough| bb_00645725
  bb_00645725 -->|branch| bb_00645748
  bb_0064572E -->|branch| bb_00645745
  bb_0064572E -->|fallthrough| bb_00645737
  bb_00645737 -->|flow| bb_00645745
  bb_00645745 -->|flow| bb_00645748
  bb_00645748 -->|branch| bb_0064572E
  bb_00645748 -->|fallthrough| bb_0064574D
  bb_0064574D -->|branch| bb_0064575E
  bb_0064574D -->|fallthrough| bb_00645752
  bb_00645752 -->|flow| bb_0064575E
  bb_0064575E -->|branch| bb_006457D6
  bb_0064575E -->|fallthrough| bb_00645772
  bb_00645772 -->|branch| bb_0064578A
  bb_00645772 -->|fallthrough| bb_0064577E
  bb_0064577E -->|branch| bb_0064579D
  bb_0064577E -->|fallthrough| bb_0064578A
  bb_0064578A -->|branch| bb_006457D6
  bb_0064578A -->|fallthrough| bb_0064579D
  bb_0064579D -->|branch| bb_006457C0
  bb_006457A6 -->|branch| bb_006457BD
  bb_006457A6 -->|fallthrough| bb_006457AF
  bb_006457AF -->|flow| bb_006457BD
  bb_006457BD -->|flow| bb_006457C0
  bb_006457C0 -->|branch| bb_006457A6
  bb_006457C0 -->|fallthrough| bb_006457C5
  bb_006457C5 -->|branch| bb_006457D6
  bb_006457C5 -->|fallthrough| bb_006457CA
  bb_006457CA -->|flow| bb_006457D6
```
