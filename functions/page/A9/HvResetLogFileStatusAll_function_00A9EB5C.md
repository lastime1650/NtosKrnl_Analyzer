# HvResetLogFileStatusAll

- RVA: `0x00A9EB5C`–`0x00A9EB78` (길이 `28` bytes)
- VA: `0x0000000140A9EB5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B4646`
- [HvpPerformLogFileRecovery](../9B/HvpPerformLogFileRecovery_function_009B7994.md) at `0x009B7DBA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9EB5C  83 B9 A8 00 00 00 01            cmp dword ptr [rcx + 0xa8], 1
00A9EB63  74 0A                           je 0x140a9eb6f
00A9EB65  66 83 A1 C0 00 00 00 00         and word ptr [rcx + 0xc0], 0
00A9EB6D  C3                              ret
00A9EB6E  CC                              int3
00A9EB6F  C6 81 C0 00 00 00 00            mov byte ptr [rcx + 0xc0], 0
00A9EB76  C3                              ret
00A9EB77  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall HvResetLogFileStatusAll(__int64 a1)
{
    if ((*(unsigned int *)(a1 + 168)) == 1) goto loc_00A9EB6F;
    return;
loc_00A9EB6F:
    *(unsigned __int8 *)(a1 + 192) = 0;
    return;
}
```

## 5. (Beta) C Style

```c
void HvResetLogFileStatusAll(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((*(uint32_t *)(arg1 + 0xA8)) == 1) goto loc_00A9EB6F;
    return;
loc_00A9EB6F:
    *(uint8_t *)(arg1 + 0xC0) = 0;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `8` | `W` |
| `Arg1` | `+ 0xC0` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9EB5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9EB5C[BB_00A9EB5C]
  bb_00A9EB65[BB_00A9EB65]
  bb_00A9EB6E[BB_00A9EB6E]
  bb_00A9EB6F[BB_00A9EB6F]
  bb_00A9EB77[BB_00A9EB77]
  bb_00A9EB5C -->|branch| bb_00A9EB6F
  bb_00A9EB5C -->|fallthrough| bb_00A9EB65
  bb_00A9EB6E -->|flow| bb_00A9EB6F
```
