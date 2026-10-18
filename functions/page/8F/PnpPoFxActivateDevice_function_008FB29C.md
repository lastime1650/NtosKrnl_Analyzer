# PnpPoFxActivateDevice

- RVA: `0x008FB29C`–`0x008FB2E9` (길이 `77` bytes)
- VA: `0x00000001408FB29C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `20`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008FB2BC` → [PnpMapActivatingDeviceNodeToThread](../../text/3E/PnpMapActivatingDeviceNodeToThread_function_003EE1D4.md) (function, `0x003EE1D4`)
- `0x008FB2C5` → [PoFxActivateDevice](../../text/4A/PoFxActivateDevice_function_004A0DAC.md) (function, `0x004A0DAC`)
- `0x008FB2CD` → [PnpUnmapActivatingDeviceNodeToThread](../../text/3E/PnpUnmapActivatingDeviceNodeToThread_function_003EE4C0.md) (function, `0x003EE4C0`)

### Direct callers
- [PnpQueryStopDeviceNode](../73/PnpQueryStopDeviceNode_function_0073F47C.md) at `0x0073F4D4`
- [PipProcessDevNodeTree](PipProcessDevNodeTree_function_008F9068.md) at `0x008F9698`
- [PipEnumerateDevice](PipEnumerateDevice_function_008F99E4.md) at `0x008F9A8E`
- [PipEnumerateDevice](PipEnumerateDevice_function_008F99E4.md) at `0x008F9AFD`
- [PiProcessQueryDeviceState](PiProcessQueryDeviceState_function_008FA0F8.md) at `0x008FA132`
- [PnpDeleteLockedDeviceNode](../A0/PnpDeleteLockedDeviceNode_function_00A09DC4.md) at `0x00A09E17`
- [PnpDeleteLockedDeviceNode](../A0/PnpDeleteLockedDeviceNode_function_00A09DC4.md) at `0x00A09E30`
- [PnpDeleteLockedDeviceNode](../A0/PnpDeleteLockedDeviceNode_function_00A09DC4.md) at `0x00A09E74`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008FB2BC` → [PnpMapActivatingDeviceNodeToThread](../../text/3E/PnpMapActivatingDeviceNodeToThread_function_003EE1D4.md) (`PAGE` → `.text`)
  - `0x008FB2C5` → [PoFxActivateDevice](../../text/4A/PoFxActivateDevice_function_004A0DAC.md) (`PAGE` → `.text`)
  - `0x008FB2CD` → [PnpUnmapActivatingDeviceNodeToThread](../../text/3E/PnpUnmapActivatingDeviceNodeToThread_function_003EE4C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008FB29C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008FB2A1  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008FB2A6  57                              push rdi
008FB2A7  48 83 EC 20                     sub rsp, 0x20
008FB2AB  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
008FB2B4  8B F2                           mov esi, edx
008FB2B6  48 8B D3                        mov rdx, rbx
008FB2B9  48 8B F9                        mov rdi, rcx
008FB2BC  E8 13 2F AF FF                  call 0x1403ee1d4
008FB2C1  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008FB2C5  E8 E2 5A BA FF                  call 0x1404a0dac
008FB2CA  48 8B CB                        mov rcx, rbx
008FB2CD  E8 EE 31 AF FF                  call 0x1403ee4c0
008FB2D2  09 B7 C0 02 00 00               or dword ptr [rdi + 0x2c0], esi
008FB2D8  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
008FB2DD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008FB2E2  48 83 C4 20                     add rsp, 0x20
008FB2E6  5F                              pop rdi
008FB2E7  C3                              ret
008FB2E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpPoFxActivateDevice(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PnpMapActivatingDeviceNodeToThread(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    result = PoFxActivateDevice(*(unsigned __int64 *)(a1 + 32), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    result = PnpUnmapActivatingDeviceNodeToThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpPoFxActivateDevice(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PnpMapActivatingDeviceNodeToThread(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    result = PoFxActivateDevice(*(uint64_t *)(arg1 + 0x20), *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    result = PnpUnmapActivatingDeviceNodeToThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x2C0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FB29C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FB29C[BB_008FB29C]
  bb_008FB2E8[BB_008FB2E8]
```
