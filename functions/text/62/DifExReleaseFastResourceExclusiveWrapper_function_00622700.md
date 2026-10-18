# DifExReleaseFastResourceExclusiveWrapper

- RVA: `0x00622700`–`0x0062285F` (길이 `351` bytes)
- VA: `0x0000000140622700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `97`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00622731` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00622759` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062278C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006227B3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006227CC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006227D7` → [ExReleaseFastResourceExclusive](../65/ExReleaseFastResourceExclusive_function_006588F0.md) (function, `0x006588F0`)
- `0x00622800` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00622827` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00622840` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062276B` → RVA `0x00F048B8` (`.data`; read)
- `0x00622779` → RVA `0x00F04980` (`.data`; read)
- `0x00622785` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00622700  4C 8B DC                        mov r11, rsp
00622703  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00622707  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062270B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062270F  57                              push rdi
00622710  41 56                           push r14
00622712  41 57                           push r15
00622714  48 83 EC 40                     sub rsp, 0x40
00622718  33 C0                           xor eax, eax
0062271A  0F 57 C0                        xorps xmm0, xmm0
0062271D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00622722  4C 8B F9                        mov r15, rcx
00622725  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00622729  B9 C3 01 00 00                  mov ecx, 0x1c3
0062272E  4C 8B F2                        mov r14, rdx
00622731  E8 FE 32 E7 FF                  call 0x140495a34
00622736  48 8B F0                        mov rsi, rax
00622739  48 85 C0                        test rax, rax
0062273C  0F 84 8F 00 00 00               je 0x1406227d1
00622742  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00622745  A8 18                           test al, 0x18
00622747  74 0C                           je 0x140622755
00622749  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062274E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00622753  EB 0E                           jmp 0x140622763
00622755  A8 04                           test al, 4
00622757  74 0A                           je 0x140622763
00622759  E8 AA 14 EB FF                  call 0x1404d3c08
0062275E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00622763  40 32 ED                        xor bpl, bpl
00622766  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062276B  40 38 2D 46 21 8E 00            cmp byte ptr [rip + 0x8e2146], bpl
00622772  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00622777  75 0C                           jne 0x140622785
00622779  F7 05 FD 21 8E 00 00 08 00 00   test dword ptr [rip + 0x8e21fd], 0x800
00622783  74 13                           je 0x140622798
00622785  48 8D 0D F4 16 8E 00            lea rcx, [rip + 0x8e16f4]
0062278C  E8 8F 3E BF FF                  call 0x140216620
00622791  40 8A E8                        mov bpl, al
00622794  84 C0                           test al, al
00622796  74 39                           je 0x1406227d1
00622798  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062279C  48 8B 1F                        mov rbx, qword ptr [rdi]
0062279F  EB 1A                           jmp 0x1406227bb
006227A1  48 8D 43 F0                     lea rax, [rbx - 0x10]
006227A5  48 85 C0                        test rax, rax
006227A8  74 0E                           je 0x1406227b8
006227AA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006227AE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006227B3  E8 18 83 09 00                  call 0x1406baad0
006227B8  48 8B 1B                        mov rbx, qword ptr [rbx]
006227BB  48 3B DF                        cmp rbx, rdi
006227BE  75 E1                           jne 0x1406227a1
006227C0  40 84 ED                        test bpl, bpl
006227C3  74 0C                           je 0x1406227d1
006227C5  48 8D 0D B4 16 8E 00            lea rcx, [rip + 0x8e16b4]
006227CC  E8 AF 76 D2 FF                  call 0x140349e80
006227D1  49 8B D6                        mov rdx, r14
006227D4  49 8B CF                        mov rcx, r15
006227D7  E8 14 61 03 00                  call 0x1406588f0
006227DC  48 85 F6                        test rsi, rsi
006227DF  74 64                           je 0x140622845
006227E1  40 32 FF                        xor dil, dil
006227E4  40 38 3D CD 20 8E 00            cmp byte ptr [rip + 0x8e20cd], dil
006227EB  75 0C                           jne 0x1406227f9
006227ED  F7 05 89 21 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2189], 0x800
006227F7  74 13                           je 0x14062280c
006227F9  48 8D 0D 80 16 8E 00            lea rcx, [rip + 0x8e1680]
00622800  E8 1B 3E BF FF                  call 0x140216620
00622805  40 8A F8                        mov dil, al
00622808  84 C0                           test al, al
0062280A  74 39                           je 0x140622845
0062280C  48 83 C6 30                     add rsi, 0x30
00622810  48 8B 1E                        mov rbx, qword ptr [rsi]
00622813  EB 1A                           jmp 0x14062282f
00622815  48 8D 43 F0                     lea rax, [rbx - 0x10]
00622819  48 85 C0                        test rax, rax
0062281C  74 0E                           je 0x14062282c
0062281E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00622822  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00622827  E8 A4 82 09 00                  call 0x1406baad0
0062282C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062282F  48 3B DE                        cmp rbx, rsi
00622832  75 E1                           jne 0x140622815
00622834  40 84 FF                        test dil, dil
00622837  74 0C                           je 0x140622845
00622839  48 8D 0D 40 16 8E 00            lea rcx, [rip + 0x8e1640]
00622840  E8 3B 76 D2 FF                  call 0x140349e80
00622845  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062284A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062284F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00622854  48 83 C4 40                     add rsp, 0x40
00622858  41 5F                           pop r15
0062285A  41 5E                           pop r14
0062285C  5F                              pop rdi
0062285D  C3                              ret
0062285E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExReleaseFastResourceExclusiveWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
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
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(451, a2, a3, a4);
    if (result == 0) goto loc_006227D1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00622755;
    v_stack_m38 = v_stack_p0;
    goto loc_00622763;
loc_00622755:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9314630)) != 0) goto loc_00622785;
    if (((*(unsigned int *)(v_rip + 9314813)) & (0x800ULL)) == 0) goto loc_00622798;
loc_00622785:
    result = ExAcquireRundownProtection(v_rip + 9311988, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006227D1;
loc_00622798:
    goto loc_006227BB;
loc_006227A1:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006227BB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006227A1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9311924;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExReleaseFastResourceExclusive(a1, a2, a3, a4);
    if (result == 0) goto loc_00622845;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9314509)) != 0) goto loc_006227F9;
    if (((*(unsigned int *)(v_rip + 9314697)) & (0x800ULL)) == 0) goto loc_0062280C;
loc_006227F9:
    result = ExAcquireRundownProtection(v_rip + 9311872, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00622845;
loc_0062280C:
    v_rsi = (result) + (48);
    goto loc_0062282F;
loc_00622815:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062282F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00622815;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9311808;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExReleaseFastResourceExclusiveWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
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
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(451, Arg2, a3, a4);
    if (result == 0) goto loc_006227D1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00622755;
    v_stack_m38 = v_stack_p0;
    goto loc_00622763;
loc_00622755:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8E2146)) != 0) goto loc_00622785;
    if (((*(uint32_t *)(v_rip + 0x8E21FD)) & (0x800ULL)) == 0) goto loc_00622798;
loc_00622785:
    result = ExAcquireRundownProtection(v_rip + 9311988, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006227D1;
loc_00622798:
    goto loc_006227BB;
loc_006227A1:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006227BB:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006227A1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9311924;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ExReleaseFastResourceExclusive(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_00622845;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E20CD)) != 0) goto loc_006227F9;
    if (((*(uint32_t *)(v_rip + 0x8E2189)) & (0x800ULL)) == 0) goto loc_0062280C;
loc_006227F9:
    result = ExAcquireRundownProtection(v_rip + 9311872, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00622845;
loc_0062280C:
    local_rsi = (result) + (48);
    goto loc_0062282F;
loc_00622815:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062282F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00622815;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9311808;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00622700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00622700[BB_00622700]
  bb_00622742[BB_00622742]
  bb_00622749[BB_00622749]
  bb_00622755[BB_00622755]
  bb_00622759[BB_00622759]
  bb_00622763[BB_00622763]
  bb_00622779[BB_00622779]
  bb_00622785[BB_00622785]
  bb_00622798[BB_00622798]
  bb_006227A1[BB_006227A1]
  bb_006227AA[BB_006227AA]
  bb_006227B8[BB_006227B8]
  bb_006227BB[BB_006227BB]
  bb_006227C0[BB_006227C0]
  bb_006227C5[BB_006227C5]
  bb_006227D1[BB_006227D1]
  bb_006227E1[BB_006227E1]
  bb_006227ED[BB_006227ED]
  bb_006227F9[BB_006227F9]
  bb_0062280C[BB_0062280C]
  bb_00622815[BB_00622815]
  bb_0062281E[BB_0062281E]
  bb_0062282C[BB_0062282C]
  bb_0062282F[BB_0062282F]
  bb_00622834[BB_00622834]
  bb_00622839[BB_00622839]
  bb_00622845[BB_00622845]
  bb_0062285E[BB_0062285E]
  bb_00622700 -->|branch| bb_006227D1
  bb_00622700 -->|fallthrough| bb_00622742
  bb_00622742 -->|branch| bb_00622755
  bb_00622742 -->|fallthrough| bb_00622749
  bb_00622749 -->|branch| bb_00622763
  bb_00622755 -->|branch| bb_00622763
  bb_00622755 -->|fallthrough| bb_00622759
  bb_00622759 -->|flow| bb_00622763
  bb_00622763 -->|branch| bb_00622785
  bb_00622763 -->|fallthrough| bb_00622779
  bb_00622779 -->|branch| bb_00622798
  bb_00622779 -->|fallthrough| bb_00622785
  bb_00622785 -->|branch| bb_006227D1
  bb_00622785 -->|fallthrough| bb_00622798
  bb_00622798 -->|branch| bb_006227BB
  bb_006227A1 -->|branch| bb_006227B8
  bb_006227A1 -->|fallthrough| bb_006227AA
  bb_006227AA -->|flow| bb_006227B8
  bb_006227B8 -->|flow| bb_006227BB
  bb_006227BB -->|branch| bb_006227A1
  bb_006227BB -->|fallthrough| bb_006227C0
  bb_006227C0 -->|branch| bb_006227D1
  bb_006227C0 -->|fallthrough| bb_006227C5
  bb_006227C5 -->|flow| bb_006227D1
  bb_006227D1 -->|branch| bb_00622845
  bb_006227D1 -->|fallthrough| bb_006227E1
  bb_006227E1 -->|branch| bb_006227F9
  bb_006227E1 -->|fallthrough| bb_006227ED
  bb_006227ED -->|branch| bb_0062280C
  bb_006227ED -->|fallthrough| bb_006227F9
  bb_006227F9 -->|branch| bb_00622845
  bb_006227F9 -->|fallthrough| bb_0062280C
  bb_0062280C -->|branch| bb_0062282F
  bb_00622815 -->|branch| bb_0062282C
  bb_00622815 -->|fallthrough| bb_0062281E
  bb_0062281E -->|flow| bb_0062282C
  bb_0062282C -->|flow| bb_0062282F
  bb_0062282F -->|branch| bb_00622815
  bb_0062282F -->|fallthrough| bb_00622834
  bb_00622834 -->|branch| bb_00622845
  bb_00622834 -->|fallthrough| bb_00622839
  bb_00622839 -->|flow| bb_00622845
```
