# HvlIsRootPowerSchedulerQosPresent

- RVA: `0x00583B94`–`0x00583B9E` (길이 `10` bytes)
- VA: `0x0000000140583B94`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PpmHvEnableQosEnlightenment](../../page/A8/PpmHvEnableQosEnlightenment_function_00A84D00.md) at `0x00A84D2B`

### Static image references
- `0x00583B94` → RVA `0x00FC6A92` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00583B94  8A 05 F8 2E A4 00               mov al, byte ptr [rip + 0xa42ef8]
00583B9A  24 01                           and al, 1
00583B9C  C3                              ret
00583B9D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlIsRootPowerSchedulerQosPresent(void)
{
    __int64 result;

    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 10759928)) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
void HvlIsRootPowerSchedulerQosPresent(void)
{
    int64_t result;

    result = (uint8_t)((*(uint8_t *)(v_rip + 0xA42EF8)) & (1));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00583B94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00583B94[BB_00583B94]
  bb_00583B9D[BB_00583B9D]
```
