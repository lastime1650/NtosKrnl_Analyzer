# PiPdcDeactivate

- RVA: `0x009552C4`–`0x009552D8` (길이 `20` bytes)
- VA: `0x00000001409552C4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009552CD` → [Pdcv2ActivationClientDeactivate](Pdcv2ActivationClientDeactivate_function_009552E0.md) (function, `0x009552E0`)

### Direct callers
- [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) at `0x004783E6`
- [PnpDeleteDeviceActionRequest](PnpDeleteDeviceActionRequest_function_00955284.md) at `0x0095529E`
- [PnpCompleteDeviceEvent](PnpCompleteDeviceEvent_function_00955548.md) at `0x00955585`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009552C4  48 83 EC 28                     sub rsp, 0x28
009552C8  48 85 C9                        test rcx, rcx
009552CB  74 05                           je 0x1409552d2
009552CD  E8 0E 00 00 00                  call 0x1409552e0
009552D2  48 83 C4 28                     add rsp, 0x28
009552D6  C3                              ret
009552D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPdcDeactivate(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        result = Pdcv2ActivationClientDeactivate(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiPdcDeactivate(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        result = Pdcv2ActivationClientDeactivate(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009552C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009552C4[BB_009552C4]
  bb_009552CD[BB_009552CD]
  bb_009552D2[BB_009552D2]
  bb_009552D7[BB_009552D7]
  bb_009552C4 -->|branch| bb_009552D2
  bb_009552C4 -->|fallthrough| bb_009552CD
  bb_009552CD -->|flow| bb_009552D2
```
