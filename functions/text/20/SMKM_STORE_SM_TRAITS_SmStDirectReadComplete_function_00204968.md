# SMKM_STORE&lt;SM_TRAITS&gt;::SmStDirectReadComplete

- RVA: `0x00204968`–`0x00204995` (길이 `45` bytes)
- VA: `0x0000000140204968`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC40`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00204988` → [SMKM_STORE_MGR<SM_TRAITS>::SmWorkItemFree](SMKM_STORE_MGR_SM_TRAITS_SmWorkItemFree_function_00205570.md) (function, `0x00205570`)

### Direct callers
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStReadThread](SMKM_STORE_SM_TRAITS_SmStReadThread_function_00203230.md) at `0x002033AD`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStDirectReadCallout](../2F/SMKM_STORE_SM_TRAITS_SmStDirectReadCallout_function_002FA3E0.md) at `0x002FA45E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00204968  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0020496D  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00204972  48 83 EC 28                     sub rsp, 0x28
00204976  4C 8B C2                        mov r8, rdx
00204979  48 8B D1                        mov rdx, rcx
0020497C  48 8B 89 90 1D 00 00            mov rcx, qword ptr [rcx + 0x1d90]
00204983  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00204988  E8 E3 0B 00 00                  call 0x140205570
0020498D  EB 00                           jmp 0x14020498f
0020498F  48 83 C4 28                     add rsp, 0x28
00204993  C3                              ret
00204994  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_SM_TRAITS___SmStDirectReadComplete(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    result = SMKM_STORE_MGR_SM_TRAITS___SmWorkItemFree(*(unsigned __int64 *)(a1 + 7568), a1, a2, v_stack_p18);
    goto loc_0020498F;
loc_0020498F:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_SM_TRAITS___SmStDirectReadComplete(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    result = SMKM_STORE_MGR_SM_TRAITS___SmWorkItemFree(*(uint64_t *)(arg1 + 0x1D90), Arg1, Arg2, v_stack_p18);
    goto loc_0020498F;
loc_0020498F:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1D90` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00204968&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00204968[BB_00204968]
  bb_0020498F[BB_0020498F]
  bb_00204994[BB_00204994]
  bb_00204968 -->|branch| bb_0020498F
```
