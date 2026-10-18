# KiCanThreadBeReadiedImmediately

- RVA: `0x0041B530`–`0x0041B546` (길이 `22` bytes)
- VA: `0x000000014041B530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021E3FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041B530  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
0041B533  0F BA E0 11                     bt eax, 0x11
0041B537  73 09                           jae 0x14041b542
0041B539  C1 E8 14                        shr eax, 0x14
0041B53C  F6 D0                           not al
0041B53E  24 01                           and al, 1
0041B540  C3                              ret
0041B541  CC                              int3
0041B542  32 C0                           xor al, al
0041B544  C3                              ret
0041B545  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCanThreadBeReadiedImmediately(__int64 a1)
{
    __int64 result;

    if (condition_is_above_or_equal) goto loc_0041B542;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) >> (20));
    result = (unsigned __int8)(~(result));
    result = (unsigned __int8)((result) & (1));
    return result;
loc_0041B542:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiCanThreadBeReadiedImmediately(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (condition_is_above_or_equal) goto loc_0041B542;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) >> (20));
    result = (uint8_t)(~(result));
    result = (uint8_t)((result) & (1));
    return result;
loc_0041B542:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041B530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041B530[BB_0041B530]
  bb_0041B539[BB_0041B539]
  bb_0041B541[BB_0041B541]
  bb_0041B542[BB_0041B542]
  bb_0041B545[BB_0041B545]
  bb_0041B530 -->|branch| bb_0041B542
  bb_0041B530 -->|fallthrough| bb_0041B539
  bb_0041B541 -->|flow| bb_0041B542
```
