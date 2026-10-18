# RtlUIntAdd

- RVA: `0x0045D360`–`0x0045D377` (길이 `23` bytes)
- VA: `0x000000014045D360`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096AB57`
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096AB7C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045D360  8D 04 11                        lea eax, [rcx + rdx]
0045D363  83 CA FF                        or edx, 0xffffffff
0045D366  3B C1                           cmp eax, ecx
0045D368  0F 43 D0                        cmovae edx, eax
0045D36B  1B C0                           sbb eax, eax
0045D36D  25 95 00 00 C0                  and eax, 0xc0000095
0045D372  41 89 10                        mov dword ptr [r8], edx
0045D375  C3                              ret
0045D376  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlUIntAdd(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (((unsigned int)(a1 + a2 * 1)) >= ((unsigned int)(a1))) { a2 = (unsigned int)(a1 + a2 * 1); }
    result = (unsigned int)((a1 + a2 * 1) & (0xC0000095ULL));
    *(unsigned int *)(a3) = (unsigned int)(a2);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlUIntAdd(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (((uint32_t)(Arg1 + Arg2 * 1)) >= ((uint32_t)(Arg1))) { Arg2 = (uint32_t)(Arg1 + Arg2 * 1); }
    result = (uint32_t)((Arg1 + Arg2 * 1) & (0xC0000095ULL));
    *(uint32_t *)(arg3) = (uint32_t)(Arg2);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdx*1` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045D360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045D360[BB_0045D360]
  bb_0045D376[BB_0045D376]
```
