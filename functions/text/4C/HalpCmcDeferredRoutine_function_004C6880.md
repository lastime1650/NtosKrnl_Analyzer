# HalpCmcDeferredRoutine

- RVA: `0x004C6880`–`0x004C68AE` (길이 `46` bytes)
- VA: `0x00000001404C6880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `13`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C68A7` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C6880  48 83 EC 28                     sub rsp, 0x28
004C6884  41 B8 01 00 00 00               mov r8d, 1
004C688A  41 8B C0                        mov eax, r8d
004C688D  87 82 A8 00 00 00               xchg dword ptr [rdx + 0xa8], eax
004C6893  85 C0                           test eax, eax
004C6895  74 06                           je 0x1404c689d
004C6897  48 83 C4 28                     add rsp, 0x28
004C689B  C3                              ret
004C689C  CC                              int3
004C689D  48 8D 8A 88 00 00 00            lea rcx, [rdx + 0x88]
004C68A4  41 8B D0                        mov edx, r8d
004C68A7  E8 74 2C E3 FF                  call 0x1402f9520
004C68AC  EB E9                           jmp 0x1404c6897
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCmcDeferredRoutine(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (1 == 0) goto loc_004C689D;
loc_004C6897:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_004C689D:
    result = ExQueueWorkItem(a2 + 136, 1, 1, a4);
    goto loc_004C6897;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCmcDeferredRoutine(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (1 == 0) goto loc_004C689D;
loc_004C6897:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_004C689D:
    result = ExQueueWorkItem(Arg2 + 136, 1, 1, a4);
    goto loc_004C6897;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x88` | `64` | `R` |
| `Arg2` | `+ 0xA8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C6880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C6880[BB_004C6880]
  bb_004C6897[BB_004C6897]
  bb_004C689C[BB_004C689C]
  bb_004C689D[BB_004C689D]
  bb_004C6880 -->|branch| bb_004C689D
  bb_004C6880 -->|fallthrough| bb_004C6897
  bb_004C689C -->|flow| bb_004C689D
  bb_004C689D -->|branch| bb_004C6897
```
