# SLSendPolicyChangeNotifications

- RVA: `0x007C9BDC`–`0x007C9BFC` (길이 `32` bytes)
- VA: `0x00000001407C9BDC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007C9BF1` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (function, `0x003926B0`)

### Direct callers
- [SLUpdateLicenseDataInternal](SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA08C`
- [SLUpdateLicenseDataInternal](SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CA834`
- [SLUpdateLicenseDataInternal](SLUpdateLicenseDataInternal_function_007C9C04.md) at `0x007CAA7F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007C9BF1` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C9BDC  48 83 EC 28                     sub rsp, 0x28
007C9BE0  48 8B 89 00 B7 00 00            mov rcx, qword ptr [rcx + 0xb700]
007C9BE7  48 85 C9                        test rcx, rcx
007C9BEA  74 0A                           je 0x1407c9bf6
007C9BEC  45 33 C0                        xor r8d, r8d
007C9BEF  33 D2                           xor edx, edx
007C9BF1  E8 BA 8A BC FF                  call 0x1403926b0
007C9BF6  48 83 C4 28                     add rsp, 0x28
007C9BFA  C3                              ret
007C9BFB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SLSendPolicyChangeNotifications(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 46848) != 0) {
        a3 = 0;
        a2 = 0;
        result = ExNotifyCallback(*(unsigned __int64 *)(a1 + 46848), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SLSendPolicyChangeNotifications(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0xB700) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = ExNotifyCallback(*(uint64_t *)(arg1 + 0xB700), Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB700` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C9BDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C9BDC[BB_007C9BDC]
  bb_007C9BEC[BB_007C9BEC]
  bb_007C9BF6[BB_007C9BF6]
  bb_007C9BFB[BB_007C9BFB]
  bb_007C9BDC -->|branch| bb_007C9BF6
  bb_007C9BDC -->|fallthrough| bb_007C9BEC
  bb_007C9BEC -->|flow| bb_007C9BF6
```
