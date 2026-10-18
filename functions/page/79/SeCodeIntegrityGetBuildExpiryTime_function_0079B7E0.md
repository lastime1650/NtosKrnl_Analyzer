# SeCodeIntegrityGetBuildExpiryTime

- RVA: `0x0079B7E0`–`0x0079B800` (길이 `32` bytes)
- VA: `0x000000014079B7E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0079B7F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ExpKernelExpirationDateCacheProvider](../7C/ExpKernelExpirationDateCacheProvider_function_007C8630.md) at `0x007C868D`

### Static image references
- `0x0079B7E4` → RVA `0x00F04EF0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0079B7F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079B7E0  48 83 EC 28                     sub rsp, 0x28
0079B7E4  48 8B 05 05 97 76 00            mov rax, qword ptr [rip + 0x769705]
0079B7EB  48 85 C0                        test rax, rax
0079B7EE  75 05                           jne 0x14079b7f5
0079B7F0  48 21 01                        and qword ptr [rcx], rax
0079B7F3  EB 05                           jmp 0x14079b7fa
0079B7F5  E8 D6 F2 F1 FF                  call 0x1406baad0
0079B7FA  48 83 C4 28                     add rsp, 0x28
0079B7FE  C3                              ret
0079B7FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeCodeIntegrityGetBuildExpiryTime(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 7771909) != 0) goto loc_0079B7F5;
    goto loc_0079B7FA;
loc_0079B7F5:
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_0079B7FA:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeCodeIntegrityGetBuildExpiryTime(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x769705) != 0) goto loc_0079B7F5;
    goto loc_0079B7FA;
loc_0079B7F5:
    result = guard_dispatch_icall(Arg1, a2, a3, a4);
loc_0079B7FA:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079B7E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079B7E0[BB_0079B7E0]
  bb_0079B7F0[BB_0079B7F0]
  bb_0079B7F5[BB_0079B7F5]
  bb_0079B7FA[BB_0079B7FA]
  bb_0079B7FF[BB_0079B7FF]
  bb_0079B7E0 -->|branch| bb_0079B7F5
  bb_0079B7E0 -->|fallthrough| bb_0079B7F0
  bb_0079B7F0 -->|branch| bb_0079B7FA
  bb_0079B7F5 -->|flow| bb_0079B7FA
```
