# PnpAllocateDeviceInstancePath

- RVA: `0x0072DC30`–`0x0072DC6A` (길이 `58` bytes)
- VA: `0x000000014072DC30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0072DC4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [IoReportDetectedDevice](IoReportDetectedDevice_function_00725CD0.md) at `0x007261B9`
- [PiInitializeDevice](../73/PiInitializeDevice_function_0073EC5C.md) at `0x0073EF6E`
- [sub_00B420B0](../B4/Unknown_function_00B420B0.md) at `0x00B42160`
- [IopInitializePlugPlayServices](../../init/C2/IopInitializePlugPlayServices_function_00C2F298.md) at `0x00C2FD32`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0072DC4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0072DC30  40 53                           push rbx
0072DC32  48 83 EC 20                     sub rsp, 0x20
0072DC36  33 C0                           xor eax, eax
0072DC38  66 89 51 2A                     mov word ptr [rcx + 0x2a], dx
0072DC3C  48 8B D9                        mov rbx, rcx
0072DC3F  66 89 41 28                     mov word ptr [rcx + 0x28], ax
0072DC43  8B D2                           mov edx, edx
0072DC45  41 B8 50 6E 70 49               mov r8d, 0x49706e50
0072DC4B  8D 48 40                        lea ecx, [rax + 0x40]
0072DC4E  E8 9D 44 45 00                  call 0x140b820f0
0072DC53  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
0072DC57  48 F7 D8                        neg rax
0072DC5A  1B C0                           sbb eax, eax
0072DC5C  F7 D0                           not eax
0072DC5E  25 9A 00 00 C0                  and eax, 0xc000009a
0072DC63  48 83 C4 20                     add rsp, 0x20
0072DC67  5B                              pop rbx
0072DC68  C3                              ret
0072DC69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpAllocateDeviceInstancePath(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 0;
    *(unsigned __int16 *)(a1 + 42) = (unsigned __int16)(a2);
    *(unsigned __int16 *)(a1 + 40) = 0;
    result = ExAllocatePool2(result + 64, (unsigned int)(a2), (unsigned int)(0x49706E50ULL), a4);
    *(unsigned __int64 *)(a1 + 48) = result;
    result = -(result);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC000009AULL));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpAllocateDeviceInstancePath(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 0;
    *(uint16_t *)(arg1 + 0x2A) = (uint16_t)(Arg2);
    *(uint16_t *)(arg1 + 0x28) = 0;
    result = ExAllocatePool2(result + 64, (uint32_t)(Arg2), (uint32_t)(0x49706E50ULL), a4);
    *(uint64_t *)(arg1 + 0x30) = result;
    result = -(result);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC000009AULL));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `16` | `W` |
| `Arg1` | `+ 0x2A` | `16` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072DC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072DC30[BB_0072DC30]
  bb_0072DC69[BB_0072DC69]
```
