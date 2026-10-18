# KeSubtractAffinityEx2

- RVA: `0x002D5BA0`–`0x002D5BC0` (길이 `32` bytes)
- VA: `0x00000001402D5BA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002D5BAE` → [KiSubtractAffinityEx](KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)
- `0x002D5BB9` → [KiSubtractAffinityExNoResult](../4D/KiSubtractAffinityExNoResult_function_004D99D4.md) (function, `0x004D99D4`)

### Direct callers
- [KiStopProfileTarget](../30/KiStopProfileTarget_function_00304510.md) at `0x003046B8`
- [HalpRemoveProfileSourceFromList](../54/HalpRemoveProfileSourceFromList_function_005477B8.md) at `0x005477F5`
- [KeCpuPartitionMoveCpus](../5C/KeCpuPartitionMoveCpus_function_005C0B70.md) at `0x005C0C40`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E0448`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E045E`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E0477`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E04B4`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0AEF`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0B02`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0B13`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0B23`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0B33`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0B43`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0CB3`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0E58`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0F1C`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E115C`
- [sub_006F962E](../6F/Unknown_function_006F962E.md) at `0x006F9715`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D5BA0  48 83 EC 28                     sub rsp, 0x28
002D5BA4  4D 85 C0                        test r8, r8
002D5BA7  74 10                           je 0x1402d5bb9
002D5BA9  45 0F B7 48 02                  movzx r9d, word ptr [r8 + 2]
002D5BAE  E8 35 06 00 00                  call 0x1402d61e8
002D5BB3  48 83 C4 28                     add rsp, 0x28
002D5BB7  C3                              ret
002D5BB8  CC                              int3
002D5BB9  E8 16 3E 20 00                  call 0x1404d99d4
002D5BBE  EB F3                           jmp 0x1402d5bb3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSubtractAffinityEx2(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_002D5BB9;
    result = KiSubtractAffinityEx(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
loc_002D5BB3:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002D5BB9:
    result = KiSubtractAffinityExNoResult(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
    goto loc_002D5BB3;
}
```

## 5. (Beta) C Style

```c
int64_t KeSubtractAffinityEx2(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_002D5BB9;
    result = KiSubtractAffinityEx(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
loc_002D5BB3:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002D5BB9:
    result = KiSubtractAffinityExNoResult(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
    goto loc_002D5BB3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D5BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D5BA0[BB_002D5BA0]
  bb_002D5BA9[BB_002D5BA9]
  bb_002D5BB3[BB_002D5BB3]
  bb_002D5BB8[BB_002D5BB8]
  bb_002D5BB9[BB_002D5BB9]
  bb_002D5BA0 -->|branch| bb_002D5BB9
  bb_002D5BA0 -->|fallthrough| bb_002D5BA9
  bb_002D5BA9 -->|flow| bb_002D5BB3
  bb_002D5BB8 -->|flow| bb_002D5BB9
  bb_002D5BB9 -->|branch| bb_002D5BB3
```
