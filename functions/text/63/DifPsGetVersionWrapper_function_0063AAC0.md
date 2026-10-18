# DifPsGetVersionWrapper

- RVA: `0x0063AAC0`–`0x0063AC45` (길이 `389` bytes)
- VA: `0x000000014063AAC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063AB00` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063AB26` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063AB62` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063AB88` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063ABA1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063ABB3` → [PsGetVersion](../49/PsGetVersion_function_00495AB0.md) (function, `0x00495AB0`)
- `0x0063ABDF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063AC05` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063AC1E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063AB36` → RVA `0x00F048B8` (`.data`; read)
- `0x0063AB4F` → RVA `0x00F04980` (`.data`; read)
- `0x0063AB5B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063AAC0  48 8B C4                        mov rax, rsp
0063AAC3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063AAC7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063AACB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063AACF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0063AAD3  55                              push rbp
0063AAD4  41 54                           push r12
0063AAD6  41 55                           push r13
0063AAD8  41 56                           push r14
0063AADA  41 57                           push r15
0063AADC  48 8B EC                        mov rbp, rsp
0063AADF  48 83 EC 50                     sub rsp, 0x50
0063AAE3  0F 57 C0                        xorps xmm0, xmm0
0063AAE6  B9 AE 00 00 00                  mov ecx, 0xae
0063AAEB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063AAEF  4D 8B F9                        mov r15, r9
0063AAF2  4D 8B E0                        mov r12, r8
0063AAF5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063AAF9  4C 8B EA                        mov r13, rdx
0063AAFC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0063AB00  E8 2F AF E5 FF                  call 0x140495a34
0063AB05  48 8B F0                        mov rsi, rax
0063AB08  48 85 C0                        test rax, rax
0063AB0B  0F 84 95 00 00 00               je 0x14063aba6
0063AB11  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063AB14  A8 18                           test al, 0x18
0063AB16  74 0A                           je 0x14063ab22
0063AB18  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063AB1C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063AB20  EB 0D                           jmp 0x14063ab2f
0063AB22  A8 04                           test al, 4
0063AB24  74 09                           je 0x14063ab2f
0063AB26  E8 DD 90 E9 FF                  call 0x1404d3c08
0063AB2B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063AB2F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063AB33  45 32 F6                        xor r14b, r14b
0063AB36  44 38 35 7B 9D 8C 00            cmp byte ptr [rip + 0x8c9d7b], r14b
0063AB3D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063AB41  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063AB45  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063AB49  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0063AB4D  75 0C                           jne 0x14063ab5b
0063AB4F  F7 05 27 9E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9e27], 0x800
0063AB59  74 13                           je 0x14063ab6e
0063AB5B  48 8D 0D 1E 93 8C 00            lea rcx, [rip + 0x8c931e]
0063AB62  E8 B9 BA BD FF                  call 0x140216620
0063AB67  44 8A F0                        mov r14b, al
0063AB6A  84 C0                           test al, al
0063AB6C  74 38                           je 0x14063aba6
0063AB6E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063AB72  48 8B 1F                        mov rbx, qword ptr [rdi]
0063AB75  EB 19                           jmp 0x14063ab90
0063AB77  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063AB7B  48 85 C0                        test rax, rax
0063AB7E  74 0D                           je 0x14063ab8d
0063AB80  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063AB84  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063AB88  E8 43 FF 07 00                  call 0x1406baad0
0063AB8D  48 8B 1B                        mov rbx, qword ptr [rbx]
0063AB90  48 3B DF                        cmp rbx, rdi
0063AB93  75 E2                           jne 0x14063ab77
0063AB95  45 84 F6                        test r14b, r14b
0063AB98  74 0C                           je 0x14063aba6
0063AB9A  48 8D 0D DF 92 8C 00            lea rcx, [rip + 0x8c92df]
0063ABA1  E8 DA F2 D0 FF                  call 0x140349e80
0063ABA6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063ABAA  4D 8B CF                        mov r9, r15
0063ABAD  4D 8B C4                        mov r8, r12
0063ABB0  49 8B D5                        mov rdx, r13
0063ABB3  E8 F8 AE E5 FF                  call 0x140495ab0
0063ABB8  88 45 F8                        mov byte ptr [rbp - 8], al
0063ABBB  48 85 F6                        test rsi, rsi
0063ABBE  74 63                           je 0x14063ac23
0063ABC0  40 32 FF                        xor dil, dil
0063ABC3  40 38 3D EE 9C 8C 00            cmp byte ptr [rip + 0x8c9cee], dil
0063ABCA  75 0C                           jne 0x14063abd8
0063ABCC  F7 05 AA 9D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9daa], 0x800
0063ABD6  74 13                           je 0x14063abeb
0063ABD8  48 8D 0D A1 92 8C 00            lea rcx, [rip + 0x8c92a1]
0063ABDF  E8 3C BA BD FF                  call 0x140216620
0063ABE4  40 8A F8                        mov dil, al
0063ABE7  84 C0                           test al, al
0063ABE9  74 38                           je 0x14063ac23
0063ABEB  48 83 C6 30                     add rsi, 0x30
0063ABEF  48 8B 1E                        mov rbx, qword ptr [rsi]
0063ABF2  EB 19                           jmp 0x14063ac0d
0063ABF4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063ABF8  48 85 C0                        test rax, rax
0063ABFB  74 0D                           je 0x14063ac0a
0063ABFD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063AC01  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063AC05  E8 C6 FE 07 00                  call 0x1406baad0
0063AC0A  48 8B 1B                        mov rbx, qword ptr [rbx]
0063AC0D  48 3B DE                        cmp rbx, rsi
0063AC10  75 E2                           jne 0x14063abf4
0063AC12  40 84 FF                        test dil, dil
0063AC15  74 0C                           je 0x14063ac23
0063AC17  48 8D 0D 62 92 8C 00            lea rcx, [rip + 0x8c9262]
0063AC1E  E8 5D F2 D0 FF                  call 0x140349e80
0063AC23  8A 45 F8                        mov al, byte ptr [rbp - 8]
0063AC26  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063AC2B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063AC2F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063AC33  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063AC37  49 8B E3                        mov rsp, r11
0063AC3A  41 5F                           pop r15
0063AC3C  41 5E                           pop r14
0063AC3E  41 5D                           pop r13
0063AC40  41 5C                           pop r12
0063AC42  5D                              pop rbp
0063AC43  C3                              ret
0063AC44  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPsGetVersionWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(174, a2, a3, a4);
    if (result == 0) goto loc_0063ABA6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063AB22;
    v_stack_m58 = v_stack_p0;
    goto loc_0063AB2F;
