# DefaultDisableMonitoring

- RVA: `0x0054DB30`–`0x0054DB43` (길이 `19` bytes)
- VA: `0x000000014054DB30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0054DB38` → [HalpTimerStopProfileInterrupt](HalpTimerStopProfileInterrupt_function_0054B8A4.md) (function, `0x0054B8A4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054DB30  48 83 EC 28                     sub rsp, 0x28
0054DB34  85 C9                           test ecx, ecx
0054DB36  75 05                           jne 0x14054db3d
0054DB38  E8 67 DD FF FF                  call 0x14054b8a4
0054DB3D  48 83 C4 28                     add rsp, 0x28
0054DB41  C3                              ret
0054DB42  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DefaultDisableMonitoring(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) {
        result = HalpTimerStopProfileInterrupt(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DefaultDisableMonitoring(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) {
        result = HalpTimerStopProfileInterrupt(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054DB30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054DB30[BB_0054DB30]
  bb_0054DB38[BB_0054DB38]
  bb_0054DB3D[BB_0054DB3D]
  bb_0054DB42[BB_0054DB42]
  bb_0054DB30 -->|branch| bb_0054DB3D
  bb_0054DB30 -->|fallthrough| bb_0054DB38
  bb_0054DB38 -->|flow| bb_0054DB3D
```
