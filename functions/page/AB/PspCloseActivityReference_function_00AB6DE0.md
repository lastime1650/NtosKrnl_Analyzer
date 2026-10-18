# PspCloseActivityReference

- RVA: `0x00AB6DE0`–`0x00AB6DFF` (길이 `31` bytes)
- VA: `0x0000000140AB6DE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D35C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB6DF8` → [PsReleaseProcessWakeCounter](../88/PsReleaseProcessWakeCounter_function_0088B940.md) (function, `0x0088B940`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB6DE0  48 83 EC 28                     sub rsp, 0x28
00AB6DE4  49 83 F9 01                     cmp r9, 1
00AB6DE8  74 06                           je 0x140ab6df0
00AB6DEA  48 83 C4 28                     add rsp, 0x28
00AB6DEE  C3                              ret
00AB6DEF  CC                              int3
00AB6DF0  48 8B 0A                        mov rcx, qword ptr [rdx]
00AB6DF3  48 85 C9                        test rcx, rcx
00AB6DF6  74 F2                           je 0x140ab6dea
00AB6DF8  E8 43 4B DD FF                  call 0x14088b940
00AB6DFD  EB EB                           jmp 0x140ab6dea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCloseActivityReference(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a4 == 1) goto loc_00AB6DF0;
loc_00AB6DEA:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB6DF0:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00AB6DEA;
    result = PsReleaseProcessWakeCounter(*(unsigned __int64 *)(a2), a2, a3, a4);
    goto loc_00AB6DEA;
}
```

## 5. (Beta) C Style

```c
int64_t PspCloseActivityReference(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg4 == 1) goto loc_00AB6DF0;
loc_00AB6DEA:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB6DF0:
    if (*(uint64_t *)(arg2) == 0) goto loc_00AB6DEA;
    result = PsReleaseProcessWakeCounter(*(uint64_t *)(arg2), Arg2, Arg3, Arg4);
    goto loc_00AB6DEA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB6DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB6DE0[BB_00AB6DE0]
  bb_00AB6DEA[BB_00AB6DEA]
  bb_00AB6DEF[BB_00AB6DEF]
  bb_00AB6DF0[BB_00AB6DF0]
  bb_00AB6DF8[BB_00AB6DF8]
  bb_00AB6DE0 -->|branch| bb_00AB6DF0
  bb_00AB6DE0 -->|fallthrough| bb_00AB6DEA
  bb_00AB6DEF -->|flow| bb_00AB6DF0
  bb_00AB6DF0 -->|branch| bb_00AB6DEA
  bb_00AB6DF0 -->|fallthrough| bb_00AB6DF8
  bb_00AB6DF8 -->|branch| bb_00AB6DEA
```
