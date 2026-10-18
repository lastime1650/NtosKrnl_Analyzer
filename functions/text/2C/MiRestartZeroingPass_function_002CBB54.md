# MiRestartZeroingPass

- RVA: `0x002CBB54`–`0x002CBB78` (길이 `36` bytes)
- VA: `0x00000001402CBB54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiReassessZeroThreads](MiReassessZeroThreads_function_002CB0C0.md) at `0x002CB288`
- [MiAddZeroingThreads](MiAddZeroingThreads_function_002CBF78.md) at `0x002CC386`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CBB54  83 61 10 00                     and dword ptr [rcx + 0x10], 0
002CBB58  48 8D 91 C0 00 00 00            lea rdx, [rcx + 0xc0]
002CBB5F  48 83 61 60 00                  and qword ptr [rcx + 0x60], 0
002CBB64  48 8B 0A                        mov rcx, qword ptr [rdx]
002CBB67  EB 08                           jmp 0x1402cbb71
002CBB69  33 C0                           xor eax, eax
002CBB6B  87 41 E4                        xchg dword ptr [rcx - 0x1c], eax
002CBB6E  48 8B 09                        mov rcx, qword ptr [rcx]
002CBB71  48 3B CA                        cmp rcx, rdx
002CBB74  75 F3                           jne 0x1402cbb69
002CBB76  C3                              ret
002CBB77  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRestartZeroingPass(__int64 a1)
{
    __int64 result;

    goto loc_002CBB71;
loc_002CBB69:
    result = 0;
loc_002CBB71:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192))) != (a1 + 192)) goto loc_002CBB69;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiRestartZeroingPass(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    goto loc_002CBB71;
loc_002CBB69:
    result = 0;
loc_002CBB71:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0))) != (Arg1 + 192)) goto loc_002CBB69;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R/W` |
| `Arg1` | `+ 0x60` | `64` | `R/W` |
| `Arg1` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CBB54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CBB54[BB_002CBB54]
  bb_002CBB69[BB_002CBB69]
  bb_002CBB71[BB_002CBB71]
  bb_002CBB76[BB_002CBB76]
  bb_002CBB77[BB_002CBB77]
  bb_002CBB54 -->|branch| bb_002CBB71
  bb_002CBB69 -->|flow| bb_002CBB71
  bb_002CBB71 -->|branch| bb_002CBB69
  bb_002CBB71 -->|fallthrough| bb_002CBB76
```
