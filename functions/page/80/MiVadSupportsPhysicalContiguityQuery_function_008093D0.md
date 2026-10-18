# MiVadSupportsPhysicalContiguityQuery

- RVA: `0x008093D0`–`0x008093EB` (길이 `27` bytes)
- VA: `0x00000001408093D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiProcessVaContiguityInformation](../../text/69/MiProcessVaContiguityInformation_function_006939C0.md) at `0x00693B6D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008093D0  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
008093D3  A8 70                           test al, 0x70
008093D5  0F 94 C1                        sete cl
008093D8  0F BA E0 15                     bt eax, 0x15
008093DC  0F 92 C0                        setb al
008093DF  84 C8                           test al, cl
008093E1  B8 00 00 00 00                  mov eax, 0
008093E6  0F 95 C0                        setne al
008093E9  C3                              ret
008093EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiVadSupportsPhysicalContiguityQuery(__int64 a1)
{
    __int64 result;

    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (112)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    result = ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiVadSupportsPhysicalContiguityQuery(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (112)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    result = ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008093D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008093D0[BB_008093D0]
  bb_008093EA[BB_008093EA]
```
