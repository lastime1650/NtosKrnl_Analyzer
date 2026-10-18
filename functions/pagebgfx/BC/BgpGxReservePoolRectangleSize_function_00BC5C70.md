# BgpGxReservePoolRectangleSize

- RVA: `0x00BC5C70`–`0x00BC5C88` (길이 `24` bytes)
- VA: `0x0000000140BC5C70`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC5C74` → [BgpGxRectangleSize](../../text/4C/BgpGxRectangleSize_function_004C1DE4.md) (function, `0x004C1DE4`)

### Direct callers
- [BgpTxtRegionSize](../../text/69/BgpTxtRegionSize_function_0069F484.md) at `0x0069F4AF`
- [BgpTxtRegionSize](../../text/69/BgpTxtRegionSize_function_0069F484.md) at `0x0069F4C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC5C74` → [BgpGxRectangleSize](../../text/4C/BgpGxRectangleSize_function_004C1DE4.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC5C70  48 83 EC 28                     sub rsp, 0x28
00BC5C74  E8 6B C1 8F FF                  call 0x1404c1de4
00BC5C79  83 C0 0F                        add eax, 0xf
00BC5C7C  83 E0 F0                        and eax, 0xfffffff0
00BC5C7F  83 C0 20                        add eax, 0x20
00BC5C82  48 83 C4 28                     add rsp, 0x28
00BC5C86  C3                              ret
00BC5C87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpGxReservePoolRectangleSize(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = BgpGxRectangleSize(a1, a2, a3, a4);
    result = (unsigned int)((result) + (15));
    result = (unsigned int)((result) & (0xFFFFFFF0ULL));
    result = (unsigned int)((result) + (32));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void BgpGxReservePoolRectangleSize(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = BgpGxRectangleSize(a1, a2, a3, a4);
    result = (uint32_t)((result) + (15));
    result = (uint32_t)((result) & (0xFFFFFFF0ULL));
    result = (uint32_t)((result) + (32));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC5C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC5C70[BB_00BC5C70]
  bb_00BC5C87[BB_00BC5C87]
```
