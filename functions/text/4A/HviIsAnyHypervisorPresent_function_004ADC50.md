# HviIsAnyHypervisorPresent

- RVA: `0x004ADC50`–`0x004ADCA6` (길이 `86` bytes)
- VA: `0x00000001404ADC50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B64AC`
- 디코드: `26`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004ADC9A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HviGetHypervisorVendorAndMaxFunction](HviGetHypervisorVendorAndMaxFunction_function_004ADB6C.md) at `0x004ADB79`
- [HviGetHardwareFeatures](HviGetHardwareFeatures_function_004ADBC0.md) at `0x004ADBE4`
- [HvlPhase1Initialize](../58/HvlPhase1Initialize_function_00583D80.md) at `0x00583D8F`
- [KiDetectAmdNonArchSsbdSupport](../5B/KiDetectAmdNonArchSsbdSupport_function_005BEB64.md) at `0x005BEBCF`
- [KiDetectHardwareSpecControlFeatures](../5B/KiDetectHardwareSpecControlFeatures_function_005BEC4C.md) at `0x005BED04`
- [KiIsBranchConfusionPresent](../5B/KiIsBranchConfusionPresent_function_005BF2E8.md) at `0x005BF307`
- [KiIsTsaMitigationSupported](../5B/KiIsTsaMitigationSupported_function_005BF454.md) at `0x005BF477`
- [KiIsTsaPresent](../5B/KiIsTsaPresent_function_005BF4CC.md) at `0x005BF510`
- [KiApplyProcessorErrata](../5C/KiApplyProcessorErrata_function_005C1704.md) at `0x005C172D`
- [KiApplyProcessorErrata](../5C/KiApplyProcessorErrata_function_005C1704.md) at `0x005C1777`
- [KiApplyProcessorErrata](../5C/KiApplyProcessorErrata_function_005C1704.md) at `0x005C17F3`
- [HviGetHypervisorInterface](../66/HviGetHypervisorInterface_function_00666678.md) at `0x00666685`
- [HviIsHypervisorVendorMicrosoft](../66/HviIsHypervisorVendorMicrosoft_function_00666920.md) at `0x00666935`
- [HvlPhase0Initialize](../../page/71/HvlPhase0Initialize_function_00717AC8.md) at `0x00717AD5`
- [RtlpInitFunctionOverrideCapabilities](../../page/79/RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE4E`
- [NtFilterBootOption](../../page/7A/NtFilterBootOption_function_007A1BE0.md) at `0x007A1C31`
- [SepSecureBootCorrectBcd](../../page/7A/SepSecureBootCorrectBcd_function_007A2174.md) at `0x007A21B7`
- [KiConfigureAmdTprLowerInterruptDelayWorkaround](../../pagelk/B6/KiConfigureAmdTprLowerInterruptDelayWorkaround_function_00B68374.md) at `0x00B683B9`
- [ViFilterIsDeviceExcluded](../../pagevrfy/BA/ViFilterIsDeviceExcluded_function_00BAD470.md) at `0x00BAD486`
- [InitializeDynamicPartitioningPolicy](../../init/C1/InitializeDynamicPartitioningPolicy_function_00C1C2E8.md) at `0x00C1C316`
- [KiComputeDispatchInterruptCost](../../init/C3/KiComputeDispatchInterruptCost_function_00C377C0.md) at `0x00C37811`
- [KiIntSteerInit](../../init/C3/KiIntSteerInit_function_00C3A1CC.md) at `0x00C3A2D6`
- [KeInitSystem](../../init/C7/KeInitSystem_function_00C71660.md) at `0x00C717D6`
- [KeInitSystem](../../init/C7/KeInitSystem_function_00C71660.md) at `0x00C71C1A`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72C72`

### Static image references
- `0x004ADC56` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004ADC50  40 53                           push rbx
004ADC52  48 83 EC 20                     sub rsp, 0x20
004ADC56  48 8B 05 E3 CA 95 00            mov rax, qword ptr [rip + 0x95cae3]
004ADC5D  48 33 C4                        xor rax, rsp
004ADC60  48 89 44 24 10                  mov qword ptr [rsp + 0x10], rax
004ADC65  33 C9                           xor ecx, ecx
004ADC67  41 B9 01 00 00 00               mov r9d, 1
004ADC6D  41 8B C1                        mov eax, r9d
004ADC70  45 32 C0                        xor r8b, r8b
004ADC73  0F A2                           cpuid
004ADC75  85 C9                           test ecx, ecx
004ADC77  79 16                           jns 0x1404adc8f
004ADC79  33 C9                           xor ecx, ecx
004ADC7B  45 0F B6 C0                     movzx r8d, r8b
004ADC7F  B8 01 00 00 40                  mov eax, 0x40000001
004ADC84  0F A2                           cpuid
004ADC86  3D 58 62 6E 76                  cmp eax, 0x766e6258
004ADC8B  45 0F 45 C1                     cmovne r8d, r9d
004ADC8F  41 8A C0                        mov al, r8b
004ADC92  48 8B 4C 24 10                  mov rcx, qword ptr [rsp + 0x10]
004ADC97  48 33 CC                        xor rcx, rsp
004ADC9A  E8 A1 E9 1F 00                  call 0x1406ac640
004ADC9F  48 83 C4 20                     add rsp, 0x20
004ADCA3  5B                              pop rbx
004ADCA4  C3                              ret
004ADCA5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HviIsAnyHypervisorPresent(int a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (32);
    result = (*(unsigned __int64 *)(v_rip + 9816803)) ^ (v_rsp);
    v_stack_m18 = result;
    a1 = 0;
    a3 = 0;
    result = 1;
    if (sign_flag) {
        a1 = 0;
        a3 = 0;
        result = 0x40000001ULL;
        if (((unsigned int)(result)) != 0x766E6258ULL) { a3 = 1; }
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 1);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HviIsAnyHypervisorPresent(int32_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (32);
    result = (*(uint64_t *)(v_rip + 0x95CAE3)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg1 = 0;
    Arg3 = 0;
    result = 1;
    if (sign_flag) {
        Arg1 = 0;
        Arg3 = 0;
        result = 0x40000001ULL;
        if (((uint32_t)(result)) != 0x766E6258ULL) { Arg3 = 1; }
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 1);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004ADC50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004ADC50[BB_004ADC50]
  bb_004ADC79[BB_004ADC79]
  bb_004ADC8F[BB_004ADC8F]
  bb_004ADCA5[BB_004ADCA5]
  bb_004ADC50 -->|branch| bb_004ADC8F
  bb_004ADC50 -->|fallthrough| bb_004ADC79
  bb_004ADC79 -->|flow| bb_004ADC8F
```
