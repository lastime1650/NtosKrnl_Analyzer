# KeReenterRetpolinedCode

- RVA: `0x0044EE40`–`0x0044EE5D` (길이 `29` bytes)
- VA: `0x000000014044EE40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044EE56` → [KxReenterRetpolinedCode](KxReenterRetpolinedCode_function_0044EE64.md) (function, `0x0044EE64`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044EE40  48 83 EC 28                     sub rsp, 0x28
0044EE44  65 8A 04 25 5E 08 00 00         mov al, byte ptr gs:[0x85e]
0044EE4C  A8 01                           test al, 1
0044EE4E  75 06                           jne 0x14044ee56
0044EE50  48 83 C4 28                     add rsp, 0x28
0044EE54  C3                              ret
0044EE55  CC                              int3
0044EE56  E8 09 00 00 00                  call 0x14044ee64
0044EE5B  EB F3                           jmp 0x14044ee50
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReenterRetpolinedCode(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 2142)))) & (1)) != 0) goto loc_0044EE56;
loc_0044EE50:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int8 *)(gs_base + (0 + 2142));
loc_0044EE56:
    result = KxReenterRetpolinedCode(a1, a2, a3, a4);
    goto loc_0044EE50;
}
```

## 5. (Beta) C Style

```c
void KeReenterRetpolinedCode(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(*(uint8_t *)(gs_base + (0 + 0x85E)))) & (1)) != 0) goto loc_0044EE56;
loc_0044EE50:
    local_rsp = (local_rsp) + (40);
    return *(uint8_t *)(gs_base + (0 + 0x85E));
loc_0044EE56:
    result = KxReenterRetpolinedCode(a1, a2, a3, a4);
    goto loc_0044EE50;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044EE40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044EE40[BB_0044EE40]
  bb_0044EE50[BB_0044EE50]
  bb_0044EE55[BB_0044EE55]
  bb_0044EE56[BB_0044EE56]
  bb_0044EE40 -->|branch| bb_0044EE56
  bb_0044EE40 -->|fallthrough| bb_0044EE50
  bb_0044EE55 -->|flow| bb_0044EE56
  bb_0044EE56 -->|branch| bb_0044EE50
```
