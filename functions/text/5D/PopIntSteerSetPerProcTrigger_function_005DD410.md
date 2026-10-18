# PopIntSteerSetPerProcTrigger

- RVA: `0x005DD410`–`0x005DD429` (길이 `25` bytes)
- VA: `0x00000001405DD410`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005DD41F` → RVA `0x00E0C470` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD410  41 83 F8 04                     cmp r8d, 4
005DD414  74 07                           je 0x1405dd41d
005DD416  B8 0D 00 00 C0                  mov eax, 0xc000000d
005DD41B  C3                              ret
005DD41C  CC                              int3
005DD41D  8B 02                           mov eax, dword ptr [rdx]
005DD41F  89 05 4B F0 82 00               mov dword ptr [rip + 0x82f04b], eax
005DD425  33 C0                           xor eax, eax
005DD427  C3                              ret
005DD428  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIntSteerSetPerProcTrigger(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    if (a3 == 4) goto loc_005DD41D;
    return (unsigned int)(0xC000000DULL);
loc_005DD41D:
    *(unsigned int *)(v_rip + 8581195) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopIntSteerSetPerProcTrigger(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg3 == 4) goto loc_005DD41D;
    return (uint32_t)(0xC000000DULL);
loc_005DD41D:
    *(uint32_t *)(v_rip + 0x82F04B) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD410[BB_005DD410]
  bb_005DD416[BB_005DD416]
  bb_005DD41C[BB_005DD41C]
  bb_005DD41D[BB_005DD41D]
  bb_005DD428[BB_005DD428]
  bb_005DD410 -->|branch| bb_005DD41D
  bb_005DD410 -->|fallthrough| bb_005DD416
  bb_005DD41C -->|flow| bb_005DD41D
```
