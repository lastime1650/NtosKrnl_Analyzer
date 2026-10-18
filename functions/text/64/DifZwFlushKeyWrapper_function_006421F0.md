# DifZwFlushKeyWrapper

- RVA: `0x006421F0`–`0x0064234D` (길이 `349` bytes)
- VA: `0x00000001406421F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064221D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00642245` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00642273` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064229A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006422B3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006422BB` → [ZwFlushKey](../6A/ZwFlushKey_function_006AEF10.md) (function, `0x006AEF10`)
- `0x006422E8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064230F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00642328` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00642257` → RVA `0x00F048B8` (`.data`; read)
- `0x00642260` → RVA `0x00F04980` (`.data`; read)
- `0x0064226C` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006421F0  4C 8B DC                        mov r11, rsp
006421F3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006421F7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006421FB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006421FF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00642203  41 56                           push r14
00642205  48 83 EC 40                     sub rsp, 0x40
00642209  33 C0                           xor eax, eax
0064220B  0F 57 C0                        xorps xmm0, xmm0
0064220E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00642213  48 8B E9                        mov rbp, rcx
00642216  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0064221A  8D 48 63                        lea ecx, [rax + 0x63]
0064221D  E8 12 38 E5 FF                  call 0x140495a34
00642222  48 8B F0                        mov rsi, rax
00642225  48 85 C0                        test rax, rax
00642228  0F 84 8A 00 00 00               je 0x1406422b8
0064222E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00642231  A8 18                           test al, 0x18
00642233  74 0C                           je 0x140642241
00642235  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0064223A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0064223F  EB 0E                           jmp 0x14064224f
00642241  A8 04                           test al, 4
00642243  74 0A                           je 0x14064224f
00642245  E8 BE 19 E9 FF                  call 0x1404d3c08
0064224A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064224F  40 32 FF                        xor dil, dil
00642252  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00642257  40 38 3D 5A 26 8C 00            cmp byte ptr [rip + 0x8c265a], dil
0064225E  75 0C                           jne 0x14064226c
00642260  F7 05 16 27 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2716], 0x800
0064226A  74 13                           je 0x14064227f
0064226C  48 8D 0D 0D 1C 8C 00            lea rcx, [rip + 0x8c1c0d]
00642273  E8 A8 43 BD FF                  call 0x140216620
00642278  40 8A F8                        mov dil, al
0064227B  84 C0                           test al, al
0064227D  74 39                           je 0x1406422b8
0064227F  4C 8D 76 20                     lea r14, [rsi + 0x20]
00642283  49 8B 1E                        mov rbx, qword ptr [r14]
00642286  EB 1A                           jmp 0x1406422a2
00642288  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064228C  48 85 C0                        test rax, rax
0064228F  74 0E                           je 0x14064229f
00642291  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642295  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064229A  E8 31 88 07 00                  call 0x1406baad0
0064229F  48 8B 1B                        mov rbx, qword ptr [rbx]
006422A2  49 3B DE                        cmp rbx, r14
006422A5  75 E1                           jne 0x140642288
006422A7  40 84 FF                        test dil, dil
006422AA  74 0C                           je 0x1406422b8
006422AC  48 8D 0D CD 1B 8C 00            lea rcx, [rip + 0x8c1bcd]
006422B3  E8 C8 7B D0 FF                  call 0x140349e80
006422B8  48 8B CD                        mov rcx, rbp
006422BB  E8 50 CC 06 00                  call 0x1406aef10
006422C0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006422C4  48 85 F6                        test rsi, rsi
006422C7  74 64                           je 0x14064232d
006422C9  40 32 FF                        xor dil, dil
006422CC  40 38 3D E5 25 8C 00            cmp byte ptr [rip + 0x8c25e5], dil
006422D3  75 0C                           jne 0x1406422e1
006422D5  F7 05 A1 26 8C 00 00 08 00 00   test dword ptr [rip + 0x8c26a1], 0x800
006422DF  74 13                           je 0x1406422f4
006422E1  48 8D 0D 98 1B 8C 00            lea rcx, [rip + 0x8c1b98]
006422E8  E8 33 43 BD FF                  call 0x140216620
006422ED  40 8A F8                        mov dil, al
006422F0  84 C0                           test al, al
006422F2  74 39                           je 0x14064232d
006422F4  48 83 C6 30                     add rsi, 0x30
006422F8  48 8B 1E                        mov rbx, qword ptr [rsi]
006422FB  EB 1A                           jmp 0x140642317
006422FD  48 8D 43 F0                     lea rax, [rbx - 0x10]
00642301  48 85 C0                        test rax, rax
00642304  74 0E                           je 0x140642314
00642306  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064230A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064230F  E8 BC 87 07 00                  call 0x1406baad0
00642314  48 8B 1B                        mov rbx, qword ptr [rbx]
00642317  48 3B DE                        cmp rbx, rsi
0064231A  75 E1                           jne 0x1406422fd
0064231C  40 84 FF                        test dil, dil
0064231F  74 0C                           je 0x14064232d
00642321  48 8D 0D 58 1B 8C 00            lea rcx, [rip + 0x8c1b58]
00642328  E8 53 7B D0 FF                  call 0x140349e80
0064232D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00642331  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00642336  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0064233B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00642340  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00642345  48 83 C4 40                     add rsp, 0x40
00642349  41 5E                           pop r14
0064234B  C3                              ret
0064234C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFlushKeyWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(result + 99, a2, a3, a4);
    if (result == 0) goto loc_006422B8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00642241;
    v_stack_m28 = v_stack_p0;
    goto loc_0064224F;
loc_00642241:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9184858)) != 0) goto loc_0064226C;
    if (((*(unsigned int *)(v_rip + 9185046)) & (0x800ULL)) == 0) goto loc_0064227F;
loc_0064226C:
    result = ExAcquireRundownProtection(v_rip + 9182221, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006422B8;
loc_0064227F:
    goto loc_006422A2;
loc_00642288:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006422A2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00642288;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182157;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwFlushKey(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0064232D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9184741)) != 0) goto loc_006422E1;
    if (((*(unsigned int *)(v_rip + 9184929)) & (0x800ULL)) == 0) goto loc_006422F4;
loc_006422E1:
    result = ExAcquireRundownProtection(v_rip + 9182104, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064232D;
loc_006422F4:
    v_rsi = (result) + (48);
    goto loc_00642317;
loc_006422FD:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00642317:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006422FD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182040;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFlushKeyWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(result + 99, a2, a3, a4);
    if (result == 0) goto loc_006422B8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00642241;
    v_stack_m28 = v_stack_p0;
    goto loc_0064224F;
loc_00642241:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C265A)) != 0) goto loc_0064226C;
    if (((*(uint32_t *)(v_rip + 0x8C2716)) & (0x800ULL)) == 0) goto loc_0064227F;
loc_0064226C:
    result = ExAcquireRundownProtection(v_rip + 9182221, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006422B8;
loc_0064227F:
    goto loc_006422A2;
loc_00642288:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006422A2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00642288;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182157;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwFlushKey(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0064232D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C25E5)) != 0) goto loc_006422E1;
    if (((*(uint32_t *)(v_rip + 0x8C26A1)) & (0x800ULL)) == 0) goto loc_006422F4;
loc_006422E1:
    result = ExAcquireRundownProtection(v_rip + 9182104, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064232D;
loc_006422F4:
    local_rsi = (result) + (48);
    goto loc_00642317;
loc_006422FD:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00642317:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006422FD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182040;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006421F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006421F0[BB_006421F0]
  bb_0064222E[BB_0064222E]
  bb_00642235[BB_00642235]
  bb_00642241[BB_00642241]
  bb_00642245[BB_00642245]
  bb_0064224F[BB_0064224F]
  bb_00642260[BB_00642260]
  bb_0064226C[BB_0064226C]
  bb_0064227F[BB_0064227F]
  bb_00642288[BB_00642288]
  bb_00642291[BB_00642291]
  bb_0064229F[BB_0064229F]
  bb_006422A2[BB_006422A2]
  bb_006422A7[BB_006422A7]
  bb_006422AC[BB_006422AC]
  bb_006422B8[BB_006422B8]
  bb_006422C9[BB_006422C9]
  bb_006422D5[BB_006422D5]
  bb_006422E1[BB_006422E1]
  bb_006422F4[BB_006422F4]
  bb_006422FD[BB_006422FD]
  bb_00642306[BB_00642306]
  bb_00642314[BB_00642314]
  bb_00642317[BB_00642317]
  bb_0064231C[BB_0064231C]
  bb_00642321[BB_00642321]
  bb_0064232D[BB_0064232D]
  bb_0064234C[BB_0064234C]
  bb_006421F0 -->|branch| bb_006422B8
  bb_006421F0 -->|fallthrough| bb_0064222E
  bb_0064222E -->|branch| bb_00642241
  bb_0064222E -->|fallthrough| bb_00642235
  bb_00642235 -->|branch| bb_0064224F
  bb_00642241 -->|branch| bb_0064224F
  bb_00642241 -->|fallthrough| bb_00642245
  bb_00642245 -->|flow| bb_0064224F
  bb_0064224F -->|branch| bb_0064226C
  bb_0064224F -->|fallthrough| bb_00642260
  bb_00642260 -->|branch| bb_0064227F
  bb_00642260 -->|fallthrough| bb_0064226C
  bb_0064226C -->|branch| bb_006422B8
  bb_0064226C -->|fallthrough| bb_0064227F
  bb_0064227F -->|branch| bb_006422A2
  bb_00642288 -->|branch| bb_0064229F
  bb_00642288 -->|fallthrough| bb_00642291
  bb_00642291 -->|flow| bb_0064229F
  bb_0064229F -->|flow| bb_006422A2
  bb_006422A2 -->|branch| bb_00642288
  bb_006422A2 -->|fallthrough| bb_006422A7
  bb_006422A7 -->|branch| bb_006422B8
  bb_006422A7 -->|fallthrough| bb_006422AC
  bb_006422AC -->|flow| bb_006422B8
  bb_006422B8 -->|branch| bb_0064232D
  bb_006422B8 -->|fallthrough| bb_006422C9
  bb_006422C9 -->|branch| bb_006422E1
  bb_006422C9 -->|fallthrough| bb_006422D5
  bb_006422D5 -->|branch| bb_006422F4
  bb_006422D5 -->|fallthrough| bb_006422E1
  bb_006422E1 -->|branch| bb_0064232D
  bb_006422E1 -->|fallthrough| bb_006422F4
  bb_006422F4 -->|branch| bb_00642317
  bb_006422FD -->|branch| bb_00642314
  bb_006422FD -->|fallthrough| bb_00642306
  bb_00642306 -->|flow| bb_00642314
  bb_00642314 -->|flow| bb_00642317
  bb_00642317 -->|branch| bb_006422FD
  bb_00642317 -->|fallthrough| bb_0064231C
  bb_0064231C -->|branch| bb_0064232D
  bb_0064231C -->|fallthrough| bb_00642321
  bb_00642321 -->|flow| bb_0064232D
```
