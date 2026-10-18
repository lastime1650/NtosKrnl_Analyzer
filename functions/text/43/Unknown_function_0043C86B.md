# sub_0043C86B

- RVA: `0x0043C86B`–`0x0043C88C` (길이 `33` bytes)
- VA: `0x000000014043C86B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A45B4`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0043C885` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0043C883` → [sub_0043C846 + 0x15](Unknown_function_0043C846.md) (`tail-transfer`)
  - `0x0043C88A` → [sub_0043C846 + 0x15](Unknown_function_0043C846.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0043C86B  41 0F 0D 08                     prefetchw byte ptr [r8]
0043C86F  41 8B 00                        mov eax, dword ptr [r8]
0043C872  8B D0                           mov edx, eax
0043C874  0F BA F2 15                     btr edx, 0x15
0043C878  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0043C87D  75 F3                           jne 0x14043c872
0043C87F  0F BA E0 15                     bt eax, 0x15
0043C883  73 D6                           jae 0x14043c85b
0043C885  E8 46 69 E2 FF                  call 0x1402631d0
0043C88A  EB CF                           jmp 0x14043c85b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0043C86B(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

loc_0043C872:
    if (condition_is_not_equal) goto loc_0043C872;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0043C86B(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

loc_0043C872:
    if (condition_is_not_equal) goto loc_0043C872;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043C86B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043C86B[BB_0043C86B]
  bb_0043C872[BB_0043C872]
  bb_0043C87F[BB_0043C87F]
  bb_0043C885[BB_0043C885]
  bb_0043C86B -->|flow| bb_0043C872
  bb_0043C872 -->|branch| bb_0043C872
  bb_0043C872 -->|fallthrough| bb_0043C87F
  bb_0043C87F -->|fallthrough| bb_0043C885
```
