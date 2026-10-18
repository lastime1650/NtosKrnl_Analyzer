# RtlInitializeSwapReference

- RVA: `0x0079AEEC`–`0x0079AEFB` (길이 `15` bytes)
- VA: `0x000000014079AEEC`
- 실행 섹션: `PAGE`
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
- [CmFcManagerInitialize](../../init/C5/CmFcManagerInitialize_function_00C5D93C.md) at `0x00C5D9AB`
- [CmFcManagerInitialize](../../init/C5/CmFcManagerInitialize_function_00C5D93C.md) at `0x00C5D9DB`
- [CmFcManagerInitialize](../../init/C5/CmFcManagerInitialize_function_00C5D93C.md) at `0x00C5DAEA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079AEEC  33 C0                           xor eax, eax
0079AEEE  48 89 01                        mov qword ptr [rcx], rax
0079AEF1  48 89 41 08                     mov qword ptr [rcx + 8], rax
0079AEF5  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0079AEF9  C3                              ret
0079AEFA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlInitializeSwapReference(__int64 a1)
{
    __int64 result;

    result = 0;
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    *(unsigned __int64 *)(a1 + 16) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlInitializeSwapReference(void *SwapReference)
{
    uint8_t *swapReference = (uint8_t *)SwapReference;

    int64_t result;

    result = 0;
    *(uint64_t *)(swapReference) = 0;
    *(uint64_t *)(swapReference + 0x8) = 0;
    *(uint64_t *)(swapReference + 0x10) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `SwapReference` | `+ 0x0` | `64` | `W` |
| `SwapReference` | `+ 0x8` | `64` | `W` |
| `SwapReference` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079AEEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079AEEC[BB_0079AEEC]
  bb_0079AEFA[BB_0079AEFA]
```
