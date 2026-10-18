# KeQueryHighestNodeNumber

- RVA: `0x0045CEC0`–`0x0045CECC` (길이 `12` bytes)
- VA: `0x000000014045CEC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpProcessorRundown](../../page/7C/EtwpProcessorRundown_function_007C0868.md) at `0x007C0A0B`
- [ExpQueryNumaProcessorMap](../../page/A5/ExpQueryNumaProcessorMap_function_00A5E784.md) at `0x00A5E7AB`
- [IoGetDeviceNumaNode](../../page/AA/IoGetDeviceNumaNode_function_00AAA050.md) at `0x00AAA0B3`

### Static image references
- `0x0045CEC0` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045CEC0  0F B7 05 39 81 B6 00            movzx eax, word ptr [rip + 0xb68139]
0045CEC7  66 FF C8                        dec ax
0045CECA  C3                              ret
0045CECB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryHighestNodeNumber(void)
{
    __int64 result;

    result = (unsigned __int16)((*(unsigned __int16 *)(v_rip + 11960633)) - 1);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeQueryHighestNodeNumber(void)
{
    int64_t result;

    result = (uint16_t)((*(uint16_t *)(v_rip + 0xB68139)) - 1);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045CEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045CEC0[BB_0045CEC0]
  bb_0045CECB[BB_0045CECB]
```
