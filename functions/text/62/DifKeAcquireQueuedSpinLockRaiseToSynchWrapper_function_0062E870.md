# DifKeAcquireQueuedSpinLockRaiseToSynchWrapper

- RVA: `0x0062E870`–`0x0062E9CF` (길이 `351` bytes)
- VA: `0x000000014062E870`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062E89F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062E8C7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062E8F5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062E91C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062E935` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062E93D` → [KeAcquireQueuedSpinLockRaiseToSynch](../5B/KeAcquireQueuedSpinLockRaiseToSynch_function_005BD410.md) (function, `0x005BD410`)
- `0x0062E96A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062E991` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062E9AA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062E8D9` → RVA `0x00F048B8` (`.data`; read)
- `0x0062E8E2` → RVA `0x00F04980` (`.data`; read)
- `0x0062E8EE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062E870  4C 8B DC                        mov r11, rsp
0062E873  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062E877  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062E87B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062E87F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062E883  41 56                           push r14
0062E885  48 83 EC 40                     sub rsp, 0x40
0062E889  33 C0                           xor eax, eax
0062E88B  0F 57 C0                        xorps xmm0, xmm0
0062E88E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062E893  48 8B E9                        mov rbp, rcx
0062E896  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062E89A  B9 25 01 00 00                  mov ecx, 0x125
0062E89F  E8 90 71 E6 FF                  call 0x140495a34
0062E8A4  48 8B F0                        mov rsi, rax
0062E8A7  48 85 C0                        test rax, rax
0062E8AA  0F 84 8A 00 00 00               je 0x14062e93a
0062E8B0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062E8B3  A8 18                           test al, 0x18
0062E8B5  74 0C                           je 0x14062e8c3
0062E8B7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062E8BC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062E8C1  EB 0E                           jmp 0x14062e8d1
0062E8C3  A8 04                           test al, 4
0062E8C5  74 0A                           je 0x14062e8d1
0062E8C7  E8 3C 53 EA FF                  call 0x1404d3c08
0062E8CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062E8D1  40 32 FF                        xor dil, dil
0062E8D4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062E8D9  40 38 3D D8 5F 8D 00            cmp byte ptr [rip + 0x8d5fd8], dil
0062E8E0  75 0C                           jne 0x14062e8ee
0062E8E2  F7 05 94 60 8D 00 00 08 00 00   test dword ptr [rip + 0x8d6094], 0x800
0062E8EC  74 13                           je 0x14062e901
0062E8EE  48 8D 0D 8B 55 8D 00            lea rcx, [rip + 0x8d558b]
0062E8F5  E8 26 7D BE FF                  call 0x140216620
0062E8FA  40 8A F8                        mov dil, al
0062E8FD  84 C0                           test al, al
0062E8FF  74 39                           je 0x14062e93a
0062E901  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062E905  49 8B 1E                        mov rbx, qword ptr [r14]
0062E908  EB 1A                           jmp 0x14062e924
0062E90A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062E90E  48 85 C0                        test rax, rax
0062E911  74 0E                           je 0x14062e921
0062E913  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062E917  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062E91C  E8 AF C1 08 00                  call 0x1406baad0
0062E921  48 8B 1B                        mov rbx, qword ptr [rbx]
0062E924  49 3B DE                        cmp rbx, r14
0062E927  75 E1                           jne 0x14062e90a
0062E929  40 84 FF                        test dil, dil
0062E92C  74 0C                           je 0x14062e93a
0062E92E  48 8D 0D 4B 55 8D 00            lea rcx, [rip + 0x8d554b]
0062E935  E8 46 B5 D1 FF                  call 0x140349e80
0062E93A  48 8B CD                        mov rcx, rbp
0062E93D  E8 CE EA F8 FF                  call 0x1405bd410
0062E942  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0062E946  48 85 F6                        test rsi, rsi
0062E949  74 64                           je 0x14062e9af
0062E94B  40 32 FF                        xor dil, dil
0062E94E  40 38 3D 63 5F 8D 00            cmp byte ptr [rip + 0x8d5f63], dil
0062E955  75 0C                           jne 0x14062e963
0062E957  F7 05 1F 60 8D 00 00 08 00 00   test dword ptr [rip + 0x8d601f], 0x800
0062E961  74 13                           je 0x14062e976
0062E963  48 8D 0D 16 55 8D 00            lea rcx, [rip + 0x8d5516]
0062E96A  E8 B1 7C BE FF                  call 0x140216620
0062E96F  40 8A F8                        mov dil, al
0062E972  84 C0                           test al, al
0062E974  74 39                           je 0x14062e9af
0062E976  48 83 C6 30                     add rsi, 0x30
0062E97A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062E97D  EB 1A                           jmp 0x14062e999
0062E97F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062E983  48 85 C0                        test rax, rax
0062E986  74 0E                           je 0x14062e996
0062E988  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062E98C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062E991  E8 3A C1 08 00                  call 0x1406baad0
0062E996  48 8B 1B                        mov rbx, qword ptr [rbx]
0062E999  48 3B DE                        cmp rbx, rsi
0062E99C  75 E1                           jne 0x14062e97f
0062E99E  40 84 FF                        test dil, dil
0062E9A1  74 0C                           je 0x14062e9af
0062E9A3  48 8D 0D D6 54 8D 00            lea rcx, [rip + 0x8d54d6]
0062E9AA  E8 D1 B4 D1 FF                  call 0x140349e80
0062E9AF  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
0062E9B3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062E9B8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062E9BD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062E9C2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062E9C7  48 83 C4 40                     add rsp, 0x40
0062E9CB  41 5E                           pop r14
0062E9CD  C3                              ret
0062E9CE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeAcquireQueuedSpinLockRaiseToSynchWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(293, a2, a3, a4);
    if (result == 0) goto loc_0062E93A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062E8C3;
    v_stack_m28 = v_stack_p0;
    goto loc_0062E8D1;
