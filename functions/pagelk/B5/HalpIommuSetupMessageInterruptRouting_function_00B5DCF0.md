# HalpIommuSetupMessageInterruptRouting

- RVA: `0x00B5DCF0`–`0x00B5DD1A` (길이 `42` bytes)
- VA: `0x0000000140B5DCF0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `10`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B5DD0F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpIommuConfigureInterrupt](../../text/55/HalpIommuConfigureInterrupt_function_00553464.md) at `0x005535CE`
- [HalpIommuInitializeAll](../B7/HalpIommuInitializeAll_function_00B7A684.md) at `0x00B7A8D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B5DD0F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5DCF0  48 83 EC 38                     sub rsp, 0x38
00B5DCF4  48 8B 81 18 01 00 00            mov rax, qword ptr [rcx + 0x118]
00B5DCFB  B2 01                           mov dl, 1
00B5DCFD  44 8B 89 F8 01 00 00            mov r9d, dword ptr [rcx + 0x1f8]
00B5DD04  4C 8B 81 F0 01 00 00            mov r8, qword ptr [rcx + 0x1f0]
00B5DD0B  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B5DD0F  E8 BC CD B5 FF                  call 0x1406baad0
00B5DD14  48 83 C4 38                     add rsp, 0x38
00B5DD18  C3                              ret
00B5DD19  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuSetupMessageInterruptRouting(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 16), 1, *(unsigned __int64 *)(a1 + 496), (unsigned int)(*(unsigned int *)(a1 + 504)));
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIommuSetupMessageInterruptRouting(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x10), 1, *(uint64_t *)(arg1 + 0x1F0), (uint32_t)(*(uint32_t *)(arg1 + 0x1F8)));
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R` |
| `Arg1` | `+ 0x1F0` | `64` | `R` |
| `Arg1` | `+ 0x1F8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5DCF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5DCF0[BB_00B5DCF0]
  bb_00B5DD19[BB_00B5DD19]
```
