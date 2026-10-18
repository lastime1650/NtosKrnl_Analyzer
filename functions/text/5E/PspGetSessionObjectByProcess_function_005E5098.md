# PspGetSessionObjectByProcess

- RVA: `0x005E5098`–`0x005E50BA` (길이 `34` bytes)
- VA: `0x00000001405E5098`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspEstablishDfssHierarchy](../../page/78/PspEstablishDfssHierarchy_function_00784EF0.md) at `0x00784F1F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E5098  48 8B 81 E8 02 00 00            mov rax, qword ptr [rcx + 0x2e8]
005E509F  48 85 C0                        test rax, rax
005E50A2  74 12                           je 0x1405e50b6
005E50A4  F7 81 FC 05 00 00 00 10 00 00   test dword ptr [rcx + 0x5fc], 0x1000
005E50AE  75 06                           jne 0x1405e50b6
005E50B0  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
005E50B4  C3                              ret
005E50B5  CC                              int3
005E50B6  33 C0                           xor eax, eax
005E50B8  C3                              ret
005E50B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspGetSessionObjectByProcess(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 744) == 0) goto loc_005E50B6;
    if (((*(unsigned int *)(a1 + 1532)) & (0x1000ULL)) != 0) goto loc_005E50B6;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 744) + 32);
loc_005E50B6:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspGetSessionObjectByProcess(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x2E8) == 0) goto loc_005E50B6;
    if (((*(uint32_t *)(arg1 + 0x5FC)) & (0x1000ULL)) != 0) goto loc_005E50B6;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x2E8) + 0x20);
loc_005E50B6:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2E8` | `64` | `R` |
| `Arg1` | `+ 0x5FC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E5098&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E5098[BB_005E5098]
  bb_005E50A4[BB_005E50A4]
  bb_005E50B0[BB_005E50B0]
  bb_005E50B5[BB_005E50B5]
  bb_005E50B6[BB_005E50B6]
  bb_005E50B9[BB_005E50B9]
  bb_005E5098 -->|branch| bb_005E50B6
  bb_005E5098 -->|fallthrough| bb_005E50A4
  bb_005E50A4 -->|branch| bb_005E50B6
  bb_005E50A4 -->|fallthrough| bb_005E50B0
  bb_005E50B5 -->|flow| bb_005E50B6
```
