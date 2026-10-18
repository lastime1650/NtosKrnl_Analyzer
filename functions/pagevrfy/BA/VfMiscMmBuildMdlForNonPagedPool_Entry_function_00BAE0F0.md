# VfMiscMmBuildMdlForNonPagedPool_Entry

- RVA: `0x00BAE0F0`–`0x00BAE13F` (길이 `79` bytes)
- VA: `0x0000000140BAE0F0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAE10A` → [MmDeterminePoolType](../../text/35/MmDeterminePoolType_function_0035F5B0.md) (function, `0x0035F5B0`)
- `0x00BAE134` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAE10A` → [MmDeterminePoolType](../../text/35/MmDeterminePoolType_function_0035F5B0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAE0F0  48 83 EC 48                     sub rsp, 0x48
00BAE0F4  48 8B D1                        mov rdx, rcx
00BAE0F7  44 0F 20 C0                     mov rax, cr8
00BAE0FB  84 C0                           test al, al
00BAE0FD  75 3A                           jne 0x140bae139
00BAE0FF  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
00BAE103  4D 8B 41 20                     mov r8, qword ptr [r9 + 0x20]
00BAE107  49 8B C8                        mov rcx, r8
00BAE10A  E8 A1 14 7B FF                  call 0x14035f5b0
00BAE10F  48 83 F8 40                     cmp rax, 0x40
00BAE113  74 24                           je 0x140bae139
00BAE115  48 8B 02                        mov rax, qword ptr [rdx]
00BAE118  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAE11D  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BAE125  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00BAE12A  45 33 C0                        xor r8d, r8d
00BAE12D  41 8D 50 7F                     lea edx, [r8 + 0x7f]
00BAE131  8D 4A 45                        lea ecx, [rdx + 0x45]
00BAE134  E8 CB F7 FE FF                  call 0x140b9d904
00BAE139  48 83 C4 48                     add rsp, 0x48
00BAE13D  C3                              ret
00BAE13E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscMmBuildMdlForNonPagedPool_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((unsigned __int8)(v_cr8) != 0) goto loc_00BAE139;
    result = MmDeterminePoolType(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), *(unsigned __int64 *)(a1 + 8));
    if (result != 64) {
        result = *(unsigned __int64 *)(a1);
        v_stack_m18 = result;
        v_stack_m20 = 11;
        v_stack_m28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        a3 = 0;
        a2 = a3 + 127;
        a1 = a2 + 69;
        result = CarReportRuleViolationFromNt(a1, a2, a3, *(unsigned __int64 *)(a1 + 8));
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscMmBuildMdlForNonPagedPool_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((uint8_t)(v_cr8) != 0) goto loc_00BAE139;
    result = MmDeterminePoolType(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), *(uint64_t *)(arg1 + 0x8));
    if (result != 64) {
        result = *(uint64_t *)(arg1);
        v_stack_m18 = result;
        v_stack_m20 = 11;
        v_stack_m28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        a3 = 0;
        a2 = a3 + 127;
        Arg1 = a2 + 69;
        result = CarReportRuleViolationFromNt(Arg1, a2, a3, *(uint64_t *)(arg1 + 0x8));
    }
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAE0F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAE0F0[BB_00BAE0F0]
  bb_00BAE0FF[BB_00BAE0FF]
  bb_00BAE115[BB_00BAE115]
  bb_00BAE139[BB_00BAE139]
  bb_00BAE13E[BB_00BAE13E]
  bb_00BAE0F0 -->|branch| bb_00BAE139
  bb_00BAE0F0 -->|fallthrough| bb_00BAE0FF
  bb_00BAE0FF -->|branch| bb_00BAE139
  bb_00BAE0FF -->|fallthrough| bb_00BAE115
  bb_00BAE115 -->|flow| bb_00BAE139
```
