# WmipGECleanup

- RVA: `0x007B3D00`–`0x007B3D2C` (길이 `44` bytes)
- VA: `0x00000001407B3D00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007B3D12` → [EtwUnregister](../A7/EtwUnregister_function_00A723D0.md) (function, `0x00A723D0`)
- `0x007B3D20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007B3D20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B3D00  40 53                           push rbx
007B3D02  48 83 EC 20                     sub rsp, 0x20
007B3D06  48 8B D9                        mov rbx, rcx
007B3D09  48 8B 49 68                     mov rcx, qword ptr [rcx + 0x68]
007B3D0D  48 85 C9                        test rcx, rcx
007B3D10  74 05                           je 0x1407b3d17
007B3D12  E8 B9 E6 2B 00                  call 0x140a723d0
007B3D17  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
007B3D1B  BA 57 6D 69 70                  mov edx, 0x70696d57
007B3D20  E8 4B EB 3C 00                  call 0x140b82870
007B3D25  48 83 C4 20                     add rsp, 0x20
007B3D29  5B                              pop rbx
007B3D2A  C3                              ret
007B3D2B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipGECleanup(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 104) != 0) {
        result = EtwUnregister(*(unsigned __int64 *)(a1 + 104), a2, a3, a4);
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 96), (unsigned int)(0x70696D57ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmipGECleanup(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x68) != 0) {
        result = EtwUnregister(*(uint64_t *)(arg1 + 0x68), a2, a3, a4);
    }
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x60), (uint32_t)(0x70696D57ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B3D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B3D00[BB_007B3D00]
  bb_007B3D12[BB_007B3D12]
  bb_007B3D17[BB_007B3D17]
  bb_007B3D2B[BB_007B3D2B]
  bb_007B3D00 -->|branch| bb_007B3D17
  bb_007B3D00 -->|fallthrough| bb_007B3D12
  bb_007B3D12 -->|flow| bb_007B3D17
```
