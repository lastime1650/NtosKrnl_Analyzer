# CmpFreeParseContext

- RVA: `0x008768E0`–`0x008768FF` (길이 `31` bytes)
- VA: `0x00000001408768E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008768EB` → [CmpCleanupParseContext](CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x008768F3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)

### Direct callers
- [CmCreateKey](CmCreateKey_function_00875020.md) at `0x00875475`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008768F3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008768E0  40 53                           push rbx
008768E2  48 83 EC 20                     sub rsp, 0x20
008768E6  33 D2                           xor edx, edx
008768E8  48 8B D9                        mov rbx, rcx
008768EB  E8 20 00 00 00                  call 0x140876910
008768F0  48 8B CB                        mov rcx, rbx
008768F3  E8 88 F4 BF FF                  call 0x140475d80
008768F8  48 83 C4 20                     add rsp, 0x20
008768FC  5B                              pop rbx
008768FD  C3                              ret
008768FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFreeParseContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = CmpCleanupParseContext(a1, a2, a3, a4);
    result = CmSiFreeMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFreeParseContext(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = CmpCleanupParseContext(Arg1, Arg2, a3, a4);
    result = CmSiFreeMemory(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008768E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008768E0[BB_008768E0]
  bb_008768FE[BB_008768FE]
```
