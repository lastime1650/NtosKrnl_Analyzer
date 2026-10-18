# MmAllocateMappingAddress

- RVA: `0x00A72690`–`0x00A726A2` (길이 `18` bytes)
- VA: `0x0000000140A72690`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A72697` → [MmAllocateMappingAddressEx](MmAllocateMappingAddressEx_function_00A726B0.md) (function, `0x00A726B0`)

### Direct callers
- [SmFpPreAllocate](../../text/4C/SmFpPreAllocate_function_004CF32C.md) at `0x004CF46A`
- [HvlpInitializeHvCrashdump](../../text/58/HvlpInitializeHvCrashdump_function_0058BCCC.md) at `0x0058BEC0`
- [DifMmAllocateMappingAddressWrapper](../../text/63/DifMmAllocateMappingAddressWrapper_function_006343F0.md) at `0x006344C4`
- [HalpDmaAllocateEmergencyResources](../../init/C2/HalpDmaAllocateEmergencyResources_function_00C2075C.md) at `0x00C207F3`
- [HalpDmaAllocateEmergencyResources](../../init/C2/HalpDmaAllocateEmergencyResources_function_00C2075C.md) at `0x00C2081E`
- [HalpDmaAllocateReservedMapping](../../init/C2/HalpDmaAllocateReservedMapping_function_00C20A18.md) at `0x00C20A3E`
- [PspIumInitialize](../../init/C4/PspIumInitialize_function_00C467A8.md) at `0x00C467E1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A72690  48 83 EC 28                     sub rsp, 0x28
00A72694  45 33 C0                        xor r8d, r8d
00A72697  E8 14 00 00 00                  call 0x140a726b0
00A7269C  48 83 C4 28                     add rsp, 0x28
00A726A0  C3                              ret
00A726A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateMappingAddress(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    result = MmAllocateMappingAddressEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateMappingAddress(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    result = MmAllocateMappingAddressEx(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A72690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A72690[BB_00A72690]
  bb_00A726A1[BB_00A726A1]
```
