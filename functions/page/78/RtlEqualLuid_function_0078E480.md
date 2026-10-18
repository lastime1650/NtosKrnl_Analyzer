# RtlEqualLuid

- RVA: `0x0078E480`–`0x0078E496` (길이 `22` bytes)
- VA: `0x000000014078E480`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `22/22` bytes 표시
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
0078E480  8B 42 04                        mov eax, dword ptr [rdx + 4]
0078E483  39 41 04                        cmp dword ptr [rcx + 4], eax
0078E486  75 0A                           jne 0x14078e492
0078E488  8B 02                           mov eax, dword ptr [rdx]
0078E48A  39 01                           cmp dword ptr [rcx], eax
0078E48C  75 04                           jne 0x14078e492
0078E48E  B0 01                           mov al, 1
0078E490  C3                              ret
0078E491  CC                              int3
0078E492  32 C0                           xor al, al
0078E494  C3                              ret
0078E495  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlEqualLuid(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4))))) goto loc_0078E492;
    if ((*(unsigned int *)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_0078E492;
    return 1;
loc_0078E492:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlEqualLuid(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4))))) goto loc_0078E492;
    if ((*(uint32_t *)(arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_0078E492;
    return 1;
loc_0078E492:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0078E480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0078E480[BB_0078E480]
  bb_0078E488[BB_0078E488]
  bb_0078E48E[BB_0078E48E]
  bb_0078E491[BB_0078E491]
  bb_0078E492[BB_0078E492]
  bb_0078E495[BB_0078E495]
  bb_0078E480 -->|branch| bb_0078E492
  bb_0078E480 -->|fallthrough| bb_0078E488
  bb_0078E488 -->|branch| bb_0078E492
  bb_0078E488 -->|fallthrough| bb_0078E48E
  bb_0078E491 -->|flow| bb_0078E492
```
