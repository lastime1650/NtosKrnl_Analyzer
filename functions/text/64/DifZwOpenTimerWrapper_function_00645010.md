# DifZwOpenTimerWrapper

- RVA: `0x00645010`–`0x00645185` (길이 `373` bytes)
- VA: `0x0000000140645010`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064504C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00645072` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006450A6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006450CC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006450E5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006450F3` → [ZwOpenTimer](../6A/ZwOpenTimer_function_006AF830.md) (function, `0x006AF830`)
- `0x0064511F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645145` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064515E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645082` → RVA `0x00F048B8` (`.data`; read)
- `0x00645093` → RVA `0x00F04980` (`.data`; read)
- `0x0064509F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645010  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00645015  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064501A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064501F  55                              push rbp
00645020  41 54                           push r12
00645022  41 55                           push r13
00645024  41 56                           push r14
00645026  41 57                           push r15
00645028  48 8B EC                        mov rbp, rsp
0064502B  48 83 EC 50                     sub rsp, 0x50
0064502F  33 C0                           xor eax, eax
00645031  0F 57 C0                        xorps xmm0, xmm0
00645034  4C 8B E9                        mov r13, rcx
00645037  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064503B  4D 8B F8                        mov r15, r8
0064503E  44 8B E2                        mov r12d, edx
00645041  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00645045  8D 48 46                        lea ecx, [rax + 0x46]
00645048  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064504C  E8 E3 09 E5 FF                  call 0x140495a34
00645051  48 8B F0                        mov rsi, rax
00645054  48 85 C0                        test rax, rax
00645057  0F 84 8D 00 00 00               je 0x1406450ea
0064505D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00645060  A8 18                           test al, 0x18
00645062  74 0A                           je 0x14064506e
00645064  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00645068  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064506C  EB 0D                           jmp 0x14064507b
0064506E  A8 04                           test al, 4
00645070  74 09                           je 0x14064507b
00645072  E8 91 EB E8 FF                  call 0x1404d3c08
00645077  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064507B  45 32 F6                        xor r14b, r14b
0064507E  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00645082  44 38 35 2F F8 8B 00            cmp byte ptr [rip + 0x8bf82f], r14b
00645089  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0064508D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00645091  75 0C                           jne 0x14064509f
00645093  F7 05 E3 F8 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf8e3], 0x800
0064509D  74 13                           je 0x1406450b2
0064509F  48 8D 0D DA ED 8B 00            lea rcx, [rip + 0x8bedda]
006450A6  E8 75 15 BD FF                  call 0x140216620
006450AB  44 8A F0                        mov r14b, al
006450AE  84 C0                           test al, al
006450B0  74 38                           je 0x1406450ea
006450B2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006450B6  48 8B 1F                        mov rbx, qword ptr [rdi]
006450B9  EB 19                           jmp 0x1406450d4
006450BB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006450BF  48 85 C0                        test rax, rax
006450C2  74 0D                           je 0x1406450d1
006450C4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006450C8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006450CC  E8 FF 59 07 00                  call 0x1406baad0
006450D1  48 8B 1B                        mov rbx, qword ptr [rbx]
006450D4  48 3B DF                        cmp rbx, rdi
006450D7  75 E2                           jne 0x1406450bb
006450D9  45 84 F6                        test r14b, r14b
006450DC  74 0C                           je 0x1406450ea
006450DE  48 8D 0D 9B ED 8B 00            lea rcx, [rip + 0x8bed9b]
006450E5  E8 96 4D D0 FF                  call 0x140349e80
006450EA  4D 8B C7                        mov r8, r15
006450ED  41 8B D4                        mov edx, r12d
006450F0  49 8B CD                        mov rcx, r13
006450F3  E8 38 A7 06 00                  call 0x1406af830
006450F8  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006450FB  48 85 F6                        test rsi, rsi
006450FE  74 63                           je 0x140645163
00645100  40 32 FF                        xor dil, dil
00645103  40 38 3D AE F7 8B 00            cmp byte ptr [rip + 0x8bf7ae], dil
0064510A  75 0C                           jne 0x140645118
0064510C  F7 05 6A F8 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf86a], 0x800
00645116  74 13                           je 0x14064512b
00645118  48 8D 0D 61 ED 8B 00            lea rcx, [rip + 0x8bed61]
0064511F  E8 FC 14 BD FF                  call 0x140216620
00645124  40 8A F8                        mov dil, al
00645127  84 C0                           test al, al
00645129  74 38                           je 0x140645163
0064512B  48 83 C6 30                     add rsi, 0x30
0064512F  48 8B 1E                        mov rbx, qword ptr [rsi]
00645132  EB 19                           jmp 0x14064514d
00645134  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645138  48 85 C0                        test rax, rax
0064513B  74 0D                           je 0x14064514a
0064513D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645141  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00645145  E8 86 59 07 00                  call 0x1406baad0
0064514A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064514D  48 3B DE                        cmp rbx, rsi
00645150  75 E2                           jne 0x140645134
00645152  40 84 FF                        test dil, dil
00645155  74 0C                           je 0x140645163
00645157  48 8D 0D 22 ED 8B 00            lea rcx, [rip + 0x8bed22]
0064515E  E8 1D 4D D0 FF                  call 0x140349e80
00645163  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00645166  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064516B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0064516F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00645173  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00645177  49 8B E3                        mov rsp, r11
0064517A  41 5F                           pop r15
0064517C  41 5E                           pop r14
0064517E  41 5D                           pop r13
00645180  41 5C                           pop r12
00645182  5D                              pop rbp
00645183  C3                              ret
00645184  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenTimerWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 70, a2, a3, a4);
    if (result == 0) goto loc_006450EA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064506E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064507B;
