# Below4gb_MmAllocatePagesForMdl_Entry

- RVA: `0x00BAC2D0`–`0x00BAC314` (길이 `68` bytes)
- VA: `0x0000000140BAC2D0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `16`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAC309` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAC2D0  48 83 EC 48                     sub rsp, 0x48
00BAC2D4  4C 8B 41 18                     mov r8, qword ptr [rcx + 0x18]
00BAC2D8  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
00BAC2E2  4C 3B C0                        cmp r8, rax
00BAC2E5  73 27                           jae 0x140bac30e
00BAC2E7  48 8B 01                        mov rax, qword ptr [rcx]
00BAC2EA  BA 41 01 00 00                  mov edx, 0x141
00BAC2EF  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
00BAC2F3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAC2F8  C7 44 24 28 1A 00 00 00         mov dword ptr [rsp + 0x28], 0x1a
00BAC300  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BAC306  8D 4A 83                        lea ecx, [rdx - 0x7d]
00BAC309  E8 F6 15 FF FF                  call 0x140b9d904
00BAC30E  48 83 C4 48                     add rsp, 0x48
00BAC312  C3                              ret
00BAC313  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Below4gb_MmAllocatePagesForMdl_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int64 *)(a1 + 24)) < result) {
        result = *(unsigned __int64 *)(a1);
        a2 = 321;
        a4 = *(unsigned __int64 *)(a1 + 8);
        v_stack_m18 = result;
        v_stack_m20 = 26;
        a1 = a2 - 125;
        result = CarReportRuleViolationFromNt(a1, a2, *(unsigned __int64 *)(a1 + 24), a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Below4gb_MmAllocatePagesForMdl_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((*(uint64_t *)(arg1 + 0x18)) < result) {
        result = *(uint64_t *)(arg1);
        a2 = 321;
        a4 = *(uint64_t *)(arg1 + 0x8);
        v_stack_m18 = result;
        v_stack_m20 = 26;
        Arg1 = a2 - 125;
        result = CarReportRuleViolationFromNt(Arg1, a2, *(uint64_t *)(arg1 + 0x18), a4);
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
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAC2D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAC2D0[BB_00BAC2D0]
  bb_00BAC2E7[BB_00BAC2E7]
  bb_00BAC30E[BB_00BAC30E]
  bb_00BAC313[BB_00BAC313]
  bb_00BAC2D0 -->|branch| bb_00BAC30E
  bb_00BAC2D0 -->|fallthrough| bb_00BAC2E7
  bb_00BAC2E7 -->|flow| bb_00BAC30E
```
