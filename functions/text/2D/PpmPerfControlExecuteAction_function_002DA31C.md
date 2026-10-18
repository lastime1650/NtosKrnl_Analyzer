# PpmPerfControlExecuteAction

- RVA: `0x002DA31C`–`0x002DA345` (길이 `41` bytes)
- VA: `0x00000001402DA31C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000704F4`
- 디코드: `15`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002DA33E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PpmCheckAcquireProcessorPerformance](PpmCheckAcquireProcessorPerformance_function_002DA170.md) at `0x002DA1BD`
- [PpmPerfReadFeedback](PpmPerfReadFeedback_function_002DA300.md) at `0x002DA30B`
- [PpmPerfCommitPerformance](../4A/PpmPerfCommitPerformance_function_004A2460.md) at `0x004A246B`

### Static image references
- `0x002DA337` → RVA `0x004BAB80` (`PpmPerfControlActionCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DA31C  40 53                           push rbx
002DA31E  48 83 EC 20                     sub rsp, 0x20
002DA322  33 DB                           xor ebx, ebx
002DA324  48 8B C1                        mov rax, rcx
002DA327  48 85 C9                        test rcx, rcx
002DA32A  75 0B                           jne 0x1402da337
002DA32C  B3 01                           mov bl, 1
002DA32E  8A C3                           mov al, bl
002DA330  48 83 C4 20                     add rsp, 0x20
002DA334  5B                              pop rbx
002DA335  C3                              ret
002DA336  CC                              int3
002DA337  48 8D 0D 42 08 1E 00            lea rcx, [rip + 0x1e0842]
002DA33E  E8 8D 07 3E 00                  call 0x1406baad0
002DA343  EB E9                           jmp 0x1402da32e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfControlExecuteAction(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (a1 != 0) goto loc_002DA337;
loc_002DA32E:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_002DA337:
    result = guard_dispatch_icall(v_rip + 1968194, a2, a3, a4);
    goto loc_002DA32E;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfControlExecuteAction(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (Arg1 != 0) goto loc_002DA337;
loc_002DA32E:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_002DA337:
    result = guard_dispatch_icall(v_rip + 1968194, a2, a3, a4);
    goto loc_002DA32E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DA31C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002DA31C[BB_002DA31C]
  bb_002DA32C[BB_002DA32C]
  bb_002DA32E[BB_002DA32E]
  bb_002DA336[BB_002DA336]
  bb_002DA337[BB_002DA337]
  bb_002DA31C -->|branch| bb_002DA337
  bb_002DA31C -->|fallthrough| bb_002DA32C
  bb_002DA32C -->|flow| bb_002DA32E
  bb_002DA336 -->|flow| bb_002DA337
  bb_002DA337 -->|branch| bb_002DA32E
```
