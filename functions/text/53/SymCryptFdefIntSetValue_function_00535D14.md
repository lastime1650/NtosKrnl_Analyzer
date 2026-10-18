# SymCryptFdefIntSetValue

- RVA: `0x00535D14`–`0x00535D2F` (길이 `27` bytes)
- VA: `0x0000000140535D14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00535D24` → [SymCryptFdefRawSetValue](SymCryptFdefRawSetValue_function_00535EB0.md) (function, `0x00535EB0`)

### Direct callers
- [SymCryptIntSetValue](../52/SymCryptIntSetValue_function_00525730.md) at `0x00525734`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00535D14  48 83 EC 38                     sub rsp, 0x38
00535D18  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00535D1C  49 83 C1 20                     add r9, 0x20
00535D20  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00535D24  E8 87 01 00 00                  call 0x140535eb0
00535D29  48 83 C4 38                     add rsp, 0x38
00535D2D  C3                              ret
00535D2E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntSetValue(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = (a4) + (32);
    v_stack_m18 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)));
    result = SymCryptFdefRawSetValue(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntSetValue(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = (Arg4) + (32);
    v_stack_m18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)));
    result = SymCryptFdefRawSetValue(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00535D14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00535D14[BB_00535D14]
  bb_00535D2E[BB_00535D2E]
```
