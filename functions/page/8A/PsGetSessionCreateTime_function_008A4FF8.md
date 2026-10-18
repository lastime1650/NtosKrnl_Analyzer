# PsGetSessionCreateTime

- RVA: `0x008A4FF8`–`0x008A501D` (길이 `37` bytes)
- VA: `0x00000001408A4FF8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwQueryProcessTelemetryInfo](EtwQueryProcessTelemetryInfo_function_008A51A0.md) at `0x008A53D5`
- [EtwpWriteProcessStarted](../A4/EtwpWriteProcessStarted_function_00A487A4.md) at `0x00A4890C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A4FF8  48 8B 81 E8 02 00 00            mov rax, qword ptr [rcx + 0x2e8]
008A4FFF  48 85 C0                        test rax, rax
008A5002  74 15                           je 0x1408a5019
008A5004  F7 81 FC 05 00 00 00 10 00 00   test dword ptr [rcx + 0x5fc], 0x1000
008A500E  75 09                           jne 0x1408a5019
008A5010  48 8B 80 A8 00 00 00            mov rax, qword ptr [rax + 0xa8]
008A5017  C3                              ret
008A5018  CC                              int3
008A5019  33 C0                           xor eax, eax
008A501B  C3                              ret
008A501C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetSessionCreateTime(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 744) == 0) goto loc_008A5019;
    if (((*(unsigned int *)(a1 + 1532)) & (0x1000ULL)) != 0) goto loc_008A5019;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 744) + 168);
loc_008A5019:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetSessionCreateTime(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x2E8) == 0) goto loc_008A5019;
    if (((*(uint32_t *)(arg1 + 0x5FC)) & (0x1000ULL)) != 0) goto loc_008A5019;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x2E8) + 0xA8);
loc_008A5019:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2E8` | `64` | `R` |
| `Arg1` | `+ 0x5FC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A4FF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A4FF8[BB_008A4FF8]
  bb_008A5004[BB_008A5004]
  bb_008A5010[BB_008A5010]
  bb_008A5018[BB_008A5018]
  bb_008A5019[BB_008A5019]
  bb_008A501C[BB_008A501C]
  bb_008A4FF8 -->|branch| bb_008A5019
  bb_008A4FF8 -->|fallthrough| bb_008A5004
  bb_008A5004 -->|branch| bb_008A5019
  bb_008A5004 -->|fallthrough| bb_008A5010
  bb_008A5018 -->|flow| bb_008A5019
```
