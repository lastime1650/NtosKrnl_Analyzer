# CarFindRuleOverrideEntryByLocalRuleId

- RVA: `0x006189D8`–`0x006189F4` (길이 `28` bytes)
- VA: `0x00000001406189D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CarDeregisterRuleOverride](CarDeregisterRuleOverride_function_00618910.md) at `0x00618930`
- [CarSetCustomIdInRuleOverride](CarSetCustomIdInRuleOverride_function_00619580.md) at `0x006195A8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006189D8  48 8B 01                        mov rax, qword ptr [rcx]
006189DB  48 3B C1                        cmp rax, rcx
006189DE  74 10                           je 0x1406189f0
006189E0  39 50 C0                        cmp dword ptr [rax - 0x40], edx
006189E3  74 05                           je 0x1406189ea
006189E5  48 8B 00                        mov rax, qword ptr [rax]
006189E8  EB F1                           jmp 0x1406189db
006189EA  48 83 C0 C0                     add rax, -0x40
006189EE  C3                              ret
006189EF  CC                              int3
006189F0  33 C0                           xor eax, eax
006189F2  C3                              ret
006189F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CarFindRuleOverrideEntryByLocalRuleId(__int64 a1, int a2)
{
    __int64 result;

loc_006189DB:
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_006189F0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) - 64)) == a2) goto loc_006189EA;
    goto loc_006189DB;
loc_006189EA:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) + (-64);
    return result;
loc_006189F0:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CarFindRuleOverrideEntryByLocalRuleId(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

loc_006189DB:
    if ((*(uint64_t *)(arg1)) == Arg1) goto loc_006189F0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) - 0x40)) == Arg2) goto loc_006189EA;
    goto loc_006189DB;
loc_006189EA:
    result = (*(uint64_t *)(*(uint64_t *)(arg1))) + (-64);
    return result;
loc_006189F0:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006189D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006189D8[BB_006189D8]
  bb_006189DB[BB_006189DB]
  bb_006189E0[BB_006189E0]
  bb_006189E5[BB_006189E5]
  bb_006189EA[BB_006189EA]
  bb_006189EF[BB_006189EF]
  bb_006189F0[BB_006189F0]
  bb_006189F3[BB_006189F3]
  bb_006189D8 -->|flow| bb_006189DB
  bb_006189DB -->|branch| bb_006189F0
  bb_006189DB -->|fallthrough| bb_006189E0
  bb_006189E0 -->|branch| bb_006189EA
  bb_006189E0 -->|fallthrough| bb_006189E5
  bb_006189E5 -->|branch| bb_006189DB
  bb_006189EF -->|flow| bb_006189F0
```
