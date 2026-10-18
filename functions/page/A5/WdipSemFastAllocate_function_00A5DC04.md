# WdipSemFastAllocate

- RVA: `0x00A5DC04`–`0x00A5DC37` (길이 `51` bytes)
- VA: `0x0000000140A5DC04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BD8`
- 디코드: `17`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A5DC1D` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00A5DC30` → [WdipSemAllocatePool](../AA/WdipSemAllocatePool_function_00AA0B64.md) (function, `0x00AA0B64`)

### Direct callers
- [WdipSemAddContextEventToScenario](../7A/WdipSemAddContextEventToScenario_function_007AF338.md) at `0x007AF3AF`
- [WdipSemAddEndEventToScenario](../7A/WdipSemAddEndEventToScenario_function_007AF3FC.md) at `0x007AF481`
- [WdipSemLoadNextScenario](../7A/WdipSemLoadNextScenario_function_007AFDE0.md) at `0x007B017F`
- [WdipSemLoadNextScenario](../7A/WdipSemLoadNextScenario_function_007AFDE0.md) at `0x007B028E`
- [WdipSemLoadScenarioTable](../7B/WdipSemLoadScenarioTable_function_007B02D8.md) at `0x007B0616`
- [WdipSemUpdateProviderTableWithEvent](../7B/WdipSemUpdateProviderTableWithEvent_function_007B09F8.md) at `0x007B0ACE`
- [WdipSemUpdateFrequentScenarioTable](../7B/WdipSemUpdateFrequentScenarioTable_function_007B0D7C.md) at `0x007B0E0D`
- [WdipSemUpdateInflightScenarioTable](../7B/WdipSemUpdateInflightScenarioTable_function_007B0EB4.md) at `0x007B0F4D`
- [WdipSemBuildScenarioInstance](WdipSemBuildScenarioInstance_function_00A5DB90.md) at `0x00A5DBB9`
- [WdipSemWriteSemActionsEvent](../AB/WdipSemWriteSemActionsEvent_function_00ABC618.md) at `0x00ABC730`

### Static image references
- `0x00A5DC0D` → RVA `0x00E28C90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A5DC1D` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A5DC04  40 53                           push rbx
00A5DC06  48 83 EC 20                     sub rsp, 0x20
00A5DC0A  48 63 C9                        movsxd rcx, ecx
00A5DC0D  48 8D 05 7C B0 3C 00            lea rax, [rip + 0x3cb07c]
00A5DC14  48 C1 E1 04                     shl rcx, 4
00A5DC18  8B DA                           mov ebx, edx
00A5DC1A  48 03 C8                        add rcx, rax
00A5DC1D  E8 4E C9 C5 FF                  call 0x1406ba570
00A5DC22  48 85 C0                        test rax, rax
00A5DC25  74 07                           je 0x140a5dc2e
00A5DC27  48 83 C4 20                     add rsp, 0x20
00A5DC2B  5B                              pop rbx
00A5DC2C  C3                              ret
00A5DC2D  CC                              int3
00A5DC2E  8B CB                           mov ecx, ebx
00A5DC30  E8 2F 2F 04 00                  call 0x140aa0b64
00A5DC35  EB F0                           jmp 0x140a5dc27
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemFastAllocate(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = ((int)(a1)) << (4);
    a1 = (a1) + (v_rip + 3977340);
    result = ExpInterlockedPopEntrySList(a1, a2, a3, a4);
    if (result == 0) goto loc_00A5DC2E;
loc_00A5DC27:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A5DC2E:
    result = WdipSemAllocatePool((unsigned int)((unsigned int)((unsigned int)(a2))), a2, a3, a4);
    goto loc_00A5DC27;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemFastAllocate(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = ((int32_t)(Arg1)) << (4);
    Arg1 = (Arg1) + (v_rip + 3977340);
    result = ExpInterlockedPopEntrySList(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_00A5DC2E;
loc_00A5DC27:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A5DC2E:
    result = WdipSemAllocatePool((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg2, a3, a4);
    goto loc_00A5DC27;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A5DC04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A5DC04[BB_00A5DC04]
  bb_00A5DC27[BB_00A5DC27]
  bb_00A5DC2D[BB_00A5DC2D]
  bb_00A5DC2E[BB_00A5DC2E]
  bb_00A5DC04 -->|branch| bb_00A5DC2E
  bb_00A5DC04 -->|fallthrough| bb_00A5DC27
  bb_00A5DC2D -->|flow| bb_00A5DC2E
  bb_00A5DC2E -->|branch| bb_00A5DC27
```
