# IommuDomainDelete

- RVA: `0x0070D3C0`–`0x0070D3D8` (길이 `24` bytes)
- VA: `0x000000014070D3C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0070D3CD` → [HalpIommuFreeDmaDomain](../../text/55/HalpIommuFreeDmaDomain_function_005550F8.md) (function, `0x005550F8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0070D3CD` → [HalpIommuFreeDmaDomain](../../text/55/HalpIommuFreeDmaDomain_function_005550F8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070D3C0  48 83 EC 28                     sub rsp, 0x28
0070D3C4  48 85 C9                        test rcx, rcx
0070D3C7  75 04                           jne 0x14070d3cd
0070D3C9  33 C0                           xor eax, eax
0070D3CB  EB 05                           jmp 0x14070d3d2
0070D3CD  E8 26 7D E4 FF                  call 0x1405550f8
0070D3D2  48 83 C4 28                     add rsp, 0x28
0070D3D6  C3                              ret
0070D3D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommuDomainDelete(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_0070D3CD;
    result = 0;
    goto loc_0070D3D2;
loc_0070D3CD:
    result = HalpIommuFreeDmaDomain(a1, a2, a3, a4);
loc_0070D3D2:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IommuDomainDelete(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_0070D3CD;
    result = 0;
    goto loc_0070D3D2;
loc_0070D3CD:
    result = HalpIommuFreeDmaDomain(Arg1, a2, a3, a4);
loc_0070D3D2:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070D3C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070D3C0[BB_0070D3C0]
  bb_0070D3C9[BB_0070D3C9]
  bb_0070D3CD[BB_0070D3CD]
  bb_0070D3D2[BB_0070D3D2]
  bb_0070D3D7[BB_0070D3D7]
  bb_0070D3C0 -->|branch| bb_0070D3CD
  bb_0070D3C0 -->|fallthrough| bb_0070D3C9
  bb_0070D3C9 -->|branch| bb_0070D3D2
  bb_0070D3CD -->|flow| bb_0070D3D2
```
