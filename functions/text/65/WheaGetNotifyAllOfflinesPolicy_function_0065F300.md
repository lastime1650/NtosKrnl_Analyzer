# WheaGetNotifyAllOfflinesPolicy

- RVA: `0x0065F300`–`0x0065F30F` (길이 `15` bytes)
- VA: `0x000000014065F300`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [WheapAttemptPhysicalPageOffline](../../page/7D/WheapAttemptPhysicalPageOffline_function_007D79AC.md) at `0x007D7A92`
- [WheapExecuteRowFailureCheck](../../page/7D/WheapExecuteRowFailureCheck_function_007D8ED8.md) at `0x007D90A6`

### Static image references
- `0x0065F300` → RVA `0x00E097A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065F300  48 8B 05 A1 A4 7A 00            mov rax, qword ptr [rip + 0x7aa4a1]
0065F307  83 38 01                        cmp dword ptr [rax], 1
0065F30A  0F 96 C0                        setbe al
0065F30D  C3                              ret
0065F30E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaGetNotifyAllOfflinesPolicy(void)
{
    __int64 result;

    result = ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8037537))) <= 1) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void WheaGetNotifyAllOfflinesPolicy(void)
{
    int64_t result;

    result = ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x7AA4A1))) <= 1) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065F300&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065F300[BB_0065F300]
  bb_0065F30E[BB_0065F30E]
```
