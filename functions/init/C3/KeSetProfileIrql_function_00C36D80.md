# KeSetProfileIrql

- RVA: `0x00C36D80`–`0x00C36D88` (길이 `8` bytes)
- VA: `0x0000000140C36D80`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `8/8` bytes 표시
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
- `0x00C36D80` → RVA `0x00FC501A` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C36D80  88 0D 94 E2 38 00               mov byte ptr [rip + 0x38e294], cl
00C36D86  C3                              ret
00C36D87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KeSetProfileIrql(unsigned __int8 a1)
{
    *(unsigned __int8 *)(v_rip + 3728020) = a1;
    return;
}
```

## 5. (Beta) C Style

```c
void KeSetProfileIrql(uint8_t Arg1)
{
    *(uint8_t *)(v_rip + 0x38E294) = Arg1;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C36D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C36D80[BB_00C36D80]
  bb_00C36D87[BB_00C36D87]
```
