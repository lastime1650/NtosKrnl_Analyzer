# PnpAcquireDependencyRelationsLock

- RVA: `0x00A06788`–`0x00A067CF` (길이 `71` bytes)
- VA: `0x0000000140A06788`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `20`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A067AA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A067BC` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A067C8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)

### Direct callers
- [IoResolveDependency](../../text/4C/IoResolveDependency_function_004C4380.md) at `0x004C43A4`
- [IoDuplicateDependency](../72/IoDuplicateDependency_function_00727580.md) at `0x007275BB`
- [IoReserveDependency](../72/IoReserveDependency_function_007276B0.md) at `0x00727705`
- [IoSetDependency](../72/IoSetDependency_function_00727740.md) at `0x007277A1`
- [PnpRequestDeviceRemoval](../8F/PnpRequestDeviceRemoval_function_008FC294.md) at `0x008FC2C2`
- [PnpQueuePendingSurpriseRemoval](PnpQueuePendingSurpriseRemoval_function_00A05FAC.md) at `0x00A06000`
- [PnpNewDeviceNodeDependencyCheck](PnpNewDeviceNodeDependencyCheck_function_00A062A0.md) at `0x00A062BA`
- [PnpDeleteAllDependencyRelations](PnpDeleteAllDependencyRelations_function_00A06724.md) at `0x00A0673A`
- [PipProcessRebuildPowerRelationsQueue](PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A0685A`
- [PnpSurpriseRemovedDeviceNodeDependencyCheck](PnpSurpriseRemovedDeviceNodeDependencyCheck_function_00A0861C.md) at `0x00A08637`
- [IopInitializePlugPlayServices](../../init/C2/IopInitializePlugPlayServices_function_00C2F298.md) at `0x00C2FAFF`

### Static image references
- `0x00A0679B` → RVA `0x00F8C560` (`.data`; read)
- `0x00A067AF` → RVA `0x00F8CEA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A067AA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A067BC` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A067C8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A06788  40 53                           push rbx
00A0678A  48 83 EC 20                     sub rsp, 0x20
00A0678E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A06797  8A D9                           mov bl, cl
00A06799  B2 01                           mov dl, 1
00A0679B  48 8D 0D BE 5D 58 00            lea rcx, [rip + 0x585dbe]
00A067A2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A067A9  90                              nop
00A067AA  E8 11 B4 80 FF                  call 0x140211bc0
00A067AF  48 8D 0D EA 66 58 00            lea rcx, [rip + 0x5866ea]
00A067B6  B2 01                           mov dl, 1
00A067B8  84 DB                           test bl, bl
00A067BA  74 0C                           je 0x140a067c8
00A067BC  E8 5F E6 80 FF                  call 0x140214e20
00A067C1  48 83 C4 20                     add rsp, 0x20
00A067C5  5B                              pop rbx
00A067C6  C3                              ret
00A067C7  CC                              int3
00A067C8  E8 F3 B3 80 FF                  call 0x140211bc0
00A067CD  EB F2                           jmp 0x140a067c1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpAcquireDependencyRelationsLock(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAcquireResourceSharedLite(v_rip + 5791166, 1, a3, a4);
    if (a1 == 0) goto loc_00A067C8;
    result = ExAcquireResourceExclusiveLite(v_rip + 5793514, 1, a3, a4);
loc_00A067C1:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A067C8:
    result = ExAcquireResourceSharedLite(v_rip + 5793514, 1, a3, a4);
    goto loc_00A067C1;
}
```

## 5. (Beta) C Style

```c
int64_t PnpAcquireDependencyRelationsLock(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAcquireResourceSharedLite(v_rip + 5791166, 1, a3, a4);
    if (Arg1 == 0) goto loc_00A067C8;
    result = ExAcquireResourceExclusiveLite(v_rip + 5793514, 1, a3, a4);
loc_00A067C1:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A067C8:
    result = ExAcquireResourceSharedLite(v_rip + 5793514, 1, a3, a4);
    goto loc_00A067C1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A06788&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A06788[BB_00A06788]
  bb_00A067BC[BB_00A067BC]
  bb_00A067C1[BB_00A067C1]
  bb_00A067C7[BB_00A067C7]
  bb_00A067C8[BB_00A067C8]
  bb_00A06788 -->|branch| bb_00A067C8
  bb_00A06788 -->|fallthrough| bb_00A067BC
  bb_00A067BC -->|flow| bb_00A067C1
  bb_00A067C7 -->|flow| bb_00A067C8
  bb_00A067C8 -->|branch| bb_00A067C1
```
