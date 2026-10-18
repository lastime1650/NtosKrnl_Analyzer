# WdiUpdateSem

- RVA: `0x0064E064`–`0x0064E07C` (길이 `24` bytes)
- VA: `0x000000014064E064`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0064E068` → [WdipAccessCheck](WdipAccessCheck_function_0064E084.md) (function, `0x0064E084`)
- `0x0064E071` → [WdipSemUpdate](../../page/7A/WdipSemUpdate_function_007AED28.md) (function, `0x007AED28`)

### Direct callers
- [NtTraceControl](../../page/A9/NtTraceControl_function_00A9ED40.md) at `0x00A9F29A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0064E071` → [WdipSemUpdate](../../page/7A/WdipSemUpdate_function_007AED28.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064E064  48 83 EC 28                     sub rsp, 0x28
0064E068  E8 17 00 00 00                  call 0x14064e084
0064E06D  85 C0                           test eax, eax
0064E06F  78 05                           js 0x14064e076
0064E071  E8 B2 0C 16 00                  call 0x1407aed28
0064E076  48 83 C4 28                     add rsp, 0x28
0064E07A  C3                              ret
0064E07B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdiUpdateSem(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = WdipAccessCheck(a1, a2, a3, a4);
    if (!(sign_flag)) {
        result = WdipSemUpdate(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void WdiUpdateSem(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = WdipAccessCheck(a1, a2, a3, a4);
    if (!(sign_flag)) {
        result = WdipSemUpdate(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064E064&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064E064[BB_0064E064]
  bb_0064E071[BB_0064E071]
  bb_0064E076[BB_0064E076]
  bb_0064E07B[BB_0064E07B]
  bb_0064E064 -->|branch| bb_0064E076
  bb_0064E064 -->|fallthrough| bb_0064E071
  bb_0064E071 -->|flow| bb_0064E076
```
