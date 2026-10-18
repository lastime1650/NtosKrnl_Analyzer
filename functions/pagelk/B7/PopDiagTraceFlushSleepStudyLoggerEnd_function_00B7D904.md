# PopDiagTraceFlushSleepStudyLoggerEnd

- RVA: `0x00B7D904`–`0x00B7D91A` (길이 `22` bytes)
- VA: `0x0000000140B7D904`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B7D90F` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (function, `0x004982F8`)

### Direct callers
- [PopUmpoSendFlushSleepStudyLoggerNotification](../../text/4C/PopUmpoSendFlushSleepStudyLoggerNotification_function_004C4314.md) at `0x004C4365`

### Static image references
- `0x00B7D908` → RVA `0x0001E9A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B7D90F` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7D904  48 83 EC 28                     sub rsp, 0x28
00B7D908  48 8D 0D 99 10 4A FF            lea rcx, [rip - 0xb5ef67]
00B7D90F  E8 E4 A9 91 FF                  call 0x1404982f8
00B7D914  48 83 C4 28                     add rsp, 0x28
00B7D918  C3                              ret
00B7D919  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceFlushSleepStudyLoggerEnd(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopDiagTraceEventNoPayload(v_rip - 11923303, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopDiagTraceFlushSleepStudyLoggerEnd(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopDiagTraceEventNoPayload(v_rip - 11923303, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7D904&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B7D904[BB_00B7D904]
  bb_00B7D919[BB_00B7D919]
```
