# ArbAddAllocation

- RVA: `0x0070DE60`–`0x0070DEAA` (길이 `74` bytes)
- VA: `0x000000014070DE60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `18`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0070DE9F` → [RtlAddRange](../A8/RtlAddRange_function_00A8E860.md) (function, `0x00A8E860`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070DE60  48 83 EC 48                     sub rsp, 0x48
0070DE64  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0070DE68  4C 8B 4A 20                     mov r9, qword ptr [rdx + 0x20]
0070DE6C  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0070DE70  44 8B 40 24                     mov r8d, dword ptr [rax + 0x24]
0070DE74  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
0070DE78  41 83 E0 01                     and r8d, 1
0070DE7C  44 8A 4A 42                     mov r9b, byte ptr [rdx + 0x42]
0070DE80  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0070DE85  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0070DE8B  46 8D 04 45 01 00 00 00         lea r8d, [r8*2 + 1]
0070DE93  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0070DE98  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
0070DE9C  48 8B 12                        mov rdx, qword ptr [rdx]
0070DE9F  E8 BC 09 38 00                  call 0x140a8e860
0070DEA4  48 83 C4 48                     add rsp, 0x48
0070DEA8  C3                              ret
0070DEA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ArbAddAllocation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 40) + 36))) & (1));
    v_stack_m18 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 32);
    v_stack_m28 = (unsigned int)(a3 * 2 + 1);
    result = RtlAddRange(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a2), *(unsigned __int64 *)(a2 + 8), *(unsigned __int8 *)(a2 + 66));
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ArbAddAllocation(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x28) + 0x24))) & (1));
    v_stack_m18 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x20);
    v_stack_m28 = (uint32_t)(a3 * 2 + 1);
    result = RtlAddRange(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg2), *(uint64_t *)(arg2 + 0x8), *(uint8_t *)(arg2 + 0x42));
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x42` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070DE60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070DE60[BB_0070DE60]
  bb_0070DEA9[BB_0070DEA9]
```
