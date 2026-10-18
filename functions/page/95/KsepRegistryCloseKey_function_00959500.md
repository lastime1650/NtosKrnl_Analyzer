# KsepRegistryCloseKey

- RVA: `0x00959500`–`0x0095951D` (길이 `29` bytes)
- VA: `0x0000000140959500`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0095950F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [KseSetDeviceFlags](../74/KseSetDeviceFlags_function_00748B20.md) at `0x00748BD0`
- [KseSetDeviceFlags](../74/KseSetDeviceFlags_function_00748B20.md) at `0x00748C48`
- [KsepDbQueryRegistryDeviceDataList](../74/KsepDbQueryRegistryDeviceDataList_function_007490B4.md) at `0x007491F9`
- [KsepRegistryQueryDriverShims](KsepRegistryQueryDriverShims_function_00959524.md) at `0x009595BA`
- [KsepDbQueryRegistryDeviceData](KsepDbQueryRegistryDeviceData_function_0095B174.md) at `0x0095B25A`
- [KsepMatchInitBiosInfo](../../init/C3/KsepMatchInitBiosInfo_function_00C3BCB0.md) at `0x00C3BEC9`
- [KsepEngineReadFlags](../../init/C3/KsepEngineReadFlags_function_00C3C310.md) at `0x00C3C451`
- [KsepEngineReadFlags](../../init/C3/KsepEngineReadFlags_function_00C3C310.md) at `0x00C3C630`

### Static image references
- `0x00959514` → RVA `0x00F1017C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0095950F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00959500  48 83 EC 28                     sub rsp, 0x28
00959504  48 85 C9                        test rcx, rcx
00959507  75 06                           jne 0x14095950f
00959509  48 83 C4 28                     add rsp, 0x28
0095950D  C3                              ret
0095950E  CC                              int3
0095950F  E8 9C 3D D5 FF                  call 0x1406ad2b0
00959514  F0 FF 05 61 6C 5B 00            lock inc dword ptr [rip + 0x5b6c61]
0095951B  EB EC                           jmp 0x140959509
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepRegistryCloseKey(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_0095950F;
loc_00959509:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0095950F:
    result = ZwClose(a1, a2, a3, a4);
    goto loc_00959509;
}
```

## 5. (Beta) C Style

```c
int64_t KsepRegistryCloseKey(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_0095950F;
loc_00959509:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0095950F:
    result = ZwClose(Arg1, a2, a3, a4);
    goto loc_00959509;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00959500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00959500[BB_00959500]
  bb_00959509[BB_00959509]
  bb_0095950E[BB_0095950E]
  bb_0095950F[BB_0095950F]
  bb_00959500 -->|branch| bb_0095950F
  bb_00959500 -->|fallthrough| bb_00959509
  bb_0095950E -->|flow| bb_0095950F
  bb_0095950F -->|branch| bb_00959509
```
