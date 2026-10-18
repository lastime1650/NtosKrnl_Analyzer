# RtlpGetLegacyContextLength

- RVA: `0x004B6060`–`0x004B606F` (길이 `15` bytes)
- VA: `0x00000001404B6060`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B6064` → [RtlpGetLegacyContextLength2](../4E/RtlpGetLegacyContextLength2_function_004EF8A4.md) (function, `0x004EF8A4`)

### Direct callers
- [PspWow64SetupCpuArea](../../page/8C/PspWow64SetupCpuArea_function_008CDBFC.md) at `0x008CDC30`
- [RtlWow64GetCpuAreaInfo](../../page/8C/RtlWow64GetCpuAreaInfo_function_008CDE0C.md) at `0x008CDE50`
- [RtlpWriteExtendedContext](../../page/8D/RtlpWriteExtendedContext_function_008D4A5C.md) at `0x008D4AB4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B6060  48 83 EC 28                     sub rsp, 0x28
004B6064  E8 3B 98 03 00                  call 0x1404ef8a4
004B6069  48 83 C4 28                     add rsp, 0x28
004B606D  C3                              ret
004B606E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGetLegacyContextLength(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpGetLegacyContextLength2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlpGetLegacyContextLength(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpGetLegacyContextLength2(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B6060&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B6060[BB_004B6060]
  bb_004B606E[BB_004B606E]
```
