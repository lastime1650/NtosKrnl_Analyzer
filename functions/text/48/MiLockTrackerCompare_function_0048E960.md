# MiLockTrackerCompare

- RVA: `0x0048E960`–`0x0048E978` (길이 `24` bytes)
- VA: `0x000000014048E960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `24/24` bytes 표시
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
0048E960  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
0048E964  49 3B C8                        cmp rcx, r8
0048E967  73 05                           jae 0x14048e96e
0048E969  83 C8 FF                        or eax, 0xffffffff
0048E96C  C3                              ret
0048E96D  CC                              int3
0048E96E  33 C0                           xor eax, eax
0048E970  49 3B C8                        cmp rcx, r8
0048E973  0F 97 C0                        seta al
0048E976  C3                              ret
0048E977  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockTrackerCompare(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a1 >= (*(unsigned __int64 *)(a2 + 24))) goto loc_0048E96E;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_0048E96E:
    result = 0;
    result = (a1 > (*(unsigned __int64 *)(a2 + 24))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockTrackerCompare(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg1 >= (*(uint64_t *)(arg2 + 0x18))) goto loc_0048E96E;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_0048E96E:
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048E960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048E960[BB_0048E960]
  bb_0048E969[BB_0048E969]
  bb_0048E96D[BB_0048E96D]
  bb_0048E96E[BB_0048E96E]
  bb_0048E977[BB_0048E977]
  bb_0048E960 -->|branch| bb_0048E96E
  bb_0048E960 -->|fallthrough| bb_0048E969
  bb_0048E96D -->|flow| bb_0048E96E
```
