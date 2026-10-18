# McGenEventRegister_EtwRegister

- RVA: `0x0057EF04`–`0x0057EF21` (길이 `29` bytes)
- VA: `0x000000014057EF04`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0057EF16` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)

### Direct callers
- [PdcInitializeETW](../60/PdcInitializeETW_function_00605D30.md) at `0x00605D59`
- [CarEtwRegister](../61/CarEtwRegister_function_006179D4.md) at `0x00617A16`
- [sub_006E5110](../6E/Unknown_function_006E5110.md) at `0x006E52B5`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B63D`
- [IopInitializePlugPlayServices](../../init/C2/IopInitializePlugPlayServices_function_00C2F298.md) at `0x00C2FEF7`

### Static image references
- `0x0057EF0F` → RVA `0x004949E0` (`McGenControlCallbackV2`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0057EF16` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057EF04  48 83 EC 28                     sub rsp, 0x28
0057EF08  33 C0                           xor eax, eax
0057EF0A  49 39 01                        cmp qword ptr [r9], rax
0057EF0D  75 0C                           jne 0x14057ef1b
0057EF0F  48 8D 15 CA 5A F1 FF            lea rdx, [rip - 0xea536]
0057EF16  E8 45 1A 3A 00                  call 0x140920960
0057EF1B  48 83 C4 28                     add rsp, 0x28
0057EF1F  C3                              ret
0057EF20  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McGenEventRegister_EtwRegister(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if ((*(unsigned __int64 *)(a4)) == 0) {
        a2 = v_rip - 959798;
        result = EtwRegister(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McGenEventRegister_EtwRegister(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if ((*(uint64_t *)(arg4)) == 0) {
        Arg2 = v_rip - 959798;
        result = EtwRegister(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057EF04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057EF04[BB_0057EF04]
  bb_0057EF0F[BB_0057EF0F]
  bb_0057EF1B[BB_0057EF1B]
  bb_0057EF20[BB_0057EF20]
  bb_0057EF04 -->|branch| bb_0057EF1B
  bb_0057EF04 -->|fallthrough| bb_0057EF0F
  bb_0057EF0F -->|flow| bb_0057EF1B
```
