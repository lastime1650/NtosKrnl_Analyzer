# PsLookupThreadByThreadId

- RVA: `0x00868300`–`0x00868310` (길이 `16` bytes)
- VA: `0x0000000140868300`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BD40`
- 디코드: `4`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtAlertMultipleThreadByThreadId](../78/NtAlertMultipleThreadByThreadId_function_00789650.md) at `0x0078980B`
- [PsOpenProcess](../89/PsOpenProcess_function_00894A30.md) at `0x00894BF1`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C5EF9`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C5F46`
- [PopInitSystemSleeperThread](../9E/PopInitSystemSleeperThread_function_009ECBA8.md) at `0x009ECC8D`
- [PsLookupProcessThreadByCid](../A3/PsLookupProcessThreadByCid_function_00A37420.md) at `0x00A3744B`
- [PopManageTransitionRecordRequest](../A6/PopManageTransitionRecordRequest_function_00A63B34.md) at `0x00A63C0C`
- [PfpServiceMainThreadBoostPrep](../AC/PfpServiceMainThreadBoostPrep_function_00ACB08C.md) at `0x00ACB0C1`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F684`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00868300  40 55                           push rbp
00868302  56                              push rsi
00868303  48 83 EC 48                     sub rsp, 0x48
00868307  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PsLookupThreadByThreadId(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    return;
}
```

## 5. (Beta) C Style

```c
void PsLookupThreadByThreadId(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00868300&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00868300[BB_00868300]
```
