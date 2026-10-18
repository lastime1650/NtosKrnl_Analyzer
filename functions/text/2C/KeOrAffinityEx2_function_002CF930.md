# KeOrAffinityEx2

- RVA: `0x002CF930`–`0x002CF950` (길이 `32` bytes)
- VA: `0x00000001402CF930`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002CF93E` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x002CF949` → [KiOrAffinityExNoResult](../4D/KiOrAffinityExNoResult_function_004D70BC.md) (function, `0x004D70BC`)

### Direct callers
- [KeQueryLogicalProcessorRelationship](KeQueryLogicalProcessorRelationship_function_002CEA60.md) at `0x002CF26C`
- [KeQueryLogicalProcessorRelationship](KeQueryLogicalProcessorRelationship_function_002CEA60.md) at `0x002CF50C`
- [KiTryPopulateLogicalProcessorInformation](KiTryPopulateLogicalProcessorInformation_function_002CF724.md) at `0x002CF795`
- [KiForwardTick](../39/KiForwardTick_function_0039D40C.md) at `0x0039D64D`
- [KiQueryCpuPartitionAffinityProcess](../3C/KiQueryCpuPartitionAffinityProcess_function_003C01A0.md) at `0x003C021D`
- [EmonAddProfileSource](../55/EmonAddProfileSource_function_0055BEA0.md) at `0x0055C05A`
- [Amd64AddProfileSource](../56/Amd64AddProfileSource_function_0056B720.md) at `0x0056B8D6`
- [KeCpuPartitionMoveCpus](../5C/KeCpuPartitionMoveCpus_function_005C0B70.md) at `0x005C0C82`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E0489`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E049B`
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E04C6`
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E0F3D`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressManagerUpdateTopology](../60/SMKM_STORE_MGR_SM_TRAITS_SmCompressManagerUpdateTopology_function_0060C634.md) at `0x0060C6B6`
- [PsInitializeBootCpuPartitions](../../init/C4/PsInitializeBootCpuPartitions_function_00C44D94.md) at `0x00C45047`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CF930  48 83 EC 28                     sub rsp, 0x28
002CF934  4D 85 C0                        test r8, r8
002CF937  74 10                           je 0x1402cf949
002CF939  45 0F B7 48 02                  movzx r9d, word ptr [r8 + 2]
002CF93E  E8 09 AF 0C 00                  call 0x14039a84c
002CF943  48 83 C4 28                     add rsp, 0x28
002CF947  C3                              ret
002CF948  CC                              int3
002CF949  E8 6E 77 20 00                  call 0x1404d70bc
002CF94E  EB F3                           jmp 0x1402cf943
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeOrAffinityEx2(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_002CF949;
    result = KiOrAffinityEx(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
loc_002CF943:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002CF949:
    result = KiOrAffinityExNoResult(a1, a2, a3, *(unsigned __int16 *)(a3 + 2));
    goto loc_002CF943;
}
```

## 5. (Beta) C Style

```c
int64_t KeOrAffinityEx2(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_002CF949;
    result = KiOrAffinityEx(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
loc_002CF943:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002CF949:
    result = KiOrAffinityExNoResult(Arg1, Arg2, Arg3, *(uint16_t *)(Arg3 + 0x2));
    goto loc_002CF943;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CF930&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CF930[BB_002CF930]
  bb_002CF939[BB_002CF939]
  bb_002CF943[BB_002CF943]
  bb_002CF948[BB_002CF948]
  bb_002CF949[BB_002CF949]
  bb_002CF930 -->|branch| bb_002CF949
  bb_002CF930 -->|fallthrough| bb_002CF939
  bb_002CF939 -->|flow| bb_002CF943
  bb_002CF948 -->|flow| bb_002CF949
  bb_002CF949 -->|branch| bb_002CF943
```
