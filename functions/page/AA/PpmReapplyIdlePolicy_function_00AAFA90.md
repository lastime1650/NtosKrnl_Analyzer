# PpmReapplyIdlePolicy

- RVA: `0x00AAFA90`–`0x00AAFAB3` (길이 `35` bytes)
- VA: `0x0000000140AAFA90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AAFAA8` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (function, `0x002DD834`)

### Direct callers
- [PpmInfoApplySettingUpdate](../91/PpmInfoApplySettingUpdate_function_009160A8.md) at `0x0091613A`
- [PpmCompareAndApplyPolicySettings](../A5/PpmCompareAndApplyPolicySettings_function_00A52CEC.md) at `0x00A52EA2`

### Static image references
- `0x00AAFA97` → RVA `0x00446E60` (`PpmApplyIdlePolicyChanges`; read)
- `0x00AAFAA1` → RVA `0x00FC7120` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AAFAA8` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAFA90  48 83 EC 28                     sub rsp, 0x28
00AAFA94  45 33 C9                        xor r9d, r9d
00AAFA97  48 8D 15 C2 73 99 FF            lea rdx, [rip - 0x668c3e]
00AAFA9E  45 33 C0                        xor r8d, r8d
00AAFAA1  48 8D 0D 78 76 51 00            lea rcx, [rip + 0x517678]
00AAFAA8  E8 87 DD 82 FF                  call 0x1402dd834
00AAFAAD  48 83 C4 28                     add rsp, 0x28
00AAFAB1  C3                              ret
00AAFAB2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmReapplyIdlePolicy(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    a3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 5338744, v_rip - 6720574, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmReapplyIdlePolicy(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    Arg3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 5338744, v_rip - 6720574, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAFA90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAFA90[BB_00AAFA90]
  bb_00AAFAB2[BB_00AAFAB2]
```
