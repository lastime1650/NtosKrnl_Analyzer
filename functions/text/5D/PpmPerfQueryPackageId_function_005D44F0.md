# PpmPerfQueryPackageId

- RVA: `0x005D44F0`–`0x005D4505` (길이 `21` bytes)
- VA: `0x00000001405D44F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D44F4` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D44F0  48 83 EC 28                     sub rsp, 0x28
005D44F4  E8 D7 40 D0 FF                  call 0x1402d85d0
005D44F9  8B 80 28 8E 00 00               mov eax, dword ptr [rax + 0x8e28]
005D44FF  48 83 C4 28                     add rsp, 0x28
005D4503  C3                              ret
005D4504  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfQueryPackageId(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeGetPrcb(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(result + 36392));
}
```

## 5. (Beta) C Style

```c
void PpmPerfQueryPackageId(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeGetPrcb(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(result + 0x8E28));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D44F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D44F0[BB_005D44F0]
  bb_005D4504[BB_005D4504]
```
