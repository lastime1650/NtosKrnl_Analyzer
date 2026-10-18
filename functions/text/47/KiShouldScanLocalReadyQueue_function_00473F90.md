# KiShouldScanLocalReadyQueue

- RVA: `0x00473F90`–`0x00473FAA` (길이 `26` bytes)
- VA: `0x0000000140473F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiNormalPriorityReadyScan](../21/KiNormalPriorityReadyScan_function_0021B400.md) at `0x0021B444`
- [KiUpdateRunTime](../39/KiUpdateRunTime_function_0039BB70.md) at `0x0039C070`

### Static image references
- `0x00473F90` → RVA `0x00FC52E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00473F90  83 3D 49 13 B5 00 00            cmp dword ptr [rip + 0xb51349], 0
00473F97  74 06                           je 0x140473f9f
00473F99  F6 41 23 20                     test byte ptr [rcx + 0x23], 0x20
00473F9D  75 07                           jne 0x140473fa6
00473F9F  B8 01 00 00 00                  mov eax, 1
00473FA4  C3                              ret
00473FA5  CC                              int3
00473FA6  33 C0                           xor eax, eax
00473FA8  C3                              ret
00473FA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiShouldScanLocalReadyQueue(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(v_rip + 11866953)) == 0) goto loc_00473F9F;
    if (((*(unsigned __int8 *)(a1 + 35)) & (32)) != 0) goto loc_00473FA6;
loc_00473F9F:
    return 1;
loc_00473FA6:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiShouldScanLocalReadyQueue(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(v_rip + 0xB51349)) == 0) goto loc_00473F9F;
    if (((*(uint8_t *)(arg1 + 0x23)) & (32)) != 0) goto loc_00473FA6;
loc_00473F9F:
    return 1;
loc_00473FA6:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x23` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00473F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00473F90[BB_00473F90]
  bb_00473F99[BB_00473F99]
  bb_00473F9F[BB_00473F9F]
  bb_00473FA5[BB_00473FA5]
  bb_00473FA6[BB_00473FA6]
  bb_00473FA9[BB_00473FA9]
  bb_00473F90 -->|branch| bb_00473F9F
  bb_00473F90 -->|fallthrough| bb_00473F99
  bb_00473F99 -->|branch| bb_00473FA6
  bb_00473F99 -->|fallthrough| bb_00473F9F
  bb_00473FA5 -->|flow| bb_00473FA6
```
