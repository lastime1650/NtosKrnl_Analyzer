# IvtLegacyFlushTb

- RVA: `0x005714A0`–`0x005714E1` (길이 `65` bytes)
- VA: `0x00000001405714A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `17`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005714D6` → [IvtLegacyFlushTbInternal](IvtLegacyFlushTbInternal_function_005714E8.md) (function, `0x005714E8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005714A0  48 83 EC 48                     sub rsp, 0x48
005714A4  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005714A8  45 33 C0                        xor r8d, r8d
005714AB  90                              nop
005714AC  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
005714AF  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
005714B7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005714BC  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
005714C0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005714C4  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
005714C9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005714CE  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005714D3  45 33 C9                        xor r9d, r9d
005714D6  E8 0D 00 00 00                  call 0x1405714e8
005714DB  48 83 C4 48                     add rsp, 0x48
005714DF  C3                              ret
005714E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtLegacyFlushTb(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a3 = 0;
    v_stack_m10 = a7;
    v_stack_m18 = (unsigned int)((unsigned int)(a6));
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    a4 = 0;
    result = IvtLegacyFlushTbInternal(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IvtLegacyFlushTb(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg3 = 0;
    v_stack_m10 = Arg7;
    v_stack_m18 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    Arg4 = 0;
    result = IvtLegacyFlushTbInternal(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005714A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005714A0[BB_005714A0]
  bb_005714E0[BB_005714E0]
```
