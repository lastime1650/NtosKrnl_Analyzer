# HalpIvtReserveDomainIds

- RVA: `0x00579CD8`–`0x00579D1B` (길이 `67` bytes)
- VA: `0x0000000140579CD8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `23`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpIvtLegacyProcessDrhdEntry](HalpIvtLegacyProcessDrhdEntry_function_00578C58.md) at `0x005791EA`
- [HalpIvtProcessDrhdEntry](HalpIvtProcessDrhdEntry_function_005794B4.md) at `0x00579AC8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00579CD8  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
00579CDD  4C 8B D9                        mov r11, rcx
00579CE0  8D 0C 55 04 00 00 00            lea ecx, [rdx*2 + 4]
00579CE7  B8 01 00 00 00                  mov eax, 1
00579CEC  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00579CF1  D3 E0                           shl eax, cl
00579CF3  89 02                           mov dword ptr [rdx], eax
00579CF5  4D 85 D2                        test r10, r10
00579CF8  74 07                           je 0x140579d01
00579CFA  FF C8                           dec eax
00579CFC  89 02                           mov dword ptr [rdx], eax
00579CFE  41 89 02                        mov dword ptr [r10], eax
00579D01  FF 0A                           dec dword ptr [rdx]
00579D03  8B 0A                           mov ecx, dword ptr [rdx]
00579D05  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00579D0A  89 08                           mov dword ptr [rax], ecx
00579D0C  41 8B 03                        mov eax, dword ptr [r11]
00579D0F  2B C8                           sub ecx, eax
00579D11  89 0A                           mov dword ptr [rdx], ecx
00579D13  41 89 08                        mov dword ptr [r8], ecx
00579D16  41 89 01                        mov dword ptr [r9], eax
00579D19  C3                              ret
00579D1A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIvtReserveDomainIds(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;

    result = (unsigned int)((1) << ((unsigned __int8)(a2 * 2 + 4)));
    *(unsigned int *)(a7) = (unsigned int)(result);
    if (a6 != 0) {
        result = (unsigned int)((result) - 1);
        *(unsigned int *)(a7) = (unsigned int)(result);
        *(unsigned int *)(a6) = (unsigned int)(result);
    }
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(a7)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a7))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    *(unsigned int *)(a7) = (unsigned int)(a1);
    *(unsigned int *)(a3) = (unsigned int)(a1);
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    return (unsigned int)(*(unsigned int *)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t HalpIvtReserveDomainIds(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4, void *Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;

    result = (uint32_t)((1) << ((uint8_t)(Arg2 * 2 + 4)));
    *(uint32_t *)(arg7) = (uint32_t)(result);
    if (Arg6 != 0) {
        result = (uint32_t)((result) - 1);
        *(uint32_t *)(arg7) = (uint32_t)(result);
        *(uint32_t *)(Arg6) = (uint32_t)(result);
    }
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(arg7)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg7))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))));
    *(uint32_t *)(arg7) = (uint32_t)(Arg1);
    *(uint32_t *)(arg3) = (uint32_t)(Arg1);
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    return (uint32_t)(*(uint32_t *)(arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `R/W` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00579CD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00579CD8[BB_00579CD8]
  bb_00579CFA[BB_00579CFA]
  bb_00579D01[BB_00579D01]
  bb_00579D1A[BB_00579D1A]
  bb_00579CD8 -->|branch| bb_00579D01
  bb_00579CD8 -->|fallthrough| bb_00579CFA
  bb_00579CFA -->|flow| bb_00579D01
```
