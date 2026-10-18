# HalpPmuArbiterNotifyActor

- RVA: `0x00707B54`–`0x00707B7C` (길이 `40` bytes)
- VA: `0x0000000140707B54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00707B71` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpNotifyActorIfPmuAvailable](HalpNotifyActorIfPmuAvailable_function_00707880.md) at `0x007079E8`
- [HalpRequestPmuAccess](../AD/HalpRequestPmuAccess_function_00ADB340.md) at `0x00ADB462`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00707B71` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00707B54  48 83 EC 28                     sub rsp, 0x28
00707B58  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00707B5C  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00707B60  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00707B64  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00707B69  C7 44 24 30 01 00 08 00         mov dword ptr [rsp + 0x30], 0x80001
00707B71  E8 5A 2F FB FF                  call 0x1406baad0
00707B76  48 83 C4 28                     add rsp, 0x28
00707B7A  C3                              ret
00707B7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPmuArbiterNotifyActor(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pC;

    v_rsp = (v_rsp) - (40);
    v_stack_pC = a2;
    v_stack_p8 = 0x80001ULL;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 24), v_stack_p8, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpPmuArbiterNotifyActor(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;
    uint32_t v_stack_pC;

    local_rsp = (local_rsp) - (40);
    v_stack_pC = Arg2;
    v_stack_p8 = 0x80001ULL;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x18), v_stack_p8, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00707B54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00707B54[BB_00707B54]
  bb_00707B7B[BB_00707B7B]
```
