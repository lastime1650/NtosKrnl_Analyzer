# PspSendJobNotification

- RVA: `0x0049EC28`–`0x0049EC64` (길이 `60` bytes)
- VA: `0x000000014049EC28`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `16`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049EC4C` → [IoSetIoCompletion](../../page/9F/IoSetIoCompletion_function_009FDCA0.md) (function, `0x009FDCA0`)

### Direct callers
- [PspCompleteServerSiloShutdownDeferred](../../page/77/PspCompleteServerSiloShutdownDeferred_function_0077F860.md) at `0x0077F97C`
- [PsReportProcessMemoryLimitViolation](../../page/78/PsReportProcessMemoryLimitViolation_function_00784A5C.md) at `0x00784AE1`
- [PspValidateJobAssignmentProcessLimits](../../page/87/PspValidateJobAssignmentProcessLimits_function_0087DDA8.md) at `0x0087DE63`
- [PspIncrementJobChainProcessCounts](../../page/87/PspIncrementJobChainProcessCounts_function_0087E0B4.md) at `0x0087E164`
- [sub_0087F483](../../page/87/Unknown_function_0087F483.md) at `0x0087F501`
- [PspRemoveProcessFromJobChain](../../page/90/PspRemoveProcessFromJobChain_function_00907288.md) at `0x00907423`
- [PspSendProcessNotificationToJobChain](../../page/A4/PspSendProcessNotificationToJobChain_function_00A45ADC.md) at `0x00A45BAA`
- [PspAssociateCompletionPortCallback](../../page/A8/PspAssociateCompletionPortCallback_function_00A83290.md) at `0x00A832C8`
- [sub_00B21AB8](../../page/B2/Unknown_function_00B21AB8.md) at `0x00B21B16`
- [sub_00B21AB8](../../page/B2/Unknown_function_00B21AB8.md) at `0x00B21B99`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0049EC4C` → [IoSetIoCompletion](../../page/9F/IoSetIoCompletion_function_009FDCA0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049EC28  40 53                           push rbx
0049EC2A  48 83 EC 30                     sub rsp, 0x30
0049EC2E  44 88 4C 24 28                  mov byte ptr [rsp + 0x28], r9b
0049EC33  48 8B D9                        mov rbx, rcx
0049EC36  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0049EC3B  45 33 C9                        xor r9d, r9d
0049EC3E  48 8B 91 30 02 00 00            mov rdx, qword ptr [rcx + 0x230]
0049EC45  48 8B 89 28 02 00 00            mov rcx, qword ptr [rcx + 0x228]
0049EC4C  E8 4F F0 55 00                  call 0x1409fdca0
0049EC51  85 C0                           test eax, eax
0049EC53  78 08                           js 0x14049ec5d
0049EC55  F0 48 FF 83 38 02 00 00         lock inc qword ptr [rbx + 0x238]
0049EC5D  48 83 C4 30                     add rsp, 0x30
0049EC61  5B                              pop rbx
0049EC62  C3                              ret
0049EC63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspSendJobNotification(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m10 = (unsigned __int8)(a4);
    v_stack_m18 = a2;
    a4 = 0;
    result = IoSetIoCompletion(*(unsigned __int64 *)(a1 + 552), *(unsigned __int64 *)(a1 + 560), a3, a4);
    if (!(sign_flag)) {
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspSendJobNotification(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m10 = (uint8_t)(Arg4);
    v_stack_m18 = Arg2;
    Arg4 = 0;
    result = IoSetIoCompletion(*(uint64_t *)(arg1 + 0x228), *(uint64_t *)(arg1 + 0x230), Arg3, Arg4);
    if (!(sign_flag)) {
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x228` | `64` | `R` |
| `Arg1` | `+ 0x230` | `64` | `R` |
| `Arg1` | `+ 0x238` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049EC28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049EC28[BB_0049EC28]
  bb_0049EC55[BB_0049EC55]
  bb_0049EC5D[BB_0049EC5D]
  bb_0049EC63[BB_0049EC63]
  bb_0049EC28 -->|branch| bb_0049EC5D
  bb_0049EC28 -->|fallthrough| bb_0049EC55
  bb_0049EC55 -->|flow| bb_0049EC5D
```
