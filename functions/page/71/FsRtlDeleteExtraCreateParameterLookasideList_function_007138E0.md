# FsRtlDeleteExtraCreateParameterLookasideList

- RVA: `0x007138E0`–`0x007138FB` (길이 `27` bytes)
- VA: `0x00000001407138E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007138E9` → [ExDeleteNPagedLookasideList](../../text/48/ExDeleteNPagedLookasideList_function_00481D50.md) (function, `0x00481D50`)
- `0x007138F0` → [ExDeletePagedLookasideList](../../text/48/ExDeletePagedLookasideList_function_00481D20.md) (function, `0x00481D20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007138E9` → [ExDeleteNPagedLookasideList](../../text/48/ExDeleteNPagedLookasideList_function_00481D50.md) (`PAGE` → `.text`)
  - `0x007138F0` → [ExDeletePagedLookasideList](../../text/48/ExDeletePagedLookasideList_function_00481D20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007138E0  48 83 EC 28                     sub rsp, 0x28
007138E4  F6 C2 02                        test dl, 2
007138E7  74 07                           je 0x1407138f0
007138E9  E8 62 E4 D6 FF                  call 0x140481d50
007138EE  EB 05                           jmp 0x1407138f5
007138F0  E8 2B E4 D6 FF                  call 0x140481d20
007138F5  48 83 C4 28                     add rsp, 0x28
007138F9  C3                              ret
007138FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlDeleteExtraCreateParameterLookasideList(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((a2) & (2)) == 0) goto loc_007138F0;
    result = ExDeleteNPagedLookasideList(a1, a2, a3, a4);
    goto loc_007138F5;
loc_007138F0:
    result = ExDeletePagedLookasideList(a1, a2, a3, a4);
loc_007138F5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlDeleteExtraCreateParameterLookasideList(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((Arg2) & (2)) == 0) goto loc_007138F0;
    result = ExDeleteNPagedLookasideList(Arg1, Arg2, a3, a4);
    goto loc_007138F5;
loc_007138F0:
    result = ExDeletePagedLookasideList(Arg1, Arg2, a3, a4);
loc_007138F5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007138E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007138E0[BB_007138E0]
  bb_007138E9[BB_007138E9]
  bb_007138F0[BB_007138F0]
  bb_007138F5[BB_007138F5]
  bb_007138FA[BB_007138FA]
  bb_007138E0 -->|branch| bb_007138F0
  bb_007138E0 -->|fallthrough| bb_007138E9
  bb_007138E9 -->|branch| bb_007138F5
  bb_007138F0 -->|flow| bb_007138F5
```
