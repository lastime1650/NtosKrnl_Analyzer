# IopLiveDumpTraceNoArgs

- RVA: `0x005A43C0`–`0x005A43DD` (길이 `29` bytes)
- VA: `0x00000001405A43C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005A43C4` → [IopLiveDumpIsTracingEnabled](../4F/IopLiveDumpIsTracingEnabled_function_004FC5AC.md) (function, `0x004FC5AC`)
- `0x005A43D2` → [IopLiveDumpTrace](IopLiveDumpTrace_function_005A4070.md) (function, `0x005A4070`)

### Direct callers
- [IoCaptureLiveDump](../4E/IoCaptureLiveDump_function_004E085C.md) at `0x004E0D14`
- [IoCaptureLiveDump](../4E/IoCaptureLiveDump_function_004E085C.md) at `0x004E0D9D`
- [IoWriteDeferredLiveDumpData](../59/IoWriteDeferredLiveDumpData_function_00598CD0.md) at `0x00598D0E`
- [IopLiveDumpCallRemovePagesCallbacks](../59/IopLiveDumpCallRemovePagesCallbacks_function_0059AC28.md) at `0x0059ACBB`
- [IopLiveDumpCallRemovePagesCallbacks](../59/IopLiveDumpCallRemovePagesCallbacks_function_0059AC28.md) at `0x0059AF4E`
- [IopLiveDumpCollectPages](../59/IopLiveDumpCollectPages_function_0059B328.md) at `0x0059B61B`
- [IopLiveDumpCollectPages](../59/IopLiveDumpCollectPages_function_0059B328.md) at `0x0059B63D`
- [IopLiveDumpCorralProcessors](../59/IopLiveDumpCorralProcessors_function_0059B720.md) at `0x0059B7E5`
- [IopLiveDumpEndMirroringCallback](../59/IopLiveDumpEndMirroringCallback_function_0059B990.md) at `0x0059B9D8`
- [IopLiveDumpEndMirroringCallback](../59/IopLiveDumpEndMirroringCallback_function_0059B990.md) at `0x0059BA07`
- [IopLiveDumpStartMirroringCallback](../59/IopLiveDumpStartMirroringCallback_function_0059E250.md) at `0x0059E27B`
- [IopLiveDumpTraceInterfaceStart](../59/IopLiveDumpTraceInterfaceStart_function_0059EE0C.md) at `0x0059EE30`
- [IopLiveDumpUncorralProcessors](../59/IopLiveDumpUncorralProcessors_function_0059F4E0.md) at `0x0059F5B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A43C0  48 83 EC 28                     sub rsp, 0x28
005A43C4  E8 E3 81 F5 FF                  call 0x1404fc5ac
005A43C9  84 C0                           test al, al
005A43CB  74 0A                           je 0x1405a43d7
005A43CD  45 33 C0                        xor r8d, r8d
005A43D0  33 D2                           xor edx, edx
005A43D2  E8 99 FC FF FF                  call 0x1405a4070
005A43D7  48 83 C4 28                     add rsp, 0x28
005A43DB  C3                              ret
005A43DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpTraceNoArgs(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = IopLiveDumpIsTracingEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a3 = 0;
        a2 = 0;
        result = IopLiveDumpTrace(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpTraceNoArgs(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = IopLiveDumpIsTracingEnabled(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = IopLiveDumpTrace(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A43C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A43C0[BB_005A43C0]
  bb_005A43CD[BB_005A43CD]
  bb_005A43D7[BB_005A43D7]
  bb_005A43DC[BB_005A43DC]
  bb_005A43C0 -->|branch| bb_005A43D7
  bb_005A43C0 -->|fallthrough| bb_005A43CD
  bb_005A43CD -->|flow| bb_005A43D7
```
