# ExDeleteNPagedLookasideList

- RVA: `0x00481D50`–`0x00481D77` (길이 `39` bytes)
- VA: `0x0000000140481D50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00481D63` → [ExpRemoveGeneralLookaside](ExpRemoveGeneralLookaside_function_00481E10.md) (function, `0x00481E10`)
- `0x00481D6B` → [ExpFlushGeneralLookaside](ExpFlushGeneralLookaside_function_00481D80.md) (function, `0x00481D80`)

### Direct callers
- [DifExDeleteNPagedLookasideListWrapper](../61/DifExDeleteNPagedLookasideListWrapper_function_0061F750.md) at `0x0061F816`
- [FsRtlDeleteExtraCreateParameterLookasideList](../../page/71/FsRtlDeleteExtraCreateParameterLookasideList_function_007138E0.md) at `0x007138E9`

### Static image references
- `0x00481D5C` → RVA `0x00EFABC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00481D50  40 53                           push rbx
00481D52  48 83 EC 20                     sub rsp, 0x20
00481D56  48 8B D9                        mov rbx, rcx
00481D59  48 8B D1                        mov rdx, rcx
00481D5C  48 8D 0D 5D 8E A7 00            lea rcx, [rip + 0xa78e5d]
00481D63  E8 A8 00 00 00                  call 0x140481e10
00481D68  48 8B CB                        mov rcx, rbx
00481D6B  E8 10 00 00 00                  call 0x140481d80
00481D70  48 83 C4 20                     add rsp, 0x20
00481D74  5B                              pop rbx
00481D75  C3                              ret
00481D76  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExDeleteNPagedLookasideList(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExpRemoveGeneralLookaside(v_rip + 10980957, a1, a3, a4);
    result = ExpFlushGeneralLookaside(a1, a1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExDeleteNPagedLookasideList(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExpRemoveGeneralLookaside(v_rip + 10980957, Arg1, a3, a4);
    result = ExpFlushGeneralLookaside(Arg1, Arg1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00481D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00481D50[BB_00481D50]
  bb_00481D76[BB_00481D76]
```
