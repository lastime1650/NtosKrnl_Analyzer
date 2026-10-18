# MiSortMdlFrames

- RVA: `0x006778C4`–`0x006778EB` (길이 `39` bytes)
- VA: `0x00000001406778C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006778E0` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)

### Direct callers
- [MiRemoveMdlPages](../../page/7F/MiRemoveMdlPages_function_007FC568.md) at `0x007FC5B4`

### Static image references
- `0x006778CB` → RVA `0x00558EA0` (`HalpNodeCostSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006778C4  48 83 EC 28                     sub rsp, 0x28
006778C8  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
006778CB  4C 8D 0D CE 15 EE FF            lea r9, [rip - 0x11ea32]
006778D2  48 C1 EA 0C                     shr rdx, 0xc
006778D6  48 83 C1 30                     add rcx, 0x30
006778DA  41 B8 08 00 00 00               mov r8d, 8
006778E0  E8 0B 91 E8 FF                  call 0x1405009f0
006778E5  48 83 C4 28                     add rsp, 0x28
006778E9  C3                              ret
006778EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSortMdlFrames(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 40))) >> (12);
    a1 = (a1) + (48);
    result = qsort(a1, a2, 8, v_rip - 1174066);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSortMdlFrames(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (12);
    Arg1 = (Arg1) + (48);
    result = qsort(Arg1, a2, 8, v_rip - 1174066);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006778C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006778C4[BB_006778C4]
  bb_006778EA[BB_006778EA]
```
