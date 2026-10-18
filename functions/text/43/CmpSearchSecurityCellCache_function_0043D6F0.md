# CmpSearchSecurityCellCache

- RVA: `0x0043D6F0`–`0x0043D703` (길이 `19` bytes)
- VA: `0x000000014043D6F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_009BCB28](../../page/9B/Unknown_function_009BCB28.md) at `0x009BCB6B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043D6F0  44 8B 01                        mov r8d, dword ptr [rcx]
0043D6F3  44 3B 02                        cmp r8d, dword ptr [rdx]
0043D6F6  77 04                           ja 0x14043d6fc
0043D6F8  1B C0                           sbb eax, eax
0043D6FA  C3                              ret
0043D6FB  CC                              int3
0043D6FC  B8 01 00 00 00                  mov eax, 1
0043D701  C3                              ret
0043D702  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSearchSecurityCellCache(__int64 a1, __int64 a2)
{
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > (*(unsigned int *)(a2))) goto loc_0043D6FC;
    return result;
loc_0043D6FC:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSearchSecurityCellCache(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > (*(uint32_t *)(arg2))) goto loc_0043D6FC;
    return result;
loc_0043D6FC:
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043D6F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043D6F0[BB_0043D6F0]
  bb_0043D6F8[BB_0043D6F8]
  bb_0043D6FB[BB_0043D6FB]
  bb_0043D6FC[BB_0043D6FC]
  bb_0043D702[BB_0043D702]
  bb_0043D6F0 -->|branch| bb_0043D6FC
  bb_0043D6F0 -->|fallthrough| bb_0043D6F8
  bb_0043D6FB -->|flow| bb_0043D6FC
```
