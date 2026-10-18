# CmpFileRead

- RVA: `0x00A6DBC0`–`0x00A6DBF6` (길이 `54` bytes)
- VA: `0x0000000140A6DBC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B47C0`
- 디코드: `16`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A6DBE7` → [CmpDoFileRead](../../text/48/CmpDoFileRead_function_00485658.md) (function, `0x00485658`)

### Direct callers
- [CmpSaveKeyByFileCopy](../7D/CmpSaveKeyByFileCopy_function_007DEFC0.md) at `0x007DF052`
- [CmpSaveKeyByFileCopy](../7D/CmpSaveKeyByFileCopy_function_007DEFC0.md) at `0x007DF0D3`
- [CmpSaveKeyByFileCopy](../7D/CmpSaveKeyByFileCopy_function_007DEFC0.md) at `0x007DF13E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A6DBE7` → [CmpDoFileRead](../../text/48/CmpDoFileRead_function_00485658.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6DBC0  48 83 EC 48                     sub rsp, 0x48
00A6DBC4  8B C2                           mov eax, edx
00A6DBC6  48 8B 94 C1 08 06 00 00         mov rdx, qword ptr [rcx + rax*8 + 0x608]
00A6DBCE  48 85 D2                        test rdx, rdx
00A6DBD1  74 1F                           je 0x140a6dbf2
00A6DBD3  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00A6DBD7  48 8B CA                        mov rcx, rdx
00A6DBDA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A6DBDF  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00A6DBE3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A6DBE7  E8 6C 7A A1 FF                  call 0x140485658
00A6DBEC  48 83 C4 48                     add rsp, 0x48
00A6DBF0  C3                              ret
00A6DBF1  CC                              int3
00A6DBF2  33 C0                           xor eax, eax
00A6DBF4  EB F6                           jmp 0x140a6dbec
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFileRead(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(a1 + (unsigned int)(a2) * 8 + 1544) == 0) goto loc_00A6DBF2;
    v_stack_m18 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = CmpDoFileRead(*(unsigned __int64 *)(a1 + (unsigned int)(a2) * 8 + 1544), *(unsigned __int64 *)(a1 + (unsigned int)(a2) * 8 + 1544), a3, a4);
loc_00A6DBEC:
    v_rsp = (v_rsp) + (72);
    return result;
loc_00A6DBF2:
    result = 0;
    goto loc_00A6DBEC;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFileRead(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(arg1 + (uint32_t)(Arg2) * 8 + 0x608) == 0) goto loc_00A6DBF2;
    v_stack_m18 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = CmpDoFileRead(*(uint64_t *)(arg1 + (uint32_t)(Arg2) * 8 + 0x608), *(uint64_t *)(arg1 + (uint32_t)(Arg2) * 8 + 0x608), Arg3, Arg4);
loc_00A6DBEC:
    local_rsp = (local_rsp) + (72);
    return result;
loc_00A6DBF2:
    result = 0;
    goto loc_00A6DBEC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x608 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6DBC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6DBC0[BB_00A6DBC0]
  bb_00A6DBD3[BB_00A6DBD3]
  bb_00A6DBEC[BB_00A6DBEC]
  bb_00A6DBF1[BB_00A6DBF1]
  bb_00A6DBF2[BB_00A6DBF2]
  bb_00A6DBC0 -->|branch| bb_00A6DBF2
  bb_00A6DBC0 -->|fallthrough| bb_00A6DBD3
  bb_00A6DBD3 -->|flow| bb_00A6DBEC
  bb_00A6DBF1 -->|flow| bb_00A6DBF2
  bb_00A6DBF2 -->|branch| bb_00A6DBEC
```
