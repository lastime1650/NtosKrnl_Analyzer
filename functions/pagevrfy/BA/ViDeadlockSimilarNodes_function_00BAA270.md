# ViDeadlockSimilarNodes

- RVA: `0x00BAA270`–`0x00BAA28D` (길이 `29` bytes)
- VA: `0x0000000140BAA270`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ViDeadlockCheckDuplicatesAmongChildren](ViDeadlockCheckDuplicatesAmongChildren_function_00BA9038.md) at `0x00BA906C`
- [ViDeadlockCheckDuplicatesAmongRoots](ViDeadlockCheckDuplicatesAmongRoots_function_00BA90B8.md) at `0x00BA90F6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAA270  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
00BAA274  48 39 41 38                     cmp qword ptr [rcx + 0x38], rax
00BAA278  75 0F                           jne 0x140baa289
00BAA27A  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
00BAA27D  33 42 48                        xor eax, dword ptr [rdx + 0x48]
00BAA280  D1 E8                           shr eax, 1
00BAA282  F7 D0                           not eax
00BAA284  83 E0 01                        and eax, 1
00BAA287  C3                              ret
00BAA288  CC                              int3
00BAA289  33 C0                           xor eax, eax
00BAA28B  C3                              ret
00BAA28C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDeadlockSimilarNodes(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a1 + 56)) != (*(unsigned __int64 *)(a2 + 56))) goto loc_00BAA289;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 72))) ^ (*(unsigned int *)(a2 + 72)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (1));
    return result;
loc_00BAA289:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViDeadlockSimilarNodes(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint64_t *)(arg1 + 0x38)) != (*(uint64_t *)(arg2 + 0x38))) goto loc_00BAA289;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x48))) ^ (*(uint32_t *)(arg2 + 0x48)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (1));
    return result;
loc_00BAA289:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAA270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAA270[BB_00BAA270]
  bb_00BAA27A[BB_00BAA27A]
  bb_00BAA288[BB_00BAA288]
  bb_00BAA289[BB_00BAA289]
  bb_00BAA28C[BB_00BAA28C]
  bb_00BAA270 -->|branch| bb_00BAA289
  bb_00BAA270 -->|fallthrough| bb_00BAA27A
  bb_00BAA288 -->|flow| bb_00BAA289
```
