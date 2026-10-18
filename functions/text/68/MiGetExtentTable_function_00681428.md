# MiGetExtentTable

- RVA: `0x00681428`–`0x00681438` (길이 `16` bytes)
- VA: `0x0000000140681428`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDeleteFileExtentList](../../page/80/MiDeleteFileExtentList_function_00800F6C.md) at `0x00800F86`

### Static image references
- `0x0068142B` → RVA `0x00E2D888` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00681428  48 63 C1                        movsxd rax, ecx
0068142B  48 8D 0D 56 C4 7A 00            lea rcx, [rip + 0x7ac456]
00681432  48 8D 04 C1                     lea rax, [rcx + rax*8]
00681436  C3                              ret
00681437  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetExtentTable(int a1)
{
    return v_rip + 8045654 + (int)(a1) * 8;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetExtentTable(int32_t Arg1)
{
    return v_rip + 8045654 + (int32_t)(Arg1) * 8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00681428&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00681428[BB_00681428]
  bb_00681437[BB_00681437]
```
