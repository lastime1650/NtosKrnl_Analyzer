# EtwpCoverageResetTimerCallback

- RVA: `0x00651D60`–`0x00651D89` (길이 `41` bytes)
- VA: `0x0000000140651D60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00651D7E` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00651D60  48 83 EC 28                     sub rsp, 0x28
00651D64  B9 01 00 00 00                  mov ecx, 1
00651D69  33 C0                           xor eax, eax
00651D6B  F0 0F B1 4A 08                  lock cmpxchg dword ptr [rdx + 8], ecx
00651D70  75 11                           jne 0x140651d83
00651D72  48 8D 8A 98 01 00 00            lea rcx, [rdx + 0x198]
00651D79  BA 03 00 00 00                  mov edx, 3
00651D7E  E8 9D 77 CA FF                  call 0x1402f9520
00651D83  48 83 C4 28                     add rsp, 0x28
00651D87  C3                              ret
00651D88  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCoverageResetTimerCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        a1 = a2 + 408;
        a2 = 3;
        result = ExQueueWorkItem(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCoverageResetTimerCallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        Arg1 = Arg2 + 408;
        Arg2 = 3;
        result = ExQueueWorkItem(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x198` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00651D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00651D60[BB_00651D60]
  bb_00651D72[BB_00651D72]
  bb_00651D83[BB_00651D83]
  bb_00651D88[BB_00651D88]
  bb_00651D60 -->|branch| bb_00651D83
  bb_00651D60 -->|fallthrough| bb_00651D72
  bb_00651D72 -->|flow| bb_00651D83
```
