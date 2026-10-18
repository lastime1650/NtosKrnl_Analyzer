# ExSystemExceptionFilter

- RVA: `0x007C6980`–`0x007C6996` (길이 `22` bytes)
- VA: `0x00000001407C6980`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **37**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpGetSystemProcessorInformation$filt$0](../../text/6D/ExpGetSystemProcessorInformation_filt_0_function_006D1DA0.md) at `0x006D1DA9`
- [NtShutdownWorkerFactory$filt$0](../../text/6D/NtShutdownWorkerFactory_filt_0_function_006D1E0F.md) at `0x006D1E18`
- [NtGetWriteWatch$filt$0](../../text/6D/NtGetWriteWatch_filt_0_function_006D1E2B.md) at `0x006D1E34`
- [NtGetWriteWatch$filt$1](../../text/6D/NtGetWriteWatch_filt_1_function_006D1E41.md) at `0x006D1E4A`
- [NtSetInformationWorkerFactory$filt$0](../../text/6D/NtSetInformationWorkerFactory_filt_0_function_006D2210.md) at `0x006D2219`
- [NtSetInformationWorkerFactory$filt$1](../../text/6D/NtSetInformationWorkerFactory_filt_1_function_006D2226.md) at `0x006D222F`
- [NtWaitForWorkViaWorkerFactory$filt$0](../../text/6D/NtWaitForWorkViaWorkerFactory_filt_0_function_006D2450.md) at `0x006D2459`
- [EtwpApplyPayloadFilterInternal$filt$0](../../text/6D/EtwpApplyPayloadFilterInternal_filt_0_function_006D2F20.md) at `0x006D2F2A`
- [EtwpApplyPayloadFilterInternal$filt$1](../../text/6D/EtwpApplyPayloadFilterInternal_filt_1_function_006D2F37.md) at `0x006D2F41`
- [EtwpApplyPayloadFilterInternal$filt$3](../../text/6D/EtwpApplyPayloadFilterInternal_filt_3_function_006D2F4E.md) at `0x006D2F58`
- [EtwpApplyPayloadFilterInternal$filt$2](../../text/6D/EtwpApplyPayloadFilterInternal_filt_2_function_006D2F65.md) at `0x006D2F6F`
- [EtwpApplyPredicate$filt$2](../../text/6D/EtwpApplyPredicate_filt_2_function_006D2F90.md) at `0x006D2F99`
- [EtwpApplyPredicate$filt$1](../../text/6D/EtwpApplyPredicate_filt_1_function_006D2FA6.md) at `0x006D2FAF`
- [EtwpApplyPredicate$filt$4](../../text/6D/EtwpApplyPredicate_filt_4_function_006D2FBC.md) at `0x006D2FC5`
- [EtwpApplyPredicate$filt$3](../../text/6D/EtwpApplyPredicate_filt_3_function_006D2FD2.md) at `0x006D2FDB`
- [EtwpApplyPredicate$filt$0](../../text/6D/EtwpApplyPredicate_filt_0_function_006D2FE8.md) at `0x006D2FF1`
- [EtwpGetFieldValue$filt$0](../../text/6D/EtwpGetFieldValue_filt_0_function_006D3004.md) at `0x006D300D`
- [ExpGetSystemBasicInformation$filt$0](../../text/6D/ExpGetSystemBasicInformation_filt_0_function_006D3214.md) at `0x006D321D`
- [ExpGetSystemEmulationBasicInformation$filt$0](../../text/6D/ExpGetSystemEmulationBasicInformation_filt_0_function_006D355F.md) at `0x006D3568`
- [NtQueryInformationWorkerFactory$filt$0](../../text/6D/NtQueryInformationWorkerFactory_filt_0_function_006D4FE4.md) at `0x006D4FED`
- [EtwpGetSignedFieldValue$filt$0](../../text/6D/EtwpGetSignedFieldValue_filt_0_function_006D5548.md) at `0x006D5551`
- [ExPoolQueryLimits$filt$1](../../text/6D/ExPoolQueryLimits_filt_1_function_006D5BDF.md) at `0x006D5BE8`
- [ExPoolQueryLimits$filt$0](../../text/6D/ExPoolQueryLimits_filt_0_function_006D5BF5.md) at `0x006D5BFE`
- [NtSetInformationProcess$filt$3](../B1/NtSetInformationProcess_filt_3_function_00B141CA.md) at `0x00B141D3`
- [NtSetInformationProcess$filt$4](../B1/NtSetInformationProcess_filt_4_function_00B141E0.md) at `0x00B141E9`
- [NtSetInformationProcess$filt$5](../B1/NtSetInformationProcess_filt_5_function_00B141F6.md) at `0x00B141FF`
- [NtSetInformationProcess$filt$6](../B1/NtSetInformationProcess_filt_6_function_00B1420C.md) at `0x00B14215`
- [NtSetInformationProcess$filt$10](../B1/NtSetInformationProcess_filt_10_function_00B14222.md) at `0x00B1422B`
- [NtSetInformationProcess$filt$9](../B1/NtSetInformationProcess_filt_9_function_00B14238.md) at `0x00B14241`
- [NtSetInformationProcess$filt$8](../B1/NtSetInformationProcess_filt_8_function_00B1424E.md) at `0x00B14257`
- [NtSetInformationProcess$filt$7](../B1/NtSetInformationProcess_filt_7_function_00B14264.md) at `0x00B1426D`
- [NtSetInformationProcess$filt$14](../B1/NtSetInformationProcess_filt_14_function_00B1427A.md) at `0x00B14283`
- [NtSetInformationProcess$filt$13](../B1/NtSetInformationProcess_filt_13_function_00B14290.md) at `0x00B14299`
- [NtSetInformationProcess$filt$12](../B1/NtSetInformationProcess_filt_12_function_00B142A6.md) at `0x00B142AF`
- [NtSetInformationProcess$filt$11](../B1/NtSetInformationProcess_filt_11_function_00B142BC.md) at `0x00B142C5`
- [NtSetInformationProcess$filt$15](../B1/NtSetInformationProcess_filt_15_function_00B142D2.md) at `0x00B142DB`
- [NtSetInformationProcess$filt$16](../B1/NtSetInformationProcess_filt_16_function_00B142E8.md) at `0x00B142F1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C6980  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007C6989  33 C0                           xor eax, eax
007C698B  38 81 32 02 00 00               cmp byte ptr [rcx + 0x232], al
007C6991  0F 95 C0                        setne al
007C6994  C3                              ret
007C6995  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExSystemExceptionFilter(void)
{
    __int64 result;

    result = 0;
    result = ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void ExSystemExceptionFilter(void)
{
    int64_t result;

    result = 0;
    result = ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C6980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C6980[BB_007C6980]
  bb_007C6995[BB_007C6995]
```
