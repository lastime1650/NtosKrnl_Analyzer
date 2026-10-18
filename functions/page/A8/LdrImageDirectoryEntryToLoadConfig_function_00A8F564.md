# LdrImageDirectoryEntryToLoadConfig

- RVA: `0x00A8F564`–`0x00A8F573` (길이 `15` bytes)
- VA: `0x0000000140A8F564`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8F568` → [LdrImageDirectoryEntryToLoadConfigEx](../../text/4F/LdrImageDirectoryEntryToLoadConfigEx_function_004F087C.md) (function, `0x004F087C`)

### Direct callers
- [RtlGuardCheckExceptionHandler](../../text/2F/RtlGuardCheckExceptionHandler_function_002F2038.md) at `0x002F2096`
- [RtlGetImageBaseAndLoadConfig](../../text/46/RtlGetImageBaseAndLoadConfig_function_0046C3A4.md) at `0x0046C40D`
- [RtlIsImageFullyRetpolined](../../text/4C/RtlIsImageFullyRetpolined_function_004CDE74.md) at `0x004CDE78`
- [RtlpCaptureDynamicRelocationTableRva](../../text/5E/RtlpCaptureDynamicRelocationTableRva_function_005EC760.md) at `0x005EC787`
- [RtlGuardCheckLongJumpTarget](../../text/5E/RtlGuardCheckLongJumpTarget_function_005EEF28.md) at `0x005EEF6A`
- [RtlpCaptureRetpolineBinaryInfoForImage](../../text/6A/RtlpCaptureRetpolineBinaryInfoForImage_function_006AA060.md) at `0x006AA0A6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A8F568` → [LdrImageDirectoryEntryToLoadConfigEx](../../text/4F/LdrImageDirectoryEntryToLoadConfigEx_function_004F087C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8F564  48 83 EC 28                     sub rsp, 0x28
00A8F568  E8 0F 13 A6 FF                  call 0x1404f087c
00A8F56D  48 83 C4 28                     add rsp, 0x28
00A8F571  C3                              ret
00A8F572  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrImageDirectoryEntryToLoadConfig(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = LdrImageDirectoryEntryToLoadConfigEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void LdrImageDirectoryEntryToLoadConfig(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = LdrImageDirectoryEntryToLoadConfigEx(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8F564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8F564[BB_00A8F564]
  bb_00A8F572[BB_00A8F572]
```
