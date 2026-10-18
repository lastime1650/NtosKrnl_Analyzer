# DifMmUnsecureVirtualMemoryWrapper

- RVA: `0x00637100`–`0x00637250` (길이 `336` bytes)
- VA: `0x0000000140637100`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00637128` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00637150` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063717E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006371A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006371BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006371C6` → [MmUnsecureVirtualMemory](../../page/88/MmUnsecureVirtualMemory_function_0088A2A0.md) (function, `0x0088A2A0`)
- `0x006371EF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637216` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063722F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00637162` → RVA `0x00F048B8` (`.data`; read)
- `0x0063716B` → RVA `0x00F04980` (`.data`; read)
- `0x00637177` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006371C6` → [MmUnsecureVirtualMemory](../../page/88/MmUnsecureVirtualMemory_function_0088A2A0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00637100  48 8B C4                        mov rax, rsp
00637103  48 89 58 08                     mov qword ptr [rax + 8], rbx
00637107  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063710B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063710F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00637113  41 56                           push r14
00637115  48 83 EC 30                     sub rsp, 0x30
00637119  48 8B E9                        mov rbp, rcx
0063711C  0F 57 C0                        xorps xmm0, xmm0
0063711F  B9 D1 00 00 00                  mov ecx, 0xd1
00637124  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00637128  E8 07 E9 E5 FF                  call 0x140495a34
0063712D  48 8B F8                        mov rdi, rax
00637130  48 85 C0                        test rax, rax
00637133  0F 84 8A 00 00 00               je 0x1406371c3
00637139  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063713C  A8 18                           test al, 0x18
0063713E  74 0C                           je 0x14063714c
00637140  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00637145  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063714A  EB 0E                           jmp 0x14063715a
0063714C  A8 04                           test al, 4
0063714E  74 0A                           je 0x14063715a
00637150  E8 B3 CA E9 FF                  call 0x1404d3c08
00637155  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063715A  40 32 F6                        xor sil, sil
0063715D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00637162  40 38 35 4F D7 8C 00            cmp byte ptr [rip + 0x8cd74f], sil
00637169  75 0C                           jne 0x140637177
0063716B  F7 05 0B D8 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd80b], 0x800
00637175  74 13                           je 0x14063718a
00637177  48 8D 0D 02 CD 8C 00            lea rcx, [rip + 0x8ccd02]
0063717E  E8 9D F4 BD FF                  call 0x140216620
00637183  40 8A F0                        mov sil, al
00637186  84 C0                           test al, al
00637188  74 39                           je 0x1406371c3
0063718A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0063718E  49 8B 1E                        mov rbx, qword ptr [r14]
00637191  EB 1A                           jmp 0x1406371ad
00637193  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637197  48 85 C0                        test rax, rax
0063719A  74 0E                           je 0x1406371aa
0063719C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006371A0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006371A5  E8 26 39 08 00                  call 0x1406baad0
006371AA  48 8B 1B                        mov rbx, qword ptr [rbx]
006371AD  49 3B DE                        cmp rbx, r14
006371B0  75 E1                           jne 0x140637193
006371B2  40 84 F6                        test sil, sil
006371B5  74 0C                           je 0x1406371c3
006371B7  48 8D 0D C2 CC 8C 00            lea rcx, [rip + 0x8cccc2]
006371BE  E8 BD 2C D1 FF                  call 0x140349e80
006371C3  48 8B CD                        mov rcx, rbp
006371C6  E8 D5 30 25 00                  call 0x14088a2a0
006371CB  48 85 FF                        test rdi, rdi
006371CE  74 64                           je 0x140637234
006371D0  40 32 F6                        xor sil, sil
006371D3  40 38 35 DE D6 8C 00            cmp byte ptr [rip + 0x8cd6de], sil
006371DA  75 0C                           jne 0x1406371e8
006371DC  F7 05 9A D7 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd79a], 0x800
006371E6  74 13                           je 0x1406371fb
006371E8  48 8D 0D 91 CC 8C 00            lea rcx, [rip + 0x8ccc91]
006371EF  E8 2C F4 BD FF                  call 0x140216620
006371F4  40 8A F0                        mov sil, al
006371F7  84 C0                           test al, al
006371F9  74 39                           je 0x140637234
006371FB  48 83 C7 30                     add rdi, 0x30
006371FF  48 8B 1F                        mov rbx, qword ptr [rdi]
00637202  EB 1A                           jmp 0x14063721e
00637204  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637208  48 85 C0                        test rax, rax
0063720B  74 0E                           je 0x14063721b
0063720D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00637211  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00637216  E8 B5 38 08 00                  call 0x1406baad0
0063721B  48 8B 1B                        mov rbx, qword ptr [rbx]
0063721E  48 3B DF                        cmp rbx, rdi
00637221  75 E1                           jne 0x140637204
00637223  40 84 F6                        test sil, sil
00637226  74 0C                           je 0x140637234
00637228  48 8D 0D 51 CC 8C 00            lea rcx, [rip + 0x8ccc51]
0063722F  E8 4C 2C D1 FF                  call 0x140349e80
00637234  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00637239  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0063723E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00637243  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00637248  48 83 C4 30                     add rsp, 0x30
0063724C  41 5E                           pop r14
0063724E  C3                              ret
0063724F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmUnsecureVirtualMemoryWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(209, a2, a3, a4);
    if (result == 0) goto loc_006371C3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063714C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063715A;
loc_0063714C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9230159)) != 0) goto loc_00637177;
    if (((*(unsigned int *)(v_rip + 9230347)) & (0x800ULL)) == 0) goto loc_0063718A;
loc_00637177:
    result = ExAcquireRundownProtection(v_rip + 9227522, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006371C3;
loc_0063718A:
    goto loc_006371AD;
loc_00637193:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006371AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00637193;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9227458;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmUnsecureVirtualMemory(a1, a2, a3, a4);
    if (result == 0) goto loc_00637234;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9230046)) != 0) goto loc_006371E8;
    if (((*(unsigned int *)(v_rip + 9230234)) & (0x800ULL)) == 0) goto loc_006371FB;
loc_006371E8:
    result = ExAcquireRundownProtection(v_rip + 9227409, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00637234;
loc_006371FB:
    v_rdi = (result) + (48);
    goto loc_0063721E;
loc_00637204:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063721E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00637204;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9227345;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmUnsecureVirtualMemoryWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(209, a2, a3, a4);
    if (result == 0) goto loc_006371C3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063714C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063715A;
loc_0063714C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CD74F)) != 0) goto loc_00637177;
    if (((*(uint32_t *)(v_rip + 0x8CD80B)) & (0x800ULL)) == 0) goto loc_0063718A;
loc_00637177:
    result = ExAcquireRundownProtection(v_rip + 9227522, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006371C3;
loc_0063718A:
    goto loc_006371AD;
loc_00637193:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006371AD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00637193;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9227458;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmUnsecureVirtualMemory(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00637234;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CD6DE)) != 0) goto loc_006371E8;
    if (((*(uint32_t *)(v_rip + 0x8CD79A)) & (0x800ULL)) == 0) goto loc_006371FB;
loc_006371E8:
    result = ExAcquireRundownProtection(v_rip + 9227409, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00637234;
loc_006371FB:
    local_rdi = (result) + (48);
    goto loc_0063721E;
loc_00637204:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063721E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00637204;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9227345;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00637100&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00637100[BB_00637100]
  bb_00637139[BB_00637139]
  bb_00637140[BB_00637140]
  bb_0063714C[BB_0063714C]
  bb_00637150[BB_00637150]
  bb_0063715A[BB_0063715A]
  bb_0063716B[BB_0063716B]
  bb_00637177[BB_00637177]
  bb_0063718A[BB_0063718A]
  bb_00637193[BB_00637193]
  bb_0063719C[BB_0063719C]
  bb_006371AA[BB_006371AA]
  bb_006371AD[BB_006371AD]
  bb_006371B2[BB_006371B2]
  bb_006371B7[BB_006371B7]
  bb_006371C3[BB_006371C3]
  bb_006371D0[BB_006371D0]
  bb_006371DC[BB_006371DC]
  bb_006371E8[BB_006371E8]
  bb_006371FB[BB_006371FB]
  bb_00637204[BB_00637204]
  bb_0063720D[BB_0063720D]
  bb_0063721B[BB_0063721B]
  bb_0063721E[BB_0063721E]
  bb_00637223[BB_00637223]
  bb_00637228[BB_00637228]
  bb_00637234[BB_00637234]
  bb_0063724F[BB_0063724F]
  bb_00637100 -->|branch| bb_006371C3
  bb_00637100 -->|fallthrough| bb_00637139
  bb_00637139 -->|branch| bb_0063714C
  bb_00637139 -->|fallthrough| bb_00637140
  bb_00637140 -->|branch| bb_0063715A
  bb_0063714C -->|branch| bb_0063715A
  bb_0063714C -->|fallthrough| bb_00637150
  bb_00637150 -->|flow| bb_0063715A
  bb_0063715A -->|branch| bb_00637177
  bb_0063715A -->|fallthrough| bb_0063716B
  bb_0063716B -->|branch| bb_0063718A
  bb_0063716B -->|fallthrough| bb_00637177
  bb_00637177 -->|branch| bb_006371C3
  bb_00637177 -->|fallthrough| bb_0063718A
  bb_0063718A -->|branch| bb_006371AD
  bb_00637193 -->|branch| bb_006371AA
  bb_00637193 -->|fallthrough| bb_0063719C
  bb_0063719C -->|flow| bb_006371AA
  bb_006371AA -->|flow| bb_006371AD
  bb_006371AD -->|branch| bb_00637193
  bb_006371AD -->|fallthrough| bb_006371B2
  bb_006371B2 -->|branch| bb_006371C3
  bb_006371B2 -->|fallthrough| bb_006371B7
  bb_006371B7 -->|flow| bb_006371C3
  bb_006371C3 -->|branch| bb_00637234
  bb_006371C3 -->|fallthrough| bb_006371D0
  bb_006371D0 -->|branch| bb_006371E8
  bb_006371D0 -->|fallthrough| bb_006371DC
  bb_006371DC -->|branch| bb_006371FB
  bb_006371DC -->|fallthrough| bb_006371E8
  bb_006371E8 -->|branch| bb_00637234
  bb_006371E8 -->|fallthrough| bb_006371FB
  bb_006371FB -->|branch| bb_0063721E
  bb_00637204 -->|branch| bb_0063721B
  bb_00637204 -->|fallthrough| bb_0063720D
  bb_0063720D -->|flow| bb_0063721B
  bb_0063721B -->|flow| bb_0063721E
  bb_0063721E -->|branch| bb_00637204
  bb_0063721E -->|fallthrough| bb_00637223
  bb_00637223 -->|branch| bb_00637234
  bb_00637223 -->|fallthrough| bb_00637228
  bb_00637228 -->|flow| bb_00637234
```
