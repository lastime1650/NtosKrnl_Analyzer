# KeReleaseInStackQueuedSpinLockForDpc

- RVA: `0x0046A3E0`–`0x0046A40B` (길이 `43` bytes)
- VA: `0x000000014046A3E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0046A3F9` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0046A404` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)

### Direct callers
- [KeRemoveByKeyDeviceQueueIfBusy](../5B/KeRemoveByKeyDeviceQueueIfBusy_function_005BE340.md) at `0x005BE38B`
- [DifKeReleaseInStackQueuedSpinLockForDpcWrapper](../63/DifKeReleaseInStackQueuedSpinLockForDpcWrapper_function_006313B0.md) at `0x00631476`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046A3E0  48 83 EC 28                     sub rsp, 0x28
0046A3E4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0046A3ED  8B 90 BC 38 00 00               mov edx, dword ptr [rax + 0x38bc]
0046A3F3  0F BA E2 10                     bt edx, 0x10
0046A3F7  72 0B                           jb 0x14046a404
0046A3F9  E8 B2 CD DA FF                  call 0x1402171b0
0046A3FE  48 83 C4 28                     add rsp, 0x28
0046A402  C3                              ret
0046A403  CC                              int3
0046A404  E8 D7 88 ED FF                  call 0x140342ce0
0046A409  EB F3                           jmp 0x14046a3fe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReleaseInStackQueuedSpinLockForDpc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (condition_is_below) goto loc_0046A404;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)), a3, a4);
loc_0046A3FE:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0046A404:
    result = KeReleaseInStackQueuedSpinLock(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)), a3, a4);
    goto loc_0046A3FE;
}
```

## 5. (Beta) C Style

```c
void KeReleaseInStackQueuedSpinLockForDpc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (condition_is_below) goto loc_0046A404;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)), a3, a4);
loc_0046A3FE:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0046A404:
    result = KeReleaseInStackQueuedSpinLock(a1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)), a3, a4);
    goto loc_0046A3FE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046A3E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046A3E0[BB_0046A3E0]
  bb_0046A3F9[BB_0046A3F9]
  bb_0046A3FE[BB_0046A3FE]
  bb_0046A403[BB_0046A403]
  bb_0046A404[BB_0046A404]
  bb_0046A3E0 -->|branch| bb_0046A404
  bb_0046A3E0 -->|fallthrough| bb_0046A3F9
  bb_0046A3F9 -->|flow| bb_0046A3FE
  bb_0046A403 -->|flow| bb_0046A404
  bb_0046A404 -->|branch| bb_0046A3FE
```
