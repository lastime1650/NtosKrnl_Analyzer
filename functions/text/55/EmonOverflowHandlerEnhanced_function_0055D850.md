# EmonOverflowHandlerEnhanced

- RVA: `0x0055D850`–`0x0055D886` (길이 `54` bytes)
- VA: `0x000000014055D850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0055D874` → [EmonOverflowHandlerInternalV1Enhanced](EmonOverflowHandlerInternalV1Enhanced_function_0055D88C.md) (function, `0x0055D88C`)
- `0x0055D87B` → [EmonOverflowHandlerInternalV2Enhanced](EmonOverflowHandlerInternalV2Enhanced_function_0055E110.md) (function, `0x0055E110`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0055D85C` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0055D863` → RVA `0x00F8FDE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055D850  48 83 EC 28                     sub rsp, 0x28
0055D854  65 8B 14 25 A4 01 00 00         mov edx, dword ptr gs:[0x1a4]
0055D85C  4C 8D 05 DD B3 A6 00            lea r8, [rip + 0xa6b3dd]
0055D863  83 3D 76 25 A3 00 02            cmp dword ptr [rip + 0xa32576], 2
0055D86A  4D 8B 04 D0                     mov r8, qword ptr [r8 + rdx*8]
0055D86E  73 0B                           jae 0x14055d87b
0055D870  49 8B 50 58                     mov rdx, qword ptr [r8 + 0x58]
0055D874  E8 13 00 00 00                  call 0x14055d88c
0055D879  EB 05                           jmp 0x14055d880
0055D87B  E8 90 08 00 00                  call 0x14055e110
0055D880  48 83 C4 28                     add rsp, 0x28
0055D884  C3                              ret
0055D885  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonOverflowHandlerEnhanced(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 10691958)) >= 2) goto loc_0055D87B;
    result = EmonOverflowHandlerInternalV1Enhanced(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10925021 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) + 88), *(unsigned __int64 *)(v_rip + 10925021 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8), a4);
    goto loc_0055D880;
loc_0055D87B:
    result = EmonOverflowHandlerInternalV2Enhanced(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10925021 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) + 88), *(unsigned __int64 *)(v_rip + 10925021 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8), a4);
loc_0055D880:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void EmonOverflowHandlerEnhanced(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xA32576)) >= 2) goto loc_0055D87B;
    result = EmonOverflowHandlerInternalV1Enhanced(a1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA6B3DD + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) + 0x58), *(uint64_t *)(v_rip + 0xA6B3DD + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8), a4);
    goto loc_0055D880;
loc_0055D87B:
    result = EmonOverflowHandlerInternalV2Enhanced(a1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA6B3DD + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) + 0x58), *(uint64_t *)(v_rip + 0xA6B3DD + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8), a4);
loc_0055D880:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055D850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0055D850[BB_0055D850]
  bb_0055D870[BB_0055D870]
  bb_0055D87B[BB_0055D87B]
  bb_0055D880[BB_0055D880]
  bb_0055D885[BB_0055D885]
  bb_0055D850 -->|branch| bb_0055D87B
  bb_0055D850 -->|fallthrough| bb_0055D870
  bb_0055D870 -->|branch| bb_0055D880
  bb_0055D87B -->|flow| bb_0055D880
```
