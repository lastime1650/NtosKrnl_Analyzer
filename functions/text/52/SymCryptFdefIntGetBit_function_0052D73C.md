# SymCryptFdefIntGetBit

- RVA: `0x0052D73C`–`0x0052D752` (길이 `22` bytes)
- VA: `0x000000014052D73C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptIntGetBit](SymCryptIntGetBit_function_00525620.md) at `0x00525624`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D73C  8B C2                           mov eax, edx
0052D73E  83 E2 1F                        and edx, 0x1f
0052D741  48 C1 E8 05                     shr rax, 5
0052D745  8B 44 81 20                     mov eax, dword ptr [rcx + rax*4 + 0x20]
0052D749  8A CA                           mov cl, dl
0052D74B  D3 E8                           shr eax, cl
0052D74D  83 E0 01                        and eax, 1
0052D750  C3                              ret
0052D751  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntGetBit(__int64 a1, int a2)
{
    __int64 result;

    a2 = (unsigned int)((a2) & (31));
    result = ((unsigned int)(a2)) >> (5);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 4 + 32))) >> ((unsigned __int8)((unsigned __int8)(a2))));
    result = (unsigned int)((result) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntGetBit(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg2 = (uint32_t)((Arg2) & (31));
    result = ((uint32_t)(Arg2)) >> (5);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + result * 4 + 0x20))) >> ((uint8_t)((uint8_t)(Arg2))));
    result = (uint32_t)((result) & (1));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20 + rax*4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D73C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D73C[BB_0052D73C]
  bb_0052D751[BB_0052D751]
```
