# CcTelemetryPeriodicTimerDpc

- RVA: `0x004CDEB0`–`0x004CDEE6` (길이 `54` bytes)
- VA: `0x00000001404CDEB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D6C`
- 디코드: `14`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004CDEDF` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004CDEBB` → RVA `0x00F8F3C4` (`.data`; read/write)
- `0x004CDEC3` → RVA `0x00F8F3C8` (`.data`; read)
- `0x004CDED8` → RVA `0x00F8F450` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CDEB0  48 83 EC 28                     sub rsp, 0x28
004CDEB4  33 C0                           xor eax, eax
004CDEB6  B9 01 00 00 00                  mov ecx, 1
004CDEBB  87 05 03 15 AC 00               xchg dword ptr [rip + 0xac1503], eax
004CDEC1  33 C0                           xor eax, eax
004CDEC3  F0 0F B1 0D FD 14 AC 00         lock cmpxchg dword ptr [rip + 0xac14fd], ecx
004CDECB  74 06                           je 0x1404cded3
004CDECD  48 83 C4 28                     add rsp, 0x28
004CDED1  C3                              ret
004CDED2  CC                              int3
004CDED3  BA 03 00 00 00                  mov edx, 3
004CDED8  48 8D 0D 71 15 AC 00            lea rcx, [rip + 0xac1571]
004CDEDF  E8 3C B6 E2 FF                  call 0x1402f9520
004CDEE4  EB E7                           jmp 0x1404cdecd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcTelemetryPeriodicTimerDpc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    result = 0;
    if (condition_is_equal) goto loc_004CDED3;
loc_004CDECD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004CDED3:
    result = ExQueueWorkItem(v_rip + 11277681, 3, a3, a4);
    goto loc_004CDECD;
}
```

## 5. (Beta) C Style

```c
void CcTelemetryPeriodicTimerDpc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    result = 0;
    if (condition_is_equal) goto loc_004CDED3;
loc_004CDECD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004CDED3:
    result = ExQueueWorkItem(v_rip + 11277681, 3, a3, a4);
    goto loc_004CDECD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CDEB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CDEB0[BB_004CDEB0]
  bb_004CDECD[BB_004CDECD]
  bb_004CDED2[BB_004CDED2]
  bb_004CDED3[BB_004CDED3]
  bb_004CDEB0 -->|branch| bb_004CDED3
  bb_004CDEB0 -->|fallthrough| bb_004CDECD
  bb_004CDED2 -->|flow| bb_004CDED3
  bb_004CDED3 -->|branch| bb_004CDECD
```
