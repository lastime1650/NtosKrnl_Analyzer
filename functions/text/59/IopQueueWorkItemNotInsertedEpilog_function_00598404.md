# IopQueueWorkItemNotInsertedEpilog

- RVA: `0x00598404`–`0x0059843F` (길이 `59` bytes)
- VA: `0x0000000140598404`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0059841B` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0059842E` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [IoQueueWorkItemToNode](../43/IoQueueWorkItemToNode_function_0043C960.md) at `0x0043C9A0`
- [IoTryQueueWorkItem](../4E/IoTryQueueWorkItem_function_004E8390.md) at `0x004E83CF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00598404  40 53                           push rbx
00598406  48 83 EC 20                     sub rsp, 0x20
0059840A  48 83 61 58 00                  and qword ptr [rcx + 0x58], 0
0059840F  48 8B D9                        mov rbx, rcx
00598412  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00598416  BA 44 66 6C 74                  mov edx, 0x746c6644
0059841B  E8 C0 F4 D5 FF                  call 0x1402f78e0
00598420  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00598424  48 85 C9                        test rcx, rcx
00598427  74 0F                           je 0x140598438
00598429  BA 44 66 6C 74                  mov edx, 0x746c6644
0059842E  E8 AD F4 D5 FF                  call 0x1402f78e0
00598433  48 83 63 38 00                  and qword ptr [rbx + 0x38], 0
00598438  48 83 C4 20                     add rsp, 0x20
0059843C  5B                              pop rbx
0059843D  C3                              ret
0059843E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopQueueWorkItemNotInsertedEpilog(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 40), (unsigned int)(0x746C6644ULL), a3, a4);
    if (*(unsigned __int64 *)(a1 + 56) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 56), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopQueueWorkItemNotInsertedEpilog(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x28), (uint32_t)(0x746C6644ULL), a3, a4);
    if (*(uint64_t *)(arg1 + 0x38) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x38), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R/W` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00598404&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00598404[BB_00598404]
  bb_00598429[BB_00598429]
  bb_00598438[BB_00598438]
  bb_0059843E[BB_0059843E]
  bb_00598404 -->|branch| bb_00598438
  bb_00598404 -->|fallthrough| bb_00598429
  bb_00598429 -->|flow| bb_00598438
```
