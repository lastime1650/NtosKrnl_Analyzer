# PoUnregisterSystemState

- RVA: `0x004B9FA0`–`0x004B9FB6` (길이 `22` bytes)
- VA: `0x00000001404B9FA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `8`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B9FAF` → [PoDeletePowerRequest](../../page/A4/PoDeletePowerRequest_function_00A48F00.md) (function, `0x00A48F00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004B9FAF` → [PoDeletePowerRequest](../../page/A4/PoDeletePowerRequest_function_00A48F00.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B9FA0  48 83 EC 28                     sub rsp, 0x28
004B9FA4  48 85 C9                        test rcx, rcx
004B9FA7  75 06                           jne 0x1404b9faf
004B9FA9  48 83 C4 28                     add rsp, 0x28
004B9FAD  C3                              ret
004B9FAE  CC                              int3
004B9FAF  E8 4C EF 58 00                  call 0x140a48f00
004B9FB4  EB F3                           jmp 0x1404b9fa9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoUnregisterSystemState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_004B9FAF;
loc_004B9FA9:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004B9FAF:
    result = PoDeletePowerRequest(a1, a2, a3, a4);
    goto loc_004B9FA9;
}
```

## 5. (Beta) C Style

```c
int64_t PoUnregisterSystemState(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_004B9FAF;
loc_004B9FA9:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004B9FAF:
    result = PoDeletePowerRequest(Arg1, a2, a3, a4);
    goto loc_004B9FA9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B9FA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B9FA0[BB_004B9FA0]
  bb_004B9FA9[BB_004B9FA9]
  bb_004B9FAE[BB_004B9FAE]
  bb_004B9FAF[BB_004B9FAF]
  bb_004B9FA0 -->|branch| bb_004B9FAF
  bb_004B9FA0 -->|fallthrough| bb_004B9FA9
  bb_004B9FAE -->|flow| bb_004B9FAF
  bb_004B9FAF -->|branch| bb_004B9FA9
```
