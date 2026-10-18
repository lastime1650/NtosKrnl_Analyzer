# PopPowerRequestStatsFreeId

- RVA: `0x00A2D74C`–`0x00A2D77D` (길이 `49` bytes)
- VA: `0x0000000140A2D74C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2D764` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2D771` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopPowerRequestStatsCreate](PopPowerRequestStatsCreate_function_00A2D6DC.md) at `0x00A2D73A`
- [PopPowerRequestStatsGetIdForRequest](PopPowerRequestStatsGetIdForRequest_function_00A2D784.md) at `0x00A2D923`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A2D764` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2D771` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2D74C  40 53                           push rbx
00A2D74E  48 83 EC 20                     sub rsp, 0x20
00A2D752  8B 01                           mov eax, dword ptr [rcx]
00A2D754  48 8B D9                        mov rbx, rcx
00A2D757  A8 02                           test al, 2
00A2D759  74 0E                           je 0x140a2d769
00A2D75B  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A2D75F  BA 50 57 51 54                  mov edx, 0x54515750
00A2D764  E8 07 51 15 00                  call 0x140b82870
00A2D769  BA 50 57 51 54                  mov edx, 0x54515750
00A2D76E  48 8B CB                        mov rcx, rbx
00A2D771  E8 FA 50 15 00                  call 0x140b82870
00A2D776  48 83 C4 20                     add rsp, 0x20
00A2D77A  5B                              pop rbx
00A2D77B  C3                              ret
00A2D77C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestStatsFreeId(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = 0x54515750ULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExFreePoolWithTag(a1, (unsigned int)(0x54515750ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerRequestStatsFreeId(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        a2 = 0x54515750ULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x54515750ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2D74C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2D74C[BB_00A2D74C]
  bb_00A2D75B[BB_00A2D75B]
  bb_00A2D769[BB_00A2D769]
  bb_00A2D77C[BB_00A2D77C]
  bb_00A2D74C -->|branch| bb_00A2D769
  bb_00A2D74C -->|fallthrough| bb_00A2D75B
  bb_00A2D75B -->|flow| bb_00A2D769
```
