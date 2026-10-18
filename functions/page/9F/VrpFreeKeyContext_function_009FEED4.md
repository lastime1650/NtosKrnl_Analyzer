# VrpFreeKeyContext

- RVA: `0x009FEED4`–`0x009FEF04` (길이 `48` bytes)
- VA: `0x00000001409FEED4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009FEEDD` → [VrpDecommissionKeyContext](VrpDecommissionKeyContext_function_009FEF0C.md) (function, `0x009FEF0C`)
- `0x009FEEEB` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x009FEEF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [VrpRegistryCallback](../86/VrpRegistryCallback_function_00867450.md) at `0x00867599`
- [VrpHandleIoctlInitializeJobForVreg](../93/VrpHandleIoctlInitializeJobForVreg_function_00937254.md) at `0x00937572`
- [VrpPreLoadKey](../A8/VrpPreLoadKey_function_00A8A43C.md) at `0x00A8A852`
- [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) at `0x00B24E05`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009FEEEB` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x009FEEF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FEED4  40 53                           push rbx
009FEED6  48 83 EC 20                     sub rsp, 0x20
009FEEDA  48 8B D9                        mov rbx, rcx
009FEEDD  E8 2A 00 00 00                  call 0x1409fef0c
009FEEE2  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
009FEEE6  BA 56 52 65 67                  mov edx, 0x67655256
009FEEEB  E8 B0 4F 86 FF                  call 0x140263ea0
009FEEF0  BA 56 52 65 67                  mov edx, 0x67655256
009FEEF5  48 8B CB                        mov rcx, rbx
009FEEF8  E8 73 39 18 00                  call 0x140b82870
009FEEFD  48 83 C4 20                     add rsp, 0x20
009FEF01  5B                              pop rbx
009FEF02  C3                              ret
009FEF03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpFreeKeyContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VrpDecommissionKeyContext(a1, a2, a3, a4);
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(a1 + 40), (unsigned int)(0x67655256ULL), a3, a4);
    result = ExFreePoolWithTag(a1, (unsigned int)(0x67655256ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VrpFreeKeyContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VrpDecommissionKeyContext(Arg1, a2, a3, a4);
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(arg1 + 0x28), (uint32_t)(0x67655256ULL), a3, a4);
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x67655256ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FEED4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FEED4[BB_009FEED4]
  bb_009FEF03[BB_009FEF03]
```
