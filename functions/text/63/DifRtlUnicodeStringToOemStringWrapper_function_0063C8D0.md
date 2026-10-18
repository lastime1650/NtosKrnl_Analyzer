# DifRtlUnicodeStringToOemStringWrapper

- RVA: `0x0063C8D0`–`0x0063CA47` (길이 `375` bytes)
- VA: `0x000000014063C8D0`
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
- `0x0063C90E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063C934` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063C968` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063C98E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063C9A7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063C9B5` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (function, `0x00AC1C10`)
- `0x0063C9E1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CA07` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CA20` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063C944` → RVA `0x00F048B8` (`.data`; read)
- `0x0063C955` → RVA `0x00F04980` (`.data`; read)
- `0x0063C961` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063C9B5` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063C8D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063C8D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063C8DA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063C8DF  55                              push rbp
0063C8E0  41 54                           push r12
0063C8E2  41 55                           push r13
0063C8E4  41 56                           push r14
0063C8E6  41 57                           push r15
0063C8E8  48 8B EC                        mov rbp, rsp
0063C8EB  48 83 EC 50                     sub rsp, 0x50
0063C8EF  0F 57 C0                        xorps xmm0, xmm0
0063C8F2  33 C0                           xor eax, eax
0063C8F4  4C 8B E9                        mov r13, rcx
0063C8F7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063C8FB  B9 9A 00 00 00                  mov ecx, 0x9a
0063C900  45 8A F8                        mov r15b, r8b
0063C903  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063C907  4C 8B E2                        mov r12, rdx
0063C90A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063C90E  E8 21 91 E5 FF                  call 0x140495a34
0063C913  48 8B F0                        mov rsi, rax
0063C916  48 85 C0                        test rax, rax
0063C919  0F 84 8D 00 00 00               je 0x14063c9ac
0063C91F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063C922  A8 18                           test al, 0x18
0063C924  74 0A                           je 0x14063c930
0063C926  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063C92A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063C92E  EB 0D                           jmp 0x14063c93d
0063C930  A8 04                           test al, 4
0063C932  74 09                           je 0x14063c93d
0063C934  E8 CF 72 E9 FF                  call 0x1404d3c08
0063C939  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063C93D  45 32 F6                        xor r14b, r14b
0063C940  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063C944  44 38 35 6D 7F 8C 00            cmp byte ptr [rip + 0x8c7f6d], r14b
0063C94B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063C94F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063C953  75 0C                           jne 0x14063c961
0063C955  F7 05 21 80 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8021], 0x800
0063C95F  74 13                           je 0x14063c974
0063C961  48 8D 0D 18 75 8C 00            lea rcx, [rip + 0x8c7518]
0063C968  E8 B3 9C BD FF                  call 0x140216620
0063C96D  44 8A F0                        mov r14b, al
0063C970  84 C0                           test al, al
0063C972  74 38                           je 0x14063c9ac
0063C974  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063C978  48 8B 1F                        mov rbx, qword ptr [rdi]
0063C97B  EB 19                           jmp 0x14063c996
0063C97D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C981  48 85 C0                        test rax, rax
0063C984  74 0D                           je 0x14063c993
0063C986  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063C98A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063C98E  E8 3D E1 07 00                  call 0x1406baad0
0063C993  48 8B 1B                        mov rbx, qword ptr [rbx]
0063C996  48 3B DF                        cmp rbx, rdi
0063C999  75 E2                           jne 0x14063c97d
0063C99B  45 84 F6                        test r14b, r14b
0063C99E  74 0C                           je 0x14063c9ac
0063C9A0  48 8D 0D D9 74 8C 00            lea rcx, [rip + 0x8c74d9]
0063C9A7  E8 D4 D4 D0 FF                  call 0x140349e80
0063C9AC  45 8A C7                        mov r8b, r15b
0063C9AF  49 8B D4                        mov rdx, r12
0063C9B2  49 8B CD                        mov rcx, r13
0063C9B5  E8 56 52 48 00                  call 0x140ac1c10
0063C9BA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063C9BD  48 85 F6                        test rsi, rsi
0063C9C0  74 63                           je 0x14063ca25
0063C9C2  40 32 FF                        xor dil, dil
0063C9C5  40 38 3D EC 7E 8C 00            cmp byte ptr [rip + 0x8c7eec], dil
0063C9CC  75 0C                           jne 0x14063c9da
0063C9CE  F7 05 A8 7F 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7fa8], 0x800
0063C9D8  74 13                           je 0x14063c9ed
0063C9DA  48 8D 0D 9F 74 8C 00            lea rcx, [rip + 0x8c749f]
0063C9E1  E8 3A 9C BD FF                  call 0x140216620
0063C9E6  40 8A F8                        mov dil, al
0063C9E9  84 C0                           test al, al
0063C9EB  74 38                           je 0x14063ca25
0063C9ED  48 83 C6 30                     add rsi, 0x30
0063C9F1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063C9F4  EB 19                           jmp 0x14063ca0f
0063C9F6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C9FA  48 85 C0                        test rax, rax
0063C9FD  74 0D                           je 0x14063ca0c
0063C9FF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CA03  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CA07  E8 C4 E0 07 00                  call 0x1406baad0
0063CA0C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CA0F  48 3B DE                        cmp rbx, rsi
0063CA12  75 E2                           jne 0x14063c9f6
0063CA14  40 84 FF                        test dil, dil
0063CA17  74 0C                           je 0x14063ca25
0063CA19  48 8D 0D 60 74 8C 00            lea rcx, [rip + 0x8c7460]
0063CA20  E8 5B D4 D0 FF                  call 0x140349e80
0063CA25  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063CA28  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063CA2D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063CA31  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063CA35  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063CA39  49 8B E3                        mov rsp, r11
0063CA3C  41 5F                           pop r15
0063CA3E  41 5E                           pop r14
0063CA40  41 5D                           pop r13
0063CA42  41 5C                           pop r12
0063CA44  5D                              pop rbp
0063CA45  C3                              ret
0063CA46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlUnicodeStringToOemStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    result = DifGetAPIThunkContextById(154, a2, a3, a4);
    if (result == 0) goto loc_0063C9AC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063C930;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C93D;
loc_0063C930:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9207661)) != 0) goto loc_0063C961;
    if (((*(unsigned int *)(v_rip + 9207841)) & (0x800ULL)) == 0) goto loc_0063C974;
loc_0063C961:
    result = ExAcquireRundownProtection(v_rip + 9205016, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063C9AC;
loc_0063C974:
    goto loc_0063C996;
loc_0063C97D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063C996:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063C97D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204953;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlUnicodeStringToOemString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063CA25;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9207532)) != 0) goto loc_0063C9DA;
    if (((*(unsigned int *)(v_rip + 9207720)) & (0x800ULL)) == 0) goto loc_0063C9ED;
loc_0063C9DA:
    result = ExAcquireRundownProtection(v_rip + 9204895, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CA25;
loc_0063C9ED:
    v_rsi = (result) + (48);
    goto loc_0063CA0F;
loc_0063C9F6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CA0F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063C9F6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9204832;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlUnicodeStringToOemStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    result = DifGetAPIThunkContextById(154, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063C9AC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063C930;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C93D;
loc_0063C930:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C7F6D)) != 0) goto loc_0063C961;
    if (((*(uint32_t *)(v_rip + 0x8C8021)) & (0x800ULL)) == 0) goto loc_0063C974;
loc_0063C961:
    result = ExAcquireRundownProtection(v_rip + 9205016, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063C9AC;
loc_0063C974:
    goto loc_0063C996;
loc_0063C97D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063C996:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063C97D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204953;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlUnicodeStringToOemString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063CA25;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C7EEC)) != 0) goto loc_0063C9DA;
    if (((*(uint32_t *)(v_rip + 0x8C7FA8)) & (0x800ULL)) == 0) goto loc_0063C9ED;
loc_0063C9DA:
    result = ExAcquireRundownProtection(v_rip + 9204895, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CA25;
loc_0063C9ED:
    local_rsi = (result) + (48);
    goto loc_0063CA0F;
loc_0063C9F6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CA0F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063C9F6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9204832;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063C8D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063C8D0[BB_0063C8D0]
  bb_0063C91F[BB_0063C91F]
  bb_0063C926[BB_0063C926]
  bb_0063C930[BB_0063C930]
  bb_0063C934[BB_0063C934]
  bb_0063C93D[BB_0063C93D]
  bb_0063C955[BB_0063C955]
  bb_0063C961[BB_0063C961]
  bb_0063C974[BB_0063C974]
  bb_0063C97D[BB_0063C97D]
  bb_0063C986[BB_0063C986]
  bb_0063C993[BB_0063C993]
  bb_0063C996[BB_0063C996]
  bb_0063C99B[BB_0063C99B]
  bb_0063C9A0[BB_0063C9A0]
  bb_0063C9AC[BB_0063C9AC]
  bb_0063C9C2[BB_0063C9C2]
  bb_0063C9CE[BB_0063C9CE]
  bb_0063C9DA[BB_0063C9DA]
  bb_0063C9ED[BB_0063C9ED]
  bb_0063C9F6[BB_0063C9F6]
  bb_0063C9FF[BB_0063C9FF]
  bb_0063CA0C[BB_0063CA0C]
  bb_0063CA0F[BB_0063CA0F]
  bb_0063CA14[BB_0063CA14]
  bb_0063CA19[BB_0063CA19]
  bb_0063CA25[BB_0063CA25]
  bb_0063CA46[BB_0063CA46]
  bb_0063C8D0 -->|branch| bb_0063C9AC
  bb_0063C8D0 -->|fallthrough| bb_0063C91F
  bb_0063C91F -->|branch| bb_0063C930
  bb_0063C91F -->|fallthrough| bb_0063C926
  bb_0063C926 -->|branch| bb_0063C93D
  bb_0063C930 -->|branch| bb_0063C93D
  bb_0063C930 -->|fallthrough| bb_0063C934
  bb_0063C934 -->|flow| bb_0063C93D
  bb_0063C93D -->|branch| bb_0063C961
  bb_0063C93D -->|fallthrough| bb_0063C955
  bb_0063C955 -->|branch| bb_0063C974
  bb_0063C955 -->|fallthrough| bb_0063C961
  bb_0063C961 -->|branch| bb_0063C9AC
  bb_0063C961 -->|fallthrough| bb_0063C974
  bb_0063C974 -->|branch| bb_0063C996
  bb_0063C97D -->|branch| bb_0063C993
  bb_0063C97D -->|fallthrough| bb_0063C986
  bb_0063C986 -->|flow| bb_0063C993
  bb_0063C993 -->|flow| bb_0063C996
  bb_0063C996 -->|branch| bb_0063C97D
  bb_0063C996 -->|fallthrough| bb_0063C99B
  bb_0063C99B -->|branch| bb_0063C9AC
  bb_0063C99B -->|fallthrough| bb_0063C9A0
  bb_0063C9A0 -->|flow| bb_0063C9AC
  bb_0063C9AC -->|branch| bb_0063CA25
  bb_0063C9AC -->|fallthrough| bb_0063C9C2
  bb_0063C9C2 -->|branch| bb_0063C9DA
  bb_0063C9C2 -->|fallthrough| bb_0063C9CE
  bb_0063C9CE -->|branch| bb_0063C9ED
  bb_0063C9CE -->|fallthrough| bb_0063C9DA
  bb_0063C9DA -->|branch| bb_0063CA25
  bb_0063C9DA -->|fallthrough| bb_0063C9ED
  bb_0063C9ED -->|branch| bb_0063CA0F
  bb_0063C9F6 -->|branch| bb_0063CA0C
  bb_0063C9F6 -->|fallthrough| bb_0063C9FF
  bb_0063C9FF -->|flow| bb_0063CA0C
  bb_0063CA0C -->|flow| bb_0063CA0F
  bb_0063CA0F -->|branch| bb_0063C9F6
  bb_0063CA0F -->|fallthrough| bb_0063CA14
  bb_0063CA14 -->|branch| bb_0063CA25
  bb_0063CA14 -->|fallthrough| bb_0063CA19
  bb_0063CA19 -->|flow| bb_0063CA25
```
