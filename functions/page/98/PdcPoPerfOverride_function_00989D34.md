# PdcPoPerfOverride

- RVA: `0x00989D34`–`0x00989D54` (길이 `32` bytes)
- VA: `0x0000000140989D34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00989D38` → [PpmBeginHighPerfRequest](../../text/47/PpmBeginHighPerfRequest_function_004774FC.md) (function, `0x004774FC`)
- `0x00989D3F` → [PpmDisableHighPerfRequestDeferredExpiration](../../text/4B/PpmDisableHighPerfRequestDeferredExpiration_function_004BA678.md) (function, `0x004BA678`)
- `0x00989D49` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (function, `0x00477490`)

### Direct callers
- [PopPowerAggregatorModernStandbyExitStateHandler](PopPowerAggregatorModernStandbyExitStateHandler_function_00989D90.md) at `0x00989DBA`
- [PopPowerAggregatorEnterScreenOff](PopPowerAggregatorEnterScreenOff_function_00989F38.md) at `0x00989FD8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00989D38` → [PpmBeginHighPerfRequest](../../text/47/PpmBeginHighPerfRequest_function_004774FC.md) (`PAGE` → `.text`)
  - `0x00989D3F` → [PpmDisableHighPerfRequestDeferredExpiration](../../text/4B/PpmDisableHighPerfRequestDeferredExpiration_function_004BA678.md) (`PAGE` → `.text`)
  - `0x00989D49` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00989D34  48 83 EC 28                     sub rsp, 0x28
00989D38  E8 BF D7 AE FF                  call 0x1404774fc
00989D3D  33 C9                           xor ecx, ecx
00989D3F  E8 34 09 B3 FF                  call 0x1404ba678
00989D44  B9 01 00 00 00                  mov ecx, 1
00989D49  E8 42 D7 AE FF                  call 0x140477490
00989D4E  48 83 C4 28                     add rsp, 0x28
00989D52  C3                              ret
00989D53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PdcPoPerfOverride(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PpmBeginHighPerfRequest(a1, a2, a3, a4);
    a1 = 0;
    result = PpmDisableHighPerfRequestDeferredExpiration(a1, a2, a3, a4);
    result = PpmEndHighPerfRequest(1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PdcPoPerfOverride(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PpmBeginHighPerfRequest(Arg1, a2, a3, a4);
    Arg1 = 0;
    result = PpmDisableHighPerfRequestDeferredExpiration(Arg1, a2, a3, a4);
    result = PpmEndHighPerfRequest(1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00989D34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00989D34[BB_00989D34]
  bb_00989D53[BB_00989D53]
```
