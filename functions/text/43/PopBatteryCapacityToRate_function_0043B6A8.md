# PopBatteryCapacityToRate

- RVA: `0x0043B6A8`–`0x0043B6C6` (길이 `30` bytes)
- VA: `0x000000014043B6A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopCalculateCsSummary](PopCalculateCsSummary_function_0043A1B0.md) at `0x0043A242`
- [PopDripsWatchdogUpdateMetrics](../../page/76/PopDripsWatchdogUpdateMetrics_function_0076C830.md) at `0x0076C8F5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043B6A8  4C 8B C2                        mov r8, rdx
0043B6AB  48 85 D2                        test rdx, rdx
0043B6AE  75 04                           jne 0x14043b6b4
0043B6B0  33 C0                           xor eax, eax
0043B6B2  C3                              ret
0043B6B3  CC                              int3
0043B6B4  8B C1                           mov eax, ecx
0043B6B6  33 D2                           xor edx, edx
0043B6B8  B9 00 A4 93 D6                  mov ecx, 0xd693a400
0043B6BD  48 0F AF C1                     imul rax, rcx
0043B6C1  49 F7 F0                        div r8
0043B6C4  C3                              ret
0043B6C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopBatteryCapacityToRate(int a1, __int64 a2)
{
    __int64 result;

    if (a2 != 0) goto loc_0043B6B4;
    result = 0;
    return result;
loc_0043B6B4:
    a2 = 0;
    result = ((unsigned int)(a1)) * ((unsigned int)(0xD693A400ULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopBatteryCapacityToRate(int32_t Arg1, int64_t Arg2)
{
    int64_t result;

    if (Arg2 != 0) goto loc_0043B6B4;
    result = 0;
    return result;
loc_0043B6B4:
    Arg2 = 0;
    result = ((uint32_t)(Arg1)) * ((uint32_t)(0xD693A400ULL));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043B6A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043B6A8[BB_0043B6A8]
  bb_0043B6B0[BB_0043B6B0]
  bb_0043B6B3[BB_0043B6B3]
  bb_0043B6B4[BB_0043B6B4]
  bb_0043B6C5[BB_0043B6C5]
  bb_0043B6A8 -->|branch| bb_0043B6B4
  bb_0043B6A8 -->|fallthrough| bb_0043B6B0
  bb_0043B6B3 -->|flow| bb_0043B6B4
```
