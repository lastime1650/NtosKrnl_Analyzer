# EtwpCoverageSamplerFreeTable

- RVA: `0x00A878A4`–`0x00A878D9` (길이 `53` bytes)
- VA: `0x0000000140A878A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A878BB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A878CD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpCoverageSamplerCleanup](../7C/EtwpCoverageSamplerCleanup_function_007C1E80.md) at `0x007C1ECC`
- [EtwpCovSampContextAddSamples](../8D/EtwpCovSampContextAddSamples_function_008D7C9C.md) at `0x008D7F13`
- [EtwpCovSampHashMakeRoomAndAcquireLock](../8D/EtwpCovSampHashMakeRoomAndAcquireLock_function_008D91F8.md) at `0x008D9442`
- [sub_00B27A94](../B2/Unknown_function_00B27A94.md) at `0x00B27AD5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A878BB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A878CD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A878A4  40 53                           push rbx
00A878A6  48 83 EC 20                     sub rsp, 0x20
00A878AA  48 8B D9                        mov rbx, rcx
00A878AD  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00A878B1  48 85 C9                        test rcx, rcx
00A878B4  74 0F                           je 0x140a878c5
00A878B6  BA 45 74 77 56                  mov edx, 0x56777445
00A878BB  E8 B0 AF 0F 00                  call 0x140b82870
00A878C0  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
00A878C5  BA 45 74 77 56                  mov edx, 0x56777445
00A878CA  48 8B CB                        mov rcx, rbx
00A878CD  E8 9E AF 0F 00                  call 0x140b82870
00A878D2  48 83 C4 20                     add rsp, 0x20
00A878D6  5B                              pop rbx
00A878D7  C3                              ret
00A878D8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCoverageSamplerFreeTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = 0x56777445ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    result = ExFreePoolWithTag(a1, (unsigned int)(0x56777445ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCoverageSamplerFreeTable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        a2 = 0x56777445ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x18), a2, a3, a4);
    }
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x56777445ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A878A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A878A4[BB_00A878A4]
  bb_00A878B6[BB_00A878B6]
  bb_00A878C5[BB_00A878C5]
  bb_00A878D8[BB_00A878D8]
  bb_00A878A4 -->|branch| bb_00A878C5
  bb_00A878A4 -->|fallthrough| bb_00A878B6
  bb_00A878B6 -->|flow| bb_00A878C5
```
