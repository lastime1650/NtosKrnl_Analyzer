# MiGetAvailablePagesForTrimPass

- RVA: `0x0034D324`–`0x0034D338` (길이 `20` bytes)
- VA: `0x000000014034D324`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034D32D` → [MiGetAvailablePagesBelowPriority](MiGetAvailablePagesBelowPriority_function_0034D340.md) (function, `0x0034D340`)

### Direct callers
- [MiForcedTrim](MiForcedTrim_function_0034DC0C.md) at `0x0034DC4D`
- [MiComputeSystemTrimCriteria](MiComputeSystemTrimCriteria_function_0034E184.md) at `0x0034E1B4`
- [MiComputeAgingPercent](MiComputeAgingPercent_function_0034F508.md) at `0x0034F515`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034D324  48 83 EC 28                     sub rsp, 0x28
0034D328  BA 06 00 00 00                  mov edx, 6
0034D32D  E8 0E 00 00 00                  call 0x14034d340
0034D332  48 83 C4 28                     add rsp, 0x28
0034D336  C3                              ret
0034D337  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetAvailablePagesForTrimPass(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiGetAvailablePagesBelowPriority(a1, 6, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiGetAvailablePagesForTrimPass(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiGetAvailablePagesBelowPriority(a1, 6, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034D324&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034D324[BB_0034D324]
  bb_0034D337[BB_0034D337]
```
