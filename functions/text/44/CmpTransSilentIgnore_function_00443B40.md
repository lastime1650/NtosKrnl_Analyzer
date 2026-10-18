# CmpTransSilentIgnore

- RVA: `0x00443B40`–`0x00443B4C` (길이 `12` bytes)
- VA: `0x0000000140443B40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpDoParseKey](../../page/85/CmpDoParseKey_function_0085F750.md) at `0x0085FE22`

### Static image references
- `0x00443B40` → RVA `0x00FD8006` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00443B40  80 3D BF 44 B9 00 00            cmp byte ptr [rip + 0xb944bf], 0
00443B47  0F 95 C0                        setne al
00443B4A  C3                              ret
00443B4B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTransSilentIgnore(void)
{
    __int64 result;

    result = ((*(unsigned __int8 *)(v_rip + 12141759)) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpTransSilentIgnore(void)
{
    int64_t result;

    result = ((*(uint8_t *)(v_rip + 0xB944BF)) != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00443B40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00443B40[BB_00443B40]
  bb_00443B4B[BB_00443B4B]
```
