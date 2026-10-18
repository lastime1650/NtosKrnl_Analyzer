# HalFreeAdapterObject

- RVA: `0x003DA9F0`–`0x003DAA10` (길이 `32` bytes)
- VA: `0x00000001403DA9F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DAA05` → [IoFreeAdapterChannelV3](IoFreeAdapterChannelV3_function_003DAA20.md) (function, `0x003DAA20`)

### Direct callers
- [HalpAllocateDmaResourcesInternal](HalpAllocateDmaResourcesInternal_function_003DA7C4.md) at `0x003DA8E2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DA9F0  48 83 EC 28                     sub rsp, 0x28
003DA9F4  83 FA 02                        cmp edx, 2
003DA9F7  74 0C                           je 0x1403daa05
003DA9F9  83 FA 03                        cmp edx, 3
003DA9FC  75 0C                           jne 0x1403daa0a
003DA9FE  83 A1 F8 00 00 00 00            and dword ptr [rcx + 0xf8], 0
003DAA05  E8 16 00 00 00                  call 0x1403daa20
003DAA0A  48 83 C4 28                     add rsp, 0x28
003DAA0E  C3                              ret
003DAA0F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalFreeAdapterObject(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 2) goto loc_003DAA05;
    if (a2 != 3) goto loc_003DAA0A;
loc_003DAA05:
    result = IoFreeAdapterChannelV3(a1, a2, a3, a4);
loc_003DAA0A:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalFreeAdapterObject(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 2) goto loc_003DAA05;
    if (Arg2 != 3) goto loc_003DAA0A;
loc_003DAA05:
    result = IoFreeAdapterChannelV3(Arg1, Arg2, a3, a4);
loc_003DAA0A:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DA9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DA9F0[BB_003DA9F0]
  bb_003DA9F9[BB_003DA9F9]
  bb_003DA9FE[BB_003DA9FE]
  bb_003DAA05[BB_003DAA05]
  bb_003DAA0A[BB_003DAA0A]
  bb_003DAA0F[BB_003DAA0F]
  bb_003DA9F0 -->|branch| bb_003DAA05
  bb_003DA9F0 -->|fallthrough| bb_003DA9F9
  bb_003DA9F9 -->|branch| bb_003DAA0A
  bb_003DA9F9 -->|fallthrough| bb_003DA9FE
  bb_003DA9FE -->|flow| bb_003DAA05
  bb_003DAA05 -->|flow| bb_003DAA0A
```
