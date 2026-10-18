# ST_STORE&lt;SM_TRAITS&gt;::StWorkItemProcess

- RVA: `0x00205DD0`–`0x00205DDB` (길이 `11` bytes)
- VA: `0x0000000140205DD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CDF0`
- 디코드: `4`개 명령, `11/11` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00206865](Unknown_function_00206865.md) at `0x002069C6`
- [ST_STORE&lt;SM_TRAITS&gt;::StLazyWorkMgrRunExpiredWork](../41/ST_STORE_SM_TRAITS_StLazyWorkMgrRunExpiredWork_function_004157B8.md) at `0x004158A7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00205DD0  40 53                           push rbx
00205DD2  55                              push rbp
00205DD3  56                              push rsi
00205DD4  48 81 EC 80 00 00 00            sub rsp, 0x80
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ST_STORE_SM_TRAITS___StWorkItemProcess(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (128);
    return;
}
```

## 5. (Beta) C Style

```c
void ST_STORE_SM_TRAITS___StWorkItemProcess(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (128);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00205DD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00205DD0[BB_00205DD0]
```
