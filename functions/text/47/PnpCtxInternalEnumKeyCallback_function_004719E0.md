# PnpCtxInternalEnumKeyCallback

- RVA: `0x004719E0`–`0x00471A13` (길이 `51` bytes)
- VA: `0x00000001404719E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ABF48`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004719FE` → [DrvDbGetObjectSubKeyCallback](../../page/A1/DrvDbGetObjectSubKeyCallback_function_00A11300.md) (function, `0x00A11300`)
- `0x00471A0C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [SysCtxInternalEnumSubkeyCallback](SysCtxInternalEnumSubkeyCallback_function_00471998.md) at `0x004719BC`

### Static image references
- `0x004719EF` → RVA `0x00A11300` (`DrvDbGetObjectSubKeyCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004719FE` → [DrvDbGetObjectSubKeyCallback](../../page/A1/DrvDbGetObjectSubKeyCallback_function_00A11300.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004719E0  48 83 EC 38                     sub rsp, 0x38
004719E4  4D 8B 51 08                     mov r10, qword ptr [r9 + 8]
004719E8  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
004719EC  49 8B 09                        mov rcx, qword ptr [r9]
004719EF  4C 8D 0D 0A F9 59 00            lea r9, [rip + 0x59f90a]
004719F6  4D 3B D1                        cmp r10, r9
004719F9  4C 8B C8                        mov r9, rax
004719FC  75 0B                           jne 0x140471a09
004719FE  E8 FD F8 59 00                  call 0x140a11300
00471A03  48 83 C4 38                     add rsp, 0x38
00471A07  C3                              ret
00471A08  CC                              int3
00471A09  49 8B C2                        mov rax, r10
00471A0C  E8 BF 90 24 00                  call 0x1406baad0
00471A11  EB F0                           jmp 0x140471a03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCtxInternalEnumKeyCallback(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if ((*(unsigned __int64 *)(a4 + 8)) != (v_rip + 5896458)) goto loc_00471A09;
    result = DrvDbGetObjectSubKeyCallback(*(unsigned __int64 *)(a4), a2, a3, *(unsigned __int64 *)(a4 + 16));
loc_00471A03:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00471A09:
    result = guard_dispatch_icall(*(unsigned __int64 *)(a4), a2, a3, *(unsigned __int64 *)(a4 + 16));
    goto loc_00471A03;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCtxInternalEnumKeyCallback(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if ((*(uint64_t *)(arg4 + 0x8)) != (v_rip + 5896458)) goto loc_00471A09;
    result = DrvDbGetObjectSubKeyCallback(*(uint64_t *)(arg4), Arg2, Arg3, *(uint64_t *)(arg4 + 0x10));
loc_00471A03:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00471A09:
    result = guard_dispatch_icall(*(uint64_t *)(arg4), Arg2, Arg3, *(uint64_t *)(arg4 + 0x10));
    goto loc_00471A03;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004719E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004719E0[BB_004719E0]
  bb_004719FE[BB_004719FE]
  bb_00471A03[BB_00471A03]
  bb_00471A08[BB_00471A08]
  bb_00471A09[BB_00471A09]
  bb_004719E0 -->|branch| bb_00471A09
  bb_004719E0 -->|fallthrough| bb_004719FE
  bb_004719FE -->|flow| bb_00471A03
  bb_00471A08 -->|flow| bb_00471A09
  bb_00471A09 -->|branch| bb_00471A03
```
