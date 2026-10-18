# DifIoWMIRegistrationControlWrapper

- RVA: `0x0062D880`–`0x0062D9E4` (길이 `356` bytes)
- VA: `0x000000014062D880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062D8AE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062D8D6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062D909` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D930` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D949` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062D954` → [IoWMIRegistrationControl](../../page/9E/IoWMIRegistrationControl_function_009E2D60.md) (function, `0x009E2D60`)
- `0x0062D981` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D9A8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D9C1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062D8E8` → RVA `0x00F048B8` (`.data`; read)
- `0x0062D8F6` → RVA `0x00F04980` (`.data`; read)
- `0x0062D902` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062D954` → [IoWMIRegistrationControl](../../page/9E/IoWMIRegistrationControl_function_009E2D60.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062D880  48 8B C4                        mov rax, rsp
0062D883  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062D887  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062D88B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062D88F  57                              push rdi
0062D890  41 56                           push r14
0062D892  41 57                           push r15
0062D894  48 83 EC 40                     sub rsp, 0x40
0062D898  0F 57 C0                        xorps xmm0, xmm0
0062D89B  4C 8B F9                        mov r15, rcx
0062D89E  B9 31 01 00 00                  mov ecx, 0x131
0062D8A3  44 8B F2                        mov r14d, edx
0062D8A6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062D8AA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062D8AE  E8 81 81 E6 FF                  call 0x140495a34
0062D8B3  48 8B F0                        mov rsi, rax
0062D8B6  48 85 C0                        test rax, rax
0062D8B9  0F 84 8F 00 00 00               je 0x14062d94e
0062D8BF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062D8C2  A8 18                           test al, 0x18
0062D8C4  74 0C                           je 0x14062d8d2
0062D8C6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062D8CB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062D8D0  EB 0E                           jmp 0x14062d8e0
0062D8D2  A8 04                           test al, 4
0062D8D4  74 0A                           je 0x14062d8e0
0062D8D6  E8 2D 63 EA FF                  call 0x1404d3c08
0062D8DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062D8E0  40 32 ED                        xor bpl, bpl
0062D8E3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062D8E8  40 38 2D C9 6F 8D 00            cmp byte ptr [rip + 0x8d6fc9], bpl
0062D8EF  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0062D8F4  75 0C                           jne 0x14062d902
0062D8F6  F7 05 80 70 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7080], 0x800
0062D900  74 13                           je 0x14062d915
0062D902  48 8D 0D 77 65 8D 00            lea rcx, [rip + 0x8d6577]
0062D909  E8 12 8D BE FF                  call 0x140216620
0062D90E  40 8A E8                        mov bpl, al
0062D911  84 C0                           test al, al
0062D913  74 39                           je 0x14062d94e
0062D915  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062D919  48 8B 1F                        mov rbx, qword ptr [rdi]
0062D91C  EB 1A                           jmp 0x14062d938
0062D91E  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D922  48 85 C0                        test rax, rax
0062D925  74 0E                           je 0x14062d935
0062D927  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D92B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062D930  E8 9B D1 08 00                  call 0x1406baad0
0062D935  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D938  48 3B DF                        cmp rbx, rdi
0062D93B  75 E1                           jne 0x14062d91e
0062D93D  40 84 ED                        test bpl, bpl
0062D940  74 0C                           je 0x14062d94e
0062D942  48 8D 0D 37 65 8D 00            lea rcx, [rip + 0x8d6537]
0062D949  E8 32 C5 D1 FF                  call 0x140349e80
0062D94E  41 8B D6                        mov edx, r14d
0062D951  49 8B CF                        mov rcx, r15
0062D954  E8 07 54 3B 00                  call 0x1409e2d60
0062D959  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0062D95D  48 85 F6                        test rsi, rsi
0062D960  74 64                           je 0x14062d9c6
0062D962  40 32 FF                        xor dil, dil
0062D965  40 38 3D 4C 6F 8D 00            cmp byte ptr [rip + 0x8d6f4c], dil
0062D96C  75 0C                           jne 0x14062d97a
0062D96E  F7 05 08 70 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7008], 0x800
0062D978  74 13                           je 0x14062d98d
0062D97A  48 8D 0D FF 64 8D 00            lea rcx, [rip + 0x8d64ff]
0062D981  E8 9A 8C BE FF                  call 0x140216620
0062D986  40 8A F8                        mov dil, al
0062D989  84 C0                           test al, al
0062D98B  74 39                           je 0x14062d9c6
0062D98D  48 83 C6 30                     add rsi, 0x30
0062D991  48 8B 1E                        mov rbx, qword ptr [rsi]
0062D994  EB 1A                           jmp 0x14062d9b0
0062D996  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D99A  48 85 C0                        test rax, rax
0062D99D  74 0E                           je 0x14062d9ad
0062D99F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D9A3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062D9A8  E8 23 D1 08 00                  call 0x1406baad0
0062D9AD  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D9B0  48 3B DE                        cmp rbx, rsi
0062D9B3  75 E1                           jne 0x14062d996
0062D9B5  40 84 FF                        test dil, dil
0062D9B8  74 0C                           je 0x14062d9c6
0062D9BA  48 8D 0D BF 64 8D 00            lea rcx, [rip + 0x8d64bf]
0062D9C1  E8 BA C4 D1 FF                  call 0x140349e80
0062D9C6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0062D9CA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062D9CF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062D9D4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062D9D9  48 83 C4 40                     add rsp, 0x40
0062D9DD  41 5F                           pop r15
0062D9DF  41 5E                           pop r14
0062D9E1  5F                              pop rdi
0062D9E2  C3                              ret
0062D9E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoWMIRegistrationControlWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(305, a2, a3, a4);
    if (result == 0) goto loc_0062D94E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062D8D2;
    v_stack_m38 = v_stack_p0;
    goto loc_0062D8E0;
loc_0062D8D2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9269193)) != 0) goto loc_0062D902;
    if (((*(unsigned int *)(v_rip + 9269376)) & (0x800ULL)) == 0) goto loc_0062D915;
loc_0062D902:
    result = ExAcquireRundownProtection(v_rip + 9266551, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D94E;
loc_0062D915:
    goto loc_0062D938;
loc_0062D91E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062D938:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062D91E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9266487;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoWMIRegistrationControl(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_0062D9C6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9269068)) != 0) goto loc_0062D97A;
    if (((*(unsigned int *)(v_rip + 9269256)) & (0x800ULL)) == 0) goto loc_0062D98D;
loc_0062D97A:
    result = ExAcquireRundownProtection(v_rip + 9266431, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D9C6;
loc_0062D98D:
    v_rsi = (result) + (48);
    goto loc_0062D9B0;
loc_0062D996:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062D9B0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062D996;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9266367;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoWMIRegistrationControlWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(305, Arg2, a3, a4);
    if (result == 0) goto loc_0062D94E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062D8D2;
    v_stack_m38 = v_stack_p0;
    goto loc_0062D8E0;
loc_0062D8D2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8D6FC9)) != 0) goto loc_0062D902;
    if (((*(uint32_t *)(v_rip + 0x8D7080)) & (0x800ULL)) == 0) goto loc_0062D915;
loc_0062D902:
    result = ExAcquireRundownProtection(v_rip + 9266551, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062D94E;
loc_0062D915:
    goto loc_0062D938;
loc_0062D91E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062D938:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062D91E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9266487;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoWMIRegistrationControl(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_0062D9C6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D6F4C)) != 0) goto loc_0062D97A;
    if (((*(uint32_t *)(v_rip + 0x8D7008)) & (0x800ULL)) == 0) goto loc_0062D98D;
loc_0062D97A:
    result = ExAcquireRundownProtection(v_rip + 9266431, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062D9C6;
loc_0062D98D:
    local_rsi = (result) + (48);
    goto loc_0062D9B0;
loc_0062D996:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_0062D9B0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062D996;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9266367;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062D880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062D880[BB_0062D880]
  bb_0062D8BF[BB_0062D8BF]
  bb_0062D8C6[BB_0062D8C6]
  bb_0062D8D2[BB_0062D8D2]
  bb_0062D8D6[BB_0062D8D6]
  bb_0062D8E0[BB_0062D8E0]
  bb_0062D8F6[BB_0062D8F6]
  bb_0062D902[BB_0062D902]
  bb_0062D915[BB_0062D915]
  bb_0062D91E[BB_0062D91E]
  bb_0062D927[BB_0062D927]
  bb_0062D935[BB_0062D935]
  bb_0062D938[BB_0062D938]
  bb_0062D93D[BB_0062D93D]
  bb_0062D942[BB_0062D942]
  bb_0062D94E[BB_0062D94E]
  bb_0062D962[BB_0062D962]
  bb_0062D96E[BB_0062D96E]
  bb_0062D97A[BB_0062D97A]
  bb_0062D98D[BB_0062D98D]
  bb_0062D996[BB_0062D996]
  bb_0062D99F[BB_0062D99F]
  bb_0062D9AD[BB_0062D9AD]
  bb_0062D9B0[BB_0062D9B0]
  bb_0062D9B5[BB_0062D9B5]
  bb_0062D9BA[BB_0062D9BA]
  bb_0062D9C6[BB_0062D9C6]
  bb_0062D9E3[BB_0062D9E3]
  bb_0062D880 -->|branch| bb_0062D94E
  bb_0062D880 -->|fallthrough| bb_0062D8BF
  bb_0062D8BF -->|branch| bb_0062D8D2
  bb_0062D8BF -->|fallthrough| bb_0062D8C6
  bb_0062D8C6 -->|branch| bb_0062D8E0
  bb_0062D8D2 -->|branch| bb_0062D8E0
  bb_0062D8D2 -->|fallthrough| bb_0062D8D6
  bb_0062D8D6 -->|flow| bb_0062D8E0
  bb_0062D8E0 -->|branch| bb_0062D902
  bb_0062D8E0 -->|fallthrough| bb_0062D8F6
  bb_0062D8F6 -->|branch| bb_0062D915
  bb_0062D8F6 -->|fallthrough| bb_0062D902
  bb_0062D902 -->|branch| bb_0062D94E
  bb_0062D902 -->|fallthrough| bb_0062D915
  bb_0062D915 -->|branch| bb_0062D938
  bb_0062D91E -->|branch| bb_0062D935
  bb_0062D91E -->|fallthrough| bb_0062D927
  bb_0062D927 -->|flow| bb_0062D935
  bb_0062D935 -->|flow| bb_0062D938
  bb_0062D938 -->|branch| bb_0062D91E
  bb_0062D938 -->|fallthrough| bb_0062D93D
  bb_0062D93D -->|branch| bb_0062D94E
  bb_0062D93D -->|fallthrough| bb_0062D942
  bb_0062D942 -->|flow| bb_0062D94E
  bb_0062D94E -->|branch| bb_0062D9C6
  bb_0062D94E -->|fallthrough| bb_0062D962
  bb_0062D962 -->|branch| bb_0062D97A
  bb_0062D962 -->|fallthrough| bb_0062D96E
  bb_0062D96E -->|branch| bb_0062D98D
  bb_0062D96E -->|fallthrough| bb_0062D97A
  bb_0062D97A -->|branch| bb_0062D9C6
  bb_0062D97A -->|fallthrough| bb_0062D98D
  bb_0062D98D -->|branch| bb_0062D9B0
  bb_0062D996 -->|branch| bb_0062D9AD
  bb_0062D996 -->|fallthrough| bb_0062D99F
  bb_0062D99F -->|flow| bb_0062D9AD
  bb_0062D9AD -->|flow| bb_0062D9B0
  bb_0062D9B0 -->|branch| bb_0062D996
  bb_0062D9B0 -->|fallthrough| bb_0062D9B5
  bb_0062D9B5 -->|branch| bb_0062D9C6
  bb_0062D9B5 -->|fallthrough| bb_0062D9BA
  bb_0062D9BA -->|flow| bb_0062D9C6
```
