# KiUpdateVpBackingThreadPriorityOnPriorityQuery

- RVA: `0x004BF550`–`0x004BF5B0` (길이 `96` bytes)
- VA: `0x00000001404BF550`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F13C`
- 디코드: `23`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BF569` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x004BF592` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x004BF5A9` → [KiUpdateVpBackingThreadPriorityFromTopLevel](../30/KiUpdateVpBackingThreadPriorityFromTopLevel_function_00303BA0.md) (function, `0x00303BA0`)

### Direct callers
- [KeQueryPriorityThread](../38/KeQueryPriorityThread_function_0038F4F0.md) at `0x0038F527`
- [KeQueryEffectivePriorityThread](../3C/KeQueryEffectivePriorityThread_function_003C7CA0.md) at `0x003C7F07`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BF550  40 53                           push rbx
004BF552  48 83 EC 20                     sub rsp, 0x20
004BF556  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
004BF55C  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
004BF561  48 8B D9                        mov rbx, rcx
004BF564  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
004BF569  E8 12 6D ED FF                  call 0x140396280
004BF56E  F7 43 78 00 00 40 00            test dword ptr [rbx + 0x78], 0x400000
004BF575  75 27                           jne 0x1404bf59e
004BF577  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
004BF57F  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004BF584  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
004BF58D  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
004BF592  E8 69 12 D9 FF                  call 0x140250800
004BF597  48 83 C4 20                     add rsp, 0x20
004BF59B  5B                              pop rbx
004BF59C  C3                              ret
004BF59D  CC                              int3
004BF59E  41 B0 01                        mov r8b, 1
004BF5A1  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004BF5A6  48 8B CB                        mov rcx, rbx
004BF5A9  E8 F2 45 E4 FF                  call 0x140303ba0
004BF5AE  EB C7                           jmp 0x1404bf577
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiUpdateVpBackingThreadPriorityOnPriorityQuery(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
    result = KiAcquireThreadLockRaiseToDpc(a1, v_stack_p8, a3, a4);
    if (((*(unsigned int *)(a1 + 120)) & (0x400000ULL)) != 0) goto loc_004BF59E;
loc_004BF577:
    *(unsigned __int64 *)(a1 + 64) = 0;
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_p10, v_stack_p8, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004BF59E:
    result = KiUpdateVpBackingThreadPriorityFromTopLevel(a1, v_stack_p38, 1, a4);
    goto loc_004BF577;
}
```

## 5. (Beta) C Style

```c
int64_t KiUpdateVpBackingThreadPriorityOnPriorityQuery(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
    result = KiAcquireThreadLockRaiseToDpc(Arg1, v_stack_p8, a3, a4);
    if (((*(uint32_t *)(arg1 + 0x78)) & (0x400000ULL)) != 0) goto loc_004BF59E;
loc_004BF577:
    *(uint64_t *)(arg1 + 0x40) = 0;
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_p10, v_stack_p8, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004BF59E:
    result = KiUpdateVpBackingThreadPriorityFromTopLevel(Arg1, v_stack_p38, 1, a4);
    goto loc_004BF577;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x78` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BF550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BF550[BB_004BF550]
  bb_004BF577[BB_004BF577]
  bb_004BF59D[BB_004BF59D]
  bb_004BF59E[BB_004BF59E]
  bb_004BF550 -->|branch| bb_004BF59E
  bb_004BF550 -->|fallthrough| bb_004BF577
  bb_004BF59D -->|flow| bb_004BF59E
  bb_004BF59E -->|branch| bb_004BF577
```
