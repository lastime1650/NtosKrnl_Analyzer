# RtlStateDurationDelta

- RVA: `0x0044F76C`–`0x0044F7A6` (길이 `58` bytes)
- VA: `0x000000014044F76C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `20`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopEtEnergyValuesDeltaCalculate](../../page/98/PopEtEnergyValuesDeltaCalculate_function_0098D8FC.md) at `0x0098D996`
- [PopEtEnergyValuesDeltaCalculate](../../page/98/PopEtEnergyValuesDeltaCalculate_function_0098D8FC.md) at `0x0098D9B9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F76C  48 83 21 00                     and qword ptr [rcx], 0
0044F770  4C 8B D1                        mov r10, rcx
0044F773  45 8B 48 04                     mov r9d, dword ptr [r8 + 4]
0044F777  41 BB FF FF FF 7F               mov r11d, 0x7fffffff
0044F77D  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
0044F780  41 8B C1                        mov eax, r9d
0044F783  41 23 C3                        and eax, r11d
0044F786  41 23 CB                        and ecx, r11d
0044F789  3B C1                           cmp eax, ecx
0044F78B  76 0A                           jbe 0x14044f797
0044F78D  44 2B C9                        sub r9d, ecx
0044F790  45 23 CB                        and r9d, r11d
0044F793  45 89 4A 04                     mov dword ptr [r10 + 4], r9d
0044F797  8B 0A                           mov ecx, dword ptr [rdx]
0044F799  41 8B 00                        mov eax, dword ptr [r8]
0044F79C  3B C8                           cmp ecx, eax
0044F79E  0F 46 C8                        cmovbe ecx, eax
0044F7A1  41 89 0A                        mov dword ptr [r10], ecx
0044F7A4  C3                              ret
0044F7A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlStateDurationDelta(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
    if (((unsigned int)(result)) >= = ((unsigned int)(a1))) {
        a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 4))) - ((unsigned int)(a1)));
        a4 = (unsigned int)((a4) & ((unsigned int)((unsigned int)(0x7FFFFFFFULL))));
        *(unsigned int *)(a1 + 4) = (unsigned int)(a4);
    }
    a1 = (unsigned int)(*(unsigned int *)(a2));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a3))); }
    *(unsigned int *)(a1) = (unsigned int)(a1);
    return (unsigned int)(*(unsigned int *)(a3));
}
```

## 5. (Beta) C Style

```c
int64_t RtlStateDurationDelta(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
    if (((uint32_t)(result)) >= = ((uint32_t)(Arg1))) {
        a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x4))) - ((uint32_t)(Arg1)));
        a4 = (uint32_t)((a4) & ((uint32_t)((uint32_t)(0x7FFFFFFFULL))));
        *(uint32_t *)(arg1 + 0x4) = (uint32_t)(a4);
    }
    Arg1 = (uint32_t)(*(uint32_t *)(arg2));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg3))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3))); }
    *(uint32_t *)(arg1) = (uint32_t)(Arg1);
    return (uint32_t)(*(uint32_t *)(arg3));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F76C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F76C[BB_0044F76C]
  bb_0044F78D[BB_0044F78D]
  bb_0044F797[BB_0044F797]
  bb_0044F7A5[BB_0044F7A5]
  bb_0044F76C -->|branch| bb_0044F797
  bb_0044F76C -->|fallthrough| bb_0044F78D
  bb_0044F78D -->|flow| bb_0044F797
```
