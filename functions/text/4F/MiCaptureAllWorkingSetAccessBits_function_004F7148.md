# MiCaptureAllWorkingSetAccessBits

- RVA: `0x004F7148`–`0x004F7161` (길이 `25` bytes)
- VA: `0x00000001404F7148`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004F7156` → [MiQueueWorkingSetRequest](MiQueueWorkingSetRequest_function_004F7168.md) (function, `0x004F7168`)

### Direct callers
- [MmPerformMemoryListCommand](../../pagelk/B7/MmPerformMemoryListCommand_function_00B7D730.md) at `0x00B7D7B6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F7148  48 83 EC 28                     sub rsp, 0x28
004F714C  F7 DA                           neg edx
004F714E  1B D2                           sbb edx, edx
004F7150  83 E2 08                        and edx, 8
004F7153  83 C2 08                        add edx, 8
004F7156  E8 0D 00 00 00                  call 0x1404f7168
004F715B  48 83 C4 28                     add rsp, 0x28
004F715F  C3                              ret
004F7160  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCaptureAllWorkingSetAccessBits(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (unsigned int)(-(a2));
    a2 = (unsigned int)((a2) & (8));
    a2 = (unsigned int)((a2) + (8));
    result = MiQueueWorkingSetRequest(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCaptureAllWorkingSetAccessBits(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (uint32_t)(-(Arg2));
    Arg2 = (uint32_t)((Arg2) & (8));
    Arg2 = (uint32_t)((Arg2) + (8));
    result = MiQueueWorkingSetRequest(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F7148&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F7148[BB_004F7148]
  bb_004F7160[BB_004F7160]
```
