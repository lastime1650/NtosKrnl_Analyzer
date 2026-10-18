# DifRtlUpcaseUnicodeStringToCountedOemStringWrapper

- RVA: `0x0063CBD0`–`0x0063CD47` (길이 `375` bytes)
- VA: `0x000000014063CBD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063CC0E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063CC34` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063CC68` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CC8E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CCA7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063CCB5` → [RtlUpcaseUnicodeStringToCountedOemString](../../page/90/RtlUpcaseUnicodeStringToCountedOemString_function_0090E4D0.md) (function, `0x0090E4D0`)
- `0x0063CCE1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CD07` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CD20` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063CC44` → RVA `0x00F048B8` (`.data`; read)
- `0x0063CC55` → RVA `0x00F04980` (`.data`; read)
- `0x0063CC61` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063CCB5` → [RtlUpcaseUnicodeStringToCountedOemString](../../page/90/RtlUpcaseUnicodeStringToCountedOemString_function_0090E4D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063CBD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063CBD5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063CBDA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063CBDF  55                              push rbp
0063CBE0  41 54                           push r12
0063CBE2  41 55                           push r13
0063CBE4  41 56                           push r14
0063CBE6  41 57                           push r15
0063CBE8  48 8B EC                        mov rbp, rsp
0063CBEB  48 83 EC 50                     sub rsp, 0x50
0063CBEF  0F 57 C0                        xorps xmm0, xmm0
0063CBF2  33 C0                           xor eax, eax
0063CBF4  4C 8B E9                        mov r13, rcx
0063CBF7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063CBFB  B9 97 00 00 00                  mov ecx, 0x97
0063CC00  45 8A F8                        mov r15b, r8b
0063CC03  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063CC07  4C 8B E2                        mov r12, rdx
0063CC0A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063CC0E  E8 21 8E E5 FF                  call 0x140495a34
0063CC13  48 8B F0                        mov rsi, rax
0063CC16  48 85 C0                        test rax, rax
0063CC19  0F 84 8D 00 00 00               je 0x14063ccac
0063CC1F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063CC22  A8 18                           test al, 0x18
0063CC24  74 0A                           je 0x14063cc30
0063CC26  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063CC2A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063CC2E  EB 0D                           jmp 0x14063cc3d
0063CC30  A8 04                           test al, 4
0063CC32  74 09                           je 0x14063cc3d
0063CC34  E8 CF 6F E9 FF                  call 0x1404d3c08
0063CC39  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063CC3D  45 32 F6                        xor r14b, r14b
0063CC40  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063CC44  44 38 35 6D 7C 8C 00            cmp byte ptr [rip + 0x8c7c6d], r14b
0063CC4B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063CC4F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063CC53  75 0C                           jne 0x14063cc61
0063CC55  F7 05 21 7D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7d21], 0x800
0063CC5F  74 13                           je 0x14063cc74
0063CC61  48 8D 0D 18 72 8C 00            lea rcx, [rip + 0x8c7218]
0063CC68  E8 B3 99 BD FF                  call 0x140216620
0063CC6D  44 8A F0                        mov r14b, al
0063CC70  84 C0                           test al, al
0063CC72  74 38                           je 0x14063ccac
0063CC74  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063CC78  48 8B 1F                        mov rbx, qword ptr [rdi]
0063CC7B  EB 19                           jmp 0x14063cc96
0063CC7D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CC81  48 85 C0                        test rax, rax
0063CC84  74 0D                           je 0x14063cc93
0063CC86  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CC8A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CC8E  E8 3D DE 07 00                  call 0x1406baad0
0063CC93  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CC96  48 3B DF                        cmp rbx, rdi
0063CC99  75 E2                           jne 0x14063cc7d
0063CC9B  45 84 F6                        test r14b, r14b
0063CC9E  74 0C                           je 0x14063ccac
0063CCA0  48 8D 0D D9 71 8C 00            lea rcx, [rip + 0x8c71d9]
0063CCA7  E8 D4 D1 D0 FF                  call 0x140349e80
0063CCAC  45 8A C7                        mov r8b, r15b
0063CCAF  49 8B D4                        mov rdx, r12
0063CCB2  49 8B CD                        mov rcx, r13
0063CCB5  E8 16 18 2D 00                  call 0x14090e4d0
0063CCBA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063CCBD  48 85 F6                        test rsi, rsi
0063CCC0  74 63                           je 0x14063cd25
0063CCC2  40 32 FF                        xor dil, dil
0063CCC5  40 38 3D EC 7B 8C 00            cmp byte ptr [rip + 0x8c7bec], dil
0063CCCC  75 0C                           jne 0x14063ccda
0063CCCE  F7 05 A8 7C 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7ca8], 0x800
0063CCD8  74 13                           je 0x14063cced
0063CCDA  48 8D 0D 9F 71 8C 00            lea rcx, [rip + 0x8c719f]
0063CCE1  E8 3A 99 BD FF                  call 0x140216620
0063CCE6  40 8A F8                        mov dil, al
0063CCE9  84 C0                           test al, al
0063CCEB  74 38                           je 0x14063cd25
0063CCED  48 83 C6 30                     add rsi, 0x30
0063CCF1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063CCF4  EB 19                           jmp 0x14063cd0f
0063CCF6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CCFA  48 85 C0                        test rax, rax
0063CCFD  74 0D                           je 0x14063cd0c
0063CCFF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CD03  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CD07  E8 C4 DD 07 00                  call 0x1406baad0
0063CD0C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CD0F  48 3B DE                        cmp rbx, rsi
0063CD12  75 E2                           jne 0x14063ccf6
0063CD14  40 84 FF                        test dil, dil
0063CD17  74 0C                           je 0x14063cd25
0063CD19  48 8D 0D 60 71 8C 00            lea rcx, [rip + 0x8c7160]
0063CD20  E8 5B D1 D0 FF                  call 0x140349e80
0063CD25  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063CD28  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063CD2D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063CD31  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063CD35  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063CD39  49 8B E3                        mov rsp, r11
0063CD3C  41 5F                           pop r15
0063CD3E  41 5E                           pop r14
0063CD40  41 5D                           pop r13
0063CD42  41 5C                           pop r12
0063CD44  5D                              pop rbp
0063CD45  C3                              ret
0063CD46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlUpcaseUnicodeStringToCountedOemStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    unsigned __int8 v_stack_m50;
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
    result = DifGetAPIThunkContextById(151, a2, a3, a4);
    if (result == 0) goto loc_0063CCAC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063CC30;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CC3D;
loc_0063CC30:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9206893)) != 0) goto loc_0063CC61;
    if (((*(unsigned int *)(v_rip + 9207073)) & (0x800ULL)) == 0) goto loc_0063CC74;
loc_0063CC61:
    result = ExAcquireRundownProtection(v_rip + 9204248, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CCAC;
loc_0063CC74:
    goto loc_0063CC96;
loc_0063CC7D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CC96:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063CC7D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204185;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlUpcaseUnicodeStringToCountedOemString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063CD25;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9206764)) != 0) goto loc_0063CCDA;
    if (((*(unsigned int *)(v_rip + 9206952)) & (0x800ULL)) == 0) goto loc_0063CCED;
loc_0063CCDA:
    result = ExAcquireRundownProtection(v_rip + 9204127, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CD25;
loc_0063CCED:
    v_rsi = (result) + (48);
    goto loc_0063CD0F;
loc_0063CCF6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CD0F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063CCF6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204064;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlUpcaseUnicodeStringToCountedOemStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    uint8_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(151, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063CCAC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063CC30;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CC3D;
loc_0063CC30:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C7C6D)) != 0) goto loc_0063CC61;
    if (((*(uint32_t *)(v_rip + 0x8C7D21)) & (0x800ULL)) == 0) goto loc_0063CC74;
loc_0063CC61:
    result = ExAcquireRundownProtection(v_rip + 9204248, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CCAC;
loc_0063CC74:
    goto loc_0063CC96;
loc_0063CC7D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CC96:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063CC7D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204185;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlUpcaseUnicodeStringToCountedOemString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063CD25;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C7BEC)) != 0) goto loc_0063CCDA;
    if (((*(uint32_t *)(v_rip + 0x8C7CA8)) & (0x800ULL)) == 0) goto loc_0063CCED;
loc_0063CCDA:
    result = ExAcquireRundownProtection(v_rip + 9204127, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CD25;
loc_0063CCED:
    local_rsi = (result) + (48);
    goto loc_0063CD0F;
loc_0063CCF6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CD0F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063CCF6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204064;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063CBD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063CBD0[BB_0063CBD0]
  bb_0063CC1F[BB_0063CC1F]
  bb_0063CC26[BB_0063CC26]
  bb_0063CC30[BB_0063CC30]
  bb_0063CC34[BB_0063CC34]
  bb_0063CC3D[BB_0063CC3D]
  bb_0063CC55[BB_0063CC55]
  bb_0063CC61[BB_0063CC61]
  bb_0063CC74[BB_0063CC74]
  bb_0063CC7D[BB_0063CC7D]
  bb_0063CC86[BB_0063CC86]
  bb_0063CC93[BB_0063CC93]
  bb_0063CC96[BB_0063CC96]
  bb_0063CC9B[BB_0063CC9B]
  bb_0063CCA0[BB_0063CCA0]
  bb_0063CCAC[BB_0063CCAC]
  bb_0063CCC2[BB_0063CCC2]
  bb_0063CCCE[BB_0063CCCE]
  bb_0063CCDA[BB_0063CCDA]
  bb_0063CCED[BB_0063CCED]
  bb_0063CCF6[BB_0063CCF6]
  bb_0063CCFF[BB_0063CCFF]
  bb_0063CD0C[BB_0063CD0C]
  bb_0063CD0F[BB_0063CD0F]
  bb_0063CD14[BB_0063CD14]
  bb_0063CD19[BB_0063CD19]
  bb_0063CD25[BB_0063CD25]
  bb_0063CD46[BB_0063CD46]
  bb_0063CBD0 -->|branch| bb_0063CCAC
  bb_0063CBD0 -->|fallthrough| bb_0063CC1F
  bb_0063CC1F -->|branch| bb_0063CC30
  bb_0063CC1F -->|fallthrough| bb_0063CC26
  bb_0063CC26 -->|branch| bb_0063CC3D
  bb_0063CC30 -->|branch| bb_0063CC3D
  bb_0063CC30 -->|fallthrough| bb_0063CC34
  bb_0063CC34 -->|flow| bb_0063CC3D
  bb_0063CC3D -->|branch| bb_0063CC61
  bb_0063CC3D -->|fallthrough| bb_0063CC55
  bb_0063CC55 -->|branch| bb_0063CC74
  bb_0063CC55 -->|fallthrough| bb_0063CC61
  bb_0063CC61 -->|branch| bb_0063CCAC
  bb_0063CC61 -->|fallthrough| bb_0063CC74
  bb_0063CC74 -->|branch| bb_0063CC96
  bb_0063CC7D -->|branch| bb_0063CC93
  bb_0063CC7D -->|fallthrough| bb_0063CC86
  bb_0063CC86 -->|flow| bb_0063CC93
  bb_0063CC93 -->|flow| bb_0063CC96
  bb_0063CC96 -->|branch| bb_0063CC7D
  bb_0063CC96 -->|fallthrough| bb_0063CC9B
  bb_0063CC9B -->|branch| bb_0063CCAC
  bb_0063CC9B -->|fallthrough| bb_0063CCA0
  bb_0063CCA0 -->|flow| bb_0063CCAC
  bb_0063CCAC -->|branch| bb_0063CD25
  bb_0063CCAC -->|fallthrough| bb_0063CCC2
  bb_0063CCC2 -->|branch| bb_0063CCDA
  bb_0063CCC2 -->|fallthrough| bb_0063CCCE
  bb_0063CCCE -->|branch| bb_0063CCED
  bb_0063CCCE -->|fallthrough| bb_0063CCDA
  bb_0063CCDA -->|branch| bb_0063CD25
  bb_0063CCDA -->|fallthrough| bb_0063CCED
  bb_0063CCED -->|branch| bb_0063CD0F
  bb_0063CCF6 -->|branch| bb_0063CD0C
  bb_0063CCF6 -->|fallthrough| bb_0063CCFF
  bb_0063CCFF -->|flow| bb_0063CD0C
  bb_0063CD0C -->|flow| bb_0063CD0F
  bb_0063CD0F -->|branch| bb_0063CCF6
  bb_0063CD0F -->|fallthrough| bb_0063CD14
  bb_0063CD14 -->|branch| bb_0063CD25
  bb_0063CD14 -->|fallthrough| bb_0063CD19
  bb_0063CD19 -->|flow| bb_0063CD25
```
