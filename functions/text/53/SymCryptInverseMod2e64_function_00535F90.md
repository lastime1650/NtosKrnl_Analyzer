# SymCryptInverseMod2e64

- RVA: `0x00535F90`–`0x00535FEA` (길이 `90` bytes)
- VA: `0x0000000140535F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefIntToModulus](SymCryptFdefIntToModulus_function_00534144.md) at `0x005341AA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00535F90  8D 04 49                        lea eax, [rcx + rcx*2]
00535F93  8B D1                           mov edx, ecx
00535F95  44 8D 04 45 FA FF FF FF         lea r8d, [rax*2 - 6]
00535F9D  4C 8B D1                        mov r10, rcx
00535FA0  41 B9 02 00 00 00               mov r9d, 2
00535FA6  41 83 E0 08                     and r8d, 8
00535FAA  44 33 C1                        xor r8d, ecx
00535FAD  41 8B C1                        mov eax, r9d
00535FB0  41 0F AF D0                     imul edx, r8d
00535FB4  2B C2                           sub eax, edx
00535FB6  41 8B D1                        mov edx, r9d
00535FB9  44 0F AF C0                     imul r8d, eax
00535FBD  8B C1                           mov eax, ecx
00535FBF  41 8B C9                        mov ecx, r9d
00535FC2  41 0F AF C0                     imul eax, r8d
00535FC6  2B C8                           sub ecx, eax
00535FC8  44 0F AF C1                     imul r8d, ecx
00535FCC  41 8B CA                        mov ecx, r10d
00535FCF  41 0F AF C8                     imul ecx, r8d
00535FD3  2B D1                           sub edx, ecx
00535FD5  41 0F AF D0                     imul edx, r8d
00535FD9  8B CA                           mov ecx, edx
00535FDB  49 0F AF CA                     imul rcx, r10
00535FDF  8B C2                           mov eax, edx
00535FE1  4C 2B C9                        sub r9, rcx
00535FE4  49 0F AF C1                     imul rax, r9
00535FE8  C3                              ret
00535FE9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptInverseMod2e64(__int64 a1)
{
    __int64 result;

    a3 = (unsigned int)((a1 + a1 * 2 * 2 - 6) & (8));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) * ((unsigned int)(a3)));
    result = (unsigned int)((2) - ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) * ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) * ((unsigned int)(a3)));
    a1 = (unsigned int)((2) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) * ((unsigned int)(a1)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a1))) * ((unsigned int)(a3)));
    a2 = (unsigned int)((2) - ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) * ((unsigned int)(a3)));
    a1 = ((unsigned int)((unsigned int)(a2))) * (a1);
    a4 = (2) - (a1);
    result = ((unsigned int)((unsigned int)(a2))) * (a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptInverseMod2e64(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a3 = (uint32_t)((Arg1 + Arg1 * 2 * 2 - 6) & (8));
    a3 = (uint32_t)((a3) ^ ((uint32_t)(Arg1)));
    a2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) * ((uint32_t)(a3)));
    result = (uint32_t)((2) - ((uint32_t)(a2)));
    a3 = (uint32_t)((a3) * ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) * ((uint32_t)(a3)));
    Arg1 = (uint32_t)((2) - ((uint32_t)(result)));
    a3 = (uint32_t)((a3) * ((uint32_t)(Arg1)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) * ((uint32_t)(a3)));
    a2 = (uint32_t)((2) - ((uint32_t)(Arg1)));
    a2 = (uint32_t)((a2) * ((uint32_t)(a3)));
    Arg1 = ((uint32_t)((uint32_t)(a2))) * (Arg1);
    a4 = (2) - (Arg1);
    result = ((uint32_t)((uint32_t)(a2))) * (a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00535F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00535F90[BB_00535F90]
  bb_00535FE9[BB_00535FE9]
```
