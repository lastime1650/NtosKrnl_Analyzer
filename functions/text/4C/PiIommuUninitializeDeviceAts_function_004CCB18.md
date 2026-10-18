# PiIommuUninitializeDeviceAts

- RVA: `0x004CCB18`–`0x004CCB3B` (길이 `35` bytes)
- VA: `0x00000001404CCB18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `11`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004CCB34` → [ExUninitializeDeviceAts](../65/ExUninitializeDeviceAts_function_00659D6C.md) (function, `0x00659D6C`)

### Direct callers
- [sub_00B347A2](../../page/B3/Unknown_function_00B347A2.md) at `0x00B347A5`
- [sub_00B49BD6](../../page/B4/Unknown_function_00B49BD6.md) at `0x00B49BD6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CCB18  48 83 EC 28                     sub rsp, 0x28
004CCB1C  48 8B 81 D0 02 00 00            mov rax, qword ptr [rcx + 0x2d0]
004CCB23  8A 50 10                        mov dl, byte ptr [rax + 0x10]
004CCB26  84 D2                           test dl, dl
004CCB28  78 06                           js 0x1404ccb30
004CCB2A  48 83 C4 28                     add rsp, 0x28
004CCB2E  C3                              ret
004CCB2F  CC                              int3
004CCB30  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
004CCB34  E8 33 D2 18 00                  call 0x140659d6c
004CCB39  EB EF                           jmp 0x1404ccb2a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiIommuUninitializeDeviceAts(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (sign_flag) goto loc_004CCB30;
loc_004CCB2A:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(a1 + 720);
loc_004CCB30:
    result = ExUninitializeDeviceAts(*(unsigned __int64 *)(a1 + 32), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 720) + 16), a3, a4);
    goto loc_004CCB2A;
}
```

## 5. (Beta) C Style

```c
int64_t PiIommuUninitializeDeviceAts(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (sign_flag) goto loc_004CCB30;
loc_004CCB2A:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(arg1 + 0x2D0);
loc_004CCB30:
    result = ExUninitializeDeviceAts(*(uint64_t *)(arg1 + 0x20), *(uint8_t *)(*(uint64_t *)(arg1 + 0x2D0) + 0x10), a3, a4);
    goto loc_004CCB2A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x2D0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CCB18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CCB18[BB_004CCB18]
  bb_004CCB2A[BB_004CCB2A]
  bb_004CCB2F[BB_004CCB2F]
  bb_004CCB30[BB_004CCB30]
  bb_004CCB18 -->|branch| bb_004CCB30
  bb_004CCB18 -->|fallthrough| bb_004CCB2A
  bb_004CCB2F -->|flow| bb_004CCB30
  bb_004CCB30 -->|branch| bb_004CCB2A
```
