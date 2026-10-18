# PopIntSteerSetTimeUnparkTrigger

- RVA: `0x005DD430`–`0x005DD44A` (길이 `26` bytes)
- VA: `0x00000001405DD430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
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
- `0x005DD43F` → RVA `0x00E0C468` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD430  41 83 F8 04                     cmp r8d, 4
005DD434  74 07                           je 0x1405dd43d
005DD436  B8 0D 00 00 C0                  mov eax, 0xc000000d
005DD43B  C3                              ret
005DD43C  CC                              int3
005DD43D  8B 02                           mov eax, dword ptr [rdx]
005DD43F  48 89 05 22 F0 82 00            mov qword ptr [rip + 0x82f022], rax
005DD446  33 C0                           xor eax, eax
005DD448  C3                              ret
005DD449  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIntSteerSetTimeUnparkTrigger(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    if (a3 == 4) goto loc_005DD43D;
    return (unsigned int)(0xC000000DULL);
loc_005DD43D:
    *(unsigned __int64 *)(v_rip + 8581154) = (unsigned int)(*(unsigned int *)(a2));
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopIntSteerSetTimeUnparkTrigger(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg3 == 4) goto loc_005DD43D;
    return (uint32_t)(0xC000000DULL);
loc_005DD43D:
    *(uint64_t *)(v_rip + 0x82F022) = (uint32_t)(*(uint32_t *)(arg2));
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD430[BB_005DD430]
  bb_005DD436[BB_005DD436]
  bb_005DD43C[BB_005DD43C]
  bb_005DD43D[BB_005DD43D]
  bb_005DD449[BB_005DD449]
  bb_005DD430 -->|branch| bb_005DD43D
  bb_005DD430 -->|fallthrough| bb_005DD436
  bb_005DD43C -->|flow| bb_005DD43D
```
