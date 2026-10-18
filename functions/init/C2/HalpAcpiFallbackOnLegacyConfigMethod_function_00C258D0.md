# HalpAcpiFallbackOnLegacyConfigMethod

- RVA: `0x00C258D0`–`0x00C258D9` (길이 `9` bytes)
- VA: `0x0000000140C258D0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C258D0` → RVA `0x00E103F8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C258D0  C6 05 21 AB 1E 00 01            mov byte ptr [rip + 0x1eab21], 1
00C258D7  C3                              ret
00C258D8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall HalpAcpiFallbackOnLegacyConfigMethod(void)
{
    *(unsigned __int8 *)(v_rip + 2009889) = 1;
    return;
}
```

## 5. (Beta) C Style

```c
void HalpAcpiFallbackOnLegacyConfigMethod(void)
{
    *(uint8_t *)(v_rip + 0x1EAB21) = 1;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C258D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C258D0[BB_00C258D0]
  bb_00C258D8[BB_00C258D8]
```
