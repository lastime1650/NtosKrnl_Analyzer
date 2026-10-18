# KiFreeLocalSharedReadyQueue

- RVA: `0x005B7F0C`–`0x005B7F37` (길이 `43` bytes)
- VA: `0x00000001405B7F0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B7F23` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [KiAssignSubNodeSharedReadyQueues](KiAssignSubNodeSharedReadyQueues_function_005B737C.md) at `0x005B75D5`
- [KiStartDynamicProcessor](../../page/74/KiStartDynamicProcessor_function_007456C8.md) at `0x00745C86`
- [KeStartAllProcessors](../../init/C3/KeStartAllProcessors_function_00C36F78.md) at `0x00C3744E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005B7F23` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B7F0C  40 53                           push rbx
005B7F0E  48 83 EC 20                     sub rsp, 0x20
005B7F12  48 8B D9                        mov rbx, rcx
005B7F15  48 8B 89 00 94 00 00            mov rcx, qword ptr [rcx + 0x9400]
005B7F1C  48 85 C9                        test rcx, rcx
005B7F1F  74 0F                           je 0x1405b7f30
005B7F21  33 D2                           xor edx, edx
005B7F23  E8 48 A9 5C 00                  call 0x140b82870
005B7F28  48 83 A3 00 94 00 00 00         and qword ptr [rbx + 0x9400], 0
005B7F30  48 83 C4 20                     add rsp, 0x20
005B7F34  5B                              pop rbx
005B7F35  C3                              ret
005B7F36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiFreeLocalSharedReadyQueue(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 37888) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 37888), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiFreeLocalSharedReadyQueue(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x9400) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x9400), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9400` | `64` | `R` |
| `Arg1` | `+ 0x9400` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B7F0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B7F0C[BB_005B7F0C]
  bb_005B7F21[BB_005B7F21]
  bb_005B7F30[BB_005B7F30]
  bb_005B7F36[BB_005B7F36]
  bb_005B7F0C -->|branch| bb_005B7F30
  bb_005B7F0C -->|fallthrough| bb_005B7F21
  bb_005B7F21 -->|flow| bb_005B7F30
```
