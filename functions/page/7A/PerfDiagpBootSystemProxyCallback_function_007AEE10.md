# PerfDiagpBootSystemProxyCallback

- RVA: `0x007AEE10`–`0x007AEE35` (길이 `37` bytes)
- VA: `0x00000001407AEE10`
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
- `0x007AEE2A` → [PerfDiagpRequestState](../AA/PerfDiagpRequestState_function_00AA6CAC.md) (function, `0x00AA6CAC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007AEE10  48 83 EC 28                     sub rsp, 0x28
007AEE14  85 D2                           test edx, edx
007AEE16  74 0D                           je 0x1407aee25
007AEE18  41 80 F8 55                     cmp r8b, 0x55
007AEE1C  75 11                           jne 0x1407aee2f
007AEE1E  B9 01 00 00 00                  mov ecx, 1
007AEE23  EB 05                           jmp 0x1407aee2a
007AEE25  B9 02 00 00 00                  mov ecx, 2
007AEE2A  E8 7D 7E 2F 00                  call 0x140aa6cac
007AEE2F  48 83 C4 28                     add rsp, 0x28
007AEE33  C3                              ret
007AEE34  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PerfDiagpBootSystemProxyCallback(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 0) goto loc_007AEE25;
    if (a3 != 85) goto loc_007AEE2F;
    goto loc_007AEE2A;
loc_007AEE25:
loc_007AEE2A:
    result = PerfDiagpRequestState(2, a2, a3, a4);
loc_007AEE2F:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PerfDiagpBootSystemProxyCallback(int64_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 0) goto loc_007AEE25;
    if (Arg3 != 85) goto loc_007AEE2F;
    goto loc_007AEE2A;
loc_007AEE25:
loc_007AEE2A:
    result = PerfDiagpRequestState(2, Arg2, Arg3, a4);
loc_007AEE2F:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007AEE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007AEE10[BB_007AEE10]
  bb_007AEE18[BB_007AEE18]
  bb_007AEE1E[BB_007AEE1E]
  bb_007AEE25[BB_007AEE25]
  bb_007AEE2A[BB_007AEE2A]
  bb_007AEE2F[BB_007AEE2F]
  bb_007AEE34[BB_007AEE34]
  bb_007AEE10 -->|branch| bb_007AEE25
  bb_007AEE10 -->|fallthrough| bb_007AEE18
  bb_007AEE18 -->|branch| bb_007AEE2F
  bb_007AEE18 -->|fallthrough| bb_007AEE1E
  bb_007AEE1E -->|branch| bb_007AEE2A
  bb_007AEE25 -->|flow| bb_007AEE2A
  bb_007AEE2A -->|flow| bb_007AEE2F
```
