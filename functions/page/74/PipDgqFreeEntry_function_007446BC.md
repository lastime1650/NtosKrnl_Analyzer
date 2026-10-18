# PipDgqFreeEntry

- RVA: `0x007446BC`–`0x007446EC` (길이 `48` bytes)
- VA: `0x00000001407446BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007446CE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x007446E0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiDmaGuardQueueRemoveEntry](../../text/4C/PiDmaGuardQueueRemoveEntry_function_004C822C.md) at `0x004C8293`
- [PipDmgFlushQueueAndRestartDevices](../73/PipDmgFlushQueueAndRestartDevices_function_0073BF9C.md) at `0x0073C040`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007446CE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x007446E0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007446BC  40 53                           push rbx
007446BE  48 83 EC 20                     sub rsp, 0x20
007446C2  48 8B D9                        mov rbx, rcx
007446C5  BA 50 6E 70 64                  mov edx, 0x64706e50
007446CA  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007446CE  E8 0D 32 BB FF                  call 0x1402f78e0
007446D3  48 83 63 10 00                  and qword ptr [rbx + 0x10], 0
007446D8  BA 50 6E 70 64                  mov edx, 0x64706e50
007446DD  48 8B CB                        mov rcx, rbx
007446E0  E8 8B E1 43 00                  call 0x140b82870
007446E5  48 83 C4 20                     add rsp, 0x20
007446E9  5B                              pop rbx
007446EA  C3                              ret
007446EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipDgqFreeEntry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 16), (unsigned int)(0x64706E50ULL), a3, a4);
    result = ExFreePoolWithTag(a1, (unsigned int)(0x64706E50ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipDgqFreeEntry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x10), (uint32_t)(0x64706E50ULL), a3, a4);
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x64706E50ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007446BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007446BC[BB_007446BC]
  bb_007446EB[BB_007446EB]
```