loc_0062E8C3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9265112)) != 0) goto loc_0062E8EE;
    if (((*(unsigned int *)(v_rip + 9265300)) & (0x800ULL)) == 0) goto loc_0062E901;
loc_0062E8EE:
    result = ExAcquireRundownProtection(v_rip + 9262475, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062E93A;
loc_0062E901:
    goto loc_0062E924;
loc_0062E90A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062E924:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062E90A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9262411;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeAcquireQueuedSpinLockRaiseToSynch(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062E9AF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9264995)) != 0) goto loc_0062E963;
    if (((*(unsigned int *)(v_rip + 9265183)) & (0x800ULL)) == 0) goto loc_0062E976;
loc_0062E963:
    result = ExAcquireRundownProtection(v_rip + 9262358, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062E9AF;
loc_0062E976:
    v_rsi = (result) + (48);
    goto loc_0062E999;
loc_0062E97F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062E999:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062E97F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9262294;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeAcquireQueuedSpinLockRaiseToSynchWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(293, a2, a3, a4);
    if (result == 0) goto loc_0062E93A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062E8C3;
    v_stack_m28 = v_stack_p0;
    goto loc_0062E8D1;
loc_0062E8C3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D5FD8)) != 0) goto loc_0062E8EE;
    if (((*(uint32_t *)(v_rip + 0x8D6094)) & (0x800ULL)) == 0) goto loc_0062E901;
loc_0062E8EE:
    result = ExAcquireRundownProtection(v_rip + 9262475, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062E93A;
loc_0062E901:
    goto loc_0062E924;
loc_0062E90A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062E924:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062E90A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9262411;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeAcquireQueuedSpinLockRaiseToSynch(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062E9AF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D5F63)) != 0) goto loc_0062E963;
    if (((*(uint32_t *)(v_rip + 0x8D601F)) & (0x800ULL)) == 0) goto loc_0062E976;
