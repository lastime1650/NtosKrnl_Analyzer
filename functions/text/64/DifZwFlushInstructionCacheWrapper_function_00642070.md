# DifZwFlushInstructionCacheWrapper

- RVA: `0x00642070`–`0x006421E5` (길이 `373` bytes)
- VA: `0x0000000140642070`
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
- `0x006420AC` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006420D2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00642106` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064212C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00642145` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00642153` → [ZwFlushInstructionCache](../6A/ZwFlushInstructionCache_function_006AEEF0.md) (function, `0x006AEEF0`)
- `0x0064217F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006421A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006421BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006420E2` → RVA `0x00F048B8` (`.data`; read)
- `0x006420F3` → RVA `0x00F04980` (`.data`; read)
- `0x006420FF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00642070  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00642075  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064207A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064207F  55                              push rbp
00642080  41 54                           push r12
00642082  41 55                           push r13
00642084  41 56                           push r14
00642086  41 57                           push r15
00642088  48 8B EC                        mov rbp, rsp
0064208B  48 83 EC 50                     sub rsp, 0x50
0064208F  33 C0                           xor eax, eax
00642091  0F 57 C0                        xorps xmm0, xmm0
00642094  4C 8B E9                        mov r13, rcx
00642097  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064209B  4D 8B F8                        mov r15, r8
0064209E  4C 8B E2                        mov r12, rdx
006420A1  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006420A5  8D 48 64                        lea ecx, [rax + 0x64]
006420A8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006420AC  E8 83 39 E5 FF                  call 0x140495a34
006420B1  48 8B F0                        mov rsi, rax
006420B4  48 85 C0                        test rax, rax
006420B7  0F 84 8D 00 00 00               je 0x14064214a
006420BD  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006420C0  A8 18                           test al, 0x18
006420C2  74 0A                           je 0x1406420ce
006420C4  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006420C8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006420CC  EB 0D                           jmp 0x1406420db
006420CE  A8 04                           test al, 4
006420D0  74 09                           je 0x1406420db
006420D2  E8 31 1B E9 FF                  call 0x1404d3c08
006420D7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006420DB  45 32 F6                        xor r14b, r14b
006420DE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
006420E2  44 38 35 CF 27 8C 00            cmp byte ptr [rip + 0x8c27cf], r14b
006420E9  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
006420ED  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
006420F1  75 0C                           jne 0x1406420ff
006420F3  F7 05 83 28 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2883], 0x800
006420FD  74 13                           je 0x140642112
006420FF  48 8D 0D 7A 1D 8C 00            lea rcx, [rip + 0x8c1d7a]
00642106  E8 15 45 BD FF                  call 0x140216620
0064210B  44 8A F0                        mov r14b, al
0064210E  84 C0                           test al, al
00642110  74 38                           je 0x14064214a
00642112  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00642116  48 8B 1F                        mov rbx, qword ptr [rdi]
00642119  EB 19                           jmp 0x140642134
0064211B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064211F  48 85 C0                        test rax, rax
00642122  74 0D                           je 0x140642131
00642124  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642128  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064212C  E8 9F 89 07 00                  call 0x1406baad0
00642131  48 8B 1B                        mov rbx, qword ptr [rbx]
00642134  48 3B DF                        cmp rbx, rdi
00642137  75 E2                           jne 0x14064211b
00642139  45 84 F6                        test r14b, r14b
0064213C  74 0C                           je 0x14064214a
0064213E  48 8D 0D 3B 1D 8C 00            lea rcx, [rip + 0x8c1d3b]
00642145  E8 36 7D D0 FF                  call 0x140349e80
0064214A  4D 8B C7                        mov r8, r15
0064214D  49 8B D4                        mov rdx, r12
00642150  49 8B CD                        mov rcx, r13
00642153  E8 98 CD 06 00                  call 0x1406aeef0
00642158  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064215B  48 85 F6                        test rsi, rsi
0064215E  74 63                           je 0x1406421c3
00642160  40 32 FF                        xor dil, dil
00642163  40 38 3D 4E 27 8C 00            cmp byte ptr [rip + 0x8c274e], dil
0064216A  75 0C                           jne 0x140642178
0064216C  F7 05 0A 28 8C 00 00 08 00 00   test dword ptr [rip + 0x8c280a], 0x800
00642176  74 13                           je 0x14064218b
00642178  48 8D 0D 01 1D 8C 00            lea rcx, [rip + 0x8c1d01]
0064217F  E8 9C 44 BD FF                  call 0x140216620
00642184  40 8A F8                        mov dil, al
00642187  84 C0                           test al, al
00642189  74 38                           je 0x1406421c3
0064218B  48 83 C6 30                     add rsi, 0x30
0064218F  48 8B 1E                        mov rbx, qword ptr [rsi]
00642192  EB 19                           jmp 0x1406421ad
00642194  48 8D 43 F0                     lea rax, [rbx - 0x10]
00642198  48 85 C0                        test rax, rax
0064219B  74 0D                           je 0x1406421aa
0064219D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006421A1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006421A5  E8 26 89 07 00                  call 0x1406baad0
006421AA  48 8B 1B                        mov rbx, qword ptr [rbx]
006421AD  48 3B DE                        cmp rbx, rsi
006421B0  75 E2                           jne 0x140642194
006421B2  40 84 FF                        test dil, dil
006421B5  74 0C                           je 0x1406421c3
006421B7  48 8D 0D C2 1C 8C 00            lea rcx, [rip + 0x8c1cc2]
006421BE  E8 BD 7C D0 FF                  call 0x140349e80
006421C3  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006421C6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006421CB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006421CF  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
006421D3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
006421D7  49 8B E3                        mov rsp, r11
006421DA  41 5F                           pop r15
006421DC  41 5E                           pop r14
006421DE  41 5D                           pop r13
006421E0  41 5C                           pop r12
006421E2  5D                              pop rbp
006421E3  C3                              ret
006421E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFlushInstructionCacheWrapper(__int64 a1, __int64 a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 100, a2, a3, a4);
    if (result == 0) goto loc_0064214A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006420CE;
    v_stack_m58 = v_stack_p0;
    goto loc_006420DB;
