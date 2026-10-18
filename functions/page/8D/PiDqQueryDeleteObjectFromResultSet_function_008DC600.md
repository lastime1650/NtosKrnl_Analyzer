# PiDqQueryDeleteObjectFromResultSet

- RVA: `0x008DC600`–`0x008DC62B` (길이 `43` bytes)
- VA: `0x00000001408DC600`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085914`
- 디코드: `12`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DC612` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (function, `0x003EE750`)
- `0x008DC620` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)

### Direct callers
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DDD9A`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DE07A`
- [PiDqQueryFreeActiveData](PiDqQueryFreeActiveData_function_008DE4FC.md) at `0x008DE56C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008DC612` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DC600  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008DC605  48 83 EC 28                     sub rsp, 0x28
008DC609  48 83 C1 48                     add rcx, 0x48
008DC60D  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
008DC612  E8 39 21 B1 FF                  call 0x1403ee750
008DC617  84 C0                           test al, al
008DC619  74 0A                           je 0x1408dc625
008DC61B  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
008DC620  E8 4B 89 00 00                  call 0x1408e4f70
008DC625  48 83 C4 28                     add rsp, 0x28
008DC629  C3                              ret
008DC62A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqQueryDeleteObjectFromResultSet(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (72);
    result = RtlDeleteElementGenericTableAvl(a1, v_stack_p10, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_p10;
        result = PiDmObjectRelease(a1, v_stack_p10, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqQueryDeleteObjectFromResultSet(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (72);
    result = RtlDeleteElementGenericTableAvl(Arg1, v_stack_p10, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_p10;
        result = PiDmObjectRelease(Arg1, v_stack_p10, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DC600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008DC600[BB_008DC600]
  bb_008DC61B[BB_008DC61B]
  bb_008DC625[BB_008DC625]
  bb_008DC62A[BB_008DC62A]
  bb_008DC600 -->|branch| bb_008DC625
  bb_008DC600 -->|fallthrough| bb_008DC61B
  bb_008DC61B -->|flow| bb_008DC625
```
