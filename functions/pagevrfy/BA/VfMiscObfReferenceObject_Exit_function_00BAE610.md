# VfMiscObfReferenceObject_Exit

- RVA: `0x00BAE610`–`0x00BAE64E` (길이 `62` bytes)
- VA: `0x0000000140BAE610`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `15`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAE643` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAE610  48 83 EC 48                     sub rsp, 0x48
00BAE614  41 B9 01 00 00 00               mov r9d, 1
00BAE61A  4C 39 49 10                     cmp qword ptr [rcx + 0x10], r9
00BAE61E  75 28                           jne 0x140bae648
00BAE620  48 8B 01                        mov rax, qword ptr [rcx]
00BAE623  41 8D 51 3E                     lea edx, [r9 + 0x3e]
00BAE627  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00BAE62B  B9 C4 00 00 00                  mov ecx, 0xc4
00BAE630  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAE635  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BAE63D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BAE643  E8 BC F2 FE FF                  call 0x140b9d904
00BAE648  48 83 C4 48                     add rsp, 0x48
00BAE64C  C3                              ret
00BAE64D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscObfReferenceObject_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int64 *)(a1 + 16)) == 1) {
        result = *(unsigned __int64 *)(a1);
        a2 = 1 + 62;
        a3 = *(unsigned __int64 *)(a1 + 8);
        a1 = 196;
        v_stack_m18 = result;
        v_stack_m20 = 11;
        result = CarReportRuleViolationFromNt(a1, a2, a3, 1);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscObfReferenceObject_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((*(uint64_t *)(arg1 + 0x10)) == 1) {
        result = *(uint64_t *)(arg1);
        a2 = 1 + 62;
        a3 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = 196;
        v_stack_m18 = result;
        v_stack_m20 = 11;
        result = CarReportRuleViolationFromNt(Arg1, a2, a3, 1);
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
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAE610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAE610[BB_00BAE610]
  bb_00BAE620[BB_00BAE620]
  bb_00BAE648[BB_00BAE648]
  bb_00BAE64D[BB_00BAE64D]
  bb_00BAE610 -->|branch| bb_00BAE648
  bb_00BAE610 -->|fallthrough| bb_00BAE620
  bb_00BAE620 -->|flow| bb_00BAE648
```
