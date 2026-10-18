# HalPutScatterGatherListDmaThin

- RVA: `0x0043D8E0`–`0x0043D901` (길이 `33` bytes)
- VA: `0x000000014043D8E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0043D8F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0043D8F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043D8E0  48 83 EC 28                     sub rsp, 0x28
0043D8E4  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0043D8E8  48 8B C2                        mov rax, rdx
0043D8EB  80 79 61 00                     cmp byte ptr [rcx + 0x61], 0
0043D8EF  74 0A                           je 0x14043d8fb
0043D8F1  33 D2                           xor edx, edx
0043D8F3  48 8B C8                        mov rcx, rax
0043D8F6  E8 75 4F 74 00                  call 0x140b82870
0043D8FB  48 83 C4 28                     add rsp, 0x28
0043D8FF  C3                              ret
0043D900  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalPutScatterGatherListDmaThin(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 97)) != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalPutScatterGatherListDmaThin(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg2;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x61)) != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043D8E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043D8E0[BB_0043D8E0]
  bb_0043D8F1[BB_0043D8F1]
  bb_0043D8FB[BB_0043D8FB]
  bb_0043D900[BB_0043D900]
  bb_0043D8E0 -->|branch| bb_0043D8FB
  bb_0043D8E0 -->|fallthrough| bb_0043D8F1
  bb_0043D8F1 -->|flow| bb_0043D8FB
```
