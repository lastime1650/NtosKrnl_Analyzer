# PopSetupUserPresencePredictionNotification

- RVA: `0x00753C4C`–`0x00753C80` (길이 `52` bytes)
- VA: `0x0000000140753C4C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00753C75` → [ExSubscribeWnfStateChange](../9D/ExSubscribeWnfStateChange_function_009D4BC0.md) (function, `0x009D4BC0`)

### Direct callers
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C731D2`

### Static image references
- `0x00753C56` → RVA `0x00758640` (`PopWnfUserAwayPredictionCallback`; read)
- `0x00753C65` → RVA `0x00020BB8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00753C4C  48 83 EC 38                     sub rsp, 0x38
00753C50  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00753C56  48 8D 05 E3 49 00 00            lea rax, [rip + 0x49e3]
00753C5D  45 33 C9                        xor r9d, r9d
00753C60  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00753C65  48 8D 15 4C CF 8C FF            lea rdx, [rip - 0x7330b4]
00753C6C  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00753C71  45 8D 41 01                     lea r8d, [r9 + 1]
00753C75  E8 46 0F 28 00                  call 0x1409d4bc0
00753C7A  48 83 C4 38                     add rsp, 0x38
00753C7E  C3                              ret
00753C7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetupUserPresencePredictionNotification(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    v_stack_m18 = v_rip + 18915;
    result = ExSubscribeWnfStateChange(v_stack_p8, v_rip - 7549108, a4 + 1, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSetupUserPresencePredictionNotification(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    v_stack_m18 = v_rip + 18915;
    result = ExSubscribeWnfStateChange(v_stack_p8, v_rip - 7549108, Arg4 + 1, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00753C4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00753C4C[BB_00753C4C]
  bb_00753C7F[BB_00753C7F]
```
