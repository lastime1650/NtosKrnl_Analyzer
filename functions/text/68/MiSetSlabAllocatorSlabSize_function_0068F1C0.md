# MiSetSlabAllocatorSlabSize

- RVA: `0x0068F1C0`–`0x0068F1DF` (길이 `31` bytes)
- VA: `0x000000014068F1C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068F1C0  8B 82 88 00 00 00               mov eax, dword ptr [rdx + 0x88]
0068F1C6  41 C1 E0 04                     shl r8d, 4
0068F1CA  44 33 C0                        xor r8d, eax
0068F1CD  41 83 E0 30                     and r8d, 0x30
0068F1D1  44 33 C0                        xor r8d, eax
0068F1D4  33 C0                           xor eax, eax
0068F1D6  44 89 82 88 00 00 00            mov dword ptr [rdx + 0x88], r8d
0068F1DD  C3                              ret
0068F1DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetSlabAllocatorSlabSize(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 136)))));
    a3 = (unsigned int)((a3) & (48));
    a3 = (unsigned int)((a3) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 136)))));
    result = 0;
    *(unsigned int *)(a2 + 136) = a3;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetSlabAllocatorSlabSize(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    Arg3 = (uint32_t)((Arg3) << (4));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x88)))));
    Arg3 = (uint32_t)((Arg3) & (48));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x88)))));
    result = 0;
    *(uint32_t *)(arg2 + 0x88) = Arg3;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x88` | `32` | `R` |
| `Arg2` | `+ 0x88` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068F1C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0068F1C0[BB_0068F1C0]
  bb_0068F1DE[BB_0068F1DE]
```