loc_0063AB22:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9215355)) != 0) goto loc_0063AB5B;
    if (((*(unsigned int *)(v_rip + 9215527)) & (0x800ULL)) == 0) goto loc_0063AB6E;
loc_0063AB5B:
    result = ExAcquireRundownProtection(v_rip + 9212702, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063ABA6;
loc_0063AB6E:
    goto loc_0063AB90;
loc_0063AB77:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063AB90:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063AB77;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9212639;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PsGetVersion(v_stack_p8, a2, a3, a4);
    v_stack_m30 = (unsigned __int8)(result);
    if (result == 0) goto loc_0063AC23;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9215214)) != 0) goto loc_0063ABD8;
    if (((*(unsigned int *)(v_rip + 9215402)) & (0x800ULL)) == 0) goto loc_0063ABEB;
loc_0063ABD8:
    result = ExAcquireRundownProtection(v_rip + 9212577, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063AC23;
loc_0063ABEB:
    v_rsi = (result) + (48);
    goto loc_0063AC0D;
loc_0063ABF4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063AC0D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063ABF4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9212514;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m30;
}
```

## 5. (Beta) C Style

```c
int64_t DifPsGetVersionWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(174, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063ABA6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063AB22;
    v_stack_m58 = v_stack_p0;
    goto loc_0063AB2F;
loc_0063AB22:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C9D7B)) != 0) goto loc_0063AB5B;
    if (((*(uint32_t *)(v_rip + 0x8C9E27)) & (0x800ULL)) == 0) goto loc_0063AB6E;
loc_0063AB5B:
    result = ExAcquireRundownProtection(v_rip + 9212702, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063ABA6;
loc_0063AB6E:
    goto loc_0063AB90;
loc_0063AB77:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063AB90:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063AB77;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9212639;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = PsGetVersion(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m30 = (uint8_t)(result);
    if (result == 0) goto loc_0063AC23;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C9CEE)) != 0) goto loc_0063ABD8;
    if (((*(uint32_t *)(v_rip + 0x8C9DAA)) & (0x800ULL)) == 0) goto loc_0063ABEB;
