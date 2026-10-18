# RtlpAllocateSecondLevelDir

- RVA: `0x0048C520`–`0x0048C544` (길이 `36` bytes)
- VA: `0x000000014048C520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048C539` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [RtlExpandHashTable](../41/RtlExpandHashTable_function_0041D3A0.md) at `0x0041D526`
- [RtlpCreateHashTable](RtlpCreateHashTable_function_0048C400.md) at `0x0048C48B`
- [sub_006F647C](../6F/Unknown_function_006F647C.md) at `0x006F6486`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0048C539` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048C520  48 83 EC 28                     sub rsp, 0x28
0048C524  83 C1 07                        add ecx, 7
0048C527  BA 10 00 00 00                  mov edx, 0x10
0048C52C  D3 E2                           shl edx, cl
0048C52E  41 B8 48 54 61 62               mov r8d, 0x62615448
0048C534  B9 40 00 00 00                  mov ecx, 0x40
0048C539  E8 B2 5B 6F 00                  call 0x140b820f0
0048C53E  48 83 C4 28                     add rsp, 0x28
0048C542  C3                              ret
0048C543  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAllocateSecondLevelDir(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)((a1) + (7));
    a2 = (unsigned int)((16) << ((unsigned __int8)(a1)));
    result = ExAllocatePool2(64, a2, (unsigned int)(0x62615448ULL), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAllocateSecondLevelDir(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)((Arg1) + (7));
    a2 = (uint32_t)((16) << ((uint8_t)(Arg1)));
    result = ExAllocatePool2(64, a2, (uint32_t)(0x62615448ULL), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048C520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048C520[BB_0048C520]
  bb_0048C543[BB_0048C543]
```
