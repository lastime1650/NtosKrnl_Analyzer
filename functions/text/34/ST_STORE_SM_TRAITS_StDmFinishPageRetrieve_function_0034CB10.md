# ST_STORE&lt;SM_TRAITS&gt;::StDmFinishPageRetrieve

- RVA: `0x0034CB10`–`0x0034CB1A` (길이 `10` bytes)
- VA: `0x000000014034CB10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000787C8`
- 디코드: `5`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00420657](../42/Unknown_function_00420657.md) at `0x00420667`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmCompletePendingReads](../60/ST_STORE_SM_TRAITS_StDmCompletePendingReads_function_0060D174.md) at `0x0060D27E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034CB10  40 53                           push rbx
0034CB12  55                              push rbp
0034CB13  56                              push rsi
0034CB14  41 56                           push r14
0034CB16  48 83 EC 38                     sub rsp, 0x38
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ST_STORE_SM_TRAITS___StDmFinishPageRetrieve(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    return;
}
```

## 5. (Beta) C Style

```c
void ST_STORE_SM_TRAITS___StDmFinishPageRetrieve(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034CB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034CB10[BB_0034CB10]
```
