# CmpTransDereferenceTransaction

- RVA: `0x00873608`–`0x0087361B` (길이 `19` bytes)
- VA: `0x0000000140873608`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00873610` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [CmpTransInitializeTransaction](../84/CmpTransInitializeTransaction_function_008422C8.md) at `0x00842446`
- [CmpCleanupTransactionState](../84/CmpCleanupTransactionState_function_008428E0.md) at `0x008429ED`
- [CmpTransSearchAddLightWeightTrans](CmpTransSearchAddLightWeightTrans_function_00873494.md) at `0x008734E8`
- [CmpTransSearchAddTransFromKeyBody](CmpTransSearchAddTransFromKeyBody_function_008736B8.md) at `0x00873723`
- [CmpTransSearchAddTrans](CmpTransSearchAddTrans_function_008743FC.md) at `0x008744CE`
- [NtOpenKeyTransactedEx](NtOpenKeyTransactedEx_function_00874EC0.md) at `0x00874FD6`
- [CmpRollbackTransactionArray](../94/CmpRollbackTransactionArray_function_0094B3AC.md) at `0x0094B3F3`
- [CmpPerformUnloadKey](../9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009B0005`
- [CmpPerformUnloadKey](../9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009B004C`
- [CmpPerformUnloadKey](../9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009B00CE`
- [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) at `0x009B0198`
- [CmpCleanupLightWeightTransaction](../9B/CmpCleanupLightWeightTransaction_function_009B1340.md) at `0x009B13D9`
- [NtCreateKeyTransacted](../AA/NtCreateKeyTransacted_function_00AAF830.md) at `0x00AAF988`
- [CmpAbortRollbackPacket](../AB/CmpAbortRollbackPacket_function_00ABEA80.md) at `0x00ABEADF`
- [CmRmFinalizeRecovery](../AB/CmRmFinalizeRecovery_function_00ABEB68.md) at `0x00ABEC18`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00873610` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00873608  48 83 EC 28                     sub rsp, 0x28
0087360C  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00873610  E8 3B 5D A8 FF                  call 0x1402f9350
00873615  48 83 C4 28                     add rsp, 0x28
00873619  C3                              ret
0087361A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTransDereferenceTransaction(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) & (-2);
    result = ObfDereferenceObject(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTransDereferenceTransaction(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) & (-2);
    result = ObfDereferenceObject(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00873608&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00873608[BB_00873608]
  bb_0087361A[BB_0087361A]
```
