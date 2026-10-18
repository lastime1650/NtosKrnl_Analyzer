# KiGetCurrentScheduledThreadProcessor

- RVA: `0x00352B20`–`0x00352B2F` (길이 `15` bytes)
- VA: `0x0000000140352B20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiParkCurrentProcessor](KiParkCurrentProcessor_function_003533A4.md) at `0x00353565`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00352B20  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00352B24  48 85 C0                        test rax, rax
00352B27  75 04                           jne 0x140352b2d
00352B29  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00352B2D  C3                              ret
00352B2E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiGetCurrentScheduledThreadProcessor(__int64 a1)
{
    __int64 result;

    result = *(unsigned __int64 *)(a1 + 16);
    if (*(unsigned __int64 *)(a1 + 16) == 0) {
        result = *(unsigned __int64 *)(a1 + 8);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiGetCurrentScheduledThreadProcessor(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = *(uint64_t *)(arg1 + 0x10);
    if (*(uint64_t *)(arg1 + 0x10) == 0) {
        result = *(uint64_t *)(arg1 + 0x8);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00352B20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00352B20[BB_00352B20]
  bb_00352B29[BB_00352B29]
  bb_00352B2D[BB_00352B2D]
  bb_00352B2E[BB_00352B2E]
  bb_00352B20 -->|branch| bb_00352B2D
  bb_00352B20 -->|fallthrough| bb_00352B29
  bb_00352B29 -->|flow| bb_00352B2D
```