loc_0064506E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9173039)) != 0) goto loc_0064509F;
    if (((*(unsigned int *)(v_rip + 9173219)) & (0x800ULL)) == 0) goto loc_006450B2;
loc_0064509F:
    result = ExAcquireRundownProtection(v_rip + 9170394, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006450EA;
loc_006450B2:
    goto loc_006450D4;
loc_006450BB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006450D4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006450BB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9170331;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenTimer(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00645163;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9172910)) != 0) goto loc_00645118;
    if (((*(unsigned int *)(v_rip + 9173098)) & (0x800ULL)) == 0) goto loc_0064512B;
loc_00645118:
    result = ExAcquireRundownProtection(v_rip + 9170273, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645163;
loc_0064512B:
    v_rsi = (result) + (48);
    goto loc_0064514D;
loc_00645134:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064514D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00645134;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9170210;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenTimerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 70, Arg2, Arg3, a4);
    if (result == 0) goto loc_006450EA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064506E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064507B;
loc_0064506E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8BF82F)) != 0) goto loc_0064509F;
    if (((*(uint32_t *)(v_rip + 0x8BF8E3)) & (0x800ULL)) == 0) goto loc_006450B2;
loc_0064509F:
    result = ExAcquireRundownProtection(v_rip + 9170394, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006450EA;
loc_006450B2:
    goto loc_006450D4;
loc_006450BB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006450D4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006450BB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9170331;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenTimer(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00645163;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BF7AE)) != 0) goto loc_00645118;
    if (((*(uint32_t *)(v_rip + 0x8BF86A)) & (0x800ULL)) == 0) goto loc_0064512B;
loc_00645118:
    result = ExAcquireRundownProtection(v_rip + 9170273, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645163;
loc_0064512B:
    local_rsi = (result) + (48);
    goto loc_0064514D;
loc_00645134:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0064514D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00645134;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9170210;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645010[BB_00645010]
  bb_0064505D[BB_0064505D]
  bb_00645064[BB_00645064]
  bb_0064506E[BB_0064506E]
  bb_00645072[BB_00645072]
  bb_0064507B[BB_0064507B]
  bb_00645093[BB_00645093]
  bb_0064509F[BB_0064509F]
  bb_006450B2[BB_006450B2]
  bb_006450BB[BB_006450BB]
  bb_006450C4[BB_006450C4]
  bb_006450D1[BB_006450D1]
  bb_006450D4[BB_006450D4]
  bb_006450D9[BB_006450D9]
  bb_006450DE[BB_006450DE]
  bb_006450EA[BB_006450EA]
  bb_00645100[BB_00645100]
  bb_0064510C[BB_0064510C]
  bb_00645118[BB_00645118]
  bb_0064512B[BB_0064512B]
  bb_00645134[BB_00645134]
  bb_0064513D[BB_0064513D]
  bb_0064514A[BB_0064514A]
  bb_0064514D[BB_0064514D]
  bb_00645152[BB_00645152]
  bb_00645157[BB_00645157]
  bb_00645163[BB_00645163]
  bb_00645184[BB_00645184]
  bb_00645010 -->|branch| bb_006450EA
  bb_00645010 -->|fallthrough| bb_0064505D
  bb_0064505D -->|branch| bb_0064506E
  bb_0064505D -->|fallthrough| bb_00645064
  bb_00645064 -->|branch| bb_0064507B
  bb_0064506E -->|branch| bb_0064507B
  bb_0064506E -->|fallthrough| bb_00645072
  bb_00645072 -->|flow| bb_0064507B
  bb_0064507B -->|branch| bb_0064509F
  bb_0064507B -->|fallthrough| bb_00645093
  bb_00645093 -->|branch| bb_006450B2
  bb_00645093 -->|fallthrough| bb_0064509F
  bb_0064509F -->|branch| bb_006450EA
  bb_0064509F -->|fallthrough| bb_006450B2
  bb_006450B2 -->|branch| bb_006450D4
  bb_006450BB -->|branch| bb_006450D1
  bb_006450BB -->|fallthrough| bb_006450C4
  bb_006450C4 -->|flow| bb_006450D1
  bb_006450D1 -->|flow| bb_006450D4
  bb_006450D4 -->|branch| bb_006450BB
  bb_006450D4 -->|fallthrough| bb_006450D9
  bb_006450D9 -->|branch| bb_006450EA
  bb_006450D9 -->|fallthrough| bb_006450DE
  bb_006450DE -->|flow| bb_006450EA
  bb_006450EA -->|branch| bb_00645163
  bb_006450EA -->|fallthrough| bb_00645100
  bb_00645100 -->|branch| bb_00645118
  bb_00645100 -->|fallthrough| bb_0064510C
  bb_0064510C -->|branch| bb_0064512B
  bb_0064510C -->|fallthrough| bb_00645118
  bb_00645118 -->|branch| bb_00645163
  bb_00645118 -->|fallthrough| bb_0064512B
  bb_0064512B -->|branch| bb_0064514D
  bb_00645134 -->|branch| bb_0064514A
  bb_00645134 -->|fallthrough| bb_0064513D
  bb_0064513D -->|flow| bb_0064514A
  bb_0064514A -->|flow| bb_0064514D
  bb_0064514D -->|branch| bb_00645134
  bb_0064514D -->|fallthrough| bb_00645152
  bb_00645152 -->|branch| bb_00645163
  bb_00645152 -->|fallthrough| bb_00645157
  bb_00645157 -->|flow| bb_00645163
```
