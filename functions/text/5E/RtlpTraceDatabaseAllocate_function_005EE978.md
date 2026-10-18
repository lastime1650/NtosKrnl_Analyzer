# RtlpTraceDatabaseAllocate

- RVA: `0x005EE978`–`0x005EE999` (길이 `33` bytes)
- VA: `0x00000001405EE978`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005EE98E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [RtlTraceDatabaseCreate](RtlTraceDatabaseCreate_function_005EE5E0.md) at `0x005EE626`
- [RtlpTraceDatabaseInternalAdd](RtlpTraceDatabaseInternalAdd_function_005EE9A0.md) at `0x005EEA43`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005EE98E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EE978  48 83 EC 28                     sub rsp, 0x28
005EE97C  F6 C2 04                        test dl, 4
005EE97F  48 8B D1                        mov rdx, rcx
005EE982  B9 40 00 00 00                  mov ecx, 0x40
005EE987  75 05                           jne 0x1405ee98e
005EE989  B9 00 01 00 00                  mov ecx, 0x100
005EE98E  E8 5D 37 59 00                  call 0x140b820f0
005EE993  48 83 C4 28                     add rsp, 0x28
005EE997  C3                              ret
005EE998  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpTraceDatabaseAllocate(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((a2) & (4)) == 0) {
        a1 = 256;
    }
    result = ExAllocatePool2(a1, a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpTraceDatabaseAllocate(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((Arg2) & (4)) == 0) {
        Arg1 = 256;
    }
    result = ExAllocatePool2(Arg1, Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EE978&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EE978[BB_005EE978]
  bb_005EE989[BB_005EE989]
  bb_005EE98E[BB_005EE98E]
  bb_005EE998[BB_005EE998]
  bb_005EE978 -->|branch| bb_005EE98E
  bb_005EE978 -->|fallthrough| bb_005EE989
  bb_005EE989 -->|flow| bb_005EE98E
```
