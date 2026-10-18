# TmRollbackEnlistment

- RVA: `0x004FE380`–`0x004FE38C` (길이 `12` bytes)
- VA: `0x00000001404FE380`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpRollbackTransactionArray](../../page/94/CmpRollbackTransactionArray_function_0094B3AC.md) at `0x0094B3FC`
- [CmpAbortRollbackPacket](../../page/AB/CmpAbortRollbackPacket_function_00ABEA80.md) at `0x00ABEAE8`
- [sub_00B160F4](../../page/B1/Unknown_function_00B160F4.md) at `0x00B161B4`
- [sub_00B2D90C](../../page/B2/Unknown_function_00B2D90C.md) at `0x00B2D90E`
- [sub_00B2D90C](../../page/B2/Unknown_function_00B2D90C.md) at `0x00B2D969`
- [sub_00B2D90C](../../page/B2/Unknown_function_00B2D90C.md) at `0x00B2D9C4`

### Static image references
- `0x004FE380` → RVA `0x001514E0` (`ext-ms-win-ntos-tm-l1-1-0.dll!TmRollbackEnlistment (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FE380  48 FF 25 59 31 C5 FF            jmp qword ptr [rip - 0x3acea7]
004FE387  CC                              int3
004FE388  CC                              int3
004FE389  CC                              int3
004FE38A  CC                              int3
004FE38B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall TmRollbackEnlistment(void)
{
}
```

## 5. (Beta) C Style

```c
void TmRollbackEnlistment(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FE380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FE380[BB_004FE380]
  bb_004FE387[BB_004FE387]
```
