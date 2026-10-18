# RtlGenerateQpcToIncrementConstants

- RVA: `0x004BCB20`–`0x004BCB7F` (길이 `95` bytes)
- VA: `0x00000001404BCB20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FC80`
- 디코드: `32`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BCB3A` → [RtlpComputeFraction](../4F/RtlpComputeFraction_function_004FC140.md) (function, `0x004FC140`)

### Direct callers
- [KeSetTimeAdjustment](../23/KeSetTimeAdjustment_function_00235670.md) at `0x002356B9`
- [KiSetupTimeIncrement](../5B/KiSetupTimeIncrement_function_005B2244.md) at `0x005B230B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BCB20  40 53                           push rbx
004BCB22  48 83 EC 20                     sub rsp, 0x20
004BCB26  48 8B DA                        mov rbx, rdx
004BCB29  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
004BCB2E  8B D1                           mov edx, ecx
004BCB30  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
004BCB35  B9 80 96 98 00                  mov ecx, 0x989680
004BCB3A  E8 01 F6 03 00                  call 0x1404fc140
004BCB3F  4C 8B C8                        mov r9, rax
004BCB42  0F BE 44 24 38                  movsx eax, byte ptr [rsp + 0x38]
004BCB47  84 C0                           test al, al
004BCB49  78 0C                           js 0x1404bcb57
004BCB4B  88 03                           mov byte ptr [rbx], al
004BCB4D  49 8B C1                        mov rax, r9
004BCB50  48 83 C4 20                     add rsp, 0x20
004BCB54  5B                              pop rbx
004BCB55  C3                              ret
004BCB56  CC                              int3
004BCB57  8B C8                           mov ecx, eax
004BCB59  BA 01 00 00 00                  mov edx, 1
004BCB5E  F7 D1                           not ecx
004BCB60  44 8B C0                        mov r8d, eax
004BCB63  D3 E2                           shl edx, cl
004BCB65  49 03 D1                        add rdx, r9
004BCB68  49 3B D1                        cmp rdx, r9
004BCB6B  49 0F 42 D1                     cmovb rdx, r9
004BCB6F  41 F7 D8                        neg r8d
004BCB72  41 8A C8                        mov cl, r8b
004BCB75  4C 8B CA                        mov r9, rdx
004BCB78  49 D3 E9                        shr r9, cl
004BCB7B  32 C0                           xor al, al
004BCB7D  EB CC                           jmp 0x1404bcb4b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGenerateQpcToIncrementConstants(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;

    v_rsp = (v_rsp) - (32);
    v_stack_p10 = 0;
    result = RtlpComputeFraction((unsigned int)(0x989680ULL), (unsigned int)(a1), v_stack_p10, a4);
    if (sign_flag) goto loc_004BCB57;
loc_004BCB4B:
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(v_stack_p10));
    v_rsp = (v_rsp) + (32);
    return result;
loc_004BCB57:
    a1 = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    a2 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a2 = (a2) + (result);
    if (a2 < result) { a2 = result; }
    a3 = (unsigned int)(-((unsigned int)((unsigned int)(result))));
    a4 = (a2) >> ((unsigned __int8)((unsigned __int8)(a3)));
    result = 0;
    goto loc_004BCB4B;
}
```

## 5. (Beta) C Style

```c
int64_t RtlGenerateQpcToIncrementConstants(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p10;

    local_rsp = (local_rsp) - (32);
    v_stack_p10 = 0;
    result = RtlpComputeFraction((uint32_t)(0x989680ULL), (uint32_t)(Arg1), v_stack_p10, a4);
    if (sign_flag) goto loc_004BCB57;
loc_004BCB4B:
    *(uint8_t *)(arg2) = (uint8_t)((int8_t)(v_stack_p10));
    local_rsp = (local_rsp) + (32);
    return result;
loc_004BCB57:
    Arg1 = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    Arg2 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg2 = (Arg2) + (result);
    if (Arg2 < result) { Arg2 = result; }
    a3 = (uint32_t)(-((uint32_t)((uint32_t)(result))));
    a4 = (Arg2) >> ((uint8_t)((uint8_t)(a3)));
    result = 0;
    goto loc_004BCB4B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BCB20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BCB20[BB_004BCB20]
  bb_004BCB4B[BB_004BCB4B]
  bb_004BCB56[BB_004BCB56]
  bb_004BCB57[BB_004BCB57]
  bb_004BCB20 -->|branch| bb_004BCB57
  bb_004BCB20 -->|fallthrough| bb_004BCB4B
  bb_004BCB56 -->|flow| bb_004BCB57
  bb_004BCB57 -->|branch| bb_004BCB4B
```
