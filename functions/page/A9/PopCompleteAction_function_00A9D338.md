# PopCompleteAction

- RVA: `0x00A9D338`–`0x00A9D362` (길이 `42` bytes)
- VA: `0x0000000140A9D338`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E0D8`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A9D35B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [PopExecutePowerAction](../75/PopExecutePowerAction_function_0075E6B4.md) at `0x0075E761`
- [PopExecutePowerAction](../75/PopExecutePowerAction_function_0075E6B4.md) at `0x0075E791`
- [PopExecutePowerAction](../75/PopExecutePowerAction_function_0075E6B4.md) at `0x0075EB87`
- [PopPolicyWorkerAction](PopPolicyWorkerAction_function_00A9CC40.md) at `0x00A9CD7D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A9D35B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9D338  48 83 EC 28                     sub rsp, 0x28
00A9D33C  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A9D33F  A8 20                           test al, 0x20
00A9D341  75 06                           jne 0x140a9d349
00A9D343  48 83 C4 28                     add rsp, 0x28
00A9D347  C3                              ret
00A9D348  CC                              int3
00A9D349  83 E0 DF                        and eax, 0xffffffdf
00A9D34C  45 33 C0                        xor r8d, r8d
00A9D34F  89 41 04                        mov dword ptr [rcx + 4], eax
00A9D352  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A9D356  89 51 18                        mov dword ptr [rcx + 0x18], edx
00A9D359  33 D2                           xor edx, edx
00A9D35B  E8 B0 1F 8A FF                  call 0x14033f310
00A9D360  EB E1                           jmp 0x140a9d343
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCompleteAction(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) != 0) goto loc_00A9D349;
loc_00A9D343:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(a1 + 4));
loc_00A9D349:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (0xFFFFFFDFULL));
    a3 = 0;
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 24) = a2;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    goto loc_00A9D343;
}
```

## 5. (Beta) C Style

```c
int64_t PopCompleteAction(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (32)) != 0) goto loc_00A9D349;
loc_00A9D343:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x4));
loc_00A9D349:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (0xFFFFFFDFULL));
    Arg3 = 0;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) = Arg2;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, a4);
    goto loc_00A9D343;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9D338&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9D338[BB_00A9D338]
  bb_00A9D343[BB_00A9D343]
  bb_00A9D348[BB_00A9D348]
  bb_00A9D349[BB_00A9D349]
  bb_00A9D338 -->|branch| bb_00A9D349
  bb_00A9D338 -->|fallthrough| bb_00A9D343
  bb_00A9D348 -->|flow| bb_00A9D349
  bb_00A9D349 -->|branch| bb_00A9D343
```
