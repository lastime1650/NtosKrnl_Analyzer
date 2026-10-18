# IopPortGetNextAlias

- RVA: `0x0072F4CC`–`0x0072F4FA` (길이 `46` bytes)
- VA: `0x000000014072F4CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopPortAddAllocation](IopPortAddAllocation_function_0072F280.md) at `0x0072F339`
- [IopPortBacktrackAllocation](IopPortBacktrackAllocation_function_0072F360.md) at `0x0072F3A8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0072F4CC  F6 C1 04                        test cl, 4
0072F4CF  74 07                           je 0x14072f4d8
0072F4D1  B8 00 04 00 00                  mov eax, 0x400
0072F4D6  EB 0A                           jmp 0x14072f4e2
0072F4D8  F6 C1 08                        test cl, 8
0072F4DB  74 19                           je 0x14072f4f6
0072F4DD  B8 00 10 00 00                  mov eax, 0x1000
0072F4E2  48 8D 0C 10                     lea rcx, [rax + rdx]
0072F4E6  48 81 F9 FF FF 00 00            cmp rcx, 0xffff
0072F4ED  77 07                           ja 0x14072f4f6
0072F4EF  49 89 08                        mov qword ptr [r8], rcx
0072F4F2  B0 01                           mov al, 1
0072F4F4  C3                              ret
0072F4F5  CC                              int3
0072F4F6  32 C0                           xor al, al
0072F4F8  C3                              ret
0072F4F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopPortGetNextAlias(unsigned __int8 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (((a1) & (4)) == 0) goto loc_0072F4D8;
    goto loc_0072F4E2;
loc_0072F4D8:
    if (((a1) & (8)) == 0) goto loc_0072F4F6;
loc_0072F4E2:
    if (((unsigned int)(0x1000ULL) + a2 * 1) > 0xFFFFULL) goto loc_0072F4F6;
    *(unsigned __int64 *)(a3) = (unsigned int)(0x1000ULL) + a2 * 1;
    return 1;
loc_0072F4F6:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopPortGetNextAlias(uint8_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (((Arg1) & (4)) == 0) goto loc_0072F4D8;
    goto loc_0072F4E2;
loc_0072F4D8:
    if (((Arg1) & (8)) == 0) goto loc_0072F4F6;
loc_0072F4E2:
    if (((uint32_t)(0x1000ULL) + Arg2 * 1) > 0xFFFFULL) goto loc_0072F4F6;
    *(uint64_t *)(arg3) = (uint32_t)(0x1000ULL) + Arg2 * 1;
    return 1;
loc_0072F4F6:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072F4CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072F4CC[BB_0072F4CC]
  bb_0072F4D1[BB_0072F4D1]
  bb_0072F4D8[BB_0072F4D8]
  bb_0072F4DD[BB_0072F4DD]
  bb_0072F4E2[BB_0072F4E2]
  bb_0072F4EF[BB_0072F4EF]
  bb_0072F4F5[BB_0072F4F5]
  bb_0072F4F6[BB_0072F4F6]
  bb_0072F4F9[BB_0072F4F9]
  bb_0072F4CC -->|branch| bb_0072F4D8
  bb_0072F4CC -->|fallthrough| bb_0072F4D1
  bb_0072F4D1 -->|branch| bb_0072F4E2
  bb_0072F4D8 -->|branch| bb_0072F4F6
  bb_0072F4D8 -->|fallthrough| bb_0072F4DD
  bb_0072F4DD -->|flow| bb_0072F4E2
  bb_0072F4E2 -->|branch| bb_0072F4F6
  bb_0072F4E2 -->|fallthrough| bb_0072F4EF
  bb_0072F4F5 -->|flow| bb_0072F4F6
```
