# Feature_IoInvalidateDeviceState_Unconditional__private_ReportDeviceUsage

- RVA: `0x00478C84`–`0x00478CE7` (길이 `99` bytes)
- VA: `0x0000000140478C84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `23`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00478CCA` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x00478CE0` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [IoInvalidateDeviceState](IoInvalidateDeviceState_function_00477F10.md) at `0x00477F4F`
- [PiProcessRequeryDeviceState](../../page/8F/PiProcessRequeryDeviceState_function_008FA054.md) at `0x008FA09F`

### Static image references
- `0x00478C8E` → RVA `0x00FC4828` (`.data`; read)
- `0x00478CBA` → RVA `0x000DDB38` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00478C84  48 83 EC 28                     sub rsp, 0x28
00478C88  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00478C8E  8B 0D 94 BB B4 00               mov ecx, dword ptr [rip + 0xb4bb94]
00478C94  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00478C98  F6 C1 10                        test cl, 0x10
00478C9B  74 06                           je 0x140478ca3
00478C9D  48 83 C4 28                     add rsp, 0x28
00478CA1  C3                              ret
00478CA2  CC                              int3
00478CA3  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00478CA8  41 B9 01 00 00 00               mov r9d, 1
00478CAE  41 0B C9                        or ecx, r9d
00478CB1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00478CB6  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00478CBA  48 8D 0D 77 4E C6 FF            lea rcx, [rip - 0x39b189]
00478CC1  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00478CC6  45 8D 41 02                     lea r8d, [r9 + 2]
00478CCA  E8 15 5A 0C 00                  call 0x14053e6e4
00478CCF  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00478CD4  4C 8D 05 5D 4E C6 FF            lea r8, [rip - 0x39b1a3]
00478CDB  BA 03 00 00 00                  mov edx, 3
00478CE0  E8 8F 5A 0C 00                  call 0x14053e774
00478CE5  EB B6                           jmp 0x140478c9d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_IoInvalidateDeviceState_Unconditional__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11844500)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11844500)))) & (16)) == 0) goto loc_00478CA3;
loc_00478C9D:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00478CA3:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11844500))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3781001, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3781027, 1);
    goto loc_00478C9D;
}
```

## 5. (Beta) C Style

```c
void Feature_IoInvalidateDeviceState_Unconditional__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4BB94)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4BB94)))) & (16)) == 0) goto loc_00478CA3;
loc_00478C9D:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00478CA3:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB4BB94))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3781001, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3781027, 1);
    goto loc_00478C9D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00478C84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00478C84[BB_00478C84]
  bb_00478C9D[BB_00478C9D]
  bb_00478CA2[BB_00478CA2]
  bb_00478CA3[BB_00478CA3]
  bb_00478C84 -->|branch| bb_00478CA3
  bb_00478C84 -->|fallthrough| bb_00478C9D
  bb_00478CA2 -->|flow| bb_00478CA3
  bb_00478CA3 -->|branch| bb_00478C9D
```
