# WheapDeviceDriverGetPacketLength

- RVA: `0x0065EC04`–`0x0065EC1D` (길이 `25` bytes)
- VA: `0x000000014065EC04`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [WheaAddErrorSourceDeviceDriver](../../page/7D/WheaAddErrorSourceDeviceDriver_function_007D6E70.md) at `0x007D6F85`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065EC04  8D 04 D2                        lea eax, [rdx + rdx*8]
0065EC07  8D 04 C5 6C 00 00 00            lea eax, [rax*8 + 0x6c]
0065EC0E  03 C1                           add eax, ecx
0065EC10  8D 48 FF                        lea ecx, [rax - 1]
0065EC13  83 E1 07                        and ecx, 7
0065EC16  2B C1                           sub eax, ecx
0065EC18  83 C0 6F                        add eax, 0x6f
0065EC1B  C3                              ret
0065EC1C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheapDeviceDriverGetPacketLength(int a1, __int64 a2)
{
    __int64 result;

    result = (unsigned int)((a2 + a2 * 8 * 8 + 108) + (a1));
    a1 = (unsigned int)((result - 1) & (7));
    result = (unsigned int)((result) - (a1));
    result = (unsigned int)((result) + (111));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WheapDeviceDriverGetPacketLength(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (uint32_t)((Arg2 + Arg2 * 8 * 8 + 108) + (Arg1));
    Arg1 = (uint32_t)((result - 1) & (7));
    result = (uint32_t)((result) - (Arg1));
    result = (uint32_t)((result) + (111));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rdx*8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065EC04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065EC04[BB_0065EC04]
  bb_0065EC1C[BB_0065EC1C]
```