loc_0063ABD8:
    result = ExAcquireRundownProtection(v_rip + 9212577, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063AC23;
loc_0063ABEB:
    local_rsi = (result) + (48);
    goto loc_0063AC0D;
loc_0063ABF4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063AC0D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063ABF4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9212514;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return v_stack_m30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063AAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063AAC0[BB_0063AAC0]
  bb_0063AB11[BB_0063AB11]
  bb_0063AB18[BB_0063AB18]
  bb_0063AB22[BB_0063AB22]
  bb_0063AB26[BB_0063AB26]
  bb_0063AB2F[BB_0063AB2F]
  bb_0063AB4F[BB_0063AB4F]
  bb_0063AB5B[BB_0063AB5B]
  bb_0063AB6E[BB_0063AB6E]
  bb_0063AB77[BB_0063AB77]
  bb_0063AB80[BB_0063AB80]
  bb_0063AB8D[BB_0063AB8D]
  bb_0063AB90[BB_0063AB90]
  bb_0063AB95[BB_0063AB95]
  bb_0063AB9A[BB_0063AB9A]
  bb_0063ABA6[BB_0063ABA6]
  bb_0063ABC0[BB_0063ABC0]
  bb_0063ABCC[BB_0063ABCC]
  bb_0063ABD8[BB_0063ABD8]
  bb_0063ABEB[BB_0063ABEB]
  bb_0063ABF4[BB_0063ABF4]
  bb_0063ABFD[BB_0063ABFD]
  bb_0063AC0A[BB_0063AC0A]
  bb_0063AC0D[BB_0063AC0D]
  bb_0063AC12[BB_0063AC12]
  bb_0063AC17[BB_0063AC17]
  bb_0063AC23[BB_0063AC23]
  bb_0063AC44[BB_0063AC44]
  bb_0063AAC0 -->|branch| bb_0063ABA6
  bb_0063AAC0 -->|fallthrough| bb_0063AB11
  bb_0063AB11 -->|branch| bb_0063AB22
  bb_0063AB11 -->|fallthrough| bb_0063AB18
  bb_0063AB18 -->|branch| bb_0063AB2F
  bb_0063AB22 -->|branch| bb_0063AB2F
  bb_0063AB22 -->|fallthrough| bb_0063AB26
  bb_0063AB26 -->|flow| bb_0063AB2F
  bb_0063AB2F -->|branch| bb_0063AB5B
  bb_0063AB2F -->|fallthrough| bb_0063AB4F
  bb_0063AB4F -->|branch| bb_0063AB6E
  bb_0063AB4F -->|fallthrough| bb_0063AB5B
  bb_0063AB5B -->|branch| bb_0063ABA6
  bb_0063AB5B -->|fallthrough| bb_0063AB6E
  bb_0063AB6E -->|branch| bb_0063AB90
  bb_0063AB77 -->|branch| bb_0063AB8D
  bb_0063AB77 -->|fallthrough| bb_0063AB80
  bb_0063AB80 -->|flow| bb_0063AB8D
  bb_0063AB8D -->|flow| bb_0063AB90
  bb_0063AB90 -->|branch| bb_0063AB77
  bb_0063AB90 -->|fallthrough| bb_0063AB95
  bb_0063AB95 -->|branch| bb_0063ABA6
  bb_0063AB95 -->|fallthrough| bb_0063AB9A
  bb_0063AB9A -->|flow| bb_0063ABA6
  bb_0063ABA6 -->|branch| bb_0063AC23
  bb_0063ABA6 -->|fallthrough| bb_0063ABC0
  bb_0063ABC0 -->|branch| bb_0063ABD8
  bb_0063ABC0 -->|fallthrough| bb_0063ABCC
  bb_0063ABCC -->|branch| bb_0063ABEB
  bb_0063ABCC -->|fallthrough| bb_0063ABD8
  bb_0063ABD8 -->|branch| bb_0063AC23
  bb_0063ABD8 -->|fallthrough| bb_0063ABEB
  bb_0063ABEB -->|branch| bb_0063AC0D
  bb_0063ABF4 -->|branch| bb_0063AC0A
  bb_0063ABF4 -->|fallthrough| bb_0063ABFD
  bb_0063ABFD -->|flow| bb_0063AC0A
  bb_0063AC0A -->|flow| bb_0063AC0D
  bb_0063AC0D -->|branch| bb_0063ABF4
  bb_0063AC0D -->|fallthrough| bb_0063AC12
  bb_0063AC12 -->|branch| bb_0063AC23
  bb_0063AC12 -->|fallthrough| bb_0063AC17
  bb_0063AC17 -->|flow| bb_0063AC23
```
