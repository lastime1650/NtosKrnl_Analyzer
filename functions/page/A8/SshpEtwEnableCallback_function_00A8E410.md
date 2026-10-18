# SshpEtwEnableCallback

- RVA: `0x00A8E410`–`0x00A8E42B` (길이 `27` bytes)
- VA: `0x0000000140A8E410`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090138`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8E41F` → [SshpTracingRundownBlockerState](SshpTracingRundownBlockerState_function_00A8E434.md) (function, `0x00A8E434`)
- `0x00A8E424` → [SshpTracingRundownCollectionState](SshpTracingRundownCollectionState_function_00A8E534.md) (function, `0x00A8E534`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8E410  48 83 EC 28                     sub rsp, 0x28
00A8E414  83 FA 02                        cmp edx, 2
00A8E417  74 06                           je 0x140a8e41f
00A8E419  48 83 C4 28                     add rsp, 0x28
00A8E41D  C3                              ret
00A8E41E  CC                              int3
00A8E41F  E8 10 00 00 00                  call 0x140a8e434
00A8E424  E8 0B 01 00 00                  call 0x140a8e534
00A8E429  EB EE                           jmp 0x140a8e419
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpEtwEnableCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 2) goto loc_00A8E41F;
loc_00A8E419:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A8E41F:
    result = SshpTracingRundownBlockerState(a1, a2, a3, a4);
    result = SshpTracingRundownCollectionState(a1, a2, a3, a4);
    goto loc_00A8E419;
}
```

## 5. (Beta) C Style

```c
int64_t SshpEtwEnableCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 2) goto loc_00A8E41F;
loc_00A8E419:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A8E41F:
    result = SshpTracingRundownBlockerState(Arg1, Arg2, a3, a4);
    result = SshpTracingRundownCollectionState(Arg1, Arg2, a3, a4);
    goto loc_00A8E419;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8E410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8E410[BB_00A8E410]
  bb_00A8E419[BB_00A8E419]
  bb_00A8E41E[BB_00A8E41E]
  bb_00A8E41F[BB_00A8E41F]
  bb_00A8E410 -->|branch| bb_00A8E41F
  bb_00A8E410 -->|fallthrough| bb_00A8E419
  bb_00A8E41E -->|flow| bb_00A8E41F
  bb_00A8E41F -->|branch| bb_00A8E419
```
