# RtlLongLongAdd

- RVA: `0x005D5128`–`0x005D5164` (길이 `60` bytes)
- VA: `0x00000001405D5128`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `18`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlParseLeapSecondData](../../page/83/RtlParseLeapSecondData_function_0083D0A4.md) at `0x0083D14C`
- [PopReadPagesFromHiberFile](../../page/AC/PopReadPagesFromHiberFile_function_00AC8F78.md) at `0x00AC9079`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D5128  4C 8D 14 11                     lea r10, [rcx + rdx]
005D512C  45 33 C9                        xor r9d, r9d
005D512F  48 C1 E9 3F                     shr rcx, 0x3f
005D5133  48 C1 EA 3F                     shr rdx, 0x3f
005D5137  3B CA                           cmp ecx, edx
005D5139  75 21                           jne 0x1405d515c
005D513B  41 8B C1                        mov eax, r9d
005D513E  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
005D5148  4C 3B D2                        cmp r10, rdx
005D514B  0F 97 C0                        seta al
005D514E  3B C8                           cmp ecx, eax
005D5150  74 0A                           je 0x1405d515c
005D5152  41 B9 95 00 00 C0               mov r9d, 0xc0000095
005D5158  49 83 CA FF                     or r10, 0xffffffffffffffff
005D515C  4D 89 10                        mov qword ptr [r8], r10
005D515F  41 8B C1                        mov eax, r9d
005D5162  C3                              ret
005D5163  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlLongLongAdd(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;

    a4 = 0;
    a1 = (a1) >> (63);
    a2 = (a2) >> (63);
    if (((unsigned int)(a1)) != ((unsigned int)(a2))) goto loc_005D515C;
    result = ((a1 + a2 * 1) > a2) ? 1 : 0;
    v_r10 = a1 + a2 * 1;
    if (((unsigned int)(a1)) != ((unsigned int)(result))) {
        a4 = 0xC0000095ULL;
        v_r10 = (a1 + a2 * 1) | (-1);
    }
    *(unsigned __int64 *)(a3) = v_r10;
    return (unsigned int)(a4);
}
```

## 5. (Beta) C Style

```c
int64_t RtlLongLongAdd(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;

    Arg4 = 0;
    Arg1 = (Arg1) >> (63);
    Arg2 = (Arg2) >> (63);
    if (((uint32_t)(Arg1)) != ((uint32_t)(Arg2))) goto loc_005D515C;
    result = ((Arg1 + Arg2 * 1) > Arg2) ? 1 : 0;
    local_r10 = Arg1 + Arg2 * 1;
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) {
        Arg4 = 0xC0000095ULL;
        local_r10 = (Arg1 + Arg2 * 1) | (-1);
    }
    *(uint64_t *)(arg3) = local_r10;
    return (uint32_t)(Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D5128&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D5128[BB_005D5128]
  bb_005D513B[BB_005D513B]
  bb_005D5152[BB_005D5152]
  bb_005D515C[BB_005D515C]
  bb_005D5163[BB_005D5163]
  bb_005D5128 -->|branch| bb_005D515C
  bb_005D5128 -->|fallthrough| bb_005D513B
  bb_005D513B -->|branch| bb_005D515C
  bb_005D513B -->|fallthrough| bb_005D5152
  bb_005D5152 -->|flow| bb_005D515C
```
