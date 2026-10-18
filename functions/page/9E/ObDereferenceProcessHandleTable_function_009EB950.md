# ObDereferenceProcessHandleTable

- RVA: `0x009EB950`–`0x009EB97D` (길이 `45` bytes)
- VA: `0x00000001409EB950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009EB976` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)

### Direct callers
- [IoRevokeHandlesForProcess](../../text/59/IoRevokeHandlesForProcess_function_005981A8.md) at `0x0059830E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009EB976` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009EB950  48 83 EC 28                     sub rsp, 0x28
009EB954  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009EB95B  0F 0D 09                        prefetchw byte ptr [rcx]
009EB95E  48 8B 01                        mov rax, qword ptr [rcx]
009EB961  48 83 E0 FE                     and rax, 0xfffffffffffffffe
009EB965  48 8D 50 FE                     lea rdx, [rax - 2]
009EB969  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
009EB96E  75 06                           jne 0x1409eb976
009EB970  48 83 C4 28                     add rsp, 0x28
009EB974  C3                              ret
009EB975  CC                              int3
009EB976  E8 35 E5 95 FF                  call 0x140349eb0
009EB97B  EB F3                           jmp 0x1409eb970
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObDereferenceProcessHandleTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (488);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_009EB976;
loc_009EB970:
    v_rsp = (v_rsp) + (40);
    return result;
loc_009EB976:
    result = ExfReleaseRundownProtection(a1, result - 2, a3, a4);
    goto loc_009EB970;
}
```

## 5. (Beta) C Style

```c
int64_t ObDereferenceProcessHandleTable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (488);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_009EB976;
loc_009EB970:
    local_rsp = (local_rsp) + (40);
    return result;
loc_009EB976:
    result = ExfReleaseRundownProtection(Arg1, result - 2, a3, a4);
    goto loc_009EB970;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009EB950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009EB950[BB_009EB950]
  bb_009EB970[BB_009EB970]
  bb_009EB975[BB_009EB975]
  bb_009EB976[BB_009EB976]
  bb_009EB950 -->|branch| bb_009EB976
  bb_009EB950 -->|fallthrough| bb_009EB970
  bb_009EB975 -->|flow| bb_009EB976
  bb_009EB976 -->|branch| bb_009EB970
```
