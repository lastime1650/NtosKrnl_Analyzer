# KiNodeCostSort

- RVA: `0x00C388C0`–`0x00C388DC` (길이 `28` bytes)
- VA: `0x0000000140C388C0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `28/28` bytes 표시
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
00C388C0  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00C388C4  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
00C388C8  4C 3B C1                        cmp r8, rcx
00C388CB  73 05                           jae 0x140c388d2
00C388CD  83 C8 FF                        or eax, 0xffffffff
00C388D0  C3                              ret
00C388D1  CC                              int3
00C388D2  33 C0                           xor eax, eax
00C388D4  4C 3B C1                        cmp r8, rcx
00C388D7  0F 97 C0                        seta al
00C388DA  C3                              ret
00C388DB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiNodeCostSort(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a1 + 8)) >= (*(unsigned __int64 *)(a2 + 8))) goto loc_00C388D2;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_00C388D2:
    result = 0;
    result = ((*(unsigned __int64 *)(a1 + 8)) > (*(unsigned __int64 *)(a2 + 8))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiNodeCostSort(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint64_t *)(arg1 + 0x8)) >= (*(uint64_t *)(arg2 + 0x8))) goto loc_00C388D2;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_00C388D2:
    result = 0;
    result = ((*(uint64_t *)(arg1 + 0x8)) > (*(uint64_t *)(arg2 + 0x8))) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C388C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C388C0[BB_00C388C0]
  bb_00C388CD[BB_00C388CD]
  bb_00C388D1[BB_00C388D1]
  bb_00C388D2[BB_00C388D2]
  bb_00C388DB[BB_00C388DB]
  bb_00C388C0 -->|branch| bb_00C388D2
  bb_00C388C0 -->|fallthrough| bb_00C388CD
  bb_00C388D1 -->|flow| bb_00C388D2
```
