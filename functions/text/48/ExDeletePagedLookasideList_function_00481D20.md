# ExDeletePagedLookasideList

- RVA: `0x00481D20`–`0x00481D47` (길이 `39` bytes)
- VA: `0x0000000140481D20`
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
- `0x00481D33` → [ExpRemoveGeneralLookaside](ExpRemoveGeneralLookaside_function_00481E10.md) (function, `0x00481E10`)
- `0x00481D3B` → [ExpFlushGeneralLookaside](ExpFlushGeneralLookaside_function_00481D80.md) (function, `0x00481D80`)

### Direct callers
- [DifExDeletePagedLookasideListWrapper](../61/DifExDeletePagedLookasideListWrapper_function_0061F8B0.md) at `0x0061F976`
- [FsRtlDeleteExtraCreateParameterLookasideList](../../page/71/FsRtlDeleteExtraCreateParameterLookasideList_function_007138E0.md) at `0x007138F0`

### Static image references
- `0x00481D2C` → RVA `0x00EFABE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00481D20  40 53                           push rbx
00481D22  48 83 EC 20                     sub rsp, 0x20
00481D26  48 8B D9                        mov rbx, rcx
00481D29  48 8B D1                        mov rdx, rcx
00481D2C  48 8D 0D AD 8E A7 00            lea rcx, [rip + 0xa78ead]
00481D33  E8 D8 00 00 00                  call 0x140481e10
00481D38  48 8B CB                        mov rcx, rbx
00481D3B  E8 40 00 00 00                  call 0x140481d80
00481D40  48 83 C4 20                     add rsp, 0x20
00481D44  5B                              pop rbx
00481D45  C3                              ret
00481D46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExDeletePagedLookasideList(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExpRemoveGeneralLookaside(v_rip + 10981037, a1, a3, a4);
    result = ExpFlushGeneralLookaside(a1, a1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExDeletePagedLookasideList(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExpRemoveGeneralLookaside(v_rip + 10981037, Arg1, a3, a4);
    result = ExpFlushGeneralLookaside(Arg1, Arg1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00481D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00481D20[BB_00481D20]
  bb_00481D46[BB_00481D46]
```
