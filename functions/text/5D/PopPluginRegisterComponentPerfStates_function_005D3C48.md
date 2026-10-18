# PopPluginRegisterComponentPerfStates

- RVA: `0x005D3C48`–`0x005D3C90` (길이 `72` bytes)
- VA: `0x00000001405D3C48`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082420`
- 디코드: `21`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D3C7F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopFxRegisterComponentPerfStates](../../page/75/PopFxRegisterComponentPerfStates_function_00759764.md) at `0x00759807`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D3C48  4C 8B DC                        mov r11, rsp
005D3C4B  48 83 EC 48                     sub rsp, 0x48
005D3C4F  4C 8B 51 40                     mov r10, qword ptr [rcx + 0x40]
005D3C53  45 33 C9                        xor r9d, r9d
005D3C56  45 89 4B E4                     mov dword ptr [r11 - 0x1c], r9d
005D3C5A  4D 85 D2                        test r10, r10
005D3C5D  74 28                           je 0x1405d3c87
005D3C5F  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
005D3C63  41 8D 49 20                     lea ecx, [r9 + 0x20]
005D3C67  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
005D3C6B  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
005D3C6F  49 8D 53 D8                     lea rdx, [r11 - 0x28]
005D3C73  4D 89 4B E8                     mov qword ptr [r11 - 0x18], r9
005D3C77  4D 89 43 F0                     mov qword ptr [r11 - 0x10], r8
005D3C7B  49 8B 42 60                     mov rax, qword ptr [r10 + 0x60]
005D3C7F  E8 4C 6E 0E 00                  call 0x1406baad0
005D3C84  44 8A C8                        mov r9b, al
005D3C87  41 8A C1                        mov al, r9b
005D3C8A  48 83 C4 48                     add rsp, 0x48
005D3C8E  C3                              ret
005D3C8F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPluginRegisterComponentPerfStates(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m20;

    v_rsp = (v_rsp) - (72);
    a4 = 0;
    *(unsigned int *)(v_rsp - 28) = 0;
    if (*(unsigned __int64 *)(a1 + 64) != 0) {
        result = *(unsigned __int64 *)(a1 + 72);
        a1 = a4 + 32;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        v_stack_m20 = a2;
        a2 = v_rsp - 40;
        *(unsigned __int64 *)(v_rsp - 24) = 0;
        *(unsigned __int64 *)(v_rsp - 16) = a3;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 96);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a4 = (unsigned __int8)(result);
    }
    v_rsp = (v_rsp) + (72);
    return (unsigned __int8)(a4);
}
```

## 5. (Beta) C Style

```c
int64_t PopPluginRegisterComponentPerfStates(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m20;

    local_rsp = (local_rsp) - (72);
    Arg4 = 0;
    *(uint32_t *)(local_rsp - 0x1C) = 0;
    if (*(uint64_t *)(arg1 + 0x40) != 0) {
        result = *(uint64_t *)(arg1 + 0x48);
        Arg1 = Arg4 + 32;
        *(uint64_t *)(local_rsp - 0x28) = result;
        v_stack_m20 = Arg2;
        Arg2 = local_rsp - 40;
        *(uint64_t *)(local_rsp - 0x18) = 0;
        *(uint64_t *)(local_rsp - 0x10) = Arg3;
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x60);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        Arg4 = (uint8_t)(result);
    }
    local_rsp = (local_rsp) + (72);
    return (uint8_t)(Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D3C48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D3C48[BB_005D3C48]
  bb_005D3C5F[BB_005D3C5F]
  bb_005D3C87[BB_005D3C87]
  bb_005D3C8F[BB_005D3C8F]
  bb_005D3C48 -->|branch| bb_005D3C87
  bb_005D3C48 -->|fallthrough| bb_005D3C5F
  bb_005D3C5F -->|flow| bb_005D3C87
```
