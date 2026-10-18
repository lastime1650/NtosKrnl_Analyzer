# MmReserveViewInSystemCache

- RVA: `0x007FE368`–`0x007FE385` (길이 `29` bytes)
- VA: `0x00000001407FE368`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007FE36F` → [MiObtainSystemCacheView](../../text/23/MiObtainSystemCacheView_function_00238870.md) (function, `0x00238870`)

### Direct callers
- [CcBuildUpHighPriorityMappings](../../text/4E/CcBuildUpHighPriorityMappings_function_004E161C.md) at `0x004E166C`
- [CcInitializePartitionVacbs](../../text/57/CcInitializePartitionVacbs_function_0057EB60.md) at `0x0057EBFB`

### Static image references
- `0x007FE379` → RVA `0x00E388E0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007FE36F` → [MiObtainSystemCacheView](../../text/23/MiObtainSystemCacheView_function_00238870.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FE368  48 83 EC 28                     sub rsp, 0x28
007FE36C  48 8B 09                        mov rcx, qword ptr [rcx]
007FE36F  E8 FC A4 A3 FF                  call 0x140238870
007FE374  48 85 C0                        test rax, rax
007FE377  75 06                           jne 0x1407fe37f
007FE379  FF 05 61 A5 63 00               inc dword ptr [rip + 0x63a561]
007FE37F  48 83 C4 28                     add rsp, 0x28
007FE383  C3                              ret
007FE384  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmReserveViewInSystemCache(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiObtainSystemCacheView(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (result == 0) {
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmReserveViewInSystemCache(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiObtainSystemCacheView(*(uint64_t *)(arg1), a2, a3, a4);
    if (result == 0) {
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FE368&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007FE368[BB_007FE368]
  bb_007FE379[BB_007FE379]
  bb_007FE37F[BB_007FE37F]
  bb_007FE384[BB_007FE384]
  bb_007FE368 -->|branch| bb_007FE37F
  bb_007FE368 -->|fallthrough| bb_007FE379
  bb_007FE379 -->|flow| bb_007FE37F
```
