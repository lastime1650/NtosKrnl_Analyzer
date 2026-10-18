# HvlHalGetVpIndexFromApicId

- RVA: `0x005886E0`–`0x00588705` (길이 `37` bytes)
- VA: `0x00000001405886E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005886F3` → [HvlpGetVpIndexFromApicId](HvlpGetVpIndexFromApicId_function_00585880.md) (function, `0x00585880`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005886E0  40 53                           push rbx
005886E2  48 83 EC 20                     sub rsp, 0x20
005886E6  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
005886EB  48 8B DA                        mov rbx, rdx
005886EE  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
005886F3  E8 88 D1 FF FF                  call 0x140585880
005886F8  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
005886FC  89 0B                           mov dword ptr [rbx], ecx
005886FE  48 83 C4 20                     add rsp, 0x20
00588702  5B                              pop rbx
00588703  C3                              ret
00588704  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlHalGetVpIndexFromApicId(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p10;

    v_rsp = (v_rsp) - (32);
    result = HvlpGetVpIndexFromApicId(a1, v_stack_p10, a3, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(v_stack_p10));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlHalGetVpIndexFromApicId(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p10;

    local_rsp = (local_rsp) - (32);
    result = HvlpGetVpIndexFromApicId(Arg1, v_stack_p10, a3, a4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(v_stack_p10));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005886E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005886E0[BB_005886E0]
  bb_00588704[BB_00588704]
```
