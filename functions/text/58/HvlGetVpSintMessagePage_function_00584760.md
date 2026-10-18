# HvlGetVpSintMessagePage

- RVA: `0x00584760`–`0x0058477A` (길이 `26` bytes)
- VA: `0x0000000140584760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00584764` → [HvlGetLpIndexFromProcessorIndex](../44/HvlGetLpIndexFromProcessorIndex_function_0044FFE0.md) (function, `0x0044FFE0`)
- `0x0058476B` → [HvlpGetLpcbByLpIndex](../44/HvlpGetLpcbByLpIndex_function_0044FFA0.md) (function, `0x0044FFA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00584760  48 83 EC 28                     sub rsp, 0x28
00584764  E8 77 B8 EC FF                  call 0x14044ffe0
00584769  8B C8                           mov ecx, eax
0058476B  E8 30 B8 EC FF                  call 0x14044ffa0
00584770  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00584774  48 83 C4 28                     add rsp, 0x28
00584778  C3                              ret
00584779  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlGetVpSintMessagePage(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HvlGetLpIndexFromProcessorIndex(a1, a2, a3, a4);
    result = HvlpGetLpcbByLpIndex((unsigned int)((unsigned int)(result)), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(result + 32);
}
```

## 5. (Beta) C Style

```c
void HvlGetVpSintMessagePage(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HvlGetLpIndexFromProcessorIndex(a1, a2, a3, a4);
    result = HvlpGetLpcbByLpIndex((uint32_t)((uint32_t)(result)), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(result + 0x20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00584760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00584760[BB_00584760]
  bb_00584779[BB_00584779]
```
