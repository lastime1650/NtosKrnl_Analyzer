# IoAllocateGenericErrorLogEntry

- RVA: `0x00597908`–`0x0059791E` (길이 `22` bytes)
- VA: `0x0000000140597908`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00597913` → [IopAllocateErrorLogEntry](../4A/IopAllocateErrorLogEntry_function_004ABF5C.md) (function, `0x004ABF5C`)

### Direct callers
- [IopLogBlockedDriverEvent](../../page/71/IopLogBlockedDriverEvent_function_0071BBFC.md) at `0x0071BC0E`
- [PnpLogEvent](../../page/72/PnpLogEvent_function_0072C8FC.md) at `0x0072C969`
- [MiLogFailedDriverLoad](../../page/A2/MiLogFailedDriverLoad_function_00A24ACC.md) at `0x00A24C2E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00597908  48 83 EC 28                     sub rsp, 0x28
0059790C  44 8A C1                        mov r8b, cl
0059790F  33 D2                           xor edx, edx
00597911  33 C9                           xor ecx, ecx
00597913  E8 44 46 F1 FF                  call 0x1404abf5c
00597918  48 83 C4 28                     add rsp, 0x28
0059791C  C3                              ret
0059791D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoAllocateGenericErrorLogEntry(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    a1 = 0;
    result = IopAllocateErrorLogEntry(a1, a2, (unsigned __int8)(a1), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoAllocateGenericErrorLogEntry(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    Arg1 = 0;
    result = IopAllocateErrorLogEntry(Arg1, Arg2, (uint8_t)(Arg1), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00597908&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00597908[BB_00597908]
  bb_0059791D[BB_0059791D]
```
