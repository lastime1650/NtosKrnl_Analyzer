# RtlSetBit

- RVA: `0x004466C0`–`0x004466DA` (길이 `26` bytes)
- VA: `0x00000001404466C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `26/26` bytes 표시
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
004466C0  44 8B C2                        mov r8d, edx
004466C3  83 E2 07                        and edx, 7
004466C6  49 C1 E8 03                     shr r8, 3
004466CA  4C 03 41 08                     add r8, qword ptr [rcx + 8]
004466CE  41 0F BE 00                     movsx eax, byte ptr [r8]
004466D2  0F AB D0                        bts eax, edx
004466D5  41 88 00                        mov byte ptr [r8], al
004466D8  C3                              ret
004466D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSetBit(__int64 a1, int a2)
{
    a2 = (unsigned int)((a2) & (7));
    a3 = ((unsigned int)(a2)) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a1 + 8));
    *(unsigned __int8 *)(a3) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a3)));
    return (__int8)(*(unsigned __int8 *)(a3));
}
```

## 5. (Beta) C Style

```c
int64_t RtlSetBit(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg2 = (uint32_t)((Arg2) & (7));
    a3 = ((uint32_t)(Arg2)) >> (3);
    a3 = (a3) + (*(uint64_t *)(arg1 + 0x8));
    *(uint8_t *)(a3) = (uint8_t)((int8_t)(*(uint8_t *)(a3)));
    return (int8_t)(*(uint8_t *)(a3));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004466C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004466C0[BB_004466C0]
  bb_004466D9[BB_004466D9]
```
