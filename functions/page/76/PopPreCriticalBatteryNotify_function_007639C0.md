# PopPreCriticalBatteryNotify

- RVA: `0x007639C0`–`0x007639E0` (길이 `32` bytes)
- VA: `0x00000001407639C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007639C4` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x007639CE` → [PopPowerAggregatorForceSessionSwitch](PopPowerAggregatorForceSessionSwitch_function_007648D0.md) (function, `0x007648D0`)
- `0x007639D3` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007639C4` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x007639D3` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007639C0  48 83 EC 28                     sub rsp, 0x28
007639C4  E8 F7 49 41 00                  call 0x140b783c0
007639C9  B9 2D 00 00 00                  mov ecx, 0x2d
007639CE  E8 FD 0E 00 00                  call 0x1407648d0
007639D3  E8 38 4A 41 00                  call 0x140b78410
007639D8  33 C0                           xor eax, eax
007639DA  48 83 C4 28                     add rsp, 0x28
007639DE  C3                              ret
007639DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPreCriticalBatteryNotify(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    result = PopPowerAggregatorForceSessionSwitch(45, a2, a3, a4);
    result = PopReleasePolicyLock(45, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopPreCriticalBatteryNotify(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    result = PopPowerAggregatorForceSessionSwitch(45, a2, a3, a4);
    result = PopReleasePolicyLock(45, a2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007639C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007639C0[BB_007639C0]
  bb_007639DF[BB_007639DF]
```
