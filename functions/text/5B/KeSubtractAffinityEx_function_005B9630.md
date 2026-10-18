# KeSubtractAffinityEx

- RVA: `0x005B9630`–`0x005B9651` (길이 `33` bytes)
- VA: `0x00000001405B9630`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B9639` → [KiSubtractAffinityExNoResult](../4D/KiSubtractAffinityExNoResult_function_004D99D4.md) (function, `0x004D99D4`)
- `0x005B9646` → [KiSubtractAffinityEx](../2D/KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B9630  48 83 EC 28                     sub rsp, 0x28
005B9634  4D 85 C0                        test r8, r8
005B9637  75 07                           jne 0x1405b9640
005B9639  E8 96 03 F2 FF                  call 0x1404d99d4
005B963E  EB 0B                           jmp 0x1405b964b
005B9640  41 B9 14 00 00 00               mov r9d, 0x14
005B9646  E8 9D CB D1 FF                  call 0x1402d61e8
005B964B  48 83 C4 28                     add rsp, 0x28
005B964F  C3                              ret
005B9650  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSubtractAffinityEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 != 0) goto loc_005B9640;
    result = KiSubtractAffinityExNoResult(a1, a2, a3, a4);
    goto loc_005B964B;
loc_005B9640:
    result = KiSubtractAffinityEx(a1, a2, a3, 20);
loc_005B964B:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeSubtractAffinityEx(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 != 0) goto loc_005B9640;
    result = KiSubtractAffinityExNoResult(Arg1, Arg2, Arg3, a4);
    goto loc_005B964B;
loc_005B9640:
    result = KiSubtractAffinityEx(Arg1, Arg2, Arg3, 20);
loc_005B964B:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B9630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B9630[BB_005B9630]
  bb_005B9639[BB_005B9639]
  bb_005B9640[BB_005B9640]
  bb_005B964B[BB_005B964B]
  bb_005B9650[BB_005B9650]
  bb_005B9630 -->|branch| bb_005B9640
  bb_005B9630 -->|fallthrough| bb_005B9639
  bb_005B9639 -->|branch| bb_005B964B
  bb_005B9640 -->|flow| bb_005B964B
```
