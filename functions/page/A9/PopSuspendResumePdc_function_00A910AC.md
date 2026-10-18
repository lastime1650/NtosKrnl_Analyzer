# PopSuspendResumePdc

- RVA: `0x00A910AC`–`0x00A910C7` (길이 `27` bytes)
- VA: `0x0000000140A910AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A910BC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopPowerAggregatorSystemTransitionEnterStateHandler](../76/PopPowerAggregatorSystemTransitionEnterStateHandler_function_007650E0.md) at `0x00765136`
- [PopPowerAggregatorSystemTransitionExitStateHandler](../76/PopPowerAggregatorSystemTransitionExitStateHandler_function_00765180.md) at `0x00765213`
- [PopPowerAggregatorSystemTransitionExitStateHandler](../76/PopPowerAggregatorSystemTransitionExitStateHandler_function_00765180.md) at `0x0076521D`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x009569C4`

### Static image references
- `0x00A910B0` → RVA `0x00E677A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A910BC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A910AC  48 83 EC 28                     sub rsp, 0x28
00A910B0  48 8B 05 E9 66 3D 00            mov rax, qword ptr [rip + 0x3d66e9]
00A910B7  48 85 C0                        test rax, rax
00A910BA  74 05                           je 0x140a910c1
00A910BC  E8 0F 9A C2 FF                  call 0x1406baad0
00A910C1  48 83 C4 28                     add rsp, 0x28
00A910C5  C3                              ret
00A910C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSuspendResumePdc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(v_rip + 4024041);
    if (*(unsigned __int64 *)(v_rip + 4024041) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopSuspendResumePdc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(v_rip + 0x3D66E9);
    if (*(uint64_t *)(v_rip + 0x3D66E9) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A910AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A910AC[BB_00A910AC]
  bb_00A910BC[BB_00A910BC]
  bb_00A910C1[BB_00A910C1]
  bb_00A910C6[BB_00A910C6]
  bb_00A910AC -->|branch| bb_00A910C1
  bb_00A910AC -->|fallthrough| bb_00A910BC
  bb_00A910BC -->|flow| bb_00A910C1
```
