# PipMergeDependencyTypes

- RVA: `0x005A56CC`–`0x005A5704` (길이 `56` bytes)
- VA: `0x00000001405A56CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005A56E2` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005A56F3` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PipAddRequestToEdge](../../page/72/PipAddRequestToEdge_function_00727898.md) at `0x007279C0`

### Static image references
- `0x005A56DB` → RVA `0x00F8CF08` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A56CC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005A56D1  57                              push rdi
005A56D2  48 83 EC 20                     sub rsp, 0x20
005A56D6  48 8B D9                        mov rbx, rcx
005A56D9  8B FA                           mov edi, edx
005A56DB  48 8D 0D 26 78 9E 00            lea rcx, [rip + 0x9e7826]
005A56E2  E8 89 2D C6 FF                  call 0x140208470
005A56E7  09 7B 30                        or dword ptr [rbx + 0x30], edi
005A56EA  48 8D 0D 17 78 9E 00            lea rcx, [rip + 0x9e7817]
005A56F1  8A D0                           mov dl, al
005A56F3  E8 A8 D4 DE FF                  call 0x140392ba0
005A56F8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005A56FD  48 83 C4 20                     add rsp, 0x20
005A5701  5F                              pop rdi
005A5702  C3                              ret
005A5703  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipMergeDependencyTypes(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10385446, a2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 10385431, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipMergeDependencyTypes(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10385446, Arg2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 10385431, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A56CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A56CC[BB_005A56CC]
  bb_005A5703[BB_005A5703]
```
