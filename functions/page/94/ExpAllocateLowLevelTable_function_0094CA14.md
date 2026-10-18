# ExpAllocateLowLevelTable

- RVA: `0x0094CA14`–`0x0094CA41` (길이 `45` bytes)
- VA: `0x000000014094CA14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008AD5C`
- 디코드: `15`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094CA26` → [ExpAllocateTablePagedPoolNoZero](ExpAllocateTablePagedPoolNoZero_function_0094CA48.md) (function, `0x0094CA48`)

### Direct callers
- [ExpAllocateHandleTable](ExpAllocateHandleTable_function_0094C8F0.md) at `0x0094C98A`
- [ExpAllocateHandleTableEntrySlow](ExpAllocateHandleTableEntrySlow_function_0094D2FC.md) at `0x0094D34D`
- [ExpAllocateHandleTableEntrySlow](ExpAllocateHandleTableEntrySlow_function_0094D2FC.md) at `0x0094D3DE`
- [ExpAllocateMidLevelTable](ExpAllocateMidLevelTable_function_0094D5B4.md) at `0x0094D5EE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094CA14  40 53                           push rbx
0094CA16  48 83 EC 20                     sub rsp, 0x20
0094CA1A  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0094CA1E  48 8B DA                        mov rbx, rdx
0094CA21  BA 00 10 00 00                  mov edx, 0x1000
0094CA26  E8 1D 00 00 00                  call 0x14094ca48
0094CA2B  48 85 C0                        test rax, rax
0094CA2E  74 0F                           je 0x14094ca3f
0094CA30  48 83 20 00                     and qword ptr [rax], 0
0094CA34  48 89 58 08                     mov qword ptr [rax + 8], rbx
0094CA38  48 83 C4 20                     add rsp, 0x20
0094CA3C  5B                              pop rbx
0094CA3D  C3                              ret
0094CA3E  CC                              int3
0094CA3F  EB F7                           jmp 0x14094ca38
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAllocateLowLevelTable(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExpAllocateTablePagedPoolNoZero(*(unsigned __int64 *)(a1 + 16), (unsigned int)(0x1000ULL), a3, a4);
    if (result == 0) goto loc_0094CA3F;
    *(unsigned __int64 *)(result + 8) = a2;
loc_0094CA38:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0094CA3F:
    goto loc_0094CA38;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAllocateLowLevelTable(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExpAllocateTablePagedPoolNoZero(*(uint64_t *)(arg1 + 0x10), (uint32_t)(0x1000ULL), a3, a4);
    if (result == 0) goto loc_0094CA3F;
    *(uint64_t *)(result + 0x8) = Arg2;
loc_0094CA38:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0094CA3F:
    goto loc_0094CA38;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094CA14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094CA14[BB_0094CA14]
  bb_0094CA30[BB_0094CA30]
  bb_0094CA38[BB_0094CA38]
  bb_0094CA3E[BB_0094CA3E]
  bb_0094CA3F[BB_0094CA3F]
  bb_0094CA14 -->|branch| bb_0094CA3F
  bb_0094CA14 -->|fallthrough| bb_0094CA30
  bb_0094CA30 -->|flow| bb_0094CA38
  bb_0094CA3E -->|flow| bb_0094CA3F
  bb_0094CA3F -->|branch| bb_0094CA38
```
