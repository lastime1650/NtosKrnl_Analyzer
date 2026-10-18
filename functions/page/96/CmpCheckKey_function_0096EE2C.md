# CmpCheckKey

- RVA: `0x0096EE2C`–`0x00970B82` (길이 `7,510` bytes)
- VA: `0x000000014096EE2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00095F68`
- 디코드: `1,728`개 명령, `7,510/7,510` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **125**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0096EEC5` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0096EEEC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F004` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F04F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F0FF` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F15B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F177` → [CmpIncrementCachedSecurityRefcount](../97/CmpIncrementCachedSecurityRefcount_function_00970F08.md) (function, `0x00970F08`)
- `0x0096F1C3` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0096F1F3` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F270` → [CmpCheckValueList](../97/CmpCheckValueList_function_00970F6C.md) (function, `0x00970F6C`)
- `0x0096F28B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F327` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F345` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F3F7` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F41B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F438` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F443` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F44D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F457` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F461` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F46B` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F495` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0096F4BC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096F4EE` → [CmpGetIndexElementSize](CmpGetIndexElementSize_function_0096E590.md) (function, `0x0096E590`)
- `0x0096F50A` → [CmpGetIndexElementSize](CmpGetIndexElementSize_function_0096E590.md) (function, `0x0096E590`)
- `0x0096F58B` → [CmpCheckLeaf](CmpCheckLeaf_function_0096E5BC.md) (function, `0x0096E5BC`)
- `0x0096F5C8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F605` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F62D` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096F69E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096F6D7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F6E8` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096F710` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096F79E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F7AF` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096F801` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F824` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F862` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096F8B6` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096F936` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F947` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096F9AC` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096F9F1` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FA02` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FA2F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096FA39` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096FA77` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FA88` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FAB7` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096FADE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096FB0C` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096FB32` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FB68` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FB79` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FBD2` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FBF9` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096FC1B` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FC84` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FC95` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FCE6` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FD1A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FD2B` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FD62` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096FD7F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FD90` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FE39` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FEC3` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FED4` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FF09` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096FF5F` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096FF87` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096FFA5` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FFC1` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0096FFE1` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (function, `0x0049FC64`)
- `0x0097001D` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00970036` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00970077` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00970088` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x009700EE` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009700FF` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0097015F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00970170` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x009701E2` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00970217` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00970261` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009702A1` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0097036C` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0097038F` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x009703CE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009703FB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970420` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0097042A` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00970468` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0097048E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009704CA` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009704FC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00970529` → [CmpGetIndexElementSize](CmpGetIndexElementSize_function_0096E590.md) (function, `0x0096E590`)
- `0x00970545` → [CmpGetIndexElementSize](CmpGetIndexElementSize_function_0096E590.md) (function, `0x0096E590`)
- `0x009705B0` → [CmpCheckLeaf](CmpCheckLeaf_function_0096E5BC.md) (function, `0x0096E5BC`)
- `0x009705FE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00970639` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00970670` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00970689` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009706D1` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00970719` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0097073D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970747` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970751` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0097075B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970765` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0097076F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970794` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0097079E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009707A8` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009707E8` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0097080D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970817` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970842` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00970957` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x009709E2` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970A40` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970A6B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970A96` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00970ABA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00970B34` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)

### Direct callers
- [sub_0096E9E9](Unknown_function_0096E9E9.md) at `0x0096EA71`

