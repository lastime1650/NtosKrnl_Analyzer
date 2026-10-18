# RtlpHpSegLockAcquire

- RVA: `0x002E34A0`–`0x002E34BC` (길이 `28` bytes)
- VA: `0x00000001402E34A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002E34B1` → [RtlpHpAcquireLockExclusive](../32/RtlpHpAcquireLockExclusive_function_003246B0.md) (function, `0x003246B0`)

### Direct callers
- [RtlpHpSegPageRangeShrink](RtlpHpSegPageRangeShrink_function_002E2FA0.md) at `0x002E2FE3`
- [RtlpHpSegPageRangeCoalesce](../32/RtlpHpSegPageRangeCoalesce_function_00325860.md) at `0x00325A4F`
- [RtlpHpSegPageRangeAllocate](../32/RtlpHpSegPageRangeAllocate_function_00326790.md) at `0x003267C1`
- [sub_003267E9](../32/Unknown_function_003267E9.md) at `0x003268E7`
- [RtlpHpSegContextCompact](../32/RtlpHpSegContextCompact_function_00326F90.md) at `0x00326FC4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E34A0  48 83 EC 28                     sub rsp, 0x28
002E34A4  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
002E34A7  48 83 C1 40                     add rcx, 0x40
002E34AB  0F B6 D0                        movzx edx, al
002E34AE  83 E2 01                        and edx, 1
002E34B1  E8 FA 11 04 00                  call 0x1403246b0
002E34B6  48 83 C4 28                     add rsp, 0x28
002E34BA  C3                              ret
002E34BB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpSegLockAcquire(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (64);
    a2 = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (1));
    result = RtlpHpAcquireLockExclusive(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpSegLockAcquire(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (64);
    a2 = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (1));
    result = RtlpHpAcquireLockExclusive(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E34A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E34A0[BB_002E34A0]
  bb_002E34BB[BB_002E34BB]
```
