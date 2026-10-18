# CarFindRuleOverrideEntryByGlobalRuleId

- RVA: `0x006189B4`–`0x006189D0` (길이 `28` bytes)
- VA: `0x00000001406189B4`
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
- [CarQueryReportActionForTriage](CarQueryReportActionForTriage_function_00618E10.md) at `0x00618EA5`
- [CarRegisterRuleOverride](CarRegisterRuleOverride_function_00619040.md) at `0x0061909A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006189B4  48 8B 01                        mov rax, qword ptr [rcx]
006189B7  48 3B C1                        cmp rax, rcx
006189BA  74 10                           je 0x1406189cc
006189BC  39 50 FC                        cmp dword ptr [rax - 4], edx
006189BF  74 05                           je 0x1406189c6
006189C1  48 8B 00                        mov rax, qword ptr [rax]
006189C4  EB F1                           jmp 0x1406189b7
006189C6  48 83 C0 C0                     add rax, -0x40
006189CA  C3                              ret
006189CB  CC                              int3
006189CC  33 C0                           xor eax, eax
006189CE  C3                              ret
006189CF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CarFindRuleOverrideEntryByGlobalRuleId(__int64 a1, int a2)
{
    __int64 result;

loc_006189B7:
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_006189CC;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) - 4)) == a2) goto loc_006189C6;
    goto loc_006189B7;
loc_006189C6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) + (-64);
    return result;
loc_006189CC:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CarFindRuleOverrideEntryByGlobalRuleId(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

loc_006189B7:
    if ((*(uint64_t *)(arg1)) == Arg1) goto loc_006189CC;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) - 0x4)) == Arg2) goto loc_006189C6;
    goto loc_006189B7;
loc_006189C6:
    result = (*(uint64_t *)(*(uint64_t *)(arg1))) + (-64);
    return result;
loc_006189CC:
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006189B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006189B4[BB_006189B4]
  bb_006189B7[BB_006189B7]
  bb_006189BC[BB_006189BC]
  bb_006189C1[BB_006189C1]
  bb_006189C6[BB_006189C6]
  bb_006189CB[BB_006189CB]
  bb_006189CC[BB_006189CC]
  bb_006189CF[BB_006189CF]
  bb_006189B4 -->|flow| bb_006189B7
  bb_006189B7 -->|branch| bb_006189CC
  bb_006189B7 -->|fallthrough| bb_006189BC
  bb_006189BC -->|branch| bb_006189C6
  bb_006189BC -->|fallthrough| bb_006189C1
  bb_006189C1 -->|branch| bb_006189B7
  bb_006189CB -->|flow| bb_006189CC
```
