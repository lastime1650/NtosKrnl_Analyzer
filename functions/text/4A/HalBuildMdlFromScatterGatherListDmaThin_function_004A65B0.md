# HalBuildMdlFromScatterGatherListDmaThin

- RVA: `0x004A65B0`–`0x004A65C3` (길이 `19` bytes)
- VA: `0x00000001404A65B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `19/19` bytes 표시
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
004A65B0  4D 85 C0                        test r8, r8
004A65B3  74 07                           je 0x1404a65bc
004A65B5  4D 89 01                        mov qword ptr [r9], r8
004A65B8  33 C0                           xor eax, eax
004A65BA  C3                              ret
004A65BB  CC                              int3
004A65BC  B8 0D 00 00 C0                  mov eax, 0xc000000d
004A65C1  C3                              ret
004A65C2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalBuildMdlFromScatterGatherListDmaThin(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    if (a3 == 0) goto loc_004A65BC;
    *(unsigned __int64 *)(a4) = a3;
    result = 0;
    return result;
loc_004A65BC:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t HalBuildMdlFromScatterGatherListDmaThin(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;

    if (Arg3 == 0) goto loc_004A65BC;
    *(uint64_t *)(arg4) = Arg3;
    result = 0;
    return result;
loc_004A65BC:
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A65B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A65B0[BB_004A65B0]
  bb_004A65B5[BB_004A65B5]
  bb_004A65BB[BB_004A65BB]
  bb_004A65BC[BB_004A65BC]
  bb_004A65C2[BB_004A65C2]
  bb_004A65B0 -->|branch| bb_004A65BC
  bb_004A65B0 -->|fallthrough| bb_004A65B5
  bb_004A65BB -->|flow| bb_004A65BC
```
