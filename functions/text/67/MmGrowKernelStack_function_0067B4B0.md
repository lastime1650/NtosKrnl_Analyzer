# MmGrowKernelStack

- RVA: `0x0067B4B0`–`0x0067B4C5` (길이 `21` bytes)
- VA: `0x000000014067B4B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0067B4BA` → [MmGrowKernelStackEx](../2A/MmGrowKernelStackEx_function_002A04E0.md) (function, `0x002A04E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0067B4B4` → RVA `0x00FC51B4` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067B4B0  48 83 EC 28                     sub rsp, 0x28
0067B4B4  8B 15 FA 9C 94 00               mov edx, dword ptr [rip + 0x949cfa]
0067B4BA  E8 21 50 C2 FF                  call 0x1402a04e0
0067B4BF  48 83 C4 28                     add rsp, 0x28
0067B4C3  C3                              ret
0067B4C4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmGrowKernelStack(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MmGrowKernelStackEx(a1, (unsigned int)(*(unsigned int *)(v_rip + 9739514)), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmGrowKernelStack(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MmGrowKernelStackEx(a1, (uint32_t)(*(uint32_t *)(v_rip + 0x949CFA)), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067B4B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0067B4B0[BB_0067B4B0]
  bb_0067B4C4[BB_0067B4C4]
```
