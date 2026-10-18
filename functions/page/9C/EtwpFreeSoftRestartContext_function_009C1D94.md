# EtwpFreeSoftRestartContext

- RVA: `0x009C1D94`–`0x009C1DDB` (길이 `71` bytes)
- VA: `0x00000001409C1D94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000687A0`
- 디코드: `20`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009C1DB9` → [EtwpCancelMemoryPreservation](../7B/EtwpCancelMemoryPreservation_function_007BEC0C.md) (function, `0x007BEC0C`)
- `0x009C1DC2` → [RtlFreeAnsiString](RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x009C1DCC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpFreeLoggerContext](EtwpFreeLoggerContext_function_009C1688.md) at `0x009C1756`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009C1DCC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C1D94  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009C1D99  57                              push rdi
009C1D9A  48 83 EC 20                     sub rsp, 0x20
009C1D9E  48 8B B9 48 05 00 00            mov rdi, qword ptr [rcx + 0x548]
009C1DA5  48 8B D9                        mov rbx, rcx
009C1DA8  48 85 FF                        test rdi, rdi
009C1DAB  75 0C                           jne 0x1409c1db9
009C1DAD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009C1DB2  48 83 C4 20                     add rsp, 0x20
009C1DB6  5F                              pop rdi
009C1DB7  C3                              ret
009C1DB8  CC                              int3
009C1DB9  E8 4E CE DF FF                  call 0x1407bec0c
009C1DBE  48 8D 4F 10                     lea rcx, [rdi + 0x10]
009C1DC2  E8 39 EA FF FF                  call 0x1409c0800
009C1DC7  33 D2                           xor edx, edx
009C1DC9  48 8B CF                        mov rcx, rdi
009C1DCC  E8 9F 0A 1C 00                  call 0x140b82870
009C1DD1  48 83 A3 48 05 00 00 00         and qword ptr [rbx + 0x548], 0
009C1DD9  EB D2                           jmp 0x1409c1dad
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpFreeSoftRestartContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 1352) != 0) goto loc_009C1DB9;
loc_009C1DAD:
    v_rsp = (v_rsp) + (32);
    return result;
loc_009C1DB9:
    result = EtwpCancelMemoryPreservation(a1, a2, a3, a4);
    result = RtlFreeAnsiString(*(unsigned __int64 *)(a1 + 1352) + 16, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 1352), a2, a3, a4);
    goto loc_009C1DAD;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpFreeSoftRestartContext(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x548) != 0) goto loc_009C1DB9;
loc_009C1DAD:
    local_rsp = (local_rsp) + (32);
    return result;
loc_009C1DB9:
    result = EtwpCancelMemoryPreservation(Arg1, Arg2, a3, a4);
    result = RtlFreeAnsiString(*(uint64_t *)(arg1 + 0x548) + 16, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x548), Arg2, a3, a4);
    goto loc_009C1DAD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x548` | `64` | `R` |
| `Arg1` | `+ 0x548` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C1D94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009C1D94[BB_009C1D94]
  bb_009C1DAD[BB_009C1DAD]
  bb_009C1DB8[BB_009C1DB8]
  bb_009C1DB9[BB_009C1DB9]
  bb_009C1D94 -->|branch| bb_009C1DB9
  bb_009C1D94 -->|fallthrough| bb_009C1DAD
  bb_009C1DB8 -->|flow| bb_009C1DB9
  bb_009C1DB9 -->|branch| bb_009C1DAD
```
