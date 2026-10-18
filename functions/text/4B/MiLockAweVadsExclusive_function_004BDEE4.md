# MiLockAweVadsExclusive

- RVA: `0x004BDEE4`–`0x004BDF15` (길이 `49` bytes)
- VA: `0x00000001404BDEE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BDF0A` → [ExAcquireAutoExpandPushLockExclusive](../26/ExAcquireAutoExpandPushLockExclusive_function_00264B70.md) (function, `0x00264B70`)

### Direct callers
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022DD4D`
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022E185`
- [MiRemoveUserPhysicalPagesView](../68/MiRemoveUserPhysicalPagesView_function_00689658.md) at `0x006896A4`
- [MmSetGraphicsPtes](../../page/7F/MmSetGraphicsPtes_function_007FC8B0.md) at `0x007FC9D0`
- [MiCreateProcessDefaultAweInfo](../../page/80/MiCreateProcessDefaultAweInfo_function_0080A8C0.md) at `0x0080A927`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BDEE4  48 83 EC 28                     sub rsp, 0x28
004BDEE8  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
004BDEEF  48 8B D1                        mov rdx, rcx
004BDEF2  48 8B 88 10 04 00 00            mov rcx, qword ptr [rax + 0x410]
004BDEF9  66 FF 8A E6 01 00 00            dec word ptr [rdx + 0x1e6]
004BDF00  48 81 C1 58 04 00 00            add rcx, 0x458
004BDF07  33 D2                           xor edx, edx
004BDF09  90                              nop
004BDF0A  E8 61 6C DA FF                  call 0x140264b70
004BDF0F  48 83 C4 28                     add rsp, 0x28
004BDF13  C3                              ret
004BDF14  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockAweVadsExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 1040)) + (0x458ULL);
    a2 = 0;
    result = ExAcquireAutoExpandPushLockExclusive(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockAweVadsExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x410)) + (0x458ULL);
    a2 = 0;
    result = ExAcquireAutoExpandPushLockExclusive(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BDEE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BDEE4[BB_004BDEE4]
  bb_004BDF14[BB_004BDF14]
```
