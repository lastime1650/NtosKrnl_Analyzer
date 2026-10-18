# Below4gb_MmAllocateNodePagesForMdlEx_Entry

- RVA: `0x00BAC230`–`0x00BAC274` (길이 `68` bytes)
- VA: `0x0000000140BAC230`
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
- `0x00BAC269` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAC230  48 83 EC 48                     sub rsp, 0x48
00BAC234  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00BAC238  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
00BAC242  4C 3B C0                        cmp r8, rax
00BAC245  73 27                           jae 0x140bac26e
00BAC247  48 8B 01                        mov rax, qword ptr [rcx]
00BAC24A  BA 41 01 00 00                  mov edx, 0x141
00BAC24F  4C 8B 49 18                     mov r9, qword ptr [rcx + 0x18]
00BAC253  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAC258  C7 44 24 28 1A 00 00 00         mov dword ptr [rsp + 0x28], 0x1a
00BAC260  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BAC266  8D 4A 83                        lea ecx, [rdx - 0x7d]
00BAC269  E8 96 16 FF FF                  call 0x140b9d904
00BAC26E  48 83 C4 48                     add rsp, 0x48
00BAC272  C3                              ret
00BAC273  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Below4gb_MmAllocateNodePagesForMdlEx_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int64 *)(a1 + 40)) < result) {
        result = *(unsigned __int64 *)(a1);
        a2 = 321;
        a4 = *(unsigned __int64 *)(a1 + 24);
        v_stack_m18 = result;
        v_stack_m20 = 26;
        a1 = a2 - 125;
        result = CarReportRuleViolationFromNt(a1, a2, *(unsigned __int64 *)(a1 + 40), a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Below4gb_MmAllocateNodePagesForMdlEx_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((*(uint64_t *)(arg1 + 0x28)) < result) {
        result = *(uint64_t *)(arg1);
        a2 = 321;
        a4 = *(uint64_t *)(arg1 + 0x18);
        v_stack_m18 = result;
        v_stack_m20 = 26;
        Arg1 = a2 - 125;
        result = CarReportRuleViolationFromNt(Arg1, a2, *(uint64_t *)(arg1 + 0x28), a4);
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
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAC230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAC230[BB_00BAC230]
  bb_00BAC247[BB_00BAC247]
  bb_00BAC26E[BB_00BAC26E]
  bb_00BAC273[BB_00BAC273]
  bb_00BAC230 -->|branch| bb_00BAC26E
  bb_00BAC230 -->|fallthrough| bb_00BAC247
  bb_00BAC247 -->|flow| bb_00BAC26E
```
