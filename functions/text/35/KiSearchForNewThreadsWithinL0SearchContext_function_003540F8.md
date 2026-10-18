# KiSearchForNewThreadsWithinL0SearchContext

- RVA: `0x003540F8`–`0x00354115` (길이 `29` bytes)
- VA: `0x00000001403540F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0035410A` → [KiSearchForNewThreadsWithinSearchContext](KiSearchForNewThreadsWithinSearchContext_function_00353B30.md) (function, `0x00353B30`)

### Direct callers
- [KiSearchForNewThreadsWithinRestOfSystem](KiSearchForNewThreadsWithinRestOfSystem_function_003540A8.md) at `0x003540C3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003540F8  48 83 EC 28                     sub rsp, 0x28
003540FC  4C 8B 81 18 94 00 00            mov r8, qword ptr [rcx + 0x9418]
00354103  4C 8B 89 28 94 00 00            mov r9, qword ptr [rcx + 0x9428]
0035410A  E8 21 FA FF FF                  call 0x140353b30
0035410F  48 83 C4 28                     add rsp, 0x28
00354113  C3                              ret
00354114  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSearchForNewThreadsWithinL0SearchContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KiSearchForNewThreadsWithinSearchContext(a1, a2, *(unsigned __int64 *)(a1 + 37912), *(unsigned __int64 *)(a1 + 37928));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiSearchForNewThreadsWithinL0SearchContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KiSearchForNewThreadsWithinSearchContext(Arg1, a2, *(uint64_t *)(arg1 + 0x9418), *(uint64_t *)(arg1 + 0x9428));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9418` | `64` | `R` |
| `Arg1` | `+ 0x9428` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003540F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003540F8[BB_003540F8]
  bb_00354114[BB_00354114]
```
