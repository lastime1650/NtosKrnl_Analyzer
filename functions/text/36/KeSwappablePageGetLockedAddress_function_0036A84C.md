# KeSwappablePageGetLockedAddress

- RVA: `0x0036A84C`–`0x0036A85D` (길이 `17` bytes)
- VA: `0x000000014036A84C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeSwapProcessOrStack](../5C/KeSwapProcessOrStack_function_005C5E00.md) at `0x005C5EB4`
- [PspSchedulerSharedDataRegionSlotAllocate](../../page/A2/PspSchedulerSharedDataRegionSlotAllocate_function_00A268C8.md) at `0x00A26A7F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036A84C  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0036A850  A8 01                           test al, 1
0036A852  74 05                           je 0x14036a859
0036A854  48 8B 01                        mov rax, qword ptr [rcx]
0036A857  C3                              ret
0036A858  CC                              int3
0036A859  33 C0                           xor eax, eax
0036A85B  C3                              ret
0036A85C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSwappablePageGetLockedAddress(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) == 0) goto loc_0036A859;
    return *(unsigned __int64 *)(a1);
loc_0036A859:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeSwappablePageGetLockedAddress(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) == 0) goto loc_0036A859;
    return *(uint64_t *)(arg1);
loc_0036A859:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036A84C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0036A84C[BB_0036A84C]
  bb_0036A854[BB_0036A854]
  bb_0036A858[BB_0036A858]
  bb_0036A859[BB_0036A859]
  bb_0036A85C[BB_0036A85C]
  bb_0036A84C -->|branch| bb_0036A859
  bb_0036A84C -->|fallthrough| bb_0036A854
  bb_0036A858 -->|flow| bb_0036A859
```
