# VmpVaRangeNumberOfGpaRanges

- RVA: `0x00429E34`–`0x00429E4C` (길이 `24` bytes)
- VA: `0x0000000140429E34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VmpSplitMemoryRange](VmpSplitMemoryRange_function_00429754.md) at `0x004297F6`
- [VmpRemoveMemoryRange](../48/VmpRemoveMemoryRange_function_00489018.md) at `0x00489264`
- [VmpMergeMemoryRanges](../4D/VmpMergeMemoryRanges_function_004D9EDC.md) at `0x004D9FA8`
- [VmpMergeMemoryRanges](../4D/VmpMergeMemoryRanges_function_004D9EDC.md) at `0x004D9FB3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00429E34  48 8D 51 28                     lea rdx, [rcx + 0x28]
00429E38  33 C0                           xor eax, eax
00429E3A  48 8B 0A                        mov rcx, qword ptr [rdx]
00429E3D  EB 06                           jmp 0x140429e45
00429E3F  48 8B 09                        mov rcx, qword ptr [rcx]
00429E42  48 FF C0                        inc rax
00429E45  48 3B CA                        cmp rcx, rdx
00429E48  75 F5                           jne 0x140429e3f
00429E4A  C3                              ret
00429E4B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpVaRangeNumberOfGpaRanges(__int64 a1)
{
    __int64 result;

    result = 0;
    goto loc_00429E45;
loc_00429E3F:
    result = (result) + 1;
loc_00429E45:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40))) != (a1 + 40)) goto loc_00429E3F;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpVaRangeNumberOfGpaRanges(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    goto loc_00429E45;
loc_00429E3F:
    result = (result) + 1;
loc_00429E45:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x28))) != (Arg1 + 40)) goto loc_00429E3F;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00429E34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00429E34[BB_00429E34]
  bb_00429E3F[BB_00429E3F]
  bb_00429E45[BB_00429E45]
  bb_00429E4A[BB_00429E4A]
  bb_00429E4B[BB_00429E4B]
  bb_00429E34 -->|branch| bb_00429E45
  bb_00429E3F -->|flow| bb_00429E45
  bb_00429E45 -->|branch| bb_00429E3F
  bb_00429E45 -->|fallthrough| bb_00429E4A
```
