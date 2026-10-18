# EtwpClearPartitionContext

- RVA: `0x004C4208`–`0x004C4232` (길이 `42` bytes)
- VA: `0x00000001404C4208`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070B1C`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C4227` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- [EtwpFreeLoggerContext](../../page/9C/EtwpFreeLoggerContext_function_009C1688.md) at `0x009C18EC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C4208  40 53                           push rbx
004C420A  48 83 EC 20                     sub rsp, 0x20
004C420E  48 8B D9                        mov rbx, rcx
004C4211  48 8B 09                        mov rcx, qword ptr [rcx]
004C4214  48 85 C9                        test rcx, rcx
004C4217  75 09                           jne 0x1404c4222
004C4219  33 C0                           xor eax, eax
004C421B  48 83 C4 20                     add rsp, 0x20
004C421F  5B                              pop rbx
004C4220  C3                              ret
004C4221  CC                              int3
004C4222  BA 45 74 77 6F                  mov edx, 0x6f777445
004C4227  E8 44 EC E7 FF                  call 0x140342e70
004C422C  48 83 23 00                     and qword ptr [rbx], 0
004C4230  EB E7                           jmp 0x1404c4219
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpClearPartitionContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1) != 0) goto loc_004C4222;
loc_004C4219:
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_004C4222:
    result = PsDereferencePartition(*(unsigned __int64 *)(a1), (unsigned int)(0x6F777445ULL), a3, a4);
    goto loc_004C4219;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpClearPartitionContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1) != 0) goto loc_004C4222;
loc_004C4219:
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_004C4222:
    result = PsDereferencePartition(*(uint64_t *)(arg1), (uint32_t)(0x6F777445ULL), a3, a4);
    goto loc_004C4219;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C4208&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C4208[BB_004C4208]
  bb_004C4219[BB_004C4219]
  bb_004C4221[BB_004C4221]
  bb_004C4222[BB_004C4222]
  bb_004C4208 -->|branch| bb_004C4222
  bb_004C4208 -->|fallthrough| bb_004C4219
  bb_004C4221 -->|flow| bb_004C4222
  bb_004C4222 -->|branch| bb_004C4219
```
