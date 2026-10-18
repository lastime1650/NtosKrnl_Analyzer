# MiFreeRotateView

- RVA: `0x007FE6CC`–`0x007FE6FD` (길이 `49` bytes)
- VA: `0x00000001407FE6CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007FE6D7` → [MiGetVadWakeList](../../text/43/MiGetVadWakeList_function_00431134.md) (function, `0x00431134`)
- `0x007FE6E7` → [MiFreeRotateVadEvent](../A9/MiFreeRotateVadEvent_function_00A95140.md) (function, `0x00A95140`)
- `0x007FE6F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiDeleteNewlyCreatedPartialVads](../81/MiDeleteNewlyCreatedPartialVads_function_00810374.md) at `0x0081043E`
- [MiInitializePartialVad](../88/MiInitializePartialVad_function_00887954.md) at `0x00887B28`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007FE6D7` → [MiGetVadWakeList](../../text/43/MiGetVadWakeList_function_00431134.md) (`PAGE` → `.text`)
  - `0x007FE6F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FE6CC  40 53                           push rbx
007FE6CE  48 83 EC 20                     sub rsp, 0x20
007FE6D2  BA 08 00 00 00                  mov edx, 8
007FE6D7  E8 58 2A C3 FF                  call 0x140431134
007FE6DC  48 8B D8                        mov rbx, rax
007FE6DF  48 85 C0                        test rax, rax
007FE6E2  74 12                           je 0x1407fe6f6
007FE6E4  48 8B C8                        mov rcx, rax
007FE6E7  E8 54 6A 29 00                  call 0x140a95140
007FE6EC  33 D2                           xor edx, edx
007FE6EE  48 8B CB                        mov rcx, rbx
007FE6F1  E8 7A 41 38 00                  call 0x140b82870
007FE6F6  48 83 C4 20                     add rsp, 0x20
007FE6FA  5B                              pop rbx
007FE6FB  C3                              ret
007FE6FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeRotateView(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiGetVadWakeList(a1, 8, a3, a4);
    if (result != 0) {
        a1 = result;
        result = MiFreeRotateVadEvent(a1, 8, a3, a4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiFreeRotateView(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiGetVadWakeList(a1, 8, a3, a4);
    if (result != 0) {
        a1 = result;
        result = MiFreeRotateVadEvent(a1, 8, a3, a4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FE6CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007FE6CC[BB_007FE6CC]
  bb_007FE6E4[BB_007FE6E4]
  bb_007FE6F6[BB_007FE6F6]
  bb_007FE6FC[BB_007FE6FC]
  bb_007FE6CC -->|branch| bb_007FE6F6
  bb_007FE6CC -->|fallthrough| bb_007FE6E4
  bb_007FE6E4 -->|flow| bb_007FE6F6
```
