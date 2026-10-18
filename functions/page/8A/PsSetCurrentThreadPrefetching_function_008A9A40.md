# PsSetCurrentThreadPrefetching

- RVA: `0x008A9A40`–`0x008A9A9B` (길이 `91` bytes)
- VA: `0x00000001408A9A40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `27`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008A9A8D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [PfSnSectionInfoCleanupWorkItem](PfSnSectionInfoCleanupWorkItem_function_008A8DA0.md) at `0x008A8DCB`
- [PfSnSectionInfoCleanupWorkItem](PfSnSectionInfoCleanupWorkItem_function_008A8DA0.md) at `0x008A8E26`
- [sub_008A8E86](Unknown_function_008A8E86.md) at `0x008A8EEC`
- [sub_008A9240](Unknown_function_008A9240.md) at `0x008A9255`
- [PfpPrefetchSharedStart](../93/PfpPrefetchSharedStart_function_00939D24.md) at `0x00939D55`
- [PfpPrefetchSharedCleanup](../93/PfpPrefetchSharedCleanup_function_00939EB0.md) at `0x00939F43`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008A9A8D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A9A40  40 53                           push rbx
008A9A42  48 83 EC 20                     sub rsp, 0x20
008A9A46  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
008A9A4F  C0 E1 06                        shl cl, 6
008A9A52  66 FF 8A E6 01 00 00            dec word ptr [rdx + 0x1e6]
008A9A59  90                              nop
008A9A5A  8A 82 A8 05 00 00               mov al, byte ptr [rdx + 0x5a8]
008A9A60  32 C8                           xor cl, al
008A9A62  8A D8                           mov bl, al
008A9A64  80 E1 40                        and cl, 0x40
008A9A67  C0 EB 06                        shr bl, 6
008A9A6A  32 C8                           xor cl, al
008A9A6C  80 E3 01                        and bl, 1
008A9A6F  88 8A A8 05 00 00               mov byte ptr [rdx + 0x5a8], cl
008A9A75  90                              nop
008A9A76  66 83 82 E6 01 00 00 01         add word ptr [rdx + 0x1e6], 1
008A9A7E  75 12                           jne 0x1408a9a92
008A9A80  48 8D 8A 98 00 00 00            lea rcx, [rdx + 0x98]
008A9A87  90                              nop
008A9A88  48 39 09                        cmp qword ptr [rcx], rcx
008A9A8B  74 05                           je 0x1408a9a92
008A9A8D  E8 EE 91 A3 FF                  call 0x1402e2c80
008A9A92  8A C3                           mov al, bl
008A9A94  48 83 C4 20                     add rsp, 0x20
008A9A98  5B                              pop rbx
008A9A99  C3                              ret
008A9A9A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSetCurrentThreadPrefetching(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (unsigned __int8)((a1) << (6));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448))));
    a1 = (unsigned __int8)((a1) & (64));
    v_rbx = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448))) >> (6));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448))));
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448) = a1;
    if (condition_is_not_equal) goto loc_008A9A92;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
int64_t PsSetCurrentThreadPrefetching(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (uint8_t)((Arg1) << (6));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8))));
    Arg1 = (uint8_t)((Arg1) & (64));
    local_rbx = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8))) >> (6));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8))));
    local_rbx = (uint8_t)((local_rbx) & (1));
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8) = Arg1;
    if (condition_is_not_equal) goto loc_008A9A92;
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)) + 152, *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A9A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A9A40[BB_008A9A40]
  bb_008A9A80[BB_008A9A80]
  bb_008A9A8D[BB_008A9A8D]
  bb_008A9A92[BB_008A9A92]
  bb_008A9A9A[BB_008A9A9A]
  bb_008A9A40 -->|branch| bb_008A9A92
  bb_008A9A40 -->|fallthrough| bb_008A9A80
  bb_008A9A80 -->|branch| bb_008A9A92
  bb_008A9A80 -->|fallthrough| bb_008A9A8D
  bb_008A9A8D -->|flow| bb_008A9A92
```
