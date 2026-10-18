# ExSystemTimeToLocalTime

- RVA: `0x002FE1C0`–`0x002FE1E6` (길이 `38` bytes)
- VA: `0x00000001402FE1C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002FE1C7` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [IopCopyBootLogRegistryToFile](../../page/71/IopCopyBootLogRegistryToFile_function_0071B19C.md) at `0x0071B246`
- [PopDiagTracePassiveCooling](../../page/76/PopDiagTracePassiveCooling_function_00761CAC.md) at `0x00761DDE`
- [PopPowerAdapterPublishRecState](../../page/76/PopPowerAdapterPublishRecState_function_007679CC.md) at `0x00767A86`
- [PopPowerAdapterPublishRecState](../../page/76/PopPowerAdapterPublishRecState_function_007679CC.md) at `0x00767AB1`
- [PopNetGetNextDueRefreshTime](../../page/76/PopNetGetNextDueRefreshTime_function_00768BD4.md) at `0x00768C22`
- [PopAdaptiveStandbyTraceBatteryUpdate](../../page/76/PopAdaptiveStandbyTraceBatteryUpdate_function_0076EF7C.md) at `0x0076F02A`
- [ExpRefreshSystemTime](../../page/7C/ExpRefreshSystemTime_function_007C6264.md) at `0x007C6307`
- [NtSetSystemTime](../../page/7C/NtSetSystemTime_function_007C65F0.md) at `0x007C6808`
- [CmpUpdateReorganizeRegistryValues](../../page/7E/CmpUpdateReorganizeRegistryValues_function_007EA7D4.md) at `0x007EA897`
- [HalpUtcTimeToAcpiRealTime](../../page/A9/HalpUtcTimeToAcpiRealTime_function_00A980E8.md) at `0x00A98178`
- [PopDiagTraceActiveCooling](../../page/AD/PopDiagTraceActiveCooling_function_00AD72A8.md) at `0x00AD73D4`
- [ExpSetSystemTime](../../pagelk/B7/ExpSetSystemTime_function_00B7C838.md) at `0x00B7C889`
- [ExpSetSystemTime](../../pagelk/B7/ExpSetSystemTime_function_00B7C838.md) at `0x00B7C8CA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002FE1C0  48 83 EC 28                     sub rsp, 0x28
002FE1C4  4C 8B C1                        mov r8, rcx
002FE1C7  E8 24 00 00 00                  call 0x1402fe1f0
002FE1CC  49 8B 08                        mov rcx, qword ptr [r8]
002FE1CF  48 8B 80 C8 04 00 00            mov rax, qword ptr [rax + 0x4c8]
002FE1D6  48 2B 88 B8 01 00 00            sub rcx, qword ptr [rax + 0x1b8]
002FE1DD  48 89 0A                        mov qword ptr [rdx], rcx
002FE1E0  48 83 C4 28                     add rsp, 0x28
002FE1E4  C3                              ret
002FE1E5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExSystemTimeToLocalTime(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a1, a4);
    a1 = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440));
    *(unsigned __int64 *)(a2) = a1;
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(result + 1224);
}
```

## 5. (Beta) C Style

```c
int64_t ExSystemTimeToLocalTime(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg1, a4);
    Arg1 = (*(uint64_t *)(Arg1)) - (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8));
    *(uint64_t *)(Arg2) = Arg1;
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(result + 0x4C8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FE1C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002FE1C0[BB_002FE1C0]
  bb_002FE1E5[BB_002FE1E5]
```
