# HsaLegacySetDeviceSvmCapabilities

- RVA: `0x005747B0`–`0x005747D6` (길이 `38` bytes)
- VA: `0x00000001405747B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005747B0  48 81 FA 00 00 01 00            cmp rdx, 0x10000
005747B7  73 16                           jae 0x1405747cf
005747B9  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
005747BD  48 C1 E8 05                     shr rax, 5
005747C1  48 3B D0                        cmp rdx, rax
005747C4  1B C0                           sbb eax, eax
005747C6  F7 D0                           not eax
005747C8  25 0D 00 00 C0                  and eax, 0xc000000d
005747CD  C3                              ret
005747CE  CC                              int3
005747CF  B8 0D 00 00 C0                  mov eax, 0xc000000d
005747D4  C3                              ret
005747D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HsaLegacySetDeviceSvmCapabilities(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a2 >= 0x10000ULL) goto loc_005747CF;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (5);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC000000DULL));
    return result;
loc_005747CF:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t HsaLegacySetDeviceSvmCapabilities(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 >= 0x10000ULL) goto loc_005747CF;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (5);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC000000DULL));
    return result;
loc_005747CF:
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005747B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005747B0[BB_005747B0]
  bb_005747B9[BB_005747B9]
  bb_005747CE[BB_005747CE]
  bb_005747CF[BB_005747CF]
  bb_005747D5[BB_005747D5]
  bb_005747B0 -->|branch| bb_005747CF
  bb_005747B0 -->|fallthrough| bb_005747B9
  bb_005747CE -->|flow| bb_005747CF
```
