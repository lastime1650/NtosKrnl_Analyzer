# EtwpCCSwapDeleteProcessor

- RVA: `0x00654598`–`0x006545D3` (길이 `59` bytes)
- VA: `0x0000000140654598`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `18`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006545B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwDeleteProcessor](../../page/7B/EtwDeleteProcessor_function_007B4CC0.md) at `0x007B4D15`
- [EtwInitializeProcessor](../../page/7B/EtwInitializeProcessor_function_007B4EBC.md) at `0x007B4FA8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006545B8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00654598  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0065459D  57                              push rdi
0065459E  48 83 EC 20                     sub rsp, 0x20
006545A2  48 8D 99 98 01 00 00            lea rbx, [rcx + 0x198]
006545A9  BF 05 00 00 00                  mov edi, 5
006545AE  48 8B 0B                        mov rcx, qword ptr [rbx]
006545B1  48 85 C9                        test rcx, rcx
006545B4  74 07                           je 0x1406545bd
006545B6  33 D2                           xor edx, edx
006545B8  E8 B3 E2 52 00                  call 0x140b82870
006545BD  48 83 C3 08                     add rbx, 8
006545C1  48 83 EF 01                     sub rdi, 1
006545C5  75 E7                           jne 0x1406545ae
006545C7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
006545CC  48 83 C4 20                     add rsp, 0x20
006545D0  5F                              pop rdi
006545D1  C3                              ret
006545D2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCCSwapDeleteProcessor(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
loc_006545AE:
    if (*(unsigned __int64 *)(a1 + 408) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 408), a2, a3, a4);
    }
    v_rbx = (a1 + 408) + (8);
    v_rdi = (5) - (1);
    if (condition_is_not_equal) goto loc_006545AE;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCCSwapDeleteProcessor(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
loc_006545AE:
    if (*(uint64_t *)(arg1 + 0x198) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x198), Arg2, a3, a4);
    }
    local_rbx = (Arg1 + 408) + (8);
    local_rdi = (5) - (1);
    if (condition_is_not_equal) goto loc_006545AE;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x198` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00654598&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00654598[BB_00654598]
  bb_006545AE[BB_006545AE]
  bb_006545B6[BB_006545B6]
  bb_006545BD[BB_006545BD]
  bb_006545C7[BB_006545C7]
  bb_006545D2[BB_006545D2]
  bb_00654598 -->|flow| bb_006545AE
  bb_006545AE -->|branch| bb_006545BD
  bb_006545AE -->|fallthrough| bb_006545B6
  bb_006545B6 -->|flow| bb_006545BD
  bb_006545BD -->|branch| bb_006545AE
  bb_006545BD -->|fallthrough| bb_006545C7
```
