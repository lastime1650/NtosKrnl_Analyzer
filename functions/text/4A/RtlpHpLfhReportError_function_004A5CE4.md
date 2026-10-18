# RtlpHpLfhReportError

- RVA: `0x004A5CE4`–`0x004A5D0B` (길이 `39` bytes)
- VA: `0x00000001404A5CE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A5D00` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)

### Direct callers
- [RtlpHpLfhSubsegmentDelayFreeListBatch](../47/RtlpHpLfhSubsegmentDelayFreeListBatch_function_004792F4.md) at `0x004794B6`
- [RtlpHpLfhSubsegmentDelayFreeListBatch](../47/RtlpHpLfhSubsegmentDelayFreeListBatch_function_004792F4.md) at `0x004794D5`
- [RtlpHpLfhSubsegmentDelayFreeListBatch](../47/RtlpHpLfhSubsegmentDelayFreeListBatch_function_004792F4.md) at `0x00479516`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A5CE4  48 83 EC 38                     sub rsp, 0x38
004A5CE8  83 F9 11                        cmp ecx, 0x11
004A5CEB  75 03                           jne 0x1404a5cf0
004A5CED  48 8B 12                        mov rdx, qword ptr [rdx]
004A5CF0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004A5CF5  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004A5CFB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004A5D00  E8 B7 5A EB FF                  call 0x14035b7bc
004A5D05  48 83 C4 38                     add rsp, 0x38
004A5D09  C3                              ret
004A5D0A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpLfhReportError(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (a1 == 17) {
        a2 = *(unsigned __int64 *)(a2);
    }
    v_stack_m18 = a5;
    result = RtlpLogHeapFailure(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpLfhReportError(int32_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (Arg1 == 17) {
        Arg2 = *(uint64_t *)(arg2);
    }
    v_stack_m18 = Arg5;
    result = RtlpLogHeapFailure(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A5CE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A5CE4[BB_004A5CE4]
  bb_004A5CED[BB_004A5CED]
  bb_004A5CF0[BB_004A5CF0]
  bb_004A5D0A[BB_004A5D0A]
  bb_004A5CE4 -->|branch| bb_004A5CF0
  bb_004A5CE4 -->|fallthrough| bb_004A5CED
  bb_004A5CED -->|flow| bb_004A5CF0
```
