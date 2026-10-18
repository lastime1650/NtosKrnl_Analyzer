# HalpCompareNumaMemoryRanges

- RVA: `0x00558E70`–`0x00558E8C` (길이 `28` bytes)
- VA: `0x0000000140558E70`
- 실행 섹션: `.text`
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
00558E70  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00558E74  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
00558E78  4C 3B C1                        cmp r8, rcx
00558E7B  73 05                           jae 0x140558e82
00558E7D  83 C8 FF                        or eax, 0xffffffff
00558E80  C3                              ret
00558E81  CC                              int3
00558E82  33 C0                           xor eax, eax
00558E84  4C 3B C1                        cmp r8, rcx
00558E87  0F 97 C0                        seta al
00558E8A  C3                              ret
00558E8B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCompareNumaMemoryRanges(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a1 + 8)) >= (*(unsigned __int64 *)(a2 + 8))) goto loc_00558E82;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_00558E82:
    result = 0;
    result = ((*(unsigned __int64 *)(a1 + 8)) > (*(unsigned __int64 *)(a2 + 8))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCompareNumaMemoryRanges(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint64_t *)(arg1 + 0x8)) >= (*(uint64_t *)(arg2 + 0x8))) goto loc_00558E82;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_00558E82:
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00558E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00558E70[BB_00558E70]
  bb_00558E7D[BB_00558E7D]
  bb_00558E81[BB_00558E81]
  bb_00558E82[BB_00558E82]
  bb_00558E8B[BB_00558E8B]
  bb_00558E70 -->|branch| bb_00558E82
  bb_00558E70 -->|fallthrough| bb_00558E7D
  bb_00558E81 -->|flow| bb_00558E82
```
