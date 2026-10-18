# CmpLightWeightCleanupSetSecDescUoW

- RVA: `0x0094B374`–`0x0094B3A3` (길이 `47` bytes)
- VA: `0x000000014094B374`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FBDC`
- 디코드: `16`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094B38C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0094B39C` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (function, `0x004A672C`)

### Direct callers
- [CmpLightWeightPrepareSetSecDescUoW](CmpLightWeightPrepareSetSecDescUoW_function_0094B098.md) at `0x0094B316`
- [CmpLightWeightCommitSetSecDescUoW](CmpLightWeightCommitSetSecDescUoW_function_0094B4AC.md) at `0x0094B5D0`
- [CmpCleanupLightWeightUoWData](../9B/CmpCleanupLightWeightUoWData_function_009B0A68.md) at `0x009B0ABE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0094B38C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0094B39C` → [CmpDereferenceSecurityNode](../../text/4A/CmpDereferenceSecurityNode_function_004A672C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094B374  40 53                           push rbx
0094B376  48 83 EC 20                     sub rsp, 0x20
0094B37A  8B 11                           mov edx, dword ptr [rcx]
0094B37C  48 8B D9                        mov rbx, rcx
0094B37F  83 FA FF                        cmp edx, -1
0094B382  75 14                           jne 0x14094b398
0094B384  BA 43 4D 55 77                  mov edx, 0x77554d43
0094B389  48 8B CB                        mov rcx, rbx
0094B38C  E8 DF 74 23 00                  call 0x140b82870
0094B391  48 83 C4 20                     add rsp, 0x20
0094B395  5B                              pop rbx
0094B396  C3                              ret
0094B397  CC                              int3
0094B398  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0094B39C  E8 8B B3 B5 FF                  call 0x1404a672c
0094B3A1  EB E1                           jmp 0x14094b384
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLightWeightCleanupSetSecDescUoW(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) != -1) goto loc_0094B398;
loc_0094B384:
    result = ExFreePoolWithTag(a1, (unsigned int)(0x77554D43ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0094B398:
    result = CmpDereferenceSecurityNode(*(unsigned __int64 *)(a1 + 8), (unsigned int)(0x77554D43ULL), a3, a4);
    goto loc_0094B384;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLightWeightCleanupSetSecDescUoW(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) != -1) goto loc_0094B398;
loc_0094B384:
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x77554D43ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0094B398:
    result = CmpDereferenceSecurityNode(*(uint64_t *)(arg1 + 0x8), (uint32_t)(0x77554D43ULL), a3, a4);
    goto loc_0094B384;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094B374&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094B374[BB_0094B374]
  bb_0094B384[BB_0094B384]
  bb_0094B397[BB_0094B397]
  bb_0094B398[BB_0094B398]
  bb_0094B374 -->|branch| bb_0094B398
  bb_0094B374 -->|fallthrough| bb_0094B384
  bb_0094B397 -->|flow| bb_0094B398
  bb_0094B398 -->|branch| bb_0094B384
```
