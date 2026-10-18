# KiScanQueues

- RVA: `0x0069BE90`–`0x0069BEB7` (길이 `39` bytes)
- VA: `0x000000014069BE90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0069BEAC` → [KiMcaDeferredRecoveryService](../6B/KiMcaDeferredRecoveryService_function_006BC790.md) (function, `0x006BC790`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069BE90  48 83 EC 38                     sub rsp, 0x38
0069BE94  48 8B 42 60                     mov rax, qword ptr [rdx + 0x60]
0069BE98  8B 4A 40                        mov ecx, dword ptr [rdx + 0x40]
0069BE9B  4C 8B 4A 58                     mov r9, qword ptr [rdx + 0x58]
0069BE9F  4C 8B 42 50                     mov r8, qword ptr [rdx + 0x50]
0069BEA3  48 8B 52 48                     mov rdx, qword ptr [rdx + 0x48]
0069BEA7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0069BEAC  E8 DF 08 02 00                  call 0x1406bc790
0069BEB1  48 83 C4 38                     add rsp, 0x38
0069BEB5  C3                              ret
0069BEB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiScanQueues(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = *(unsigned __int64 *)(a2 + 96);
    result = KiMcaDeferredRecoveryService((unsigned int)(*(unsigned int *)(a2 + 64)), *(unsigned __int64 *)(a2 + 72), *(unsigned __int64 *)(a2 + 80), *(unsigned __int64 *)(a2 + 88));
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiScanQueues(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = *(uint64_t *)(arg2 + 0x60);
    result = KiMcaDeferredRecoveryService((uint32_t)(*(uint32_t *)(arg2 + 0x40)), *(uint64_t *)(arg2 + 0x48), *(uint64_t *)(arg2 + 0x50), *(uint64_t *)(arg2 + 0x58));
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069BE90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069BE90[BB_0069BE90]
  bb_0069BEB6[BB_0069BEB6]
```
