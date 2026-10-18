# CmpFreeSiloContextCallback

- RVA: `0x009E7BA0`–`0x009E7BE9` (길이 `73` bytes)
- VA: `0x00000001409E7BA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `21`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009E7BBD` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x009E7BC5` → [CmpStopSiloKeyLockTracker](CmpStopSiloKeyLockTracker_function_009E7BF0.md) (function, `0x009E7BF0`)
- `0x009E7BD3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009E7BDD` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009E7BBD` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x009E7BD3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009E7BDD` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E7BA0  40 53                           push rbx
009E7BA2  48 83 EC 40                     sub rsp, 0x40
009E7BA6  0F 57 C0                        xorps xmm0, xmm0
009E7BA9  33 C0                           xor eax, eax
009E7BAB  48 8B D9                        mov rbx, rcx
009E7BAE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009E7BB3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
009E7BB8  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
009E7BBD  E8 AE 42 A1 FF                  call 0x1403fbe70
009E7BC2  48 8B CB                        mov rcx, rbx
009E7BC5  E8 26 00 00 00                  call 0x1409e7bf0
009E7BCA  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009E7BCE  48 85 C9                        test rcx, rcx
009E7BD1  74 05                           je 0x1409e7bd8
009E7BD3  E8 78 17 91 FF                  call 0x1402f9350
009E7BD8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
009E7BDD  E8 6E 81 A3 FF                  call 0x14041fd50
009E7BE2  48 83 C4 40                     add rsp, 0x40
009E7BE6  5B                              pop rbx
009E7BE7  C3                              ret
009E7BE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFreeSiloContextCallback(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m28, a2, a3, a4);
    result = CmpStopSiloKeyLockTracker(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 32) != 0) {
        result = ObfDereferenceObject(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m28, a2, a3, a4);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFreeSiloContextCallback(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m28, a2, a3, a4);
    result = CmpStopSiloKeyLockTracker(Arg1, a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0x20) != 0) {
        result = ObfDereferenceObject(*(uint64_t *)(arg1 + 0x20), a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m28, a2, a3, a4);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E7BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E7BA0[BB_009E7BA0]
  bb_009E7BD3[BB_009E7BD3]
  bb_009E7BD8[BB_009E7BD8]
  bb_009E7BE8[BB_009E7BE8]
  bb_009E7BA0 -->|branch| bb_009E7BD8
  bb_009E7BA0 -->|fallthrough| bb_009E7BD3
  bb_009E7BD3 -->|flow| bb_009E7BD8
```
