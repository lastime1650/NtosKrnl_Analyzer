# IovUtilMarkDeviceObject

- RVA: `0x004B77B0`–`0x004B77CA` (길이 `26` bytes)
- VA: `0x00000001404B77B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B77C3` → [IovpUtilMarkDeviceObject](../../pagevrfy/BA/IovpUtilMarkDeviceObject_function_00BA2D5C.md) (function, `0x00BA2D5C`)

### Direct callers
- [IovUtilMarkStack](IovUtilMarkStack_function_004B7734.md) at `0x004B774E`
- [IovUtilMarkStack](IovUtilMarkStack_function_004B7734.md) at `0x004B777E`
- [IovUtilMarkStack](IovUtilMarkStack_function_004B7734.md) at `0x004B779E`
- [VfIoDeleteDevice](../../pagevrfy/BA/VfIoDeleteDevice_function_00BA221C.md) at `0x00BA22B1`
- [ViPnpVerifyMinorWasProcessedProperly](../../pagevrfy/BB/ViPnpVerifyMinorWasProcessedProperly_function_00BB5BC0.md) at `0x00BB5D26`

### Static image references
- `0x004B77B4` → RVA `0x00F048E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004B77C3` → [IovpUtilMarkDeviceObject](../../pagevrfy/BA/IovpUtilMarkDeviceObject_function_00BA2D5C.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B77B0  48 83 EC 28                     sub rsp, 0x28
004B77B4  83 3D 25 D1 A4 00 00            cmp dword ptr [rip + 0xa4d125], 0
004B77BB  75 06                           jne 0x1404b77c3
004B77BD  48 83 C4 28                     add rsp, 0x28
004B77C1  C3                              ret
004B77C2  CC                              int3
004B77C3  E8 94 B5 6E 00                  call 0x140ba2d5c
004B77C8  EB F3                           jmp 0x1404b77bd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovUtilMarkDeviceObject(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 10801445)) != 0) goto loc_004B77C3;
loc_004B77BD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004B77C3:
    result = IovpUtilMarkDeviceObject(a1, a2, a3, a4);
    goto loc_004B77BD;
}
```

## 5. (Beta) C Style

```c
void IovUtilMarkDeviceObject(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xA4D125)) != 0) goto loc_004B77C3;
loc_004B77BD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004B77C3:
    result = IovpUtilMarkDeviceObject(a1, a2, a3, a4);
    goto loc_004B77BD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B77B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B77B0[BB_004B77B0]
  bb_004B77BD[BB_004B77BD]
  bb_004B77C2[BB_004B77C2]
  bb_004B77C3[BB_004B77C3]
  bb_004B77B0 -->|branch| bb_004B77C3
  bb_004B77B0 -->|fallthrough| bb_004B77BD
  bb_004B77C2 -->|flow| bb_004B77C3
  bb_004B77C3 -->|branch| bb_004B77BD
```
