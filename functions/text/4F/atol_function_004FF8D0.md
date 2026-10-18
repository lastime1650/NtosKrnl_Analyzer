# atol

- RVA: `0x004FF8D0`–`0x004FF8F2` (길이 `34` bytes)
- VA: `0x00000001404FF8D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FF8E7` → [strtolX](strtolX_function_004FF388.md) (function, `0x004FF388`)

### Direct callers
- [atoi](atoi_function_004FF8B0.md) at `0x004FF8B4`
- [HvlDebuggerSupportInitialize](../58/HvlDebuggerSupportInitialize_function_00583790.md) at `0x00583925`
- [HvlDebuggerSupportInitialize](../58/HvlDebuggerSupportInitialize_function_00583790.md) at `0x005839AA`
- [HvlDebuggerSupportInitialize](../58/HvlDebuggerSupportInitialize_function_00583790.md) at `0x005839D1`
- [HvlDebuggerSupportInitialize](../58/HvlDebuggerSupportInitialize_function_00583790.md) at `0x005839F4`
- [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) at `0x00B8601F`
- [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1B380`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1C850`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1C898`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CE07`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CF2C`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CF63`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CF9A`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CFD9`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D010`
- [RamdiskStart](../../init/C6/RamdiskStart_function_00C6EF68.md) at `0x00C6F0FE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FF8D0  48 83 EC 28                     sub rsp, 0x28
004FF8D4  48 85 C9                        test rcx, rcx
004FF8D7  75 04                           jne 0x1404ff8dd
004FF8D9  33 C0                           xor eax, eax
004FF8DB  EB 0F                           jmp 0x1404ff8ec
004FF8DD  33 D2                           xor edx, edx
004FF8DF  44 8D 4A 01                     lea r9d, [rdx + 1]
004FF8E3  44 8D 42 0A                     lea r8d, [rdx + 0xa]
004FF8E7  E8 9C FA FF FF                  call 0x1404ff388
004FF8EC  48 83 C4 28                     add rsp, 0x28
004FF8F0  C3                              ret
004FF8F1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall atol(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_004FF8DD;
    result = 0;
    goto loc_004FF8EC;
loc_004FF8DD:
    a2 = 0;
    result = strtolX(a1, a2, a2 + 10, a2 + 1);
loc_004FF8EC:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t atol(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_004FF8DD;
    result = 0;
    goto loc_004FF8EC;
loc_004FF8DD:
    Arg2 = 0;
    result = strtolX(Arg1, Arg2, Arg2 + 10, Arg2 + 1);
loc_004FF8EC:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF8D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF8D0[BB_004FF8D0]
  bb_004FF8D9[BB_004FF8D9]
  bb_004FF8DD[BB_004FF8DD]
  bb_004FF8EC[BB_004FF8EC]
  bb_004FF8F1[BB_004FF8F1]
  bb_004FF8D0 -->|branch| bb_004FF8DD
  bb_004FF8D0 -->|fallthrough| bb_004FF8D9
  bb_004FF8D9 -->|branch| bb_004FF8EC
  bb_004FF8DD -->|flow| bb_004FF8EC
```
