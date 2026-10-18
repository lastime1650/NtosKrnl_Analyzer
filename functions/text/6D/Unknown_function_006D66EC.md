# sub_006D66EC

- RVA: `0x006D66EC`–`0x006D670A` (길이 `30` bytes)
- VA: `0x00000001406D66EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D8E4`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D66FF` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006D6705` → [sub_0020C2D4 + 0x9B8](../20/Unknown_function_0020C2D4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D66EC  8B D0                           mov edx, eax
006D66EE  0F BA F2 15                     btr edx, 0x15
006D66F2  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
006D66F7  75 F3                           jne 0x1406d66ec
006D66F9  0F BA E0 15                     bt eax, 0x15
006D66FD  73 05                           jae 0x1406d6704
006D66FF  E8 CC CA B8 FF                  call 0x1402631d0
006D6704  FB                              sti
006D6705  E9 82 65 B3 FF                  jmp 0x14020cc8c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D66EC(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (condition_is_not_equal) goto loc_006D66EC;
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D66EC(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (condition_is_not_equal) goto loc_006D66EC;
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)(result)), Arg3, a4);
    }
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D66EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D66EC[BB_006D66EC]
  bb_006D66F9[BB_006D66F9]
  bb_006D66FF[BB_006D66FF]
  bb_006D6704[BB_006D6704]
  bb_006D66EC -->|branch| bb_006D66EC
  bb_006D66EC -->|fallthrough| bb_006D66F9
  bb_006D66F9 -->|branch| bb_006D6704
  bb_006D66F9 -->|fallthrough| bb_006D66FF
  bb_006D66FF -->|flow| bb_006D6704
```
