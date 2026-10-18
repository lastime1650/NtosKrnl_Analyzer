# SshpWorkItemTryAllowNextWorker

- RVA: `0x004BC078`–`0x004BC091` (길이 `25` bytes)
- VA: `0x00000001404BC078`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SshpPurgeBlockersWorker](../../page/A4/SshpPurgeBlockersWorker_function_00A4DE90.md) at `0x00A4DEC2`
- [SshpPurgeBlockersWorker](../../page/A4/SshpPurgeBlockersWorker_function_00A4DE90.md) at `0x00A4E0AF`
- [SshpSessionManagerFlushControlEventBufferWorker](../../page/A7/SshpSessionManagerFlushControlEventBufferWorker_function_00A76CC0.md) at `0x00A76D70`
- [SshpSessionManagerFlushControlEventBufferWorker](../../page/A7/SshpSessionManagerFlushControlEventBufferWorker_function_00A76CC0.md) at `0x00A76E7C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BC078  33 D2                           xor edx, edx
004BC07A  8D 42 01                        lea eax, [rdx + 1]
004BC07D  F0 0F B1 51 20                  lock cmpxchg dword ptr [rcx + 0x20], edx
004BC082  75 06                           jne 0x1404bc08a
004BC084  B2 01                           mov dl, 1
004BC086  8A C2                           mov al, dl
004BC088  C3                              ret
004BC089  CC                              int3
004BC08A  F0 83 61 20 FD                  lock and dword ptr [rcx + 0x20], 0xfffffffd
004BC08F  EB F5                           jmp 0x1404bc086
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpWorkItemTryAllowNextWorker(__int64 a1, int a2)
{
    a2 = 0;
    if (condition_is_not_equal) goto loc_004BC08A;
loc_004BC086:
    return 1;
loc_004BC08A:
    goto loc_004BC086;
}
```

## 5. (Beta) C Style

```c
int64_t SshpWorkItemTryAllowNextWorker(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg2 = 0;
    if (condition_is_not_equal) goto loc_004BC08A;
loc_004BC086:
    return 1;
loc_004BC08A:
    goto loc_004BC086;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BC078&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BC078[BB_004BC078]
  bb_004BC084[BB_004BC084]
  bb_004BC086[BB_004BC086]
  bb_004BC089[BB_004BC089]
  bb_004BC08A[BB_004BC08A]
  bb_004BC078 -->|branch| bb_004BC08A
  bb_004BC078 -->|fallthrough| bb_004BC084
  bb_004BC084 -->|flow| bb_004BC086
  bb_004BC089 -->|flow| bb_004BC08A
  bb_004BC08A -->|branch| bb_004BC086
```
