# sub_002E3461

- RVA: `0x002E3461`–`0x002E3489` (길이 `40` bytes)
- VA: `0x00000001402E3461`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070E60`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002E347F` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002E3479` → [sub_002E3191 + 0xEB](Unknown_function_002E3191.md) (`tail-transfer`)
  - `0x002E3484` → [sub_002E3191 + 0xEB](Unknown_function_002E3191.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E3461  41 0F 0D 08                     prefetchw byte ptr [r8]
002E3465  41 8B 00                        mov eax, dword ptr [r8]
002E3468  8B D0                           mov edx, eax
002E346A  0F BA F2 15                     btr edx, 0x15
002E346E  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002E3473  75 F3                           jne 0x1402e3468
002E3475  0F BA E0 15                     bt eax, 0x15
002E3479  0F 83 FD FD FF FF               jae 0x1402e327c
002E347F  E8 4C FD F7 FF                  call 0x1402631d0
002E3484  E9 F3 FD FF FF                  jmp 0x1402e327c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E3461(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

loc_002E3468:
    if (condition_is_not_equal) goto loc_002E3468;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E3461(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

loc_002E3468:
    if (condition_is_not_equal) goto loc_002E3468;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))), Arg3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `8` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E3461&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E3461[BB_002E3461]
  bb_002E3468[BB_002E3468]
  bb_002E3475[BB_002E3475]
  bb_002E347F[BB_002E347F]
  bb_002E3461 -->|flow| bb_002E3468
  bb_002E3468 -->|branch| bb_002E3468
  bb_002E3468 -->|fallthrough| bb_002E3475
  bb_002E3475 -->|fallthrough| bb_002E347F
```
