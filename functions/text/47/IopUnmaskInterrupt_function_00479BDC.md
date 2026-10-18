# IopUnmaskInterrupt

- RVA: `0x00479BDC`–`0x00479BFC` (길이 `32` bytes)
- VA: `0x0000000140479BDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00479BF1` → [KeUnmaskInterrupt](KeUnmaskInterrupt_function_00479C04.md) (function, `0x00479C04`)

### Direct callers
- [IoReportInterruptActive](IoReportInterruptActive_function_00479B60.md) at `0x00479B86`
- [sub_006F483C](../6F/Unknown_function_006F483C.md) at `0x006F484A`
- [sub_006F483C](../6F/Unknown_function_006F483C.md) at `0x006F4869`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00479BDC  48 83 EC 28                     sub rsp, 0x28
00479BE0  F3 48 0F B8 51 98               popcnt rdx, qword ptr [rcx - 0x68]
00479BE6  4C 8D 41 A0                     lea r8, [rcx - 0x60]
00479BEA  48 81 C1 88 01 00 00            add rcx, 0x188
00479BF1  E8 0E 00 00 00                  call 0x140479c04
00479BF6  48 83 C4 28                     add rsp, 0x28
00479BFA  C3                              ret
00479BFB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopUnmaskInterrupt(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (392);
    result = KeUnmaskInterrupt(a1, a2, a1 - 96, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopUnmaskInterrupt(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (392);
    result = KeUnmaskInterrupt(Arg1, a2, Arg1 - 96, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x68` | `64` | `R` |
| `Arg1` | `- 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00479BDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00479BDC[BB_00479BDC]
  bb_00479BFB[BB_00479BFB]
```
