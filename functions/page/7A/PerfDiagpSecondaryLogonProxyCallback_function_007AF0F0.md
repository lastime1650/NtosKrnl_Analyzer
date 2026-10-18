# PerfDiagpSecondaryLogonProxyCallback

- RVA: `0x007AF0F0`–`0x007AF115` (길이 `37` bytes)
- VA: `0x00000001407AF0F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007AF10A` → [PerfDiagpRequestState](../AA/PerfDiagpRequestState_function_00AA6CAC.md) (function, `0x00AA6CAC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007AF0F0  48 83 EC 28                     sub rsp, 0x28
007AF0F4  85 D2                           test edx, edx
007AF0F6  74 0D                           je 0x1407af105
007AF0F8  41 80 F8 55                     cmp r8b, 0x55
007AF0FC  75 11                           jne 0x1407af10f
007AF0FE  B9 05 00 00 00                  mov ecx, 5
007AF103  EB 05                           jmp 0x1407af10a
007AF105  B9 06 00 00 00                  mov ecx, 6
007AF10A  E8 9D 7B 2F 00                  call 0x140aa6cac
007AF10F  48 83 C4 28                     add rsp, 0x28
007AF113  C3                              ret
007AF114  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PerfDiagpSecondaryLogonProxyCallback(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 0) goto loc_007AF105;
    if (a3 != 85) goto loc_007AF10F;
    goto loc_007AF10A;
loc_007AF105:
loc_007AF10A:
    result = PerfDiagpRequestState(6, a2, a3, a4);
loc_007AF10F:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PerfDiagpSecondaryLogonProxyCallback(int64_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 0) goto loc_007AF105;
    if (Arg3 != 85) goto loc_007AF10F;
    goto loc_007AF10A;
loc_007AF105:
loc_007AF10A:
    result = PerfDiagpRequestState(6, Arg2, Arg3, a4);
loc_007AF10F:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007AF0F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007AF0F0[BB_007AF0F0]
  bb_007AF0F8[BB_007AF0F8]
  bb_007AF0FE[BB_007AF0FE]
  bb_007AF105[BB_007AF105]
  bb_007AF10A[BB_007AF10A]
  bb_007AF10F[BB_007AF10F]
  bb_007AF114[BB_007AF114]
  bb_007AF0F0 -->|branch| bb_007AF105
  bb_007AF0F0 -->|fallthrough| bb_007AF0F8
  bb_007AF0F8 -->|branch| bb_007AF10F
  bb_007AF0F8 -->|fallthrough| bb_007AF0FE
  bb_007AF0FE -->|branch| bb_007AF10A
  bb_007AF105 -->|flow| bb_007AF10A
  bb_007AF10A -->|flow| bb_007AF10F
```
