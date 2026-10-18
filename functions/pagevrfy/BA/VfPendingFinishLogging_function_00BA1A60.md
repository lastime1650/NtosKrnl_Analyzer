# VfPendingFinishLogging

- RVA: `0x00BA1A60`–`0x00BA1A9C` (길이 `60` bytes)
- VA: `0x0000000140BA1A60`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA1A7D` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)

### Direct callers
- [IovpCallDriver1](../B9/IovpCallDriver1_function_00B9CCA4.md) at `0x00B9D246`
- [sub_00BBBCB2](../BB/Unknown_function_00BBBCB2.md) at `0x00BBBD57`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA1A7D` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA1A60  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BA1A65  57                              push rdi
00BA1A66  48 83 EC 20                     sub rsp, 0x20
00BA1A6A  45 33 C9                        xor r9d, r9d
00BA1A6D  4C 8D 41 10                     lea r8, [rcx + 0x10]
00BA1A71  48 8B D9                        mov rbx, rcx
00BA1A74  41 8D 79 3E                     lea edi, [r9 + 0x3e]
00BA1A78  8B D7                           mov edx, edi
00BA1A7A  8D 4F C3                        lea ecx, [rdi - 0x3d]
00BA1A7D  E8 6E 85 75 FF                  call 0x1402f9ff0
00BA1A82  66 3B C7                        cmp ax, di
00BA1A85  73 09                           jae 0x140ba1a90
00BA1A87  0F B7 C0                        movzx eax, ax
00BA1A8A  48 83 64 C3 10 00               and qword ptr [rbx + rax*8 + 0x10], 0
00BA1A90  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BA1A95  48 83 C4 20                     add rsp, 0x20
00BA1A99  5F                              pop rdi
00BA1A9A  C3                              ret
00BA1A9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfPendingFinishLogging(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a4 = 0;
    result = RtlCaptureStackBackTrace(a4 + 62 - 61, (unsigned int)((unsigned int)(a4 + 62)), a1 + 16, a4);
    if (((unsigned __int16)(result)) < ((unsigned __int16)(a4 + 62))) {
        result = (unsigned __int16)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfPendingFinishLogging(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg4 = 0;
    result = RtlCaptureStackBackTrace(Arg4 + 62 - 61, (uint32_t)((uint32_t)(Arg4 + 62)), Arg1 + 16, Arg4);
    if (((uint16_t)(result)) < ((uint16_t)(Arg4 + 62))) {
        result = (uint16_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10 + rax*8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA1A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA1A60[BB_00BA1A60]
  bb_00BA1A87[BB_00BA1A87]
  bb_00BA1A90[BB_00BA1A90]
  bb_00BA1A9B[BB_00BA1A9B]
  bb_00BA1A60 -->|branch| bb_00BA1A90
  bb_00BA1A60 -->|fallthrough| bb_00BA1A87
  bb_00BA1A87 -->|flow| bb_00BA1A90
```
