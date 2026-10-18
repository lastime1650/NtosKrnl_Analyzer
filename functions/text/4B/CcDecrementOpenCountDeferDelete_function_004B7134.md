# CcDecrementOpenCountDeferDelete

- RVA: `0x004B7134`–`0x004B714B` (길이 `23` bytes)
- VA: `0x00000001404B7134`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD218`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E873B`
- [sub_006E8840](../6E/Unknown_function_006E8840.md) at `0x006E889A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7134  8B 41 04                        mov eax, dword ptr [rcx + 4]
004B7137  FF C8                           dec eax
004B7139  89 41 04                        mov dword ptr [rcx + 4], eax
004B713C  45 84 C0                        test r8b, r8b
004B713F  75 02                           jne 0x1404b7143
004B7141  C3                              ret
004B7142  CC                              int3
004B7143  FF 89 20 02 00 00               dec dword ptr [rcx + 0x220]
004B7149  C3                              ret
004B714A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcDecrementOpenCountDeferDelete(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) - 1);
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if (a3 != 0) goto loc_004B7143;
    return result;
loc_004B7143:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcDecrementOpenCountDeferDelete(void *Arg1, int64_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) - 1);
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if (Arg3 != 0) goto loc_004B7143;
    return result;
loc_004B7143:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x220` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7134&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7134[BB_004B7134]
  bb_004B7141[BB_004B7141]
  bb_004B7142[BB_004B7142]
  bb_004B7143[BB_004B7143]
  bb_004B714A[BB_004B714A]
  bb_004B7134 -->|branch| bb_004B7143
  bb_004B7134 -->|fallthrough| bb_004B7141
  bb_004B7142 -->|flow| bb_004B7143
```
