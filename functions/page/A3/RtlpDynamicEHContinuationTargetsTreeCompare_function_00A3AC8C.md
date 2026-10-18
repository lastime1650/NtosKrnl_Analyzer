# RtlpDynamicEHContinuationTargetsTreeCompare

- RVA: `0x00A3AC8C`–`0x00A3ACA4` (길이 `24` bytes)
- VA: `0x0000000140A3AC8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspProcessDynamicEHContinuationTargets](../78/PspProcessDynamicEHContinuationTargets_function_00782348.md) at `0x00782523`
- [RtlAddDynamicEHContinuationTarget](../79/RtlAddDynamicEHContinuationTarget_function_00794DB8.md) at `0x00794DE4`
- [RtlpFindDynamicEHContinuationTarget](RtlpFindDynamicEHContinuationTarget_function_00A3ABA0.md) at `0x00A3AC2B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A3AC8C  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
00A3AC90  49 3B C8                        cmp rcx, r8
00A3AC93  73 05                           jae 0x140a3ac9a
00A3AC95  83 C8 FF                        or eax, 0xffffffff
00A3AC98  C3                              ret
00A3AC99  CC                              int3
00A3AC9A  33 C0                           xor eax, eax
00A3AC9C  49 3B C8                        cmp rcx, r8
00A3AC9F  0F 97 C0                        seta al
00A3ACA2  C3                              ret
00A3ACA3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpDynamicEHContinuationTargetsTreeCompare(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a1 >= (*(unsigned __int64 *)(a2 + 24))) goto loc_00A3AC9A;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_00A3AC9A:
    result = 0;
    result = (a1 > (*(unsigned __int64 *)(a2 + 24))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpDynamicEHContinuationTargetsTreeCompare(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg1 >= (*(uint64_t *)(arg2 + 0x18))) goto loc_00A3AC9A;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_00A3AC9A:
    result = 0;
    result = (Arg1 > (*(uint64_t *)(arg2 + 0x18))) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A3AC8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A3AC8C[BB_00A3AC8C]
  bb_00A3AC95[BB_00A3AC95]
  bb_00A3AC99[BB_00A3AC99]
  bb_00A3AC9A[BB_00A3AC9A]
  bb_00A3ACA3[BB_00A3ACA3]
  bb_00A3AC8C -->|branch| bb_00A3AC9A
  bb_00A3AC8C -->|fallthrough| bb_00A3AC95
  bb_00A3AC99 -->|flow| bb_00A3AC9A
```