loc_006420CE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9185231)) != 0) goto loc_006420FF;
    if (((*(unsigned int *)(v_rip + 9185411)) & (0x800ULL)) == 0) goto loc_00642112;
loc_006420FF:
    result = ExAcquireRundownProtection(v_rip + 9182586, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064214A;
loc_00642112:
    goto loc_00642134;
loc_0064211B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00642134:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064211B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182523;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwFlushInstructionCache(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006421C3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9185102)) != 0) goto loc_00642178;
    if (((*(unsigned int *)(v_rip + 9185290)) & (0x800ULL)) == 0) goto loc_0064218B;
loc_00642178:
    result = ExAcquireRundownProtection(v_rip + 9182465, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006421C3;
loc_0064218B:
    v_rsi = (result) + (48);
    goto loc_006421AD;
loc_00642194:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006421AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00642194;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182402;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFlushInstructionCacheWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 100, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064214A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006420CE;
    v_stack_m58 = v_stack_p0;
    goto loc_006420DB;
loc_006420CE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C27CF)) != 0) goto loc_006420FF;
    if (((*(uint32_t *)(v_rip + 0x8C2883)) & (0x800ULL)) == 0) goto loc_00642112;
loc_006420FF:
    result = ExAcquireRundownProtection(v_rip + 9182586, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064214A;
loc_00642112:
    goto loc_00642134;
loc_0064211B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00642134:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064211B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182523;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwFlushInstructionCache(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006421C3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C274E)) != 0) goto loc_00642178;
    if (((*(uint32_t *)(v_rip + 0x8C280A)) & (0x800ULL)) == 0) goto loc_0064218B;
