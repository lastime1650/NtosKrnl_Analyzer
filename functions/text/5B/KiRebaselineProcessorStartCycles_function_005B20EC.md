# KiRebaselineProcessorStartCycles

- RVA: `0x005B20EC`–`0x005B2139` (길이 `77` bytes)
- VA: `0x00000001405B20EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B20F7` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)

### Direct callers
- [KiInitializeProcessorCycleAccumulation](KiInitializeProcessorCycleAccumulation_function_005B2014.md) at `0x005B2094`
- [KiCalibrateTimeAdjustment](../../pagelk/B7/KiCalibrateTimeAdjustment_function_00B797E0.md) at `0x00B7996B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B20EC  40 53                           push rbx
005B20EE  48 83 EC 20                     sub rsp, 0x20
005B20F2  48 8B D9                        mov rbx, rcx
005B20F5  33 C9                           xor ecx, ecx
005B20F7  E8 E4 C6 DC FF                  call 0x14037e7e0
005B20FC  8A 8B AC 00 00 00               mov cl, byte ptr [rbx + 0xac]
005B2102  4C 8B C0                        mov r8, rax
005B2105  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005B210B  49 8B D0                        mov rdx, r8
005B210E  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
005B2115  84 C9                           test cl, cl
005B2117  74 03                           je 0x1405b211c
005B2119  48 D3 E2                        shl rdx, cl
005B211C  48 F7 E2                        mul rdx
005B211F  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
005B2124  4C 89 83 F8 86 00 00            mov qword ptr [rbx + 0x86f8], r8
005B212B  48 89 93 80 86 00 00            mov qword ptr [rbx + 0x8680], rdx
005B2132  48 83 C4 20                     add rsp, 0x20
005B2136  5B                              pop rbx
005B2137  C3                              ret
005B2138  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiRebaselineProcessorStartCycles(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_p8 = a2;
    *(unsigned __int64 *)(a1 + 34552) = result;
    *(unsigned __int64 *)(a1 + 34432) = a2;
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 176);
}
```

## 5. (Beta) C Style

```c
int64_t KiRebaselineProcessorStartCycles(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, a2, a3, a4);
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        a2 = (result) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_p8 = a2;
    *(uint64_t *)(arg1 + 0x86F8) = result;
    *(uint64_t *)(arg1 + 0x8680) = a2;
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0xB0);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0x8680` | `64` | `W` |
| `Arg1` | `+ 0x86F8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B20EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B20EC[BB_005B20EC]
  bb_005B2119[BB_005B2119]
  bb_005B211C[BB_005B211C]
  bb_005B2138[BB_005B2138]
  bb_005B20EC -->|branch| bb_005B211C
  bb_005B20EC -->|fallthrough| bb_005B2119
  bb_005B2119 -->|flow| bb_005B211C
```
