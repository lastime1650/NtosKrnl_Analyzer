# PpmUtilityComparer

- RVA: `0x0047F870`–`0x0047F889` (길이 `25` bytes)
- VA: `0x000000014047F870`
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
0047F870  44 8B 01                        mov r8d, dword ptr [rcx]
0047F873  8B 0A                           mov ecx, dword ptr [rdx]
0047F875  44 3B C1                        cmp r8d, ecx
0047F878  77 0A                           ja 0x14047f884
0047F87A  33 C0                           xor eax, eax
0047F87C  44 3B C1                        cmp r8d, ecx
0047F87F  0F 92 C0                        setb al
0047F882  C3                              ret
0047F883  CC                              int3
0047F884  83 C8 FF                        or eax, 0xffffffff
0047F887  C3                              ret
0047F888  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmUtilityComparer(__int64 a1, __int64 a2)
{
    __int64 result;

    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_0047F884;
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) ? 1 : 0;
    return result;
loc_0047F884:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmUtilityComparer(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_0047F884;
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) ? 1 : 0;
    return result;
loc_0047F884:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047F870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047F870[BB_0047F870]
  bb_0047F87A[BB_0047F87A]
  bb_0047F883[BB_0047F883]
  bb_0047F884[BB_0047F884]
  bb_0047F888[BB_0047F888]
  bb_0047F870 -->|branch| bb_0047F884
  bb_0047F870 -->|fallthrough| bb_0047F87A
  bb_0047F883 -->|flow| bb_0047F884
```
