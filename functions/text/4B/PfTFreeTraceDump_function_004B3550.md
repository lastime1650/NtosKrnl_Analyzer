# PfTFreeTraceDump

- RVA: `0x004B3550`–`0x004B3574` (길이 `36` bytes)
- VA: `0x00000001404B3550`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `12`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B3562` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004B356D` → [PfpRepurposeNameLoggingTrace](../../page/AA/PfpRepurposeNameLoggingTrace_function_00AA3C34.md) (function, `0x00AA3C34`)

### Direct callers
- [PfGetCompletedTrace](../../page/90/PfGetCompletedTrace_function_00902950.md) at `0x00902C51`
- [PfTTraceListFree](../../page/A6/PfTTraceListFree_function_00A60FA4.md) at `0x00A60FE9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004B3562` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004B356D` → [PfpRepurposeNameLoggingTrace](../../page/AA/PfpRepurposeNameLoggingTrace_function_00AA3C34.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B3550  48 83 EC 28                     sub rsp, 0x28
004B3554  83 7A 1C 01                     cmp dword ptr [rdx + 0x1c], 1
004B3558  48 8B C2                        mov rax, rdx
004B355B  74 10                           je 0x1404b356d
004B355D  33 D2                           xor edx, edx
004B355F  48 8B C8                        mov rcx, rax
004B3562  E8 09 F3 6C 00                  call 0x140b82870
004B3567  48 83 C4 28                     add rsp, 0x28
004B356B  C3                              ret
004B356C  CC                              int3
004B356D  E8 C2 06 5F 00                  call 0x140aa3c34
004B3572  EB F3                           jmp 0x1404b3567
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfTFreeTraceDump(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(a2 + 28)) == 1) goto loc_004B356D;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, a4);
loc_004B3567:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004B356D:
    result = PfpRepurposeNameLoggingTrace(0, a2, a3, a4);
    goto loc_004B3567;
}
```

## 5. (Beta) C Style

```c
int64_t PfTFreeTraceDump(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(arg2 + 0x1C)) == 1) goto loc_004B356D;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, a3, a4);
loc_004B3567:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004B356D:
    result = PfpRepurposeNameLoggingTrace(0, Arg2, a3, a4);
    goto loc_004B3567;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B3550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B3550[BB_004B3550]
  bb_004B355D[BB_004B355D]
  bb_004B3567[BB_004B3567]
  bb_004B356C[BB_004B356C]
  bb_004B356D[BB_004B356D]
  bb_004B3550 -->|branch| bb_004B356D
  bb_004B3550 -->|fallthrough| bb_004B355D
  bb_004B355D -->|flow| bb_004B3567
  bb_004B356C -->|flow| bb_004B356D
  bb_004B356D -->|branch| bb_004B3567
```
