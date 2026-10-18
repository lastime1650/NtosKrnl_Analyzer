# ViIoInitializeTimer_Entry

- RVA: `0x006AACE0`–`0x006AAD1C` (길이 `60` bytes)
- VA: `0x00000001406AACE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `15`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006AAD11` → [CarReportRuleViolationFromNt](../../pagevrfy/B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006AAD11` → [CarReportRuleViolationFromNt](../../pagevrfy/B9/CarReportRuleViolationFromNt_function_00B9D904.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AACE0  48 83 EC 48                     sub rsp, 0x48
006AACE4  4C 8B 41 18                     mov r8, qword ptr [rcx + 0x18]
006AACE8  49 83 78 28 00                  cmp qword ptr [r8 + 0x28], 0
006AACED  74 27                           je 0x1406aad16
006AACEF  48 8B 01                        mov rax, qword ptr [rcx]
006AACF2  45 33 C9                        xor r9d, r9d
006AACF5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006AACFA  B9 C9 00 00 00                  mov ecx, 0xc9
006AACFF  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
006AAD07  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
006AAD0D  41 8D 51 0A                     lea edx, [r9 + 0xa]
006AAD11  E8 EE 2B 4F 00                  call 0x140b9d904
006AAD16  48 83 C4 48                     add rsp, 0x48
006AAD1A  C3                              ret
006AAD1B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIoInitializeTimer_Entry(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40)) != 0) {
        result = *(unsigned __int64 *)(a1);
        a4 = 0;
        v_stack_m18 = result;
        a1 = 201;
        v_stack_m20 = 4;
        a2 = a4 + 10;
        result = CarReportRuleViolationFromNt(a1, a2, *(unsigned __int64 *)(a1 + 24), a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIoInitializeTimer_Entry(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28)) != 0) {
        result = *(uint64_t *)(arg1);
        Arg4 = 0;
        v_stack_m18 = result;
        Arg1 = 201;
        v_stack_m20 = 4;
        Arg2 = Arg4 + 10;
        result = CarReportRuleViolationFromNt(Arg1, Arg2, *(uint64_t *)(arg1 + 0x18), Arg4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AACE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AACE0[BB_006AACE0]
  bb_006AACEF[BB_006AACEF]
  bb_006AAD16[BB_006AAD16]
  bb_006AAD1B[BB_006AAD1B]
  bb_006AACE0 -->|branch| bb_006AAD16
  bb_006AACE0 -->|fallthrough| bb_006AACEF
  bb_006AACEF -->|flow| bb_006AAD16
```
