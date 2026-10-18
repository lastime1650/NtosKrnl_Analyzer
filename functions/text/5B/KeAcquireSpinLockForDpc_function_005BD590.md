# KeAcquireSpinLockForDpc

- RVA: `0x005BD590`–`0x005BD5C4` (길이 `52` bytes)
- VA: `0x00000001405BD590`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005BD5AB` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005BD5B6` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BD590  40 53                           push rbx
005BD592  48 83 EC 20                     sub rsp, 0x20
005BD596  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
005BD59F  8B 90 BC 38 00 00               mov edx, dword ptr [rax + 0x38bc]
005BD5A5  0F BA E2 10                     bt edx, 0x10
005BD5A9  73 09                           jae 0x1405bd5b4
005BD5AB  E8 C0 AE C4 FF                  call 0x140208470
005BD5B0  8A D8                           mov bl, al
005BD5B2  EB 07                           jmp 0x1405bd5bb
005BD5B4  B3 02                           mov bl, 2
005BD5B6  E8 75 AE C4 FF                  call 0x140208430
005BD5BB  8A C3                           mov al, bl
005BD5BD  48 83 C4 20                     add rsp, 0x20
005BD5C1  5B                              pop rbx
005BD5C2  C3                              ret
005BD5C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeAcquireSpinLockForDpc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (condition_is_above_or_equal) goto loc_005BD5B4;
    result = KeAcquireSpinLockRaiseToDpc(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)), a3, a4);
    goto loc_005BD5BB;
loc_005BD5B4:
    result = KeAcquireSpinLockAtDpcLevel(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)), a3, a4);
loc_005BD5BB:
    v_rsp = (v_rsp) + (32);
    return 2;
}
```

## 5. (Beta) C Style

```c
void KeAcquireSpinLockForDpc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (condition_is_above_or_equal) goto loc_005BD5B4;
    result = KeAcquireSpinLockRaiseToDpc(a1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)), a3, a4);
    goto loc_005BD5BB;
loc_005BD5B4:
    result = KeAcquireSpinLockAtDpcLevel(a1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)), a3, a4);
loc_005BD5BB:
    local_rsp = (local_rsp) + (32);
    return 2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BD590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005BD590[BB_005BD590]
  bb_005BD5AB[BB_005BD5AB]
  bb_005BD5B4[BB_005BD5B4]
  bb_005BD5BB[BB_005BD5BB]
  bb_005BD5C3[BB_005BD5C3]
  bb_005BD590 -->|branch| bb_005BD5B4
  bb_005BD590 -->|fallthrough| bb_005BD5AB
  bb_005BD5AB -->|branch| bb_005BD5BB
  bb_005BD5B4 -->|flow| bb_005BD5BB
```
