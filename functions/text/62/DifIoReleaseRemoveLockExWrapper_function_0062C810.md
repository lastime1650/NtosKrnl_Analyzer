# DifIoReleaseRemoveLockExWrapper

- RVA: `0x0062C810`–`0x0062C982` (길이 `370` bytes)
- VA: `0x000000014062C810`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062C846` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062C86E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062C8A6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C8CD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C8E6` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062C8F4` → [IoReleaseRemoveLockEx](../33/IoReleaseRemoveLockEx_function_0033D330.md) (function, `0x0033D330`)
- `0x0062C91D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C944` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C95D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062C880` → RVA `0x00F048B8` (`.data`; read)
- `0x0062C893` → RVA `0x00F04980` (`.data`; read)
- `0x0062C89F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062C810  48 8B C4                        mov rax, rsp
0062C813  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062C817  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062C81B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062C81F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062C823  41 54                           push r12
0062C825  41 56                           push r14
0062C827  41 57                           push r15
0062C829  48 83 EC 40                     sub rsp, 0x40
0062C82D  0F 57 C0                        xorps xmm0, xmm0
0062C830  4C 8B E1                        mov r12, rcx
0062C833  B9 3C 01 00 00                  mov ecx, 0x13c
0062C838  45 8B F0                        mov r14d, r8d
0062C83B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062C83F  4C 8B FA                        mov r15, rdx
0062C842  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062C846  E8 E9 91 E6 FF                  call 0x140495a34
0062C84B  48 8B F0                        mov rsi, rax
0062C84E  48 85 C0                        test rax, rax
0062C851  0F 84 94 00 00 00               je 0x14062c8eb
0062C857  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062C85A  A8 18                           test al, 0x18
0062C85C  74 0C                           je 0x14062c86a
0062C85E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062C863  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062C868  EB 0E                           jmp 0x14062c878
0062C86A  A8 04                           test al, 4
0062C86C  74 0A                           je 0x14062c878
0062C86E  E8 95 73 EA FF                  call 0x1404d3c08
0062C873  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062C878  40 32 ED                        xor bpl, bpl
0062C87B  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0062C880  40 38 2D 31 80 8D 00            cmp byte ptr [rip + 0x8d8031], bpl
0062C887  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062C88C  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0062C891  75 0C                           jne 0x14062c89f
0062C893  F7 05 E3 80 8D 00 00 08 00 00   test dword ptr [rip + 0x8d80e3], 0x800
0062C89D  74 13                           je 0x14062c8b2
0062C89F  48 8D 0D DA 75 8D 00            lea rcx, [rip + 0x8d75da]
0062C8A6  E8 75 9D BE FF                  call 0x140216620
0062C8AB  40 8A E8                        mov bpl, al
0062C8AE  84 C0                           test al, al
0062C8B0  74 39                           je 0x14062c8eb
0062C8B2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062C8B6  48 8B 1F                        mov rbx, qword ptr [rdi]
0062C8B9  EB 1A                           jmp 0x14062c8d5
0062C8BB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C8BF  48 85 C0                        test rax, rax
0062C8C2  74 0E                           je 0x14062c8d2
0062C8C4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C8C8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C8CD  E8 FE E1 08 00                  call 0x1406baad0
0062C8D2  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C8D5  48 3B DF                        cmp rbx, rdi
0062C8D8  75 E1                           jne 0x14062c8bb
0062C8DA  40 84 ED                        test bpl, bpl
0062C8DD  74 0C                           je 0x14062c8eb
0062C8DF  48 8D 0D 9A 75 8D 00            lea rcx, [rip + 0x8d759a]
0062C8E6  E8 95 D5 D1 FF                  call 0x140349e80
0062C8EB  45 8B C6                        mov r8d, r14d
0062C8EE  49 8B D7                        mov rdx, r15
0062C8F1  49 8B CC                        mov rcx, r12
0062C8F4  E8 37 0A D1 FF                  call 0x14033d330
0062C8F9  48 85 F6                        test rsi, rsi
0062C8FC  74 64                           je 0x14062c962
0062C8FE  40 32 FF                        xor dil, dil
0062C901  40 38 3D B0 7F 8D 00            cmp byte ptr [rip + 0x8d7fb0], dil
0062C908  75 0C                           jne 0x14062c916
0062C90A  F7 05 6C 80 8D 00 00 08 00 00   test dword ptr [rip + 0x8d806c], 0x800
0062C914  74 13                           je 0x14062c929
0062C916  48 8D 0D 63 75 8D 00            lea rcx, [rip + 0x8d7563]
0062C91D  E8 FE 9C BE FF                  call 0x140216620
0062C922  40 8A F8                        mov dil, al
0062C925  84 C0                           test al, al
0062C927  74 39                           je 0x14062c962
0062C929  48 83 C6 30                     add rsi, 0x30
0062C92D  48 8B 1E                        mov rbx, qword ptr [rsi]
0062C930  EB 1A                           jmp 0x14062c94c
0062C932  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C936  48 85 C0                        test rax, rax
0062C939  74 0E                           je 0x14062c949
0062C93B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C93F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C944  E8 87 E1 08 00                  call 0x1406baad0
0062C949  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C94C  48 3B DE                        cmp rbx, rsi
0062C94F  75 E1                           jne 0x14062c932
0062C951  40 84 FF                        test dil, dil
0062C954  74 0C                           je 0x14062c962
0062C956  48 8D 0D 23 75 8D 00            lea rcx, [rip + 0x8d7523]
0062C95D  E8 1E D5 D1 FF                  call 0x140349e80
0062C962  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062C967  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062C96C  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062C971  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062C976  48 83 C4 40                     add rsp, 0x40
0062C97A  41 5F                           pop r15
0062C97C  41 5E                           pop r14
0062C97E  41 5C                           pop r12
0062C980  C3                              ret
0062C981  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoReleaseRemoveLockExWrapper(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(316, a2, a3, a4);
    if (result == 0) goto loc_0062C8EB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062C86A;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C878;
loc_0062C86A:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9273393)) != 0) goto loc_0062C89F;
    if (((*(unsigned int *)(v_rip + 9273571)) & (0x800ULL)) == 0) goto loc_0062C8B2;
loc_0062C89F:
    result = ExAcquireRundownProtection(v_rip + 9270746, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C8EB;
loc_0062C8B2:
    goto loc_0062C8D5;
loc_0062C8BB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C8D5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062C8BB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9270682;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoReleaseRemoveLockEx(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_0062C962;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9273264)) != 0) goto loc_0062C916;
    if (((*(unsigned int *)(v_rip + 9273452)) & (0x800ULL)) == 0) goto loc_0062C929;
loc_0062C916:
    result = ExAcquireRundownProtection(v_rip + 9270627, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C962;
loc_0062C929:
    v_rsi = (result) + (48);
    goto loc_0062C94C;
loc_0062C932:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0062C94C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062C932;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9270563;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoReleaseRemoveLockExWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(316, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062C8EB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062C86A;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C878;
loc_0062C86A:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8D8031)) != 0) goto loc_0062C89F;
    if (((*(uint32_t *)(v_rip + 0x8D80E3)) & (0x800ULL)) == 0) goto loc_0062C8B2;
loc_0062C89F:
    result = ExAcquireRundownProtection(v_rip + 9270746, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062C8EB;
loc_0062C8B2:
    goto loc_0062C8D5;
loc_0062C8BB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062C8D5:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062C8BB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9270682;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoReleaseRemoveLockEx(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (result == 0) goto loc_0062C962;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D7FB0)) != 0) goto loc_0062C916;
    if (((*(uint32_t *)(v_rip + 0x8D806C)) & (0x800ULL)) == 0) goto loc_0062C929;
loc_0062C916:
    result = ExAcquireRundownProtection(v_rip + 9270627, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_0062C962;
loc_0062C929:
    local_rsi = (result) + (48);
    goto loc_0062C94C;
loc_0062C932:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0062C94C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062C932;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9270563;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062C810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062C810[BB_0062C810]
  bb_0062C857[BB_0062C857]
  bb_0062C85E[BB_0062C85E]
  bb_0062C86A[BB_0062C86A]
  bb_0062C86E[BB_0062C86E]
  bb_0062C878[BB_0062C878]
  bb_0062C893[BB_0062C893]
  bb_0062C89F[BB_0062C89F]
  bb_0062C8B2[BB_0062C8B2]
  bb_0062C8BB[BB_0062C8BB]
  bb_0062C8C4[BB_0062C8C4]
  bb_0062C8D2[BB_0062C8D2]
  bb_0062C8D5[BB_0062C8D5]
  bb_0062C8DA[BB_0062C8DA]
  bb_0062C8DF[BB_0062C8DF]
  bb_0062C8EB[BB_0062C8EB]
  bb_0062C8FE[BB_0062C8FE]
  bb_0062C90A[BB_0062C90A]
  bb_0062C916[BB_0062C916]
  bb_0062C929[BB_0062C929]
  bb_0062C932[BB_0062C932]
  bb_0062C93B[BB_0062C93B]
  bb_0062C949[BB_0062C949]
  bb_0062C94C[BB_0062C94C]
  bb_0062C951[BB_0062C951]
  bb_0062C956[BB_0062C956]
  bb_0062C962[BB_0062C962]
  bb_0062C981[BB_0062C981]
  bb_0062C810 -->|branch| bb_0062C8EB
  bb_0062C810 -->|fallthrough| bb_0062C857
  bb_0062C857 -->|branch| bb_0062C86A
  bb_0062C857 -->|fallthrough| bb_0062C85E
  bb_0062C85E -->|branch| bb_0062C878
  bb_0062C86A -->|branch| bb_0062C878
  bb_0062C86A -->|fallthrough| bb_0062C86E
  bb_0062C86E -->|flow| bb_0062C878
  bb_0062C878 -->|branch| bb_0062C89F
  bb_0062C878 -->|fallthrough| bb_0062C893
  bb_0062C893 -->|branch| bb_0062C8B2
  bb_0062C893 -->|fallthrough| bb_0062C89F
  bb_0062C89F -->|branch| bb_0062C8EB
  bb_0062C89F -->|fallthrough| bb_0062C8B2
  bb_0062C8B2 -->|branch| bb_0062C8D5
  bb_0062C8BB -->|branch| bb_0062C8D2
  bb_0062C8BB -->|fallthrough| bb_0062C8C4
  bb_0062C8C4 -->|flow| bb_0062C8D2
  bb_0062C8D2 -->|flow| bb_0062C8D5
  bb_0062C8D5 -->|branch| bb_0062C8BB
  bb_0062C8D5 -->|fallthrough| bb_0062C8DA
  bb_0062C8DA -->|branch| bb_0062C8EB
  bb_0062C8DA -->|fallthrough| bb_0062C8DF
  bb_0062C8DF -->|flow| bb_0062C8EB
  bb_0062C8EB -->|branch| bb_0062C962
  bb_0062C8EB -->|fallthrough| bb_0062C8FE
  bb_0062C8FE -->|branch| bb_0062C916
  bb_0062C8FE -->|fallthrough| bb_0062C90A
  bb_0062C90A -->|branch| bb_0062C929
  bb_0062C90A -->|fallthrough| bb_0062C916
  bb_0062C916 -->|branch| bb_0062C962
  bb_0062C916 -->|fallthrough| bb_0062C929
  bb_0062C929 -->|branch| bb_0062C94C
  bb_0062C932 -->|branch| bb_0062C949
  bb_0062C932 -->|fallthrough| bb_0062C93B
  bb_0062C93B -->|flow| bb_0062C949
  bb_0062C949 -->|flow| bb_0062C94C
  bb_0062C94C -->|branch| bb_0062C932
  bb_0062C94C -->|fallthrough| bb_0062C951
  bb_0062C951 -->|branch| bb_0062C962
  bb_0062C951 -->|fallthrough| bb_0062C956
  bb_0062C956 -->|flow| bb_0062C962
```
