# PfpRepurposeNameLoggingTrace

- RVA: `0x00AA3C34`–`0x00AA3C5A` (길이 `38` bytes)
- VA: `0x0000000140AA3C34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AA3C4F` → [PfFbBufferListInsertInFree](../../text/48/PfFbBufferListInsertInFree_function_00484210.md) (function, `0x00484210`)

### Direct callers
- [PfTFreeTraceDump](../../text/4B/PfTFreeTraceDump_function_004B3550.md) at `0x004B356D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AA3C4F` → [PfFbBufferListInsertInFree](../../text/48/PfFbBufferListInsertInFree_function_00484210.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA3C34  48 83 EC 38                     sub rsp, 0x38
00AA3C38  44 8B 4A 38                     mov r9d, dword ptr [rdx + 0x38]
00AA3C3C  48 81 C1 20 01 00 00            add rcx, 0x120
00AA3C43  44 8B 42 34                     mov r8d, dword ptr [rdx + 0x34]
00AA3C47  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AA3C4F  E8 BC 05 9E FF                  call 0x140484210
00AA3C54  48 83 C4 38                     add rsp, 0x38
00AA3C58  C3                              ret
00AA3C59  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpRepurposeNameLoggingTrace(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a1 = (a1) + (288);
    v_stack_m18 = 1;
    result = PfFbBufferListInsertInFree(a1, a2, (unsigned int)(*(unsigned int *)(a2 + 52)), (unsigned int)(*(unsigned int *)(a2 + 56)));
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpRepurposeNameLoggingTrace(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg1 = (Arg1) + (288);
    v_stack_m18 = 1;
    result = PfFbBufferListInsertInFree(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x34)), (uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x34` | `32` | `R` |
| `Arg2` | `+ 0x38` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA3C34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA3C34[BB_00AA3C34]
  bb_00AA3C59[BB_00AA3C59]
```
