# HalpMceRecoveryMemoryError

- RVA: `0x00556000`–`0x0055601C` (길이 `28` bytes)
- VA: `0x0000000140556000`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0055600A` → [HalpMceRecoveryMemoryErrorIntel](HalpMceRecoveryMemoryErrorIntel_function_00556138.md) (function, `0x00556138`)
- `0x00556011` → [HalpMceRecoveryMemoryErrorAmd](HalpMceRecoveryMemoryErrorAmd_function_00556024.md) (function, `0x00556024`)

### Direct callers
- [HalpMceRecoveryRequired](HalpMceRecoveryRequired_function_0055637C.md) at `0x005563C1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00556000  48 83 EC 28                     sub rsp, 0x28
00556004  83 79 04 01                     cmp dword ptr [rcx + 4], 1
00556008  75 07                           jne 0x140556011
0055600A  E8 29 01 00 00                  call 0x140556138
0055600F  EB 05                           jmp 0x140556016
00556011  E8 0E 00 00 00                  call 0x140556024
00556016  48 83 C4 28                     add rsp, 0x28
0055601A  C3                              ret
0055601B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMceRecoveryMemoryError(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(a1 + 4)) != 1) goto loc_00556011;
    result = HalpMceRecoveryMemoryErrorIntel(a1, a2, a3, a4);
    goto loc_00556016;
loc_00556011:
    result = HalpMceRecoveryMemoryErrorAmd(a1, a2, a3, a4);
loc_00556016:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMceRecoveryMemoryError(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(arg1 + 0x4)) != 1) goto loc_00556011;
    result = HalpMceRecoveryMemoryErrorIntel(Arg1, a2, a3, a4);
    goto loc_00556016;
loc_00556011:
    result = HalpMceRecoveryMemoryErrorAmd(Arg1, a2, a3, a4);
loc_00556016:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00556000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00556000[BB_00556000]
  bb_0055600A[BB_0055600A]
  bb_00556011[BB_00556011]
  bb_00556016[BB_00556016]
  bb_0055601B[BB_0055601B]
  bb_00556000 -->|branch| bb_00556011
  bb_00556000 -->|fallthrough| bb_0055600A
  bb_0055600A -->|branch| bb_00556016
  bb_00556011 -->|flow| bb_00556016
```
