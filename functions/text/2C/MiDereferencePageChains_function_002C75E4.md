# MiDereferencePageChains

- RVA: `0x002C75E4`–`0x002C7604` (길이 `32` bytes)
- VA: `0x00000001402C75E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C75FD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiRevertProcessorMove](MiRevertProcessorMove_function_002C7420.md) at `0x002C7464`
- [MiInitializeMdlOneNodeBatchPages](MiInitializeMdlOneNodeBatchPages_function_002C9480.md) at `0x002C9643`
- [MiProcessPageGroupInfo](../37/MiProcessPageGroupInfo_function_00376910.md) at `0x00376980`
- [MiGroupZeroHugeRange](../68/MiGroupZeroHugeRange_function_0068C384.md) at `0x0068C465`
- [MiFindLargePageMemory](../../page/AA/MiFindLargePageMemory_function_00AA8334.md) at `0x00AA8658`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002C75FD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C75E4  48 83 EC 28                     sub rsp, 0x28
002C75E8  83 C8 FF                        or eax, 0xffffffff
002C75EB  F0 0F C1 41 70                  lock xadd dword ptr [rcx + 0x70], eax
002C75F0  83 F8 01                        cmp eax, 1
002C75F3  74 06                           je 0x1402c75fb
002C75F5  48 83 C4 28                     add rsp, 0x28
002C75F9  C3                              ret
002C75FA  CC                              int3
002C75FB  33 D2                           xor edx, edx
002C75FD  E8 6E B2 8B 00                  call 0x140b82870
002C7602  EB F1                           jmp 0x1402c75f5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDereferencePageChains(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) goto loc_002C75FB;
loc_002C75F5:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002C75FB:
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    goto loc_002C75F5;
}
```

## 5. (Beta) C Style

```c
int64_t MiDereferencePageChains(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) goto loc_002C75FB;
loc_002C75F5:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002C75FB:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    goto loc_002C75F5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x70` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C75E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C75E4[BB_002C75E4]
  bb_002C75F5[BB_002C75F5]
  bb_002C75FA[BB_002C75FA]
  bb_002C75FB[BB_002C75FB]
  bb_002C75E4 -->|branch| bb_002C75FB
  bb_002C75E4 -->|fallthrough| bb_002C75F5
  bb_002C75FA -->|flow| bb_002C75FB
  bb_002C75FB -->|branch| bb_002C75F5
```
