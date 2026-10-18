# PfSnPowerBoostWorker

- RVA: `0x007523C0`–`0x007523DF` (길이 `31` bytes)
- VA: `0x00000001407523C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007523CB` → [PfSnPowerBoostUpdate](../A9/PfSnPowerBoostUpdate_function_00A952C4.md) (function, `0x00A952C4`)
- `0x007523D3` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007523D3` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007523C0  40 53                           push rbx
007523C2  48 83 EC 20                     sub rsp, 0x20
007523C6  48 8B D9                        mov rbx, rcx
007523C9  33 C9                           xor ecx, ecx
007523CB  E8 F4 2E 34 00                  call 0x140a952c4
007523D0  48 8B CB                        mov rcx, rbx
007523D3  E8 A8 7A BF FF                  call 0x140349e80
007523D8  48 83 C4 20                     add rsp, 0x20
007523DC  5B                              pop rbx
007523DD  C3                              ret
007523DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnPowerBoostWorker(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = PfSnPowerBoostUpdate(a1, a2, a3, a4);
    result = ExReleaseRundownProtection(0, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnPowerBoostWorker(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = PfSnPowerBoostUpdate(Arg1, a2, a3, a4);
    result = ExReleaseRundownProtection(0, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007523C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007523C0[BB_007523C0]
  bb_007523DE[BB_007523DE]
```
