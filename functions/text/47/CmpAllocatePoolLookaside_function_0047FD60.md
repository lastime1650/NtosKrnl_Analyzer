# CmpAllocatePoolLookaside

- RVA: `0x0047FD60`–`0x0047FD7B` (길이 `27` bytes)
- VA: `0x000000014047FD60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0047FD70` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0047FD70` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047FD60  48 83 EC 28                     sub rsp, 0x28
0047FD64  83 F9 01                        cmp ecx, 1
0047FD67  74 02                           je 0x14047fd6b
0047FD69  CD 2C                           int 0x2c
0047FD6B  B9 00 01 00 00                  mov ecx, 0x100
0047FD70  E8 7B 23 70 00                  call 0x140b820f0
0047FD75  48 83 C4 28                     add rsp, 0x28
0047FD79  C3                              ret
0047FD7A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAllocatePoolLookaside(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 1) {
    }
    result = ExAllocatePool2(256, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpAllocatePoolLookaside(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 1) {
    }
    result = ExAllocatePool2(256, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047FD60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047FD60[BB_0047FD60]
  bb_0047FD69[BB_0047FD69]
  bb_0047FD6B[BB_0047FD6B]
  bb_0047FD7A[BB_0047FD7A]
  bb_0047FD60 -->|branch| bb_0047FD6B
  bb_0047FD60 -->|fallthrough| bb_0047FD69
  bb_0047FD69 -->|flow| bb_0047FD6B
```
