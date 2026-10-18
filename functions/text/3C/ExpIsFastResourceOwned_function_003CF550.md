# ExpIsFastResourceOwned

- RVA: `0x003CF550`–`0x003CF567` (길이 `23` bytes)
- VA: `0x00000001403CF550`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExReinitializeFastResource](ExReinitializeFastResource_function_003CF400.md) at `0x003CF44C`
- [ExDeleteFastResource](ExDeleteFastResource_function_003CF4C0.md) at `0x003CF50B`
- [DifExDeleteFastResourceWrapper](../61/DifExDeleteFastResourceWrapper_function_0061F420.md) at `0x0061F52D`
- [ExpFastResourceLegacyIsAcquiredShared](../65/ExpFastResourceLegacyIsAcquiredShared_function_00658C84.md) at `0x00658CA2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003CF550  48 8B 01                        mov rax, qword ptr [rcx]
003CF553  A8 01                           test al, 1
003CF555  75 0C                           jne 0x1403cf563
003CF557  48 A9 FC FF FF FF               test rax, -4
003CF55D  75 04                           jne 0x1403cf563
003CF55F  32 C0                           xor al, al
003CF561  C3                              ret
003CF562  CC                              int3
003CF563  B0 01                           mov al, 1
003CF565  C3                              ret
003CF566  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpIsFastResourceOwned(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) != 0) goto loc_003CF563;
    if (((*(unsigned __int64 *)(a1)) & (-4)) != 0) goto loc_003CF563;
    result = 0;
    return result;
loc_003CF563:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t ExpIsFastResourceOwned(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) != 0) goto loc_003CF563;
    if (((*(uint64_t *)(arg1)) & (-4)) != 0) goto loc_003CF563;
    result = 0;
    return result;
loc_003CF563:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CF550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003CF550[BB_003CF550]
  bb_003CF557[BB_003CF557]
  bb_003CF55F[BB_003CF55F]
  bb_003CF562[BB_003CF562]
  bb_003CF563[BB_003CF563]
  bb_003CF566[BB_003CF566]
  bb_003CF550 -->|branch| bb_003CF563
  bb_003CF550 -->|fallthrough| bb_003CF557
  bb_003CF557 -->|branch| bb_003CF563
  bb_003CF557 -->|fallthrough| bb_003CF55F
  bb_003CF562 -->|flow| bb_003CF563
```
