# PopFxWorkOrderWatchdog

- RVA: `0x005D3A40`–`0x005D3A61` (길이 `33` bytes)
- VA: `0x00000001405D3A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E574`
- 디코드: `9`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D3A5B` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D3A40  48 83 EC 28                     sub rsp, 0x28
005D3A44  45 33 C0                        xor r8d, r8d
005D3A47  48 85 D2                        test rdx, rdx
005D3A4A  74 07                           je 0x1405d3a53
005D3A4C  4C 8B 82 A8 00 00 00            mov r8, qword ptr [rdx + 0xa8]
005D3A53  45 33 C9                        xor r9d, r9d
005D3A56  B9 18 06 00 00                  mov ecx, 0x618
005D3A5B  E8 0C C2 CE FF                  call 0x1402bfc6c
005D3A60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxWorkOrderWatchdog(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2 + 168);
    }
    a4 = 0;
    result = PopFxBugCheck((unsigned int)(0x618ULL), a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxWorkOrderWatchdog(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2 + 0xA8);
    }
    Arg4 = 0;
    result = PopFxBugCheck((uint32_t)(0x618ULL), Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D3A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D3A40[BB_005D3A40]
  bb_005D3A4C[BB_005D3A4C]
  bb_005D3A53[BB_005D3A53]
  bb_005D3A40 -->|branch| bb_005D3A53
  bb_005D3A40 -->|fallthrough| bb_005D3A4C
  bb_005D3A4C -->|flow| bb_005D3A53
```
