# ApiSetpIsFeatureEnabled

- RVA: `0x006648A8`–`0x006648BD` (길이 `21` bytes)
- VA: `0x00000001406648A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006648AC` → [IsFeatureEnabled](IsFeatureEnabled_function_006649C0.md) (function, `0x006649C0`)

### Direct callers
- [ApiSetQuerySchemaInfo2_V7](ApiSetQuerySchemaInfo2_V7_function_0066301C.md) at `0x0066332A`
- [ApiSetpResolveHost](ApiSetpResolveHost_function_006638D0.md) at `0x00663AD5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006648A8  48 83 EC 28                     sub rsp, 0x28
006648AC  E8 0F 01 00 00                  call 0x1406649c0
006648B1  83 F8 02                        cmp eax, 2
006648B4  0F 94 C0                        sete al
006648B7  48 83 C4 28                     add rsp, 0x28
006648BB  C3                              ret
006648BC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetpIsFeatureEnabled(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = IsFeatureEnabled(a1, a2, a3, a4);
    result = (((unsigned int)(result)) == 2) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ApiSetpIsFeatureEnabled(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = IsFeatureEnabled(a1, a2, a3, a4);
    result = (((uint32_t)(result)) == 2) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006648A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006648A8[BB_006648A8]
  bb_006648BC[BB_006648BC]
```
