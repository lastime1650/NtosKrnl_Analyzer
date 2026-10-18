# ViTargetUpdateTreeAllowed

- RVA: `0x00B9BC04`–`0x00B9BC1F` (길이 `27` bytes)
- VA: `0x0000000140B9BC04`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **17**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfTargetFreeContiguousMemory](VfTargetFreeContiguousMemory_function_00B9B6BC.md) at `0x00B9B6E1`
- [ViTargetAddToCounter](ViTargetAddToCounter_function_00B9B8E0.md) at `0x00B9B909`
- [VerifierKeAcquireQueuedSpinLock](VerifierKeAcquireQueuedSpinLock_function_00B9FBD0.md) at `0x00B9FC1B`
- [VerifierKeAcquireInStackQueuedSpinLockAtDpcLevel](../BA/VerifierKeAcquireInStackQueuedSpinLockAtDpcLevel_function_00BA4F20.md) at `0x00BA4F5E`
- [VerifierKeAcquireInStackQueuedSpinLockCommon](../BA/VerifierKeAcquireInStackQueuedSpinLockCommon_function_00BA4FD8.md) at `0x00BA502E`
- [VerifierKeAcquireInStackQueuedSpinLockForDpcCommon](../BA/VerifierKeAcquireInStackQueuedSpinLockForDpcCommon_function_00BA5100.md) at `0x00BA513C`
- [VerifierKeAcquireInStackQueuedSpinLockRaiseToSynch](../BA/VerifierKeAcquireInStackQueuedSpinLockRaiseToSynch_function_00BA51C0.md) at `0x00BA5218`
- [VerifierKeAcquireQueuedSpinLockRaiseToSynch](../BA/VerifierKeAcquireQueuedSpinLockRaiseToSynch_function_00BA52C0.md) at `0x00BA5310`
- [VerifierKeAcquireSpinLockAtDpcLevel](../BA/VerifierKeAcquireSpinLockAtDpcLevel_function_00BA53B0.md) at `0x00BA53E7`
- [VerifierKeSynchronizeExecution](../BA/VerifierKeSynchronizeExecution_function_00BA59A0.md) at `0x00BA59F4`
- [VerifierKeTryToAcquireQueuedSpinLock](../BA/VerifierKeTryToAcquireQueuedSpinLock_function_00BA5A80.md) at `0x00BA5AD8`
- [VerifierKeTryToAcquireQueuedSpinLockRaiseToSynch](../BA/VerifierKeTryToAcquireQueuedSpinLockRaiseToSynch_function_00BA5B80.md) at `0x00BA5BD8`
- [VerifierKeTryToAcquireSpinLockAtDpcLevel](../BA/VerifierKeTryToAcquireSpinLockAtDpcLevel_function_00BA5C80.md) at `0x00BA5CB7`
- [VerifierPortKeAcquireSpinLockNoXdv](../BA/VerifierPortKeAcquireSpinLockNoXdv_function_00BA5E80.md) at `0x00BA5EF0`
- [ViKeAcquireSpinLockCommon](../BA/ViKeAcquireSpinLockCommon_function_00BA60B0.md) at `0x00BA6123`
- [ViFaultsInjectionNotification](../BA/ViFaultsInjectionNotification_function_00BA6BDC.md) at `0x00BA6C1B`
- [VfHandlePoolAlloc](../BB/VfHandlePoolAlloc_function_00BB8A90.md) at `0x00BB8D4A`

### Static image references
- `0x00B9BC0F` → RVA `0x00F04954` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9BC04  33 C0                           xor eax, eax
00B9BC06  44 0F 20 C1                     mov rcx, cr8
00B9BC0A  80 F9 02                        cmp cl, 2
00B9BC0D  77 0E                           ja 0x140b9bc1d
00B9BC0F  8B 0D 3F 8D 36 00               mov ecx, dword ptr [rip + 0x368d3f]
00B9BC15  8D 50 01                        lea edx, [rax + 1]
00B9BC18  85 C9                           test ecx, ecx
00B9BC1A  0F 45 C2                        cmovne eax, edx
00B9BC1D  C3                              ret
00B9BC1E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViTargetUpdateTreeAllowed(void)
{
    __int64 result;

    result = 0;
    if (((unsigned __int8)(v_cr8)) <= 2) {
        a1 = *(unsigned int *)(v_rip + 3575103);
        a2 = result + 1;
        if ((unsigned int)(a1) != 0) { result = (unsigned int)(a2); }
    }
    return result;
}
```

## 5. (Beta) C Style

```c
void ViTargetUpdateTreeAllowed(void)
{
    int64_t result;

    result = 0;
    if (((uint8_t)(v_cr8)) <= 2) {
        a1 = *(uint32_t *)(v_rip + 0x368D3F);
        a2 = result + 1;
        if ((uint32_t)(a1) != 0) { result = (uint32_t)(a2); }
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9BC04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9BC04[BB_00B9BC04]
  bb_00B9BC0F[BB_00B9BC0F]
  bb_00B9BC1D[BB_00B9BC1D]
  bb_00B9BC1E[BB_00B9BC1E]
  bb_00B9BC04 -->|branch| bb_00B9BC1D
  bb_00B9BC04 -->|fallthrough| bb_00B9BC0F
  bb_00B9BC0F -->|flow| bb_00B9BC1D
```
