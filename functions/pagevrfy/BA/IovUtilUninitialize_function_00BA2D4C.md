# IovUtilUninitialize

- RVA: `0x00BA2D4C`–`0x00BA2D55` (길이 `9` bytes)
- VA: `0x0000000140BA2D4C`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ViIovPluginUnload](../../text/6A/ViIovPluginUnload_function_006AADB0.md) at `0x006AADD2`

### Static image references
- `0x00BA2D4C` → RVA `0x00F048E0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA2D4C  83 25 8D 1B 36 00 00            and dword ptr [rip + 0x361b8d], 0
00BA2D53  C3                              ret
00BA2D54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall IovUtilUninitialize(void)
{
    return;
}
```

## 5. (Beta) C Style

```c
void IovUtilUninitialize(void)
{
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA2D4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA2D4C[BB_00BA2D4C]
  bb_00BA2D54[BB_00BA2D54]
```
