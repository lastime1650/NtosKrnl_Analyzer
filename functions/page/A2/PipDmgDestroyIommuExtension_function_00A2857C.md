# PipDmgDestroyIommuExtension

- RVA: `0x00A2857C`–`0x00A285A7` (길이 `43` bytes)
- VA: `0x0000000140A2857C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC084`
- 디코드: `13`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A28598` → [PiIommuFreeExtension](../74/PiIommuFreeExtension_function_007401D8.md) (function, `0x007401D8`)

### Direct callers
- [PiProcessNewDeviceNode](PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A2A149`
- [sub_00B347A2](../B3/Unknown_function_00B347A2.md) at `0x00B3485C`
- [sub_00B49BD6](../B4/Unknown_function_00B49BD6.md) at `0x00B49C8D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2857C  40 53                           push rbx
00A2857E  48 83 EC 20                     sub rsp, 0x20
00A28582  48 8B D9                        mov rbx, rcx
00A28585  48 8B 89 D0 02 00 00            mov rcx, qword ptr [rcx + 0x2d0]
00A2858C  48 85 C9                        test rcx, rcx
00A2858F  75 07                           jne 0x140a28598
00A28591  48 83 C4 20                     add rsp, 0x20
00A28595  5B                              pop rbx
00A28596  C3                              ret
00A28597  CC                              int3
00A28598  E8 3B 7C D1 FF                  call 0x1407401d8
00A2859D  48 83 A3 D0 02 00 00 00         and qword ptr [rbx + 0x2d0], 0
00A285A5  EB EA                           jmp 0x140a28591
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipDmgDestroyIommuExtension(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 720) != 0) goto loc_00A28598;
loc_00A28591:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A28598:
    result = PiIommuFreeExtension(*(unsigned __int64 *)(a1 + 720), a2, a3, a4);
    goto loc_00A28591;
}
```

## 5. (Beta) C Style

```c
int64_t PipDmgDestroyIommuExtension(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x2D0) != 0) goto loc_00A28598;
loc_00A28591:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A28598:
    result = PiIommuFreeExtension(*(uint64_t *)(arg1 + 0x2D0), a2, a3, a4);
    goto loc_00A28591;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2D0` | `64` | `R` |
| `Arg1` | `+ 0x2D0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2857C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2857C[BB_00A2857C]
  bb_00A28591[BB_00A28591]
  bb_00A28597[BB_00A28597]
  bb_00A28598[BB_00A28598]
  bb_00A2857C -->|branch| bb_00A28598
  bb_00A2857C -->|fallthrough| bb_00A28591
  bb_00A28597 -->|flow| bb_00A28598
  bb_00A28598 -->|branch| bb_00A28591
```
