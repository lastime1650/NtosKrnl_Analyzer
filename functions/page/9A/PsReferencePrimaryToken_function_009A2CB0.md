# PsReferencePrimaryToken

- RVA: `0x009A2CB0`–`0x009A2CC4` (길이 `20` bytes)
- VA: `0x00000001409A2CB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A2CB9` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)

### Direct callers
- [MiCreateSystemSection](../../text/45/MiCreateSystemSection_function_00453158.md) at `0x004532AB`
- [PspIsTamperProtectedProcess](../../text/5E/PspIsTamperProtectedProcess_function_005E36D4.md) at `0x005E36E8`
- [SeGetProcessAntiTamperIdentity](../../text/60/SeGetProcessAntiTamperIdentity_function_00606740.md) at `0x00606764`
- [SeGetProcessAntiTamperUIPolicy](../../text/60/SeGetProcessAntiTamperUIPolicy_function_00606800.md) at `0x00606838`
- [SeReportLearningModeViolation](../../text/60/SeReportLearningModeViolation_function_00608B50.md) at `0x00608CB3`
- [SeSetTokenTamperProtection](../../text/60/SeSetTokenTamperProtection_function_00609644.md) at `0x00609705`
- [SepConstructAntiTamperBaselinePolicy](../../text/60/SepConstructAntiTamperBaselinePolicy_function_0060A83C.md) at `0x0060A861`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009A2CB9` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A2CB0  48 83 EC 28                     sub rsp, 0x28
009A2CB4  BA 44 66 6C 74                  mov edx, 0x746c6644
009A2CB9  E8 C2 D2 86 FF                  call 0x14020ff80
009A2CBE  48 83 C4 28                     add rsp, 0x28
009A2CC2  C3                              ret
009A2CC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsReferencePrimaryToken(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsReferencePrimaryTokenWithTag(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PsReferencePrimaryToken(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsReferencePrimaryTokenWithTag(a1, (uint32_t)(0x746C6644ULL), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A2CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A2CB0[BB_009A2CB0]
  bb_009A2CC3[BB_009A2CC3]
```
