# EtwInitializeProcessorActivityId

- RVA: `0x007B508C`–`0x007B50A7` (길이 `27` bytes)
- VA: `0x00000001407B508C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007B509A` → [EtwpInitializeActivityIdSeed](EtwpInitializeActivityIdSeed_function_007B69A4.md) (function, `0x007B69A4`)

### Direct callers
- [EtwpInitialize](../../init/C4/EtwpInitialize_function_00C4DBCC.md) at `0x00C4DD60`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B508C  48 83 EC 28                     sub rsp, 0x28
007B5090  8B 51 24                        mov edx, dword ptr [rcx + 0x24]
007B5093  48 8B 89 A8 8B 00 00            mov rcx, qword ptr [rcx + 0x8ba8]
007B509A  E8 05 19 00 00                  call 0x1407b69a4
007B509F  33 C0                           xor eax, eax
007B50A1  48 83 C4 28                     add rsp, 0x28
007B50A5  C3                              ret
007B50A6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwInitializeProcessorActivityId(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = EtwpInitializeActivityIdSeed(*(unsigned __int64 *)(a1 + 35752), (unsigned int)(*(unsigned int *)(a1 + 36)), a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwInitializeProcessorActivityId(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = EtwpInitializeActivityIdSeed(*(uint64_t *)(arg1 + 0x8BA8), (uint32_t)(*(uint32_t *)(arg1 + 0x24)), a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x8BA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B508C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B508C[BB_007B508C]
  bb_007B50A6[BB_007B50A6]
```
