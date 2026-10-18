# CmpCompareLayerDescriptors

- RVA: `0x00ABFDD0`–`0x00ABFE00` (길이 `48` bytes)
- VA: `0x0000000140ABFDD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABFDD0  4C 8B 01                        mov r8, qword ptr [rcx]
00ABFDD3  4C 8B 0A                        mov r9, qword ptr [rdx]
00ABFDD6  41 8B 88 20 03 00 00            mov ecx, dword ptr [r8 + 0x320]
00ABFDDD  41 8B 81 20 03 00 00            mov eax, dword ptr [r9 + 0x320]
00ABFDE4  83 E1 01                        and ecx, 1
00ABFDE7  83 E0 01                        and eax, 1
00ABFDEA  2B C1                           sub eax, ecx
00ABFDEC  74 02                           je 0x140abfdf0
00ABFDEE  C3                              ret
00ABFDEF  CC                              int3
00ABFDF0  41 8B 80 1C 03 00 00            mov eax, dword ptr [r8 + 0x31c]
00ABFDF7  41 2B 81 1C 03 00 00            sub eax, dword ptr [r9 + 0x31c]
00ABFDFE  C3                              ret
00ABFDFF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCompareLayerDescriptors(__int64 a1, __int64 a2)
{
    __int64 result;

    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 800))) & (1));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 800))) & (1));
    result = (unsigned int)((result) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_00ABFDF0;
    return result;
loc_00ABFDF0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 796))) - (*(unsigned int *)(*(unsigned __int64 *)(a2) + 796)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCompareLayerDescriptors(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x320))) & (1));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x320))) & (1));
    result = (uint32_t)((result) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_00ABFDF0;
    return result;
loc_00ABFDF0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x31C))) - (*(uint32_t *)(*(uint64_t *)(arg2) + 0x31C)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABFDD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABFDD0[BB_00ABFDD0]
  bb_00ABFDEE[BB_00ABFDEE]
  bb_00ABFDEF[BB_00ABFDEF]
  bb_00ABFDF0[BB_00ABFDF0]
  bb_00ABFDFF[BB_00ABFDFF]
  bb_00ABFDD0 -->|branch| bb_00ABFDF0
  bb_00ABFDD0 -->|fallthrough| bb_00ABFDEE
  bb_00ABFDEF -->|flow| bb_00ABFDF0
```