### Static image references
- `0x0096F0C0` → RVA `0x00FD8002` (`PAGEDATA`; read)
- `0x0096F8D8` → RVA `0x00EF7C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x0096F41B` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F605` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F6D7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F79E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F801` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F824` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F936` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F9AC` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096F9F1` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FA77` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FB32` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FB68` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FC84` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FCE6` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FD1A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FD7F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FEC3` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FF09` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096FFE1` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (`PAGE` → `.text`)
  - `0x00970077` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009700EE` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0097015F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00970842` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00970ABA` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00970B34` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **13**
  - `0x00970951` → [sub_00B28E18](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x0097095D` → [sub_00B28E18 + 0x5](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x009709DC` → [sub_00B28E18 + 0x1F](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x009709E8` → [sub_00B28E18 + 0x24](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A3A` → [sub_00B28E18 + 0x32](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A46` → [sub_00B28E18 + 0x37](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A65` → [sub_00B28E18 + 0x63](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A71` → [sub_00B28E18 + 0x68](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A90` → [sub_00B28E18 + 0x94](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970A9C` → [sub_00B28E18 + 0x99](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970AF9` → [sub_00B28E18 + 0xC5](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970B06` → [sub_00B28E18 + 0xC5](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)
  - `0x00970B16` → [sub_00B28E18 + 0xC8](../B2/Unknown_function_00B28E18.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0096EE2C  48 8B C4                        mov rax, rsp
0096EE2F  48 89 58 08                     mov qword ptr [rax + 8], rbx
0096EE33  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0096EE37  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0096EE3B  89 50 10                        mov dword ptr [rax + 0x10], edx
0096EE3E  55                              push rbp
0096EE3F  56                              push rsi
0096EE40  57                              push rdi
0096EE41  41 54                           push r12
0096EE43  41 55                           push r13
0096EE45  41 56                           push r14
0096EE47  41 57                           push r15
0096EE49  48 8D 68 B9                     lea rbp, [rax - 0x47]
0096EE4D  48 81 EC C0 00 00 00            sub rsp, 0xc0
0096EE54  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
0096EE58  45 33 F6                        xor r14d, r14d
0096EE5B  44 89 75 DB                     mov dword ptr [rbp - 0x25], r14d
0096EE5F  48 8B D9                        mov rbx, rcx
0096EE62  44 89 75 E3                     mov dword ptr [rbp - 0x1d], r14d
0096EE66  B9 FF FF FF FF                  mov ecx, 0xffffffff
0096EE6B  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
0096EE6E  41 8B F8                        mov edi, r8d
0096EE71  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
0096EE74  8B F2                           mov esi, edx
0096EE76  89 4D BF                        mov dword ptr [rbp - 0x41], ecx
0096EE79  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
0096EE7C  89 4D A7                        mov dword ptr [rbp - 0x59], ecx
0096EE7F  44 89 75 DF                     mov dword ptr [rbp - 0x21], r14d
0096EE83  44 89 75 F3                     mov dword ptr [rbp - 0xd], r14d
0096EE87  44 89 75 C3                     mov dword ptr [rbp - 0x3d], r14d
0096EE8B  44 89 75 B3                     mov dword ptr [rbp - 0x4d], r14d
0096EE8F  44 89 75 AB                     mov dword ptr [rbp - 0x55], r14d
0096EE93  44 88 75 7F                     mov byte ptr [rbp + 0x7f], r14b
0096EE97  4C 89 75 B7                     mov qword ptr [rbp - 0x49], r14
0096EE9B  4D 85 FF                        test r15, r15
0096EE9E  74 1C                           je 0x14096eebc
0096EEA0  45 89 87 F0 00 00 00            mov dword ptr [r15 + 0xf0], r8d
0096EEA7  4D 89 B7 F8 00 00 00            mov qword ptr [r15 + 0xf8], r14
0096EEAE  4D 89 B7 00 01 00 00            mov qword ptr [r15 + 0x100], r14
0096EEB5  41 89 8F 08 01 00 00            mov dword ptr [r15 + 0x108], ecx
0096EEBC  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0096EEC0  8B D7                           mov edx, edi
0096EEC2  48 8B CB                        mov rcx, rbx
0096EEC5  E8 96 6E EE FF                  call 0x140855d60
0096EECA  84 C0                           test al, al
0096EECC  0F 84 E9 0E 00 00               je 0x14096fdbb
0096EED2  B9 01 00 00 00                  mov ecx, 1
0096EED7  4C 8D 45 EF                     lea r8, [rbp - 0x11]
0096EEDB  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
0096EEE1  8B D7                           mov edx, edi
0096EEE3  48 8B CB                        mov rcx, rbx
0096EEE6  0F 84 57 05 00 00               je 0x14096f443
0096EEEC  E8 6F 5D EE FF                  call 0x140854c60
0096EEF1  45 33 C9                        xor r9d, r9d
0096EEF4  4C 8B E0                        mov r12, rax
0096EEF7  48 85 C0                        test rax, rax
0096EEFA  0F 84 32 14 00 00               je 0x140970332
0096EF00  4D 85 FF                        test r15, r15
0096EF03  74 07                           je 0x14096ef0c
0096EF05  49 89 87 F8 00 00 00            mov qword ptr [r15 + 0xf8], rax
0096EF0C  BA FC FF FF FF                  mov edx, 0xfffffffc
0096EF11  41 2B 54 24 FC                  sub edx, dword ptr [r12 - 4]
0096EF16  8D 42 B4                        lea eax, [rdx - 0x4c]
0096EF19  3D 10 04 00 00                  cmp eax, 0x410
0096EF1E  0F 87 DD 13 00 00               ja 0x140970301
0096EF24  41 0F B7 4C 24 48               movzx ecx, word ptr [r12 + 0x48]
0096EF2A  8D 41 4C                        lea eax, [rcx + 0x4c]
0096EF2D  83 F8 4C                        cmp eax, 0x4c
0096EF30  0F 82 3E 07 00 00               jb 0x14096f674
0096EF36  66 85 C9                        test cx, cx
0096EF39  0F 84 35 07 00 00               je 0x14096f674
0096EF3F  3B C2                           cmp eax, edx
0096EF41  0F 87 2D 07 00 00               ja 0x14096f674
0096EF47  41 F6 44 24 02 20               test byte ptr [r12 + 2], 0x20
0096EF4D  BA 00 02 00 00                  mov edx, 0x200
0096EF52  41 B8 00 01 00 00               mov r8d, 0x100
0096EF58  0F 84 8A 0E 00 00               je 0x14096fde8
0096EF5E  66 41 3B C8                     cmp cx, r8w
0096EF62  0F 87 8D 19 00 00               ja 0x1409708f5
0096EF68  45 38 4C 24 4C                  cmp byte ptr [r12 + 0x4c], r9b
0096EF6D  0F 84 8F 19 00 00               je 0x140970902
0096EF73  41 8B D1                        mov edx, r9d
0096EF76  41 BA 01 00 00 00               mov r10d, 1
0096EF7C  3B D1                           cmp edx, ecx
0096EF7E  73 13                           jae 0x14096ef93
0096EF80  8B C2                           mov eax, edx
0096EF82  42 80 7C 20 4C 5C               cmp byte ptr [rax + r12 + 0x4c], 0x5c
0096EF88  0F 84 70 04 00 00               je 0x14096f3fe
0096EF8E  41 03 D2                        add edx, r10d
0096EF91  EB E9                           jmp 0x14096ef7c
0096EF93  44 8B EE                        mov r13d, esi
0096EF96  B8 6E 6B 00 00                  mov eax, 0x6b6e
0096EF9B  41 81 E5 00 00 02 00            and r13d, 0x20000
0096EFA2  BE 4C 01 00 C0                  mov esi, 0xc000014c
0096EFA7  41 BE 0E 00 00 00               mov r14d, 0xe
0096EFAD  44 89 6D 9F                     mov dword ptr [rbp - 0x61], r13d
0096EFB1  66 41 39 04 24                  cmp word ptr [r12], ax
0096EFB6  0F 85 05 0A 00 00               jne 0x14096f9c1
0096EFBC  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096EFC0  8B 88 90 00 00 00               mov ecx, dword ptr [rax + 0x90]
0096EFC6  F6 C1 02                        test cl, 2
0096EFC9  75 0C                           jne 0x14096efd7
0096EFCB  41 F6 44 24 0D 03               test byte ptr [r12 + 0xd], 3
0096EFD1  0F 85 E9 08 00 00               jne 0x14096f8c0
0096EFD7  8B 4D 67                        mov ecx, dword ptr [rbp + 0x67]
0096EFDA  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0096EFE0  41 3B C8                        cmp ecx, r8d
0096EFE3  0F 84 5D 07 00 00               je 0x14096f746
0096EFE9  BF 01 00 00 00                  mov edi, 1
0096EFEE  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0096EFF2  8B D1                           mov edx, ecx
0096EFF4  48 8B CB                        mov rcx, rbx
0096EFF7  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096EFFE  0F 84 5D 04 00 00               je 0x14096f461
0096F004  E8 57 5C EE FF                  call 0x140854c60
0096F009  4C 8B C0                        mov r8, rax
0096F00C  49 8D 44 24 0D                  lea rax, [r12 + 0xd]
0096F011  8A 10                           mov dl, byte ptr [rax]
0096F013  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0096F017  80 E2 03                        and dl, 3
0096F01A  41 8A 40 0D                     mov al, byte ptr [r8 + 0xd]
0096F01E  24 03                           and al, 3
0096F020  3C 03                           cmp al, 3
0096F022  0F 94 C1                        sete cl
0096F025  80 FA 03                        cmp dl, 3
0096F028  0F 95 C0                        setne al
0096F02B  84 C8                           test al, cl
0096F02D  0F 85 4E 06 00 00               jne 0x14096f681
0096F033  45 33 C9                        xor r9d, r9d
0096F036  4D 85 C0                        test r8, r8
0096F039  74 1C                           je 0x14096f057
0096F03B  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096F03F  48 8B CB                        mov rcx, rbx
0096F042  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F049  0F 85 68 0A 00 00               jne 0x14096fab7
0096F04F  E8 EC 6E EE FF                  call 0x140855f40
0096F054  45 33 C9                        xor r9d, r9d
0096F057  49 8D 54 24 0D                  lea rdx, [r12 + 0xd]
0096F05C  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0096F062  41 0F B7 4C 24 4A               movzx ecx, word ptr [r12 + 0x4a]
0096F068  41 8B 44 24 24                  mov eax, dword ptr [r12 + 0x24]
0096F06D  45 8B 6C 24 2C                  mov r13d, dword ptr [r12 + 0x2c]
0096F072  41 8B 7C 24 30                  mov edi, dword ptr [r12 + 0x30]
0096F077  89 45 E7                        mov dword ptr [rbp - 0x19], eax
0096F07A  41 8B 44 24 28                  mov eax, dword ptr [r12 + 0x28]
0096F07F  89 45 FB                        mov dword ptr [rbp - 5], eax
0096F082  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
0096F085  44 89 6D CF                     mov dword ptr [rbp - 0x31], r13d
0096F089  85 C9                           test ecx, ecx
0096F08B  0F 85 65 08 00 00               jne 0x14096f8f6
0096F091  41 3B F8                        cmp edi, r8d
0096F094  0F 85 F2 0D 00 00               jne 0x14096fe8c
0096F09A  44 8A 6D 7F                     mov r13b, byte ptr [rbp + 0x7f]
0096F09E  BF 01 00 00 00                  mov edi, 1
0096F0A3  44 39 45 CF                     cmp dword ptr [rbp - 0x31], r8d
0096F0A7  0F 84 49 0E 00 00               je 0x14096fef6
0096F0AD  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
0096F0B0  8B 4D 9F                        mov ecx, dword ptr [rbp - 0x61]
0096F0B3  41 3B D0                        cmp edx, r8d
0096F0B6  0F 84 5E 06 00 00               je 0x14096f71a
0096F0BC  85 C9                           test ecx, ecx
0096F0BE  75 17                           jne 0x14096f0d7
0096F0C0  44 38 0D 3B 8F 66 00            cmp byte ptr [rip + 0x668f3b], r9b
0096F0C7  0F 84 08 0D 00 00               je 0x14096fdd5
0096F0CD  44 38 4D 6F                     cmp byte ptr [rbp + 0x6f], r9b
0096F0D1  0F 85 46 0E 00 00               jne 0x14096ff1d
0096F0D7  41 3B D0                        cmp edx, r8d
0096F0DA  0F 84 3A 06 00 00               je 0x14096f71a
0096F0E0  41 39 54 24 10                  cmp dword ptr [r12 + 0x10], edx
0096F0E5  0F 85 CC 0F 00 00               jne 0x1409700b7
0096F0EB  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0096F0EF  48 8B CB                        mov rcx, rbx
0096F0F2  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F0F9  0F 84 58 03 00 00               je 0x14096f457
0096F0FF  E8 5C 5B EE FF                  call 0x140854c60
0096F104  45 33 C0                        xor r8d, r8d
0096F107  4C 8B E8                        mov r13, rax
0096F10A  48 85 C0                        test rax, rax
0096F10D  0F 84 C8 19 00 00               je 0x140970adb
0096F113  41 0F B7 54 24 48               movzx edx, word ptr [r12 + 0x48]
0096F119  8B 40 34                        mov eax, dword ptr [rax + 0x34]
0096F11C  0F B7 CA                        movzx ecx, dx
0096F11F  66 03 C9                        add cx, cx
0096F122  41 F6 44 24 02 20               test byte ptr [r12 + 2], 0x20
0096F128  66 0F 44 CA                     cmove cx, dx
0096F12C  0F B7 D1                        movzx edx, cx
0096F12F  0F B7 C8                        movzx ecx, ax
0096F132  3B CA                           cmp ecx, edx
0096F134  0F 82 F1 0F 00 00               jb 0x14097012b
0096F13A  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
0096F13D  41 39 45 38                     cmp dword ptr [r13 + 0x38], eax
0096F141  0F 82 27 08 00 00               jb 0x14096f96e
0096F147  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096F14B  48 8B CB                        mov rcx, rbx
0096F14E  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F155  0F 85 DE 08 00 00               jne 0x14096fa39
0096F15B  E8 E0 6D EE FF                  call 0x140855f40
0096F160  44 8B 6D 9F                     mov r13d, dword ptr [rbp - 0x61]
0096F164  45 84 74 24 02                  test byte ptr [r12 + 2], r14b
0096F169  0F 85 D4 08 00 00               jne 0x14096fa43
0096F16F  41 8B 54 24 2C                  mov edx, dword ptr [r12 + 0x2c]
0096F174  48 8B CB                        mov rcx, rbx
0096F177  E8 8C 1D 00 00                  call 0x140970f08
0096F17C  3D 25 02 00 C0                  cmp eax, 0xc0000225
0096F181  0F 84 27 15 00 00               je 0x1409706ae
0096F187  33 C9                           xor ecx, ecx
0096F189  85 C0                           test eax, eax
0096F18B  0F 88 92 15 00 00               js 0x140970723
0096F191  41 F6 44 24 02 40               test byte ptr [r12 + 2], 0x40
0096F197  0F 85 9E 06 00 00               jne 0x14096f83b
0096F19D  39 4D E7                        cmp dword ptr [rbp - 0x19], ecx
0096F1A0  0F 86 C3 04 00 00               jbe 0x14096f669
0096F1A6  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
0096F1AA  8A 00                           mov al, byte ptr [rax]
0096F1AC  24 03                           and al, 3
0096F1AE  40 3A C7                        cmp al, dil
0096F1B1  0F 84 FA 0F 00 00               je 0x1409701b1
0096F1B7  8B 7D FB                        mov edi, dword ptr [rbp - 5]
0096F1BA  48 8B CB                        mov rcx, rbx
0096F1BD  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0096F1C1  8B D7                           mov edx, edi
0096F1C3  E8 98 6B EE FF                  call 0x140855d60
0096F1C8  33 C9                           xor ecx, ecx
0096F1CA  84 C0                           test al, al
0096F1CC  0F 84 A4 0C 00 00               je 0x14096fe76
0096F1D2  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096F1D9  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0096F1DD  B8 FF FF FF FF                  mov eax, 0xffffffff
0096F1E2  89 4D AB                        mov dword ptr [rbp - 0x55], ecx
0096F1E5  89 45 A7                        mov dword ptr [rbp - 0x59], eax
0096F1E8  8B D7                           mov edx, edi
0096F1EA  48 8B CB                        mov rcx, rbx
0096F1ED  0F 84 78 02 00 00               je 0x14096f46b
0096F1F3  E8 68 5A EE FF                  call 0x140854c60
0096F1F8  4C 8B E8                        mov r13, rax
0096F1FB  48 85 C0                        test rax, rax
0096F1FE  0F 84 E1 11 00 00               je 0x1409703e5
0096F204  44 8B 45 E7                     mov r8d, dword ptr [rbp - 0x19]
0096F208  B9 FF FF FF FF                  mov ecx, 0xffffffff
0096F20D  41 8B C0                        mov eax, r8d
0096F210  48 C1 E0 02                     shl rax, 2
0096F214  48 3B C1                        cmp rax, rcx
0096F217  0F 87 AB 17 00 00               ja 0x1409709c8
0096F21D  B9 FC FF FF FF                  mov ecx, 0xfffffffc
0096F222  41 2B 4D FC                     sub ecx, dword ptr [r13 - 4]
0096F226  3B C1                           cmp eax, ecx
0096F228  0F 87 9A 17 00 00               ja 0x1409709c8
0096F22E  41 8A 54 24 02                  mov dl, byte ptr [r12 + 2]
0096F233  48 8D 45 E3                     lea rax, [rbp - 0x1d]
0096F237  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0096F23C  45 8B C8                        mov r9d, r8d
0096F23F  48 8D 45 DF                     lea rax, [rbp - 0x21]
0096F243  C0 EA 04                        shr dl, 4
0096F246  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0096F24B  80 E2 01                        and dl, 1
0096F24E  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0096F252  4D 8B C5                        mov r8, r13
0096F255  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0096F25A  48 8B CB                        mov rcx, rbx
0096F25D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0096F262  8B 45 57                        mov eax, dword ptr [rbp + 0x57]
0096F265  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0096F269  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
0096F26C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0096F270  E8 F7 1C 00 00                  call 0x140970f6c
0096F275  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096F27C  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0096F280  8B F8                           mov edi, eax
0096F282  48 8B CB                        mov rcx, rbx
0096F285  0F 85 6E 09 00 00               jne 0x14096fbf9
0096F28B  E8 B0 6C EE FF                  call 0x140855f40
0096F290  81 FF 2A 00 00 80               cmp edi, 0x8000002a
0096F296  0F 84 0B 06 00 00               je 0x14096f8a7
0096F29C  B9 00 00 00 80                  mov ecx, 0x80000000
0096F2A1  8D 04 0F                        lea eax, [rdi + rcx]
0096F2A4  85 C1                           test ecx, eax
0096F2A6  0F 84 B0 03 00 00               je 0x14096f65c
0096F2AC  3B FE                           cmp edi, esi
0096F2AE  0F 84 24 03 00 00               je 0x14096f5d8
0096F2B4  41 B8 01 00 00 00               mov r8d, 1
0096F2BA  33 C9                           xor ecx, ecx
0096F2BC  41 BD FF FF FF FF               mov r13d, 0xffffffff
0096F2C2  41 39 4C 24 24                  cmp dword ptr [r12 + 0x24], ecx
0096F2C7  0F 84 08 16 00 00               je 0x1409708d5
0096F2CD  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
0096F2D0  41 39 44 24 3C                  cmp dword ptr [r12 + 0x3c], eax
0096F2D5  0F 82 E0 0E 00 00               jb 0x1409701bb
0096F2DB  8B 45 E3                        mov eax, dword ptr [rbp - 0x1d]
0096F2DE  41 39 44 24 40                  cmp dword ptr [r12 + 0x40], eax
0096F2E3  0F 82 BE 08 00 00               jb 0x14096fba7
0096F2E9  39 4D 9F                        cmp dword ptr [rbp - 0x61], ecx
0096F2EC  75 20                           jne 0x14096f30e
0096F2EE  44 8B 6D 5F                     mov r13d, dword ptr [rbp + 0x5f]
0096F2F2  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
0096F2F5  41 39 44 24 3C                  cmp dword ptr [r12 + 0x3c], eax
0096F2FA  0F 85 0B 0F 00 00               jne 0x14097020b
0096F300  8B 45 E3                        mov eax, dword ptr [rbp - 0x1d]
0096F303  41 39 44 24 40                  cmp dword ptr [r12 + 0x40], eax
0096F308  0F 85 1F 0B 00 00               jne 0x14096fe2d
0096F30E  BF 01 00 00 00                  mov edi, 1
0096F313  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0096F317  48 8B CB                        mov rcx, rbx
0096F31A  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F321  0F 85 08 07 00 00               jne 0x14096fa2f
0096F327  E8 14 6C EE FF                  call 0x140855f40
0096F32C  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F333  4C 8D 45 EF                     lea r8, [rbp - 0x11]
0096F337  8B 7D 5F                        mov edi, dword ptr [rbp + 0x5f]
0096F33A  48 8B CB                        mov rcx, rbx
0096F33D  8B D7                           mov edx, edi
0096F33F  0F 84 08 01 00 00               je 0x14096f44d
0096F345  E8 16 59 EE FF                  call 0x140854c60
0096F34A  45 33 C0                        xor r8d, r8d
0096F34D  4C 8B E8                        mov r13, rax
0096F350  48 85 C0                        test rax, rax
0096F353  0F 84 B2 04 00 00               je 0x14096f80b
0096F359  4D 85 FF                        test r15, r15
0096F35C  74 07                           je 0x14096f365
0096F35E  49 89 87 F8 00 00 00            mov qword ptr [r15 + 0xf8], rax
0096F365  85 FF                           test edi, edi
0096F367  0F 88 E9 08 00 00               js 0x14096fc56
0096F36D  45 39 45 14                     cmp dword ptr [r13 + 0x14], r8d
0096F371  0F 87 FE 00 00 00               ja 0x14096f475
0096F377  4D 8B E0                        mov r12, r8
0096F37A  B8 FF FF FF FF                  mov eax, 0xffffffff
0096F37F  41 39 45 20                     cmp dword ptr [r13 + 0x20], eax
0096F383  0F 85 10 05 00 00               jne 0x14096f899
0096F389  45 39 45 18                     cmp dword ptr [r13 + 0x18], r8d
0096F38D  0F 85 06 05 00 00               jne 0x14096f899
0096F393  41 8A C8                        mov cl, r8b
0096F396  41 B9 01 00 00 00               mov r9d, 1
0096F39C  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
0096F39F  0F BA E2 12                     bt edx, 0x12
0096F3A3  0F 82 3B 04 00 00               jb 0x14096f7e4
0096F3A9  8B C2                           mov eax, edx
0096F3AB  D1 E8                           shr eax, 1
0096F3AD  41 22 C1                        and al, r9b
0096F3B0  F6 C2 0D                        test dl, 0xd
0096F3B3  74 09                           je 0x14096f3be
0096F3B5  84 C9                           test cl, cl
0096F3B7  0F B6 C0                        movzx eax, al
0096F3BA  41 0F 45 C1                     cmovne eax, r9d
0096F3BE  F6 C2 08                        test dl, 8
0096F3C1  0F 85 3C 08 00 00               jne 0x14096fc03
0096F3C7  84 C0                           test al, al
0096F3C9  0F 85 41 08 00 00               jne 0x14096fc10
0096F3CF  F6 5D 7F                        neg byte ptr [rbp + 0x7f]
0096F3D2  1B FF                           sbb edi, edi
0096F3D4  81 E7 2A 00 00 80               and edi, 0x8000002a
0096F3DA  4D 85 E4                        test r12, r12
0096F3DD  74 41                           je 0x14096f420
0096F3DF  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0096F3E3  B9 01 00 00 00                  mov ecx, 1
0096F3E8  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
0096F3EE  48 8B CB                        mov rcx, rbx
0096F3F1  0F 85 6B 09 00 00               jne 0x14096fd62
0096F3F7  E8 44 6B EE FF                  call 0x140855f40
0096F3FC  EB 22                           jmp 0x14096f420
0096F3FE  C7 44 24 20 00 05 00 00         mov dword ptr [rsp + 0x20], 0x500
0096F406  41 B8 0E 00 00 00               mov r8d, 0xe
0096F40C  BE 4C 01 00 C0                  mov esi, 0xc000014c
0096F411  8B FE                           mov edi, esi
0096F413  44 8B CE                        mov r9d, esi
0096F416  33 D2                           xor edx, edx
0096F418  49 8B CF                        mov rcx, r15
0096F41B  E8 34 FB AF FF                  call 0x14046ef54
0096F420  B9 01 00 00 00                  mov ecx, 1
0096F425  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0096F429  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
0096F42F  48 8B CB                        mov rcx, rbx
0096F432  0F 85 7E 04 00 00               jne 0x14096f8b6
0096F438  E8 03 6B EE FF                  call 0x140855f40
0096F43D  E9 23 17 00 00                  jmp 0x140970b65
0096F442  CC                              int3
0096F443  E8 68 58 EE FF                  call 0x140854cb0
0096F448  E9 A4 FA FF FF                  jmp 0x14096eef1
0096F44D  E8 5E 58 EE FF                  call 0x140854cb0
0096F452  E9 F3 FE FF FF                  jmp 0x14096f34a
0096F457  E8 54 58 EE FF                  call 0x140854cb0
0096F45C  E9 A3 FC FF FF                  jmp 0x14096f104
0096F461  E8 4A 58 EE FF                  call 0x140854cb0
0096F466  E9 9E FB FF FF                  jmp 0x14096f009
0096F46B  E8 40 58 EE FF                  call 0x140854cb0
0096F470  E9 83 FD FF FF                  jmp 0x14096f1f8
0096F475  41 8A 45 0D                     mov al, byte ptr [r13 + 0xd]
0096F479  41 B8 01 00 00 00               mov r8d, 1
0096F47F  24 03                           and al, 3
0096F481  41 3A C0                        cmp al, r8b
0096F484  0F 84 C9 09 00 00               je 0x14096fe53
0096F48A  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0096F48E  48 8B CB                        mov rcx, rbx
0096F491  41 8B 55 1C                     mov edx, dword ptr [r13 + 0x1c]
0096F495  E8 C6 68 EE FF                  call 0x140855d60
0096F49A  33 C9                           xor ecx, ecx
0096F49C  84 C0                           test al, al
0096F49E  0F 84 8D 0D 00 00               je 0x140970231
0096F4A4  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096F4AB  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0096F4AF  41 8B 55 1C                     mov edx, dword ptr [r13 + 0x1c]
0096F4B3  48 8B CB                        mov rcx, rbx
0096F4B6  0F 84 54 02 00 00               je 0x14096f710
0096F4BC  E8 9F 57 EE FF                  call 0x140854c60
0096F4C1  45 33 DB                        xor r11d, r11d
0096F4C4  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0096F4C8  4C 8B E0                        mov r12, rax
0096F4CB  48 85 C0                        test rax, rax
0096F4CE  0F 84 E7 11 00 00               je 0x1409706bb
0096F4D4  45 8D 4B FC                     lea r9d, [r11 - 4]
0096F4D8  44 2B 48 FC                     sub r9d, dword ptr [rax - 4]
0096F4DC  41 83 F9 08                     cmp r9d, 8
0096F4E0  0F 82 DB 05 00 00               jb 0x14096fac1
0096F4E6  44 0F B7 50 02                  movzx r10d, word ptr [rax + 2]
0096F4EB  48 8B C8                        mov rcx, rax
0096F4EE  E8 9D F0 FF FF                  call 0x14096e590
0096F4F3  41 0F AF C2                     imul eax, r10d
0096F4F7  8B C8                           mov ecx, eax
0096F4F9  48 83 C1 04                     add rcx, 4
0096F4FD  48 83 F9 04                     cmp rcx, 4
0096F501  0F 82 BA 05 00 00               jb 0x14096fac1
0096F507  49 8B CC                        mov rcx, r12
0096F50A  E8 81 F0 FF FF                  call 0x14096e590
0096F50F  41 0F AF C2                     imul eax, r10d
0096F513  8B C8                           mov ecx, eax
0096F515  48 83 C1 04                     add rcx, 4
0096F519  41 8B C1                        mov eax, r9d
0096F51C  48 3B C8                        cmp rcx, rax
0096F51F  0F 87 9C 05 00 00               ja 0x14096fac1
0096F525  66 45 85 D2                     test r10w, r10w
0096F529  0F 84 C0 05 00 00               je 0x14096faef
0096F52F  4D 85 FF                        test r15, r15
0096F532  74 07                           je 0x14096f53b
0096F534  4D 89 A7 00 01 00 00            mov qword ptr [r15 + 0x100], r12
0096F53B  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
0096F540  BA 6C 66 00 00                  mov edx, 0x666c
0096F545  0F B7 C1                        movzx eax, cx
0096F548  41 B8 FF FC 00 00               mov r8d, 0xfcff
0096F54E  66 2B C2                        sub ax, dx
0096F551  BA 6C 67 00 00                  mov edx, 0x676c
0096F556  66 41 85 C0                     test r8w, ax
0096F55A  0F 85 16 0D 00 00               jne 0x140970276
0096F560  66 3B CA                        cmp cx, dx
0096F563  0F 84 0D 0D 00 00               je 0x140970276
0096F569  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
0096F56F  41 3B 45 14                     cmp eax, dword ptr [r13 + 0x14]
0096F573  0F 85 CB 0C 00 00               jne 0x140970244
0096F579  45 8B 4D 1C                     mov r9d, dword ptr [r13 + 0x1c]
0096F57D  4D 8B C4                        mov r8, r12
0096F580  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
0096F583  48 8B CB                        mov rcx, rbx
0096F586  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0096F58B  E8 2C F0 FF FF                  call 0x14096e5bc
0096F590  8B F8                           mov edi, eax
0096F592  3D 2A 00 00 80                  cmp eax, 0x8000002a
0096F597  0F 84 A0 01 00 00               je 0x14096f73d
0096F59D  B9 00 00 00 80                  mov ecx, 0x80000000
0096F5A2  03 C1                           add eax, ecx
0096F5A4  85 C1                           test ecx, eax
0096F5A6  0F 84 82 02 00 00               je 0x14096f82e
0096F5AC  3B FE                           cmp edi, esi
0096F5AE  0F 84 60 14 00 00               je 0x140970a14
0096F5B4  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096F5BB  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0096F5BF  48 8B CB                        mov rcx, rbx
0096F5C2  0F 85 33 0E 00 00               jne 0x1409703fb
0096F5C8  E8 73 69 EE FF                  call 0x140855f40
0096F5CD  8B 7D 5F                        mov edi, dword ptr [rbp + 0x5f]
0096F5D0  45 33 C0                        xor r8d, r8d
0096F5D3  E9 9F FD FF FF                  jmp 0x14096f377
0096F5D8  4D 85 FF                        test r15, r15
0096F5DB  74 07                           je 0x14096f5e4
0096F5DD  4D 89 AF F8 00 00 00            mov qword ptr [r15 + 0xf8], r13
0096F5E4  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0096F5E8  B9 30 02 00 00                  mov ecx, 0x230
0096F5ED  41 BD FF FF FF FF               mov r13d, 0xffffffff
0096F5F3  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0096F5F7  44 8B CE                        mov r9d, esi
0096F5FA  49 8B CF                        mov rcx, r15
0096F5FD  45 8B C6                        mov r8d, r14d
0096F600  BA 01 00 00 00                  mov edx, 1
0096F605  E8 4A F9 AF FF                  call 0x14046ef54
0096F60A  33 C0                           xor eax, eax
0096F60C  39 45 9F                        cmp dword ptr [rbp - 0x61], eax
0096F60F  0F 85 E1 10 00 00               jne 0x1409706f6
0096F615  38 05 E7 89 66 00               cmp byte ptr [rip + 0x6689e7], al
0096F61B  0F 84 C7 10 00 00               je 0x1409706e8
0096F621  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F624  45 33 C9                        xor r9d, r9d
0096F627  45 33 C0                        xor r8d, r8d
0096F62A  48 8B CB                        mov rcx, rbx
0096F62D  E8 4E 8A EE FF                  call 0x140858080
0096F632  33 C9                           xor ecx, ecx
0096F634  8B F8                           mov edi, eax
0096F636  85 C0                           test eax, eax
0096F638  0F 88 AF 13 00 00               js 0x1409709ed
0096F63E  41 89 4C 24 24                  mov dword ptr [r12 + 0x24], ecx
0096F643  44 8D 41 01                     lea r8d, [rcx + 1]
0096F647  45 89 6C 24 28                  mov dword ptr [r12 + 0x28], r13d
0096F64C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096F650  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096F657  E9 66 FC FF FF                  jmp 0x14096f2c2
0096F65C  3B FE                           cmp edi, esi
0096F65E  0F 84 48 FC FF FF               je 0x14096f2ac
0096F664  E9 B7 FD FF FF                  jmp 0x14096f420
0096F669  41 B8 01 00 00 00               mov r8d, 1
0096F66F  E9 48 FC FF FF                  jmp 0x14096f2bc
0096F674  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
0096F67C  E9 85 FD FF FF                  jmp 0x14096f406
0096F681  40 3A D7                        cmp dl, dil
0096F684  0F 84 A9 F9 FF FF               je 0x14096f033
0096F68A  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096F68E  48 8B CB                        mov rcx, rbx
0096F691  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096F698  0F 85 9F 10 00 00               jne 0x14097073d
0096F69E  E8 9D 68 EE FF                  call 0x140855f40
0096F6A3  33 C0                           xor eax, eax
0096F6A5  B9 01 00 00 00                  mov ecx, 1
0096F6AA  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096F6AD  8B FE                           mov edi, esi
0096F6AF  45 85 ED                        test r13d, r13d
0096F6B2  0F 85 5B 0D 00 00               jne 0x140970413
0096F6B8  38 05 44 89 66 00               cmp byte ptr [rip + 0x668944], al
0096F6BE  0F 84 41 0D 00 00               je 0x140970405
0096F6C4  8B D1                           mov edx, ecx
0096F6C6  C7 44 24 20 98 00 00 00         mov dword ptr [rsp + 0x20], 0x98
0096F6CE  49 8B CF                        mov rcx, r15
0096F6D1  44 8B CE                        mov r9d, esi
0096F6D4  45 8B C6                        mov r8d, r14d
0096F6D7  E8 78 F8 AF FF                  call 0x14046ef54
0096F6DC  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F6DF  45 33 C9                        xor r9d, r9d
0096F6E2  45 33 C0                        xor r8d, r8d
0096F6E5  48 8B CB                        mov rcx, rbx
0096F6E8  E8 93 89 EE FF                  call 0x140858080
0096F6ED  45 33 C9                        xor r9d, r9d
0096F6F0  8B F8                           mov edi, eax
0096F6F2  85 C0                           test eax, eax
0096F6F4  0F 88 22 12 00 00               js 0x14097091c
0096F6FA  41 80 4C 24 0D 03               or byte ptr [r12 + 0xd], 3
0096F700  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096F704  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096F70B  E9 47 F9 FF FF                  jmp 0x14096f057
0096F710  E8 9B 55 EE FF                  call 0x140854cb0
0096F715  E9 A7 FD FF FF                  jmp 0x14096f4c1
0096F71A  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
0096F720  A8 50                           test al, 0x50
0096F722  0F 85 04 0F 00 00               jne 0x14097062c
0096F728  44 88 6D 7F                     mov byte ptr [rbp + 0x7f], r13b
0096F72C  A8 02                           test al, 2
0096F72E  0F 85 13 09 00 00               jne 0x140970047
0096F734  44 8B 6D 9F                     mov r13d, dword ptr [rbp - 0x61]
0096F738  E9 32 FA FF FF                  jmp 0x14096f16f
0096F73D  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0096F741  E9 6E FE FF FF                  jmp 0x14096f5b4
0096F746  4D 8D 6C 24 0D                  lea r13, [r12 + 0xd]
0096F74B  41 8A 45 00                     mov al, byte ptr [r13]
0096F74F  49 8B D5                        mov rdx, r13
0096F752  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
0096F756  24 03                           and al, 3
0096F758  0F 84 04 F9 FF FF               je 0x14096f062
0096F75E  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
0096F762  3C 02                           cmp al, 2
0096F764  0F 84 F8 F8 FF FF               je 0x14096f062
0096F76A  B9 01 00 00 00                  mov ecx, 1
0096F76F  8B FE                           mov edi, esi
0096F771  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096F774  44 39 4D 9F                     cmp dword ptr [rbp - 0x61], r9d
0096F778  0F 85 D8 0B 00 00               jne 0x140970356
0096F77E  44 38 0D 7D 88 66 00            cmp byte ptr [rip + 0x66887d], r9b
0096F785  0F 84 BD 0B 00 00               je 0x140970348
0096F78B  8B D1                           mov edx, ecx
0096F78D  C7 44 24 20 E4 01 00 00         mov dword ptr [rsp + 0x20], 0x1e4
0096F795  49 8B CF                        mov rcx, r15
0096F798  44 8B CE                        mov r9d, esi
0096F79B  45 8B C6                        mov r8d, r14d
0096F79E  E8 B1 F7 AF FF                  call 0x14046ef54
0096F7A3  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F7A6  45 33 C9                        xor r9d, r9d
0096F7A9  45 33 C0                        xor r8d, r8d
0096F7AC  48 8B CB                        mov rcx, rbx
0096F7AF  E8 CC 88 EE FF                  call 0x140858080
0096F7B4  45 33 C9                        xor r9d, r9d
0096F7B7  8B F8                           mov edi, eax
0096F7B9  85 C0                           test eax, eax
0096F7BB  0F 88 4C 0E 00 00               js 0x14097060d
0096F7C1  41 8A 45 00                     mov al, byte ptr [r13]
0096F7C5  49 8B D5                        mov rdx, r13
0096F7C8  24 FE                           and al, 0xfe
0096F7CA  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
0096F7CE  0C 02                           or al, 2
0096F7D0  41 88 45 00                     mov byte ptr [r13], al
0096F7D4  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096F7D8  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096F7DF  E9 78 F8 FF FF                  jmp 0x14096f05c
0096F7E4  84 C9                           test cl, cl
0096F7E6  0F 84 BD FB FF FF               je 0x14096f3a9
0096F7EC  8B FE                           mov edi, esi
0096F7EE  C7 44 24 20 10 04 00 00         mov dword ptr [rsp + 0x20], 0x410
0096F7F6  44 8B CE                        mov r9d, esi
0096F7F9  45 8B C6                        mov r8d, r14d
0096F7FC  33 D2                           xor edx, edx
0096F7FE  49 8B CF                        mov rcx, r15
0096F801  E8 4E F7 AF FF                  call 0x14046ef54
0096F806  E9 CF FB FF FF                  jmp 0x14096f3da
0096F80B  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
0096F811  C7 44 24 20 B0 02 00 00         mov dword ptr [rsp + 0x20], 0x2b0
0096F819  41 8B F9                        mov edi, r9d
0096F81C  45 8B C6                        mov r8d, r14d
0096F81F  33 D2                           xor edx, edx
0096F821  49 8B CF                        mov rcx, r15
0096F824  E8 2B F7 AF FF                  call 0x14046ef54
0096F829  E9 37 13 00 00                  jmp 0x140970b65
0096F82E  3B FE                           cmp edi, esi
0096F830  0F 84 76 FD FF FF               je 0x14096f5ac
0096F836  E9 A4 FB FF FF                  jmp 0x14096f3df
0096F83B  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0096F83F  8B FE                           mov edi, esi
0096F841  45 85 ED                        test r13d, r13d
0096F844  0F 85 3D 0F 00 00               jne 0x140970787
0096F84A  38 0D B2 87 66 00               cmp byte ptr [rip + 0x6687b2], cl
0096F850  0F 84 23 0F 00 00               je 0x140970779
0096F856  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F859  45 33 C9                        xor r9d, r9d
0096F85C  45 33 C0                        xor r8d, r8d
0096F85F  48 8B CB                        mov rcx, rbx
0096F862  E8 19 88 EE FF                  call 0x140858080
0096F867  33 C9                           xor ecx, ecx
0096F869  8B F8                           mov edi, eax
0096F86B  85 C0                           test eax, eax
0096F86D  0F 88 94 11 00 00               js 0x140970a07
0096F873  41 83 4C 24 28 FF               or dword ptr [r12 + 0x28], 0xffffffff
0096F879  B8 BF FF 00 00                  mov eax, 0xffbf
0096F87E  66 41 21 44 24 02               and word ptr [r12 + 2], ax
0096F884  41 89 4C 24 24                  mov dword ptr [r12 + 0x24], ecx
0096F889  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096F88D  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096F894  E9 75 FA FF FF                  jmp 0x14096f30e
0096F899  41 B9 01 00 00 00               mov r9d, 1
0096F89F  41 8A C9                        mov cl, r9b
0096F8A2  E9 F5 FA FF FF                  jmp 0x14096f39c
0096F8A7  41 B8 01 00 00 00               mov r8d, 1
0096F8AD  44 88 45 7F                     mov byte ptr [rbp + 0x7f], r8b
0096F8B1  E9 04 FA FF FF                  jmp 0x14096f2ba
0096F8B6  E8 65 D3 EE FF                  call 0x14085cc20
0096F8BB  E9 A5 12 00 00                  jmp 0x140970b65
0096F8C0  44 88 55 7F                     mov byte ptr [rbp + 0x7f], r10b
0096F8C4  8B FE                           mov edi, esi
0096F8C6  45 85 ED                        test r13d, r13d
0096F8C9  75 1B                           jne 0x14096f8e6
0096F8CB  44 38 0D 30 87 66 00            cmp byte ptr [rip + 0x668730], r9b
0096F8D2  0F 85 98 03 00 00               jne 0x14096fc70
0096F8D8  8B 05 82 83 58 00               mov eax, dword ptr [rip + 0x588382]
0096F8DE  A8 06                           test al, 6
0096F8E0  0F 85 8A 03 00 00               jne 0x14096fc70
0096F8E6  C7 44 24 20 94 00 00 00         mov dword ptr [rsp + 0x20], 0x94
0096F8EE  45 8B C6                        mov r8d, r14d
0096F8F1  E9 1D FB FF FF                  jmp 0x14096f413
0096F8F6  41 3B F8                        cmp edi, r8d
0096F8F9  0F 85 BB 03 00 00               jne 0x14096fcba
0096F8FF  B8 01 00 00 00                  mov eax, 1
0096F904  8B FE                           mov edi, esi
0096F906  44 8A E8                        mov r13b, al
0096F909  88 45 7F                        mov byte ptr [rbp + 0x7f], al
0096F90C  44 39 4D 9F                     cmp dword ptr [rbp - 0x61], r9d
0096F910  0F 85 C5 0E 00 00               jne 0x1409707db
0096F916  44 38 0D E5 86 66 00            cmp byte ptr [rip + 0x6686e5], r9b
0096F91D  0F 84 AA 0E 00 00               je 0x1409707cd
0096F923  44 8B CE                        mov r9d, esi
0096F926  C7 44 24 20 9B 00 00 00         mov dword ptr [rsp + 0x20], 0x9b
0096F92E  45 8B C6                        mov r8d, r14d
0096F931  33 D2                           xor edx, edx
0096F933  49 8B CF                        mov rcx, r15
0096F936  E8 19 F6 AF FF                  call 0x14046ef54
0096F93B  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F93E  45 33 C9                        xor r9d, r9d
0096F941  45 33 C0                        xor r8d, r8d
0096F944  48 8B CB                        mov rcx, rbx
0096F947  E8 34 87 EE FF                  call 0x140858080
0096F94C  45 33 C9                        xor r9d, r9d
0096F94F  8B F8                           mov edi, eax
0096F951  85 C0                           test eax, eax
0096F953  0F 88 D0 0F 00 00               js 0x140970929
0096F959  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
0096F95D  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0096F963  66 45 89 4C 24 4A               mov word ptr [r12 + 0x4a], r9w
0096F969  E9 30 F7 FF FF                  jmp 0x14096f09e
0096F96E  B9 01 00 00 00                  mov ecx, 1
0096F973  8B FE                           mov edi, esi
0096F975  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096F978  44 39 45 9F                     cmp dword ptr [rbp - 0x61], r8d
0096F97C  75 1B                           jne 0x14096f999
0096F97E  44 38 05 7D 86 66 00            cmp byte ptr [rip + 0x66867d], r8b
0096F985  0F 85 E1 03 00 00               jne 0x14096fd6c
0096F98B  8B 05 CF 82 58 00               mov eax, dword ptr [rip + 0x5882cf]
0096F991  A8 06                           test al, 6
0096F993  0F 85 D3 03 00 00               jne 0x14096fd6c
0096F999  C7 44 24 20 78 01 00 00         mov dword ptr [rsp + 0x20], 0x178
0096F9A1  44 8B CE                        mov r9d, esi
0096F9A4  33 D2                           xor edx, edx
0096F9A6  45 8B C6                        mov r8d, r14d
0096F9A9  49 8B CF                        mov rcx, r15
0096F9AC  E8 A3 F5 AF FF                  call 0x14046ef54
0096F9B1  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096F9B8  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096F9BC  E9 2D FA FF FF                  jmp 0x14096f3ee
0096F9C1  44 88 55 7F                     mov byte ptr [rbp + 0x7f], r10b
0096F9C5  8B FE                           mov edi, esi
0096F9C7  45 85 ED                        test r13d, r13d
0096F9CA  0F 85 4C 09 00 00               jne 0x14097031c
0096F9D0  44 38 0D 2B 86 66 00            cmp byte ptr [rip + 0x66862b], r9b
0096F9D7  0F 84 31 09 00 00               je 0x14097030e
0096F9DD  44 8B CE                        mov r9d, esi
0096F9E0  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0096F9E8  45 8B C6                        mov r8d, r14d
0096F9EB  41 8B D2                        mov edx, r10d
0096F9EE  49 8B CF                        mov rcx, r15
0096F9F1  E8 5E F5 AF FF                  call 0x14046ef54
0096F9F6  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096F9F9  45 33 C9                        xor r9d, r9d
0096F9FC  45 33 C0                        xor r8d, r8d
0096F9FF  48 8B CB                        mov rcx, rbx
0096FA02  E8 79 86 EE FF                  call 0x140858080
0096FA07  45 33 C9                        xor r9d, r9d
0096FA0A  8B F8                           mov edi, eax
0096FA0C  85 C0                           test eax, eax
0096FA0E  0F 88 CA 08 00 00               js 0x1409702de
0096FA14  66 41 C7 04 24 6E 6B            mov word ptr [r12], 0x6b6e
0096FA1B  45 8D 51 01                     lea r10d, [r9 + 1]
0096FA1F  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FA23  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FA2A  E9 8D F5 FF FF                  jmp 0x14096efbc
0096FA2F  E8 EC D1 EE FF                  call 0x14085cc20
0096FA34  E9 F3 F8 FF FF                  jmp 0x14096f32c
0096FA39  E8 E2 D1 EE FF                  call 0x14085cc20
0096FA3E  E9 1D F7 FF FF                  jmp 0x14096f160
0096FA43  33 C0                           xor eax, eax
0096FA45  B9 01 00 00 00                  mov ecx, 1
0096FA4A  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096FA4D  8B FE                           mov edi, esi
0096FA4F  45 85 ED                        test r13d, r13d
0096FA52  0F 85 68 0D 00 00               jne 0x1409707c0
0096FA58  38 05 A4 85 66 00               cmp byte ptr [rip + 0x6685a4], al
0096FA5E  0F 84 4E 0D 00 00               je 0x1409707b2
0096FA64  8B D1                           mov edx, ecx
0096FA66  C7 44 24 20 80 01 00 00         mov dword ptr [rsp + 0x20], 0x180
0096FA6E  49 8B CF                        mov rcx, r15
0096FA71  44 8B CE                        mov r9d, esi
0096FA74  45 8B C6                        mov r8d, r14d
0096FA77  E8 D8 F4 AF FF                  call 0x14046ef54
0096FA7C  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FA7F  45 33 C9                        xor r9d, r9d
0096FA82  45 33 C0                        xor r8d, r8d
0096FA85  48 8B CB                        mov rcx, rbx
0096FA88  E8 F3 85 EE FF                  call 0x140858080
0096FA8D  8B F8                           mov edi, eax
0096FA8F  85 C0                           test eax, eax
0096FA91  0F 88 17 0F 00 00               js 0x1409709ae
0096FA97  B8 F1 FF 00 00                  mov eax, 0xfff1
0096FA9C  BF 01 00 00 00                  mov edi, 1
0096FAA1  66 41 21 44 24 02               and word ptr [r12 + 2], ax
0096FAA7  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FAAB  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FAB2  E9 B8 F6 FF FF                  jmp 0x14096f16f
0096FAB7  E8 64 D1 EE FF                  call 0x14085cc20
0096FABC  E9 93 F5 FF FF                  jmp 0x14096f054
0096FAC1  B9 01 00 00 00                  mov ecx, 1
0096FAC6  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0096FACA  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
0096FAD0  8B FE                           mov edi, esi
0096FAD2  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096FAD5  48 8B CB                        mov rcx, rbx
0096FAD8  0F 85 3B 0C 00 00               jne 0x140970719
0096FADE  E8 5D 64 EE FF                  call 0x140855f40
0096FAE3  33 C0                           xor eax, eax
0096FAE5  44 8B E0                        mov r12d, eax
0096FAE8  B8 F0 02 00 00                  mov eax, 0x2f0
0096FAED  EB 31                           jmp 0x14096fb20
0096FAEF  B9 01 00 00 00                  mov ecx, 1
0096FAF4  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0096FAF8  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
0096FAFE  8B FE                           mov edi, esi
0096FB00  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096FB03  48 8B CB                        mov rcx, rbx
0096FB06  0F 85 4F 0C 00 00               jne 0x14097075b
0096FB0C  E8 2F 64 EE FF                  call 0x140855f40
0096FB11  33 C0                           xor eax, eax
0096FB13  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0096FB17  B8 10 03 00 00                  mov eax, 0x310
0096FB1C  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
0096FB20  44 8B CE                        mov r9d, esi
0096FB23  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0096FB27  45 8B C6                        mov r8d, r14d
0096FB2A  BA 01 00 00 00                  mov edx, 1
0096FB2F  49 8B CF                        mov rcx, r15
0096FB32  E8 1D F4 AF FF                  call 0x14046ef54
0096FB37  F7 45 57 00 00 02 00            test dword ptr [rbp + 0x57], 0x20000
0096FB3E  0F 85 AA FC FF FF               jne 0x14096f7ee
0096FB44  33 C0                           xor eax, eax
0096FB46  38 05 B6 84 66 00               cmp byte ptr [rip + 0x6684b6], al
0096FB4C  0F 84 11 03 00 00               je 0x14096fe63
0096FB52  44 8B CE                        mov r9d, esi
0096FB55  C7 44 24 20 F0 03 00 00         mov dword ptr [rsp + 0x20], 0x3f0
0096FB5D  45 8B C6                        mov r8d, r14d
0096FB60  BA 01 00 00 00                  mov edx, 1
0096FB65  49 8B CF                        mov rcx, r15
0096FB68  E8 E7 F3 AF FF                  call 0x14046ef54
0096FB6D  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FB70  45 33 C9                        xor r9d, r9d
0096FB73  45 33 C0                        xor r8d, r8d
0096FB76  48 8B CB                        mov rcx, rbx
0096FB79  E8 02 85 EE FF                  call 0x140858080
0096FB7E  45 33 C0                        xor r8d, r8d
0096FB81  8B F8                           mov edi, eax
0096FB83  85 C0                           test eax, eax
0096FB85  0F 88 39 0F 00 00               js 0x140970ac4
0096FB8B  41 83 4D 1C FF                  or dword ptr [r13 + 0x1c], 0xffffffff
0096FB90  8B 7D 5F                        mov edi, dword ptr [rbp + 0x5f]
0096FB93  45 89 45 14                     mov dword ptr [r13 + 0x14], r8d
0096FB97  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FB9B  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FBA2  E9 D3 F7 FF FF                  jmp 0x14096f37a
0096FBA7  8B FE                           mov edi, esi
0096FBA9  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0096FBAD  39 4D 9F                        cmp dword ptr [rbp - 0x61], ecx
0096FBB0  0F 85 0E 07 00 00               jne 0x1409702c4
0096FBB6  38 0D 46 84 66 00               cmp byte ptr [rip + 0x668446], cl
0096FBBC  0F 84 F4 06 00 00               je 0x1409702b6
0096FBC2  44 8B 6D 5F                     mov r13d, dword ptr [rbp + 0x5f]
0096FBC6  45 33 C9                        xor r9d, r9d
0096FBC9  41 8B D5                        mov edx, r13d
0096FBCC  45 33 C0                        xor r8d, r8d
0096FBCF  48 8B CB                        mov rcx, rbx
0096FBD2  E8 A9 84 EE FF                  call 0x140858080
0096FBD7  8B F8                           mov edi, eax
0096FBD9  85 C0                           test eax, eax
0096FBDB  0F 88 D7 0D 00 00               js 0x1409709b8
0096FBE1  8B 45 E3                        mov eax, dword ptr [rbp - 0x1d]
0096FBE4  41 89 44 24 40                  mov dword ptr [r12 + 0x40], eax
0096FBE9  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FBED  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FBF4  E9 F9 F6 FF FF                  jmp 0x14096f2f2
0096FBF9  E8 22 D0 EE FF                  call 0x14085cc20
0096FBFE  E9 8D F6 FF FF                  jmp 0x14096f290
0096FC03  83 BB DC 00 00 00 04            cmp dword ptr [rbx + 0xdc], 4
0096FC0A  0F 83 B7 F7 FF FF               jae 0x14096f3c7
0096FC10  45 33 C9                        xor r9d, r9d
0096FC13  45 33 C0                        xor r8d, r8d
0096FC16  8B D7                           mov edx, edi
0096FC18  48 8B CB                        mov rcx, rbx
0096FC1B  E8 60 84 EE FF                  call 0x140858080
0096FC20  45 33 C0                        xor r8d, r8d
0096FC23  8B F8                           mov edi, eax
0096FC25  85 C0                           test eax, eax
0096FC27  0F 88 71 0A 00 00               js 0x14097069e
0096FC2D  F6 45 57 04                     test byte ptr [rbp + 0x57], 4
0096FC31  45 89 45 18                     mov dword ptr [r13 + 0x18], r8d
0096FC35  0F 84 96 0E 00 00               je 0x140970ad1
0096FC3B  83 BB DC 00 00 00 04            cmp dword ptr [rbx + 0xdc], 4
0096FC42  0F 82 89 0E 00 00               jb 0x140970ad1
0096FC48  B8 0D F0 AD BA                  mov eax, 0xbaadf00d
0096FC4D  41 89 45 20                     mov dword ptr [r13 + 0x20], eax
0096FC51  E9 79 F7 FF FF                  jmp 0x14096f3cf
0096FC56  45 39 45 14                     cmp dword ptr [r13 + 0x14], r8d
0096FC5A  0F 84 17 F7 FF FF               je 0x14096f377
0096FC60  C7 44 24 20 C0 02 00 00         mov dword ptr [rsp + 0x20], 0x2c0
0096FC68  45 8B C6                        mov r8d, r14d
0096FC6B  E9 A1 F7 FF FF                  jmp 0x14096f411
0096FC70  44 8B CE                        mov r9d, esi
0096FC73  C7 44 24 20 92 00 00 00         mov dword ptr [rsp + 0x20], 0x92
0096FC7B  45 8B C6                        mov r8d, r14d
0096FC7E  41 8B D2                        mov edx, r10d
0096FC81  49 8B CF                        mov rcx, r15
0096FC84  E8 CB F2 AF FF                  call 0x14046ef54
0096FC89  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FC8C  45 33 C9                        xor r9d, r9d
0096FC8F  45 33 C0                        xor r8d, r8d
0096FC92  48 8B CB                        mov rcx, rbx
0096FC95  E8 E6 83 EE FF                  call 0x140858080
0096FC9A  45 33 C9                        xor r9d, r9d
0096FC9D  8B F8                           mov edi, eax
0096FC9F  85 C0                           test eax, eax
0096FCA1  0F 89 44 06 00 00               jns 0x1409702eb
0096FCA7  C7 44 24 20 96 00 00 00         mov dword ptr [rsp + 0x20], 0x96
0096FCAF  44 8B C8                        mov r9d, eax
0096FCB2  45 8B C6                        mov r8d, r14d
0096FCB5  E9 5C F7 FF FF                  jmp 0x14096f416
0096FCBA  8A 02                           mov al, byte ptr [rdx]
0096FCBC  B9 01 00 00 00                  mov ecx, 1
0096FCC1  24 03                           and al, 3
0096FCC3  3A C1                           cmp al, cl
0096FCC5  0F 85 98 06 00 00               jne 0x140970363
0096FCCB  44 8A E9                        mov r13b, cl
0096FCCE  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096FCD1  C7 44 24 20 9E 00 00 00         mov dword ptr [rsp + 0x20], 0x9e
0096FCD9  8B D1                           mov edx, ecx
0096FCDB  44 8B CE                        mov r9d, esi
0096FCDE  45 8B C6                        mov r8d, r14d
0096FCE1  49 8B CF                        mov rcx, r15
0096FCE4  8B FE                           mov edi, esi
0096FCE6  E8 69 F2 AF FF                  call 0x14046ef54
0096FCEB  B9 01 00 00 00                  mov ecx, 1
0096FCF0  33 C0                           xor eax, eax
0096FCF2  39 45 9F                        cmp dword ptr [rbp - 0x61], eax
0096FCF5  0F 85 05 0B 00 00               jne 0x140970800
0096FCFB  38 05 01 83 66 00               cmp byte ptr [rip + 0x668301], al
0096FD01  0F 84 EB 0A 00 00               je 0x1409707f2
0096FD07  8B D1                           mov edx, ecx
0096FD09  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
0096FD11  49 8B CF                        mov rcx, r15
0096FD14  44 8B CE                        mov r9d, esi
0096FD17  45 8B C6                        mov r8d, r14d
0096FD1A  E8 35 F2 AF FF                  call 0x14046ef54
0096FD1F  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FD22  45 33 C9                        xor r9d, r9d
0096FD25  45 33 C0                        xor r8d, r8d
0096FD28  48 8B CB                        mov rcx, rbx
0096FD2B  E8 50 83 EE FF                  call 0x140858080
0096FD30  45 33 C9                        xor r9d, r9d
0096FD33  8B F8                           mov edi, eax
0096FD35  85 C0                           test eax, eax
0096FD37  0F 88 25 0C 00 00               js 0x140970962
0096FD3D  66 45 89 4C 24 4A               mov word ptr [r12 + 0x4a], r9w
0096FD43  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
0096FD47  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0096FD4D  45 89 44 24 30                  mov dword ptr [r12 + 0x30], r8d
0096FD52  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FD56  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FD5D  E9 3C F3 FF FF                  jmp 0x14096f09e
0096FD62  E8 B9 CE EE FF                  call 0x14085cc20
0096FD67  E9 B4 F6 FF FF                  jmp 0x14096f420
0096FD6C  8B D1                           mov edx, ecx
0096FD6E  C7 44 24 20 7A 01 00 00         mov dword ptr [rsp + 0x20], 0x17a
0096FD76  49 8B CF                        mov rcx, r15
0096FD79  44 8B CE                        mov r9d, esi
0096FD7C  45 8B C6                        mov r8d, r14d
0096FD7F  E8 D0 F1 AF FF                  call 0x14046ef54
0096FD84  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
0096FD87  45 33 C9                        xor r9d, r9d
0096FD8A  45 33 C0                        xor r8d, r8d
0096FD8D  48 8B CB                        mov rcx, rbx
0096FD90  E8 EB 82 EE FF                  call 0x140858080
0096FD95  8B F8                           mov edi, eax
0096FD97  85 C0                           test eax, eax
0096FD99  0F 88 FF 0B 00 00               js 0x14097099e
0096FD9F  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
0096FDA2  BF 01 00 00 00                  mov edi, 1
0096FDA7  41 89 45 38                     mov dword ptr [r13 + 0x38], eax
0096FDAB  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096FDAF  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
0096FDB6  E9 8C F3 FF FF                  jmp 0x14096f147
0096FDBB  BE 4C 01 00 C0                  mov esi, 0xc000014c
0096FDC0  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0096FDC5  8B FE                           mov edi, esi
0096FDC7  44 8B CE                        mov r9d, esi
0096FDCA  41 B8 0E 00 00 00               mov r8d, 0xe
0096FDD0  E9 4A FA FF FF                  jmp 0x14096f81f
0096FDD5  8B 05 85 7E 58 00               mov eax, dword ptr [rip + 0x587e85]
0096FDDB  A8 06                           test al, 6
0096FDDD  0F 84 F4 F2 FF FF               je 0x14096f0d7
0096FDE3  E9 E5 F2 FF FF                  jmp 0x14096f0cd
0096FDE8  66 3B CA                        cmp cx, dx
0096FDEB  0F 87 1B 09 00 00               ja 0x14097070c
0096FDF1  41 BA 01 00 00 00               mov r10d, 1
0096FDF7  41 84 CA                        test r10b, cl
0096FDFA  0F 85 0F 0B 00 00               jne 0x14097090f
0096FE00  66 45 39 4C 24 4C               cmp word ptr [r12 + 0x4c], r9w
0096FE06  0F 84 37 08 00 00               je 0x140970643
0096FE0C  41 8B D1                        mov edx, r9d
0096FE0F  D1 E9                           shr ecx, 1
0096FE11  3B D1                           cmp edx, ecx
0096FE13  0F 83 7A F1 FF FF               jae 0x14096ef93
0096FE19  8B C2                           mov eax, edx
0096FE1B  66 41 83 7C 44 4C 5C            cmp word ptr [r12 + rax*2 + 0x4c], 0x5c
0096FE22  0F 84 A9 04 00 00               je 0x1409702d1
0096FE28  41 03 D2                        add edx, r10d
0096FE2B  EB E4                           jmp 0x14096fe11
0096FE2D  45 33 C9                        xor r9d, r9d
0096FE30  45 33 C0                        xor r8d, r8d
0096FE33  41 8B D5                        mov edx, r13d
0096FE36  48 8B CB                        mov rcx, rbx
0096FE39  E8 42 82 EE FF                  call 0x140858080
0096FE3E  85 C0                           test eax, eax
0096FE40  0F 88 C8 F4 FF FF               js 0x14096f30e
0096FE46  8B 45 E3                        mov eax, dword ptr [rbp - 0x1d]
0096FE49  41 89 44 24 40                  mov dword ptr [r12 + 0x40], eax
0096FE4E  E9 BB F4 FF FF                  jmp 0x14096f30e
0096FE53  8B FE                           mov edi, esi
0096FE55  44 88 45 7F                     mov byte ptr [rbp + 0x7f], r8b
0096FE59  B8 C8 02 00 00                  mov eax, 0x2c8
0096FE5E  E9 B9 FC FF FF                  jmp 0x14096fb1c
0096FE63  8B 05 F7 7D 58 00               mov eax, dword ptr [rip + 0x587df7]
0096FE69  A8 06                           test al, 6
0096FE6B  0F 84 7D F9 FF FF               je 0x14096f7ee
0096FE71  E9 DC FC FF FF                  jmp 0x14096fb52
0096FE76  B9 00 02 00 00                  mov ecx, 0x200
0096FE7B  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0096FE7F  41 BD FF FF FF FF               mov r13d, 0xffffffff
0096FE85  8B FE                           mov edi, esi
0096FE87  E9 67 F7 FF FF                  jmp 0x14096f5f3
0096FE8C  B9 01 00 00 00                  mov ecx, 1
0096FE91  8B FE                           mov edi, esi
0096FE93  44 8A E9                        mov r13b, cl
0096FE96  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
0096FE99  44 39 4D 9F                     cmp dword ptr [rbp - 0x61], r9d
0096FE9D  0F 85 B9 09 00 00               jne 0x14097085c
0096FEA3  44 38 0D 58 81 66 00            cmp byte ptr [rip + 0x668158], r9b
0096FEAA  0F 84 9E 09 00 00               je 0x14097084e
0096FEB0  8B D1                           mov edx, ecx
0096FEB2  C7 44 24 20 E8 00 00 00         mov dword ptr [rsp + 0x20], 0xe8
0096FEBA  49 8B CF                        mov rcx, r15
0096FEBD  44 8B CE                        mov r9d, esi
0096FEC0  45 8B C6                        mov r8d, r14d
0096FEC3  E8 8C F0 AF FF                  call 0x14046ef54
0096FEC8  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FECB  45 33 C9                        xor r9d, r9d
0096FECE  45 33 C0                        xor r8d, r8d
0096FED1  48 8B CB                        mov rcx, rbx
0096FED4  E8 A7 81 EE FF                  call 0x140858080
0096FED9  45 33 C9                        xor r9d, r9d
0096FEDC  8B F8                           mov edi, eax
0096FEDE  85 C0                           test eax, eax
0096FEE0  0F 89 61 FE FF FF               jns 0x14096fd47
0096FEE6  C7 44 24 20 EC 00 00 00         mov dword ptr [rsp + 0x20], 0xec
0096FEEE  44 8B C8                        mov r9d, eax
0096FEF1  E9 3A 08 00 00                  jmp 0x140970730
0096FEF6  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
0096FEFE  44 8B CE                        mov r9d, esi
0096FF01  45 8B C6                        mov r8d, r14d
0096FF04  8B D7                           mov edx, edi
0096FF06  49 8B CF                        mov rcx, r15
0096FF09  E8 46 F0 AF FF                  call 0x14046ef54
0096FF0E  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
0096FF11  45 33 C9                        xor r9d, r9d
0096FF14  8B 4D 9F                        mov ecx, dword ptr [rbp - 0x61]
0096FF17  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0096FF1D  85 C9                           test ecx, ecx
0096FF1F  0F 85 0A 09 00 00               jne 0x14097082f
0096FF25  44 38 0D D6 80 66 00            cmp byte ptr [rip + 0x6680d6], r9b
0096FF2C  0F 84 EF 08 00 00               je 0x140970821
0096FF32  83 65 D3 00                     and dword ptr [rbp - 0x2d], 0
0096FF36  83 65 AB 00                     and dword ptr [rbp - 0x55], 0
0096FF3A  44 89 45 CF                     mov dword ptr [rbp - 0x31], r8d
0096FF3E  44 89 45 A7                     mov dword ptr [rbp - 0x59], r8d
0096FF42  41 3B D0                        cmp edx, r8d
0096FF45  0F 84 0D 0C 00 00               je 0x140970b58
0096FF4B  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0096FF4F  48 8B CB                        mov rcx, rbx
0096FF52  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
0096FF59  0F 84 C1 04 00 00               je 0x140970420
0096FF5F  E8 FC 4C EE FF                  call 0x140854c60
0096FF64  4C 8B E8                        mov r13, rax
0096FF67  48 85 C0                        test rax, rax
0096FF6A  0F 84 D2 0B 00 00               je 0x140970b42
0096FF70  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096FF77  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0096FF7B  8B 50 2C                        mov edx, dword ptr [rax + 0x2c]
0096FF7E  48 8B CB                        mov rcx, rbx
0096FF81  0F 84 A3 04 00 00               je 0x14097042a
0096FF87  E8 D4 4C EE FF                  call 0x140854c60
0096FF8C  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0096FF90  48 85 C0                        test rax, rax
0096FF93  0F 84 82 0B 00 00               je 0x140970b1b
0096FF99  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0096FF9C  45 33 C9                        xor r9d, r9d
0096FF9F  45 33 C0                        xor r8d, r8d
0096FFA2  48 8B CB                        mov rcx, rbx
0096FFA5  E8 D6 80 EE FF                  call 0x140858080
0096FFAA  8B F8                           mov edi, eax
0096FFAC  85 C0                           test eax, eax
0096FFAE  0F 88 57 0B 00 00               js 0x140970b0b
0096FFB4  41 8B 55 2C                     mov edx, dword ptr [r13 + 0x2c]
0096FFB8  45 33 C9                        xor r9d, r9d
0096FFBB  45 33 C0                        xor r8d, r8d
0096FFBE  48 8B CB                        mov rcx, rbx
0096FFC1  E8 BA 80 EE FF                  call 0x140858080
0096FFC6  8B F8                           mov edi, eax
0096FFC8  85 C0                           test eax, eax
0096FFCA  0F 88 2E 0B 00 00               js 0x140970afe
0096FFD0  45 8B 45 2C                     mov r8d, dword ptr [r13 + 0x2c]
0096FFD4  41 B9 01 00 00 00               mov r9d, 1
0096FFDA  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0096FFDE  48 8B D3                        mov rdx, rbx
0096FFE1  E8 7E FC B2 FF                  call 0x14049fc64
0096FFE6  8B F8                           mov edi, eax
0096FFE8  85 C0                           test eax, eax
0096FFEA  0F 88 01 0B 00 00               js 0x140970af1
0096FFF0  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
0096FFF4  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0096FFF8  41 89 44 24 2C                  mov dword ptr [r12 + 0x2c], eax
0096FFFD  BF 01 00 00 00                  mov edi, 1
00970002  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00970006  48 8B CB                        mov rcx, rbx
00970009  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
00970010  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
00970017  0F 85 2A 07 00 00               jne 0x140970747
0097001D  E8 1E 5F EE FF                  call 0x140855f40
00970022  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00970026  48 8B CB                        mov rcx, rbx
00970029  40 84 BB 8C 00 00 00            test byte ptr [rbx + 0x8c], dil
00970030  0F 85 1B 07 00 00               jne 0x140970751
00970036  E8 05 5F EE FF                  call 0x140855f40
0097003B  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
0097003E  40 88 7D 7F                     mov byte ptr [rbp + 0x7f], dil
00970042  E9 99 F0 FF FF                  jmp 0x14096f0e0
00970047  BA 01 00 00 00                  mov edx, 1
0097004C  8B FE                           mov edi, esi
0097004E  88 55 7F                        mov byte ptr [rbp + 0x7f], dl
00970051  85 C9                           test ecx, ecx
00970053  0F 85 1E 08 00 00               jne 0x140970877
00970059  44 38 0D A2 7F 66 00            cmp byte ptr [rip + 0x667fa2], r9b
00970060  0F 84 03 08 00 00               je 0x140970869
00970066  44 8B CE                        mov r9d, esi
00970069  C7 44 24 20 C0 01 00 00         mov dword ptr [rsp + 0x20], 0x1c0
00970071  45 8B C6                        mov r8d, r14d
00970074  49 8B CF                        mov rcx, r15
00970077  E8 D8 EE AF FF                  call 0x14046ef54
0097007C  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
0097007F  45 33 C9                        xor r9d, r9d
00970082  45 33 C0                        xor r8d, r8d
00970085  48 8B CB                        mov rcx, rbx
00970088  E8 F3 7F EE FF                  call 0x140858080
0097008D  8B F8                           mov edi, eax
0097008F  85 C0                           test eax, eax
00970091  0F 88 D8 08 00 00               js 0x14097096f
00970097  B8 FD FF 00 00                  mov eax, 0xfffd
0097009C  BF 01 00 00 00                  mov edi, 1
009700A1  66 41 21 44 24 02               and word ptr [r12 + 2], ax
009700A7  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
009700AB  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
009700B2  E9 7D F6 FF FF                  jmp 0x14096f734
009700B7  45 33 ED                        xor r13d, r13d
009700BA  B9 01 00 00 00                  mov ecx, 1
009700BF  8B FE                           mov edi, esi
009700C1  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
009700C4  44 39 6D 9F                     cmp dword ptr [rbp - 0x61], r13d
009700C8  0F 85 C4 07 00 00               jne 0x140970892
009700CE  44 38 2D 2D 7F 66 00            cmp byte ptr [rip + 0x667f2d], r13b
009700D5  0F 84 A9 07 00 00               je 0x140970884
009700DB  8B D1                           mov edx, ecx
009700DD  C7 44 24 20 40 01 00 00         mov dword ptr [rsp + 0x20], 0x140
009700E5  49 8B CF                        mov rcx, r15
009700E8  44 8B CE                        mov r9d, esi
009700EB  45 8B C6                        mov r8d, r14d
009700EE  E8 61 EE AF FF                  call 0x14046ef54
009700F3  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
009700F6  45 33 C9                        xor r9d, r9d
009700F9  45 33 C0                        xor r8d, r8d
009700FC  48 8B CB                        mov rcx, rbx
009700FF  E8 7C 7F EE FF                  call 0x140858080
00970104  8B F8                           mov edi, eax
00970106  85 C0                           test eax, eax
00970108  0F 88 6E 08 00 00               js 0x14097097c
0097010E  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
00970111  BF 01 00 00 00                  mov edi, 1
00970116  41 89 54 24 10                  mov dword ptr [r12 + 0x10], edx
0097011B  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0097011F  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
00970126  E9 C0 EF FF FF                  jmp 0x14096f0eb
0097012B  B9 01 00 00 00                  mov ecx, 1
00970130  8B FE                           mov edi, esi
00970132  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00970135  44 39 45 9F                     cmp dword ptr [rbp - 0x61], r8d
00970139  0F 85 6E 07 00 00               jne 0x1409708ad
0097013F  44 38 05 BC 7E 66 00            cmp byte ptr [rip + 0x667ebc], r8b
00970146  0F 84 53 07 00 00               je 0x14097089f
0097014C  8B D1                           mov edx, ecx
0097014E  C7 44 24 20 74 01 00 00         mov dword ptr [rsp + 0x20], 0x174
00970156  49 8B CF                        mov rcx, r15
00970159  44 8B CE                        mov r9d, esi
0097015C  45 8B C6                        mov r8d, r14d
0097015F  E8 F0 ED AF FF                  call 0x14046ef54
00970164  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
00970167  45 33 C9                        xor r9d, r9d
0097016A  45 33 C0                        xor r8d, r8d
0097016D  48 8B CB                        mov rcx, rbx
00970170  E8 0B 7F EE FF                  call 0x140858080
00970175  45 33 C0                        xor r8d, r8d
00970178  8B F8                           mov edi, eax
0097017A  85 C0                           test eax, eax
0097017C  0F 88 07 08 00 00               js 0x140970989
00970182  41 0F B7 54 24 48               movzx edx, word ptr [r12 + 0x48]
00970188  41 8D 78 01                     lea edi, [r8 + 1]
0097018C  0F B7 CA                        movzx ecx, dx
0097018F  66 03 C9                        add cx, cx
00970192  41 F6 44 24 02 20               test byte ptr [r12 + 2], 0x20
00970198  66 0F 44 CA                     cmove cx, dx
0097019C  66 41 89 4D 34                  mov word ptr [r13 + 0x34], cx
009701A1  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
009701A5  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
009701AC  E9 89 EF FF FF                  jmp 0x14096f13a
009701B1  B9 F8 01 00 00                  mov ecx, 0x1f8
009701B6  E9 C0 FC FF FF                  jmp 0x14096fe7b
009701BB  8B FE                           mov edi, esi
009701BD  44 88 45 7F                     mov byte ptr [rbp + 0x7f], r8b
009701C1  39 4D 9F                        cmp dword ptr [rbp - 0x61], ecx
009701C4  0F 85 FE 06 00 00               jne 0x1409708c8
009701CA  38 0D 32 7E 66 00               cmp byte ptr [rip + 0x667e32], cl
009701D0  0F 84 E4 06 00 00               je 0x1409708ba
009701D6  8B 55 5F                        mov edx, dword ptr [rbp + 0x5f]
009701D9  45 33 C9                        xor r9d, r9d
009701DC  45 33 C0                        xor r8d, r8d
009701DF  48 8B CB                        mov rcx, rbx
009701E2  E8 99 7E EE FF                  call 0x140858080
009701E7  33 C9                           xor ecx, ecx
009701E9  8B F8                           mov edi, eax
009701EB  85 C0                           test eax, eax
009701ED  0F 88 07 08 00 00               js 0x1409709fa
009701F3  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
009701F6  41 89 44 24 3C                  mov dword ptr [r12 + 0x3c], eax
009701FB  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
009701FF  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
00970206  E9 D0 F0 FF FF                  jmp 0x14096f2db
0097020B  45 33 C9                        xor r9d, r9d
0097020E  45 33 C0                        xor r8d, r8d
00970211  41 8B D5                        mov edx, r13d
00970214  48 8B CB                        mov rcx, rbx
00970217  E8 64 7E EE FF                  call 0x140858080
0097021C  85 C0                           test eax, eax
0097021E  0F 88 DC F0 FF FF               js 0x14096f300
00970224  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
00970227  41 89 44 24 3C                  mov dword ptr [r12 + 0x3c], eax
0097022C  E9 CF F0 FF FF                  jmp 0x14096f300
00970231  8B FE                           mov edi, esi
00970233  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
00970237  B8 D0 02 00 00                  mov eax, 0x2d0
0097023C  4C 8B E1                        mov r12, rcx
0097023F  E9 DC F8 FF FF                  jmp 0x14096fb20
00970244  B9 01 00 00 00                  mov ecx, 1
00970249  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0097024D  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00970253  8B FE                           mov edi, esi
00970255  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00970258  48 8B CB                        mov rcx, rbx
0097025B  0F 85 04 05 00 00               jne 0x140970765
00970261  E8 DA 5C EE FF                  call 0x140855f40
00970266  33 C0                           xor eax, eax
00970268  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0097026C  B8 30 03 00 00                  mov eax, 0x330
00970271  E9 A6 F8 FF FF                  jmp 0x14096fb1c
00970276  B8 72 69 00 00                  mov eax, 0x6972
0097027B  66 3B C8                        cmp cx, ax
0097027E  0F 84 B0 01 00 00               je 0x140970434
00970284  B9 01 00 00 00                  mov ecx, 1
00970289  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0097028D  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00970293  8B FE                           mov edi, esi
00970295  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00970298  48 8B CB                        mov rcx, rbx
0097029B  0F 85 FD 04 00 00               jne 0x14097079e
009702A1  E8 9A 5C EE FF                  call 0x140855f40
009702A6  33 C0                           xor eax, eax
009702A8  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
009702AC  B8 E0 03 00 00                  mov eax, 0x3e0
009702B1  E9 66 F8 FF FF                  jmp 0x14096fb1c
009702B6  8B 05 A4 79 58 00               mov eax, dword ptr [rip + 0x5879a4]
009702BC  A8 06                           test al, 6
009702BE  0F 85 FE F8 FF FF               jne 0x14096fbc2
009702C4  C7 44 24 20 66 02 00 00         mov dword ptr [rsp + 0x20], 0x266
009702CC  E9 1D F6 FF FF                  jmp 0x14096f8ee
009702D1  C7 44 24 20 10 05 00 00         mov dword ptr [rsp + 0x20], 0x510
009702D9  E9 28 F1 FF FF                  jmp 0x14096f406
009702DE  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
009702E6  E9 C4 F9 FF FF                  jmp 0x14096fcaf
009702EB  41 80 64 24 0D FC               and byte ptr [r12 + 0xd], 0xfc
009702F1  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
009702F5  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
009702FC  E9 D6 EC FF FF                  jmp 0x14096efd7
00970301  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
00970309  E9 F8 F0 FF FF                  jmp 0x14096f406
0097030E  8B 05 4C 79 58 00               mov eax, dword ptr [rip + 0x58794c]
00970314  A8 06                           test al, 6
00970316  0F 85 C1 F6 FF FF               jne 0x14096f9dd
0097031C  C7 44 24 20 90 00 00 00         mov dword ptr [rsp + 0x20], 0x90
00970324  44 8B CE                        mov r9d, esi
00970327  45 8B C6                        mov r8d, r14d
0097032A  41 8B D2                        mov edx, r10d
0097032D  E9 E6 F0 FF FF                  jmp 0x14096f418
00970332  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00970338  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00970340  41 8B F9                        mov edi, r9d
00970343  E9 82 FA FF FF                  jmp 0x14096fdca
00970348  8B 05 12 79 58 00               mov eax, dword ptr [rip + 0x587912]
0097034E  A8 06                           test al, 6
00970350  0F 85 35 F4 FF FF               jne 0x14096f78b
00970356  C7 44 24 20 EC 01 00 00         mov dword ptr [rsp + 0x20], 0x1ec
0097035E  E9 8B F5 FF FF                  jmp 0x14096f8ee
00970363  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
00970367  8B D7                           mov edx, edi
00970369  48 8B CB                        mov rcx, rbx
0097036C  E8 EF 59 EE FF                  call 0x140855d60
00970371  84 C0                           test al, al
00970373  0F 84 A1 02 00 00               je 0x14097061a
00970379  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
00970380  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00970384  8B D7                           mov edx, edi
00970386  48 8B CB                        mov rcx, rbx
00970389  0F 84 42 03 00 00               je 0x1409706d1
0097038F  E8 CC 48 EE FF                  call 0x140854c60
00970394  48 8B D0                        mov rdx, rax
00970397  48 85 C0                        test rax, rax
0097039A  0F 84 96 05 00 00               je 0x140970936
009703A0  8A 8B 8C 00 00 00               mov cl, byte ptr [rbx + 0x8c]
009703A6  BF 01 00 00 00                  mov edi, 1
009703AB  B8 FC FF FF FF                  mov eax, 0xfffffffc
009703B0  40 22 CF                        and cl, dil
009703B3  2B 42 FC                        sub eax, dword ptr [rdx - 4]
009703B6  48 8D 55 A7                     lea rdx, [rbp - 0x59]
009703BA  39 45 C7                        cmp dword ptr [rbp - 0x39], eax
009703BD  0F 87 89 05 00 00               ja 0x14097094c
009703C3  84 C9                           test cl, cl
009703C5  48 8B CB                        mov rcx, rbx
009703C8  0F 85 1A 04 00 00               jne 0x1409707e8
009703CE  E8 6D 5B EE FF                  call 0x140855f40
009703D3  44 8A 6D 7F                     mov r13b, byte ptr [rbp + 0x7f]
009703D7  41 B8 FF FF FF FF               mov r8d, 0xffffffff
009703DD  45 33 C9                        xor r9d, r9d
009703E0  E9 BE EC FF FF                  jmp 0x14096f0a3
009703E5  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
009703EB  C7 44 24 20 10 02 00 00         mov dword ptr [rsp + 0x20], 0x210
009703F3  41 8B F9                        mov edi, r9d
009703F6  E9 B7 F8 FF FF                  jmp 0x14096fcb2
009703FB  E8 20 C8 EE FF                  call 0x14085cc20
00970400  E9 C8 F1 FF FF                  jmp 0x14096f5cd
00970405  8B 05 55 78 58 00               mov eax, dword ptr [rip + 0x587855]
0097040B  A8 06                           test al, 6
0097040D  0F 85 B1 F2 FF FF               jne 0x14096f6c4
00970413  C7 44 24 20 9C 00 00 00         mov dword ptr [rsp + 0x20], 0x9c
0097041B  E9 CE F4 FF FF                  jmp 0x14096f8ee
00970420  E8 8B 48 EE FF                  call 0x140854cb0
00970425  E9 3A FB FF FF                  jmp 0x14096ff64
0097042A  E8 81 48 EE FF                  call 0x140854cb0
0097042F  E9 58 FB FF FF                  jmp 0x14096ff8c
00970434  45 8B E3                        mov r12d, r11d
00970437  44 89 5D E7                     mov dword ptr [rbp - 0x19], r11d
0097043B  41 8B FB                        mov edi, r11d
0097043E  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00970442  89 7D C7                        mov dword ptr [rbp - 0x39], edi
00970445  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
00970449  3B F8                           cmp edi, eax
0097044B  73 56                           jae 0x1409704a3
0097044D  4D 85 FF                        test r15, r15
00970450  74 07                           je 0x140970459
00970452  41 89 BF 08 01 00 00            mov dword ptr [r15 + 0x108], edi
00970459  4C 8B 45 77                     mov r8, qword ptr [rbp + 0x77]
0097045D  44 8B E7                        mov r12d, edi
00970460  42 8B 54 A1 04                  mov edx, dword ptr [rcx + r12*4 + 4]
00970465  48 8B CB                        mov rcx, rbx
00970468  E8 F3 58 EE FF                  call 0x140855d60
0097046D  84 C0                           test al, al
0097046F  75 6E                           jne 0x1409704df
00970471  B9 01 00 00 00                  mov ecx, 1
00970476  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0097047A  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
00970480  8B FE                           mov edi, esi
00970482  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00970485  48 8B CB                        mov rcx, rbx
00970488  0F 85 06 03 00 00               jne 0x140970794
0097048E  E8 AD 5A EE FF                  call 0x140855f40
00970493  33 C0                           xor eax, eax
00970495  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00970499  B8 50 03 00 00                  mov eax, 0x350
0097049E  E9 79 F6 FF FF                  jmp 0x14096fb1c
009704A3  45 39 65 14                     cmp dword ptr [r13 + 0x14], r12d
009704A7  0F 84 07 F1 FF FF               je 0x14096f5b4
009704AD  B9 01 00 00 00                  mov ecx, 1
009704B2  48 8D 55 AF                     lea rdx, [rbp - 0x51]
009704B6  84 8B 8C 00 00 00               test byte ptr [rbx + 0x8c], cl
009704BC  8B FE                           mov edi, esi
009704BE  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
009704C1  48 8B CB                        mov rcx, rbx
009704C4  0F 85 A5 02 00 00               jne 0x14097076f
009704CA  E8 71 5A EE FF                  call 0x140855f40
009704CF  33 C0                           xor eax, eax
009704D1  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
009704D5  B8 C0 03 00 00                  mov eax, 0x3c0
009704DA  E9 3D F6 FF FF                  jmp 0x14096fb1c
009704DF  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
009704E6  4C 8D 45 D7                     lea r8, [rbp - 0x29]
009704EA  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
009704EE  48 8B CB                        mov rcx, rbx
009704F1  42 8B 54 A2 04                  mov edx, dword ptr [rdx + r12*4 + 4]
009704F6  0F 84 3D 01 00 00               je 0x140970639
009704FC  E8 5F 47 EE FF                  call 0x140854c60
00970501  4C 8B E0                        mov r12, rax
00970504  48 85 C0                        test rax, rax
00970507  0F 84 94 05 00 00               je 0x140970aa1
0097050D  41 B9 FC FF FF FF               mov r9d, 0xfffffffc
00970513  44 2B 48 FC                     sub r9d, dword ptr [rax - 4]
00970517  41 83 F9 08                     cmp r9d, 8
0097051B  0F 82 2F 01 00 00               jb 0x140970650
00970521  44 0F B7 50 02                  movzx r10d, word ptr [rax + 2]
00970526  48 8B C8                        mov rcx, rax
00970529  E8 62 E0 FF FF                  call 0x14096e590
0097052E  41 0F AF C2                     imul eax, r10d
00970532  8B C8                           mov ecx, eax
00970534  48 83 C1 04                     add rcx, 4
00970538  48 83 F9 04                     cmp rcx, 4
0097053C  0F 82 0E 01 00 00               jb 0x140970650
00970542  49 8B CC                        mov rcx, r12
00970545  E8 46 E0 FF FF                  call 0x14096e590
0097054A  41 0F AF C2                     imul eax, r10d
0097054E  8B C8                           mov ecx, eax
00970550  48 83 C1 04                     add rcx, 4
00970554  41 8B C1                        mov eax, r9d
00970557  48 3B C8                        cmp rcx, rax
0097055A  0F 87 F0 00 00 00               ja 0x140970650
00970560  66 45 85 D2                     test r10w, r10w
00970564  0F 84 0C 05 00 00               je 0x140970a76
0097056A  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
0097056F  BA 6C 66 00 00                  mov edx, 0x666c
00970574  0F B7 C1                        movzx eax, cx
00970577  66 2B C2                        sub ax, dx
0097057A  BA FF FC 00 00                  mov edx, 0xfcff
0097057F  66 85 C2                        test dx, ax
00970582  0F 85 C3 04 00 00               jne 0x140970a4b
00970588  B8 6C 67 00 00                  mov eax, 0x676c
0097058D  66 3B C8                        cmp cx, ax
00970590  0F 84 B5 04 00 00               je 0x140970a4b
00970596  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
0097059A  4D 8B C4                        mov r8, r12
0097059D  8B 55 57                        mov edx, dword ptr [rbp + 0x57]
009705A0  48 8B CB                        mov rcx, rbx
009705A3  44 8B CF                        mov r9d, edi
009705A6  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009705AB  46 8B 4C 88 04                  mov r9d, dword ptr [rax + r9*4 + 4]
009705B0  E8 07 E0 FF FF                  call 0x14096e5bc
009705B5  8B F8                           mov edi, eax
009705B7  3D 2A 00 00 80                  cmp eax, 0x8000002a
009705BC  0F 84 41 01 00 00               je 0x140970703
009705C2  B9 00 00 00 80                  mov ecx, 0x80000000
009705C7  03 C1                           add eax, ecx
009705C9  85 C1                           test ecx, eax
009705CB  0F 84 0A 01 00 00               je 0x1409706db
009705D1  3B FE                           cmp edi, esi
009705D3  0F 84 49 04 00 00               je 0x140970a22
009705D9  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
009705DF  48 8D 55 D7                     lea rdx, [rbp - 0x29]
009705E3  44 8B 65 E7                     mov r12d, dword ptr [rbp - 0x19]
009705E7  48 8B CB                        mov rcx, rbx
009705EA  44 03 E0                        add r12d, eax
009705ED  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
009705F4  44 89 65 E7                     mov dword ptr [rbp - 0x19], r12d
009705F8  0F 85 AA 01 00 00               jne 0x1409707a8
009705FE  E8 3D 59 EE FF                  call 0x140855f40
00970603  8B 7D C7                        mov edi, dword ptr [rbp - 0x39]
00970606  FF C7                           inc edi
00970608  E9 31 FE FF FF                  jmp 0x14097043e
0097060D  C7 44 24 20 E8 01 00 00         mov dword ptr [rsp + 0x20], 0x1e8
00970615  E9 95 F6 FF FF                  jmp 0x14096fcaf
0097061A  B9 01 00 00 00                  mov ecx, 1
0097061F  8B FE                           mov edi, esi
00970621  44 8A E9                        mov r13b, cl
00970624  88 4D 7F                        mov byte ptr [rbp + 0x7f], cl
00970627  E9 C4 F6 FF FF                  jmp 0x14096fcf0
0097062C  C7 44 24 20 B0 01 00 00         mov dword ptr [rsp + 0x20], 0x1b0
00970634  E9 2F F6 FF FF                  jmp 0x14096fc68
00970639  E8 72 46 EE FF                  call 0x140854cb0
0097063E  E9 BE FE FF FF                  jmp 0x140970501
00970643  C7 44 24 20 60 00 00 00         mov dword ptr [rsp + 0x20], 0x60
0097064B  E9 B6 ED FF FF                  jmp 0x14096f406
00970650  41 BC 01 00 00 00               mov r12d, 1
00970656  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0097065A  8B FE                           mov edi, esi
0097065C  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
00970660  48 8B CB                        mov rcx, rbx
00970663  44 84 A3 8C 00 00 00            test byte ptr [rbx + 0x8c], r12b
0097066A  0F 85 9D 01 00 00               jne 0x14097080d
00970670  E8 CB 58 EE FF                  call 0x140855f40
00970675  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00970679  48 8B CB                        mov rcx, rbx
0097067C  44 84 A3 8C 00 00 00            test byte ptr [rbx + 0x8c], r12b
00970683  0F 85 8E 01 00 00               jne 0x140970817
00970689  E8 B2 58 EE FF                  call 0x140855f40
0097068E  33 C0                           xor eax, eax
00970690  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00970694  B8 70 03 00 00                  mov eax, 0x370
00970699  E9 7E F4 FF FF                  jmp 0x14096fb1c
0097069E  C7 44 24 20 20 04 00 00         mov dword ptr [rsp + 0x20], 0x420
009706A6  44 8B C8                        mov r9d, eax
009706A9  E9 4B F1 FF FF                  jmp 0x14096f7f9
009706AE  C7 44 24 20 F0 01 00 00         mov dword ptr [rsp + 0x20], 0x1f0
009706B6  E9 43 F8 FF FF                  jmp 0x14096fefe
009706BB  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
009706C1  C7 44 24 20 E0 02 00 00         mov dword ptr [rsp + 0x20], 0x2e0
009706C9  41 8B F9                        mov edi, r9d
009706CC  E9 E1 F5 FF FF                  jmp 0x14096fcb2
009706D1  E8 DA 45 EE FF                  call 0x140854cb0
009706D6  E9 B9 FC FF FF                  jmp 0x140970394
009706DB  3B FE                           cmp edi, esi
009706DD  0F 84 EE FE FF FF               je 0x1409705d1
009706E3  E9 F7 EC FF FF                  jmp 0x14096f3df
009706E8  8B 05 72 75 58 00               mov eax, dword ptr [rip + 0x587572]
009706EE  A8 06                           test al, 6
009706F0  0F 85 2B EF FF FF               jne 0x14096f621
009706F6  C7 44 24 20 50 02 00 00         mov dword ptr [rsp + 0x20], 0x250
009706FE  E9 EB F1 FF FF                  jmp 0x14096f8ee
00970703  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
00970707  E9 CD FE FF FF                  jmp 0x1409705d9
0097070C  C7 44 24 20 45 00 00 00         mov dword ptr [rsp + 0x20], 0x45
00970714  E9 ED EC FF FF                  jmp 0x14096f406
00970719  E8 02 C5 EE FF                  call 0x14085cc20
0097071E  E9 C0 F3 FF FF                  jmp 0x14096fae3
00970723  8B FE                           mov edi, esi
00970725  C7 44 24 20 F4 01 00 00         mov dword ptr [rsp + 0x20], 0x1f4
0097072D  44 8B CE                        mov r9d, esi
00970730  45 8B C6                        mov r8d, r14d
00970733  BA 01 00 00 00                  mov edx, 1
00970738  E9 DB EC FF FF                  jmp 0x14096f418
0097073D  E8 DE C4 EE FF                  call 0x14085cc20
00970742  E9 5C EF FF FF                  jmp 0x14096f6a3
00970747  E8 D4 C4 EE FF                  call 0x14085cc20
0097074C  E9 D1 F8 FF FF                  jmp 0x140970022
00970751  E8 CA C4 EE FF                  call 0x14085cc20
00970756  E9 E0 F8 FF FF                  jmp 0x14097003b
0097075B  E8 C0 C4 EE FF                  call 0x14085cc20
00970760  E9 AC F3 FF FF                  jmp 0x14096fb11
00970765  E8 B6 C4 EE FF                  call 0x14085cc20
0097076A  E9 F7 FA FF FF                  jmp 0x140970266
0097076F  E8 AC C4 EE FF                  call 0x14085cc20
00970774  E9 56 FD FF FF                  jmp 0x1409704cf
00970779  8B 05 E1 74 58 00               mov eax, dword ptr [rip + 0x5874e1]
0097077F  A8 06                           test al, 6
00970781  0F 85 CF F0 FF FF               jne 0x14096f856
00970787  C7 44 24 20 88 02 00 00         mov dword ptr [rsp + 0x20], 0x288
0097078F  E9 5A F1 FF FF                  jmp 0x14096f8ee
00970794  E8 87 C4 EE FF                  call 0x14085cc20
00970799  E9 F5 FC FF FF                  jmp 0x140970493
0097079E  E8 7D C4 EE FF                  call 0x14085cc20
009707A3  E9 FE FA FF FF                  jmp 0x1409702a6
009707A8  E8 73 C4 EE FF                  call 0x14085cc20
009707AD  E9 51 FE FF FF                  jmp 0x140970603
009707B2  8B 05 A8 74 58 00               mov eax, dword ptr [rip + 0x5874a8]
009707B8  A8 06                           test al, 6
009707BA  0F 85 A4 F2 FF FF               jne 0x14096fa64
009707C0  C7 44 24 20 A0 01 00 00         mov dword ptr [rsp + 0x20], 0x1a0
009707C8  E9 21 F1 FF FF                  jmp 0x14096f8ee
009707CD  8B 05 8D 74 58 00               mov eax, dword ptr [rip + 0x58748d]
009707D3  A8 06                           test al, 6
009707D5  0F 85 48 F1 FF FF               jne 0x14096f923
009707DB  C7 44 24 20 9D 00 00 00         mov dword ptr [rsp + 0x20], 0x9d
009707E3  E9 06 F1 FF FF                  jmp 0x14096f8ee
009707E8  E8 33 C4 EE FF                  call 0x14085cc20
009707ED  E9 E1 FB FF FF                  jmp 0x1409703d3
009707F2  8B 05 68 74 58 00               mov eax, dword ptr [rip + 0x587468]
009707F8  A8 06                           test al, 6
009707FA  0F 85 07 F5 FF FF               jne 0x14096fd07
00970800  C7 44 24 20 C0 00 00 00         mov dword ptr [rsp + 0x20], 0xc0
00970808  E9 E1 F0 FF FF                  jmp 0x14096f8ee
0097080D  E8 0E C4 EE FF                  call 0x14085cc20
00970812  E9 5E FE FF FF                  jmp 0x140970675
00970817  E8 04 C4 EE FF                  call 0x14085cc20
0097081C  E9 6D FE FF FF                  jmp 0x14097068e
00970821  8B 05 39 74 58 00               mov eax, dword ptr [rip + 0x587439]
00970827  A8 06                           test al, 6
00970829  0F 85 03 F7 FF FF               jne 0x14096ff32
0097082F  44 8B CE                        mov r9d, esi
00970832  C7 44 24 20 30 01 00 00         mov dword ptr [rsp + 0x20], 0x130
0097083A  45 8B C6                        mov r8d, r14d
0097083D  33 D2                           xor edx, edx
0097083F  49 8B CF                        mov rcx, r15
00970842  E8 0D E7 AF FF                  call 0x14046ef54
00970847  8B FE                           mov edi, esi
00970849  E9 D2 EB FF FF                  jmp 0x14096f420
0097084E  8B 05 0C 74 58 00               mov eax, dword ptr [rip + 0x58740c]
00970854  A8 06                           test al, 6
00970856  0F 85 54 F6 FF FF               jne 0x14096feb0
0097085C  C7 44 24 20 E4 00 00 00         mov dword ptr [rsp + 0x20], 0xe4
00970864  E9 85 F0 FF FF                  jmp 0x14096f8ee
00970869  8B 05 F1 73 58 00               mov eax, dword ptr [rip + 0x5873f1]
0097086F  A8 06                           test al, 6
00970871  0F 85 EF F7 FF FF               jne 0x140970066
00970877  C7 44 24 20 E0 01 00 00         mov dword ptr [rsp + 0x20], 0x1e0
0097087F  E9 6A F0 FF FF                  jmp 0x14096f8ee
00970884  8B 05 D6 73 58 00               mov eax, dword ptr [rip + 0x5873d6]
0097088A  A8 06                           test al, 6
0097088C  0F 85 49 F8 FF FF               jne 0x1409700db
00970892  C7 44 24 20 60 01 00 00         mov dword ptr [rsp + 0x20], 0x160
0097089A  E9 4F F0 FF FF                  jmp 0x14096f8ee
0097089F  8B 05 BB 73 58 00               mov eax, dword ptr [rip + 0x5873bb]
009708A5  A8 06                           test al, 6
009708A7  0F 85 9F F8 FF FF               jne 0x14097014c
009708AD  C7 44 24 20 72 01 00 00         mov dword ptr [rsp + 0x20], 0x172
009708B5  E9 E7 F0 FF FF                  jmp 0x14096f9a1
009708BA  8B 05 A0 73 58 00               mov eax, dword ptr [rip + 0x5873a0]
009708C0  A8 06                           test al, 6
009708C2  0F 85 0E F9 FF FF               jne 0x1409701d6
009708C8  C7 44 24 20 62 02 00 00         mov dword ptr [rsp + 0x20], 0x262
009708D0  E9 19 F0 FF FF                  jmp 0x14096f8ee
009708D5  45 39 6C 24 28                  cmp dword ptr [r12 + 0x28], r13d
009708DA  75 0B                           jne 0x1409708e7
009708DC  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
009708DF  89 4D E3                        mov dword ptr [rbp - 0x1d], ecx
009708E2  E9 E6 E9 FF FF                  jmp 0x14096f2cd
009708E7  44 88 45 7F                     mov byte ptr [rbp + 0x7f], r8b
009708EB  B9 60 02 00 00                  mov ecx, 0x260
009708F0  E9 90 F5 FF FF                  jmp 0x14096fe85
009708F5  C7 44 24 20 35 00 00 00         mov dword ptr [rsp + 0x20], 0x35
009708FD  E9 04 EB FF FF                  jmp 0x14096f406
00970902  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
0097090A  E9 F7 EA FF FF                  jmp 0x14096f406
0097090F  C7 44 24 20 50 00 00 00         mov dword ptr [rsp + 0x20], 0x50
00970917  E9 EA EA FF FF                  jmp 0x14096f406
0097091C  C7 44 24 20 9A 00 00 00         mov dword ptr [rsp + 0x20], 0x9a
00970924  E9 86 F3 FF FF                  jmp 0x14096fcaf
00970929  C7 44 24 20 9F 00 00 00         mov dword ptr [rsp + 0x20], 0x9f
00970931  E9 79 F3 FF FF                  jmp 0x14096fcaf
00970936  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
0097093C  C7 44 24 20 D0 00 00 00         mov dword ptr [rsp + 0x20], 0xd0
00970944  41 8B F9                        mov edi, r9d
00970947  E9 66 F3 FF FF                  jmp 0x14096fcb2
0097094C  84 C9                           test cl, cl
0097094E  48 8B CB                        mov rcx, rbx
00970951  0F 84 C1 84 1B 00               je 0x140b28e18
00970957  E8 C4 C2 EE FF                  call 0x14085cc20
0097095C  90                              nop
0097095D  E9 BB 84 1B 00                  jmp 0x140b28e1d
00970962  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
0097096A  E9 40 F3 FF FF                  jmp 0x14096fcaf
0097096F  C7 44 24 20 D0 01 00 00         mov dword ptr [rsp + 0x20], 0x1d0
00970977  E9 33 F3 FF FF                  jmp 0x14096fcaf
0097097C  C7 44 24 20 50 01 00 00         mov dword ptr [rsp + 0x20], 0x150
00970984  E9 26 F3 FF FF                  jmp 0x14096fcaf
00970989  C7 44 24 20 76 01 00 00         mov dword ptr [rsp + 0x20], 0x176
00970991  44 8B C8                        mov r9d, eax
00970994  BA 01 00 00 00                  mov edx, 1
00970999  E9 08 F0 FF FF                  jmp 0x14096f9a6
0097099E  C7 44 24 20 7C 01 00 00         mov dword ptr [rsp + 0x20], 0x17c
009709A6  44 8B CF                        mov r9d, edi
009709A9  E9 F6 EF FF FF                  jmp 0x14096f9a4
009709AE  C7 44 24 20 90 01 00 00         mov dword ptr [rsp + 0x20], 0x190
009709B6  EB 08                           jmp 0x1409709c0
009709B8  C7 44 24 20 68 02 00 00         mov dword ptr [rsp + 0x20], 0x268
009709C0  44 8B CF                        mov r9d, edi
009709C3  E9 EA F2 FF FF                  jmp 0x14096fcb2
009709C8  41 BD 01 00 00 00               mov r13d, 1
009709CE  48 8D 55 A7                     lea rdx, [rbp - 0x59]
009709D2  48 8B CB                        mov rcx, rbx
009709D5  44 84 AB 8C 00 00 00            test byte ptr [rbx + 0x8c], r13b
009709DC  0F 84 55 84 1B 00               je 0x140b28e37
009709E2  E8 39 C2 EE FF                  call 0x14085cc20
009709E7  90                              nop
009709E8  E9 4F 84 1B 00                  jmp 0x140b28e3c
009709ED  C7 44 24 20 40 02 00 00         mov dword ptr [rsp + 0x20], 0x240
009709F5  E9 B5 F2 FF FF                  jmp 0x14096fcaf
009709FA  C7 44 24 20 64 02 00 00         mov dword ptr [rsp + 0x20], 0x264
00970A02  E9 A8 F2 FF FF                  jmp 0x14096fcaf
00970A07  C7 44 24 20 8C 02 00 00         mov dword ptr [rsp + 0x20], 0x28c
00970A0F  E9 9B F2 FF FF                  jmp 0x14096fcaf
00970A14  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
00970A18  B8 40 03 00 00                  mov eax, 0x340
00970A1D  E9 FA F0 FF FF                  jmp 0x14096fb1c
00970A22  41 BC 01 00 00 00               mov r12d, 1
00970A28  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00970A2C  48 8B CB                        mov rcx, rbx
00970A2F  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
00970A33  44 84 A3 8C 00 00 00            test byte ptr [rbx + 0x8c], r12b
00970A3A  0F 84 0A 84 1B 00               je 0x140b28e4a
00970A40  E8 DB C1 EE FF                  call 0x14085cc20
00970A45  90                              nop
00970A46  E9 04 84 1B 00                  jmp 0x140b28e4f
00970A4B  41 BC 01 00 00 00               mov r12d, 1
00970A51  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00970A55  8B FE                           mov edi, esi
00970A57  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
00970A5B  48 8B CB                        mov rcx, rbx
00970A5E  44 84 A3 8C 00 00 00            test byte ptr [rbx + 0x8c], r12b
00970A65  0F 84 10 84 1B 00               je 0x140b28e7b
00970A6B  E8 B0 C1 EE FF                  call 0x14085cc20
00970A70  90                              nop
00970A71  E9 0A 84 1B 00                  jmp 0x140b28e80
00970A76  41 BC 01 00 00 00               mov r12d, 1
00970A7C  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00970A80  8B FE                           mov edi, esi
00970A82  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
00970A86  48 8B CB                        mov rcx, rbx
00970A89  44 84 A3 8C 00 00 00            test byte ptr [rbx + 0x8c], r12b
00970A90  0F 84 16 84 1B 00               je 0x140b28eac
00970A96  E8 85 C1 EE FF                  call 0x14085cc20
00970A9B  90                              nop
00970A9C  E9 10 84 1B 00                  jmp 0x140b28eb1
00970AA1  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00970AA7  C7 44 24 20 60 03 00 00         mov dword ptr [rsp + 0x20], 0x360
00970AAF  45 8B C6                        mov r8d, r14d
00970AB2  33 D2                           xor edx, edx
00970AB4  49 8B CF                        mov rcx, r15
00970AB7  41 8B F9                        mov edi, r9d
00970ABA  E8 95 E4 AF FF                  call 0x14046ef54
00970ABF  E9 1B E9 FF FF                  jmp 0x14096f3df
00970AC4  C7 44 24 20 00 04 00 00         mov dword ptr [rsp + 0x20], 0x400
00970ACC  E9 D5 FB FF FF                  jmp 0x1409706a6
00970AD1  B8 FF FF FF FF                  mov eax, 0xffffffff
00970AD6  E9 72 F1 FF FF                  jmp 0x14096fc4d
00970ADB  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00970AE1  C7 44 24 20 70 01 00 00         mov dword ptr [rsp + 0x20], 0x170
00970AE9  41 8B F9                        mov edi, r9d
00970AEC  E9 C1 F1 FF FF                  jmp 0x14096fcb2
00970AF1  C7 44 24 20 24 01 00 00         mov dword ptr [rsp + 0x20], 0x124
00970AF9  E9 DF 83 1B 00                  jmp 0x140b28edd
00970AFE  C7 44 24 20 20 01 00 00         mov dword ptr [rsp + 0x20], 0x120
00970B06  E9 D2 83 1B 00                  jmp 0x140b28edd
00970B0B  C7 44 24 20 1C 01 00 00         mov dword ptr [rsp + 0x20], 0x11c
00970B13  44 8B C8                        mov r9d, eax
00970B16  E9 C5 83 1B 00                  jmp 0x140b28ee0
00970B1B  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00970B21  C7 44 24 20 18 01 00 00         mov dword ptr [rsp + 0x20], 0x118
00970B29  45 8B C6                        mov r8d, r14d
00970B2C  33 D2                           xor edx, edx
00970B2E  49 8B CF                        mov rcx, r15
00970B31  41 8B F9                        mov edi, r9d
00970B34  E8 1B E4 AF FF                  call 0x14046ef54
00970B39  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00970B3D  E9 A1 E8 FF FF                  jmp 0x14096f3e3
00970B42  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
00970B48  C7 44 24 20 14 01 00 00         mov dword ptr [rsp + 0x20], 0x114
00970B50  41 8B F9                        mov edi, r9d
00970B53  E9 5A F1 FF FF                  jmp 0x14096fcb2
00970B58  C7 44 24 20 10 01 00 00         mov dword ptr [rsp + 0x20], 0x110
00970B60  E9 03 F1 FF FF                  jmp 0x14096fc68
00970B65  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00970B6D  8B C7                           mov eax, edi
00970B6F  48 81 C4 C0 00 00 00            add rsp, 0xc0
00970B76  41 5F                           pop r15
00970B78  41 5E                           pop r14
00970B7A  41 5D                           pop r13
00970B7C  41 5C                           pop r12
00970B7E  5F                              pop rdi
00970B7F  5E                              pop rsi
00970B80  5D                              pop rbp
00970B81  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCheckKey(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (192);
    v_r14 = 0;
    *(unsigned int *)(v_rsp - 71 - 37) = 0;
    *(unsigned int *)(v_rsp - 71 - 29) = 0;
    *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 17) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 65) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 81) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 33) = 0;
    *(unsigned int *)(v_rsp - 71 - 13) = 0;
    *(unsigned int *)(v_rsp - 71 - 61) = 0;
    *(unsigned int *)(v_rsp - 71 - 77) = 0;
    *(unsigned int *)(v_rsp - 71 - 85) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 240) = a3;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 248) = 0;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 256) = 0;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 264) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    }
    result = HvIsCellAllocated(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(v_rsp - 71 + 119), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0096FDBB;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F443;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_rsp - 71 - 17, a4);
loc_0096EEF1:
    a4 = 0;
    if (result == 0) goto loc_00970332;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 248) = result;
    }
    a2 = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)(a2 - 76)) > 0x410ULL) goto loc_00970301;
    if (((unsigned int)(*(unsigned __int16 *)(result + 72) + 76)) < 76) goto loc_0096F674;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0096F674;
    if (((unsigned int)(*(unsigned __int16 *)(result + 72) + 76)) > a2) goto loc_0096F674;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_0096FDE8;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 72))) > 256) goto loc_009708F5;
    if ((*(unsigned __int8 *)(result + 76)) == 0) goto loc_00970902;
loc_0096EF7C:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(result + 72)))) goto loc_0096EF93;
    if ((*(unsigned __int8 *)(0 + result * 1 + 76)) == 92) goto loc_0096F3FE;
    a2 = (unsigned int)((0) + (1));
    goto loc_0096EF7C;
loc_0096EF93:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (0x20000ULL));
    *(unsigned int *)(v_rsp - 71 - 97) = (unsigned int)(v_r13);
    if ((*(unsigned __int16 *)(result)) != ((unsigned __int16)((unsigned int)(0x6B6EULL)))) goto loc_0096F9C1;
loc_0096EFBC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 144)))) & (2)) != 0) goto loc_0096EFD7;
    if (((*(unsigned __int8 *)(result + 13)) & (3)) != 0) goto loc_0096F8C0;
loc_0096EFD7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096F746;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F461;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))), v_rsp - 71 - 65, a4);
loc_0096F009:
    *(unsigned __int64 *)(v_rsp - 71 - 1) = result + 13;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (3));
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (3));
    a1 = (((unsigned __int8)(result)) == 3) ? 1 : 0;
    result = (((unsigned __int8)(a2)) != 3) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0096F681;
loc_0096F033:
    a4 = 0;
    if (result == 0) goto loc_0096F057;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096FAB7;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 65, result, a4);
loc_0096F054:
    a4 = 0;
loc_0096F057:
loc_0096F05C:
loc_0096F062:
    *(unsigned int *)(v_rsp - 71 - 25) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    *(unsigned int *)(v_rsp - 71 - 5) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(*(unsigned __int16 *)(result + 74));
    *(unsigned int *)(v_rsp - 71 - 49) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 44)));
    if ((unsigned int)(*(unsigned __int16 *)(result + 74)) != 0) goto loc_0096F8F6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 48)))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096FE8C;
loc_0096F09E:
loc_0096F0A3:
    if ((*(unsigned int *)(v_rsp - 71 - 49)) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096FEF6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096F71A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97))) != 0) goto loc_0096F0D7;
    if ((*(unsigned __int8 *)(v_rip + 6721339)) == 0) goto loc_0096FDD5;
loc_0096F0CD:
    if ((*(unsigned __int8 *)(v_rsp - 71 + 111)) != 0) goto loc_0096FF1D;
loc_0096F0D7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096F71A;
loc_0096F0E0:
    if ((*(unsigned int *)(result + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103))))) goto loc_009700B7;
loc_0096F0EB:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F457;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)), v_rsp - 71 - 65, a4);
loc_0096F104:
    a3 = 0;
    if (result == 0) goto loc_00970ADB;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 72)))));
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(result + 72)); }
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52))))) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0097012B;
loc_0096F13A:
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57))))) goto loc_0096F96E;
loc_0096F147:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096FA39;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 65, a3, a4);
loc_0096F160:
    if (((*(unsigned __int8 *)(result + 2)) & (14)) != 0) goto loc_0096FA43;
loc_0096F16F:
    result = CmpIncrementCachedSecurityRefcount(a1, (unsigned int)(*(unsigned int *)(result + 44)), a3, a4);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_009706AE;
    a1 = 0;
    if (sign_flag) goto loc_00970723;
    if (((*(unsigned __int8 *)(result + 2)) & (64)) != 0) goto loc_0096F83B;
    if ((*(unsigned int *)(v_rsp - 71 - 25)) <= 0) goto loc_0096F669;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 - 1))) & (3));
    if (((unsigned __int8)(result)) == 1) goto loc_009701B1;
    result = HvIsCellAllocated(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 5)))), *(unsigned __int64 *)(v_rsp - 71 + 119), a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0096FE76;
    *(unsigned int *)(v_rsp - 71 - 85) = 0;
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F46B;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 5)))), v_rsp - 71 - 89, a4);
loc_0096F1F8:
    if (result == 0) goto loc_009703E5;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25))))) << (2);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_009709C8;
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)(result)) > ((unsigned int)(a1))) goto loc_009709C8;
    v_stack_mB0 = v_rsp - 71 - 29;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(result + 2)) >> (4));
    v_stack_mB8 = v_rsp - 71 - 33;
    a2 = (unsigned __int8)((a2) & (1));
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 71 + 127);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 + 119);
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)));
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
    result = CmpCheckValueList(a1, a2, result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25)))));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096FBF9;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25)))));
loc_0096F290:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0x8000002AULL) goto loc_0096F8A7;
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) == 0) goto loc_0096F65C;
loc_0096F2AC:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_0096F5D8;
loc_0096F2BA:
    a1 = 0;
loc_0096F2BC:
loc_0096F2C2:
    if ((*(unsigned int *)(result + 36)) == 0) goto loc_009708D5;
loc_0096F2CD:
    if ((*(unsigned int *)(result + 60)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 33))))) goto loc_009701BB;
loc_0096F2DB:
    if ((*(unsigned int *)(result + 64)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 29))))) goto loc_0096FBA7;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_0096F30E;
loc_0096F2F2:
    if ((*(unsigned int *)(result + 60)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 33))))) goto loc_0097020B;
loc_0096F300:
    if ((*(unsigned int *)(result + 64)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 29))))) goto loc_0096FE2D;
loc_0096F30E:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096FA2F;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 17, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25)))));
loc_0096F32C:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F44D;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))), v_rsp - 71 - 17, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25)))));
loc_0096F34A:
    a3 = 0;
    if (result == 0) goto loc_0096F80B;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 248) = result;
    }
    if (sign_flag) goto loc_0096FC56;
    if ((*(unsigned int *)(result + 20)) > 0) goto loc_0096F475;
loc_0096F377:
loc_0096F37A:
    if ((*(unsigned int *)(result + 32)) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096F899;
    if ((*(unsigned int *)(result + 24)) != 0) goto loc_0096F899;
loc_0096F39C:
    if ((*(unsigned int *)(result + 24)) < 0) goto loc_0096F7E4;
loc_0096F3A9:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87))))) >> (1));
    result = (unsigned __int8)((result) & (1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))) & (13)) != 0) {
        result = (unsigned __int8)(result);
        if (0 != 0) { result = 1; }
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)))) & (8)) != 0) goto loc_0096FC03;
loc_0096F3C7:
    if ((unsigned __int8)(result) != 0) goto loc_0096FC10;
loc_0096F3CF:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95))) & (0x8000002AULL));
loc_0096F3DA:
    if (0 == 0) goto loc_0096F420;
loc_0096F3DF:
loc_0096F3E3:
loc_0096F3EE:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096FD62;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, 1);
    goto loc_0096F420;
loc_0096F3FE:
    v_stack_mD8 = 0x500ULL;
loc_0096F406:
loc_0096F411:
loc_0096F413:
loc_0096F416:
    a2 = 0;
loc_0096F418:
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_0096F420:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096F8B6;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970B65;
loc_0096F443:
    result = HvpGetCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096EEF1;
loc_0096F44D:
    result = HvpGetCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F34A;
loc_0096F457:
    result = HvpGetCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F104;
loc_0096F461:
    result = HvpGetCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F009;
loc_0096F46B:
    result = HvpGetCellPaged(0, v_rsp - 71 - 17, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F1F8;
loc_0096F475:
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (3));
    if (((unsigned __int8)(result)) == 1) goto loc_0096FE53;
    result = HvIsCellAllocated(0, (unsigned int)(*(unsigned int *)(result + 28)), *(unsigned __int64 *)(v_rsp - 71 + 119), (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00970231;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096F710;
    result = HvpGetCellFlat(0, (unsigned int)(*(unsigned int *)(result + 28)), v_rsp - 71 - 81, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_0096F4C1:
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = result;
    if (result == 0) goto loc_009706BB;
    a4 = (unsigned int)((v_r11 - 4) - (*(unsigned int *)(result - 4)));
    if (a4 < 8) goto loc_0096FAC1;
    result = CmpGetIndexElementSize(result, (unsigned int)(*(unsigned int *)(result + 28)), v_rsp - 71 - 81, a4);
    result = (unsigned int)((result) * ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    a1 = ((unsigned int)((unsigned int)(result))) + (4);
    if (a1 < 4) goto loc_0096FAC1;
    result = CmpGetIndexElementSize(result, (unsigned int)(*(unsigned int *)(result + 28)), v_rsp - 71 - 81, a4);
    result = (unsigned int)((result) * ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    a1 = ((unsigned int)((unsigned int)(result))) + (4);
    if (a1 > ((unsigned int)(a4))) goto loc_0096FAC1;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 2)) == 0) goto loc_0096FAEF;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 256) = result;
    }
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFCFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_00970276;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) == ((unsigned __int16)((unsigned int)(0x676CULL)))) goto loc_00970276;
    if (((unsigned int)(*(unsigned __int16 *)(result + 2))) != (*(unsigned int *)(result + 20))) goto loc_00970244;
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 71 + 127);
    result = CmpCheckLeaf(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)), result, (unsigned int)(*(unsigned int *)(result + 28)));
    if (((unsigned int)(result)) == 0x8000002AULL) goto loc_0096F73D;
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_0096F82E;
loc_0096F5AC:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_00970A14;
loc_0096F5B4:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_009703FB;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, result, (unsigned int)(*(unsigned int *)(result + 28)));
loc_0096F5CD:
    a3 = 0;
    goto loc_0096F377;
loc_0096F5D8:
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 248) = result;
    }
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
loc_0096F5F3:
    v_stack_mD8 = 560;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    result = 0;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_009706F6;
    if ((*(unsigned __int8 *)(v_rip + 6719975)) == 0) goto loc_009706E8;
loc_0096F621:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_009709ED;
    *(unsigned int *)(result + 36) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    goto loc_0096F2C2;
loc_0096F65C:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_0096F2AC;
    goto loc_0096F420;
loc_0096F669:
    goto loc_0096F2BC;
loc_0096F674:
    v_stack_mD8 = 48;
    goto loc_0096F406;
loc_0096F681:
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))) == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_0096F033;
    if (((*(unsigned __int8 *)(a1 + 140)) & ((unsigned __int8)((unsigned int)((unsigned int)(result))))) != 0) goto loc_0097073D;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 65, 1, a4);
loc_0096F6A3:
    result = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((unsigned int)((unsigned int)(0xFFFFFFFFULL)) != 0) goto loc_00970413;
    if ((*(unsigned __int8 *)(v_rip + 6719812)) == 0) goto loc_00970405;
loc_0096F6C4:
    v_stack_mD8 = 152;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0097091C;
    goto loc_0096F057;
loc_0096F710:
    result = HvpGetCellPaged(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    goto loc_0096F4C1;
loc_0096F71A:
    if ((((unsigned __int8)(*(unsigned __int16 *)(result + 2))) & (80)) != 0) goto loc_0097062C;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = (unsigned __int8)((unsigned int)(0xFFFFFFFFULL));
    if ((((unsigned __int8)(*(unsigned __int16 *)(result + 2))) & (2)) != 0) goto loc_00970047;
loc_0096F734:
    goto loc_0096F16F;
loc_0096F73D:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096F5B4;
loc_0096F746:
    *(unsigned __int64 *)(v_rsp - 71 - 1) = result + 13;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (3));
    if (condition_is_equal) goto loc_0096F062;
    *(unsigned __int64 *)(v_rsp - 71 - 1) = result + 13;
    if (((unsigned __int8)(result)) == 2) goto loc_0096F062;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_00970356;
    if ((*(unsigned __int8 *)(v_rip + 6719613)) == 0) goto loc_00970348;
loc_0096F78B:
    v_stack_mD8 = 484;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0097060D;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (254));
    *(unsigned __int64 *)(v_rsp - 71 - 1) = result + 13;
    result = (unsigned __int8)((result) | (2));
    *(unsigned __int8 *)(result + 13) = (unsigned __int8)(result);
    goto loc_0096F05C;
loc_0096F7E4:
    if (0 == 0) goto loc_0096F3A9;
loc_0096F7EE:
    v_stack_mD8 = 0x410ULL;
loc_0096F7F9:
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F3DA;
loc_0096F80B:
    v_stack_mD8 = 688;
loc_0096F81F:
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)(0xC000009AULL));
    goto loc_00970B65;
loc_0096F82E:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_0096F5AC;
    goto loc_0096F3DF;
loc_0096F83B:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((unsigned int)(result + 13) != 0) goto loc_00970787;
    if ((*(unsigned __int8 *)(v_rip + 6719410)) == ((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 71 + 127)))) goto loc_00970779;
loc_0096F856:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00970A07;
    *(unsigned int *)(result + 36) = 0;
    goto loc_0096F30E;
loc_0096F899:
    goto loc_0096F39C;
loc_0096F8A7:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096F2BA;
loc_0096F8B6:
    result = HvpReleaseCellFlat(1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), 1, 1);
    goto loc_00970B65;
loc_0096F8C0:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = (unsigned __int8)(*(unsigned __int16 *)(result + 2));
    if ((unsigned int)(result + 13) != 0) goto loc_0096F8E6;
    if ((*(unsigned __int8 *)(v_rip + 6719280)) != 1) goto loc_0096FC70;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5800834)))) & (6)) != 0) goto loc_0096FC70;
loc_0096F8E6:
    v_stack_mD8 = 148;
loc_0096F8EE:
    goto loc_0096F413;
loc_0096F8F6:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) != 14) goto loc_0096FCBA;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 1) goto loc_009707DB;
    if ((*(unsigned __int8 *)(v_rip + 6719205)) == 1) goto loc_009707CD;
loc_0096F923:
    v_stack_mD8 = 155;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_00970929;
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    *(unsigned __int16 *)(result + 74) = 0;
    goto loc_0096F09E;
loc_0096F96E:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096F999;
    if ((*(unsigned __int8 *)(v_rip + 6719101)) != ((unsigned __int8)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0096FD6C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5800655)))) & (6)) != 0) goto loc_0096FD6C;
loc_0096F999:
    v_stack_mD8 = 376;
loc_0096F9A1:
loc_0096F9A4:
    a2 = 0;
loc_0096F9A6:
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F3EE;
loc_0096F9C1:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = (unsigned __int8)(*(unsigned __int16 *)(result + 2));
    if (1 != 0) goto loc_0097031C;
    if ((*(unsigned __int8 *)(v_rip + 6719019)) == ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) goto loc_0097030E;
loc_0096F9DD:
    v_stack_mD8 = 112;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 2))), 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_009702DE;
    *(unsigned __int16 *)(result) = 0x6B6EULL;
    goto loc_0096EFBC;
loc_0096FA2F:
    result = HvpReleaseCellFlat(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    goto loc_0096F32C;
loc_0096FA39:
    result = HvpReleaseCellFlat(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    goto loc_0096F160;
loc_0096FA43:
    result = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (1 != 0) goto loc_009707C0;
    if ((*(unsigned __int8 *)(v_rip + 6718884)) == 0) goto loc_009707B2;
loc_0096FA64:
    v_stack_mD8 = 384;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    if (sign_flag) goto loc_009709AE;
    goto loc_0096F16F;
loc_0096FAB7:
    result = HvpReleaseCellFlat(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    goto loc_0096F054;
loc_0096FAC1:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970719;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, a4);
loc_0096FAE3:
    result = 0;
    goto loc_0096FB20;
loc_0096FAEF:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0097075B;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, a4);
loc_0096FB11:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
loc_0096FB1C:
loc_0096FB20:
    v_stack_mD8 = 784;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (((*(unsigned int *)(v_rsp - 71 + 87)) & (0x20000ULL)) != 0) goto loc_0096F7EE;
    result = 0;
    if ((*(unsigned __int8 *)(v_rip + 6718646)) == 0) goto loc_0096FE63;
loc_0096FB52:
    v_stack_mD8 = 0x3F0ULL;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00970AC4;
    *(unsigned int *)(1 + 20) = 0;
    goto loc_0096F37A;
loc_0096FBA7:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_009702C4;
    if ((*(unsigned __int8 *)(v_rip + 6718534)) == 0) goto loc_009702B6;
loc_0096FBC2:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))), a3, a4);
    if (sign_flag) goto loc_009709B8;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 29)));
    goto loc_0096F2F2;
loc_0096FBF9:
    result = HvpReleaseCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))), a3, a4);
    goto loc_0096F290;
loc_0096FC03:
    if ((*(unsigned int *)(a1 + 220)) >= 4) goto loc_0096F3C7;
loc_0096FC10:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_0097069E;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)) + 24) = 0;
    if (((*(unsigned __int8 *)(v_rsp - 71 + 87)) & (4)) == 0) goto loc_00970AD1;
    if ((*(unsigned int *)(a1 + 220)) < 4) goto loc_00970AD1;
loc_0096FC4D:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)) + 32) = (unsigned int)((unsigned int)(0xBAADF00DULL));
    goto loc_0096F3CF;
loc_0096FC56:
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)) + 20)) == 0) goto loc_0096F377;
    v_stack_mD8 = 704;
loc_0096FC68:
    goto loc_0096F411;
loc_0096FC70:
    v_stack_mD8 = 146;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), (unsigned int)((unsigned int)(a4 + 1)), 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (!sign_flag) goto loc_009702EB;
    v_stack_mD8 = 150;
loc_0096FCAF:
loc_0096FCB2:
    goto loc_0096F416;
loc_0096FCBA:
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))) & (3));
    if (((unsigned __int8)(result)) != 1) goto loc_00970363;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    v_stack_mD8 = 158;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
loc_0096FCF0:
    result = 0;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_00970800;
    if ((*(unsigned __int8 *)(v_rip + 6718209)) == 0) goto loc_009707F2;
loc_0096FD07:
    v_stack_mD8 = 160;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_00970962;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 74) = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
loc_0096FD47:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 48) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    goto loc_0096F09E;
loc_0096FD62:
    result = HvpReleaseCellFlat(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), (unsigned int)(0xFFFFFFFFULL), a4);
    goto loc_0096F420;
loc_0096FD6C:
    v_stack_mD8 = 378;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 0, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)), a3, a4);
    if (sign_flag) goto loc_0097099E;
    *(unsigned int *)(1 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)));
    goto loc_0096F147;
loc_0096FDBB:
    v_stack_mD8 = 14;
loc_0096FDCA:
    goto loc_0096F81F;
loc_0096FDD5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5799557)))) & (6)) == 0) goto loc_0096F0D7;
    goto loc_0096F0CD;
loc_0096FDE8:
    if (0 > ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103))))) goto loc_0097070C;
    if (((1) & (0)) != 0) goto loc_0097090F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 76)) == ((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) goto loc_00970643;
    a1 = (unsigned int)((0) >> (1));
loc_0096FE11:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))))) >= ((unsigned int)(a1))) goto loc_0096EF93;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))))) * 2 + 76)) == 92) goto loc_009702D1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) + (1));
    goto loc_0096FE11;
loc_0096FE2D:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, 1, a3, a4);
    if (sign_flag) goto loc_0096F30E;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 29)));
    goto loc_0096F30E;
loc_0096FE53:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 0;
    goto loc_0096FB1C;
loc_0096FE63:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5799415)))) & (6)) == 0) goto loc_0096F7EE;
    goto loc_0096FB52;
loc_0096FE76:
loc_0096FE7B:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
loc_0096FE85:
    goto loc_0096F5F3;
loc_0096FE8C:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_0097085C;
    if ((*(unsigned __int8 *)(v_rip + 6717784)) == 0) goto loc_0097084E;
loc_0096FEB0:
    v_stack_mD8 = 232;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a4 = 0;
    if (!sign_flag) goto loc_0096FD47;
    v_stack_mD8 = 236;
    goto loc_00970730;
loc_0096FEF6:
    v_stack_mD8 = 256;
loc_0096FEFE:
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
loc_0096FF1D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97))) != 0) goto loc_0097082F;
    if ((*(unsigned __int8 *)(v_rip + 6717654)) == 0) goto loc_00970821;
loc_0096FF32:
    *(unsigned int *)(v_rsp - 71 - 49) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00970B58;
    if (((*(unsigned __int8 *)(a1 + 140)) & ((unsigned __int8)((unsigned int)((unsigned int)(result))))) == 0) goto loc_00970420;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)), v_rsp - 71 - 49, a4);
loc_0096FF64:
    if (result == 0) goto loc_00970B42;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0097042A;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + 44)), v_rsp - 71 - 89, a4);
loc_0096FF8C:
    *(unsigned __int64 *)(v_rsp - 71 + 127) = result;
    if (result == 0) goto loc_00970B1B;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    if (sign_flag) goto loc_00970B0B;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(result + 44)), a3, a4);
    if (sign_flag) goto loc_00970AFE;
    result = CmpKeySecurityIncrementReferenceCount(*(unsigned __int64 *)(v_rsp - 71 + 127), a1, (unsigned int)(*(unsigned int *)(result + 44)), 1);
    if (sign_flag) goto loc_00970AF1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 44)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970747;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, (unsigned int)(*(unsigned int *)(result + 44)), 1);
loc_00970022:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970751;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 49, (unsigned int)(*(unsigned int *)(result + 44)), 1);
loc_0097003B:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096F0E0;
loc_00970047:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((unsigned int)(a1) != 0) goto loc_00970877;
    if ((*(unsigned __int8 *)(v_rip + 6717346)) == 1) goto loc_00970869;
loc_00970066:
    v_stack_mD8 = 448;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    if (sign_flag) goto loc_0097096F;
    goto loc_0096F734;
loc_009700B7:
    v_r13 = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_00970892;
    if ((*(unsigned __int8 *)(v_rip + 6717229)) == 0) goto loc_00970884;
loc_009700DB:
    v_stack_mD8 = 320;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    if (sign_flag) goto loc_0097097C;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)));
    goto loc_0096F0EB;
loc_0097012B:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 0) goto loc_009708AD;
    if ((*(unsigned __int8 *)(v_rip + 6717116)) == 0) goto loc_0097089F;
loc_0097014C:
    v_stack_mD8 = 372;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)), a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_00970989;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 72)))));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 2)) & (32)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 72)); }
    *(unsigned __int16 *)(v_r13 + 52) = (unsigned __int16)(a1);
    goto loc_0096F13A;
loc_009701B1:
    goto loc_0096FE7B;
loc_009701BB:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 0;
    if ((*(unsigned int *)(v_rsp - 71 - 97)) != 504) goto loc_009708C8;
    if ((*(unsigned __int8 *)(v_rip + 6716978)) == 504) goto loc_009708BA;
loc_009701D6:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)), a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_009709FA;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 33)));
    goto loc_0096F2DB;
loc_0097020B:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(0, 0, a3, a4);
    if (sign_flag) goto loc_0096F300;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 33)));
    goto loc_0096F300;
loc_00970231:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096FB20;
loc_00970244:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970765;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, a4);
loc_00970266:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    goto loc_0096FB1C;
loc_00970276:
    if (0 == ((unsigned __int16)((unsigned int)(0x6972ULL)))) goto loc_00970434;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0097079E;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, a4);
loc_009702A6:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    goto loc_0096FB1C;
loc_009702B6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5798308)))) & (6)) != 0) goto loc_0096FBC2;
loc_009702C4:
    v_stack_mD8 = 614;
    goto loc_0096F8EE;
loc_009702D1:
    v_stack_mD8 = 0x510ULL;
    goto loc_0096F406;
loc_009702DE:
    v_stack_mD8 = 128;
    goto loc_0096FCAF;
loc_009702EB:
    goto loc_0096EFD7;
loc_00970301:
    v_stack_mD8 = 32;
    goto loc_0096F406;
loc_0097030E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5798220)))) & (6)) != 0) goto loc_0096F9DD;
loc_0097031C:
    v_stack_mD8 = 144;
    goto loc_0096F418;
loc_00970332:
    v_stack_mD8 = 16;
    goto loc_0096FDCA;
loc_00970348:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5798162)))) & (6)) != 0) goto loc_0096F78B;
loc_00970356:
    v_stack_mD8 = 492;
    goto loc_0096F8EE;
loc_00970363:
    result = HvIsCellAllocated(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))), *(unsigned __int64 *)(v_rsp - 71 + 119), (unsigned int)(0xC000009AULL));
    if ((unsigned __int8)(result) == 0) goto loc_0097061A;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_009706D1;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))), v_rsp - 71 - 89, (unsigned int)(0xC000009AULL));
loc_00970394:
    if (result == 0) goto loc_00970936;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 140)) & (1));
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if ((*(unsigned int *)(v_rsp - 71 - 57)) > ((unsigned int)(result))) goto loc_0097094C;
    if ((unsigned __int8)(a1) != 0) goto loc_009707E8;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 89, v_rsp - 71 - 89, (unsigned int)(0xC000009AULL));
loc_009703D3:
    a4 = 0;
    goto loc_0096F0A3;
loc_009703E5:
    v_stack_mD8 = 528;
    goto loc_0096FCB2;
loc_009703FB:
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(0xC000009AULL));
    goto loc_0096F5CD;
loc_00970405:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5797973)))) & (6)) != 0) goto loc_0096F6C4;
loc_00970413:
    v_stack_mD8 = 156;
    goto loc_0096F8EE;
loc_00970420:
    result = HvpGetCellPaged(a1, v_rsp - 71 - 89, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(0xC000009AULL));
    goto loc_0096FF64;
loc_0097042A:
    result = HvpGetCellPaged(a1, v_rsp - 71 - 89, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(0xC000009AULL));
    goto loc_0096FF8C;
loc_00970434:
    *(unsigned int *)(v_rsp - 71 - 25) = 0;
loc_0097043E:
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 2)))) goto loc_009704A3;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127) + 264) = 0;
    }
    result = HvIsCellAllocated(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 0 * 4 + 4)), *(unsigned __int64 *)(v_rsp - 71 + 119), (unsigned int)(0xC000009AULL));
    if ((unsigned __int8)(result) != 0) goto loc_009704DF;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970794;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, *(unsigned __int64 *)(v_rsp - 71 + 119), (unsigned int)(0xC000009AULL));
loc_00970493:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    goto loc_0096FB1C;
loc_009704A3:
    if ((*(unsigned int *)(*(unsigned __int8 *)(v_rsp - 71 + 127) + 20)) == 0) goto loc_0096F5B4;
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0097076F;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, *(unsigned __int64 *)(v_rsp - 71 + 119), (unsigned int)(0xC000009AULL));
loc_009704CF:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    goto loc_0096FB1C;
loc_009704DF:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00970639;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 0 * 4 + 4)), v_rsp - 71 - 41, (unsigned int)(0xC000009AULL));
loc_00970501:
    if (result == 0) goto loc_00970AA1;
    a4 = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (a4 < 8) goto loc_00970650;
    result = CmpGetIndexElementSize(result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 0 * 4 + 4)), v_rsp - 71 - 41, a4);
    result = (unsigned int)((result) * ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    a1 = ((unsigned int)((unsigned int)(result))) + (4);
    if (a1 < 4) goto loc_00970650;
    result = CmpGetIndexElementSize(result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + 0 * 4 + 4)), v_rsp - 71 - 41, a4);
    result = (unsigned int)((result) * ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    a1 = ((unsigned int)((unsigned int)(result))) + (4);
    if (a1 > ((unsigned int)(a4))) goto loc_00970650;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 2)) == 0) goto loc_00970A76;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFCFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_00970A4B;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) == ((unsigned __int16)((unsigned int)(0x676CULL)))) goto loc_00970A4B;
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 71 + 127);
    result = CmpCheckLeaf(a1, (unsigned int)(*(unsigned int *)(v_rsp - 71 + 87)), result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) * 4 + 4)));
    if (((unsigned int)(result)) == 0x8000002AULL) goto loc_00970703;
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_009706DB;
loc_009705D1:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_00970A22;
loc_009705D9:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25))) + ((unsigned int)(*(unsigned __int16 *)(result + 2))));
    *(unsigned int *)(v_rsp - 71 - 25) = (unsigned int)(v_r12);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_009707A8;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 41, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) * 4 + 4)));
loc_00970603:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57))) + 1);
    goto loc_0097043E;
loc_0097060D:
    v_stack_mD8 = 488;
    goto loc_0096FCAF;
loc_0097061A:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096FCF0;
loc_0097062C:
    v_stack_mD8 = 432;
    goto loc_0096FC68;
loc_00970639:
    result = HvpGetCellPaged(1, v_rsp - 71 - 41, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) * 4 + 4)));
    goto loc_00970501;
loc_00970643:
    v_stack_mD8 = 96;
    goto loc_0096F406;
loc_00970650:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0097080D;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 41, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) * 4 + 4)));
loc_00970675:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00970817;
    result = HvpReleaseCellPaged(a1, v_rsp - 71 - 81, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 73) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))))) * 4 + 4)));
loc_0097068E:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 73) = 0;
    goto loc_0096FB1C;
loc_0097069E:
    v_stack_mD8 = 0x420ULL;
loc_009706A6:
    goto loc_0096F7F9;
loc_009706AE:
    v_stack_mD8 = 496;
    goto loc_0096FEFE;
loc_009706BB:
    v_stack_mD8 = 736;
    goto loc_0096FCB2;
loc_009706D1:
    result = HvpGetCellPaged(a1, v_rsp - 71 - 81, result, (unsigned int)(0xC000009AULL));
    goto loc_00970394;
loc_009706DB:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) == ((unsigned int)((unsigned int)(0xC000014CULL)))) goto loc_009705D1;
    goto loc_0096F3DF;
loc_009706E8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5797234)))) & (6)) != 0) goto loc_0096F621;
loc_009706F6:
    v_stack_mD8 = 592;
    goto loc_0096F8EE;
loc_00970703:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_009705D9;
loc_0097070C:
    v_stack_mD8 = 69;
    goto loc_0096F406;
loc_00970719:
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 81, result, (unsigned int)(0xC000009AULL));
    goto loc_0096FAE3;
loc_00970723:
    v_stack_mD8 = 500;
loc_00970730:
    goto loc_0096F418;
loc_0097073D:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F6A3;
loc_00970747:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970022;
loc_00970751:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0097003B;
loc_0097075B:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096FB11;
loc_00970765:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970266;
loc_0097076F:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009704CF;
loc_00970779:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5797089)))) & (6)) != 0) goto loc_0096F856;
loc_00970787:
    v_stack_mD8 = 648;
    goto loc_0096F8EE;
loc_00970794:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970493;
loc_0097079E:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009702A6;
loc_009707A8:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970603;
loc_009707B2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5797032)))) & (6)) != 0) goto loc_0096FA64;
loc_009707C0:
    v_stack_mD8 = 416;
    goto loc_0096F8EE;
loc_009707CD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5797005)))) & (6)) != 0) goto loc_0096F923;
loc_009707DB:
    v_stack_mD8 = 157;
    goto loc_0096F8EE;
loc_009707E8:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_009703D3;
loc_009707F2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796968)))) & (6)) != 0) goto loc_0096FD07;
loc_00970800:
    v_stack_mD8 = 192;
    goto loc_0096F8EE;
loc_0097080D:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_00970675;
loc_00970817:
    result = HvpReleaseCellFlat(a1, 1, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0097068E;
loc_00970821:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796921)))) & (6)) != 0) goto loc_0096FF32;
loc_0097082F:
    v_stack_mD8 = 304;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096F420;
loc_0097084E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796876)))) & (6)) != 0) goto loc_0096FEB0;
loc_0097085C:
    v_stack_mD8 = 228;
    goto loc_0096F8EE;
loc_00970869:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796849)))) & (6)) != 0) goto loc_00970066;
loc_00970877:
    v_stack_mD8 = 480;
    goto loc_0096F8EE;
loc_00970884:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796822)))) & (6)) != 0) goto loc_009700DB;
loc_00970892:
    v_stack_mD8 = 352;
    goto loc_0096F8EE;
loc_0097089F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796795)))) & (6)) != 0) goto loc_0097014C;
loc_009708AD:
    v_stack_mD8 = 370;
    goto loc_0096F9A1;
loc_009708BA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5796768)))) & (6)) != 0) goto loc_009701D6;
loc_009708C8:
    v_stack_mD8 = 610;
    goto loc_0096F8EE;
loc_009708D5:
    if ((*(unsigned int *)(1 + 40)) != 1) goto loc_009708E7;
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 127));
    *(unsigned int *)(v_rsp - 71 - 29) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 127));
    goto loc_0096F2CD;
loc_009708E7:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 14;
    goto loc_0096FE85;
loc_009708F5:
    v_stack_mD8 = 53;
    goto loc_0096F406;
loc_00970902:
    v_stack_mD8 = 64;
    goto loc_0096F406;
loc_0097090F:
    v_stack_mD8 = 80;
    goto loc_0096F406;
loc_0097091C:
    v_stack_mD8 = 154;
    goto loc_0096FCAF;
loc_00970929:
    v_stack_mD8 = 159;
    goto loc_0096FCAF;
loc_00970936:
    v_stack_mD8 = 208;
    goto loc_0096FCB2;
loc_0097094C:
    result = HvpReleaseCellFlat(a1, a2, 14, (unsigned int)(0xC000009AULL));
loc_00970962:
    v_stack_mD8 = 176;
    goto loc_0096FCAF;
loc_0097096F:
    v_stack_mD8 = 464;
    goto loc_0096FCAF;
loc_0097097C:
    v_stack_mD8 = 336;
    goto loc_0096FCAF;
loc_00970989:
    v_stack_mD8 = 374;
    goto loc_0096F9A6;
loc_0097099E:
    v_stack_mD8 = 380;
    goto loc_0096F9A4;
loc_009709AE:
    v_stack_mD8 = 400;
    goto loc_009709C0;
loc_009709B8:
    v_stack_mD8 = 616;
loc_009709C0:
    goto loc_0096FCB2;
loc_009709C8:
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 89, 14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))));
loc_009709ED:
    v_stack_mD8 = 576;
    goto loc_0096FCAF;
loc_009709FA:
    v_stack_mD8 = 612;
    goto loc_0096FCAF;
loc_00970A07:
    v_stack_mD8 = 652;
    goto loc_0096FCAF;
loc_00970A14:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    goto loc_0096FB1C;
loc_00970A22:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 41, 14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))));
loc_00970A4B:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 41, 14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))));
loc_00970A76:
    *(unsigned __int8 *)(v_rsp - 71 + 127) = 1;
    result = HvpReleaseCellFlat(a1, v_rsp - 71 - 41, 14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))));
loc_00970AA1:
    v_stack_mD8 = 864;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)(0xC000009AULL));
    goto loc_0096F3DF;
loc_00970AC4:
    v_stack_mD8 = 0x400ULL;
    goto loc_009706A6;
loc_00970AD1:
    goto loc_0096FC4D;
loc_00970ADB:
    v_stack_mD8 = 368;
    goto loc_0096FCB2;
loc_00970AF1:
    v_stack_mD8 = 292;
loc_00970AFE:
    v_stack_mD8 = 288;
loc_00970B0B:
    v_stack_mD8 = 284;
loc_00970B1B:
    v_stack_mD8 = 280;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rsp - 71 + 127), a2, 14, (unsigned int)(0xC000009AULL));
    goto loc_0096F3E3;
loc_00970B42:
    v_stack_mD8 = 276;
    goto loc_0096FCB2;
loc_00970B58:
    v_stack_mD8 = 272;
    goto loc_0096FC68;
loc_00970B65:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))));
}
```

## 5. (Beta) C Style

```c
int64_t CmpCheckKey(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (192);
    local_r14 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x25) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x1D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x11) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x41) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x51) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0xD) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x3D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x55) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0xF0) = Arg3;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0xF8) = 0;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x100) = 0;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x108) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    }
    result = HvIsCellAllocated(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(local_rsp - 0x47 + 0x77), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0096FDBB;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F443;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_rsp - 71 - 17, Arg4);
loc_0096EEF1:
    Arg4 = 0;
    if (result == 0) goto loc_00970332;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0xF8) = result;
    }
    Arg2 = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)(Arg2 - 76)) > 0x410ULL) goto loc_00970301;
    if (((uint32_t)(*(uint16_t *)(result + 0x48) + 76)) < 76) goto loc_0096F674;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0096F674;
    if (((uint32_t)(*(uint16_t *)(result + 0x48) + 76)) > Arg2) goto loc_0096F674;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_0096FDE8;
    if (((uint16_t)(*(uint16_t *)(result + 0x48))) > 256) goto loc_009708F5;
    if ((*(uint8_t *)(result + 0x4C)) == 0) goto loc_00970902;
loc_0096EF7C:
    if (0 >= ((uint32_t)(*(uint16_t *)(result + 0x48)))) goto loc_0096EF93;
    if ((*(uint8_t *)(0 + result * 1 + 0x4C)) == 92) goto loc_0096F3FE;
    Arg2 = (uint32_t)((0) + (1));
    goto loc_0096EF7C;
loc_0096EF93:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (0x20000ULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x61) = (uint32_t)(local_r13);
    if ((*(uint16_t *)(result)) != ((uint16_t)((uint32_t)(0x6B6EULL)))) goto loc_0096F9C1;
loc_0096EFBC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x90)))) & (2)) != 0) goto loc_0096EFD7;
    if (((*(uint8_t *)(result + 0xD)) & (3)) != 0) goto loc_0096F8C0;
loc_0096EFD7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096F746;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F461;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))), local_rsp - 71 - 65, Arg4);
loc_0096F009:
    *(uint64_t *)(local_rsp - 0x47 - 0x1) = result + 13;
    Arg2 = (uint8_t)((*(uint8_t *)(result + 0xD)) & (3));
    result = (uint8_t)((*(uint8_t *)(result + 0xD)) & (3));
    Arg1 = (((uint8_t)(result)) == 3) ? 1 : 0;
    result = (((uint8_t)(Arg2)) != 3) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0096F681;
loc_0096F033:
    Arg4 = 0;
    if (result == 0) goto loc_0096F057;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096FAB7;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 65, result, Arg4);
loc_0096F054:
    Arg4 = 0;
loc_0096F057:
loc_0096F05C:
loc_0096F062:
    *(uint32_t *)(local_rsp - 0x47 - 0x19) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    *(uint32_t *)(local_rsp - 0x47 - 0x5) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(*(uint16_t *)(result + 0x4A));
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)));
    if ((uint32_t)(*(uint16_t *)(result + 0x4A)) != 0) goto loc_0096F8F6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096FE8C;
loc_0096F09E:
loc_0096F0A3:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x31)) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096FEF6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096F71A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61))) != 0) goto loc_0096F0D7;
    if ((*(uint8_t *)(v_rip + 0x668F3B)) == 0) goto loc_0096FDD5;
loc_0096F0CD:
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x6F)) != 0) goto loc_0096FF1D;
loc_0096F0D7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096F71A;
loc_0096F0E0:
    if ((*(uint32_t *)(result + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67))))) goto loc_009700B7;
loc_0096F0EB:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F457;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)), local_rsp - 71 - 65, Arg4);
loc_0096F104:
    Arg3 = 0;
    if (result == 0) goto loc_00970ADB;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x48)))));
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(result + 0x48)); }
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34))))) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0097012B;
loc_0096F13A:
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39))))) goto loc_0096F96E;
loc_0096F147:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096FA39;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 65, Arg3, Arg4);
loc_0096F160:
    if (((*(uint8_t *)(result + 0x2)) & (14)) != 0) goto loc_0096FA43;
loc_0096F16F:
    result = CmpIncrementCachedSecurityRefcount(Arg1, (uint32_t)(*(uint32_t *)(result + 0x2C)), Arg3, Arg4);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_009706AE;
    Arg1 = 0;
    if (sign_flag) goto loc_00970723;
    if (((*(uint8_t *)(result + 0x2)) & (64)) != 0) goto loc_0096F83B;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x19)) <= 0) goto loc_0096F669;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x1))) & (3));
    if (((uint8_t)(result)) == 1) goto loc_009701B1;
    result = HvIsCellAllocated(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5)))), *(uint64_t *)(local_rsp - 0x47 + 0x77), Arg4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_0096FE76;
    *(uint32_t *)(local_rsp - 0x47 - 0x55) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F46B;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5)))), local_rsp - 71 - 89, Arg4);
loc_0096F1F8:
    if (result == 0) goto loc_009703E5;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19))))) << (2);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_009709C8;
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)(result)) > ((uint32_t)(Arg1))) goto loc_009709C8;
    v_stack_mB0 = local_rsp - 71 - 29;
    Arg2 = (uint8_t)((*(uint8_t *)(result + 0x2)) >> (4));
    v_stack_mB8 = local_rsp - 71 - 33;
    Arg2 = (uint8_t)((Arg2) & (1));
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 + 0x77);
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)));
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
    result = CmpCheckValueList(Arg1, Arg2, result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19)))));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096FBF9;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19)))));
loc_0096F290:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0x8000002AULL) goto loc_0096F8A7;
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) == 0) goto loc_0096F65C;
loc_0096F2AC:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_0096F5D8;
loc_0096F2BA:
    Arg1 = 0;
loc_0096F2BC:
loc_0096F2C2:
    if ((*(uint32_t *)(result + 0x24)) == 0) goto loc_009708D5;
loc_0096F2CD:
    if ((*(uint32_t *)(result + 0x3C)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21))))) goto loc_009701BB;
loc_0096F2DB:
    if ((*(uint32_t *)(result + 0x40)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x1D))))) goto loc_0096FBA7;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_0096F30E;
loc_0096F2F2:
    if ((*(uint32_t *)(result + 0x3C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21))))) goto loc_0097020B;
loc_0096F300:
    if ((*(uint32_t *)(result + 0x40)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x1D))))) goto loc_0096FE2D;
loc_0096F30E:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096FA2F;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 17, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19)))));
loc_0096F32C:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F44D;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))), local_rsp - 71 - 17, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19)))));
loc_0096F34A:
    Arg3 = 0;
    if (result == 0) goto loc_0096F80B;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0xF8) = result;
    }
    if (sign_flag) goto loc_0096FC56;
    if ((*(uint32_t *)(result + 0x14)) > 0) goto loc_0096F475;
loc_0096F377:
loc_0096F37A:
    if ((*(uint32_t *)(result + 0x20)) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096F899;
    if ((*(uint32_t *)(result + 0x18)) != 0) goto loc_0096F899;
loc_0096F39C:
    if ((*(uint32_t *)(result + 0x18)) < 0) goto loc_0096F7E4;
loc_0096F3A9:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57))))) >> (1));
    result = (uint8_t)((result) & (1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))) & (13)) != 0) {
        result = (uint8_t)(result);
        if (0 != 0) { result = 1; }
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)))) & (8)) != 0) goto loc_0096FC03;
loc_0096F3C7:
    if ((uint8_t)(result) != 0) goto loc_0096FC10;
loc_0096F3CF:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F))) & (0x8000002AULL));
loc_0096F3DA:
    if (0 == 0) goto loc_0096F420;
loc_0096F3DF:
loc_0096F3E3:
loc_0096F3EE:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096FD62;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, 1);
    goto loc_0096F420;
loc_0096F3FE:
    v_stack_mD8 = 0x500ULL;
loc_0096F406:
loc_0096F411:
loc_0096F413:
loc_0096F416:
    Arg2 = 0;
loc_0096F418:
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_0096F420:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096F8B6;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970B65;
loc_0096F443:
    result = HvpGetCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096EEF1;
loc_0096F44D:
    result = HvpGetCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F34A;
loc_0096F457:
    result = HvpGetCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F104;
loc_0096F461:
    result = HvpGetCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F009;
loc_0096F46B:
    result = HvpGetCellPaged(0, local_rsp - 71 - 17, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F1F8;
loc_0096F475:
    result = (uint8_t)((*(uint8_t *)(result + 0xD)) & (3));
    if (((uint8_t)(result)) == 1) goto loc_0096FE53;
    result = HvIsCellAllocated(0, (uint32_t)(*(uint32_t *)(result + 0x1C)), *(uint64_t *)(local_rsp - 0x47 + 0x77), (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00970231;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096F710;
    result = HvpGetCellFlat(0, (uint32_t)(*(uint32_t *)(result + 0x1C)), local_rsp - 71 - 81, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_0096F4C1:
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = result;
    if (result == 0) goto loc_009706BB;
    Arg4 = (uint32_t)((local_r11 - 4) - (*(uint32_t *)(result - 0x4)));
    if (Arg4 < 8) goto loc_0096FAC1;
    result = CmpGetIndexElementSize(result, (uint32_t)(*(uint32_t *)(result + 0x1C)), local_rsp - 71 - 81, Arg4);
    result = (uint32_t)((result) * ((uint32_t)(*(uint16_t *)(result + 0x2))));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (4);
    if (Arg1 < 4) goto loc_0096FAC1;
    result = CmpGetIndexElementSize(result, (uint32_t)(*(uint32_t *)(result + 0x1C)), local_rsp - 71 - 81, Arg4);
    result = (uint32_t)((result) * ((uint32_t)(*(uint16_t *)(result + 0x2))));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (4);
    if (Arg1 > ((uint32_t)(Arg4))) goto loc_0096FAC1;
    if ((uint16_t)(*(uint16_t *)(result + 0x2)) == 0) goto loc_0096FAEF;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x100) = result;
    }
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(result))) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFCFFULL))) & ((uint16_t)(result))) != 0) goto loc_00970276;
    if (((uint16_t)(*(uint16_t *)(result))) == ((uint16_t)((uint32_t)(0x676CULL)))) goto loc_00970276;
    if (((uint32_t)(*(uint16_t *)(result + 0x2))) != (*(uint32_t *)(result + 0x14))) goto loc_00970244;
    v_stack_mD8 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
    result = CmpCheckLeaf(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)), result, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (((uint32_t)(result)) == 0x8000002AULL) goto loc_0096F73D;
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_0096F82E;
loc_0096F5AC:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_00970A14;
loc_0096F5B4:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_009703FB;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, result, (uint32_t)(*(uint32_t *)(result + 0x1C)));
loc_0096F5CD:
    Arg3 = 0;
    goto loc_0096F377;
loc_0096F5D8:
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0xF8) = result;
    }
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
loc_0096F5F3:
    v_stack_mD8 = 560;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    result = 0;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_009706F6;
    if ((*(uint8_t *)(v_rip + 0x6689E7)) == 0) goto loc_009706E8;
loc_0096F621:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_009709ED;
    *(uint32_t *)(result + 0x24) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    goto loc_0096F2C2;
loc_0096F65C:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_0096F2AC;
    goto loc_0096F420;
loc_0096F669:
    goto loc_0096F2BC;
loc_0096F674:
    v_stack_mD8 = 48;
    goto loc_0096F406;
loc_0096F681:
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))) == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_0096F033;
    if (((*(uint8_t *)(arg1 + 0x8C)) & ((uint8_t)((uint32_t)((uint32_t)(result))))) != 0) goto loc_0097073D;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 65, 1, Arg4);
loc_0096F6A3:
    result = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((uint32_t)((uint32_t)(0xFFFFFFFFULL)) != 0) goto loc_00970413;
    if ((*(uint8_t *)(v_rip + 0x668944)) == 0) goto loc_00970405;
loc_0096F6C4:
    v_stack_mD8 = 152;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0097091C;
    goto loc_0096F057;
loc_0096F710:
    result = HvpGetCellPaged(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    goto loc_0096F4C1;
loc_0096F71A:
    if ((((uint8_t)(*(uint16_t *)(result + 0x2))) & (80)) != 0) goto loc_0097062C;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = (uint8_t)((uint32_t)(0xFFFFFFFFULL));
    if ((((uint8_t)(*(uint16_t *)(result + 0x2))) & (2)) != 0) goto loc_00970047;
loc_0096F734:
    goto loc_0096F16F;
loc_0096F73D:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096F5B4;
loc_0096F746:
    *(uint64_t *)(local_rsp - 0x47 - 0x1) = result + 13;
    result = (uint8_t)((*(uint8_t *)(result + 0xD)) & (3));
    if (condition_is_equal) goto loc_0096F062;
    *(uint64_t *)(local_rsp - 0x47 - 0x1) = result + 13;
    if (((uint8_t)(result)) == 2) goto loc_0096F062;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_00970356;
    if ((*(uint8_t *)(v_rip + 0x66887D)) == 0) goto loc_00970348;
loc_0096F78B:
    v_stack_mD8 = 484;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0097060D;
    result = (uint8_t)((*(uint8_t *)(result + 0xD)) & (254));
    *(uint64_t *)(local_rsp - 0x47 - 0x1) = result + 13;
    result = (uint8_t)((result) | (2));
    *(uint8_t *)(result + 0xD) = (uint8_t)(result);
    goto loc_0096F05C;
loc_0096F7E4:
    if (0 == 0) goto loc_0096F3A9;
loc_0096F7EE:
    v_stack_mD8 = 0x410ULL;
loc_0096F7F9:
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F3DA;
loc_0096F80B:
    v_stack_mD8 = 688;
loc_0096F81F:
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)(0xC000009AULL));
    goto loc_00970B65;
loc_0096F82E:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_0096F5AC;
    goto loc_0096F3DF;
loc_0096F83B:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((uint32_t)(result + 13) != 0) goto loc_00970787;
    if ((*(uint8_t *)(v_rip + 0x6687B2)) == ((uint8_t)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)))) goto loc_00970779;
loc_0096F856:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00970A07;
    *(uint32_t *)(result + 0x24) = 0;
    goto loc_0096F30E;
loc_0096F899:
    goto loc_0096F39C;
loc_0096F8A7:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096F2BA;
loc_0096F8B6:
    result = HvpReleaseCellFlat(1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), 1, 1);
    goto loc_00970B65;
loc_0096F8C0:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = (uint8_t)(*(uint16_t *)(result + 0x2));
    if ((uint32_t)(result + 13) != 0) goto loc_0096F8E6;
    if ((*(uint8_t *)(v_rip + 0x668730)) != 1) goto loc_0096FC70;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x588382)))) & (6)) != 0) goto loc_0096FC70;
loc_0096F8E6:
    v_stack_mD8 = 148;
loc_0096F8EE:
    goto loc_0096F413;
loc_0096F8F6:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) != 14) goto loc_0096FCBA;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 1) goto loc_009707DB;
    if ((*(uint8_t *)(v_rip + 0x6686E5)) == 1) goto loc_009707CD;
loc_0096F923:
    v_stack_mD8 = 155;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00970929;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    *(uint16_t *)(result + 0x4A) = 0;
    goto loc_0096F09E;
loc_0096F96E:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096F999;
    if ((*(uint8_t *)(v_rip + 0x66867D)) != ((uint8_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0096FD6C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5882CF)))) & (6)) != 0) goto loc_0096FD6C;
loc_0096F999:
    v_stack_mD8 = 376;
loc_0096F9A1:
loc_0096F9A4:
    Arg2 = 0;
loc_0096F9A6:
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F3EE;
loc_0096F9C1:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = (uint8_t)(*(uint16_t *)(result + 0x2));
    if (1 != 0) goto loc_0097031C;
    if ((*(uint8_t *)(v_rip + 0x66862B)) == ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) goto loc_0097030E;
loc_0096F9DD:
    v_stack_mD8 = 112;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x2))), 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_009702DE;
    *(uint16_t *)(result) = 0x6B6EULL;
    goto loc_0096EFBC;
loc_0096FA2F:
    result = HvpReleaseCellFlat(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    goto loc_0096F32C;
loc_0096FA39:
    result = HvpReleaseCellFlat(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    goto loc_0096F160;
loc_0096FA43:
    result = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (1 != 0) goto loc_009707C0;
    if ((*(uint8_t *)(v_rip + 0x6685A4)) == 0) goto loc_009707B2;
loc_0096FA64:
    v_stack_mD8 = 384;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    if (sign_flag) goto loc_009709AE;
    goto loc_0096F16F;
loc_0096FAB7:
    result = HvpReleaseCellFlat(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    goto loc_0096F054;
loc_0096FAC1:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970719;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, Arg4);
loc_0096FAE3:
    result = 0;
    goto loc_0096FB20;
loc_0096FAEF:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0097075B;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, Arg4);
loc_0096FB11:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
loc_0096FB1C:
loc_0096FB20:
    v_stack_mD8 = 784;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (((*(uint32_t *)(local_rsp - 0x47 + 0x57)) & (0x20000ULL)) != 0) goto loc_0096F7EE;
    result = 0;
    if ((*(uint8_t *)(v_rip + 0x6684B6)) == 0) goto loc_0096FE63;
loc_0096FB52:
    v_stack_mD8 = 0x3F0ULL;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_00970AC4;
    *(uint32_t *)(1 + 0x14) = 0;
    goto loc_0096F37A;
loc_0096FBA7:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_009702C4;
    if ((*(uint8_t *)(v_rip + 0x668446)) == 0) goto loc_009702B6;
loc_0096FBC2:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))), Arg3, Arg4);
    if (sign_flag) goto loc_009709B8;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x1D)));
    goto loc_0096F2F2;
loc_0096FBF9:
    result = HvpReleaseCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))), Arg3, Arg4);
    goto loc_0096F290;
loc_0096FC03:
    if ((*(uint32_t *)(arg1 + 0xDC)) >= 4) goto loc_0096F3C7;
loc_0096FC10:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_0097069E;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)) + 0x18) = 0;
    if (((*(uint8_t *)(local_rsp - 0x47 + 0x57)) & (4)) == 0) goto loc_00970AD1;
    if ((*(uint32_t *)(arg1 + 0xDC)) < 4) goto loc_00970AD1;
loc_0096FC4D:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)) + 0x20) = (uint32_t)((uint32_t)(0xBAADF00DULL));
    goto loc_0096F3CF;
loc_0096FC56:
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)) + 0x14)) == 0) goto loc_0096F377;
    v_stack_mD8 = 704;
loc_0096FC68:
    goto loc_0096F411;
loc_0096FC70:
    v_stack_mD8 = 146;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), (uint32_t)((uint32_t)(Arg4 + 1)), 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (!sign_flag) goto loc_009702EB;
    v_stack_mD8 = 150;
loc_0096FCAF:
loc_0096FCB2:
    goto loc_0096F416;
loc_0096FCBA:
    result = (uint8_t)((*(uint8_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))) & (3));
    if (((uint8_t)(result)) != 1) goto loc_00970363;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    v_stack_mD8 = 158;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
loc_0096FCF0:
    result = 0;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_00970800;
    if ((*(uint8_t *)(v_rip + 0x668301)) == 0) goto loc_009707F2;
loc_0096FD07:
    v_stack_mD8 = 160;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00970962;
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x4A) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
loc_0096FD47:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x30) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    goto loc_0096F09E;
loc_0096FD62:
    result = HvpReleaseCellFlat(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), (uint32_t)(0xFFFFFFFFULL), Arg4);
    goto loc_0096F420;
loc_0096FD6C:
    v_stack_mD8 = 378;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 0, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)), Arg3, Arg4);
    if (sign_flag) goto loc_0097099E;
    *(uint32_t *)(1 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)));
    goto loc_0096F147;
loc_0096FDBB:
    v_stack_mD8 = 14;
loc_0096FDCA:
    goto loc_0096F81F;
loc_0096FDD5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587E85)))) & (6)) == 0) goto loc_0096F0D7;
    goto loc_0096F0CD;
loc_0096FDE8:
    if (0 > ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67))))) goto loc_0097070C;
    if (((1) & (0)) != 0) goto loc_0097090F;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x4C)) == ((uint16_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) goto loc_00970643;
    Arg1 = (uint32_t)((0) >> (1));
loc_0096FE11:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))))) >= ((uint32_t)(Arg1))) goto loc_0096EF93;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))))) * 2 + 0x4C)) == 92) goto loc_009702D1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) + (1));
    goto loc_0096FE11;
loc_0096FE2D:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, 1, Arg3, Arg4);
    if (sign_flag) goto loc_0096F30E;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x1D)));
    goto loc_0096F30E;
loc_0096FE53:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 0;
    goto loc_0096FB1C;
loc_0096FE63:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587DF7)))) & (6)) == 0) goto loc_0096F7EE;
    goto loc_0096FB52;
loc_0096FE76:
loc_0096FE7B:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
loc_0096FE85:
    goto loc_0096F5F3;
loc_0096FE8C:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_0097085C;
    if ((*(uint8_t *)(v_rip + 0x668158)) == 0) goto loc_0097084E;
loc_0096FEB0:
    v_stack_mD8 = 232;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg4 = 0;
    if (!sign_flag) goto loc_0096FD47;
    v_stack_mD8 = 236;
    goto loc_00970730;
loc_0096FEF6:
    v_stack_mD8 = 256;
loc_0096FEFE:
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
loc_0096FF1D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61))) != 0) goto loc_0097082F;
    if ((*(uint8_t *)(v_rip + 0x6680D6)) == 0) goto loc_00970821;
loc_0096FF32:
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00970B58;
    if (((*(uint8_t *)(arg1 + 0x8C)) & ((uint8_t)((uint32_t)((uint32_t)(result))))) == 0) goto loc_00970420;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)), local_rsp - 71 - 49, Arg4);
loc_0096FF64:
    if (result == 0) goto loc_00970B42;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0097042A;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + 0x2C)), local_rsp - 71 - 89, Arg4);
loc_0096FF8C:
    *(uint64_t *)(local_rsp - 0x47 + 0x7F) = result;
    if (result == 0) goto loc_00970B1B;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    if (sign_flag) goto loc_00970B0B;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(result + 0x2C)), Arg3, Arg4);
    if (sign_flag) goto loc_00970AFE;
    result = CmpKeySecurityIncrementReferenceCount(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg1, (uint32_t)(*(uint32_t *)(result + 0x2C)), 1);
    if (sign_flag) goto loc_00970AF1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970747;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, (uint32_t)(*(uint32_t *)(result + 0x2C)), 1);
loc_00970022:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970751;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 49, (uint32_t)(*(uint32_t *)(result + 0x2C)), 1);
loc_0097003B:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096F0E0;
loc_00970047:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((uint32_t)(Arg1) != 0) goto loc_00970877;
    if ((*(uint8_t *)(v_rip + 0x667FA2)) == 1) goto loc_00970869;
loc_00970066:
    v_stack_mD8 = 448;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    if (sign_flag) goto loc_0097096F;
    goto loc_0096F734;
loc_009700B7:
    local_r13 = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_00970892;
    if ((*(uint8_t *)(v_rip + 0x667F2D)) == 0) goto loc_00970884;
loc_009700DB:
    v_stack_mD8 = 320;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    if (sign_flag) goto loc_0097097C;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)));
    goto loc_0096F0EB;
loc_0097012B:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 0) goto loc_009708AD;
    if ((*(uint8_t *)(v_rip + 0x667EBC)) == 0) goto loc_0097089F;
loc_0097014C:
    v_stack_mD8 = 372;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)), Arg3, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_00970989;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x48)))));
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x2)) & (32)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x48)); }
    *(uint16_t *)(local_r13 + 0x34) = (uint16_t)(Arg1);
    goto loc_0096F13A;
loc_009701B1:
    goto loc_0096FE7B;
loc_009701BB:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 0;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x61)) != 504) goto loc_009708C8;
    if ((*(uint8_t *)(v_rip + 0x667E32)) == 504) goto loc_009708BA;
loc_009701D6:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)), Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_009709FA;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21)));
    goto loc_0096F2DB;
loc_0097020B:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(0, 0, Arg3, Arg4);
    if (sign_flag) goto loc_0096F300;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21)));
    goto loc_0096F300;
loc_00970231:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096FB20;
loc_00970244:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970765;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, Arg4);
loc_00970266:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    goto loc_0096FB1C;
loc_00970276:
    if (0 == ((uint16_t)((uint32_t)(0x6972ULL)))) goto loc_00970434;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0097079E;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, Arg4);
loc_009702A6:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    goto loc_0096FB1C;
loc_009702B6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5879A4)))) & (6)) != 0) goto loc_0096FBC2;
loc_009702C4:
    v_stack_mD8 = 614;
    goto loc_0096F8EE;
loc_009702D1:
    v_stack_mD8 = 0x510ULL;
    goto loc_0096F406;
loc_009702DE:
    v_stack_mD8 = 128;
    goto loc_0096FCAF;
loc_009702EB:
    goto loc_0096EFD7;
loc_00970301:
    v_stack_mD8 = 32;
    goto loc_0096F406;
loc_0097030E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58794C)))) & (6)) != 0) goto loc_0096F9DD;
loc_0097031C:
    v_stack_mD8 = 144;
    goto loc_0096F418;
loc_00970332:
    v_stack_mD8 = 16;
    goto loc_0096FDCA;
loc_00970348:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587912)))) & (6)) != 0) goto loc_0096F78B;
loc_00970356:
    v_stack_mD8 = 492;
    goto loc_0096F8EE;
loc_00970363:
    result = HvIsCellAllocated(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))), *(uint64_t *)(local_rsp - 0x47 + 0x77), (uint32_t)(0xC000009AULL));
    if ((uint8_t)(result) == 0) goto loc_0097061A;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_009706D1;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))), local_rsp - 71 - 89, (uint32_t)(0xC000009AULL));
loc_00970394:
    if (result == 0) goto loc_00970936;
    Arg1 = (uint8_t)((*(uint8_t *)(arg1 + 0x8C)) & (1));
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x39)) > ((uint32_t)(result))) goto loc_0097094C;
    if ((uint8_t)(Arg1) != 0) goto loc_009707E8;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 89, local_rsp - 71 - 89, (uint32_t)(0xC000009AULL));
loc_009703D3:
    Arg4 = 0;
    goto loc_0096F0A3;
loc_009703E5:
    v_stack_mD8 = 528;
    goto loc_0096FCB2;
loc_009703FB:
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(0xC000009AULL));
    goto loc_0096F5CD;
loc_00970405:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587855)))) & (6)) != 0) goto loc_0096F6C4;
loc_00970413:
    v_stack_mD8 = 156;
    goto loc_0096F8EE;
loc_00970420:
    result = HvpGetCellPaged(Arg1, local_rsp - 71 - 89, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(0xC000009AULL));
    goto loc_0096FF64;
loc_0097042A:
    result = HvpGetCellPaged(Arg1, local_rsp - 71 - 89, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(0xC000009AULL));
    goto loc_0096FF8C;
loc_00970434:
    *(uint32_t *)(local_rsp - 0x47 - 0x19) = 0;
loc_0097043E:
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    if (0 >= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x2)))) goto loc_009704A3;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) {
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F) + 0x108) = 0;
    }
    result = HvIsCellAllocated(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x0 * 4 + 0x4)), *(uint64_t *)(local_rsp - 0x47 + 0x77), (uint32_t)(0xC000009AULL));
    if ((uint8_t)(result) != 0) goto loc_009704DF;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970794;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, *(uint64_t *)(local_rsp - 0x47 + 0x77), (uint32_t)(0xC000009AULL));
loc_00970493:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    goto loc_0096FB1C;
loc_009704A3:
    if ((*(uint32_t *)(*(uint8_t *)(local_rsp - 0x47 + 0x7F) + 0x14)) == 0) goto loc_0096F5B4;
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0097076F;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, *(uint64_t *)(local_rsp - 0x47 + 0x77), (uint32_t)(0xC000009AULL));
loc_009704CF:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    goto loc_0096FB1C;
loc_009704DF:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00970639;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x0 * 4 + 0x4)), local_rsp - 71 - 41, (uint32_t)(0xC000009AULL));
loc_00970501:
    if (result == 0) goto loc_00970AA1;
    Arg4 = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (Arg4 < 8) goto loc_00970650;
    result = CmpGetIndexElementSize(result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x0 * 4 + 0x4)), local_rsp - 71 - 41, Arg4);
    result = (uint32_t)((result) * ((uint32_t)(*(uint16_t *)(result + 0x2))));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (4);
    if (Arg1 < 4) goto loc_00970650;
    result = CmpGetIndexElementSize(result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + 0x0 * 4 + 0x4)), local_rsp - 71 - 41, Arg4);
    result = (uint32_t)((result) * ((uint32_t)(*(uint16_t *)(result + 0x2))));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (4);
    if (Arg1 > ((uint32_t)(Arg4))) goto loc_00970650;
    if ((uint16_t)(*(uint16_t *)(result + 0x2)) == 0) goto loc_00970A76;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(result))) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFCFFULL))) & ((uint16_t)(result))) != 0) goto loc_00970A4B;
    if (((uint16_t)(*(uint16_t *)(result))) == ((uint16_t)((uint32_t)(0x676CULL)))) goto loc_00970A4B;
    v_stack_mD8 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
    result = CmpCheckLeaf(Arg1, (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x57)), result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) * 4 + 0x4)));
    if (((uint32_t)(result)) == 0x8000002AULL) goto loc_00970703;
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_009706DB;
loc_009705D1:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_00970A22;
loc_009705D9:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19))) + ((uint32_t)(*(uint16_t *)(result + 0x2))));
    *(uint32_t *)(local_rsp - 0x47 - 0x19) = (uint32_t)(local_r12);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_009707A8;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 41, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) * 4 + 0x4)));
loc_00970603:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39))) + 1);
    goto loc_0097043E;
loc_0097060D:
    v_stack_mD8 = 488;
    goto loc_0096FCAF;
loc_0097061A:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096FCF0;
loc_0097062C:
    v_stack_mD8 = 432;
    goto loc_0096FC68;
loc_00970639:
    result = HvpGetCellPaged(1, local_rsp - 71 - 41, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) * 4 + 0x4)));
    goto loc_00970501;
loc_00970643:
    v_stack_mD8 = 96;
    goto loc_0096F406;
loc_00970650:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0097080D;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 41, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) * 4 + 0x4)));
loc_00970675:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_00970817;
    result = HvpReleaseCellPaged(Arg1, local_rsp - 71 - 81, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x49) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))))) * 4 + 0x4)));
loc_0097068E:
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x49) = 0;
    goto loc_0096FB1C;
loc_0097069E:
    v_stack_mD8 = 0x420ULL;
loc_009706A6:
    goto loc_0096F7F9;
loc_009706AE:
    v_stack_mD8 = 496;
    goto loc_0096FEFE;
loc_009706BB:
    v_stack_mD8 = 736;
    goto loc_0096FCB2;
loc_009706D1:
    result = HvpGetCellPaged(Arg1, local_rsp - 71 - 81, result, (uint32_t)(0xC000009AULL));
    goto loc_00970394;
loc_009706DB:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) == ((uint32_t)((uint32_t)(0xC000014CULL)))) goto loc_009705D1;
    goto loc_0096F3DF;
loc_009706E8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587572)))) & (6)) != 0) goto loc_0096F621;
loc_009706F6:
    v_stack_mD8 = 592;
    goto loc_0096F8EE;
loc_00970703:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_009705D9;
loc_0097070C:
    v_stack_mD8 = 69;
    goto loc_0096F406;
loc_00970719:
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 81, result, (uint32_t)(0xC000009AULL));
    goto loc_0096FAE3;
loc_00970723:
    v_stack_mD8 = 500;
loc_00970730:
    goto loc_0096F418;
loc_0097073D:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F6A3;
loc_00970747:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970022;
loc_00970751:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0097003B;
loc_0097075B:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096FB11;
loc_00970765:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970266;
loc_0097076F:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009704CF;
loc_00970779:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5874E1)))) & (6)) != 0) goto loc_0096F856;
loc_00970787:
    v_stack_mD8 = 648;
    goto loc_0096F8EE;
loc_00970794:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970493;
loc_0097079E:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009702A6;
loc_009707A8:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970603;
loc_009707B2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5874A8)))) & (6)) != 0) goto loc_0096FA64;
loc_009707C0:
    v_stack_mD8 = 416;
    goto loc_0096F8EE;
loc_009707CD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58748D)))) & (6)) != 0) goto loc_0096F923;
loc_009707DB:
    v_stack_mD8 = 157;
    goto loc_0096F8EE;
loc_009707E8:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_009703D3;
loc_009707F2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587468)))) & (6)) != 0) goto loc_0096FD07;
loc_00970800:
    v_stack_mD8 = 192;
    goto loc_0096F8EE;
loc_0097080D:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_00970675;
loc_00970817:
    result = HvpReleaseCellFlat(Arg1, 1, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0097068E;
loc_00970821:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x587439)))) & (6)) != 0) goto loc_0096FF32;
loc_0097082F:
    v_stack_mD8 = 304;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096F420;
loc_0097084E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x58740C)))) & (6)) != 0) goto loc_0096FEB0;
loc_0097085C:
    v_stack_mD8 = 228;
    goto loc_0096F8EE;
loc_00970869:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5873F1)))) & (6)) != 0) goto loc_00970066;
loc_00970877:
    v_stack_mD8 = 480;
    goto loc_0096F8EE;
loc_00970884:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5873D6)))) & (6)) != 0) goto loc_009700DB;
loc_00970892:
    v_stack_mD8 = 352;
    goto loc_0096F8EE;
loc_0097089F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5873BB)))) & (6)) != 0) goto loc_0097014C;
loc_009708AD:
    v_stack_mD8 = 370;
    goto loc_0096F9A1;
loc_009708BA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5873A0)))) & (6)) != 0) goto loc_009701D6;
loc_009708C8:
    v_stack_mD8 = 610;
    goto loc_0096F8EE;
loc_009708D5:
    if ((*(uint32_t *)(1 + 0x28)) != 1) goto loc_009708E7;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x7F));
    *(uint32_t *)(local_rsp - 0x47 - 0x1D) = (uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x7F));
    goto loc_0096F2CD;
loc_009708E7:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 14;
    goto loc_0096FE85;
loc_009708F5:
    v_stack_mD8 = 53;
    goto loc_0096F406;
loc_00970902:
    v_stack_mD8 = 64;
    goto loc_0096F406;
loc_0097090F:
    v_stack_mD8 = 80;
    goto loc_0096F406;
loc_0097091C:
    v_stack_mD8 = 154;
    goto loc_0096FCAF;
loc_00970929:
    v_stack_mD8 = 159;
    goto loc_0096FCAF;
loc_00970936:
    v_stack_mD8 = 208;
    goto loc_0096FCB2;
loc_0097094C:
    result = HvpReleaseCellFlat(Arg1, Arg2, 14, (uint32_t)(0xC000009AULL));
loc_00970962:
    v_stack_mD8 = 176;
    goto loc_0096FCAF;
loc_0097096F:
    v_stack_mD8 = 464;
    goto loc_0096FCAF;
loc_0097097C:
    v_stack_mD8 = 336;
    goto loc_0096FCAF;
loc_00970989:
    v_stack_mD8 = 374;
    goto loc_0096F9A6;
loc_0097099E:
    v_stack_mD8 = 380;
    goto loc_0096F9A4;
loc_009709AE:
    v_stack_mD8 = 400;
    goto loc_009709C0;
loc_009709B8:
    v_stack_mD8 = 616;
loc_009709C0:
    goto loc_0096FCB2;
loc_009709C8:
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 89, 14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))));
loc_009709ED:
    v_stack_mD8 = 576;
    goto loc_0096FCAF;
loc_009709FA:
    v_stack_mD8 = 612;
    goto loc_0096FCAF;
loc_00970A07:
    v_stack_mD8 = 652;
    goto loc_0096FCAF;
loc_00970A14:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    goto loc_0096FB1C;
loc_00970A22:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 41, 14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))));
loc_00970A4B:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 41, 14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))));
loc_00970A76:
    *(uint8_t *)(local_rsp - 0x47 + 0x7F) = 1;
    result = HvpReleaseCellFlat(Arg1, local_rsp - 71 - 41, 14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))));
loc_00970AA1:
    v_stack_mD8 = 864;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)(0xC000009AULL));
    goto loc_0096F3DF;
loc_00970AC4:
    v_stack_mD8 = 0x400ULL;
    goto loc_009706A6;
loc_00970AD1:
    goto loc_0096FC4D;
loc_00970ADB:
    v_stack_mD8 = 368;
    goto loc_0096FCB2;
loc_00970AF1:
    v_stack_mD8 = 292;
loc_00970AFE:
    v_stack_mD8 = 288;
loc_00970B0B:
    v_stack_mD8 = 284;
loc_00970B1B:
    v_stack_mD8 = 280;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(local_rsp - 0x47 + 0x7F), Arg2, 14, (uint32_t)(0xC000009AULL));
    goto loc_0096F3E3;
loc_00970B42:
    v_stack_mD8 = 276;
    goto loc_0096FCB2;
loc_00970B58:
    v_stack_mD8 = 272;
    goto loc_0096FC68;
loc_00970B65:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0xDC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096EE2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
