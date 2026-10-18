# KeXorAffinityEx2

- RVA: `0x002D5B70`–`0x002D5B90` (길이 `32` bytes)
- VA: `0x00000001402D5B70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002D5B7E` → [KiXorAffinityEx](KiXorAffinityEx_function_002D62D0.md) (function, `0x002D62D0`)
- `0x002D5B89` → [KiXorAffinityExNoResult](../4D/KiXorAffinityExNoResult_function_004D9CA0.md) (function, `0x004D9CA0`)

### Direct callers
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004F0024`
- [PpmHeteroDistributeUtilityEx](../4E/PpmHeteroDistributeUtilityEx_function_004EFC00.md) at `0x004F014F`
- [PpmParkDistributeUtilityEx](../4F/PpmParkDistributeUtilityEx_function_004F020C.md) at `0x004F0775`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D5B70  48 83 EC 28                     sub rsp, 0x28
002D5B74  4D 85 C0                        test r8, r8
002D5B77  74 10                           je 0x1402d5b89
002D5B79  45 0F B7 48 02                  movzx r9d, word ptr [r8 + 2]
002D5B7E  E8 4D 07 00 00                  call 0x1402d62d0
002D5B83  48 83 C4 28                     add rsp, 0x28
002D5B87  C3                              ret
002D5B88  CC                              int3
002D5B89  E8 12 41 20 00                  call 0x1404d9ca0
002D5B8E  EB F3                           jmp 0x1402d5b83
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeXorAffinityEx2(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_002D5B89;
    result = KiXorAffinityEx(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
loc_002D5B83:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002D5B89:
    result = KiXorAffinityExNoResult(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
    goto loc_002D5B83;
}
```

## 5. (Beta) C Style

```c
int64_t KeXorAffinityEx2(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_002D5B89;
    result = KiXorAffinityEx(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
loc_002D5B83:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002D5B89:
    result = KiXorAffinityExNoResult(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
    goto loc_002D5B83;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D5B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D5B70[BB_002D5B70]
  bb_002D5B79[BB_002D5B79]
  bb_002D5B83[BB_002D5B83]
  bb_002D5B88[BB_002D5B88]
  bb_002D5B89[BB_002D5B89]
  bb_002D5B70 -->|branch| bb_002D5B89
  bb_002D5B70 -->|fallthrough| bb_002D5B79
  bb_002D5B79 -->|flow| bb_002D5B83
  bb_002D5B88 -->|flow| bb_002D5B89
  bb_002D5B89 -->|branch| bb_002D5B83
```
