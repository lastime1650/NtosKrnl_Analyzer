# Amd64OverflowHandler

- RVA: `0x0056D310`–`0x0056D32A` (길이 `26` bytes)
- VA: `0x000000014056D310`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0056D31F` → [Amd64OverflowHandlerInternal](Amd64OverflowHandlerInternal_function_0056D330.md) (function, `0x0056D330`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056D310  48 83 EC 28                     sub rsp, 0x28
0056D314  65 8B 14 25 A4 01 00 00         mov edx, dword ptr gs:[0x1a4]
0056D31C  4C 8B C1                        mov r8, rcx
0056D31F  E8 0C 00 00 00                  call 0x14056d330
0056D324  48 83 C4 28                     add rsp, 0x28
0056D328  C3                              ret
0056D329  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64OverflowHandler(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = Amd64OverflowHandlerInternal(a1, (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))), a1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64OverflowHandler(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Amd64OverflowHandlerInternal(Arg1, (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))), Arg1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056D310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056D310[BB_0056D310]
  bb_0056D329[BB_0056D329]
```
