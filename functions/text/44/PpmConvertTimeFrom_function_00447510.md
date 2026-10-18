# PpmConvertTimeFrom

- RVA: `0x00447510`–`0x00447526` (길이 `22` bytes)
- VA: `0x0000000140447510`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0044751B` → [PpmConvertTime](PpmConvertTime_function_00447530.md) (function, `0x00447530`)

### Direct callers
- [PpmApplyIdlePolicy](PpmApplyIdlePolicy_function_004474A8.md) at `0x004474F8`
- [PpmRegisterPerfStates](../../page/75/PpmRegisterPerfStates_function_0075B084.md) at `0x0075B3EB`
- [PopIdleWakeConvertIntervalBucketsFrom](../../page/76/PopIdleWakeConvertIntervalBucketsFrom_function_0076B31C.md) at `0x0076B344`
- [PopIdleWakeInitialize](../../page/76/PopIdleWakeInitialize_function_0076B438.md) at `0x0076B452`
- [PpmHvEnableQosEnlightenment](../../page/A8/PpmHvEnableQosEnlightenment_function_00A84D00.md) at `0x00A84D92`
- [PopInitDripsWakeAccounting](../../init/C3/PopInitDripsWakeAccounting_function_00C3D374.md) at `0x00C3D3A1`
- [PpmInitIdlePolicy](../../init/C3/PpmInitIdlePolicy_function_00C3D8F4.md) at `0x00C3D98C`
- [PpmInitIdlePolicy](../../init/C3/PpmInitIdlePolicy_function_00C3D8F4.md) at `0x00C3D9B3`
- [PpmInitIdlePolicy](../../init/C3/PpmInitIdlePolicy_function_00C3D8F4.md) at `0x00C3D9E0`

### Static image references
- `0x00447514` → RVA `0x00FC6BE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00447510  48 83 EC 28                     sub rsp, 0x28
00447514  4C 8B 05 C5 F6 B7 00            mov r8, qword ptr [rip + 0xb7f6c5]
0044751B  E8 10 00 00 00                  call 0x140447530
00447520  48 83 C4 28                     add rsp, 0x28
00447524  C3                              ret
00447525  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmConvertTimeFrom(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PpmConvertTime(a1, a2, *(unsigned __int64 *)(v_rip + 12056261), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PpmConvertTimeFrom(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PpmConvertTime(a1, a2, *(uint64_t *)(v_rip + 0xB7F6C5), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00447510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00447510[BB_00447510]
  bb_00447525[BB_00447525]
```
