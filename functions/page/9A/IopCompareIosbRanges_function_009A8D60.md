# IopCompareIosbRanges

- RVA: `0x009A8D60`–`0x009A8D76` (길이 `22` bytes)
- VA: `0x00000001409A8D60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `22/22` bytes 표시
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
009A8D60  48 8B 0A                        mov rcx, qword ptr [rdx]
009A8D63  49 8B 00                        mov rax, qword ptr [r8]
009A8D66  48 3B C1                        cmp rax, rcx
009A8D69  77 07                           ja 0x1409a8d72
009A8D6B  1B C0                           sbb eax, eax
009A8D6D  83 C0 02                        add eax, 2
009A8D70  C3                              ret
009A8D71  CC                              int3
009A8D72  33 C0                           xor eax, eax
009A8D74  C3                              ret
009A8D75  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCompareIosbRanges(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a3)) > (*(unsigned __int64 *)(a2))) goto loc_009A8D72;
    result = (unsigned int)((*(unsigned __int64 *)(a3)) + (2));
    return result;
loc_009A8D72:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopCompareIosbRanges(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if ((*(uint64_t *)(arg3)) > (*(uint64_t *)(arg2))) goto loc_009A8D72;
    result = (uint32_t)((*(uint64_t *)(arg3)) + (2));
    return result;
loc_009A8D72:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A8D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A8D60[BB_009A8D60]
  bb_009A8D6B[BB_009A8D6B]
  bb_009A8D71[BB_009A8D71]
  bb_009A8D72[BB_009A8D72]
  bb_009A8D75[BB_009A8D75]
  bb_009A8D60 -->|branch| bb_009A8D72
  bb_009A8D60 -->|fallthrough| bb_009A8D6B
  bb_009A8D71 -->|flow| bb_009A8D72
```
