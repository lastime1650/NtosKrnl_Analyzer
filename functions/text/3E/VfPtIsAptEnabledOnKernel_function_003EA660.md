# VfPtIsAptEnabledOnKernel

- RVA: `0x003EA660`–`0x003EA67A` (길이 `26` bytes)
- VA: `0x00000001403EA660`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiAllocateContiguousMemory](MiAllocateContiguousMemory_function_003E9FDC.md) at `0x003EA37C`
- [MiAllocatePagesForMdl](MiAllocatePagesForMdl_function_003EABEC.md) at `0x003EAE10`
- [MmAllocateMappingAddressEx](../../page/A7/MmAllocateMappingAddressEx_function_00A726B0.md) at `0x00A727B2`

### Static image references
- `0x003EA660` → RVA `0x00F04240` (`.data`; read)
- `0x003EA66D` → RVA `0x00F04ABC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EA660  80 3D D9 9B B1 00 00            cmp byte ptr [rip + 0xb19bd9], 0
003EA667  75 04                           jne 0x1403ea66d
003EA669  32 C0                           xor al, al
003EA66B  C3                              ret
003EA66C  CC                              int3
003EA66D  83 3D 48 A4 B1 00 01            cmp dword ptr [rip + 0xb1a448], 1
003EA674  75 F3                           jne 0x1403ea669
003EA676  B0 01                           mov al, 1
003EA678  C3                              ret
003EA679  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfPtIsAptEnabledOnKernel(void)
{
    __int64 result;

    if ((*(unsigned __int8 *)(v_rip + 11639769)) != 0) goto loc_003EA66D;
loc_003EA669:
    result = 0;
    return result;
loc_003EA66D:
    if ((*(unsigned int *)(v_rip + 11641928)) != 1) goto loc_003EA669;
    return 1;
}
```

## 5. (Beta) C Style

```c
void VfPtIsAptEnabledOnKernel(void)
{
    int64_t result;

    if ((*(uint8_t *)(v_rip + 0xB19BD9)) != 0) goto loc_003EA66D;
loc_003EA669:
    result = 0;
    return result;
loc_003EA66D:
    if ((*(uint32_t *)(v_rip + 0xB1A448)) != 1) goto loc_003EA669;
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EA660&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EA660[BB_003EA660]
  bb_003EA669[BB_003EA669]
  bb_003EA66C[BB_003EA66C]
  bb_003EA66D[BB_003EA66D]
  bb_003EA676[BB_003EA676]
  bb_003EA679[BB_003EA679]
  bb_003EA660 -->|branch| bb_003EA66D
  bb_003EA660 -->|fallthrough| bb_003EA669
  bb_003EA66C -->|flow| bb_003EA66D
  bb_003EA66D -->|branch| bb_003EA669
  bb_003EA66D -->|fallthrough| bb_003EA676
```
