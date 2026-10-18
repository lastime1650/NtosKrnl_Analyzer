# PrExtLogLatencyTime

- RVA: `0x00666DB4`–`0x00666DBD` (길이 `9` bytes)
- VA: `0x0000000140666DB4`
- 실행 섹션: `.text`
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
- [HalpLoadMicrocode](../../page/70/HalpLoadMicrocode_function_0070B200.md) at `0x0070B386`

### Static image references
- `0x00666DB4` → RVA `0x00EF7CD0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00666DB4  48 89 0D 15 0F 89 00            mov qword ptr [rip + 0x890f15], rcx
00666DBB  C3                              ret
00666DBC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PrExtLogLatencyTime(__int64 a1)
{
    *(unsigned __int64 *)(v_rip + 8982293) = a1;
    return;
}
```

## 5. (Beta) C Style

```c
void PrExtLogLatencyTime(int64_t Arg1)
{
    *(uint64_t *)(v_rip + 0x890F15) = Arg1;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00666DB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00666DB4[BB_00666DB4]
  bb_00666DBC[BB_00666DBC]
```