loc_0062E963:
    result = ExAcquireRundownProtection(v_rip + 9262358, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062E9AF;
loc_0062E976:
    local_rsi = (result) + (48);
    goto loc_0062E999;
loc_0062E97F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062E999:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062E97F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9262294;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062E870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062E870[BB_0062E870]
  bb_0062E8B0[BB_0062E8B0]
  bb_0062E8B7[BB_0062E8B7]
  bb_0062E8C3[BB_0062E8C3]
  bb_0062E8C7[BB_0062E8C7]
  bb_0062E8D1[BB_0062E8D1]
  bb_0062E8E2[BB_0062E8E2]
  bb_0062E8EE[BB_0062E8EE]
  bb_0062E901[BB_0062E901]
  bb_0062E90A[BB_0062E90A]
  bb_0062E913[BB_0062E913]
  bb_0062E921[BB_0062E921]
  bb_0062E924[BB_0062E924]
  bb_0062E929[BB_0062E929]
  bb_0062E92E[BB_0062E92E]
  bb_0062E93A[BB_0062E93A]
  bb_0062E94B[BB_0062E94B]
  bb_0062E957[BB_0062E957]
  bb_0062E963[BB_0062E963]
  bb_0062E976[BB_0062E976]
  bb_0062E97F[BB_0062E97F]
  bb_0062E988[BB_0062E988]
  bb_0062E996[BB_0062E996]
  bb_0062E999[BB_0062E999]
  bb_0062E99E[BB_0062E99E]
  bb_0062E9A3[BB_0062E9A3]
  bb_0062E9AF[BB_0062E9AF]
  bb_0062E9CE[BB_0062E9CE]
  bb_0062E870 -->|branch| bb_0062E93A
  bb_0062E870 -->|fallthrough| bb_0062E8B0
  bb_0062E8B0 -->|branch| bb_0062E8C3
  bb_0062E8B0 -->|fallthrough| bb_0062E8B7
  bb_0062E8B7 -->|branch| bb_0062E8D1
  bb_0062E8C3 -->|branch| bb_0062E8D1
  bb_0062E8C3 -->|fallthrough| bb_0062E8C7
  bb_0062E8C7 -->|flow| bb_0062E8D1
  bb_0062E8D1 -->|branch| bb_0062E8EE
  bb_0062E8D1 -->|fallthrough| bb_0062E8E2
  bb_0062E8E2 -->|branch| bb_0062E901
  bb_0062E8E2 -->|fallthrough| bb_0062E8EE
  bb_0062E8EE -->|branch| bb_0062E93A
  bb_0062E8EE -->|fallthrough| bb_0062E901
  bb_0062E901 -->|branch| bb_0062E924
  bb_0062E90A -->|branch| bb_0062E921
  bb_0062E90A -->|fallthrough| bb_0062E913
  bb_0062E913 -->|flow| bb_0062E921
  bb_0062E921 -->|flow| bb_0062E924
  bb_0062E924 -->|branch| bb_0062E90A
  bb_0062E924 -->|fallthrough| bb_0062E929
  bb_0062E929 -->|branch| bb_0062E93A
  bb_0062E929 -->|fallthrough| bb_0062E92E
  bb_0062E92E -->|flow| bb_0062E93A
  bb_0062E93A -->|branch| bb_0062E9AF
  bb_0062E93A -->|fallthrough| bb_0062E94B
  bb_0062E94B -->|branch| bb_0062E963
  bb_0062E94B -->|fallthrough| bb_0062E957
  bb_0062E957 -->|branch| bb_0062E976
  bb_0062E957 -->|fallthrough| bb_0062E963
  bb_0062E963 -->|branch| bb_0062E9AF
  bb_0062E963 -->|fallthrough| bb_0062E976
  bb_0062E976 -->|branch| bb_0062E999
  bb_0062E97F -->|branch| bb_0062E996
  bb_0062E97F -->|fallthrough| bb_0062E988
  bb_0062E988 -->|flow| bb_0062E996
  bb_0062E996 -->|flow| bb_0062E999
  bb_0062E999 -->|branch| bb_0062E97F
  bb_0062E999 -->|fallthrough| bb_0062E99E
  bb_0062E99E -->|branch| bb_0062E9AF
  bb_0062E99E -->|fallthrough| bb_0062E9A3
  bb_0062E9A3 -->|flow| bb_0062E9AF
```
