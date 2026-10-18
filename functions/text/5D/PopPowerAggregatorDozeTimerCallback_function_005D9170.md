# PopPowerAggregatorDozeTimerCallback

- RVA: `0x005D9170`–`0x005D9198` (길이 `40` bytes)
- VA: `0x00000001405D9170`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D918D` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005D9183` → RVA `0x00F09878` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D9170  48 83 EC 28                     sub rsp, 0x28
005D9174  48 63 C2                        movsxd rax, edx
005D9177  BA 01 00 00 00                  mov edx, 1
005D917C  48 69 C8 C8 00 00 00            imul rcx, rax, 0xc8
005D9183  48 8D 05 EE 06 93 00            lea rax, [rip + 0x9306ee]
005D918A  48 03 C8                        add rcx, rax
005D918D  E8 8E 03 D2 FF                  call 0x1402f9520
005D9192  48 83 C4 28                     add rsp, 0x28
005D9196  C3                              ret
005D9197  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerAggregatorDozeTimerCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) * ((int)(a2));
    a1 = (a1) + (v_rip + 9635566);
    result = ExQueueWorkItem(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerAggregatorDozeTimerCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) * ((int32_t)(Arg2));
    Arg1 = (Arg1) + (v_rip + 9635566);
    result = ExQueueWorkItem(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D9170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D9170[BB_005D9170]
  bb_005D9197[BB_005D9197]
```
