# IoSetIrpExtraCreateParameter

- RVA: `0x009EB900`–`0x009EB928` (길이 `40` bytes)
- VA: `0x00000001409EB900`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `16`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopSymlinkAllocateAndAddECP](../8A/IopSymlinkAllocateAndAddECP_function_008A1E20.md) at `0x008A1EEC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009EB900  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
009EB903  84 C0                           test al, al
009EB905  79 13                           jns 0x1409eb91a
009EB907  48 83 79 70 00                  cmp qword ptr [rcx + 0x70], 0
009EB90C  75 13                           jne 0x1409eb921
009EB90E  48 89 51 70                     mov qword ptr [rcx + 0x70], rdx
009EB912  83 4A 04 08                     or dword ptr [rdx + 4], 8
009EB916  33 C0                           xor eax, eax
009EB918  C3                              ret
009EB919  CC                              int3
009EB91A  B8 EF 00 00 C0                  mov eax, 0xc00000ef
009EB91F  C3                              ret
009EB920  CC                              int3
009EB921  B8 F0 00 00 C0                  mov eax, 0xc00000f0
009EB926  C3                              ret
009EB927  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetIrpExtraCreateParameter(__int64 a1, __int64 a2)
{
    __int64 result;

    if (!sign_flag) goto loc_009EB91A;
    if ((*(unsigned __int64 *)(a1 + 112)) != 0) goto loc_009EB921;
    *(unsigned __int64 *)(a1 + 112) = a2;
    result = 0;
    return result;
loc_009EB91A:
    return (unsigned int)(0xC00000EFULL);
loc_009EB921:
    return (unsigned int)(0xC00000F0ULL);
}
```

## 5. (Beta) C Style

```c
int64_t IoSetIrpExtraCreateParameter(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (!sign_flag) goto loc_009EB91A;
    if ((*(uint64_t *)(arg1 + 0x70)) != 0) goto loc_009EB921;
    *(void **)(arg1 + 0x70) = Arg2;
    result = 0;
    return result;
loc_009EB91A:
    return (uint32_t)(0xC00000EFULL);
loc_009EB921:
    return (uint32_t)(0xC00000F0ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `W` |
| `Arg2` | `+ 0x4` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009EB900&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009EB900[BB_009EB900]
  bb_009EB907[BB_009EB907]
  bb_009EB90E[BB_009EB90E]
  bb_009EB919[BB_009EB919]
  bb_009EB91A[BB_009EB91A]
  bb_009EB920[BB_009EB920]
  bb_009EB921[BB_009EB921]
  bb_009EB927[BB_009EB927]
  bb_009EB900 -->|branch| bb_009EB91A
  bb_009EB900 -->|fallthrough| bb_009EB907
  bb_009EB907 -->|branch| bb_009EB921
  bb_009EB907 -->|fallthrough| bb_009EB90E
  bb_009EB919 -->|flow| bb_009EB91A
  bb_009EB920 -->|flow| bb_009EB921
```
