# PopDirectedDripsDisengageTimerCallback

- RVA: `0x005D11E0`–`0x005D1228` (길이 `72` bytes)
- VA: `0x00000001405D11E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `21`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D11F6` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005D1206` → [PopDirectedDripsClearDisengageReason](../47/PopDirectedDripsClearDisengageReason_function_00477EA4.md) (function, `0x00477EA4`)
- `0x005D1212` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D11E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005D11E5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005D11EA  57                              push rdi
005D11EB  48 83 EC 20                     sub rsp, 0x20
005D11EF  48 8D 4A 08                     lea rcx, [rdx + 8]
005D11F3  48 8B DA                        mov rbx, rdx
005D11F6  E8 75 72 C3 FF                  call 0x140208470
005D11FB  83 43 14 FF                     add dword ptr [rbx + 0x14], -1
005D11FF  40 8A F0                        mov sil, al
005D1202  75 07                           jne 0x1405d120b
005D1204  8B 0B                           mov ecx, dword ptr [rbx]
005D1206  E8 99 6C EA FF                  call 0x140477ea4
005D120B  40 8A D6                        mov dl, sil
005D120E  48 8D 4B 08                     lea rcx, [rbx + 8]
005D1212  E8 89 19 DC FF                  call 0x140392ba0
005D1217  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005D121C  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005D1221  48 83 C4 20                     add rsp, 0x20
005D1225  5F                              pop rdi
005D1226  C3                              ret
005D1227  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsDisengageTimerCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(a2 + 8, a2, a3, a4);
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned int *)(a2);
        result = PopDirectedDripsClearDisengageReason(a1, a2, a3, a4);
    }
    result = KeReleaseSpinLock(a2 + 8, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsDisengageTimerCallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(Arg2 + 8, Arg2, a3, a4);
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint32_t *)(arg2);
        result = PopDirectedDripsClearDisengageReason(Arg1, Arg2, a3, a4);
    }
    result = KeReleaseSpinLock(Arg2 + 8, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x14` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D11E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D11E0[BB_005D11E0]
  bb_005D1204[BB_005D1204]
  bb_005D120B[BB_005D120B]
  bb_005D1227[BB_005D1227]
  bb_005D11E0 -->|branch| bb_005D120B
  bb_005D11E0 -->|fallthrough| bb_005D1204
  bb_005D1204 -->|flow| bb_005D120B
```
