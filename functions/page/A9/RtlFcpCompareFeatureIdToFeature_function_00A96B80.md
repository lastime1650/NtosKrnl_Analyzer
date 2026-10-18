# RtlFcpCompareFeatureIdToFeature

- RVA: `0x00A96B80`–`0x00A96B91` (길이 `17` bytes)
- VA: `0x0000000140A96B80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpFcQueryFeatureConfigurationFromBuffers](../9B/RtlpFcQueryFeatureConfigurationFromBuffers_function_009BC928.md) at `0x009BC9C5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A96B80  8B 01                           mov eax, dword ptr [rcx]
00A96B82  3B 02                           cmp eax, dword ptr [rdx]
00A96B84  77 04                           ja 0x140a96b8a
00A96B86  1B C0                           sbb eax, eax
00A96B88  C3                              ret
00A96B89  CC                              int3
00A96B8A  B8 01 00 00 00                  mov eax, 1
00A96B8F  C3                              ret
00A96B90  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFcpCompareFeatureIdToFeature(__int64 a1, __int64 a2)
{
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > (*(unsigned int *)(a2))) goto loc_00A96B8A;
    return (unsigned int)(*(unsigned int *)(a1));
loc_00A96B8A:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t RtlFcpCompareFeatureIdToFeature(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > (*(uint32_t *)(arg2))) goto loc_00A96B8A;
    return (uint32_t)(*(uint32_t *)(arg1));
loc_00A96B8A:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A96B80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A96B80[BB_00A96B80]
  bb_00A96B86[BB_00A96B86]
  bb_00A96B89[BB_00A96B89]
  bb_00A96B8A[BB_00A96B8A]
  bb_00A96B90[BB_00A96B90]
  bb_00A96B80 -->|branch| bb_00A96B8A
  bb_00A96B80 -->|fallthrough| bb_00A96B86
  bb_00A96B89 -->|flow| bb_00A96B8A
```
