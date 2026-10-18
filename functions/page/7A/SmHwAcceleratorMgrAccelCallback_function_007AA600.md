# SmHwAcceleratorMgrAccelCallback

- RVA: `0x007AA600`–`0x007AA61F` (길이 `31` bytes)
- VA: `0x00000001407AA600`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007AA614` → [SmHwAcceleratorMgrHotRemoveAccelerator](../../text/61/SmHwAcceleratorMgrHotRemoveAccelerator_function_006115FC.md) (function, `0x006115FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007AA614` → [SmHwAcceleratorMgrHotRemoveAccelerator](../../text/61/SmHwAcceleratorMgrHotRemoveAccelerator_function_006115FC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007AA600  48 83 EC 28                     sub rsp, 0x28
007AA604  83 79 04 01                     cmp dword ptr [rcx + 4], 1
007AA608  48 8B C2                        mov rax, rdx
007AA60B  75 0C                           jne 0x1407aa619
007AA60D  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
007AA611  48 8B C8                        mov rcx, rax
007AA614  E8 E3 6F E6 FF                  call 0x1406115fc
007AA619  48 83 C4 28                     add rsp, 0x28
007AA61D  C3                              ret
007AA61E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmHwAcceleratorMgrAccelCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a2;
    if ((*(unsigned int *)(a1 + 4)) == 1) {
        a2 = *(unsigned __int64 *)(a1 + 16);
        a1 = a2;
        result = SmHwAcceleratorMgrHotRemoveAccelerator(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmHwAcceleratorMgrAccelCallback(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg2;
    if ((*(uint32_t *)(arg1 + 0x4)) == 1) {
        Arg2 = *(uint64_t *)(arg1 + 0x10);
        Arg1 = Arg2;
        result = SmHwAcceleratorMgrHotRemoveAccelerator(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007AA600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007AA600[BB_007AA600]
  bb_007AA60D[BB_007AA60D]
  bb_007AA619[BB_007AA619]
  bb_007AA61E[BB_007AA61E]
  bb_007AA600 -->|branch| bb_007AA619
  bb_007AA600 -->|fallthrough| bb_007AA60D
  bb_007AA60D -->|flow| bb_007AA619
```
