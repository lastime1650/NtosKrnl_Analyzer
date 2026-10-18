# VfDdiInit

- RVA: `0x00B94364`–`0x00B94370` (길이 `12` bytes)
- VA: `0x0000000140B94364`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfIrpTrackingPluginEntry](../../text/6A/VfIrpTrackingPluginEntry_function_006AAE60.md) at `0x006AAE9E`

### Static image references
- `0x00B94364` → RVA `0x00F048D0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B94364  C7 05 62 05 37 00 01 00 00 00   mov dword ptr [rip + 0x370562], 1
00B9436E  C3                              ret
00B9436F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall VfDdiInit(void)
{
    *(unsigned int *)(v_rip + 3605858) = 1;
    return;
}
```

## 5. (Beta) C Style

```c
void VfDdiInit(void)
{
    *(uint32_t *)(v_rip + 0x370562) = 1;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B94364&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B94364[BB_00B94364]
  bb_00B9436F[BB_00B9436F]
```
