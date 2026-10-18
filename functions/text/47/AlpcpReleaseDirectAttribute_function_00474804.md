# AlpcpReleaseDirectAttribute

- RVA: `0x00474804`–`0x00474821` (길이 `29` bytes)
- VA: `0x0000000140474804`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00474816` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F98F9`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x0039583D`
- [AlpcpReleaseAttributes](../../page/88/AlpcpReleaseAttributes_function_0088D750.md) at `0x0088D7D1`
- [sub_0088E1DC](../../page/88/Unknown_function_0088E1DC.md) at `0x0088E587`
- [AlpcpReleaseMessageAttributesOnCancel](../../page/89/AlpcpReleaseMessageAttributesOnCancel_function_00894030.md) at `0x0089409C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00474804  48 83 EC 28                     sub rsp, 0x28
00474808  F6 C1 02                        test cl, 2
0047480B  74 0E                           je 0x14047481b
0047480D  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00474811  BA 44 66 6C 74                  mov edx, 0x746c6644
00474816  E8 C5 30 E8 FF                  call 0x1402f78e0
0047481B  48 83 C4 28                     add rsp, 0x28
0047481F  C3                              ret
00474820  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReleaseDirectAttribute(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(a1)) & (2)) != 0) {
        a1 = (a1) & (-4);
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReleaseDirectAttribute(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(Arg1)) & (2)) != 0) {
        Arg1 = (Arg1) & (-4);
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00474804&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00474804[BB_00474804]
  bb_0047480D[BB_0047480D]
  bb_0047481B[BB_0047481B]
  bb_00474820[BB_00474820]
  bb_00474804 -->|branch| bb_0047481B
  bb_00474804 -->|fallthrough| bb_0047480D
  bb_0047480D -->|flow| bb_0047481B
```
