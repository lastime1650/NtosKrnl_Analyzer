# AsiSortHashTableHelper

- RVA: `0x00662F40`–`0x00662F59` (길이 `25` bytes)
- VA: `0x0000000140662F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `25/25` bytes 표시
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
00662F40  44 8B 01                        mov r8d, dword ptr [rcx]
00662F43  8B 0A                           mov ecx, dword ptr [rdx]
00662F45  44 3B C1                        cmp r8d, ecx
00662F48  73 05                           jae 0x140662f4f
00662F4A  83 C8 FF                        or eax, 0xffffffff
00662F4D  C3                              ret
00662F4E  CC                              int3
00662F4F  33 C0                           xor eax, eax
00662F51  44 3B C1                        cmp r8d, ecx
00662F54  0F 97 C0                        seta al
00662F57  C3                              ret
00662F58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AsiSortHashTableHelper(__int64 a1, __int64 a2)
{
    __int64 result;

    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_00662F4F;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_00662F4F:
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AsiSortHashTableHelper(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_00662F4F;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_00662F4F:
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00662F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00662F40[BB_00662F40]
  bb_00662F4A[BB_00662F4A]
  bb_00662F4E[BB_00662F4E]
  bb_00662F4F[BB_00662F4F]
  bb_00662F58[BB_00662F58]
  bb_00662F40 -->|branch| bb_00662F4F
  bb_00662F40 -->|fallthrough| bb_00662F4A
  bb_00662F4E -->|flow| bb_00662F4F
```