loc_00642178:
    result = ExAcquireRundownProtection(v_rip + 9182465, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006421C3;
loc_0064218B:
    local_rsi = (result) + (48);
    goto loc_006421AD;
loc_00642194:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006421AD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00642194;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182402;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00642070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00642070[BB_00642070]
  bb_006420BD[BB_006420BD]
  bb_006420C4[BB_006420C4]
  bb_006420CE[BB_006420CE]
  bb_006420D2[BB_006420D2]
  bb_006420DB[BB_006420DB]
  bb_006420F3[BB_006420F3]
  bb_006420FF[BB_006420FF]
  bb_00642112[BB_00642112]
  bb_0064211B[BB_0064211B]
  bb_00642124[BB_00642124]
  bb_00642131[BB_00642131]
  bb_00642134[BB_00642134]
  bb_00642139[BB_00642139]
  bb_0064213E[BB_0064213E]
  bb_0064214A[BB_0064214A]
  bb_00642160[BB_00642160]
  bb_0064216C[BB_0064216C]
  bb_00642178[BB_00642178]
  bb_0064218B[BB_0064218B]
  bb_00642194[BB_00642194]
  bb_0064219D[BB_0064219D]
  bb_006421AA[BB_006421AA]
  bb_006421AD[BB_006421AD]
  bb_006421B2[BB_006421B2]
  bb_006421B7[BB_006421B7]
  bb_006421C3[BB_006421C3]
  bb_006421E4[BB_006421E4]
  bb_00642070 -->|branch| bb_0064214A
  bb_00642070 -->|fallthrough| bb_006420BD
  bb_006420BD -->|branch| bb_006420CE
  bb_006420BD -->|fallthrough| bb_006420C4
  bb_006420C4 -->|branch| bb_006420DB
  bb_006420CE -->|branch| bb_006420DB
  bb_006420CE -->|fallthrough| bb_006420D2
  bb_006420D2 -->|flow| bb_006420DB
  bb_006420DB -->|branch| bb_006420FF
  bb_006420DB -->|fallthrough| bb_006420F3
  bb_006420F3 -->|branch| bb_00642112
  bb_006420F3 -->|fallthrough| bb_006420FF
  bb_006420FF -->|branch| bb_0064214A
  bb_006420FF -->|fallthrough| bb_00642112
  bb_00642112 -->|branch| bb_00642134
  bb_0064211B -->|branch| bb_00642131
  bb_0064211B -->|fallthrough| bb_00642124
  bb_00642124 -->|flow| bb_00642131
  bb_00642131 -->|flow| bb_00642134
  bb_00642134 -->|branch| bb_0064211B
  bb_00642134 -->|fallthrough| bb_00642139
  bb_00642139 -->|branch| bb_0064214A
  bb_00642139 -->|fallthrough| bb_0064213E
  bb_0064213E -->|flow| bb_0064214A
  bb_0064214A -->|branch| bb_006421C3
  bb_0064214A -->|fallthrough| bb_00642160
  bb_00642160 -->|branch| bb_00642178
  bb_00642160 -->|fallthrough| bb_0064216C
  bb_0064216C -->|branch| bb_0064218B
  bb_0064216C -->|fallthrough| bb_00642178
  bb_00642178 -->|branch| bb_006421C3
  bb_00642178 -->|fallthrough| bb_0064218B
  bb_0064218B -->|branch| bb_006421AD
  bb_00642194 -->|branch| bb_006421AA
  bb_00642194 -->|fallthrough| bb_0064219D
  bb_0064219D -->|flow| bb_006421AA
  bb_006421AA -->|flow| bb_006421AD
  bb_006421AD -->|branch| bb_00642194
  bb_006421AD -->|fallthrough| bb_006421B2
  bb_006421B2 -->|branch| bb_006421C3
  bb_006421B2 -->|fallthrough| bb_006421B7
  bb_006421B7 -->|flow| bb_006421C3
```
