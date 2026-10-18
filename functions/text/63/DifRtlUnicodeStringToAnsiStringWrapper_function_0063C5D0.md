# DifRtlUnicodeStringToAnsiStringWrapper

- RVA: `0x0063C5D0`–`0x0063C747` (길이 `375` bytes)
- VA: `0x000000014063C5D0`
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
- `0x0063C60E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063C634` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063C668` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063C68E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063C6A7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063C6B5` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (function, `0x0090D1F0`)
- `0x0063C6E1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063C707` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063C720` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063C644` → RVA `0x00F048B8` (`.data`; read)
- `0x0063C655` → RVA `0x00F04980` (`.data`; read)
- `0x0063C661` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063C6B5` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063C5D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063C5D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063C5DA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063C5DF  55                              push rbp
0063C5E0  41 54                           push r12
0063C5E2  41 55                           push r13
0063C5E4  41 56                           push r14
0063C5E6  41 57                           push r15
0063C5E8  48 8B EC                        mov rbp, rsp
0063C5EB  48 83 EC 50                     sub rsp, 0x50
0063C5EF  0F 57 C0                        xorps xmm0, xmm0
0063C5F2  33 C0                           xor eax, eax
0063C5F4  4C 8B E9                        mov r13, rcx
0063C5F7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063C5FB  B9 9C 00 00 00                  mov ecx, 0x9c
0063C600  45 8A F8                        mov r15b, r8b
0063C603  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063C607  4C 8B E2                        mov r12, rdx
0063C60A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063C60E  E8 21 94 E5 FF                  call 0x140495a34
0063C613  48 8B F0                        mov rsi, rax
0063C616  48 85 C0                        test rax, rax
0063C619  0F 84 8D 00 00 00               je 0x14063c6ac
0063C61F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063C622  A8 18                           test al, 0x18
0063C624  74 0A                           je 0x14063c630
0063C626  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063C62A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063C62E  EB 0D                           jmp 0x14063c63d
0063C630  A8 04                           test al, 4
0063C632  74 09                           je 0x14063c63d
0063C634  E8 CF 75 E9 FF                  call 0x1404d3c08
0063C639  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063C63D  45 32 F6                        xor r14b, r14b
0063C640  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063C644  44 38 35 6D 82 8C 00            cmp byte ptr [rip + 0x8c826d], r14b
0063C64B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063C64F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063C653  75 0C                           jne 0x14063c661
0063C655  F7 05 21 83 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8321], 0x800
0063C65F  74 13                           je 0x14063c674
0063C661  48 8D 0D 18 78 8C 00            lea rcx, [rip + 0x8c7818]
0063C668  E8 B3 9F BD FF                  call 0x140216620
0063C66D  44 8A F0                        mov r14b, al
0063C670  84 C0                           test al, al
0063C672  74 38                           je 0x14063c6ac
0063C674  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063C678  48 8B 1F                        mov rbx, qword ptr [rdi]
0063C67B  EB 19                           jmp 0x14063c696
0063C67D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C681  48 85 C0                        test rax, rax
0063C684  74 0D                           je 0x14063c693
0063C686  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063C68A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063C68E  E8 3D E4 07 00                  call 0x1406baad0
0063C693  48 8B 1B                        mov rbx, qword ptr [rbx]
0063C696  48 3B DF                        cmp rbx, rdi
0063C699  75 E2                           jne 0x14063c67d
0063C69B  45 84 F6                        test r14b, r14b
0063C69E  74 0C                           je 0x14063c6ac
0063C6A0  48 8D 0D D9 77 8C 00            lea rcx, [rip + 0x8c77d9]
0063C6A7  E8 D4 D7 D0 FF                  call 0x140349e80
0063C6AC  45 8A C7                        mov r8b, r15b
0063C6AF  49 8B D4                        mov rdx, r12
0063C6B2  49 8B CD                        mov rcx, r13
0063C6B5  E8 36 0B 2D 00                  call 0x14090d1f0
0063C6BA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063C6BD  48 85 F6                        test rsi, rsi
0063C6C0  74 63                           je 0x14063c725
0063C6C2  40 32 FF                        xor dil, dil
0063C6C5  40 38 3D EC 81 8C 00            cmp byte ptr [rip + 0x8c81ec], dil
0063C6CC  75 0C                           jne 0x14063c6da
0063C6CE  F7 05 A8 82 8C 00 00 08 00 00   test dword ptr [rip + 0x8c82a8], 0x800
0063C6D8  74 13                           je 0x14063c6ed
0063C6DA  48 8D 0D 9F 77 8C 00            lea rcx, [rip + 0x8c779f]
0063C6E1  E8 3A 9F BD FF                  call 0x140216620
0063C6E6  40 8A F8                        mov dil, al
0063C6E9  84 C0                           test al, al
0063C6EB  74 38                           je 0x14063c725
0063C6ED  48 83 C6 30                     add rsi, 0x30
0063C6F1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063C6F4  EB 19                           jmp 0x14063c70f
0063C6F6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C6FA  48 85 C0                        test rax, rax
0063C6FD  74 0D                           je 0x14063c70c
0063C6FF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063C703  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063C707  E8 C4 E3 07 00                  call 0x1406baad0
0063C70C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063C70F  48 3B DE                        cmp rbx, rsi
0063C712  75 E2                           jne 0x14063c6f6
0063C714  40 84 FF                        test dil, dil
0063C717  74 0C                           je 0x14063c725
0063C719  48 8D 0D 60 77 8C 00            lea rcx, [rip + 0x8c7760]
0063C720  E8 5B D7 D0 FF                  call 0x140349e80
0063C725  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063C728  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063C72D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063C731  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063C735  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063C739  49 8B E3                        mov rsp, r11
0063C73C  41 5F                           pop r15
0063C73E  41 5E                           pop r14
0063C740  41 5D                           pop r13
0063C742  41 5C                           pop r12
0063C744  5D                              pop rbp
0063C745  C3                              ret
0063C746  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlUnicodeStringToAnsiStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    result = DifGetAPIThunkContextById(156, a2, a3, a4);
    if (result == 0) goto loc_0063C6AC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063C630;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C63D;
loc_0063C630:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9208429)) != 0) goto loc_0063C661;
    if (((*(unsigned int *)(v_rip + 9208609)) & (0x800ULL)) == 0) goto loc_0063C674;
loc_0063C661:
    result = ExAcquireRundownProtection(v_rip + 9205784, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063C6AC;
loc_0063C674:
    goto loc_0063C696;
loc_0063C67D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063C696:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063C67D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9205721;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlUnicodeStringToAnsiString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063C725;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9208300)) != 0) goto loc_0063C6DA;
    if (((*(unsigned int *)(v_rip + 9208488)) & (0x800ULL)) == 0) goto loc_0063C6ED;
loc_0063C6DA:
    result = ExAcquireRundownProtection(v_rip + 9205663, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063C725;
loc_0063C6ED:
    v_rsi = (result) + (48);
    goto loc_0063C70F;
loc_0063C6F6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063C70F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063C6F6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9205600;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlUnicodeStringToAnsiStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    result = DifGetAPIThunkContextById(156, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063C6AC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063C630;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C63D;
loc_0063C630:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C826D)) != 0) goto loc_0063C661;
    if (((*(uint32_t *)(v_rip + 0x8C8321)) & (0x800ULL)) == 0) goto loc_0063C674;
loc_0063C661:
    result = ExAcquireRundownProtection(v_rip + 9205784, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063C6AC;
loc_0063C674:
    goto loc_0063C696;
loc_0063C67D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063C696:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063C67D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9205721;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlUnicodeStringToAnsiString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063C725;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C81EC)) != 0) goto loc_0063C6DA;
    if (((*(uint32_t *)(v_rip + 0x8C82A8)) & (0x800ULL)) == 0) goto loc_0063C6ED;
loc_0063C6DA:
    result = ExAcquireRundownProtection(v_rip + 9205663, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063C725;
loc_0063C6ED:
    local_rsi = (result) + (48);
    goto loc_0063C70F;
loc_0063C6F6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063C70F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063C6F6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9205600;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063C5D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063C5D0[BB_0063C5D0]
  bb_0063C61F[BB_0063C61F]
  bb_0063C626[BB_0063C626]
  bb_0063C630[BB_0063C630]
  bb_0063C634[BB_0063C634]
  bb_0063C63D[BB_0063C63D]
  bb_0063C655[BB_0063C655]
  bb_0063C661[BB_0063C661]
  bb_0063C674[BB_0063C674]
  bb_0063C67D[BB_0063C67D]
  bb_0063C686[BB_0063C686]
  bb_0063C693[BB_0063C693]
  bb_0063C696[BB_0063C696]
  bb_0063C69B[BB_0063C69B]
  bb_0063C6A0[BB_0063C6A0]
  bb_0063C6AC[BB_0063C6AC]
  bb_0063C6C2[BB_0063C6C2]
  bb_0063C6CE[BB_0063C6CE]
  bb_0063C6DA[BB_0063C6DA]
  bb_0063C6ED[BB_0063C6ED]
  bb_0063C6F6[BB_0063C6F6]
  bb_0063C6FF[BB_0063C6FF]
  bb_0063C70C[BB_0063C70C]
  bb_0063C70F[BB_0063C70F]
  bb_0063C714[BB_0063C714]
  bb_0063C719[BB_0063C719]
  bb_0063C725[BB_0063C725]
  bb_0063C746[BB_0063C746]
  bb_0063C5D0 -->|branch| bb_0063C6AC
  bb_0063C5D0 -->|fallthrough| bb_0063C61F
  bb_0063C61F -->|branch| bb_0063C630
  bb_0063C61F -->|fallthrough| bb_0063C626
  bb_0063C626 -->|branch| bb_0063C63D
  bb_0063C630 -->|branch| bb_0063C63D
  bb_0063C630 -->|fallthrough| bb_0063C634
  bb_0063C634 -->|flow| bb_0063C63D
  bb_0063C63D -->|branch| bb_0063C661
  bb_0063C63D -->|fallthrough| bb_0063C655
  bb_0063C655 -->|branch| bb_0063C674
  bb_0063C655 -->|fallthrough| bb_0063C661
  bb_0063C661 -->|branch| bb_0063C6AC
  bb_0063C661 -->|fallthrough| bb_0063C674
  bb_0063C674 -->|branch| bb_0063C696
  bb_0063C67D -->|branch| bb_0063C693
  bb_0063C67D -->|fallthrough| bb_0063C686
  bb_0063C686 -->|flow| bb_0063C693
  bb_0063C693 -->|flow| bb_0063C696
  bb_0063C696 -->|branch| bb_0063C67D
  bb_0063C696 -->|fallthrough| bb_0063C69B
  bb_0063C69B -->|branch| bb_0063C6AC
  bb_0063C69B -->|fallthrough| bb_0063C6A0
  bb_0063C6A0 -->|flow| bb_0063C6AC
  bb_0063C6AC -->|branch| bb_0063C725
  bb_0063C6AC -->|fallthrough| bb_0063C6C2
  bb_0063C6C2 -->|branch| bb_0063C6DA
  bb_0063C6C2 -->|fallthrough| bb_0063C6CE
  bb_0063C6CE -->|branch| bb_0063C6ED
  bb_0063C6CE -->|fallthrough| bb_0063C6DA
  bb_0063C6DA -->|branch| bb_0063C725
  bb_0063C6DA -->|fallthrough| bb_0063C6ED
  bb_0063C6ED -->|branch| bb_0063C70F
  bb_0063C6F6 -->|branch| bb_0063C70C
  bb_0063C6F6 -->|fallthrough| bb_0063C6FF
  bb_0063C6FF -->|flow| bb_0063C70C
  bb_0063C70C -->|flow| bb_0063C70F
  bb_0063C70F -->|branch| bb_0063C6F6
  bb_0063C70F -->|fallthrough| bb_0063C714
  bb_0063C714 -->|branch| bb_0063C725
  bb_0063C714 -->|fallthrough| bb_0063C719
  bb_0063C719 -->|flow| bb_0063C725
```
