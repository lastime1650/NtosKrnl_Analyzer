# Feature_ExpandSTEIgnoreReasons__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F7AE8`–`0x004F7B1A` (길이 `50` bytes)
- VA: `0x00000001404F7AE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F7B0F` → [Feature_ExpandSTEIgnoreReasons__private_IsEnabledFallback](Feature_ExpandSTEIgnoreReasons__private_IsEnabledFallback_function_004F7B20.md) (function, `0x004F7B20`)

### Direct callers
- [PdcPoCurrentPdcPhase](../5D/PdcPoCurrentPdcPhase_function_005D9E70.md) at `0x005D9E94`
- [PopAdaptiveGetSystemInitiatedRebootTargetState](../../page/70/PopAdaptiveGetSystemInitiatedRebootTargetState_function_00701398.md) at `0x0070148B`
- [PopRecordPhysicalPowerButton](../../page/75/PopRecordPhysicalPowerButton_function_00754464.md) at `0x00754518`
- [NtSetThreadExecutionState](../../page/AC/NtSetThreadExecutionState_function_00AC0A40.md) at `0x00AC0B90`
- [NtSetThreadExecutionState](../../page/AC/NtSetThreadExecutionState_function_00AC0A40.md) at `0x00AC0C10`
- [PopDiagTraceSetThreadExecutionState](../../page/AC/PopDiagTraceSetThreadExecutionState_function_00ACC418.md) at `0x00ACC44D`
- [PopDiagTraceSetThreadExecutionState](../../page/AC/PopDiagTraceSetThreadExecutionState_function_00ACC418.md) at `0x00ACC536`

### Static image references
- `0x004F7AF2` → RVA `0x00FC46F0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F7AE8  48 83 EC 28                     sub rsp, 0x28
004F7AEC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F7AF2  8B 05 F8 CB AC 00               mov eax, dword ptr [rip + 0xaccbf8]
004F7AF8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F7AFC  A8 10                           test al, 0x10
004F7AFE  74 05                           je 0x1404f7b05
004F7B00  83 E0 01                        and eax, 1
004F7B03  EB 0F                           jmp 0x1404f7b14
004F7B05  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F7B0A  BA 03 00 00 00                  mov edx, 3
004F7B0F  E8 0C 00 00 00                  call 0x1404f7b20
004F7B14  48 83 C4 28                     add rsp, 0x28
004F7B18  C3                              ret
004F7B19  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ExpandSTEIgnoreReasons__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11324408)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11324408)))) & (16)) == 0) goto loc_004F7B05;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11324408))) & (1));
    goto loc_004F7B14;
loc_004F7B05:
    result = Feature_ExpandSTEIgnoreReasons__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7B14:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ExpandSTEIgnoreReasons__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCBF8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCBF8)))) & (16)) == 0) goto loc_004F7B05;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACCBF8))) & (1));
    goto loc_004F7B14;
loc_004F7B05:
    result = Feature_ExpandSTEIgnoreReasons__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7B14:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F7AE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F7AE8[BB_004F7AE8]
  bb_004F7B00[BB_004F7B00]
  bb_004F7B05[BB_004F7B05]
  bb_004F7B14[BB_004F7B14]
  bb_004F7B19[BB_004F7B19]
  bb_004F7AE8 -->|branch| bb_004F7B05
  bb_004F7AE8 -->|fallthrough| bb_004F7B00
  bb_004F7B00 -->|branch| bb_004F7B14
  bb_004F7B05 -->|flow| bb_004F7B14
```
