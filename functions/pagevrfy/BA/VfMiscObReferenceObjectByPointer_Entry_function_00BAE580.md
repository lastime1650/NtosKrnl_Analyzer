# VfMiscObReferenceObjectByPointer_Entry

- RVA: `0x00BAE580`–`0x00BAE5D5` (길이 `85` bytes)
- VA: `0x0000000140BAE580`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `22`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAE595` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (function, `0x004BC694`)
- `0x00BAE5C9` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAE595` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAE580  40 53                           push rbx
00BAE582  48 83 EC 40                     sub rsp, 0x40
00BAE586  4C 8B 01                        mov r8, qword ptr [rcx]
00BAE589  48 8B D9                        mov rbx, rcx
00BAE58C  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00BAE590  BA 08 00 00 00                  mov edx, 8
00BAE595  E8 FA E0 90 FF                  call 0x1404bc694
00BAE59A  4C 8B 43 20                     mov r8, qword ptr [rbx + 0x20]
00BAE59E  49 83 78 D0 00                  cmp qword ptr [r8 - 0x30], 0
00BAE5A3  75 29                           jne 0x140bae5ce
00BAE5A5  48 8B 03                        mov rax, qword ptr [rbx]
00BAE5A8  BA 3F 00 00 00                  mov edx, 0x3f
00BAE5AD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAE5B2  B9 C4 00 00 00                  mov ecx, 0xc4
00BAE5B7  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BAE5BF  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BAE5C5  44 8D 4A C2                     lea r9d, [rdx - 0x3e]
00BAE5C9  E8 36 F3 FE FF                  call 0x140b9d904
00BAE5CE  48 83 C4 40                     add rsp, 0x40
00BAE5D2  5B                              pop rbx
00BAE5D3  C3                              ret
00BAE5D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscObReferenceObjectByPointer_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    result = VfMiscCheckKernelAddress(*(unsigned __int64 *)(a1 + 32), 8, *(unsigned __int64 *)(a1), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) - 48)) == 0) {
        result = *(unsigned __int64 *)(a1);
        a2 = 63;
        v_stack_m18 = result;
        a1 = 196;
        v_stack_m20 = 11;
        a4 = a2 - 62;
        result = CarReportRuleViolationFromNt(a1, a2, *(unsigned __int64 *)(a1 + 32), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscObReferenceObjectByPointer_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    result = VfMiscCheckKernelAddress(*(uint64_t *)(arg1 + 0x20), 8, *(uint64_t *)(arg1), a4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) - 0x30)) == 0) {
        result = *(uint64_t *)(arg1);
        a2 = 63;
        v_stack_m18 = result;
        Arg1 = 196;
        v_stack_m20 = 11;
        a4 = a2 - 62;
        result = CarReportRuleViolationFromNt(Arg1, a2, *(uint64_t *)(arg1 + 0x20), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAE580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAE580[BB_00BAE580]
  bb_00BAE5A5[BB_00BAE5A5]
  bb_00BAE5CE[BB_00BAE5CE]
  bb_00BAE5D4[BB_00BAE5D4]
  bb_00BAE580 -->|branch| bb_00BAE5CE
  bb_00BAE580 -->|fallthrough| bb_00BAE5A5
  bb_00BAE5A5 -->|flow| bb_00BAE5CE
```
