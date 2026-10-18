# IsNeutralLanguageItem

- RVA: `0x004CCF90`–`0x004CCFA8` (길이 `24` bytes)
- VA: `0x00000001404CCF90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DownLevelLangIDToLanguageName](../4B/DownLevelLangIDToLanguageName_function_004BBAA8.md) at `0x004BBB49`
- [DownLevelLanguageNameToLangID](DownLevelLanguageNameToLangID_function_004C3748.md) at `0x004C37D0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CCF90  83 79 0C 7C                     cmp dword ptr [rcx + 0xc], 0x7c
004CCF94  74 04                           je 0x1404ccf9a
004CCF96  33 C0                           xor eax, eax
004CCF98  C3                              ret
004CCF99  CC                              int3
004CCF9A  66 83 79 08 7F                  cmp word ptr [rcx + 8], 0x7f
004CCF9F  74 F5                           je 0x1404ccf96
004CCFA1  B8 01 00 00 00                  mov eax, 1
004CCFA6  C3                              ret
004CCFA7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IsNeutralLanguageItem(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 12)) == 124) goto loc_004CCF9A;
loc_004CCF96:
    result = 0;
    return result;
loc_004CCF9A:
    if ((*(unsigned __int16 *)(a1 + 8)) == 127) goto loc_004CCF96;
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t IsNeutralLanguageItem(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0xC)) == 124) goto loc_004CCF9A;
loc_004CCF96:
    result = 0;
    return result;
loc_004CCF9A:
    if ((*(uint16_t *)(arg1 + 0x8)) == 127) goto loc_004CCF96;
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `16` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CCF90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CCF90[BB_004CCF90]
  bb_004CCF96[BB_004CCF96]
  bb_004CCF99[BB_004CCF99]
  bb_004CCF9A[BB_004CCF9A]
  bb_004CCFA1[BB_004CCFA1]
  bb_004CCFA7[BB_004CCFA7]
  bb_004CCF90 -->|branch| bb_004CCF9A
  bb_004CCF90 -->|fallthrough| bb_004CCF96
  bb_004CCF99 -->|flow| bb_004CCF9A
  bb_004CCF9A -->|branch| bb_004CCF96
  bb_004CCF9A -->|fallthrough| bb_004CCFA1
```
