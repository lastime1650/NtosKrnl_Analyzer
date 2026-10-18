# KiFreezeDataTableEntry

- RVA: `0x005B1F70`–`0x005B1FA0` (길이 `48` bytes)
- VA: `0x00000001405B1F70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `48/48` bytes 표시
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
005B1F70  44 0F B7 41 6E                  movzx r8d, word ptr [rcx + 0x6e]
005B1F75  41 0F B7 C0                     movzx eax, r8w
005B1F79  66 C1 E8 07                     shr ax, 7
005B1F7D  66 83 E0 03                     and ax, 3
005B1F81  66 3B C2                        cmp ax, dx
005B1F84  73 18                           jae 0x1405b1f9e
005B1F86  66 C1 E2 07                     shl dx, 7
005B1F8A  B8 80 01 00 00                  mov eax, 0x180
005B1F8F  66 41 33 D0                     xor dx, r8w
005B1F93  66 23 D0                        and dx, ax
005B1F96  66 41 33 D0                     xor dx, r8w
005B1F9A  66 89 51 6E                     mov word ptr [rcx + 0x6e], dx
005B1F9E  C3                              ret
005B1F9F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiFreezeDataTableEntry(__int64 a1, unsigned __int16 a2)
{
    __int64 result;

    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 110))) >> (7));
    result = (unsigned __int16)((result) & (3));
    if (((unsigned __int16)(result)) < a2) {
        a2 = (unsigned __int16)((a2) << (7));
        result = 384;
        a2 = (unsigned __int16)((a2) ^ ((unsigned __int16)(*(unsigned __int16 *)(a1 + 110))));
        a2 = (unsigned __int16)((a2) & ((unsigned __int16)(result)));
        a2 = (unsigned __int16)((a2) ^ ((unsigned __int16)(*(unsigned __int16 *)(a1 + 110))));
        *(unsigned __int16 *)(a1 + 110) = a2;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiFreezeDataTableEntry(void *Arg1, uint16_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x6E))) >> (7));
    result = (uint16_t)((result) & (3));
    if (((uint16_t)(result)) < Arg2) {
        Arg2 = (uint16_t)((Arg2) << (7));
        result = 384;
        Arg2 = (uint16_t)((Arg2) ^ ((uint16_t)(*(uint16_t *)(arg1 + 0x6E))));
        Arg2 = (uint16_t)((Arg2) & ((uint16_t)(result)));
        Arg2 = (uint16_t)((Arg2) ^ ((uint16_t)(*(uint16_t *)(arg1 + 0x6E))));
        *(uint16_t *)(arg1 + 0x6E) = Arg2;
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x6E` | `16` | `R` |
| `Arg1` | `+ 0x6E` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B1F70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B1F70[BB_005B1F70]
  bb_005B1F86[BB_005B1F86]
  bb_005B1F9E[BB_005B1F9E]
  bb_005B1F9F[BB_005B1F9F]
  bb_005B1F70 -->|branch| bb_005B1F9E
  bb_005B1F70 -->|fallthrough| bb_005B1F86
  bb_005B1F86 -->|flow| bb_005B1F9E
```
